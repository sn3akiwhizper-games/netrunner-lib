import sys, re
from unidecode import unidecode

from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.cards import agenda, asset, event, hardware, ice, identity, operation, program, resource, upgrade

def to_card_id(card_name: str) -> str:
    '''
    convert stripped card title to card ID
    '''
    # Remove accents and convert to lowercase
    card_name = unidecode(card_name.lower())
    # swap spaces for underscore
    card_name = re.sub(' ','_',card_name)
    # Remove special characters
    card_name = re.sub(r'[^a-z0-9_]+', '', card_name)
    # Remove underscores from the beginning and end of the string
    card_name = card_name.strip('_')
    return card_name

def switch_card_type(card_data) -> Card:
    '''
    deprecated in favor of create_card function
    '''
    raise Exception('DEPRECATED')
    card_type = card_data['type_code']
    if card_type == "agenda":
        return Agenda(card_data)
    elif card_type == "asset":
        return Asset(card_data)
    elif card_type == "event":
        return Event(card_data)
    elif card_type == "hardware":
        return Hardware(card_data)
    elif card_type == "ice":
        return Ice(card_data)
    elif card_type == "identity":
        return Identity(card_data)
    elif card_type == "operation":
        return Operation(card_data)
    elif card_type == "program":
        return Program(card_data)
    elif card_type == "resource":
        return Resource(card_data)
    elif card_type == "upgrade":
        return Upgrade(card_data)
    else:
        print('unrecognized card type')
        print(card_data)
        sys.exit(-1)

def create_card(card_name:str,card_type:str,card_id:str) -> Card:
    '''
    create an instance of the specific card class using only its type and name
    card classes organized by type
    in each type file, each card has a class subclasses the main type class
    INPUT:
        card_name: title of card, parsed through "to_card_id" before sending here
        card_type: type_code of card
        card_id: id number of card
    
    RETURN:
        an instance of the desired card class, subclass of it's type, which is a subytype of the card class

    reference code:
        # Dynamically import the module containing the card class
        module = importlib.import_module(f"cards.{card_name.lower().replace(' ', '_')}")
        # Get the card class from the module
        card_class = getattr(module, card_name.replace(' ', ''))
    '''
    if card_type == "agenda":
        return getattr(agenda, f"{card_type}_{card_name}_{card_id}")()
    elif card_type == "asset":
        return getattr(asset, f"{card_type}_{card_name}_{card_id}")()
    elif card_type == "event":
        return getattr(event, f"{card_type}_{card_name}_{card_id}")()
    elif card_type == "hardware":
        return getattr(hardware, f"{card_type}_{card_name}_{card_id}")()
    elif card_type == "ice":
        return getattr(ice, f"{card_type}_{card_name}_{card_id}")()
    elif card_type == "identity":
        return getattr(identity, f"{card_type}_{card_name}_{card_id}")()
    elif card_type == "operation":
        return getattr(operation, f"{card_type}_{card_name}_{card_id}")()
    elif card_type == "program":
        return getattr(program, f"{card_type}_{card_name}_{card_id}")()
    elif card_type == "resource":
        return getattr(resource, f"{card_type}_{card_name}_{card_id}")()
    elif card_type == "upgrade":
        return getattr(upgrade, f"{card_type}_{card_name}_{card_id}")()
    else:
        print('unrecognized card type')
        print(card_type,card_name)
        sys.exit(-1)
