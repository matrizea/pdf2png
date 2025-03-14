# PDF to PNG Conversion Tool

This is a simple Python tool that converts each page of a PDF file into a PNG image using the [pdf2image](https://pypi.org/project/pdf2image/) library.

## Requirements

- Python 3.x
- pdf2image library
- Poppler for PDF rendering

## Installation

### 1. Install pdf2image

Install the library using pip:

    pip install pdf2image

### 2. Install Poppler

Depending on your operating system, follow one of the instructions below:

- Windows:  
  Download the Poppler binaries from https://github.com/oschwartz10612/poppler-windows.git and add the `bin` folder to your system's PATH.

- macOS:  
  Install Poppler using Homebrew:

    brew install poppler

- Linux (Ubuntu/Debian):  
  Install Poppler via apt:

    sudo apt-get install poppler-utils

## Usage

Once the dependencies are installed, run the script by passing the PDF file as an argument:

    python pdf_to_png.py sample.pdf

The script will convert each page of `sample.pdf` into PNG images. For example, if your PDF file is named `sample.pdf`, the output files will be named:

- sample_page_1.png
- sample_page_2.png
- etc.

## Code Example

Below is the complete code for `pdf_to_png.py`:

    import sys
    import os
    from pdf2image import convert_from_path

    def pdf_to_images(pdf_file, dpi=300):
        """
        Convert a PDF file into images (PNG format).

        :param pdf_file: Path to the PDF file.
        :param dpi: Resolution in DPI (default is 300).
        """
        try:
            # Convert PDF pages to images
            pages = convert_from_path(pdf_file, dpi=dpi)
        except Exception as e:
            print(f"Error during PDF conversion: {e}")
            return

        # Get the base name of the PDF file without extension
        base, _ = os.path.splitext(pdf_file)
        # Save each page as a PNG image
        for i, page in enumerate(pages):
            filename = f"{base}_page_{i+1}.png"
            page.save(filename, 'PNG')
            print(f"Saved: {filename}")

    if __name__ == '__main__':
        if len(sys.argv) != 2:
            print("Usage: python pdf_to_png.py <PDF file>")
            sys.exit(1)
        pdf_file = sys.argv[1]
        pdf_to_images(pdf_file)

## Summary

To summarize, perform the following steps:

1. Install the required library:
   
       pip install pdf2image

2. Install Poppler according to your operating system.
3. Run the script:
   
       python pdf_to_png.py sample.pdf

Each page of the PDF will be saved as a PNG image in the same directory.

## License

This project is licensed under the MIT License.
