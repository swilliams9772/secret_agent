import streamlit as st

class HelpSidebar:
    def __init__(self):
        self.method_info = {
            "dct": {
                "name": "Discrete Cosine Transform (DCT)",
                "security": "★★★★★",
                "capacity": "★★★",
                "speed": "★★★",
                "description": """
                Embeds data in frequency domain coefficients.
                - Higher resistance to statistical analysis
                - Better preservation of image quality
                - Survives JPEG compression
                - Ideal for watermarking and sensitive data
                """
            },
            "lsb": {
                "name": "Least Significant Bit (LSB)",
                "security": "★★★",
                "capacity": "★★★★★",
                "speed": "★★★★★",
                "description": """
                Modifies least significant bits of pixel values.
                - Higher storage capacity
                - Faster processing speed
                - Perfect reconstruction
                - Best for uncompressed formats
                """
            }
        }
        
    def render(self):
        """Render help sidebar"""
        st.sidebar.title("ℹ️ Help & Information")
        
        with st.sidebar.expander("Steganography Methods"):
            for method, info in self.method_info.items():
                st.write(f"### {info['name']}")
                st.write(f"**Security:** {info['security']}")
                st.write(f"**Capacity:** {info['capacity']}")
                st.write(f"**Speed:** {info['speed']}")
                st.write(info['description'])
                st.write("---")
        
        with st.sidebar.expander("Security Tips"):
            st.write("""
            - Use strong passwords (12+ chars)
            - Mix uppercase, lowercase, numbers, symbols
            - Avoid dictionary words
            - Use unique passwords
            - Process data locally
            - Clear temporary files
            """)
        
        with st.sidebar.expander("File Guidelines"):
            st.write("""
            **Supported Formats:**
            - PNG (recommended)
            - JPEG/JPG
            - BMP
            
            **Best Practices:**
            - Use uncompressed formats
            - Verify file integrity
            - Check carrier capacity
            - Monitor file sizes
            """) 