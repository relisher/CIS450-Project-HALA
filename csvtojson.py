import csv
import json

with open('match_database5.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('matchconverted5.json', 'w') as f:
    json.dump(rows, f)