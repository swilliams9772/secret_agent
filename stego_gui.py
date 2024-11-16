import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from steganography import SteganoExfil
import os
from PIL import Image, ImageTk
import threading

class SteganographyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Steganography Tool")
        self.window.geometry("800x600")
        self.stego = SteganoExfil()
        
        # Style configuration
        style = ttk.Style()
        style.configure('TButton', padding=5)
        style.configure('TLabel', padding=5)
        
        self._create_widgets()
        self._create_layout()
        
    def _create_widgets(self):
        """Create all GUI widgets"""
        # Mode selection
        self.mode_var = tk.StringVar(value="hide")
        self.mode_frame = ttk.LabelFrame(self.window, text="Mode")
        self.hide_radio = ttk.Radiobutton(self.mode_frame, text="Hide Data", 
                                         variable=self.mode_var, value="hide",
                                         command=self._update_mode)
        self.extract_radio = ttk.Radiobutton(self.mode_frame, text="Extract Data", 
                                           variable=self.mode_var, value="extract",
                                           command=self._update_mode)
        
        # Method selection
        self.method_var = tk.StringVar(value="dct")
        self.method_frame = ttk.LabelFrame(self.window, text="Method")
        self.dct_radio = ttk.Radiobutton(self.method_frame, text="DCT", 
                                        variable=self.method_var, value="dct")
        self.lsb_radio = ttk.Radiobutton(self.method_frame, text="LSB", 
                                        variable=self.method_var, value="lsb")
        
        # File selection
        self.file_frame = ttk.LabelFrame(self.window, text="Files")
        self.carrier_btn = ttk.Button(self.file_frame, text="Select Carrier Image",
                                    command=self._select_carrier)
        self.carrier_label = ttk.Label(self.file_frame, text="No image selected")
        
        # Image preview
        self.preview_frame = ttk.LabelFrame(self.window, text="Image Preview")
        self.preview_label = ttk.Label(self.preview_frame)
        
        # Data input
        self.data_frame = ttk.LabelFrame(self.window, text="Data")
        self.data_btn = ttk.Button(self.data_frame, text="Select Data File",
                                 command=self._select_data)
        self.data_label = ttk.Label(self.data_frame, text="No data file selected")
        
        # Password
        self.password_frame = ttk.LabelFrame(self.window, text="Password")
        self.password_entry = ttk.Entry(self.password_frame, show="*")
        
        # Quality control
        self.quality_frame = ttk.LabelFrame(self.window, text="Image Quality")
        self.quality_scale = ttk.Scale(self.quality_frame, from_=0.1, to=1.0,
                                     orient=tk.HORIZONTAL)
        self.quality_scale.set(0.8)
        
        # Progress
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(self.window, variable=self.progress_var,
                                      maximum=100)
        
        # Execute button
        self.execute_btn = ttk.Button(self.window, text="Execute",
                                    command=self._execute_operation)
        
        # Status
        self.status_label = ttk.Label(self.window, text="Ready")
        
    def _create_layout(self):
        """Arrange widgets in the window"""
        # Mode selection
        self.mode_frame.pack(fill=tk.X, padx=5, pady=5)
        self.hide_radio.pack(side=tk.LEFT, padx=5)
        self.extract_radio.pack(side=tk.LEFT, padx=5)
        
        # Method selection
        self.method_frame.pack(fill=tk.X, padx=5, pady=5)
        self.dct_radio.pack(side=tk.LEFT, padx=5)
        self.lsb_radio.pack(side=tk.LEFT, padx=5)
        
        # File selection
        self.file_frame.pack(fill=tk.X, padx=5, pady=5)
        self.carrier_btn.pack(side=tk.LEFT, padx=5)
        self.carrier_label.pack(side=tk.LEFT, padx=5)
        
        # Image preview
        self.preview_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.preview_label.pack(fill=tk.BOTH, expand=True)
        
        # Data input
        self.data_frame.pack(fill=tk.X, padx=5, pady=5)
        self.data_btn.pack(side=tk.LEFT, padx=5)
        self.data_label.pack(side=tk.LEFT, padx=5)
        
        # Password
        self.password_frame.pack(fill=tk.X, padx=5, pady=5)
        self.password_entry.pack(fill=tk.X, padx=5, pady=5)
        
        # Quality control
        self.quality_frame.pack(fill=tk.X, padx=5, pady=5)
        self.quality_scale.pack(fill=tk.X, padx=5, pady=5)
        
        # Progress and status
        self.progress.pack(fill=tk.X, padx=5, pady=5)
        self.status_label.pack(fill=tk.X, padx=5)
        
        # Execute button
        self.execute_btn.pack(pady=10)
        
    def _update_mode(self):
        """Update UI based on selected mode"""
        mode = self.mode_var.get()
        if mode == "hide":
            self.data_frame.pack(fill=tk.X, padx=5, pady=5)
            self.quality_frame.pack(fill=tk.X, padx=5, pady=5)
        else:
            self.data_frame.pack_forget()
            self.quality_frame.pack_forget()
            
    def _select_carrier(self):
        """Open file dialog to select carrier image"""
        filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp")]
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.carrier_label.config(text=os.path.basename(filename))
            self._update_preview(filename)
            
    def _select_data(self):
        """Open file dialog to select data file"""
        filename = filedialog.askopenfilename()
        if filename:
            self.data_label.config(text=os.path.basename(filename))
            
    def _update_preview(self, image_path):
        """Update image preview"""
        try:
            # Load and resize image for preview
            image = Image.open(image_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.preview_label.config(image=photo)
            self.preview_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image preview: {str(e)}")
            
    def _execute_operation(self):
        """Execute the selected steganography operation"""
        if not self.password_entry.get():
            messagebox.showerror("Error", "Password is required")
            return
            
        # Start operation in a separate thread
        thread = threading.Thread(target=self._process_operation)
        thread.start()
        
    def _process_operation(self):
        """Process the steganography operation"""
        try:
            self.execute_btn.config(state='disabled')
            self.status_label.config(text="Processing...")
            self.progress_var.set(0)
            
            mode = self.mode_var.get()
            method = self.method_var.get()
            
            if mode == "hide":
                self._process_hide()
            else:
                self._process_extract()
                
            self.status_label.config(text="Operation completed successfully")
            messagebox.showinfo("Success", "Operation completed successfully")
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
            
        finally:
            self.execute_btn.config(state='normal')
            self.progress_var.set(0)
            
    def _process_hide(self):
        """Process hide operation"""
        # Get output path
        output_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")]
        )
        if not output_path:
            return
            
        # Read data file
        with open(self.data_label.cget("text"), 'rb') as f:
            data = f.read()
            
        # Hide data
        self.stego.hide_data(
            data=data,
            carrier_image_path=self.carrier_label.cget("text"),
            output_path=output_path,
            password=self.password_entry.get(),
            method=self.method_var.get(),
            quality=self.quality_scale.get()
        )
        
    def _process_extract(self):
        """Process extract operation"""
        # Get output path
        output_path = filedialog.asksaveasfilename()
        if not output_path:
            return
            
        # Extract data
        extracted_data = self.stego.extract_data(
            stego_image_path=self.carrier_label.cget("text"),
            password=self.password_entry.get(),
            method=self.method_var.get()
        )
        
        # Save extracted data
        with open(output_path, 'wb') as f:
            f.write(extracted_data)
            
    def run(self):
        """Start the GUI application"""
        self.window.mainloop()

if __name__ == "__main__":
    app = SteganographyGUI()
    app.run() 