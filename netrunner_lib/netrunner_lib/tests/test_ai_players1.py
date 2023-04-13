import json
import os
import random
import json
import sys
import unittest
import math

random.seed(42)

from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.players import Runner

class TestPlayer(unittest.TestCase):
    '''
    test base player class
    '''
    def setup(self):
        self.card = Card(r'''{"code": "01019", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"Hey kid, you fire that up now, bound to be vamped real bad. Some real pathetic individuals around here. But thankfully I got just the ticket\u2026\"", "illustrator": "Matt Zeilinger", "keywords": "Job", "pack_code": "core", "position": 19, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 3 credits.", "stripped_title": "Easy Mark", "text": "Gain 3[credit].", "title": "Easy Mark", "type_code": "event", "uniqueness": false}''')
        self.player = Runner()
    
    def test_play_card(self):
        self.assert_(False)

    def test_get_card_index(self):
        self.assert_(False)

    def test_trash_card(self):
        self.assert_(False)
