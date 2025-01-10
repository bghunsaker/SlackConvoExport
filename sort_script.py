# Author: Bryson Hunsaker
# Date:1/9/2025

import sys
import json 

json_list = []
INPUT_FILE = "convo_hist.txt"
OUTPUT_FILE = "convo_hist_sorted.txt"

with open('INPUT_FILE', 'r') as f:
    for line in f:
        jsondata = json.loads(line)
        json_list.append(jsondata)


sorted_json = sorted(json_list, key=lambda d: d['ts'])

for x in sorted_json:
    print(x['text'])
    
msg = 1
    
with open('OUTPUT_FILE', 'w') as f:
    for x in sorted_json:
        f.write(str(msg) + ":" + json.dumps(x['text']) + "\n")
        msg += 1