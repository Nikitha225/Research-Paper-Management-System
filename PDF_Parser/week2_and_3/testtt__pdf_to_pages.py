from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator, TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.layout import LAParams, LTTextContainer, LTChar,LTLine
import pdfminer
from pdfminer.high_level import extract_pages
import io, json, os


def pdf_page_to_json(pdf_page_data):
    page_json = {}
    paraNum = 1
    paraText = ""
    prevLine = ""
    for page_line in pdf_page_data.decode('utf-8').split("\n"):
        if page_line != "":
            paraText += page_line
            paraText += "\n"

        if prevLine != "" and page_line == "":
            para_lines = []
            for para_line in paraText.strip().split("\n"):
                para_lines.append(para_line)
            page_json["paragraph_" + str(paraNum)] = para_lines
            paraText = ""
            paraNum += 1
        prevLine = page_line
    return page_json


def pdf_to_json(pdf_file):
    Extract_Data = []
    count = 0
    for pdf_layout in extract_pages(pdf_file):
        for element in pdf_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    for character in text_line:
                        if isinstance(character, LTChar):
                            Font_size = character.size
                Extract_Data.append([Font_size, (element.get_text())])
        count += 1

    print(Extract_Data)

    pdf_json = {}
    fp = open(pdf_file, 'rb')
    # resourceManager = PDFResourceManager()
    # stringIO = io.StringIO()
    # codec = 'utf-8'
    # laParams = LAParams()
    # device = TextConverter(resourceManager, stringIO, codec=codec, laparams=laParams)
    # interpreter = PDFPageInterpreter(resourceManager, device)

    page_no = 0
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == page_no:
            pdf_json[f"page_{page_no + 1}"] = pdf_page_to_json(data.encode('utf-8'))

        page_no += 1
    fp.close()

    filename = pdf_file.split(".")[0].split("/")
    filename.insert(1, "binary")
    filename = "/".join(filename) + ".json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as jp:
        json.dump(pdf_json, jp, ensure_ascii=False, indent=4)

    print("Converted PDF to Json successfully using direct binary decode from pdf binary text")


pdf_to_json('multi_agent/multi_agent.pdf')
# pdf_to_json('5G_Security/5G_Security.pdf')
