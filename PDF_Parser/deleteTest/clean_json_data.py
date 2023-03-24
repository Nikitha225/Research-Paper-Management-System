import json

boldTexts = {'introduction', 'abstract', 'key words', 'references', 'conclusion', 'acknowledgements',
             'additional information'}


# filePath = './multi_agent/text/multi_agent.json'
# newFilePath = './multi_agent/text/multi_agent_clean.json'
# filePath = './NetSquid/text/NetSquid.json'
# newFilePath = './NetSquid/text/NetSquid_clean.json'

def identify_bold_fontSize(file_path):
    try:

        with open(file_path, "r", errors="ignore") as read_file:
            json_file = json.load(read_file)
            font_sizes = dict()
            bold_lines = set()
            for page_num, page_data in json_file.items():
                for para_num, para_data in enumerate(page_data):
                    for line_num, line_data in enumerate(para_data):
                        font_sizes[line_data['font_size']] = font_sizes.get(line_data['font_size'], 0) + 1
                        if line_data['bold']:
                            bold_lines.add((page_num, para_num, line_num))

            return font_sizes, bold_lines
    except Exception as e:
        print("An unexpected error happened in clean_json_data.py > identify_bold_fontSize function" + str(e))
        return dict(), set()


def return_bold_font_sizes(font_sizes):
    try:

        fontSizesDesc = sorted(font_sizes.items(), key=lambda item: item[0], reverse=True)
        fontCountDesc = sorted(font_sizes.items(), key=lambda item: item[1], reverse=True)
        fontCountSum = sum(font_sizes.values())
        consideredFontCount = 0.7 * fontCountSum

        highFreqFonts = set()
        tempCount = 0
        for metric in fontCountDesc:
            tempCount += metric[1]
            highFreqFonts.add(metric)
            if tempCount >= consideredFontCount:
                break

        boldFontSizes = set()
        for metric in fontSizesDesc:
            if metric in highFreqFonts:
                break
            boldFontSizes.add(metric[0])

        return boldFontSizes
    except Exception as e:
        print('An unexpected error happened in clean_json_data.py > return_bold_font_sizes function' + str(e))
        return set()


def keyWordCheck(bold_texts, word):
    try:
        if word in bold_texts:
            return True
    except Exception as e:
        print('An unexpected error happened in clean_json_data.py > keyWordCheck function' + str(e))
        return False


def convert_unStructured_to_structured_json(file_path, boldFontSizes, bold_lines):
    try:

        with open(file_path, "r", errors="ignore") as read_file:
            json_file = json.load(read_file)
            newJsonFile = {}
            # pages_data = []
            for page_num, page_data in json_file.items():
                newPage = []
                if page_data:
                    for para_num, para_data in enumerate(page_data):
                        if para_data:
                            newParagraph = []
                            for line_num, line_data in enumerate(para_data):
                                if line_data:
                                    text = line_data['text']
                                    newLine = {}
                                    font_size = line_data['font_size']
                                    if (
                                            ((page_num, para_num, line_num) in bold_lines) or
                                            (font_size in boldFontSizes) or
                                            (any([keyWordCheck(boldTexts, word.lower()) for word in
                                                  text.strip().split(" ")]) and len(text.strip().split(" ")) <= 3)
                                    ):
                                        newLine['bold'] = True
                                    else:
                                        newLine['bold'] = False
                                    newLine['font_size'] = font_size
                                    newLine['text'] = text
                                    newParagraph.append(newLine)
                            newPage.append(newParagraph)
                    # pages_data.append(newPage)
                    newJsonFile[page_num] = newPage
            # newJsonFile['pages'] = page_data
            return newJsonFile
    except Exception as e:
        print('An unexpected error happened in clean_json_data.py > convert_unStructured_to_structured_json function' + str(e))
        return {}


def clean_json_data(json_file_path):
    try:
        font_sizes, bold_lines = identify_bold_fontSize(json_file_path)
        boldFontSizes = return_bold_font_sizes(font_sizes)
        newJson = convert_unStructured_to_structured_json(json_file_path, boldFontSizes, bold_lines)
        # newJson["file_name"] = json_file_path.split("/")[-1]
        # newFilePath = json_file_path[:-5] + "_clean" + ".json"
        with open(json_file_path, 'w', encoding='utf-8') as jp:
            json.dump(newJson, jp, ensure_ascii=True, indent=4)
        
        print("------------------- stage 2 -------------------------\n")
        print("Cleaned Json successfully unstructured format to structured \n")
    except Exception as e:
        print('An unexpected error happened in clean_json_data.py > clean_json_data function'+ str(e))


# clean_json_data('multi_agent/multi_agent.json')
# clean_json_data('NetSquid/NetSquid.json')
