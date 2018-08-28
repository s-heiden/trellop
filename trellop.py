import argparse
import json
from pprint import pprint


def main():
    # parse command line args
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-f", "--file", help="location of the property file")
    args = arg_parser.parse_args()

    if args.file:
        settings = parse_trellop_json(args.file)
        pprint(settings)


def parse_trellop_json(filename):
    with open(filename) as trellop_json:
        data = json.load(trellop_json)
        return data


main()
