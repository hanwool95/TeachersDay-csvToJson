import json
import csv
from collections import OrderedDict
from dictionary import *

samples = []

with open('hci+d 스승의날 편지.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    next(reader)
    next(reader)

    for row in reader:
        person = OrderedDict()
        person['name'] = row[1]
        if row[4] in pokemon_num:
            person['pokenum'] = pokemon_num[row[4]]
        else:
            print("find not pokemon")
            print(row[1], row[4])
            person['pokenum'] = row[4]
        try:
            person['level'] = int(row[5])
        except:
            print("find not num")
            print(row[1], row[5])
            person['level'] = row[5]
        person['dept'] = row[2]
        person['status'] = row[3]
        person['letter-j'] = row[6]
        person['letter-h'] = row[7]
        samples.append(person)

with open("letter.json", 'w') as outfile:
    json.dump(samples, outfile, ensure_ascii=False, indent="\t")


