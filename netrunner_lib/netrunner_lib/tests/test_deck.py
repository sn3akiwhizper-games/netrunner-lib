import json
import os
import random
import json
import sys

random.seed(42)

from netrunner_lib.cards import *
from netrunner_lib.deck import *

import unittest
import math

from netrunner_lib import deck

class TestDeck(unittest.TestCase):
    def test_to_card_id(self):
        self.assertEqual('noise_hacker_extraordinaire',to_card_id("Noise: Hacker Extraordinaire"),msg='noise hacker to_card_id failed')
        self.assertEqual('deja_vu',to_card_id("Déjà Vu"),msg='deja vu to_card_id failed')
        self.assertEqual('aesops_pawnshop',to_card_id("Aesop's Pawnshop"),msg='aesops pawnshop to_card_id failed')

    def test_load_o8n_file(self):
        '''
        test loading o8n files
        #deck2 quantities: id+3+2+3+1+2+3+2+3+2+2+2+2+1+2+2+2+3+3+2+3
        '''
        deck2_filename = 'starter-deck-runner-beginner.o8d'
        deck2 = Deck(deck2_filename, 'runner')
        #- test deck types
        self.assertIsInstance(deck2,Deck,msg='deck2 is not a Deck')
        self.assertEqual(deck2.deck_type,'runner',msg='deck2 type is not runner')
        self.assertEqual(deck2.identity_card.title,'Kate "Mac" McCaffrey: Digital Tinker',msg='deck2 identity card title not correct')

    def test_cards_unique_gids(self):
        '''
        testing unique game ID for same copies of cards
        '''
        deck2_filename = 'starter-deck-runner-beginner.o8d'
        deck2 = Deck(deck2_filename, 'runner')
        game_ids = {}
        for card in deck2.cards:
            if card.code in game_ids:
                game_ids[card.code].append(card.game_id)
            else:
                game_ids[card.code] = [card.game_id]

        for cardcode in game_ids:
            self.assertEqual(len(list(set(game_ids[cardcode]))),len(game_ids[cardcode]),msg=f'non-unique game IDs for cards: {game_ids[cardcode]}')

    def test_deck_shuffle(self):
        '''
        test deck card lengths
        '''
        deck2_filename = 'starter-deck-runner-beginner.o8d'
        deck2 = Deck(deck2_filename, 'runner')
        assert deck2.length() == 45, 'deck2 length != 45'
        print('deck2 attrs',dir(deck2))
        # print('deck2 dict',deck2.__dict__)
        #- test deck shuffle
        print('first couple deck2 cards',[str(x) for x in deck2.cards][:5])
        deck2.shuffle()
        print('first couple deck2 cardsafter shuffle',[str(x) for x in deck2.cards][:5])

    def test_deck_image_preferences(self):
        '''
        testing setting custom card image preferences
        '''
        deck2_filename = 'starter-deck-runner-beginner.o8d'
        deck2 = Deck(deck2_filename, 'runner')
        deck2.cards[0].print_details()
        print('test setting new image preference for first card')
        deck2.set_card_image_pref(deck2.cards[0].code,f"{deck2.cards[0].code}-custom.jpg")
        deck2.cards[0].print_details()
        assert deck2.cards[0].image_path == os.path.join(CARD_IMAGES_PATH,f"{deck2.cards[0].code}-custom.jpg"), 'deck2 card 0 image pref not set correctly'

    def test_save_deck_file_json(self):
        '''
        testing saving the customized deck file
        '''
        deck_filename = 'starter-deck-runner-beginner.o8d'
        deck = Deck(deck_filename, 'runner')
        deck.name
        print('test saving this deck to file')
        deck.save()
        assert os.path.isfile(os.path.join(CUSTOM_DECK_SAVE_PATH,f"{deck_filename.split('.')[0]}-customized-{datetime.now().strftime('%y-%m-%d')}.json")), 'saving customized deck2 failed'

    def test_load_custom_json(self):
        '''
        test loading the json file of the customized deck
        '''
        deck_filename = 'starter-deck-runner-beginner.o8d'
        deck = Deck(deck_filename, 'runner')
        deck2 = Deck(f"{deck_filename.split('.')[0]}-customized-{datetime.now().strftime('%y-%m-%d')}.json", 'runner')

        assert isinstance(deck2,Deck), 'deck3 not of type Deck'
        assert deck2.deck_type == 'runner', 'deck3 type is not runner'
        assert deck2.length() == 45, 'deck3 length is not 45'
        assert deck.identity_card.title == 'Kate "Mac" McCaffrey: Digital Tinker', 'deck3 identity card title not correct'

        #sort cards in both decks by code for comparison
        deck.cards.sort(key=lambda x: x.code)
        deck2.cards.sort(key=lambda x: x.code)
        for idx in range(len(deck.cards)):
            self.assertEqual(deck.cards[idx],deck2.cards[idx],f'sorted decks cards not equal: {deck.cards[idx]}!={deck2.cards[idx]}')
        
        #- test multiple card copies have unique game ids
        game_ids = {}
        for card in deck2.cards:
            if card.code in game_ids:
                game_ids[card.code].append(card.game_id)
            else:
                game_ids[card.code] = [card.game_id]
        for cardcode in game_ids:
            self.assertEqual(len(list(set(game_ids[cardcode]))),len(game_ids[cardcode]),msg=f'non-unique game IDs for cards: {game_ids[cardcode]}')
