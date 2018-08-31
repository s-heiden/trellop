from dataclasses import dataclass


@dataclass
class ClientCard:
    desc: str
    due_weekday: str
    idList: str
    idMembers: str
    name: str
    pos: str


@dataclass
class Props:
    api_key: str
    api_token: str
    client_cards: [ClientCard]
    week_start_weekday: str


@dataclass
class ServerCard:
    name: str
    desc: str
    pos: str
    due: str
    idList: str
    idMembers: str
    idLabels: str
    urlSource: str
