import json
import os
import random
import json
import sys
import unittest
import math

random.seed(42)

from netrunner_lib.deck import Deck
from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.players import *

class TestPlayer(unittest.TestCase):
    '''
    test base player class
    some tests rely on certain ordering, in which case they create their own instance of the default player
    other tests that dont rely on ordering will use the default player created during setup
    '''
    def setup(self):
        self.player = Player('testPlayer1','starter-deck-runner-beginner.o8d')
        self.player.setup()
    
    def test_setup(self):
        self.player = Player('testPlayer1','starter-deck-runner-beginner.o8d')
        self.assert_(False)

    def test_setup_mulligan(self):
        self.player = Player('testPlayer1','starter-deck-runner-beginner.o8d')
        self.assert_(False)

    def test_draw_card(self):
        self.assert_(False)

    def test_get_deck(self):
        self.assert_(False)

    def test_get_hand(self):
        self.assert_(False)

    def test_get_discard(self):
        self.assert_(False)

    def test_prompt(self):
        self.assert_(False)

    def test_turn_action(self):
        self.assert_(False)

class TestRunner(unittest.TestCase):
    '''
    test runner player class
    some tests rely on certain ordering, in which case they create their own instance of a runner player
    other tests that dont rely on ordering will use the runner player created during setup
    '''
    def setup(self):
        self.player = Runner('testRunner1','starter-deck-runner-beginner.o8d')
    
    def test_setup(self):
        self.player = Runner('testRunner1','starter-deck-runner-beginner.o8d')
        self.assert_(False)

    def test_setup_mulligan(self):
        self.assert_(False)

    def test_draw_card(self):
        self.assert_(False)

    def test_get_deck(self):
        self.assert_(False)

    def test_get_hand(self):
        self.assert_(False)

    def test_get_discard(self):
        self.assert_(False)

    def test_prompt(self):
        self.assert_(False)
    
    def test_install_program(self):
        self.assert_(False)

    def test_install_hardware(self):
        self.assert_(False)

    def test_turn_action_start(self):
        self.player = Runner('testRunner1','starter-deck-runner-beginner.o8d')
        self.assert_(False)

    def test_turn_action_gain_credit(self):
        self.player = Runner('testRunner1','starter-deck-runner-beginner.o8d')
        self.assert_(False)

    def test_turn_action_draw_card(self):
        self.player = Runner('testRunner1','starter-deck-runner-beginner.o8d')
        self.assert_(False)
    
    def test_turn_action_play_card_easy_event(self):
        self.player = Runner('testRunner1','starter-deck-runner-beginner.o8d')
        self.assert_(False)

    def test_turn_action_invalid_action(self):
        self.player = Runner('testRunner1','starter-deck-runner-beginner.o8d')
        self.assert_(False)

    def test_turn_action_run_server(self):
        self.player = Runner('testRunner1','starter-deck-runner-beginner.o8d')
        self.assert_(False)

    def test_turn_action_discard(self):
        self.player = Runner('testRunner1','starter-deck-runner-beginner.o8d')
        self.assert_(False)

class TestServer(unittest.TestCase):
    '''
    test corpo server class
    '''
    def test_create_server(self):
        self.assert_(False)
    
    def test_install_ice(self):
        self.assert_(False)

    def test_install_upgrade(self):
        self.assert_(False)

class TestCorpo(unittest.TestCase):
    '''
    test corpo player class
    some tests rely on certain ordering, in which case they create their own instance of a corpo player
    other tests that dont rely on ordering will use the corpo player created during setup
    '''
    def setup(self):
        self.player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
    
    def test_setup(self):
        self.player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
        self.assert_(False)

    def test_setup_mulligan(self):
        self.player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
        self.assert_(False)

    def test_draw_card(self):
        self.assert_(False)

    def test_get_deck(self):
        self.assert_(False)

    def test_get_hand(self):
        self.assert_(False)

    def test_get_discard(self):
        self.assert_(False)

    def test_prompt(self):
        self.assert_(False)

    def test_turn_action_start(self):
        self.player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
        self.assert_(False)

    def test_turn_action_gain_credit(self):
        self.player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
        self.assert_(False)

    def test_turn_action_draw_card(self):
        self.player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
        self.assert_(False)
    
    def test_turn_action_play_card_easy_event(self):
        self.player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
        self.assert_(False)

    def test_turn_action_invalid_action(self):
        self.player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
        self.assert_(False)

    def test_turn_action_discard(self):
        self.player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
        self.assert_(False)
