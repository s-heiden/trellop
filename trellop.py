import argparse
import json
from pprint import pprint

import requests

import constants


def main():
    # parse command line args
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-f", "--file", help="location of the property file")
    args = arg_parser.parse_args()

    if args.file:
        settings = parse_trellop_json(args.file)
        pprint(settings)

        post_cards(settings)


def parse_trellop_json(filename):
    with open(filename) as trellop_json:
        data = json.load(trellop_json)
        return data


def post_cards(settings):
    url = constants.API_URL + 'cards/?key=' + settings['api_key'] + '&token=' + settings['api_token']

    print(url)

    for card_property in settings['cards_properties']:
        data = {
            'name': card_property['name'],
            'desc': card_property['desc'],
            'idList': card_property['idList'],
            'pos': card_property['pos']
        }

        r = requests.post(url, data)

        print(r.status_code, r.reason)
        print(r.text[:300] + '...')

main()