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

    python pdf2png.py sample.pdf

The script will convert each page of `sample.pdf` into PNG images. For example, if your PDF file is named `sample.pdf`, the output files will be named:

- sample_page_1.png
- sample_page_2.png
- etc.

## License

This project is licensed under the MIT License.
