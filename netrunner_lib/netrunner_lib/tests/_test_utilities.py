
import json

from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.deck import *
from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.cards._card_utilities import *
from netrunner_lib import variables as vars
from netrunner_lib import errors

def initialize_test_environment(test_set:str) -> NetrunnerGame:
    '''
    setup a test environment for a specific type of cards
    '''
    corpo = Corpo(f"test-{test_set}-corpo-deck.json")
    runner = Runner(f"test-{test_set}-corpo-deck.json")
    test_game_state = NetrunnerGame(corpo,runner)

    return test_game_state

def create_test_deck(name:str, deck_type:str, identity_code:str, card_code_list:list[str]) -> Deck:
    '''
    create a test deck from a card code list
    INPUT:
        - name:str name of test deck
        - deck_type:str is this a runner or corpo deck
        - identity_code:str card_code of identity to use
        - carde_code_list:list[str] list of card_code's to include in the deck
    RETURN:
    '''
    #create deck object, catching raised error to bypass fake filename provided
    try:
        deck = Deck(name,deck_type, identity_code)
    except errors.INVALID_FILE_EXTENSION:
        pass

    ##############################################
    #use info from od8 file to load actual card info from json DB
    card_json_db = {}
    with open(vars.CARD_DB_JSON_PATH, "r", encoding="UTF-8") as f:
        card_json_file_data = json.load(f)
        for file_card in card_json_file_data['data']:
            # print(file_card)
            card_json_db[file_card['code']] = file_card
