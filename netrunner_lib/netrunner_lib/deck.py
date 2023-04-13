import json
import os
import random
import json
import sys
from bs4 import BeautifulSoup
import re
from unidecode import unidecode
from datetime import datetime
from importlib import import_module

from netrunner_lib.variables import *

from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.cards._card_utilities import *

class Deck:
    def __init__(self, deck_filepath, deck_type):
        '''
        create an instance of a deck and load the cards
        deck_filepath should only be a filename, full path generated on create
        on create will:
        1. load the deck list from file
        2. generate the proper paths for the card images based on preferences
        '''
        self.name = deck_filepath.split('.')[0]#remove file extension to save name of deck
        self.deck_filepath:str = os.path.join(DECKLIST_PATH,deck_filepath)
        self.date_created:str = None
        self.deck_type:str = deck_type
        self.identity_card:Card = None
        self.cards:list[Card] = []
        self.card_image_preferences:dict = {}

        print('loading deck',deck_filepath)
        if ".txt" in self.deck_filepath:
            self._load_txt_deckfile(self.deck_filepath)
        elif ".o8d" in self.deck_filepath:
            self._load_o8d_deckfile(self.deck_filepath)
        elif ".json" in self.deck_filepath:
            self._load_json_deckfile(self.deck_filepath)
        else:
            print('error loading deck file: invalid file extension')
            sys.exit(-1)

    def _load_o8d_deckfile(self,deck_path:str):
        if not os.path.exists(deck_path):
            print("deck path doesn't exist")
            sys.exit(-1)
        
        ##############################################
        #loading info from o8d file
        with open(deck_path, 'r') as infl:
            o8d_data = infl.read()
        soup = BeautifulSoup(o8d_data, 'xml')

        # Extract game ID from the deck tag
        game_id = soup.deck['game']

        # Create dictionary to store deck sections and cards
        deck_dict = {'game_id': game_id, 'sections': {}}
        
        # Extract card quantities and IDs for each section
        for section in soup.find_all('section'):
            section_name = section['name']
            card_data = []
            for card in section.find_all('card'):
                card_data.append({
                    "id":card['id'],
                    "qty":int(card['qty']),
                    "name":card.text
                })
            deck_dict['sections'][section_name] = card_data
        # print(deck_dict)

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
        ##############################################
        #load default card images
        self._load_image_preferences()

    def _load_json_deckfile(self,deck_path:str):
        if not os.path.exists(deck_path):
            print("deck path doesn't exist")
            sys.exit(-1)

        ##############################################
        #loading info from json file
        with open(deck_path, "r") as f:
            deck_data = json.load(f)
            self.date_created = deck_data["date_created"]
            self.deck_type = deck_data["type"]
            self.identity_card = deck_data['identity_card']
            self.cards = [switch_card_type(x) for x in deck_data["cards"]]
            self.card_image_preferences = deck_data['card_image_preferences']

        # Load card information from JSON files and create card instances
        # for card_id in self.cards:
        #     card_file_path = f"{card_id}.json"
        #     if os.path.exists(card_file_path):
        #         with open(card_file_path, "r") as f:
        #             card_data = json.load(f)

        #             for _ in range(card['qty']):
        #                 self.cards.append(switch_card_type(card_json_data))
        ##############################################
        #load default card images
        self._load_image_preferences()
    
    def _load_image_preferences(self):
        '''
        generate the complete path to the local card image
        if no preference is set, use the default image for that card and set that as the preference
        card_preference will be a filename for the preferred art
        default card filename should be same as card_id
        '''
        for card in self.cards:
            # print('checking image for card: ',card)
            if not card.code in self.card_image_preferences:
                self.card_image_preferences[card.code] = f"{card.code}.jpg"
            
            card.image_path = os.path.join(CARD_IMAGES_PATH,f"{self.card_image_preferences[card.code]}")
    
    def shuffle(self):
        random.shuffle(self.cards)

    def remove_card(self, card_game_id:int):
        '''
        remove a card based on its unique game ID
        '''
        for idx, card in enumerate(self.cards):
            if card.game_id == card_game_id:
                self.cards.pop(idx)
                break
    
    def length(self) -> int:
        '''
        return length of the current
        '''
        return len(self.cards)

    def set_card_image_pref(self, card_code:int, image_file:str):
        '''
        save new preference for a card_id and reload information for affected cards
        mark deck name as customized to prevent overwriting other saved decks
        '''
        self.card_image_preferences[card_code] = image_file
        self.name = f"{self.name}-customized"
        self._load_image_preferences()
    
    def save(self):
        '''
        only save one version 
        '''
        deck_data = {
            "name": self.name, 
            "date_created": self.date_created, 
            "type": self.deck_type, 
            "identity_card": self.identity_card.__dict__,
            "cards": [x.__dict__ for x in self.cards],
            "card_image_preferences": self.card_image_preferences
        }
        save_deck_filepath = os.path.join(CUSTOM_DECK_SAVE_PATH,f"{self.name}-{datetime.now().strftime('%y-%m-%d')}.json")
        if os.path.isfile(save_deck_filepath):
            print('>>warning: custom save file already exists')
        with open(save_deck_filepath, "w") as f:
            json.dump(deck_data, f)

class TestDeck(Deck):
    def __init__(self,name,deck_type):
        self.name = name
        self.deck_filepath = f"test-deck-{name}"
        self.date_created:str = None
        self.deck_type:str = deck_type
        self.identity_card:Card = None
        self.cards:list[Card] = []
        self.card_image_preferences:dict = {}
