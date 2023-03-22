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
                for para_num, para_data in page_data.items():
                    for line_num, line_data in para_data.items():
                        font_sizes[line_data['font_size']] = font_sizes.get(line_data['font_size'], 0) + 1
                        if line_data['bold']:
                            bold_lines.add((page_num, para_num, line_num))

            return font_sizes, bold_lines
    except:
        print("An unexpected error happened in cleanData.py > identify_bold_fontSize function")
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
    except:
        print('An unexpected error happened in cleanData.py > return_bold_font_sizes function')
        return set()



def keyWordCheck(bold_texts, word):
    try:
        if word in bold_texts:
            return True
    except:
        print('An unexpected error happened in cleanData.py > keyWordCheck function')
        return False



def convert_unStructured_to_structured_json(file_path, boldFontSizes, bold_lines):
    try:

        with open(file_path, "r", errors="ignore") as read_file:
            json_file = json.load(read_file)
            newJsonFile = {}
            for page_num, page_data in json_file.items():
                newPage = {}
                if page_data:
                    for para_num, para_data in page_data.items():
                        if para_data:
                            newParagraph = {}
                            for line_num, line_data in para_data.items():
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
                                    newParagraph[line_num] = newLine
                            newPage[para_num] = newParagraph
                    newJsonFile[page_num] = newPage

            return newJsonFile
    except:
        print('An unexpected error happened in cleanData.py > convert_unStructured_to_structured_json function')
        return {}



def clean_json_data(json_file_path):
    try:
        font_sizes, bold_lines = identify_bold_fontSize(json_file_path)
        boldFontSizes = return_bold_font_sizes(font_sizes)
        newJson = convert_unStructured_to_structured_json(json_file_path, boldFontSizes, bold_lines)
        newFilePath = json_file_path.split(".")[0] + "_clean" + ".json"
        with open(newFilePath, 'w', encoding='utf-8') as jp:
            json.dump(newJson, jp, ensure_ascii=True, indent=4)
    except:
        print('An unexpected error happened in cleanData.py > clean_json_data function')


# clean_json_data('./multi_agent/multi_agent.json')
clean_json_data('./NetSquid/NetSquid.json')