
from pdfminer.layout import LTTextContainer, LTChar, LTTextLineHorizontal
from pdfminer.high_level import extract_pages
import json


# https://stackoverflow.com/questions/34606382/pdfminer-extract-text-with-its-font-information
def pdf_page_to_json(pdf_page):
    try:
        page_json = []
        paraNum = 1
        paraText = ""
        prevLine = ""
        line_content = ""
        for paraNum, content in enumerate(pdf_page):
            para = []
            for lineNum, lineContent in enumerate(content):
                fontSize, bold, lineContent = lineContent[0], lineContent[1], lineContent[2]

                line_content = lineContent.strip().split("\n")
                line_content = " ".join(line_content)

                para.append({"font_size": round(fontSize), "bold": bold, "text": line_content})
            page_json.append(para)

        return page_json
    except Exception as e:
        print('An unexpected error happened in pdf_to_json.py > pdf_page_to_json function' + str(e))
        return []



def pdf_to_json(pdf_file):
    try:
        filename = pdf_file[:-4]
        pdf_json = {}
        # pages_data = []
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
            pdf_json[f"page_{page_no + 1}"] = pdf_page_to_json(Extract_Data)
            # pages_data.append(pdf_page_to_json(Extract_Data))
            Extract_Data = []
            page_no += 1
        # pdf_json["pages"] = pages_data
        with open(filename + '.json', 'w', encoding='utf-8') as jp:
            json.dump(pdf_json, jp, ensure_ascii=True, indent=4)
        print("------------------- stage 1 -------------------------\n")
        print("Converted PDF to Json successfully from text files generated in pdf pages to text convertion \n")
    except Exception as e:
        with open(filename + '.json', 'w', encoding='utf-8') as jp:
            json.dump(pdf_json, jp, ensure_ascii=True, indent=4)
        print("An unexpected error happened in pdf_to_json.py > pdf_to_json function" + str(e))


# pdf_to_json('multi_agent/multi_agent.pdf')
# pdf_to_json('5G_Security/5G_Security.pdf')
# pdf_to_json('NetSquid/NetSquid.pdf')
# pdf_to_json('Sequence/Sequence.pdf')

