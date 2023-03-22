from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams, LTTextContainer, LTChar, LTLine, LTTextLineHorizontal
from pdfminer.high_level import extract_pages
import io, json, os


# https://stackoverflow.com/questions/34606382/pdfminer-extract-text-with-its-font-information
def pdf_page_to_json(pdf_page):
    page_json = {}
    paraNum = 1
    paraText = ""
    prevLine = ""
    line_content = ""
    for paraNum, content in enumerate(pdf_page):
        para = {}
        for lineNum, lineContent in enumerate(content):
            fontSize, bold, lineContent = lineContent[0], lineContent[1], lineContent[2]

            line_content = lineContent.strip().split("\n")
            line_content = " ".join(line_content)

            para["line_" + str(lineNum)] = {"font_size": round(fontSize), "bold": bold, "text": line_content}
        page_json["paragraph_" + str(paraNum)] = para

    # for page_line in pageLines:
    #     if page_line != '\n':
    #         paraText += page_line
    #         paraText += " "
    #
    #     if prevLine != "\n" and page_line == "\n":
    #         para_lines = {}
    #         lineNum = 1
    #         for para_line in paraText.strip().split("\n "):
    #             para_lines["line_" + str(lineNum)] = para_line
    #             lineNum += 1
    #         page_json["paragraph_" + str(paraNum)] = para_lines
    #         paraText = ""
    #         paraNum += 1
    #     prevLine = page_line

    return page_json


def pdf_to_json(pdf_file):
    filename = pdf_file.split(".")[0].split("/")
    filename.insert(1, "text")
    filename = "/".join(filename)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    pdf_json = {}
    Extract_Data = []
    bold = False
    page_no = 0
    for pdf_layout in extract_pages(pdf_file):
        for element in pdf_layout:
            Extract_lines = []
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    bold = False
                    if not isinstance(text_line, LTTextLineHorizontal): continue
                    for character in text_line:
                        if isinstance(character, LTChar):
                            Font_size = character.size
                            if 'Bold' in character.fontname:
                                bold = True
                        else:
                            continue
                    Extract_lines.append((Font_size, bold, (text_line.get_text())))
            Extract_Data.append(Extract_lines)
        # print(Extract_Data)
        # break
        pdf_json[f"page_{page_no + 1}"] = pdf_page_to_json(Extract_Data)
        Extract_Data = []
        page_no += 1
        # print(pdf_json)
        # break

    filename += ".json"
    with open(filename, 'w', encoding='utf-8') as jp:
        json.dump(pdf_json, jp, ensure_ascii=True, indent=4)

    print("Converted PDF to Json successfully from text files generated in pdf pages to text convertion ")


pdf_to_json('multi_agent/multi_agent.pdf')
# pdf_to_json('5G_Security/5G_Security.pdf')
# pdf_to_json('NetSquid/NetSquid.pdf')
# pdf_to_json('Sequence/Sequence.pdf')
# pdf_to_json('Sequence2/Sequence2.pdf')
