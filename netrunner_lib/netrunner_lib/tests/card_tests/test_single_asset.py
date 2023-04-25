
'''
test cases for card classes of type asset
'''
import unittest

from netrunner_lib.cards._base_card_classes import Asset
from netrunner_lib.cards.asset import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *
from netrunner_lib.cards._card_utilities import *

######################
class Test_adonis_campaign_01056(unittest.TestCase):
    '''
    testing play functionality of adonis_campaign
    Cost: 4
    Text: Put 12 credits from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it. Take 3 credits from Adonis Campaign when your turn begins.
    '''

    def setUp(self):
        '''
        setup test environment for adonis_campaign_01056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        # self.runner_player.hand = []
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        self.corpo_player.deck.cards = [
                    create_card(
                        card_name=to_card_id("Adonis Campaign"),
                        card_type="asset",
                        card_id="01056"
                    ),
                    create_card(
                        card_name=to_card_id("Adonis Campaign"),
                        card_type="asset",
                        card_id="01056"
                    ),
                    create_card(
                        card_name=to_card_id("Adonis Campaign"),
                        card_type="asset",
                        card_id="01056"
                    ),
                    create_card(
                        card_name=to_card_id("Adonis Campaign"),
                        card_type="asset",
                        card_id="01056"
                    ),
                    create_card(
                        card_name=to_card_id("Adonis Campaign"),
                        card_type="asset",
                        card_id="01056"
                    ),
                    create_card(
                        card_name=to_card_id("Adonis Campaign"),
                        card_type="asset",
                        card_id="01056"
                    ),
                    create_card(
                        card_name=to_card_id("Adonis Campaign"),
                        card_type="asset",
                        card_id="01056"
                    ),
        ]
        self.corpo_player.hand = [
                    create_card(
                        card_name=to_card_id("Adonis Campaign"),
                        card_type="asset",
                        card_id="01056"
                    ),
                    create_card(
                        card_name=to_card_id("Adonis Campaign"),
                        card_type="asset",
                        card_id="01056"
                    ),
        ]
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
        self.test_game_environment.current_player=self.corpo_player
        self.corpo_player.credit_pool = 5
        self.test_game_environment.print_state()
    
    def test_play_card(self):
        '''
        Test playing the adonis campaign asset card, making sure we have enough credits for it, and that it adds to the corpo credit pool at the start of their turn. then make sure it trashes itself when all it's credits are used up
        '''
        ###################################################
        #play the card
        self.corpo_player.print_player_details()
        debug_print('playing adonis campaign card',1)
        track_turn_state = self.corpo_player.do_turn_actions(turn_state="start",game_manager=self.test_game_environment)
        track_turn_state = self.corpo_player.do_turn_actions(turn_state=track_turn_state,turn_action="play_card",source="hand",hand_index=0,game_manager=self.test_game_environment)
        self.assertEqual(len(self.corpo_player.remote_servers),1,f"remote server length mismatch: '{len(self.corpo_player.remote_servers)}' expected '1'")
        self.assertEqual(self.corpo_player.clicks,2,f"corpo click tracker mismatch: '{self.corpo_player.clicks}' expected '2'")

        self.corpo_player.print_player_details()

        ###################################################
        #rez the newly installed card
        debug_print('rezzing adonis campaign card',1)
        rez_result = self.corpo_player.remote_servers[-1].root.rez(self.corpo_player)

        self.assertEqual(rez_result,"rezzed",f"invalid rez result: '{rez_result}' expected 'rezzed'")
        self.assertEqual(self.corpo_player.credit_pool,1,f"invalid corpo credit pool after rez: '{self.corpo_player.credit_pool}' expected '1'")
        self.assertEqual(self.corpo_player.remote_servers[-1].root.credit_pool,12,f"invalid asset card credit pool after rez: '{self.corpo_player.remote_servers[-1].root.credit_pool}' expected '12'")

        ###################################################
        #try to play a second card that we can't afford
        debug_print(f'trying to play adonis campaign card we cant afford: state={track_turn_state}',1)
        track_turn_state = self.corpo_player.do_turn_actions(turn_state=track_turn_state,turn_action="play_card",source="hand",hand_index=0,game_manager=self.test_game_environment)
        self.assertEqual(self.corpo_player.clicks,2,f"corpo click tracker mismatch: '{self.corpo_player.clicks}' expected '2'")

        ###################################################
        # self.test_game_environment.print_state()

        #start corpo's next turn to execute "start of turn" event
        debug_print('starting new corpo turn',1)
        track_turn_state = self.corpo_player.do_turn_actions(turn_state="start",game_manager=self.test_game_environment)

        self.assertEqual(self.corpo_player.remote_servers[-1].root.credit_pool,9,f"invalid asset card credit pool after turn start: '{self.corpo_player.remote_servers[-1].root.credit_pool}' expected '9'")
        self.assertEqual(self.corpo_player.credit_pool,4,f"invalid corpo credit pool after start of turn: '{self.corpo_player.credit_pool}' expected '4'")
        
        ###################################################
        # do a couple turns to use up all the credits on the card and make sure it trashes itself
        track_turn_state = self.corpo_player.do_turn_actions(turn_state="start",game_manager=self.test_game_environment)
        self.assertEqual(self.corpo_player.remote_servers[-1].root.credit_pool,6,f"invalid asset card credit pool after turn start: '{self.corpo_player.remote_servers[-1].root.credit_pool}' expected '6'")
        track_turn_state = self.corpo_player.do_turn_actions(turn_state="start",game_manager=self.test_game_environment)
        self.assertEqual(self.corpo_player.remote_servers[-1].root.credit_pool,3,f"invalid asset card credit pool after turn start: '{self.corpo_player.remote_servers[-1].root.credit_pool}' expected '3'")
        track_turn_state = self.corpo_player.do_turn_actions(turn_state="start",game_manager=self.test_game_environment)
        self.assertEqual(len(self.corpo_player.remote_servers),0,f"remote server length mismatch: '{len(self.corpo_player.remote_servers)}' expected '0'")
