import streamlit as st
from steganography import SteganoExfil
from config import Settings
import os
import io
import json
from pathlib import Path
import mimetypes

class SteganoApp:
    def __init__(self):
        self.stego = SteganoExfil()
        self.settings = Settings()
        self.setup_page()
        
    def setup_page(self):
        """Initialize page configuration and theme"""
        theme = st.sidebar.selectbox(
            "Theme",
            ["Light", "Dark"],
            key="theme",
            on_change=self.handle_theme_change
        )
        
        st.set_page_config(
            page_title="Steganography Tool",
            page_icon="🕵️‍♂️",
            layout="wide",
            initial_sidebar_state="expanded"
        )
            
    def handle_theme_change(self):
        """Handle theme change and save settings"""
        self.settings.set("theme", st.session_state.theme)

    def validate_file_size(self, file):
        """Validate file size against maximum limit"""
        max_size = self.settings.get("max_file_size_mb", 10)
        if file.size > max_size * 1024 * 1024:
            return False, f"File too large (max {max_size}MB)"
        return True, ""

    def estimate_capacity(self, carrier_file, method):
        """Estimate storage capacity for carrier image"""
        if not carrier_file:
            return 0
            
        temp_carrier = f"temp_carrier{Path(carrier_file.name).suffix}"
        with open(temp_carrier, "wb") as f:
            f.write(carrier_file.read())
            
        try:
            carrier = self.stego._prepare_carrier_image(temp_carrier)
            if method == 'dct':
                capacity = self.stego._calculate_dct_capacity(carrier)
                return capacity // 8
            else:
                return carrier.size * 3 // 8
        finally:
            if os.path.exists(temp_carrier):
                os.remove(temp_carrier)

    def preview_text_file(self, file):
        """Preview text file contents"""
        try:
            content = file.read().decode('utf-8')
            with st.expander("File Preview"):
                st.text_area("Content", content, height=200)
            file.seek(0)
            return True
        except UnicodeDecodeError:
            return False

    def process_multiple_files(self, carrier_file, secret_files, method, password, quality):
        """Process multiple files for hiding"""
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, secret_file in enumerate(secret_files):
            progress = (i + 1) / len(secret_files)
            status_text.text(f"Processing {secret_file.name}...")
            
            output_name = f"stego_{i}_{Path(carrier_file.name).stem}.png"
            
            try:
                secret_data = secret_file.read()
                self.process_single_file(
                    carrier_file, 
                    secret_data, 
                    output_name, 
                    method, 
                    password, 
                    quality
                )
                progress_bar.progress(progress)
                
            except Exception as e:
                st.error(f"Error processing {secret_file.name}: {str(e)}")
                continue
                
        status_text.text("Processing complete!")
        progress_bar.progress(1.0)

    def process_single_file(self, carrier_file, secret_data, output_name, method, password, quality):
        """Process a single file for hiding"""
        temp_carrier = f"temp_carrier{Path(carrier_file.name).suffix}"
        with open(temp_carrier, "wb") as f:
            carrier_file.seek(0)
            f.write(carrier_file.read())
        
        try:
            self.stego.hide_data(
                data=secret_data,
                carrier_image_path=temp_carrier,
                output_path=output_name,
                password=password,
                method=method,
                quality=quality
            )
            
            with open(output_name, "rb") as f:
                st.download_button(
                    label=f"Download {output_name}",
                    data=f.read(),
                    file_name=output_name,
                    mime="image/png"
                )
                
        finally:
            if os.path.exists(temp_carrier):
                os.remove(temp_carrier)
            if os.path.exists(output_name):
                os.remove(output_name)

    def render_hide_tab(self):
        """Render the hide data tab"""
        st.header("Hide Secret Data")
        
        carrier_file = st.file_uploader(
            "Drop or choose carrier image",
            type=self.settings.get("supported_formats"),
            key="hide_carrier",
            help="Drag and drop supported!"
        )
        
        secret_files = st.file_uploader(
            "Drop or choose files to hide",
            accept_multiple_files=True,
            key="secret_files",
            help="Multiple files supported!"
        )

        if carrier_file:
            valid, error = self.validate_file_size(carrier_file)
            if not valid:
                st.error(error)
                return
                
            col1, col2 = st.columns(2)
            with col1:
                st.image(carrier_file, caption="Carrier Image")
            with col2:
                method = st.radio(
                    "Steganography Method",
                    options=['dct', 'lsb'],
                    help="DCT is more secure but slower"
                )
                
                capacity = self.estimate_capacity(carrier_file, method)
                st.info(f"""
                **Carrier Details:**
                - Size: {round(carrier_file.size/1024, 2)} KB
                - Format: {carrier_file.type}
                - Estimated Capacity: {round(capacity/1024, 2)} KB
                """)

        if secret_files:
            with st.expander("File Previews", expanded=True):
                for file in secret_files:
                    st.write(f"**{file.name}**")
                    if file.type.startswith('text/'):
                        self.preview_text_file(file)
                    st.write(f"Size: {round(file.size/1024, 2)} KB")
                    st.divider()

        with st.expander("Advanced Settings"):
            password = st.text_input(
                "Password",
                type="password",
                help="Used to encrypt data"
            )
            
            quality = st.slider(
                "Image Quality",
                min_value=0.1,
                max_value=1.0,
                value=self.settings.get("default_quality", 0.8),
                help="Higher quality = less capacity"
            )

        if st.button(
            "Hide Data",
            type="primary",
            disabled=not (carrier_file and secret_files and password)
        ):
            self.process_multiple_files(
                carrier_file,
                secret_files,
                method,
                password,
                quality
            )

    def render_extract_tab(self):
        """Render the extract data tab"""
        st.header("Extract Hidden Data")
        
        stego_file = st.file_uploader(
            "Drop or choose stego image",
            type=self.settings.get("supported_formats"),
            key="extract_stego"
        )

        if stego_file:
            st.image(stego_file, caption="Stego Image")
            
            col1, col2 = st.columns(2)
            with col1:
                method = st.radio(
                    "Extraction Method",
                    options=['dct', 'lsb'],
                    key="extract_method"
                )
            with col2:
                password = st.text_input(
                    "Password",
                    type="password",
                    key="extract_password"
                )

            if st.button("Extract Data", type="primary"):
                try:
                    with st.spinner("Extracting data..."):
                        temp_stego = f"temp_stego{Path(stego_file.name).suffix}"
                        with open(temp_stego, "wb") as f:
                            f.write(stego_file.read())
                        
                        extracted_data = self.stego.extract_data(
                            stego_image_path=temp_stego,
                            password=password,
                            method=method
                        )
                        
                        if os.path.exists(temp_stego):
                            os.remove(temp_stego)
                        
                        file_type = mimetypes.guess_type("extracted_data")[0]
                        if not file_type:
                            file_type = "application/octet-stream"
                        
                        st.success("Data extracted successfully!")
                        st.download_button(
                            "Download Extracted Data",
                            data=extracted_data,
                            file_name="extracted_data",
                            mime=file_type
                        )

                except Exception as e:
                    st.error(f"Error: {str(e)}")

    def render_settings_tab(self):
        """Render the settings tab"""
        st.header("Settings")
        
        st.subheader("General")
        max_file_size = st.number_input(
            "Maximum file size (MB)",
            min_value=1,
            max_value=100,
            value=self.settings.get("max_file_size_mb", 10)
        )
        self.settings.set("max_file_size_mb", max_file_size)
        
        st.subheader("Defaults")
        default_method = st.selectbox(
            "Default steganography method",
            options=['dct', 'lsb'],
            index=0 if self.settings.get("default_method") == 'dct' else 1
        )
        self.settings.set("default_method", default_method)
        
        default_quality = st.slider(
            "Default image quality",
            min_value=0.1,
            max_value=1.0,
            value=self.settings.get("default_quality", 0.8)
        )
        self.settings.set("default_quality", default_quality)
        
        if st.button("Save Settings"):
            self.settings.save()
            st.success("Settings saved!")

    def run(self):
        """Run the Streamlit app"""
        st.title("🕵️‍♂️ Steganography Tool")
        
        tab1, tab2, tab3 = st.tabs(["Hide Data", "Extract Data", "Settings"])
        
        with tab1:
            self.render_hide_tab()
        with tab2:
            self.render_extract_tab()
        with tab3:
            self.render_settings_tab()
        
        st.markdown("---")
        st.markdown("""
            <div style='text-align: center'>
                <p>Made with ❤️ using Streamlit</p>
                <p>Use responsibly • Data is processed locally</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    app = SteganoApp()
    app.run() 