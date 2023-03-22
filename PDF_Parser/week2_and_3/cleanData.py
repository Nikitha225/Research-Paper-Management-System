import json



filePath = './multi_agent/text/multi_agent.json'
newFilePath = './multi_agent/text/multi_agent_clean.json'
# filePath = './NetSquid/text/NetSquid.json'
# newFilePath = './NetSquid/text/NetSquid_clean.json'


def identify_bold_fontSize(filePath):
    with open(filePath, "r", errors="ignore") as read_file:
        json_file = json.load(read_file)
        fontSizes = dict()
        bold_locations_info = []
        bold_locations = set()
        for page_num, page_data in json_file.items():
            for para_num, para_data in page_data.items():
                for line_num, line_data in para_data.items():
                    fontSizes[line_data['font_size']] = fontSizes.get(line_data['font_size'], 0) + 1
                    if (line_data['bold']):
                        bold_locations_info.append({'page_num': page_num, 'para_num': para_num, 'line_num': line_num,
                                                    'font_size': line_data['font_size']})
                        bold_locations.add((page_num, para_num, line_num))

        return fontSizes, bold_locations_info, bold_locations


fontSizes, bold_locations_info, bold_locations = identify_bold_fontSize(filePath)

print(fontSizes)
fontSizesDesc = sorted(fontSizes.items(), key=lambda item: item[0], reverse= True)
fontCountDesc = sorted(fontSizes.items(), key=lambda item: item[1], reverse=True)
fontCountSum = sum(fontSizes.values())
consideredFontCount = 0.7 * fontCountSum

print(fontSizesDesc)
print(fontCountDesc)
highFreqFonts = set()
tempCount = 0
for metric in fontCountDesc:
    tempCount += metric[1]
    highFreqFonts.add(metric)
    if tempCount >= consideredFontCount:
        break
print(highFreqFonts)
boldFontSizes = set()
for metric in fontSizesDesc:
    if metric in highFreqFonts:
        break
    boldFontSizes.add(metric[0])


print(boldFontSizes)
# boldFontSizes = set()
# boldFontSizes.add(max(fontSizes))
# fontSizes.remove(max(fontSizes))
# boldFontSizes.add(max(fontSizes))

boldTexts = {'introduction', 'abstract', 'key words', 'references', 'conclusion', 'acknowledgements', 'additional information'}


def keyWordCheck(boldTexts, word):
    if word in boldTexts:
        return True


def convert_unStructured_to_structured_json(filePath, boldFontSizes, bold_locations):
    with open(filePath, "r", errors="ignore") as read_file:
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
                                        ((page_num, para_num, line_num) in bold_locations) or
                                        (font_size in boldFontSizes) or
                                        (any([keyWordCheck(boldTexts, word.lower()) for word in text.strip().split(" ")]) and len(text.strip().split(" ")) <= 3)
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


newJson = convert_unStructured_to_structured_json(filePath, boldFontSizes, bold_locations)
with open(newFilePath, 'w', encoding='utf-8') as jp:
    json.dump(newJson, jp, ensure_ascii=True, indent=4)
