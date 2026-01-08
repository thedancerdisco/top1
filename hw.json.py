import json
from typing import TextIO
from collections import Counter

def  generate_report(file:TextIO)->dict[str, int]:
    dataf =  list(filter(lambda s: s["status"] == "completed", json.load(file)))
    for i in range(len (dataf)):
        del dataf[i]["task"], dataf[i]["status"]
        dataf[i] = str(dataf[i]["assignee"])
        print({**Counter(dataf)})

with open('journal.json', mode='r', encoding='utf-8') as file1:
    generate_report(file1)
