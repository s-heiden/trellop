"""Contain domain models used in trelop"""
from dataclasses import dataclass


@dataclass
class ClientCard:
    """Card model for the client domain"""
    desc: str
    due_weekday: str
    due_time: str
    idList: str
    idMembers: str
    name: str
    pos: str


@dataclass
class Props:
    """Model representing user properties given in trellop.json"""
    api_key: str
    api_token: str
    client_cards: [ClientCard]
    timezone: str
    week_start_weekday: str


@dataclass
class ServerCard:
    """Card model for the server domain"""
    name: str
    desc: str
    pos: str
    due: str
    idList: str
    idMembers: str
    idLabels: str
    urlSource: str
