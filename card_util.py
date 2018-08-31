"""Provide utilities concerning cards"""
from munch import Munch

import date_util
from models import ServerCard, ClientCard


def from_client_to_server(card: ClientCard, timezone: str) -> ServerCard:
    """Map ClientCard object to ServerCard object"""
    due = date_util.to_earliest_future_weekday(card.due_weekday) + 'T' + card.due_time + timezone
    print(due)

    return Munch.fromDict({
        'name': card.name,
        'desc': card.desc,
        'idList': card.idList,
        'pos': card.pos,
        'due': due,
        'idMembers': card.idMembers,
        'idLabels': card.idLabels,
    })
