import json
from pprint import pprint

def main():
    parse_trellop_json()


def parse_trellop_json():
    with open('trellop.json') as trellop_json:
        data = json.load(trellop_json)
        pprint(data)


main()
