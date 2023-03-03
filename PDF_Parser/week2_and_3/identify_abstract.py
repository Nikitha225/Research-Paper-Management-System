import json


def identify_abstract(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    page1 = data["page_1"]

    abstract = []

    for para, lines in page1.items():
        if "abstract" in lines[0].lower():
            if len(lines) > 2:
                abstract = lines[1:]
            else:
                paraNum = int(para.split("_")[1]) + 1
                abstract = page1[para.split("_")[0] + "_" + str(paraNum)]
            break

    print(abstract)


# identify_abstract('multi_agent/binary/multi_agent.json')
identify_abstract('5G_Security/binary/5G_Security.json')
