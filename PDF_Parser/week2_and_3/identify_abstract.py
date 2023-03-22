import json

def identify_abstract(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    page1 = data["page_1"]

    abstract = []

    for para, paraDetails in page1.items():
        # print(paraDetails)
        if "abstract" in paraDetails["text"].lower():
            if len(paraDetails["text"]) > 20:
                abstract = paraDetails["text"][9:]
            else:
                paraNum = int(para.split("_")[1]) + 1
                abstract = page1[para.split("_")[0] + "_" + str(paraNum)]["text"]
            break

    return {"abstract": abstract}


print(identify_abstract('multi_agent/text/multi_agent.json'))
# print(identify_abstract('5G_Security/text/5G_Security.json'))
