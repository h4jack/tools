# PDF to DOCX Converter

This is a Python script to convert PDF files to DOCX format. It utilizes the `pdf2docx` library to achieve this conversion.

## Usage

To convert PDF files to DOCX, run the script with the PDF file paths as arguments. For example:

    python converter.py file1.pdf file2.pdf ... filen.pdf

## Usage Notes

- Ensure the PDF files you want to convert are accessible and correctly specified in the command line arguments.
- Output files will be saved in the same directory as the input PDF files.
- If multiple PDF files are provided as arguments, each one will be converted individually.

## Features

- Converts PDF files to DOCX format.
- Handles multiple PDF files at once.
- Automatically renames output files to prevent overwriting.

## Limitations

- Only supports conversion from PDF to DOCX.
- Does not currently support conversion from DOCX to PDF.
- Limited error handling.

## Tech Stack

**Language:** Python 3.x+\
```modules
Converter from pdf2docx 
argv and exit from sys 
os.path 
ptdhelp
glob
```

## Authors

- [@h4jack](https://www.github.com/h4jack)