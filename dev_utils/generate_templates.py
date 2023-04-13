'''
loads the netrunnerDB all card json file (the one accessed through their API)
using that information, generates one python file per type of card
in each card type file is a class for each card that is a subclass of that base card type (defined in base_card_classes)
then generates a corresponding python test file to generate tests for each card class to validate functionality
also will copy the raw json information for each card into separate files organized by type for reference

WARNING: overwrites without impunity, keep output restricted to the generated_templates/ folder, then copy/paste as needed to prevent overwriting cards that have actually been implemented beyond these basic templates
'''

from netrunner_lib.variables import *
from netrunner_lib.cards._card_utilities import *

import json
from 
import os
import sys
from bs4 import BeautifulSoup
import re
from unidecode import unidecode
from datetime import datetime
from importlib import import_module

GENERATED_OUTPUT_PATH = pjo(BASE_PROJECT_PATH,"dev_utils","generated_templates")
if not os.path.exists(GENERATED_OUTPUT_PATH):
    os.mkdir(GENERATED_OUTPUT_PATH)

masterdata = {}

if not len(sys.argv)==2:
    print('provide arguments: [json,cards,card_tests,deck_types]')
    sys.exit(-1)

#####################
#load cardDB json file
print('loading card json db')
with open(CARD_DB_JSON_PATH, "r", encoding="UTF-8") as f:
    card_json_file_data = json.load(f)
    for file_card in card_json_file_data['data']:
        if file_card['type_code'] in masterdata:
            masterdata[file_card['type_code']].append(file_card)
        else:
            masterdata[file_card['type_code']] = [file_card]

if sys.argv[1] == "json":
    #####################
    #generate json reference files
    print('generating card json references by type')
    JSON_REF_PATH = pjo(GENERATED_OUTPUT_PATH,'json_ref')
    if not os.path.exists(JSON_REF_PATH):
        os.mkdir(JSON_REF_PATH)

    for typee in masterdata:
        with open(pjo(JSON_REF_PATH,f'type-data-{typee}.json'),'w') as outfl:
            outfl.write(json.dumps(masterdata[typee]))

elif sys.argv[1] == "cards":
    #####################
    #generate type files with base card class templates
    #`cp ../cards/generated_templates/card_types/* ../cards/`
    print('generating card class templates by type')
    CARD_TYPES_PATH = pjo(GENERATED_OUTPUT_PATH,'card_types')
    if not os.path.exists(CARD_TYPES_PATH):
        os.mkdir(CARD_TYPES_PATH)

    for typee in masterdata:
        with open(pjo(CARD_TYPES_PATH,f'{typee}.py'),'w') as outfl:
            #-------------
            outfl.write(f"""
'''
card classes of type {typee}
'''
from netrunner_lib.cards._base_card_classes import {typee.capitalize()}
from netrunner_lib.game_events import *
""")
            #^^^^^^^^^^^^^^
            for card in masterdata[typee]:
                #-------------
                outfl.write(f"""
class {typee}_{to_card_id(card['stripped_title'])}_{card['code']}({typee.capitalize()}):
    '''
    Cost: {card.get('cost','n/a')}
    Text: {card.get('stripped_text','n/a')}
    '''
    def __init__(self):
        super().__init__(r'''{json.dumps(card)}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {{self.title}} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"
""")
                #^^^^^^^^^^^^^^

elif sys.argv[1] == "card_tests":
    #####################
    #generate the test files templates for these cards
    print('generating test templates for card classes by type')
    CARD_TYPES_TEST_PATH = pjo(GENERATED_OUTPUT_PATH,'test_card_types')
    if not os.path.exists(CARD_TYPES_TEST_PATH):
        os.mkdir(CARD_TYPES_TEST_PATH)

    for typee in masterdata:
        with open(pjo(CARD_TYPES_TEST_PATH,f'test_{typee}.py'),'w') as outfl:
            #-------------
            outfl.write(f"""
'''
test cases for card classes of type {typee}
'''
import unittest

from netrunner_lib.cards._base_card_classes import {typee.capitalize()}
from netrunner_lib.cards.{typee} import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *

""")
            #^^^^^^^^^^^^^^
            for card in masterdata[typee]:
                #-------------
                outfl.write(f"""
######################
class Test_{to_card_id(card['stripped_title'])}_{card['code']}:

def test_play_card():
    '''
    testing play functionality of {to_card_id(card['stripped_title'])}
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("{typee}")

    test_card = {typee}_{to_card_id(card['stripped_title'])}_{card['code']}()
    test_card.play(test_game_environment.runner,test_game_environment)
""")
                #^^^^^^^^^^^^^^

elif sys.argv[1] == "card_implement_list":
    #####################
    #generate implementation list to track created cards
    print('generating implementation list to track created cards')
    IMPLEMENT_FILE_DIR = pjo(GENERATED_OUTPUT_PATH,"implementation_checklists")
    if not os.path.exists(IMPLEMENT_FILE_DIR):
        os.mkdir(IMPLEMENT_FILE_DIR)

    for typee in masterdata:
        type_filepath = pjo(IMPLEMENT_FILE_DIR,f'{typee}_checklist.md')
        if os.path.exists(type_filepath):
            continue
        with open(type_filepath,'w') as outfl:
            outfl.write(f"# {typee} Implementation Checklist\n\n")
            #-------------
            for card in masterdata[typee]:
                outfl.write(f"- [ ] {typee}_{to_card_id(card['stripped_title'])}_{card['code']}\n")
                outfl.write(f"- [ ] {typee}_{to_card_id(card['stripped_title'])}_{card['code']} TEST\n")
            #^^^^^^^^^^^^^^

elif sys.argv[1] == "deck_types":
    #####################
    #generate test decks for each type of card, each deck will have one identity and the corresponding cards of a type for the player type of that identity
    print('generating type decks for test environments')
    DECK_TYPES_PATH = pjo(GENERATED_OUTPUT_PATH,'deck_types_for_testing')
    if not os.path.exists(DECK_TYPES_PATH):
        os.mkdir(DECK_TYPES_PATH)

    # for typee in masterdata:
    #     with open(pjo(DECK_TYPES_PATH,f'test_{typee}.py'),'w') as outfl:
