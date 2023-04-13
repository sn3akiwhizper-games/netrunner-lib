
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.deck import *
from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.cards._card_utilities import *
from netrunner_lib.variables import *

def initialize_test_environment(test_set:str) -> NetrunnerGame:
    '''
    setup a test environment for a specific type of cards
    '''
    corpo = Corpo(f"test-{test_set}-corpo-deck.json")
    runner = Runner(f"test-{test_set}-corpo-deck.json")
    test_game_state = NetrunnerGame(corpo,runner)

    return test_game_state

def create_test_deck(name:str, deck_type:str, identity_code:str, card_code_list:list) -> Deck:
    '''
    create a test deck from a card code list
    '''
    deck = TestDeck(name,deck_type, identity_code)
    ##############################################
    #use info from od8 file to load actual card info from json DB
    card_json_db = {}
    with open(CARD_DB_JSON_PATH, "r", encoding="UTF-8") as f:
        card_json_file_data = json.load(f)
        for file_card in card_json_file_data['data']:
            # print(file_card)
            card_json_db[file_card['code']] = file_card
    
    ##read identity card json info
    # print('-------')
    identity_code = deck_dict['sections']['Identity'][0]['id'][-5:]
    identity_card_info = card_json_db[identity_code]
    #create_card(card_name:str,card_type:str,card_id:str)
    self.identity_card = create_card(
            to_card_id(identity_card_info['stripped_title']),
            identity_card_info['type_code'],
            identity_card_info['code']
        )

    ##read all the other card's json info
    for deck_card in deck_dict['sections']['R&D / Stack']:
        card_info = card_json_db[deck_card['id'][-5:]]
        for _ in range(deck_card['qty']):
            self.cards.append(
                create_card(
                    to_card_id(card_info['stripped_title']),
                    card_info['type_code'],
                    card_info['code']
                )
            )
    for card in card_code_list:

