import argparse
import sys
from pathlib import Path
from typing import Optional
from steganography import SteganoExfil
from steganography.exceptions import SteganoError

class CLI:
    def __init__(self):
        self.stego = SteganoExfil()
        self.parser = self._create_parser()
        
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create command line argument parser"""
        parser = argparse.ArgumentParser(
            description="Steganography Tool - Hide and extract data in images"
        )
        
        subparsers = parser.add_subparsers(dest='command', required=True)
        
        # Hide command
        hide_parser = subparsers.add_parser('hide', help='Hide data in image')
        hide_parser.add_argument('-i', '--input', required=True, help='Carrier image path')
        hide_parser.add_argument('-d', '--data', required=True, help='Data file to hide')
        hide_parser.add_argument('-o', '--output', required=True, help='Output image path')
        hide_parser.add_argument('-p', '--password', required=True, help='Encryption password')
        hide_parser.add_argument('-m', '--method', choices=['dct', 'lsb'], 
                               default='dct', help='Steganography method')
        hide_parser.add_argument('-q', '--quality', type=float, default=0.8,
                               help='Image quality (0.1-1.0)')
        
        # Extract command
        extract_parser = subparsers.add_parser('extract', help='Extract hidden data')
        extract_parser.add_argument('-i', '--input', required=True, help='Stego image path')
        extract_parser.add_argument('-o', '--output', required=True, help='Output file path')
        extract_parser.add_argument('-p', '--password', required=True, help='Decryption password')
        extract_parser.add_argument('-m', '--method', choices=['dct', 'lsb'],
                                  default='dct', help='Steganography method')
        
        return parser
        
    def run(self, args: Optional[list] = None) -> int:
        """Run CLI with optional arguments"""
        try:
            parsed_args = self.parser.parse_args(args)
            
            if parsed_args.command == 'hide':
                return self._handle_hide(parsed_args)
            elif parsed_args.command == 'extract':
                return self._handle_extract(parsed_args)
                
        except SteganoError as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            return 1
        except Exception as e:
            print(f"Unexpected error: {str(e)}", file=sys.stderr)
            return 2
            
        return 0
        
    def _handle_hide(self, args: argparse.Namespace) -> int:
        """Handle hide command"""
        with open(args.data, 'rb') as f:
            data = f.read()
            
        self.stego.hide_data(
            data=data,
            carrier_image_path=args.input,
            output_path=args.output,
            password=args.password,
            method=args.method,
            quality=args.quality
        )
        
        print(f"Data hidden successfully in {args.output}")
        return 0
        
    def _handle_extract(self, args: argparse.Namespace) -> int:
        """Handle extract command"""
        extracted_data = self.stego.extract_data(
            stego_image_path=args.input,
            password=args.password,
            method=args.method
        )
        
        with open(args.output, 'wb') as f:
            f.write(extracted_data)
            
        print(f"Data extracted successfully to {args.output}")
        return 0

def main():
    """CLI entry point"""
    cli = CLI()
    sys.exit(cli.run())

if __name__ == "__main__":
    main() 