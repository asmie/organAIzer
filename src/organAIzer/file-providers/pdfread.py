"""Module implementing reading PDF files."""

# Read text from PDF

from pypdf import PdfReader


def read_pdf(file_path):
    """Function reading text from a PDF file."""

    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page_number in range(len(reader.pages)):
            text += reader.pages[page_number].extract_text()
    return text
