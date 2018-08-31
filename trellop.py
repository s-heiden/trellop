import argparse
import json
from pprint import pprint

import requests
from munch import Munch

import card_util
import constants
from models import Props, ServerCard


def main():
    """Handle command line arguments"""
    # parse command line args
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-f", "--file", help="location of the property file")
    args = arg_parser.parse_args()

    if args.file:
        props: Props = parse_trellop_json(args.file)
        pprint(props)

        create_cards(props)


def parse_trellop_json(filename: str) -> Props:
    with open(filename) as trellop_json:
        data: dict = json.load(trellop_json)
        pprint(data)

        props = Munch.fromDict(data)
        pprint(props.api_key)
        return props


def create_cards(props: Props) -> int:
    """Post cards given in props to API"""
    url = constants.API_URL + 'cards/?key=' + props.api_key + '&token=' + props.api_token

    print('url: ' + url)

    for card_property in props.client_cards:
        data: ServerCard = card_util.from_client_to_server(card_property, props.timezone)

        request = requests.post(url, data)

        print(request.status_code, request.reason)
        print(request.text[:300] + '...')

        return request.status_code

main()
