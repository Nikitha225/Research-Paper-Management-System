import os
import pdfplumber
from pdfminer.high_level import extract_text
from pypdf import PdfReader as pyPdfReader
from PyPDF2 import PdfReader as pyPdf2Reader
from pdfrw import PdfReader as pdfrwPdfReader


def pdfminer_convert_pdt_to_text(pdf_file, text_file):
    with open(pdf_file, 'rb') as f:
        os.remove(text_file) if os.path.exists(text_file) else None
        text = extract_text(f)
        with open(text_file, 'w', encoding="utf-8") as pdfminer_f:
            pdfminer_f.write(text)


def pypdf_convert_pdf_to_text(pdf_file, text_file):
    os.remove(text_file) if os.path.exists(text_file) else None
    reader = pyPdfReader(pdf_file)
    number_of_pages = len(reader.pages)
    with open(text_file, 'a', encoding="utf-8") as pypdf_f:
        for page_number in range(number_of_pages):
            page = reader.pages[page_number]
            text = page.extract_text()
            pypdf_f.write(text)


def pypdf2_convert_pdf_to_text(pdf_file, text_file):
    os.remove(text_file) if os.path.exists(text_file) else None
    reader = pyPdf2Reader(pdf_file)
    number_of_pages = len(reader.pages)
    with open(text_file, 'a', encoding="utf-8") as pypdf2_f:
        for page_number in range(number_of_pages):
            page = reader.pages[page_number]
            text = page.extract_text()
            pypdf2_f.write(text)


def pdfplumber_convert_pdf_to_text(pdf_file, text_file):
    os.remove(text_file) if os.path.exists(text_file) else None
    with pdfplumber.open(pdf_file) as pdf_f:
        number_of_pages = len(pdf_f.pages)
        with open(text_file, 'a', encoding="utf-8") as pdfplumber_f:
            for page_number in range(number_of_pages):
                page = pdf_f.pages[page_number]
                pdfplumber_f.write(page.extract_text())


# def pdfrw_convert_pdf_to_text(pdf_file, text_file):
#     os.remove(text_file) if os.path.exists(text_file) else None
#     reader = pdfrwPdfReader(pdf_file)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # pdfminer_convert_pdt_to_text('multi_agent.pdf', 'pdfminer_multi_agent.txt')
    # pypdf_convert_pdf_to_text('multi_agent.pdf', 'pypdf_multi_agent.txt')
    # pypdf2_convert_pdf_to_text('multi_agent.pdf', 'pypdf2_multi_agent.txt')
    pdfplumber_convert_pdf_to_text('multi_agent.pdf', 'pdfplumber_multi_agent.txt')
