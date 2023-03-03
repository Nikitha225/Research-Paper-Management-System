from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator, TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
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
            # para_lines = {}
            # lineNum = 1
            # for para_line in paraText.strip().split("\n"):
            #     para_lines["line_" + str(lineNum)] = para_line
            #     lineNum += 1
            para_lines = []
            for para_line in paraText.strip().split("\n"):
                para_lines.append(para_line)
            page_json["paragraph_" + str(paraNum)] = para_lines
            paraText = ""
            paraNum += 1
        prevLine = page_line
    return page_json


def pdf_to_json(pdf_file):
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
            pdf_json[f"page_{page_no + 1}"] = pdf_page_to_json(data.encode('utf-8'))
            data = ''
            stringIO.truncate(0)
            stringIO.seek(0)
        page_no += 1

    filename = pdf_file.split(".")[0].split("/")
    filename.insert(1, "binary")
    filename = "/".join(filename) + ".json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as jp:
        json.dump(pdf_json, jp, ensure_ascii=False, indent=4)

    print("Converted PDF to Json successfully using direct binary decode from pdf binary text")


# pdf_to_json('multi_agent/multi_agent.pdf')
pdf_to_json('5G_Security/5G_Security.pdf')
