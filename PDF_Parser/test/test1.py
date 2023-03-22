from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

def pdf_to_html(pdf_path, html_path):
    resource_manager = PDFResourceManager()
    with open(html_path, 'wb') as output_file:
        converter = HTMLConverter(resource_manager, output_file, laparams=LAParams())
        with open(pdf_path, 'rb') as input_file:
            interpreter = PDFPageInterpreter(resource_manager, converter)
            for page in PDFPage.get_pages(input_file):
                interpreter.process_page(page)
        converter.close()

pdf_to_html('multi_agent.pdf', 'output.html')
