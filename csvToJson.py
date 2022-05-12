import json
import csv
from collections import OrderedDict

samples = []

with open('hci+d 스승의날 편지.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)


    for row in reader:
        person = OrderedDict()
        person['name'] = row[1]
        person['level'] = row[5]
        person['dept'] = row[2]
        person['status'] = row[3]
        person['letter-j'] = row[6]
        person['letter-h'] = row[7]
        samples.append(person)

with open("letter.json", 'w') as outfile:
    json.dump(samples, outfile, ensure_ascii=False, indent="\t")


