from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io, json, os

# https://stackoverflow.com/questions/34606382/pdfminer-extract-text-with-its-font-information

def pdf_page_to_json(pdf_page):
    with open(pdf_page, 'r', encoding='utf-8') as f:
        pageLines = f.readlines()

    page_json = {}
    paraNum = 1
    paraText = ""
    prevLine = ""
    for page_line in pageLines:
        if page_line != '\n':
            paraText += page_line
            paraText += " "

        if prevLine != "\n" and page_line == "\n":
            para_lines = {}
            lineNum = 1
            for para_line in paraText.strip().split("\n "):
                para_lines["line_" + str(lineNum)] = para_line
                lineNum += 1
            page_json["paragraph_" + str(paraNum)] = para_lines
            paraText = ""
            paraNum += 1
        prevLine = page_line

    return page_json


def pdf_to_json(pdf_file):
    filename = pdf_file.split(".")[0].split("/")
    filename.insert(1, "text")
    filename = "/".join(filename)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    pdf_json = {}
    fp = open(pdf_file, 'rb')
    resourceManager = PDFResourceManager()
    stringIO = io.StringIO()
    codec = 'utf-8'
    laParams = LAParams()
    device = TextConverter(resourceManager, stringIO, codec=codec, laparams=laParams)
    interpreter = PDFPageInterpreter(resourceManager, device)

    page_no = 0
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == page_no:
            interpreter.process_page(page)
            data = stringIO.getvalue()
            fname = filename + f"{page_no + 1}.txt"
            with open(fname, 'wb') as file:
                file.write(data.encode('utf-8'))
            pdf_json[f"page_{page_no + 1}"] = pdf_page_to_json(fname)
            # os.remove(filename)
            data = ''
            stringIO.truncate(0)
            stringIO.seek(0)
        page_no += 1

    filename += ".json"
    with open(filename, 'w', encoding='utf-8') as jp:
        json.dump(pdf_json, jp, ensure_ascii=False, indent=4)

    print("Converted PDF to Json successfully from text files generated in pdf pages to text convertion ")


# pdf_to_json('multi_agent/multi_agent.pdf')
pdf_to_json('5G_Security/5G_Security.pdf')
