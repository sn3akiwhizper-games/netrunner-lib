
'''
test cases for card classes of type asset
'''
import unittest

from netrunner_lib.cards._base_card_classes import Asset
from netrunner_lib.cards.asset import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


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

######################
class Test_aggressive_secretary_01057(unittest.TestCase):
    '''
    testing play functionality of aggressive_secretary
    Cost: 0
    Text: Aggressive Secretary can be advanced. If you pay 2 credits when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.
    '''

    def setUp(self):
        '''
        setup test environment for aggressive_secretary_01057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_aggressive_secretary_01057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_junebug_01069(unittest.TestCase):
    '''
    testing play functionality of project_junebug
    Cost: 0
    Text: Project Junebug can be advanced. If you pay 1 credit when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.
    '''

    def setUp(self):
        '''
        setup test environment for project_junebug_01069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_project_junebug_01069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_snare_01070(unittest.TestCase):
    '''
    testing play functionality of snare
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for snare_01070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_snare_01070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zaibatsu_loyalty_01071(unittest.TestCase):
    '''
    testing play functionality of zaibatsu_loyalty
    Cost: 0
    Text: Interrupt -> When a card would be exposed, you may rez this asset. Interrupt -> 1 credit or trash: Prevent 1 card from being exposed.
    '''

    def setUp(self):
        '''
        setup test environment for zaibatsu_loyalty_01071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_zaibatsu_loyalty_01071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ghost_branch_01087(unittest.TestCase):
    '''
    testing play functionality of ghost_branch
    Cost: 0
    Text: Ghost Branch can be advanced. When the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.
    '''

    def setUp(self):
        '''
        setup test environment for ghost_branch_01087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ghost_branch_01087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_security_subcontract_01096(unittest.TestCase):
    '''
    testing play functionality of security_subcontract
    Cost: 0
    Text: click, trash a rezzed piece of ice: Gain 4 credits.
    '''

    def setUp(self):
        '''
        setup test environment for security_subcontract_01096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_security_subcontract_01096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_melange_mining_corp_01108(unittest.TestCase):
    '''
    testing play functionality of melange_mining_corp
    Cost: 1
    Text: click, click, click: Gain 7 credits.
    '''

    def setUp(self):
        '''
        setup test environment for melange_mining_corp_01108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_melange_mining_corp_01108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pad_campaign_01109(unittest.TestCase):
    '''
    testing play functionality of pad_campaign
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for pad_campaign_01109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_pad_campaign_01109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_encryption_protocol_02029(unittest.TestCase):
    '''
    testing play functionality of encryption_protocol
    Cost: 0
    Text: The trash cost of all installed cards is increased by 1.
    '''

    def setUp(self):
        '''
        setup test environment for encryption_protocol_02029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_encryption_protocol_02029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_edge_of_world_02053(unittest.TestCase):
    '''
    testing play functionality of edge_of_world
    Cost: 0
    Text: When the Runner accesses this asset while it is installed, you may pay 3 credits. If you do, do 1 core damage for each piece of ice protecting this server.
    '''

    def setUp(self):
        '''
        setup test environment for edge_of_world_02053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_edge_of_world_02053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marked_accounts_02055(unittest.TestCase):
    '''
    testing play functionality of marked_accounts
    Cost: 0
    Text: When your turn begins, take 1 credit from Marked Accounts, if able. click: Place 3 credits from the bank on Marked Accounts.
    '''

    def setUp(self):
        '''
        setup test environment for marked_accounts_02055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_marked_accounts_02055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_private_contracts_02059(unittest.TestCase):
    '''
    testing play functionality of private_contracts
    Cost: 3
    Text: Place 14 credits from the bank on Private Contracts when it is rezzed. When there are no credits left on Private Contracts, trash it. click: Take 2 credits from Private Contracts.
    '''

    def setUp(self):
        '''
        setup test environment for private_contracts_02059
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_private_contracts_02059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dedicated_server_02072(unittest.TestCase):
    '''
    testing play functionality of dedicated_server
    Cost: 3
    Text: 2 recurring credits Use these credits to rez ice.
    '''

    def setUp(self):
        '''
        setup test environment for dedicated_server_02072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_dedicated_server_02072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_net_police_02075(unittest.TestCase):
    '''
    testing play functionality of net_police
    Cost: 1
    Text: X recurring credits Use these credits during traces. X is the number of links the Runner has.
    '''

    def setUp(self):
        '''
        setup test environment for net_police_02075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_net_police_02075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_eve_campaign_02092(unittest.TestCase):
    '''
    testing play functionality of eve_campaign
    Cost: 5
    Text: Place 16 credits from the bank on Eve Campaign when it is rezzed. When there are no credits left on Eve Campaign, trash it. When your turn begins, take 2 credits from Eve Campaign.
    '''

    def setUp(self):
        '''
        setup test environment for eve_campaign_02092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_eve_campaign_02092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ronin_02112(unittest.TestCase):
    '''
    testing play functionality of ronin
    Cost: 0
    Text: You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.
    '''

    def setUp(self):
        '''
        setup test environment for ronin_02112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ronin_02112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dedicated_response_team_02118(unittest.TestCase):
    '''
    testing play functionality of dedicated_response_team
    Cost: 2
    Text: If the Runner is tagged, Dedicated Response Team gains "Whenever a successful run ends, do 2 meat damage."
    '''

    def setUp(self):
        '''
        setup test environment for dedicated_response_team_02118
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_dedicated_response_team_02118()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_alix_t4lb07_03008(unittest.TestCase):
    '''
    testing play functionality of alix_t4lb07
    Cost: 1
    Text: Place 1 power counter on Alix T4LB07 whenever you install a card. click,trash: Gain 2 credits for each power counter on Alix T4LB07.
    '''

    def setUp(self):
        '''
        setup test environment for alix_t4lb07_03008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_alix_t4lb07_03008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cerebral_overwriter_03009(unittest.TestCase):
    '''
    testing play functionality of cerebral_overwriter
    Cost: 0
    Text: You can advance this asset. When the Runner accesses this asset while it is installed, you may pay 3 credits. If you do, do 1 core damage for each hosted advancement counter.
    '''

    def setUp(self):
        '''
        setup test environment for cerebral_overwriter_03009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_cerebral_overwriter_03009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_director_haas_03010(unittest.TestCase):
    '''
    testing play functionality of director_haas
    Cost: 3
    Text: You get +1 allotted click for each of your turns. When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.
    '''

    def setUp(self):
        '''
        setup test environment for director_haas_03010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_director_haas_03010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_haas_arcology_ai_03011(unittest.TestCase):
    '''
    testing play functionality of haas_arcology_ai
    Cost: 2
    Text: Haas Arcology AI can be advanced only while unrezzed. click, hosted advancement token: Gain click click. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for haas_arcology_ai_03011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_haas_arcology_ai_03011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_thomas_haas_03012(unittest.TestCase):
    '''
    testing play functionality of thomas_haas
    Cost: 1
    Text: Thomas Haas can be advanced. trash: Gain 2 credits for each advancement token on Thomas Haas.
    '''

    def setUp(self):
        '''
        setup test environment for thomas_haas_03012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_thomas_haas_03012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_levy_university_03024(unittest.TestCase):
    '''
    testing play functionality of levy_university
    Cost: 3
    Text: click, 1 credit: Search R&D for a piece of ice, reveal it, and add it to HQ. Shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for levy_university_03024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_levy_university_03024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_server_diagnostics_03025(unittest.TestCase):
    '''
    testing play functionality of server_diagnostics
    Cost: 3
    Text: Gain 2 credits when your turn begins. Trash Server Diagnostics when you install a piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for server_diagnostics_03025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_server_diagnostics_03025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_jackson_howard_04015(unittest.TestCase):
    '''
    testing play functionality of jackson_howard
    Cost: 0
    Text: click: Draw 2 cards. Remove Jackson Howard from the game: Shuffle up to 3 cards from Archives into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for jackson_howard_04015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_jackson_howard_04015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_elizabeth_mills_04037(unittest.TestCase):
    '''
    testing play functionality of elizabeth_mills
    Cost: 2
    Text: When you rez Elizabeth Mills, remove 1 bad publicity. click, trash: Trash 1 location. Take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for elizabeth_mills_04037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_elizabeth_mills_04037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_isabel_mcguire_04050(unittest.TestCase):
    '''
    testing play functionality of isabel_mcguire
    Cost: 0
    Text: click: Add 1 of your installed cards to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for isabel_mcguire_04050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_isabel_mcguire_04050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sundew_04054(unittest.TestCase):
    '''
    testing play functionality of sundew
    Cost: 2
    Text: The first time the Runner spends 1 or more click during their turn, gain 2 credits. If those click were spent to take an action, the first time during that action a run on this server begins, pay 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for sundew_04054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_sundew_04054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_city_surveillance_04055(unittest.TestCase):
    '''
    testing play functionality of city_surveillance
    Cost: 5
    Text: When the Runner's turn begins, give them 1 tag unless they pay 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for city_surveillance_04055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_city_surveillance_04055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rex_campaign_04070(unittest.TestCase):
    '''
    testing play functionality of rex_campaign
    Cost: 1
    Text: Place 3 power counters on Rex Campaign when it is rezzed. When there are no power counters left on Rex Campaign, trash it and either remove 1 bad publicity or gain 5 credits. When your turn begins, remove 1 power counter from Rex Campaign.
    '''

    def setUp(self):
        '''
        setup test environment for rex_campaign_04070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_rex_campaign_04070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shock_04073(unittest.TestCase):
    '''
    testing play functionality of shock
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for shock_04073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_shock_04073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_toshiyuki_sakai_04092(unittest.TestCase):
    '''
    testing play functionality of toshiyuki_sakai
    Cost: 0
    Text: Toshiyuki Sakai can be advanced. If Toshiyuki Sakai is accessed while installed, you may swap him with an agenda or asset from HQ. The new agenda or asset is installed unrezzed, and keeps all advancement tokens on Toshiyuki Sakai. The Runner can choose not to access the new card.
    '''

    def setUp(self):
        '''
        setup test environment for toshiyuki_sakai_04092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_toshiyuki_sakai_04092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_grndl_refinery_04099(unittest.TestCase):
    '''
    testing play functionality of grndl_refinery
    Cost: 0
    Text: GRNDL Refinery can be advanced. click, trash: Gain 4 credits for each advancement token on GRNDL Refinery.
    '''

    def setUp(self):
        '''
        setup test environment for grndl_refinery_04099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_grndl_refinery_04099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_broadcast_square_04112(unittest.TestCase):
    '''
    testing play functionality of broadcast_square
    Cost: 2
    Text: Whenever you are about to take at least 1 bad publicity, Trace[3]. If successful, avoid taking the bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for broadcast_square_04112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_broadcast_square_04112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chairman_hiro_05008(unittest.TestCase):
    '''
    testing play functionality of chairman_hiro
    Cost: 2
    Text: The Runner gets -2 maximum hand size.
When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.
    '''

    def setUp(self):
        '''
        setup test environment for chairman_hiro_05008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_chairman_hiro_05008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mental_health_clinic_05009(unittest.TestCase):
    '''
    testing play functionality of mental_health_clinic
    Cost: 0
    Text: Gain 1 credit when your turn begins. The Runner's maximum hand size is increased by 1.
    '''

    def setUp(self):
        '''
        setup test environment for mental_health_clinic_05009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_mental_health_clinic_05009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_psychic_field_05010(unittest.TestCase):
    '''
    testing play functionality of psychic_field
    Cost: 0
    Text: If the Runner exposes or accesses Psychic Field while installed, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, do 1 net damage for each card in the Runner's grip.
    '''

    def setUp(self):
        '''
        setup test environment for psychic_field_05010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_psychic_field_05010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shikyu_05011(unittest.TestCase):
    '''
    testing play functionality of shikyu
    Cost: 0
    Text: When the Runner accesses this asset anywhere except in R&D, you may pay X credits. The Runner must either suffer X net damage or add this asset to their score area as an agenda worth -1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for shikyu_05011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_shikyu_05011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tenma_line_05012(unittest.TestCase):
    '''
    testing play functionality of tenma_line
    Cost: 2
    Text: click: Swap 2 pieces of installed ice.
    '''

    def setUp(self):
        '''
        setup test environment for tenma_line_05012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_tenma_line_05012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_plan_b_05023(unittest.TestCase):
    '''
    testing play functionality of plan_b
    Cost: 0
    Text: Plan B can be advanced. If the Runner accesses Plan B, you may reveal and score an agenda from HQ with an advancement requirement equal to or less than the number of advancement tokens on Plan B.
    '''

    def setUp(self):
        '''
        setup test environment for plan_b_05023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_plan_b_05023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_primary_transmission_dish_06006(unittest.TestCase):
    '''
    testing play functionality of primary_transmission_dish
    Cost: 2
    Text: 3 recurring credits Use these credits during traces.
    '''

    def setUp(self):
        '''
        setup test environment for primary_transmission_dish_06006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_primary_transmission_dish_06006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_root_06008(unittest.TestCase):
    '''
    testing play functionality of the_root
    Cost: 6
    Text: 3 recurring credits Use these credits to advance, install, and rez cards.
    '''

    def setUp(self):
        '''
        setup test environment for the_root_06008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_the_root_06008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sealed_vault_06029(unittest.TestCase):
    '''
    testing play functionality of sealed_vault
    Cost: 0
    Text: 1 credit: Move any number of credits from your credit pool to this asset. click: Take any number of credits from this asset. trash: Take any number of credits from this asset.
    '''

    def setUp(self):
        '''
        setup test environment for sealed_vault_06029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_sealed_vault_06029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_elizas_toybox_06042(unittest.TestCase):
    '''
    testing play functionality of elizas_toybox
    Cost: 4
    Text: click,click,click: Rez a card, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for elizas_toybox_06042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_elizas_toybox_06042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_news_now_hour_06045(unittest.TestCase):
    '''
    testing play functionality of the_news_now_hour
    Cost: 0
    Text: The Runner cannot play current events.
    '''

    def setUp(self):
        '''
        setup test environment for the_news_now_hour_06045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_the_news_now_hour_06045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shattered_remains_06050(unittest.TestCase):
    '''
    testing play functionality of shattered_remains
    Cost: 0
    Text: Shattered Remains can be advanced. If you pay 1 credit when the Runner accesses Shattered Remains, trash 1 piece of hardware for each advancement token on Shattered Remains.
    '''

    def setUp(self):
        '''
        setup test environment for shattered_remains_06050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_shattered_remains_06050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reversed_accounts_06066(unittest.TestCase):
    '''
    testing play functionality of reversed_accounts
    Cost: 0
    Text: You can advance this asset. click, trash: The Runner loses 4 credits for each hosted advancement counter.
    '''

    def setUp(self):
        '''
        setup test environment for reversed_accounts_06066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_reversed_accounts_06066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_docklands_crackdown_06072(unittest.TestCase):
    '''
    testing play functionality of docklands_crackdown
    Cost: 2
    Text: click, click: Place 1 power counter on Docklands Crackdown. The install cost of the first card the Runner installs each turn is increased by 1 for each power counter on Docklands Crackdown.
    '''

    def setUp(self):
        '''
        setup test environment for docklands_crackdown_06072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_docklands_crackdown_06072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hostile_infrastructure_06083(unittest.TestCase):
    '''
    testing play functionality of hostile_infrastructure
    Cost: 5
    Text: Whenever the Runner trashes a Corp card (including Hostile Infrastructure), do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for hostile_infrastructure_06083
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_hostile_infrastructure_06083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_daily_business_show_06086(unittest.TestCase):
    '''
    testing play functionality of daily_business_show
    Cost: 2
    Text: Interrupt -> The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for daily_business_show_06086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_daily_business_show_06086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_executive_boot_camp_06088(unittest.TestCase):
    '''
    testing play functionality of executive_boot_camp
    Cost: 0
    Text: When your turn begins, you may rez a card, lowering the rez cost by 1 credit. 1 credit,trash: Search R&D for an asset, reveal it, and add it to HQ. Shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for executive_boot_camp_06088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_executive_boot_camp_06088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_it_department_06103(unittest.TestCase):
    '''
    testing play functionality of it_department
    Cost: 2
    Text: click: Place 1 power counter on IT Department. Hosted power counter: Choose a rezzed piece of ice. That ice has +1 strength until the end of the turn for each power counter (including the one spent) on IT Department.
    '''

    def setUp(self):
        '''
        setup test environment for it_department_06103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_it_department_06103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_turtlebacks_06106(unittest.TestCase):
    '''
    testing play functionality of turtlebacks
    Cost: 2
    Text: Gain 1 credit whenever you create a server.
    '''

    def setUp(self):
        '''
        setup test environment for turtlebacks_06106
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_turtlebacks_06106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_constellation_protocol_07008(unittest.TestCase):
    '''
    testing play functionality of constellation_protocol
    Cost: 0
    Text: When your turn begins, you may move an advancement token from a piece of ice to an installed piece of ice that can be advanced.
    '''

    def setUp(self):
        '''
        setup test environment for constellation_protocol_07008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_constellation_protocol_07008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mark_yale_07009(unittest.TestCase):
    '''
    testing play functionality of mark_yale
    Cost: 1
    Text: Whenever you spend an agenda counter, gain 1 credit. trash or any agenda counter: Gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for mark_yale_07009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_mark_yale_07009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_space_camp_07010(unittest.TestCase):
    '''
    testing play functionality of space_camp
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, you may place 1 advancement counter on an installed card you can advance.
    '''

    def setUp(self):
        '''
        setup test environment for space_camp_07010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_space_camp_07010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_board_07011(unittest.TestCase):
    '''
    testing play functionality of the_board
    Cost: 3
    Text: Each agenda in the Runner's score area is worth 1 less agenda point. When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.
    '''

    def setUp(self):
        '''
        setup test environment for the_board_07011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_the_board_07011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_braintaping_warehouse_08010(unittest.TestCase):
    '''
    testing play functionality of braintaping_warehouse
    Cost: 1
    Text: The rez cost of bioroid ice is lowered by 1 for each unspent click the Runner has.
    '''

    def setUp(self):
        '''
        setup test environment for braintaping_warehouse_08010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_braintaping_warehouse_08010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_capital_investors_08018(unittest.TestCase):
    '''
    testing play functionality of capital_investors
    Cost: 2
    Text: click: Gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for capital_investors_08018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_capital_investors_08018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tech_startup_08020(unittest.TestCase):
    '''
    testing play functionality of tech_startup
    Cost: 0
    Text: When your turn begins, you may trash Tech Startup. If you do, search R&D for an asset, reveal it, and install it. Shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for tech_startup_08020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_tech_startup_08020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_blacklist_08036(unittest.TestCase):
    '''
    testing play functionality of blacklist
    Cost: 0
    Text: Cards cannot leave the Runner's heap for any reason.
    '''

    def setUp(self):
        '''
        setup test environment for blacklist_08036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_blacklist_08036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_student_loans_08038(unittest.TestCase):
    '''
    testing play functionality of student_loans
    Cost: 2
    Text: As an additional cost to play an event, if there is a copy of that event in the heap, the Runner must pay 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for student_loans_08038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_student_loans_08038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_town_08059(unittest.TestCase):
    '''
    testing play functionality of corporate_town
    Cost: 1
    Text: As an additional cost to rez this asset, forfeit 1 agenda. When your turn begins, you may trash 1 installed resource. Trashing a resource this way cannot be prevented.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_town_08059
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_corporate_town_08059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_test_ground_08071(unittest.TestCase):
    '''
    testing play functionality of test_ground
    Cost: 0
    Text: Test Ground can be advanced. trash: Derez 1 card for each advancement token on Test Ground.
    '''

    def setUp(self):
        '''
        setup test environment for test_ground_08071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_test_ground_08071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_allele_repression_08073(unittest.TestCase):
    '''
    testing play functionality of allele_repression
    Cost: 2
    Text: Allele Repression can be advanced. trash: Swap 1 card in HQ with 1 card in Archives for each advancement token on Allele Repression.
    '''

    def setUp(self):
        '''
        setup test environment for allele_repression_08073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_allele_repression_08073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_expose_08075(unittest.TestCase):
    '''
    testing play functionality of expose
    Cost: 2
    Text: Expose can be advanced. trash: Remove 1 bad publicity for each advancement token on Expose.
    '''

    def setUp(self):
        '''
        setup test environment for expose_08075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_expose_08075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_contract_killer_08078(unittest.TestCase):
    '''
    testing play functionality of contract_killer
    Cost: 2
    Text: Contract Killer can be advanced. If there are at least 2 advancement tokens on Contract Killer, it gains: "click, trash: Trash a connection or do 2 meat damage."
    '''

    def setUp(self):
        '''
        setup test environment for contract_killer_08078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_contract_killer_08078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ronald_five_08088(unittest.TestCase):
    '''
    testing play functionality of ronald_five
    Cost: 3
    Text: Whenever the Runner trashes a Corp card (including this asset), they lose click.
    '''

    def setUp(self):
        '''
        setup test environment for ronald_five_08088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ronald_five_08088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_early_premiere_08095(unittest.TestCase):
    '''
    testing play functionality of early_premiere
    Cost: 0
    Text: When your turn begins, you may pay 1 credit. If you do, place 1 advancement counter on a card you can advance in the root of a server.
    '''

    def setUp(self):
        '''
        setup test environment for early_premiere_08095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_early_premiere_08095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cybernetics_court_08109(unittest.TestCase):
    '''
    testing play functionality of cybernetics_court
    Cost: 0
    Text: Your maximum hand size is increased by 4.
    '''

    def setUp(self):
        '''
        setup test environment for cybernetics_court_08109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_cybernetics_court_08109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_team_sponsorship_08110(unittest.TestCase):
    '''
    testing play functionality of team_sponsorship
    Cost: 1
    Text: Whenever you score an agenda, you may install a card from Archives or HQ, ignoring the install cost.
    '''

    def setUp(self):
        '''
        setup test environment for team_sponsorship_08110
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_team_sponsorship_08110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_genetics_pavilion_08113(unittest.TestCase):
    '''
    testing play functionality of genetics_pavilion
    Cost: 1
    Text: The Runner cannot draw more than 2 cards during each of their turns.
    '''

    def setUp(self):
        '''
        setup test environment for genetics_pavilion_08113
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_genetics_pavilion_08113()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_franchise_city_08114(unittest.TestCase):
    '''
    testing play functionality of franchise_city
    Cost: 3
    Text: While the Runner is accessing an agenda in R&D, they must reveal it. When the Runner accesses an agenda, add this asset to your score area as an agenda worth 1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for franchise_city_08114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_franchise_city_08114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_worlds_plaza_08116(unittest.TestCase):
    '''
    testing play functionality of worlds_plaza
    Cost: 2
    Text: Worlds Plaza can host up to 3 assets. click: Install an asset from HQ on Worlds Plaza and rez it, lowering its rez cost by 2, if able.
    '''

    def setUp(self):
        '''
        setup test environment for worlds_plaza_08116
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_worlds_plaza_08116()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_public_support_08117(unittest.TestCase):
    '''
    testing play functionality of public_support
    Cost: 2
    Text: Place 3 power counters on Public Support when it is rezzed. When there are no power counters left on Public Support, add it to your score area as an agenda worth 1 agenda point. When your turn begins, remove 1 power counter from Public Support.
    '''

    def setUp(self):
        '''
        setup test environment for public_support_08117
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_public_support_08117()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lily_lockwell_09008(unittest.TestCase):
    '''
    testing play functionality of lily_lockwell
    Cost: 2
    Text: When you rez Lily Lockwell, draw 3 cards. click, remove 1 tag: Search R&D for an operation, reveal it, and shuffle the rest of R&D. Add the operation to the top of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for lily_lockwell_09008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_lily_lockwell_09008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_news_team_09009(unittest.TestCase):
    '''
    testing play functionality of news_team
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, they must either take 2 tags or add this asset to their score area as an agenda worth -1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for news_team_09009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_news_team_09009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shannon_claire_09010(unittest.TestCase):
    '''
    testing play functionality of shannon_claire
    Cost: 0
    Text: click: Draw 1 card from the bottom of R&D. trash: Search R&D or Archives for an agenda and reveal it. Shuffle the rest of R&D if you searched it. Add the agenda to the bottom of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for shannon_claire_09010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_shannon_claire_09010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_victoria_jenkins_09011(unittest.TestCase):
    '''
    testing play functionality of victoria_jenkins
    Cost: 3
    Text: The Runner gets -1 allotted click for each of their turns. When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.
    '''

    def setUp(self):
        '''
        setup test environment for victoria_jenkins_09011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_victoria_jenkins_09011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reality_threedee_09012(unittest.TestCase):
    '''
    testing play functionality of reality_threedee
    Cost: 0
    Text: When you rez Reality Threedee, take 1 bad publicity. When your turn begins, gain 1 credit (or 2 credits if the Runner is tagged).
    '''

    def setUp(self):
        '''
        setup test environment for reality_threedee_09012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_reality_threedee_09012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_launch_campaign_09027(unittest.TestCase):
    '''
    testing play functionality of launch_campaign
    Cost: 1
    Text: Place 6 credits from the bank on Launch Campaign when it is rezzed. When there are no credits left on Launch Campaign, trash it. When your turn begins, take 2 credits from Launch Campaign.
    '''

    def setUp(self):
        '''
        setup test environment for launch_campaign_09027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_launch_campaign_09027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kala_ghoda_real_tv_10015(unittest.TestCase):
    '''
    testing play functionality of kala_ghoda_real_tv
    Cost: 0
    Text: When your turn begins, you may look at the top card of the stack. trash: The Runner trashes the top card of the stack.
    '''

    def setUp(self):
        '''
        setup test environment for kala_ghoda_real_tv_10015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_kala_ghoda_real_tv_10015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mumba_temple_10018(unittest.TestCase):
    '''
    testing play functionality of mumba_temple
    Cost: 1
    Text: This card costs 0 influence if you have 15 or fewer ice in your deck. 2 recurring credits Use these credits to rez cards.
    '''

    def setUp(self):
        '''
        setup test environment for mumba_temple_10018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_mumba_temple_10018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_museum_of_history_10019(unittest.TestCase):
    '''
    testing play functionality of museum_of_history
    Cost: 1
    Text: This asset costs 0 influence if you have 50 or more cards in your deck. When your turn begins, you may shuffle 1 card from Archives into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for museum_of_history_10019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_museum_of_history_10019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_advanced_assembly_lines_10027(unittest.TestCase):
    '''
    testing play functionality of advanced_assembly_lines
    Cost: 1
    Text: When you rez Advanced Assembly Lines, gain 3 credits. trash: Install a non-agenda card from HQ (paying the install cost). You cannot use this ability during a run.
    '''

    def setUp(self):
        '''
        setup test environment for advanced_assembly_lines_10027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_advanced_assembly_lines_10027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lakshmi_smartfabrics_10028(unittest.TestCase):
    '''
    testing play functionality of lakshmi_smartfabrics
    Cost: 1
    Text: Whenever you rez a card, place 1 power counter on Lakshmi Smartfabrics. X hosted power counters: Reveal an agenda worth X points from HQ. The Runner cannot steal copies of that agenda for the remainder of this turn.
    '''

    def setUp(self):
        '''
        setup test environment for lakshmi_smartfabrics_10028
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_lakshmi_smartfabrics_10028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_palana_agroplex_10031(unittest.TestCase):
    '''
    testing play functionality of palana_agroplex
    Cost: 1
    Text: When your turn begins, each player draws 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for palana_agroplex_10031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_palana_agroplex_10031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mumbad_construction_co_10036(unittest.TestCase):
    '''
    testing play functionality of mumbad_construction_co
    Cost: 4
    Text: When your turn begins, place 1 advancement token on Mumbad Construction Co. 2 credits: Move 1 advancement token from Mumbad Construction Co. to a faceup card.
    '''

    def setUp(self):
        '''
        setup test environment for mumbad_construction_co_10036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_mumbad_construction_co_10036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pad_factory_10038(unittest.TestCase):
    '''
    testing play functionality of pad_factory
    Cost: 2
    Text: This card costs 0 influence if you have 3 PAD Campaigns in your deck. click: Place 1 advancement token on a card. You cannot score that card until your next turn begins.
    '''

    def setUp(self):
        '''
        setup test environment for pad_factory_10038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_pad_factory_10038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_clone_suffrage_movement_10049(unittest.TestCase):
    '''
    testing play functionality of clone_suffrage_movement
    Cost: 1
    Text: When your turn begins, you may add 1 operation from Archives to HQ if there is no ice protecting this server.
    '''

    def setUp(self):
        '''
        setup test environment for clone_suffrage_movement_10049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_clone_suffrage_movement_10049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bioethics_association_10050(unittest.TestCase):
    '''
    testing play functionality of bioethics_association
    Cost: 1
    Text: When your turn begins, do 1 net damage if there is no ice protecting this server.
    '''

    def setUp(self):
        '''
        setup test environment for bioethics_association_10050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_bioethics_association_10050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_political_dealings_10051(unittest.TestCase):
    '''
    testing play functionality of political_dealings
    Cost: 4
    Text: Whenever you draw an agenda, you may reveal and install it.
    '''

    def setUp(self):
        '''
        setup test environment for political_dealings_10051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_political_dealings_10051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sensie_actors_union_10053(unittest.TestCase):
    '''
    testing play functionality of sensie_actors_union
    Cost: 0
    Text: When your turn begins, you may draw 3 cards if there is no ice protecting this server. If you do, add 1 card from HQ to the bottom of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for sensie_actors_union_10053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_sensie_actors_union_10053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_commercial_bankers_group_10054(unittest.TestCase):
    '''
    testing play functionality of commercial_bankers_group
    Cost: 1
    Text: When your turn begins, gain 3 credits if there is no ice protecting this server.
    '''

    def setUp(self):
        '''
        setup test environment for commercial_bankers_group_10054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_commercial_bankers_group_10054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mumbad_city_hall_10055(unittest.TestCase):
    '''
    testing play functionality of mumbad_city_hall
    Cost: 1
    Text: click: Search R&D for an alliance card, reveal it, and play or install it (paying all costs). Shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for mumbad_city_hall_10055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_mumbad_city_hall_10055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_jeeves_model_bioroids_10067(unittest.TestCase):
    '''
    testing play functionality of jeeves_model_bioroids
    Cost: 2
    Text: This card costs 0 influence if you have 6 or more non-alliance haas-bioroid cards in your deck. The first time you spend 3click on the same action each turn, gain click.
    '''

    def setUp(self):
        '''
        setup test environment for jeeves_model_bioroids_10067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_jeeves_model_bioroids_10067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_raman_rai_10068(unittest.TestCase):
    '''
    testing play functionality of raman_rai
    Cost: 1
    Text: This asset costs 0 influence if you have 6 or more non-alliance jinteki cards in your deck. Whenever you draw a card, you may lose click. If you do, reveal that card and 1 card in Archives of the same type. Swap those cards. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for raman_rai_10068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_raman_rai_10068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aryabhata_tech_10070(unittest.TestCase):
    '''
    testing play functionality of aryabhata_tech
    Cost: 2
    Text: Whenever there is a successful trace, gain 1 credit and the Runner loses 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for aryabhata_tech_10070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_aryabhata_tech_10070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_executive_search_firm_10072(unittest.TestCase):
    '''
    testing play functionality of executive_search_firm
    Cost: 0
    Text: This card costs 0 influence if you have 6 or more non-alliance weyland-consortium cards in your deck. click: Search R&D for an executive, sysop, or character, reveal it, and add it to HQ. Shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for executive_search_firm_10072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_executive_search_firm_10072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_indian_union_stock_exchange_10073(unittest.TestCase):
    '''
    testing play functionality of indian_union_stock_exchange
    Cost: 1
    Text: Whenever you rez or play an out-of-faction card (including Indian Union Stock Exchange), gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for indian_union_stock_exchange_10073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_indian_union_stock_exchange_10073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_full_immersion_recstudio_10108(unittest.TestCase):
    '''
    testing play functionality of full_immersion_recstudio
    Cost: 2
    Text: Full Immersion RecStudio can host up to 2 assets and/or agendas. The trash cost of Full Immersion RecStudio is increased by 3 for each card hosted on it.
    '''

    def setUp(self):
        '''
        setup test environment for full_immersion_recstudio_10108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_full_immersion_recstudio_10108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ibrahim_salem_10109(unittest.TestCase):
    '''
    testing play functionality of ibrahim_salem
    Cost: 2
    Text: This card costs 0 influence if you have 6 or more non-alliance nbn cards in your deck. As an additional cost to rez Ibrahim Salem, forfeit an agenda. When your turn begins, name a card type. Look at the Runner's grip and trash 1 card in it of the named type.
    '''

    def setUp(self):
        '''
        setup test environment for ibrahim_salem_10109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ibrahim_salem_10109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zealous_judge_10111(unittest.TestCase):
    '''
    testing play functionality of zealous_judge
    Cost: 2
    Text: Zealous Judge can only be rezzed if the Runner is tagged. click, 1 credit: Give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for zealous_judge_10111
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_zealous_judge_10111()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hyoubu_research_facility_11012(unittest.TestCase):
    '''
    testing play functionality of hyoubu_research_facility
    Cost: 0
    Text: The first time each turn you reveal secretly spent credits, gain that many credits.
    '''

    def setUp(self):
        '''
        setup test environment for hyoubu_research_facility_11012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_hyoubu_research_facility_11012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_watchdog_11015(unittest.TestCase):
    '''
    testing play functionality of watchdog
    Cost: 0
    Text: The rez cost of the first piece of ice you rez each turn is lowered by 1 for each tag the Runner has.
    '''

    def setUp(self):
        '''
        setup test environment for watchdog_11015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_watchdog_11015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sandburg_11020(unittest.TestCase):
    '''
    testing play functionality of sandburg
    Cost: 0
    Text: If you have at least 10 credits, each piece of ice has +1 strength for every 5 credits in your credit pool.
    '''

    def setUp(self):
        '''
        setup test environment for sandburg_11020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_sandburg_11020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ci_fund_11036(unittest.TestCase):
    '''
    testing play functionality of ci_fund
    Cost: 0
    Text: When your turn begins, you may move up to 3 credits from your credit pool to C.I. Fund. When your turn begins, place 2 credits on C.I. Fund from the bank if there are at least 6 credits on it. 2 credits,trash: Take all credits from C.I. Fund.
    '''

    def setUp(self):
        '''
        setup test environment for ci_fund_11036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ci_fund_11036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_alexa_belsky_11055(unittest.TestCase):
    '''
    testing play functionality of alexa_belsky
    Cost: 1
    Text: trash: Shuffle all cards in HQ into R&D. The Runner may pay any number of credits to prevent 1 random card in HQ from being shuffled into R&D for every 2 credits spent.
    '''

    def setUp(self):
        '''
        setup test environment for alexa_belsky_11055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_alexa_belsky_11055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fumiko_yamamori_11073(unittest.TestCase):
    '''
    testing play functionality of fumiko_yamamori
    Cost: 4
    Text: Whenever you and the Runner reveal secretly spent credits, do 1 meat damage if you and the Runner spent a different number of credits.
    '''

    def setUp(self):
        '''
        setup test environment for fumiko_yamamori_11073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_fumiko_yamamori_11073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chief_slee_11077(unittest.TestCase):
    '''
    testing play functionality of chief_slee
    Cost: 2
    Text: Whenever an encounter with a piece of ice ends, place 1 power counter on Chief Slee for each unbroken subroutine on the encountered piece of ice. click, 5 hosted power counters: Do 5 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for chief_slee_11077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_chief_slee_11077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_anson_rose_11096(unittest.TestCase):
    '''
    testing play functionality of anson_rose
    Cost: 1
    Text: When your turn begins, place 1 advancement token on Anson Rose. Whenever you rez a piece of ice, you may move any number of advancement tokens from Anson Rose to that ice.
    '''

    def setUp(self):
        '''
        setup test environment for anson_rose_11096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_anson_rose_11096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nasx_11118(unittest.TestCase):
    '''
    testing play functionality of nasx
    Cost: 2
    Text: Gain 1 credit when your turn begins. Whenever you gain credits through a card ability other than from NASX, you may spend up to 2 credits to place that many power counters on NASX. click,trash: Gain 2 credits for each power counter on NASX.
    '''

    def setUp(self):
        '''
        setup test environment for nasx_11118
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_nasx_11118()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_synth_dna_modification_12012(unittest.TestCase):
    '''
    testing play functionality of synth_dna_modification
    Cost: 2
    Text: The first time a subroutine on a piece of AP ice is broken each turn, do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for synth_dna_modification_12012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_synth_dna_modification_12012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_net_analytics_12014(unittest.TestCase):
    '''
    testing play functionality of net_analytics
    Cost: 0
    Text: Whenever the Runner avoids or removes 1 or more tags, you may draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for net_analytics_12014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_net_analytics_12014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_quarantine_system_12017(unittest.TestCase):
    '''
    testing play functionality of quarantine_system
    Cost: 1
    Text: Forfeit an agenda: Rez up to 3 pieces of ice, lowering the cost of each by 2 credits for each printed agenda point on the forfeited agenda.
    '''

    def setUp(self):
        '''
        setup test environment for quarantine_system_12017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_quarantine_system_12017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cpc_generator_12034(unittest.TestCase):
    '''
    testing play functionality of cpc_generator
    Cost: 0
    Text: The first time the Runner spends click to gain 1 credit each turn (not through a card effect), gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for cpc_generator_12034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_cpc_generator_12034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_clyde_van_rite_12037(unittest.TestCase):
    '''
    testing play functionality of clyde_van_rite
    Cost: 2
    Text: When your turn begins, the Runner must pay 1 credit or trash the top card of the stack.
    '''

    def setUp(self):
        '''
        setup test environment for clyde_van_rite_12037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_clyde_van_rite_12037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bioroid_work_crew_12051(unittest.TestCase):
    '''
    testing play functionality of bioroid_work_crew
    Cost: 2
    Text: trash: Install 1 card from HQ. Use this ability only during the next paid ability window after playing and resolving an operation.
    '''

    def setUp(self):
        '''
        setup test environment for bioroid_work_crew_12051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_bioroid_work_crew_12051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_whampoa_reclamation_12079(unittest.TestCase):
    '''
    testing play functionality of whampoa_reclamation
    Cost: 3
    Text: Trash 1 card from HQ: Add 1 card from Archives to the bottom of R&D. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for whampoa_reclamation_12079
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_whampoa_reclamation_12079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_open_forum_12097(unittest.TestCase):
    '''
    testing play functionality of open_forum
    Cost: 1
    Text: After your mandatory draw, reveal the top card of R&D and add it to HQ. Add 1 card from HQ to the top of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for open_forum_12097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_open_forum_12097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mca_austerity_policy_12111(unittest.TestCase):
    '''
    testing play functionality of mca_austerity_policy
    Cost: 1
    Text: click: Place 1 power counter on this asset. When the Runner's next turn begins, they lose click. Use this ability only once per turn. click, trash, 3 hosted power counters: Gain click click click click.
    '''

    def setUp(self):
        '''
        setup test environment for mca_austerity_policy_12111
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_mca_austerity_policy_12111()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_breached_dome_12113(unittest.TestCase):
    '''
    testing play functionality of breached_dome
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, do 1 meat damage and trash the top card of the stack.
    '''

    def setUp(self):
        '''
        setup test environment for breached_dome_12113
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_breached_dome_12113()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_estelle_moon_13032(unittest.TestCase):
    '''
    testing play functionality of estelle_moon
    Cost: 2
    Text: Whenever you install a card in the root of a remote server, place 1 power counter on this asset. trash: For each power counter on this asset, gain 2 credits and draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for estelle_moon_13032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_estelle_moon_13032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marilyn_campaign_13033(unittest.TestCase):
    '''
    testing play functionality of marilyn_campaign
    Cost: 2
    Text: When you rez this asset, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this asset. Interrupt -> When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. (It is still considered trashed.)
    '''

    def setUp(self):
        '''
        setup test environment for marilyn_campaign_13033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_marilyn_campaign_13033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_illegal_arms_factory_13045(unittest.TestCase):
    '''
    testing play functionality of illegal_arms_factory
    Cost: 3
    Text: If the Runner trashes Illegal Arms Factory while it is installed, take 1 bad publicity. When your turn begins, gain 1 credit and draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for illegal_arms_factory_13045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_illegal_arms_factory_13045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mr_stone_13046(unittest.TestCase):
    '''
    testing play functionality of mr_stone
    Cost: 2
    Text: Whenever the Runner takes 1 or more tags, do 1 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for mr_stone_13046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_mr_stone_13046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_honeyfarm_13054(unittest.TestCase):
    '''
    testing play functionality of honeyfarm
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, they lose 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for honeyfarm_13054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_honeyfarm_13054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_longterm_investment_13055(unittest.TestCase):
    '''
    testing play functionality of longterm_investment
    Cost: 2
    Text: When your turn begins, place 2 credits on Long-Term Investment. If there are at least 8 credits on Long-Term Investment, it gains "click: Take any number of credits from Long-Term Investment."
    '''

    def setUp(self):
        '''
        setup test environment for longterm_investment_13055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_longterm_investment_13055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_investigator_inez_delgado_a_14004(unittest.TestCase):
    '''
    testing play functionality of investigator_inez_delgado_a
    Cost: 0
    Text: Whenever you score an agenda, you may swap it with an agenda in the Runner's score area worth at least 1 point, then resolve the "when scored" ability on that agenda.
    '''

    def setUp(self):
        '''
        setup test environment for investigator_inez_delgado_a_14004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_investigator_inez_delgado_a_14004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_investigator_inez_delgado_a_2_14005(unittest.TestCase):
    '''
    testing play functionality of investigator_inez_delgado_a_2
    Cost: 0
    Text: Whenever the Runner steals an agenda, you may resolve the "when scored" ability on that agenda, then swap it with an agenda in your scored area.
    '''

    def setUp(self):
        '''
        setup test environment for investigator_inez_delgado_a_2_14005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_investigator_inez_delgado_a_2_14005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lt_todachine_14006(unittest.TestCase):
    '''
    testing play functionality of lt_todachine
    Cost: 3
    Text: Whenever you rez a piece of ice, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for lt_todachine_14006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_lt_todachine_14006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lt_todachine_2_14007(unittest.TestCase):
    '''
    testing play functionality of lt_todachine_2
    Cost: 3
    Text: Whenever you rez a piece of ice, give the Runner 1 tag. Whenever the Runner accesses cards, he or she accesses 1 fewer card if he or she is tagged (to a minimum of 1 card).
    '''

    def setUp(self):
        '''
        setup test environment for lt_todachine_2_14007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_lt_todachine_2_14007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_trojan_14008(unittest.TestCase):
    '''
    testing play functionality of trojan
    Cost: 0
    Text: If Trojan is accessed from R&D, then Runner must reveal it. When the Runner accesses Trojan, lose 2 credits, trash 1 card from HQ at random, and destroy Trojan. Ignore this ability if the Runner accesses Trojan from Archives.
    '''

    def setUp(self):
        '''
        setup test environment for trojan_14008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_trojan_14008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_adonis_campaign_20064(unittest.TestCase):
    '''
    testing play functionality of adonis_campaign
    Cost: 4
    Text: Put 12 credits from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it. Take 3 credits from Adonis Campaign when your turn begins.
    '''

    def setUp(self):
        '''
        setup test environment for adonis_campaign_20064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_adonis_campaign_20064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aggressive_secretary_20065(unittest.TestCase):
    '''
    testing play functionality of aggressive_secretary
    Cost: 0
    Text: Aggressive Secretary can be advanced. If you pay 2 credits when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.
    '''

    def setUp(self):
        '''
        setup test environment for aggressive_secretary_20065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_aggressive_secretary_20065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dedicated_response_team_20081(unittest.TestCase):
    '''
    testing play functionality of dedicated_response_team
    Cost: 2
    Text: If the Runner is tagged, Dedicated Response Team gains "Whenever a successful run ends, do 2 meat damage."
    '''

    def setUp(self):
        '''
        setup test environment for dedicated_response_team_20081
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_dedicated_response_team_20081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_elizabeth_mills_20082(unittest.TestCase):
    '''
    testing play functionality of elizabeth_mills
    Cost: 2
    Text: When you rez Elizabeth Mills, remove 1 bad publicity. click, trash: Trash 1 location. Take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for elizabeth_mills_20082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_elizabeth_mills_20082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_grndl_refinery_20083(unittest.TestCase):
    '''
    testing play functionality of grndl_refinery
    Cost: 0
    Text: GRNDL Refinery can be advanced. click, trash: Gain 4 credits for each advancement token on GRNDL Refinery.
    '''

    def setUp(self):
        '''
        setup test environment for grndl_refinery_20083
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_grndl_refinery_20083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_junebug_20096(unittest.TestCase):
    '''
    testing play functionality of project_junebug
    Cost: 0
    Text: Project Junebug can be advanced. If you pay 1 credit when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.
    '''

    def setUp(self):
        '''
        setup test environment for project_junebug_20096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_project_junebug_20096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ronin_20097(unittest.TestCase):
    '''
    testing play functionality of ronin
    Cost: 0
    Text: You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.
    '''

    def setUp(self):
        '''
        setup test environment for ronin_20097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ronin_20097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_snare_20098(unittest.TestCase):
    '''
    testing play functionality of snare
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for snare_20098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_snare_20098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ghost_branch_20112(unittest.TestCase):
    '''
    testing play functionality of ghost_branch
    Cost: 0
    Text: Ghost Branch can be advanced. When the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.
    '''

    def setUp(self):
        '''
        setup test environment for ghost_branch_20112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ghost_branch_20112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_melange_mining_corp_20127(unittest.TestCase):
    '''
    testing play functionality of melange_mining_corp
    Cost: 1
    Text: click, click, click: Gain 7 credits.
    '''

    def setUp(self):
        '''
        setup test environment for melange_mining_corp_20127
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_melange_mining_corp_20127()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pad_campaign_20128(unittest.TestCase):
    '''
    testing play functionality of pad_campaign
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for pad_campaign_20128
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_pad_campaign_20128()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gene_splicer_21012(unittest.TestCase):
    '''
    testing play functionality of gene_splicer
    Cost: 2
    Text: Gene Splicer can be advanced. When the Runner accesses Gene Splicer, do 1 net damage for each advancement token on Gene Splicer. click, 3 hosted advancement tokens: Add Gene Splicer to your score area as an agenda worth 1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for gene_splicer_21012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_gene_splicer_21012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_echo_chamber_21015(unittest.TestCase):
    '''
    testing play functionality of echo_chamber
    Cost: 4
    Text: click, click, click: Add Echo Chamber to your score area as an agenda worth 1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for echo_chamber_21015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_echo_chamber_21015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_urban_renewal_21018(unittest.TestCase):
    '''
    testing play functionality of urban_renewal
    Cost: 1
    Text: Place 3 power counters on Urban Renewal when it is rezzed. When there are no power counters left on Urban Renewal, trash it and do 4 meat damage. When your turn begins, remove 1 power counter from Urban Renewal.
    '''

    def setUp(self):
        '''
        setup test environment for urban_renewal_21018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_urban_renewal_21018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reconstruction_contract_21020(unittest.TestCase):
    '''
    testing play functionality of reconstruction_contract
    Cost: 1
    Text: Whenever the Runner suffers any amount of meat damage, you may place 1 advancement token on Reconstruction Contract. trash: Move any number of advancement tokens from Reconstruction Contract to a card that can be advanced.
    '''

    def setUp(self):
        '''
        setup test environment for reconstruction_contract_21020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_reconstruction_contract_21020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ngo_front_21039(unittest.TestCase):
    '''
    testing play functionality of ngo_front
    Cost: 0
    Text: NGO Front can be advanced. trash,1 hosted advancement token: Gain 5 credits. trash,2 hosted advancement tokens: Gain 8 credits.
    '''

    def setUp(self):
        '''
        setup test environment for ngo_front_21039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ngo_front_21039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kuwinda_k4h1u3_21049(unittest.TestCase):
    '''
    testing play functionality of kuwinda_k4h1u3
    Cost: 3
    Text: When your turn begins, you may trace[X], where X is equal to the number of hosted power counters. If successful, do 1 core damage and trash this asset. If unsuccessful, place 1 power counter on this asset.
    '''

    def setUp(self):
        '''
        setup test environment for kuwinda_k4h1u3_21049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_kuwinda_k4h1u3_21049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_personalized_portal_21056(unittest.TestCase):
    '''
    testing play functionality of personalized_portal
    Cost: 3
    Text: When your turn begins, the Runner draws 1 card. You may gain 1 credit for every 2 cards in the grip.
    '''

    def setUp(self):
        '''
        setup test environment for personalized_portal_21056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_personalized_portal_21056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_technoco_21060(unittest.TestCase):
    '''
    testing play functionality of technoco
    Cost: 2
    Text: The install cost of each program, piece of hardware, and virtual resource is increased by 1. Whenever the Runner installs a program, piece of hardware, or virtual resource, you may gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for technoco_21060
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_technoco_21060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_malia_z0l0k4_21069(unittest.TestCase):
    '''
    testing play functionality of malia_z0l0k4
    Cost: 1
    Text: When you rez this asset, choose 1 installed non-virtual resource. The chosen resource loses its printed abilities.
    '''

    def setUp(self):
        '''
        setup test environment for malia_z0l0k4_21069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_malia_z0l0k4_21069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_amani_senai_21076(unittest.TestCase):
    '''
    testing play functionality of amani_senai
    Cost: 2
    Text: Whenever an agenda is scored or stolen, you may trace[X]. If successful, add an installed Runner card to the grip. X is the advancement requirement of the scored or stolen agenda.
    '''

    def setUp(self):
        '''
        setup test environment for amani_senai_21076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_amani_senai_21076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rashida_jaheem_21080(unittest.TestCase):
    '''
    testing play functionality of rashida_jaheem
    Cost: 0
    Text: When your turn begins, you may trash Rashida Jaheem to gain 3 credits and draw 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for rashida_jaheem_21080
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_rashida_jaheem_21080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_warden_fatuma_21093(unittest.TestCase):
    '''
    testing play functionality of warden_fatuma
    Cost: 1
    Text: Each piece of rezzed bioroid ice gains "Subroutine The Runner loses click, if able." before all of its other subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for warden_fatuma_21093
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_warden_fatuma_21093()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_false_flag_21120(unittest.TestCase):
    '''
    testing play functionality of false_flag
    Cost: 2
    Text: False Flag can be advanced. When the Runner accesses False Flag, give the Runner 1 tag for every 2 advancement tokens on False Flag. click, 7 hosted advancement tokens: add False Flag to your score area as an agenda worth 3 agenda points.
    '''

    def setUp(self):
        '''
        setup test environment for false_flag_21120
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_false_flag_21120()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_apis_keeper_isobel_22036(unittest.TestCase):
    '''
    testing play functionality of apis_keeper_isobel
    Cost: 2
    Text: When your turn begins, you may remove an advancement token from an installed card to gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for apis_keeper_isobel_22036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_apis_keeper_isobel_22036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_neurostasis_22037(unittest.TestCase):
    '''
    testing play functionality of neurostasis
    Cost: 0
    Text: Neurostasis can be advanced. If you pay 3 credits when the Runner accesses Neurostasis, choose 1 installed Runner card for each advancement token on Neurostasis. The Runner must shuffle the chosen cards into the stack.
    '''

    def setUp(self):
        '''
        setup test environment for neurostasis_22037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_neurostasis_22037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_siu_22044(unittest.TestCase):
    '''
    testing play functionality of siu
    Cost: 3
    Text: When your turn begins, you may trash SIU to Trace[3]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for siu_22044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_siu_22044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_drudge_work_22052(unittest.TestCase):
    '''
    testing play functionality of drudge_work
    Cost: 2
    Text: Place 3 power counters on Drudge Work when it is rezzed. When there are no power counters left on Drudge Work, trash it. click, hosted power counter: Reveal an agenda in HQ or Archives. Gain credits equal to its agenda points, then shuffle it into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for drudge_work_22052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_drudge_work_22052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lady_liberty_22058(unittest.TestCase):
    '''
    testing play functionality of lady_liberty
    Cost: 5
    Text: When your turn begins, place 1 power counter on Lady Liberty. click, click, click: Add an agenda from HQ to your score area worth agenda points equal to the exact number of hosted power counters. Limit 1 region per server. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for lady_liberty_22058
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_lady_liberty_22058()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_adonis_campaign_25070(unittest.TestCase):
    '''
    testing play functionality of adonis_campaign
    Cost: 4
    Text: Put 12 credits from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it. Take 3 credits from Adonis Campaign when your turn begins.
    '''

    def setUp(self):
        '''
        setup test environment for adonis_campaign_25070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_adonis_campaign_25070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aggressive_secretary_25071(unittest.TestCase):
    '''
    testing play functionality of aggressive_secretary
    Cost: 0
    Text: Aggressive Secretary can be advanced. If you pay 2 credits when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.
    '''

    def setUp(self):
        '''
        setup test environment for aggressive_secretary_25071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_aggressive_secretary_25071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marilyn_campaign_25072(unittest.TestCase):
    '''
    testing play functionality of marilyn_campaign
    Cost: 2
    Text: When you rez this asset, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this asset. Interrupt -> When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. (It is still considered trashed.)
    '''

    def setUp(self):
        '''
        setup test environment for marilyn_campaign_25072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_marilyn_campaign_25072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_junebug_25089(unittest.TestCase):
    '''
    testing play functionality of project_junebug
    Cost: 0
    Text: Project Junebug can be advanced. If you pay 1 credit when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.
    '''

    def setUp(self):
        '''
        setup test environment for project_junebug_25089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_project_junebug_25089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ronin_25090(unittest.TestCase):
    '''
    testing play functionality of ronin
    Cost: 0
    Text: You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.
    '''

    def setUp(self):
        '''
        setup test environment for ronin_25090
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ronin_25090()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_snare_25091(unittest.TestCase):
    '''
    testing play functionality of snare
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for snare_25091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_snare_25091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sundew_25092(unittest.TestCase):
    '''
    testing play functionality of sundew
    Cost: 2
    Text: The first time the Runner spends 1 or more click during their turn, gain 2 credits. If those click were spent to take an action, the first time during that action a run on this server begins, pay 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for sundew_25092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_sundew_25092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_daily_business_show_25108(unittest.TestCase):
    '''
    testing play functionality of daily_business_show
    Cost: 2
    Text: Interrupt -> The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for daily_business_show_25108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_daily_business_show_25108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ghost_branch_25109(unittest.TestCase):
    '''
    testing play functionality of ghost_branch
    Cost: 0
    Text: Ghost Branch can be advanced. When the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.
    '''

    def setUp(self):
        '''
        setup test environment for ghost_branch_25109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ghost_branch_25109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marked_accounts_25110(unittest.TestCase):
    '''
    testing play functionality of marked_accounts
    Cost: 0
    Text: When your turn begins, take 1 credit from Marked Accounts, if able. click: Place 3 credits from the bank on Marked Accounts.
    '''

    def setUp(self):
        '''
        setup test environment for marked_accounts_25110
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_marked_accounts_25110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reversed_accounts_25111(unittest.TestCase):
    '''
    testing play functionality of reversed_accounts
    Cost: 0
    Text: You can advance this asset. click, trash: The Runner loses 4 credits for each hosted advancement counter.
    '''

    def setUp(self):
        '''
        setup test environment for reversed_accounts_25111
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_reversed_accounts_25111()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_contract_killer_25127(unittest.TestCase):
    '''
    testing play functionality of contract_killer
    Cost: 2
    Text: Contract Killer can be advanced. If there are at least 2 advancement tokens on Contract Killer, it gains: "click, trash: Trash a connection or do 2 meat damage."
    '''

    def setUp(self):
        '''
        setup test environment for contract_killer_25127
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_contract_killer_25127()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_elizabeth_mills_25128(unittest.TestCase):
    '''
    testing play functionality of elizabeth_mills
    Cost: 2
    Text: When you rez Elizabeth Mills, remove 1 bad publicity. click, trash: Trash 1 location. Take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for elizabeth_mills_25128
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_elizabeth_mills_25128()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_public_support_25129(unittest.TestCase):
    '''
    testing play functionality of public_support
    Cost: 2
    Text: Place 3 power counters on Public Support when it is rezzed. When there are no power counters left on Public Support, add it to your score area as an agenda worth 1 agenda point. When your turn begins, remove 1 power counter from Public Support.
    '''

    def setUp(self):
        '''
        setup test environment for public_support_25129
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_public_support_25129()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pad_campaign_25142(unittest.TestCase):
    '''
    testing play functionality of pad_campaign
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for pad_campaign_25142
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_pad_campaign_25142()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_calvin_b4l3y_26033(unittest.TestCase):
    '''
    testing play functionality of calvin_b4l3y
    Cost: 0
    Text: click: Draw 2 cards. Use this ability only once per turn. When the Runner trashes this asset, you may draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for calvin_b4l3y_26033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_calvin_b4l3y_26033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nanoetching_matrix_26034(unittest.TestCase):
    '''
    testing play functionality of nanoetching_matrix
    Cost: 0
    Text: click: Gain 2 credits. Use this ability only once per turn. When the Runner trashes this asset, you may gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for nanoetching_matrix_26034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_nanoetching_matrix_26034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_public_health_portal_26042(unittest.TestCase):
    '''
    testing play functionality of public_health_portal
    Cost: 3
    Text: When your turn begins, reveal the top card of R&D and gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for public_health_portal_26042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_public_health_portal_26042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_storgotic_resonator_26043(unittest.TestCase):
    '''
    testing play functionality of storgotic_resonator
    Cost: 2
    Text: The first time each turn you trash (from any location) a card that matches the faction of the Runner's identity, place 1 power counter on this asset. click, hosted power counter: Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for storgotic_resonator_26043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_storgotic_resonator_26043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_daily_quest_26048(unittest.TestCase):
    '''
    testing play functionality of daily_quest
    Cost: 1
    Text: Rez only during your action phase. Whenever the Runner makes a successful run on this server, they gain 2 credits. When your turn begins, gain 3 credits if the Runner did not make any successful runs on this server during their last turn.
    '''

    def setUp(self):
        '''
        setup test environment for daily_quest_26048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_daily_quest_26048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tiered_subscription_26049(unittest.TestCase):
    '''
    testing play functionality of tiered_subscription
    Cost: 0
    Text: The first time each turn a run begins, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for tiered_subscription_26049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_tiered_subscription_26049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_roughneck_repair_squad_26057(unittest.TestCase):
    '''
    testing play functionality of roughneck_repair_squad
    Cost: 0
    Text: click, click, click: Gain 6 credits. You may remove 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for roughneck_repair_squad_26057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_roughneck_repair_squad_26057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_csr_campaign_26064(unittest.TestCase):
    '''
    testing play functionality of csr_campaign
    Cost: 2
    Text: When your turn begins, you may draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for csr_campaign_26064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_csr_campaign_26064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bass_ch1r180g4_26098(unittest.TestCase):
    '''
    testing play functionality of bass_ch1r180g4
    Cost: 3
    Text: click, trash: Gain click click.
    '''

    def setUp(self):
        '''
        setup test environment for bass_ch1r180g4_26098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_bass_ch1r180g4_26098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cerebral_overwriter_26099(unittest.TestCase):
    '''
    testing play functionality of cerebral_overwriter
    Cost: 0
    Text: You can advance this asset. When the Runner accesses this asset while it is installed, you may pay 3 credits. If you do, do 1 core damage for each hosted advancement counter.
    '''

    def setUp(self):
        '''
        setup test environment for cerebral_overwriter_26099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_cerebral_overwriter_26099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vaporframe_fabricator_26100(unittest.TestCase):
    '''
    testing play functionality of vaporframe_fabricator
    Cost: 2
    Text: click: Install 1 card from HQ, ignoring all costs. Use this ability only once per turn. When the Runner trashes this asset, you may install 1 card from HQ, ignoring all costs. You cannot install that card in the root of this server.
    '''

    def setUp(self):
        '''
        setup test environment for vaporframe_fabricator_26100
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_vaporframe_fabricator_26100()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_prana_condenser_26107(unittest.TestCase):
    '''
    testing play functionality of prana_condenser
    Cost: 1
    Text: Interrupt -> Whenever you would do 1 or more net damage, you may prevent 1 net damage. If you do, place 1 power counter on this asset and gain 3 credits. click click,trash: Do 1 net damage for each hosted power counter.
    '''

    def setUp(self):
        '''
        setup test environment for prana_condenser_26107
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_prana_condenser_26107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wall_to_wall_26122(unittest.TestCase):
    '''
    testing play functionality of wall_to_wall
    Cost: 1
    Text: When your turn begins, if you have any other rezzed assets, resolve 1 of the following; otherwise, resolve up to 3: * Draw 1 card. * Gain 1 credit. * Place 1 advancement token on a piece of ice. * Add this asset to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for wall_to_wall_26122
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_wall_to_wall_26122()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hostile_infrastructure_29011(unittest.TestCase):
    '''
    testing play functionality of hostile_infrastructure
    Cost: 5
    Text: Whenever the Runner trashes a Corp card (including Hostile Infrastructure), do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for hostile_infrastructure_29011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_hostile_infrastructure_29011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_turtlebacks_29012(unittest.TestCase):
    '''
    testing play functionality of turtlebacks
    Cost: 2
    Text: Gain 1 credit whenever you create a server.
    '''

    def setUp(self):
        '''
        setup test environment for turtlebacks_29012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_turtlebacks_29012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_executive_boot_camp_29015(unittest.TestCase):
    '''
    testing play functionality of executive_boot_camp
    Cost: 0
    Text: When your turn begins, you may rez a card, lowering the rez cost by 1 credit. 1 credit,trash: Search R&D for an asset, reveal it, and add it to HQ. Shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for executive_boot_camp_29015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_executive_boot_camp_29015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nico_campaign_30037(unittest.TestCase):
    '''
    testing play functionality of nico_campaign
    Cost: 2
    Text: When you rez this asset, load 9 credits onto it. When it is empty, trash it and draw 1 card. When your turn begins, take 3 credits from this asset.
    '''

    def setUp(self):
        '''
        setup test environment for nico_campaign_30037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_nico_campaign_30037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_urtica_cipher_30045(unittest.TestCase):
    '''
    testing play functionality of urtica_cipher
    Cost: 0
    Text: You can advance this asset. When the Runner accesses this asset while it is installed, do 2 net damage plus 1 net damage for each hosted advancement counter.
    '''

    def setUp(self):
        '''
        setup test environment for urtica_cipher_30045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_urtica_cipher_30045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spin_doctor_30053(unittest.TestCase):
    '''
    testing play functionality of spin_doctor
    Cost: 0
    Text: When you rez this asset, draw 2 cards. Remove this asset from the game: Shuffle up to 2 cards from Archives into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for spin_doctor_30053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_spin_doctor_30053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_clearinghouse_30061(unittest.TestCase):
    '''
    testing play functionality of clearinghouse
    Cost: 0
    Text: You can advance this asset. When your turn begins, you may trash this asset to do 1 meat damage for each hosted advancement counter.
    '''

    def setUp(self):
        '''
        setup test environment for clearinghouse_30061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_clearinghouse_30061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_regolith_mining_license_30071(unittest.TestCase):
    '''
    testing play functionality of regolith_mining_license
    Cost: 2
    Text: When you rez this asset, load 15 credits onto it. When it is empty, trash it. click: Take 3 credits from this asset.
    '''

    def setUp(self):
        '''
        setup test environment for regolith_mining_license_30071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_regolith_mining_license_30071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marilyn_campaign_31042(unittest.TestCase):
    '''
    testing play functionality of marilyn_campaign
    Cost: 2
    Text: When you rez this asset, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this asset. Interrupt -> When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. (It is still considered trashed.)
    '''

    def setUp(self):
        '''
        setup test environment for marilyn_campaign_31042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_marilyn_campaign_31042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ronin_31053(unittest.TestCase):
    '''
    testing play functionality of ronin
    Cost: 0
    Text: You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.
    '''

    def setUp(self):
        '''
        setup test environment for ronin_31053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ronin_31053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_snare_31054(unittest.TestCase):
    '''
    testing play functionality of snare
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for snare_31054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_snare_31054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_daily_business_show_31063(unittest.TestCase):
    '''
    testing play functionality of daily_business_show
    Cost: 2
    Text: Interrupt -> The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for daily_business_show_31063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_daily_business_show_31063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reversed_accounts_31064(unittest.TestCase):
    '''
    testing play functionality of reversed_accounts
    Cost: 0
    Text: You can advance this asset. click, trash: The Runner loses 4 credits for each hosted advancement counter.
    '''

    def setUp(self):
        '''
        setup test environment for reversed_accounts_31064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_reversed_accounts_31064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_town_31074(unittest.TestCase):
    '''
    testing play functionality of corporate_town
    Cost: 1
    Text: As an additional cost to rez this asset, forfeit 1 agenda. When your turn begins, you may trash 1 installed resource. Trashing a resource this way cannot be prevented.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_town_31074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_corporate_town_31074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pad_campaign_31080(unittest.TestCase):
    '''
    testing play functionality of pad_campaign
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for pad_campaign_31080
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_pad_campaign_31080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_refuge_campaign_33033(unittest.TestCase):
    '''
    testing play functionality of refuge_campaign
    Cost: 4
    Text: When your turn begins, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for refuge_campaign_33033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_refuge_campaign_33033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_trieste_model_bioroids_33034(unittest.TestCase):
    '''
    testing play functionality of trieste_model_bioroids
    Cost: 2
    Text: When you rez this asset, choose 1 rezzed piece of bioroid ice. Runner card abilities cannot break subroutines on the chosen ice.
    '''

    def setUp(self):
        '''
        setup test environment for trieste_model_bioroids_33034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_trieste_model_bioroids_33034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bladderwort_33041(unittest.TestCase):
    '''
    testing play functionality of bladderwort
    Cost: 1
    Text: When your turn begins, gain 1 credit. Then, if you have 4 credits or less, do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for bladderwort_33041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_bladderwort_33041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_moon_pool_33042(unittest.TestCase):
    '''
    testing play functionality of moon_pool
    Cost: 3
    Text: Remove this asset from the game: Trash up to 2 cards from HQ. Reveal up to 2 facedown cards in Archives and shuffle them into R&D. For each agenda revealed this way, you may place 1 advancement counter on an installed card.
    '''

    def setUp(self):
        '''
        setup test environment for moon_pool_33042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_moon_pool_33042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chekist_scion_33050(unittest.TestCase):
    '''
    testing play functionality of chekist_scion
    Cost: 0
    Text: You can advance this asset. When the Runner accesses this asset while it is installed, give them 1 tag plus 1 tag for each hosted advancement counter.
    '''

    def setUp(self):
        '''
        setup test environment for chekist_scion_33050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_chekist_scion_33050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_drago_ivanov_33051(unittest.TestCase):
    '''
    testing play functionality of drago_ivanov
    Cost: 0
    Text: You can advance this asset. 2 hosted advancement counters: Give the Runner 1 tag. Use this ability only during your turn.
    '''

    def setUp(self):
        '''
        setup test environment for drago_ivanov_33051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_drago_ivanov_33051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ubiquitous_vig_33052(unittest.TestCase):
    '''
    testing play functionality of ubiquitous_vig
    Cost: 1
    Text: You can advance this asset. When your turn begins, gain 1 credit for each hosted advancement counter.
    '''

    def setUp(self):
        '''
        setup test environment for ubiquitous_vig_33052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_ubiquitous_vig_33052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_svyatogor_excavator_33059(unittest.TestCase):
    '''
    testing play functionality of svyatogor_excavator
    Cost: 0
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for svyatogor_excavator_33059
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_svyatogor_excavator_33059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nightmare_archive_33097(unittest.TestCase):
    '''
    testing play functionality of nightmare_archive
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, they may add it to their score area as an agenda worth -1 agenda point. If they do not, do 1 core damage and remove this asset from the game.
    '''

    def setUp(self):
        '''
        setup test environment for nightmare_archive_33097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_nightmare_archive_33097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dr_vientiane_keeling_33106(unittest.TestCase):
    '''
    testing play functionality of dr_vientiane_keeling
    Cost: 3
    Text: When you rez this asset and when your turn begins, place 1 power counter on this asset. The Runner gets -1 maximum hand size for each hosted power counter.
    '''

    def setUp(self):
        '''
        setup test environment for dr_vientiane_keeling_33106
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_dr_vientiane_keeling_33106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reaper_function_33107(unittest.TestCase):
    '''
    testing play functionality of reaper_function
    Cost: 3
    Text: When your turn begins, you may trash this asset to do 2 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for reaper_function_33107
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_reaper_function_33107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gaslight_33114(unittest.TestCase):
    '''
    testing play functionality of gaslight
    Cost: 0
    Text: When your turn begins, you may trash this asset. If you do, search R&D for an operation and reveal it. (Shuffle R&D after searching it.) Add that operation to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for gaslight_33114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_gaslight_33114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vera_ivanovna_shuyskaya_33115(unittest.TestCase):
    '''
    testing play functionality of vera_ivanovna_shuyskaya
    Cost: 3
    Text: Whenever an agenda is scored or stolen, you may reveal the grip. Trash 1 card revealed this way.
    '''

    def setUp(self):
        '''
        setup test environment for vera_ivanovna_shuyskaya_33115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_vera_ivanovna_shuyskaya_33115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hostile_architecture_33122(unittest.TestCase):
    '''
    testing play functionality of hostile_architecture
    Cost: 5
    Text: The first time each turn the Runner trashes any of your installed cards (including this asset), do 2 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for hostile_architecture_33122
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_hostile_architecture_33122()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_superdeep_borehole_33123(unittest.TestCase):
    '''
    testing play functionality of superdeep_borehole
    Cost: 6
    Text: When you rez this asset, load 6 bad publicity counters onto it. When it is empty, you win the game. When your turn begins, take 1 bad publicity from this asset.
    '''

    def setUp(self):
        '''
        setup test environment for superdeep_borehole_33123
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = asset_superdeep_borehole_33123()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")
