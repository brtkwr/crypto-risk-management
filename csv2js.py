#!/usr/bin/env python
import csv
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ./csv2js.py btc-usd.js < btc-usd.csv')
        sys.exit(1)
    jsonfile = open(sys.argv[1], 'w')
    reader = csv.DictReader(sys.stdin)
    jsonfile.write('export default ' + json.dumps([row for row in reader], indent=4))
