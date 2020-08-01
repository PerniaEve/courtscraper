import json
import os
import csv
from datetime import date
fields = []

def parse_har():
    contents = os.listdir('input')
    all_cases = []
    if not os.path.exists('processed'):
        os.makedirs('processed')
    for file in contents:
        if ".har" in file:
            with open('input/' + file) as f:
                content = json.loads(f.read())
                data = get_data(content)
                all_cases.append(data)
                os.rename('input/'+file, 'processed/'+str(date.today())+'_'+file)
    
    return all_cases

def get_data(content):
    entries = content["log"]["entries"]
    all_values = []
    global fields
    for e in entries:
        if 'text' in e["response"]["content"].keys():
            text = e["response"]["content"]["text"]
            try:
                data = json.loads(text)
                d = data["layers"][0]["formats"][0]["subfiles"]
                keys = d.keys()
                for key in keys:
                    fields = d[key]["field names"]
                    idx = fields.index('CASINTX')
                    values = d[key]["data"]
                    for v in values:
                        if v[idx] == 'Eviction':
                            all_values.append(v)
            except:
                continue
    return all_values

def to_csv(items, fname):
    if not os.path.exists('output'):
        os.makedirs('output')
    with open('output/' + fname, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, fields)
        dict_writer.writeheader()
        dict_writer.writerows(items)


datasets = parse_har()
all_items = []
for data in datasets:
    for values in data:
        case = dict()
        for i in range(0, len(fields)):
            case.update({fields[i]:values[i]})
        all_items.append(case)
to_csv(all_items, 'formatted.csv')