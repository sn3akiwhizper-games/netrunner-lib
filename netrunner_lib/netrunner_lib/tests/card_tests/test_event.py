
'''
test cases for card classes of type event
'''
import unittest

from netrunner_lib.cards._base_card_classes import Event
from netrunner_lib.cards.event import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
class Test_deja_vu_01002(unittest.TestCase):
    '''
    testing play functionality of deja_vu
    Cost: 2
    Text: Add 1 card (or up to 2 virus cards) from your heap to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for deja_vu_01002
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
        test_card = event_deja_vu_01002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_demolition_run_01003(unittest.TestCase):
    '''
    testing play functionality of demolition_run
    Cost: 2
    Text: Run HQ or R&D. Access -> 0 credits: Trash the card you are accessing.
    '''

    def setUp(self):
        '''
        setup test environment for demolition_run_01003
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
        test_card = event_demolition_run_01003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_stimhack_01004(unittest.TestCase):
    '''
    testing play functionality of stimhack
    Cost: 0
    Text: Place 9 credits on this event, then run any server. During that run, hosted credits are considered to be in your credit pool. When that run ends, suffer 1 core damage. This damage cannot be prevented.
    '''

    def setUp(self):
        '''
        setup test environment for stimhack_01004
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
        test_card = event_stimhack_01004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_account_siphon_01018(unittest.TestCase):
    '''
    testing play functionality of account_siphon
    Cost: 0
    Text: Run HQ. If successful, instead of breaching HQ, you may force the Corp to lose up to 5 credits, then you gain 2 credits for each credit lost and take 2 tags.
    '''

    def setUp(self):
        '''
        setup test environment for account_siphon_01018
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
        test_card = event_account_siphon_01018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_easy_mark_01019(unittest.TestCase):
    '''
    testing play functionality of easy_mark
    Cost: 0
    Text: Gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for easy_mark_01019
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
        test_card = event_easy_mark_01019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_forged_activation_orders_01020(unittest.TestCase):
    '''
    testing play functionality of forged_activation_orders
    Cost: 1
    Text: Choose 1 unrezzed piece of ice. The Corp may rez that ice. If they do not, they trash it.
    '''

    def setUp(self):
        '''
        setup test environment for forged_activation_orders_01020
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
        test_card = event_forged_activation_orders_01020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_inside_job_01021(unittest.TestCase):
    '''
    testing play functionality of inside_job
    Cost: 2
    Text: Run any server. The first time this run you encounter a piece of ice, bypass it.
    '''

    def setUp(self):
        '''
        setup test environment for inside_job_01021
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
        test_card = event_inside_job_01021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_special_order_01022(unittest.TestCase):
    '''
    testing play functionality of special_order
    Cost: 1
    Text: Search your stack for an icebreaker, reveal it, and add it to your grip. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for special_order_01022
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
        test_card = event_special_order_01022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_diesel_01034(unittest.TestCase):
    '''
    testing play functionality of diesel
    Cost: 0
    Text: Draw 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for diesel_01034
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
        test_card = event_diesel_01034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_modded_01035(unittest.TestCase):
    '''
    testing play functionality of modded
    Cost: 0
    Text: Install a program or piece of hardware, lowering the install cost by 3.
    '''

    def setUp(self):
        '''
        setup test environment for modded_01035
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
        test_card = event_modded_01035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_makers_eye_01036(unittest.TestCase):
    '''
    testing play functionality of the_makers_eye
    Cost: 2
    Text: Run R&D. If successful, access 2 additional cards when you breach R&D.
    '''

    def setUp(self):
        '''
        setup test environment for the_makers_eye_01036
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
        test_card = event_the_makers_eye_01036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tinkering_01037(unittest.TestCase):
    '''
    testing play functionality of tinkering
    Cost: 0
    Text: Choose a piece of ice. That ice gains sentry, code gate, and barrier until the end of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for tinkering_01037
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
        test_card = event_tinkering_01037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_infiltration_01049(unittest.TestCase):
    '''
    testing play functionality of infiltration
    Cost: 0
    Text: Gain 2 credits or expose 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for infiltration_01049
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
        test_card = event_infiltration_01049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sure_gamble_01050(unittest.TestCase):
    '''
    testing play functionality of sure_gamble
    Cost: 5
    Text: Gain 9 credits.
    '''

    def setUp(self):
        '''
        setup test environment for sure_gamble_01050
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
        test_card = event_sure_gamble_01050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vamp_02021(unittest.TestCase):
    '''
    testing play functionality of vamp
    Cost: 0
    Text: Run HQ. If successful, instead of breaching HQ, you may spend X credits. If you do, the Corp loses X credits. If you spent credits, take 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for vamp_02021
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
        test_card = event_vamp_02021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_satellite_uplink_02023(unittest.TestCase):
    '''
    testing play functionality of satellite_uplink
    Cost: 2
    Text: Expose up to 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for satellite_uplink_02023
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
        test_card = event_satellite_uplink_02023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_notoriety_02026(unittest.TestCase):
    '''
    testing play functionality of notoriety
    Cost: 1
    Text: Play only if you made a successful run on R&D, HQ, and Archives this turn. Add Notoriety to your score area as an agenda worth 1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for notoriety_02026
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
        test_card = event_notoriety_02026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_emergency_shutdown_02043(unittest.TestCase):
    '''
    testing play functionality of emergency_shutdown
    Cost: 0
    Text: Play only if you made a successful run on HQ this turn. Derez 1 installed piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for emergency_shutdown_02043
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
        test_card = event_emergency_shutdown_02043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_test_run_02047(unittest.TestCase):
    '''
    testing play functionality of test_run
    Cost: 3
    Text: Search either your stack or your heap for 1 program. (Shuffle your stack if you searched it.) Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for test_run_02047
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
        test_card = event_test_run_02047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_surge_02081(unittest.TestCase):
    '''
    testing play functionality of surge
    Cost: 0
    Text: Play only if you placed at least 1 virus counter on a program this turn. Place 2 virus counters on that program.
    '''

    def setUp(self):
        '''
        setup test environment for surge_02081
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
        test_card = event_surge_02081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_networking_02084(unittest.TestCase):
    '''
    testing play functionality of networking
    Cost: 0
    Text: Remove 1 tag. Then, you may pay 1 credit to add this event to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for networking_02084
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
        test_card = event_networking_02084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_quality_time_02087(unittest.TestCase):
    '''
    testing play functionality of quality_time
    Cost: 3
    Text: Draw 5 cards.
    '''

    def setUp(self):
        '''
        setup test environment for quality_time_02087
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
        test_card = event_quality_time_02087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kraken_02090(unittest.TestCase):
    '''
    testing play functionality of kraken
    Cost: 3
    Text: Play only if you stole an agenda this turn. Choose a server. The Corp trashes 1 piece of ice protecting that server.
    '''

    def setUp(self):
        '''
        setup test environment for kraken_02090
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
        test_card = event_kraken_02090()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_retrieval_run_02101(unittest.TestCase):
    '''
    testing play functionality of retrieval_run
    Cost: 3
    Text: Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for retrieval_run_02101
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
        test_card = event_retrieval_run_02101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_indexing_02106(unittest.TestCase):
    '''
    testing play functionality of indexing
    Cost: 0
    Text: Run R&D. If successful, instead of breaching R&D, you may look at the top 5 cards of R&D and arrange them in any order.
    '''

    def setUp(self):
        '''
        setup test environment for indexing_02106
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
        test_card = event_indexing_02106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_escher_03031(unittest.TestCase):
    '''
    testing play functionality of escher
    Cost: 3
    Text: Run HQ. If successful, instead of breaching HQ, rearrange any number of ice protecting all servers. (Do not rez or derez any ice or change the number of ice protecting any server.)
    '''

    def setUp(self):
        '''
        setup test environment for escher_03031
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
        test_card = event_escher_03031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_exploratory_romp_03032(unittest.TestCase):
    '''
    testing play functionality of exploratory_romp
    Cost: 1
    Text: Run any server. If successful, instead of breaching that server, remove up to 3 advancement counters from 1 card in the root of or protecting the attacked server.
    '''

    def setUp(self):
        '''
        setup test environment for exploratory_romp_03032
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
        test_card = event_exploratory_romp_03032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_freelance_coding_contract_03033(unittest.TestCase):
    '''
    testing play functionality of freelance_coding_contract
    Cost: 0
    Text: Trash up to 5 programs from your grip. Gain 2 credits for each program trashed.
    '''

    def setUp(self):
        '''
        setup test environment for freelance_coding_contract_03033
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
        test_card = event_freelance_coding_contract_03033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_scavenge_03034(unittest.TestCase):
    '''
    testing play functionality of scavenge
    Cost: 0
    Text: Trash 1 installed program. If you do, install 1 program from your grip or heap, paying X credits less. X is equal to the install cost of the program you trashed.
    '''

    def setUp(self):
        '''
        setup test environment for scavenge_03034
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
        test_card = event_scavenge_03034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_levy_ar_lab_access_03035(unittest.TestCase):
    '''
    testing play functionality of levy_ar_lab_access
    Cost: 5
    Text: Shuffle your grip and heap into your stack. Draw 5 cards. Remove Levy AR Lab Access from the game instead of trashing it.
    '''

    def setUp(self):
        '''
        setup test environment for levy_ar_lab_access_03035
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
        test_card = event_levy_ar_lab_access_03035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dirty_laundry_03052(unittest.TestCase):
    '''
    testing play functionality of dirty_laundry
    Cost: 2
    Text: Run any server. When that run ends, if it was successful, gain 5 credits.
    '''

    def setUp(self):
        '''
        setup test environment for dirty_laundry_03052
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
        test_card = event_dirty_laundry_03052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_frame_job_04001(unittest.TestCase):
    '''
    testing play functionality of frame_job
    Cost: 1
    Text: As an additional cost to play this event, spend click. Forfeit an agenda. If you do, give the Corp 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for frame_job_04001
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
        test_card = event_frame_job_04001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hostage_04004(unittest.TestCase):
    '''
    testing play functionality of hostage
    Cost: 1
    Text: As an additional cost to play this event, spend click. Search your stack for a connection, reveal it, and add it to your grip. You may install that connection (paying its install cost). Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for hostage_04004
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
        test_card = event_hostage_04004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_recon_04024(unittest.TestCase):
    '''
    testing play functionality of recon
    Cost: 1
    Text: Make a run. You may jack out when you encounter the first piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for recon_04024
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
        test_card = event_recon_04024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_eureka_04027(unittest.TestCase):
    '''
    testing play functionality of eureka
    Cost: 3
    Text: As an additional cost to play this event, spend click. Reveal the top card of your stack. You may install that card, lowering the install cost by 10 credits, if able; otherwise, trash it.
    '''

    def setUp(self):
        '''
        setup test environment for eureka_04027
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
        test_card = event_eureka_04027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_running_interference_04044(unittest.TestCase):
    '''
    testing play functionality of running_interference
    Cost: 4
    Text: As an additional cost to play this event, spend click. Make a run. During this run, the Corp must pay X credits as an additional cost to rez each piece of ice, where X is the rez cost of that ice.
    '''

    def setUp(self):
        '''
        setup test environment for running_interference_04044
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
        test_card = event_running_interference_04044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lawyer_up_04063(unittest.TestCase):
    '''
    testing play functionality of lawyer_up
    Cost: 2
    Text: As an additional cost to play this event, spend click. Remove up to 2 tags and draw 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for lawyer_up_04063
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
        test_card = event_lawyer_up_04063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_leverage_04064(unittest.TestCase):
    '''
    testing play functionality of leverage
    Cost: 1
    Text: Play only if you made a successful run on HQ this turn. Prevent all damage until the beginning of your next turn unless the Corp takes 2 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for leverage_04064
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
        test_card = event_leverage_04064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_quest_completed_04081(unittest.TestCase):
    '''
    testing play functionality of quest_completed
    Cost: 0
    Text: Play only if you made a successful run on R&D, HQ, and Archives this turn. Access 1 installed card (non-ice).
    '''

    def setUp(self):
        '''
        setup test environment for quest_completed_04081
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
        test_card = event_quest_completed_04081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_executive_wiretaps_04084(unittest.TestCase):
    '''
    testing play functionality of executive_wiretaps
    Cost: 4
    Text: As an additional cost to play this event, spend click. Reveal all cards in HQ.
    '''

    def setUp(self):
        '''
        setup test environment for executive_wiretaps_04084
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
        test_card = event_executive_wiretaps_04084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_blackmail_04089(unittest.TestCase):
    '''
    testing play functionality of blackmail
    Cost: 1
    Text: Play only if the Corp has at least 1 bad publicity. Make a run. The Corp cannot rez ice for the duration of this run.
    '''

    def setUp(self):
        '''
        setup test environment for blackmail_04089
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
        test_card = event_blackmail_04089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_singularity_04101(unittest.TestCase):
    '''
    testing play functionality of singularity
    Cost: 4
    Text: As an additional cost to play this event, spend click. Run a remote server. If successful, instead of breaching that server, trash all cards installed in the root of that server.
    '''

    def setUp(self):
        '''
        setup test environment for singularity_04101
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
        test_card = event_singularity_04101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_queens_gambit_04102(unittest.TestCase):
    '''
    testing play functionality of queens_gambit
    Cost: 0
    Text: As an additional cost to play this event, spend click. Place up to 3 advancement counters on 1 unrezzed card in the root of a remote server. Gain 2 credits for each counter placed this way. You cannot access that card for the remainder of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for queens_gambit_04102
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
        test_card = event_queens_gambit_04102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_power_nap_04107(unittest.TestCase):
    '''
    testing play functionality of power_nap
    Cost: 0
    Text: As an additional cost to play this event, spend click. Gain 2 credits. Gain an additional 1 credit for each double event in your heap.
    '''

    def setUp(self):
        '''
        setup test environment for power_nap_04107
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
        test_card = event_power_nap_04107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lucky_find_04109(unittest.TestCase):
    '''
    testing play functionality of lucky_find
    Cost: 3
    Text: As an additional cost to play this event, spend click. Gain 9 credits.
    '''

    def setUp(self):
        '''
        setup test environment for lucky_find_04109
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
        test_card = event_lucky_find_04109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_calling_in_favors_05031(unittest.TestCase):
    '''
    testing play functionality of calling_in_favors
    Cost: 0
    Text: Gain 1 credit for each installed connection resource.
    '''

    def setUp(self):
        '''
        setup test environment for calling_in_favors_05031
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
        test_card = event_calling_in_favors_05031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_early_bird_05032(unittest.TestCase):
    '''
    testing play functionality of early_bird
    Cost: 1
    Text: Play only as your first click. Gain click. Run any server.
    '''

    def setUp(self):
        '''
        setup test environment for early_bird_05032
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
        test_card = event_early_bird_05032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_express_delivery_05033(unittest.TestCase):
    '''
    testing play functionality of express_delivery
    Cost: 1
    Text: Look at the top 4 cards of your stack and add 1 of those cards to your grip. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for express_delivery_05033
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
        test_card = event_express_delivery_05033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_feint_05034(unittest.TestCase):
    '''
    testing play functionality of feint
    Cost: 2
    Text: Run HQ. The first 2 times this run you encounter a piece of ice, bypass that ice. If successful, you cannot breach HQ.
    '''

    def setUp(self):
        '''
        setup test environment for feint_05034
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
        test_card = event_feint_05034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_legwork_05035(unittest.TestCase):
    '''
    testing play functionality of legwork
    Cost: 2
    Text: Run HQ. If successful, access 2 additional cards when you breach HQ.
    '''

    def setUp(self):
        '''
        setup test environment for legwork_05035
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
        test_card = event_legwork_05035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_planned_assault_05036(unittest.TestCase):
    '''
    testing play functionality of planned_assault
    Cost: 2
    Text: As an additional cost to play this event, spend click. Search your stack for a run event and play that run event (paying its play cost), ignoring any additional costs. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for planned_assault_05036
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
        test_card = event_planned_assault_05036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_push_your_luck_05047(unittest.TestCase):
    '''
    testing play functionality of push_your_luck
    Cost: 2
    Text: Secretly spend any number of credits. The Corp guesses if you spent an even or odd amount. Reveal spent credits. If the Corp guessed incorrectly, gain credits equal to twice the amount spent.
    '''

    def setUp(self):
        '''
        setup test environment for push_your_luck_05047
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
        test_card = event_push_your_luck_05047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mass_install_05051(unittest.TestCase):
    '''
    testing play functionality of mass_install
    Cost: 1
    Text: Install up to 3 programs from your grip (paying the install costs).
    '''

    def setUp(self):
        '''
        setup test environment for mass_install_05051
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
        test_card = event_mass_install_05051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cyber_threat_06013(unittest.TestCase):
    '''
    testing play functionality of cyber_threat
    Cost: 1
    Text: Play only as your first click. Choose a server. The Corp may rez 1 piece of ice protecting that server. If they do not, run that server. The Corp cannot rez ice during that run.
    '''

    def setUp(self):
        '''
        setup test environment for cyber_threat_06013
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
        test_card = event_cyber_threat_06013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paper_tripping_06015(unittest.TestCase):
    '''
    testing play functionality of paper_tripping
    Cost: 4
    Text: Play only as your first click. Remove all tags.
    '''

    def setUp(self):
        '''
        setup test environment for paper_tripping_06015
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
        test_card = event_paper_tripping_06015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_social_engineering_06018(unittest.TestCase):
    '''
    testing play functionality of social_engineering
    Cost: 2
    Text: Play only as your first click. Choose an unrezzed piece of ice. If the Corp rezzes that piece of ice this turn, gain credits equal to its rez cost.
    '''

    def setUp(self):
        '''
        setup test environment for social_engineering_06018
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
        test_card = event_social_engineering_06018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_scrubbed_06034(unittest.TestCase):
    '''
    testing play functionality of scrubbed
    Cost: 2
    Text: This card is not trashed until another current is played or an agenda is scored. The first piece of ice encountered each turn has -2 strength for the remainder of the run.
    '''

    def setUp(self):
        '''
        setup test environment for scrubbed_06034
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
        test_card = event_scrubbed_06034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_three_steps_ahead_06035(unittest.TestCase):
    '''
    testing play functionality of three_steps_ahead
    Cost: 1
    Text: Play only as your first click. When this turn ends, gain 2 credits for each successful run you made during it.
    '''

    def setUp(self):
        '''
        setup test environment for three_steps_ahead_06035
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
        test_card = event_three_steps_ahead_06035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_unscheduled_maintenance_06036(unittest.TestCase):
    '''
    testing play functionality of unscheduled_maintenance
    Cost: 1
    Text: This card is not trashed until another current is played or an agenda is scored. The Corp cannot install more than 1 piece of ice each turn.
    '''

    def setUp(self):
        '''
        setup test environment for unscheduled_maintenance_06036
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
        test_card = event_unscheduled_maintenance_06036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_net_celebrity_06038(unittest.TestCase):
    '''
    testing play functionality of net_celebrity
    Cost: 1
    Text: This card is not trashed until another current is played or an agenda is scored. 1 recurring credit Use this credit during a run.
    '''

    def setUp(self):
        '''
        setup test environment for net_celebrity_06038
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
        test_card = event_net_celebrity_06038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_inject_06073(unittest.TestCase):
    '''
    testing play functionality of inject
    Cost: 1
    Text: Reveal the top 4 cards of your stack and trash all programs revealed. Gain 1 credit for each program trashed, and add the rest of the revealed cards to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for inject_06073
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
        test_card = event_inject_06073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tradein_06078(unittest.TestCase):
    '''
    testing play functionality of tradein
    Cost: 1
    Text: As an additional cost to play this event, trash an installed piece of hardware. Gain credits equal to half the install cost of the trashed hardware (rounded down) and search your stack for a piece of hardware, reveal it, and add it to your grip. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for tradein_06078
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
        test_card = event_tradein_06078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_code_siphon_06115(unittest.TestCase):
    '''
    testing play functionality of code_siphon
    Cost: 0
    Text: Run R&D. If successful, instead of breaching R&D, you may search your stack for 1 program. Install it, paying 3 credits less for each piece of ice protecting R&D, and then take 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for code_siphon_06115
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
        test_card = event_code_siphon_06115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bribery_06118(unittest.TestCase):
    '''
    testing play functionality of bribery
    Cost: None
    Text: Make a run. During this run, the Corp must pay X credits as an additional cost to rez the first unrezzed piece of ice approached.
    '''

    def setUp(self):
        '''
        setup test environment for bribery_06118
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
        test_card = event_bribery_06118()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_amped_up_07031(unittest.TestCase):
    '''
    testing play functionality of amped_up
    Cost: 1
    Text: Gain click click click and suffer 1 core damage. This damage cannot be prevented.
    '''

    def setUp(self):
        '''
        setup test environment for amped_up_07031
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
        test_card = event_amped_up_07031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ive_had_worse_07032(unittest.TestCase):
    '''
    testing play functionality of ive_had_worse
    Cost: 1
    Text: Draw 3 cards. Whenever I've Had Worse is trashed by taking net or meat damage, draw 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for ive_had_worse_07032
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
        test_card = event_ive_had_worse_07032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_itinerant_protesters_07033(unittest.TestCase):
    '''
    testing play functionality of itinerant_protesters
    Cost: 2
    Text: This event is not trashed until another current is played or an agenda is scored. The Corp gets -1 maximum hand size for each bad publicity they have.
    '''

    def setUp(self):
        '''
        setup test environment for itinerant_protesters_07033
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
        test_card = event_itinerant_protesters_07033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_showing_off_07034(unittest.TestCase):
    '''
    testing play functionality of showing_off
    Cost: 2
    Text: Run R&D. If successful, when you breach R&D, access cards from the bottom of R&D instead of the top.
    '''

    def setUp(self):
        '''
        setup test environment for showing_off_07034
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
        test_card = event_showing_off_07034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wanton_destruction_07035(unittest.TestCase):
    '''
    testing play functionality of wanton_destruction
    Cost: 1
    Text: Run HQ. If successful, instead of breaching HQ, you may spend any number of click to force the Corp to trash that many cards from HQ at random.
    '''

    def setUp(self):
        '''
        setup test environment for wanton_destruction_07035
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
        test_card = event_wanton_destruction_07035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_day_job_07036(unittest.TestCase):
    '''
    testing play functionality of day_job
    Cost: 2
    Text: As an additional cost to play this event, spend click click click. Gain 10 credits.
    '''

    def setUp(self):
        '''
        setup test environment for day_job_07036
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
        test_card = event_day_job_07036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_forked_07037(unittest.TestCase):
    '''
    testing play functionality of forked
    Cost: 2
    Text: Run any server. The first time you fully break a sentry during that run, trash that sentry.
    '''

    def setUp(self):
        '''
        setup test environment for forked_07037
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
        test_card = event_forked_07037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_knifed_07038(unittest.TestCase):
    '''
    testing play functionality of knifed
    Cost: 1
    Text: Run any server. The first time you fully break a barrier during that run, trash that barrier.
    '''

    def setUp(self):
        '''
        setup test environment for knifed_07038
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
        test_card = event_knifed_07038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spooned_07039(unittest.TestCase):
    '''
    testing play functionality of spooned
    Cost: 2
    Text: Run any server. The first time you fully break a code gate during that run, trash that code gate.
    '''

    def setUp(self):
        '''
        setup test environment for spooned_07039
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
        test_card = event_spooned_07039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_uninstall_07053(unittest.TestCase):
    '''
    testing play functionality of uninstall
    Cost: 0
    Text: Add an installed program or piece of hardware to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for uninstall_07053
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
        test_card = event_uninstall_07053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_traffic_jam_08008(unittest.TestCase):
    '''
    testing play functionality of traffic_jam
    Cost: 2
    Text: This card is not trashed until another current is played or an agenda is scored. The advancement requirement of each agenda is increased by 1 for each copy of that agenda in the Corp's score area.
    '''

    def setUp(self):
        '''
        setup test environment for traffic_jam_08008
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
        test_card = event_traffic_jam_08008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hacktivist_meeting_08021(unittest.TestCase):
    '''
    testing play functionality of hacktivist_meeting
    Cost: 1
    Text: This card is not trashed until another current is played or an agenda is scored. As an additional cost to rez non-ice cards, the Corp must randomly trash a card from HQ.
    '''

    def setUp(self):
        '''
        setup test environment for hacktivist_meeting_08021
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
        test_card = event_hacktivist_meeting_08021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_career_fair_08023(unittest.TestCase):
    '''
    testing play functionality of career_fair
    Cost: 0
    Text: Install 1 resource from your grip, paying 3 credits less.
    '''

    def setUp(self):
        '''
        setup test environment for career_fair_08023
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
        test_card = event_career_fair_08023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_game_day_08026(unittest.TestCase):
    '''
    testing play functionality of game_day
    Cost: 1
    Text: As an additional cost to play this event, spend click. If you have fewer cards in your grip than your maximum hand size, draw cards until you have cards in your grip equal to your maximum hand size.
    '''

    def setUp(self):
        '''
        setup test environment for game_day_08026
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
        test_card = event_game_day_08026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_immolation_script_08041(unittest.TestCase):
    '''
    testing play functionality of immolation_script
    Cost: 0
    Text: Run Archives. If successful, whenever you would access a faceup piece of ice in Archives this run, you may instead trash 1 rezzed copy of that ice. Use this ability only once this run.
    '''

    def setUp(self):
        '''
        setup test environment for immolation_script_08041
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
        test_card = event_immolation_script_08041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_drive_by_08064(unittest.TestCase):
    '''
    testing play functionality of drive_by
    Cost: 0
    Text: As an additional cost to play this event, spend click. Expose 1 card installed in the root of a remote server. If you do and that card is an asset or upgrade, trash it.
    '''

    def setUp(self):
        '''
        setup test environment for drive_by_08064
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
        test_card = event_drive_by_08064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_power_to_the_people_08101(unittest.TestCase):
    '''
    testing play functionality of power_to_the_people
    Cost: 0
    Text: Play only as your first click. The first time you access an agenda this turn, gain 7 credits.
    '''

    def setUp(self):
        '''
        setup test environment for power_to_the_people_08101
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
        test_card = event_power_to_the_people_08101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fisk_investment_seminar_08105(unittest.TestCase):
    '''
    testing play functionality of fisk_investment_seminar
    Cost: 0
    Text: Play only as your first click. Each player draws 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for fisk_investment_seminar_08105
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
        test_card = event_fisk_investment_seminar_08105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_apocalypse_09030(unittest.TestCase):
    '''
    testing play functionality of apocalypse
    Cost: 3
    Text: Play only if you made a successful run on HQ, R&D and Archives this turn. Trash all installed Corp cards. Turn all installed Runner cards facedown.
    '''

    def setUp(self):
        '''
        setup test environment for apocalypse_09030
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
        test_card = event_apocalypse_09030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_prey_09031(unittest.TestCase):
    '''
    testing play functionality of prey
    Cost: 0
    Text: Make a run. Once during this run, when you pass a piece of ice, you may trash a number of your installed cards equal to the strength of that ice. If you do, trash that ice.
    '''

    def setUp(self):
        '''
        setup test environment for prey_09031
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
        test_card = event_prey_09031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_independent_thinking_09038(unittest.TestCase):
    '''
    testing play functionality of independent_thinking
    Cost: 1
    Text: Trash up to 5 of your installed cards. Draw 1 card for each card trashed (or 2 cards for each card trashed if you trashed at least 1 directive).
    '''

    def setUp(self):
        '''
        setup test environment for independent_thinking_09038
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
        test_card = event_independent_thinking_09038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_employee_strike_09053(unittest.TestCase):
    '''
    testing play functionality of employee_strike
    Cost: 1
    Text: This event is not trashed until another current is played or an agenda is scored. The Corp's identity loses its printed abilities.
    '''

    def setUp(self):
        '''
        setup test environment for employee_strike_09053
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
        test_card = event_employee_strike_09053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_windfall_09054(unittest.TestCase):
    '''
    testing play functionality of windfall
    Cost: 0
    Text: Shuffle your stack. Trash the top card of your stack. Gain X credits where X is equal to the install cost of that card.
    '''

    def setUp(self):
        '''
        setup test environment for windfall_09054
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
        test_card = event_windfall_09054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_run_amok_10001(unittest.TestCase):
    '''
    testing play functionality of run_amok
    Cost: 3
    Text: Make a run. When the run ends, trash 1 piece of ice that was rezzed during this run.
    '''

    def setUp(self):
        '''
        setup test environment for run_amok_10001
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
        test_card = event_run_amok_10001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_highstakes_job_10004(unittest.TestCase):
    '''
    testing play functionality of highstakes_job
    Cost: 6
    Text: Make a run on a server with at least 1 piece of unrezzed ice. When the run ends, gain 12 credits if it was successful.
    '''

    def setUp(self):
        '''
        setup test environment for highstakes_job_10004
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
        test_card = event_highstakes_job_10004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cbi_raid_10022(unittest.TestCase):
    '''
    testing play functionality of cbi_raid
    Cost: 3
    Text: Run HQ. If successful, instead of breaching HQ, the Corp adds all cards in HQ to the top of R&D in the order of their choice.
    '''

    def setUp(self):
        '''
        setup test environment for cbi_raid_10022
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
        test_card = event_cbi_raid_10022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_scandal_10025(unittest.TestCase):
    '''
    testing play functionality of corporate_scandal
    Cost: 3
    Text: This card is not trashed until another current is played or an agenda is scored. The Corp has 1 additional bad publicity (even if they have 0).
    '''

    def setUp(self):
        '''
        setup test environment for corporate_scandal_10025
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
        test_card = event_corporate_scandal_10025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_populist_rally_10026(unittest.TestCase):
    '''
    testing play functionality of populist_rally
    Cost: 2
    Text: Play only if you have a seedy card installed. The Corp gets -1 allotted click for their next turn.
    '''

    def setUp(self):
        '''
        setup test environment for populist_rally_10026
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
        test_card = event_populist_rally_10026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_political_graffiti_10039(unittest.TestCase):
    '''
    testing play functionality of political_graffiti
    Cost: 0
    Text: Run Archives. If successful, instead of breaching Archives, host this event on an agenda in the Corp's score area as a condition counter with "Host agenda is worth 1 less agenda point. When the Corp purges virus counters, trash this counter."
    '''

    def setUp(self):
        '''
        setup test environment for political_graffiti_10039
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
        test_card = event_political_graffiti_10039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_freedom_through_equality_10045(unittest.TestCase):
    '''
    testing play functionality of freedom_through_equality
    Cost: 3
    Text: This card is not trashed until another current is played or an agenda is scored. When you steal an agenda, add "Freedom Through Equality" to your score area as an agenda worth 1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for freedom_through_equality_10045
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
        test_card = event_freedom_through_equality_10045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_making_an_entrance_10058(unittest.TestCase):
    '''
    testing play functionality of making_an_entrance
    Cost: 0
    Text: Play only as your first click. Look at the top 6 cards of your stack. You may trash any of those cards and arrange the rest in any order.
    '''

    def setUp(self):
        '''
        setup test environment for making_an_entrance_10058
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
        test_card = event_making_an_entrance_10058()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_exclusive_party_10060(unittest.TestCase):
    '''
    testing play functionality of exclusive_party
    Cost: 0
    Text: Draw 1 card. Gain 1 credit for each copy of Exclusive Party in your heap. Limit 6 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for exclusive_party_10060
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
        test_card = event_exclusive_party_10060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_noble_path_10077(unittest.TestCase):
    '''
    testing play functionality of the_noble_path
    Cost: 0
    Text: Trash your grip. Make a run. Prevent all damage during this run.
    '''

    def setUp(self):
        '''
        setup test environment for the_noble_path_10077
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
        test_card = event_the_noble_path_10077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_information_sifting_10079(unittest.TestCase):
    '''
    testing play functionality of information_sifting
    Cost: 1
    Text: Run HQ. If successful, instead of breaching HQ, the Corp separates all cards in HQ into 2 facedown piles. Choose 1 of the piles. Access each card in the chosen pile.
    '''

    def setUp(self):
        '''
        setup test environment for information_sifting_10079
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
        test_card = event_information_sifting_10079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_out_of_the_ashes_10080(unittest.TestCase):
    '''
    testing play functionality of out_of_the_ashes
    Cost: 1
    Text: Make a run. When your turn begins, if Out of the Ashes is in your heap, you may remove it from the game to make a run. Limit 6 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for out_of_the_ashes_10080
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
        test_card = event_out_of_the_ashes_10080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rebirth_10083(unittest.TestCase):
    '''
    testing play functionality of rebirth
    Cost: 0
    Text: Switch your identity with another identity from the same faction. Remove Rebirth from the game instead of trashing it. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for rebirth_10083
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
        test_card = event_rebirth_10083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fear_the_masses_10096(unittest.TestCase):
    '''
    testing play functionality of fear_the_masses
    Cost: 1
    Text: Run HQ. If successful, instead of breaching HQ, reveal any number of copies of Fear the Masses from your grip. The Corp trashes X cards from the top of R&D, where X is equal to 1 plus the number of cards you revealed. Limit 6 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for fear_the_masses_10096
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
        test_card = event_fear_the_masses_10096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_price_of_freedom_10100(unittest.TestCase):
    '''
    testing play functionality of the_price_of_freedom
    Cost: 0
    Text: As an additional cost to play this event, trash 1 installed connection resource. The Corp cannot advance cards during their next turn. Remove this event from the game.
    '''

    def setUp(self):
        '''
        setup test environment for the_price_of_freedom_10100
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
        test_card = event_the_price_of_freedom_10100()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rigged_results_10102(unittest.TestCase):
    '''
    testing play functionality of rigged_results
    Cost: 0
    Text: Secretly spend up to 2 credits. The Corp guesses how much you spent. Reveal spent credits. If the Corp guessed incorrectly, choose a piece of ice protecting a server and run that server. The first time during this run you encounter the chosen ice, bypass it.
    '''

    def setUp(self):
        '''
        setup test environment for rigged_results_10102
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
        test_card = event_rigged_results_10102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_system_outage_11001(unittest.TestCase):
    '''
    testing play functionality of system_outage
    Cost: 1
    Text: This event is not trashed until another current is played or an agenda is scored. Whenever the Corp draws 1 or more cards, if it is not the first time they have drawn cards this turn, they lose 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for system_outage_11001
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
        test_card = event_system_outage_11001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_another_day_another_paycheck_11007(unittest.TestCase):
    '''
    testing play functionality of another_day_another_paycheck
    Cost: 0
    Text: This card is not trashed until another current is played or an agenda is scored. Whenever you steal an agenda, force the Corp to "Trace[0]. If unsuccessful, the Runner gains credits equal to the number of agenda points in both players' score areas."
    '''

    def setUp(self):
        '''
        setup test environment for another_day_another_paycheck_11007
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
        test_card = event_another_day_another_paycheck_11007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_deuces_wild_11008(unittest.TestCase):
    '''
    testing play functionality of deuces_wild
    Cost: 2
    Text: Resolve two of the following in any order: * Gain 3 credits. * Draw 2 cards. * Remove 1 tag. * Expose 1 piece of ice, then make a run.
    '''

    def setUp(self):
        '''
        setup test environment for deuces_wild_11008
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
        test_card = event_deuces_wild_11008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_injection_attack_11009(unittest.TestCase):
    '''
    testing play functionality of injection_attack
    Cost: 1
    Text: Choose 1 installed icebreaker and run any server. During that run, the chosen icebreaker gets +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for injection_attack_11009
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
        test_card = event_injection_attack_11009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_credit_crash_11021(unittest.TestCase):
    '''
    testing play functionality of credit_crash
    Cost: 1
    Text: Make a run. Trash the first non-agenda card you access during this run at no cost. The Corp can spend credits equal to the rez or play cost of the accessed card to prevent this trash.
    '''

    def setUp(self):
        '''
        setup test environment for credit_crash_11021
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
        test_card = event_credit_crash_11021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rumor_mill_11022(unittest.TestCase):
    '''
    testing play functionality of rumor_mill
    Cost: 1
    Text: This card is not trashed until another current is played or an agenda is scored. Each unique non-region asset and upgrade loses its printed abilities.
    '''

    def setUp(self):
        '''
        setup test environment for rumor_mill_11022
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
        test_card = event_rumor_mill_11022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_breach_11028(unittest.TestCase):
    '''
    testing play functionality of data_breach
    Cost: 0
    Text: Make a run on R&D. If successful, you may make another run on R&D when this run ends.
    '''

    def setUp(self):
        '''
        setup test environment for data_breach_11028
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
        test_card = event_data_breach_11028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_en_passant_11061(unittest.TestCase):
    '''
    testing play functionality of en_passant
    Cost: 0
    Text: Play only if you made a successful run this turn. Trash 1 unrezzed piece of ice you passed during your last run.
    '''

    def setUp(self):
        '''
        setup test environment for en_passant_11061
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
        test_card = event_en_passant_11061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_frantic_coding_11062(unittest.TestCase):
    '''
    testing play functionality of frantic_coding
    Cost: 3
    Text: Look at the top 10 cards of your stack. If any of those cards are programs, you may install one of them, lowering the install cost by 5. Trash the rest of those cards.
    '''

    def setUp(self):
        '''
        setup test environment for frantic_coding_11062
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
        test_card = event_frantic_coding_11062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_government_investigations_11069(unittest.TestCase):
    '''
    testing play functionality of government_investigations
    Cost: 0
    Text: This card is not trashed until another current is played or an agenda is scored. While secretly spending credits, players cannot spend 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for government_investigations_11069
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
        test_card = event_government_investigations_11069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_on_the_lam_11082(unittest.TestCase):
    '''
    testing play functionality of on_the_lam
    Cost: 3
    Text: Install On the Lam on a resource as a hosted condition counter with the text "trash: Avoid up to 3 tags or prevent up to 3 damage."
    '''

    def setUp(self):
        '''
        setup test environment for on_the_lam_11082
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
        test_card = event_on_the_lam_11082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cold_read_11083(unittest.TestCase):
    '''
    testing play functionality of cold_read
    Cost: 0
    Text: Place 4 credits on this event, then run any server. You can spend hosted credits during that run. When that run ends, trash 1 installed program you used during that run. Trashing a program this way cannot be prevented.
    '''

    def setUp(self):
        '''
        setup test environment for cold_read_11083
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
        test_card = event_cold_read_11083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_interdiction_11087(unittest.TestCase):
    '''
    testing play functionality of interdiction
    Cost: 1
    Text: This card is not trashed until another current is played or an agenda is scored. The Corp cannot rez non-ice cards during the Runner's turn.
    '''

    def setUp(self):
        '''
        setup test environment for interdiction_11087
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
        test_card = event_interdiction_11087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_encore_11107(unittest.TestCase):
    '''
    testing play functionality of encore
    Cost: 0
    Text: Play only if you made a successful run on R&D, HQ, and Archives this turn. Take an additional turn after this one. Remove Encore from the game instead of trashing it.
    '''

    def setUp(self):
        '''
        setup test environment for encore_11107
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
        test_card = event_encore_11107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_peace_in_our_time_11109(unittest.TestCase):
    '''
    testing play functionality of peace_in_our_time
    Cost: 1
    Text: Play only as your first click and only if the Corp scored no agendas during their last turn. Gain 10 credits. The Corp gains 5 credits. You cannot make any runs this turn.
    '''

    def setUp(self):
        '''
        setup test environment for peace_in_our_time_11109
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
        test_card = event_peace_in_our_time_11109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pushing_the_envelope_12001(unittest.TestCase):
    '''
    testing play functionality of pushing_the_envelope
    Cost: 3
    Text: Make a run. If you have 2 or fewer cards in your grip, each installed icebreaker has +2 strength until the end of the run.
    '''

    def setUp(self):
        '''
        setup test environment for pushing_the_envelope_12001
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
        test_card = event_pushing_the_envelope_12001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_exploit_12004(unittest.TestCase):
    '''
    testing play functionality of exploit
    Cost: 2
    Text: Play only if you made a successful run on R&D, HQ, and Archives this turn. Derez up to 3 pieces of ice.
    '''

    def setUp(self):
        '''
        setup test environment for exploit_12004
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
        test_card = event_exploit_12004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spot_the_prey_12005(unittest.TestCase):
    '''
    testing play functionality of spot_the_prey
    Cost: 2
    Text: Expose 1 non-ice card, then make a run.
    '''

    def setUp(self):
        '''
        setup test environment for spot_the_prey_12005
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
        test_card = event_spot_the_prey_12005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mad_dash_12008(unittest.TestCase):
    '''
    testing play functionality of mad_dash
    Cost: 0
    Text: Make a run. When this run ends, add Mad Dash to your score area as an agenda worth 1 agenda point if you stole at least 1 agenda during the run; otherwise, suffer 1 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for mad_dash_12008
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
        test_card = event_mad_dash_12008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mobius_12024(unittest.TestCase):
    '''
    testing play functionality of mobius
    Cost: 0
    Text: Make a run on R&D. If successful, you may make another run on R&D when this run ends. If the second run is successful, gain 4 credits.
    '''

    def setUp(self):
        '''
        setup test environment for mobius_12024
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
        test_card = event_mobius_12024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_system_seizure_12026(unittest.TestCase):
    '''
    testing play functionality of system_seizure
    Cost: 0
    Text: This event is not trashed until another current is played or an agenda is scored. Interrupt -> The first time each turn you would increase the strength of an icebreaker, for the remainder of the run that icebreaker gains "Abilities that increase this program's strength last for the remainder of the run (instead of any shorter duration)."
    '''

    def setUp(self):
        '''
        setup test environment for system_seizure_12026
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
        test_card = event_system_seizure_12026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_build_script_12028(unittest.TestCase):
    '''
    testing play functionality of build_script
    Cost: 0
    Text: Gain 1 credit and draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for build_script_12028
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
        test_card = event_build_script_12028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mars_for_martians_12081(unittest.TestCase):
    '''
    testing play functionality of mars_for_martians
    Cost: 0
    Text: Play only as your first click. Draw 1 card for each installed clan resource. Gain 1 credit for each tag you have.
    '''

    def setUp(self):
        '''
        setup test environment for mars_for_martians_12081
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
        test_card = event_mars_for_martians_12081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_leave_no_trace_12083(unittest.TestCase):
    '''
    testing play functionality of leave_no_trace
    Cost: 2
    Text: Make a run. When the run ends, derez all ice that was rezzed during this run.
    '''

    def setUp(self):
        '''
        setup test environment for leave_no_trace_12083
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
        test_card = event_leave_no_trace_12083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rip_deal_12084(unittest.TestCase):
    '''
    testing play functionality of rip_deal
    Cost: 3
    Text: Run HQ. If successful, when you determine the number of cards in HQ you are allowed to access during this run's breach of HQ, you may add that many cards from your heap to your grip. If you do, you cannot access any cards in HQ during this breach. (You can still access cards in the root of HQ.) When the run ends, remove this event from the game.
    '''

    def setUp(self):
        '''
        setup test environment for rip_deal_12084
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
        test_card = event_rip_deal_12084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lean_and_mean_12086(unittest.TestCase):
    '''
    testing play functionality of lean_and_mean
    Cost: 2
    Text: Make a run. If you have 3 or fewer programs installed, all icebreakers have +2 strength during this run.
    '''

    def setUp(self):
        '''
        setup test environment for lean_and_mean_12086
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
        test_card = event_lean_and_mean_12086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mining_accident_12101(unittest.TestCase):
    '''
    testing play functionality of mining_accident
    Cost: 2
    Text: Play only if you made a successful run on a central server this turn. The Corp must pay 5 credits or take 1 bad publicity. Remove Mining Accident from the game instead of trashing it.
    '''

    def setUp(self):
        '''
        setup test environment for mining_accident_12101
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
        test_card = event_mining_accident_12101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dianas_hunt_12106(unittest.TestCase):
    '''
    testing play functionality of dianas_hunt
    Cost: 4
    Text: Make a run. Whenever you encounter a piece of ice during this run, you may install a program from your grip, ignoring all costs. When this run ends, trash all programs installed using Diana's Hunt.
    '''

    def setUp(self):
        '''
        setup test environment for dianas_hunt_12106
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
        test_card = event_dianas_hunt_12106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reshape_12107(unittest.TestCase):
    '''
    testing play functionality of reshape
    Cost: 3
    Text: Swap 2 pieces of unrezzed ice.
    '''

    def setUp(self):
        '''
        setup test environment for reshape_12107
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
        test_card = event_reshape_12107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bruteforcehack_13002(unittest.TestCase):
    '''
    testing play functionality of bruteforcehack
    Cost: None
    Text: As an additional cost to play this event, spend click. Derez a piece of ice that has a rez cost of X or lower.
    '''

    def setUp(self):
        '''
        setup test environment for bruteforcehack_13002
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
        test_card = event_bruteforcehack_13002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spear_phishing_13003(unittest.TestCase):
    '''
    testing play functionality of spear_phishing
    Cost: 2
    Text: Make a run. When you encounter the innermost piece of ice protecting that server, bypass it.
    '''

    def setUp(self):
        '''
        setup test environment for spear_phishing_13003
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
        test_card = event_spear_phishing_13003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_syn_attack_13004(unittest.TestCase):
    '''
    testing play functionality of syn_attack
    Cost: 2
    Text: As an additional cost to play this event, spend click. The Corp must either discard 2 cards or draw 4 cards.
    '''

    def setUp(self):
        '''
        setup test environment for syn_attack_13004
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
        test_card = event_syn_attack_13004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_careful_planning_13013(unittest.TestCase):
    '''
    testing play functionality of careful_planning
    Cost: 3
    Text: Play only as your first click. Choose 1 card installed in the root of or protecting a remote server. That card cannot be rezzed this turn.
    '''

    def setUp(self):
        '''
        setup test environment for careful_planning_13013
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
        test_card = event_careful_planning_13013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_deep_data_mining_13014(unittest.TestCase):
    '''
    testing play functionality of deep_data_mining
    Cost: 3
    Text: Run R&D. If successful, access X additional cards when you breach R&D. X is equal to your unused MU or 4, whichever is less.
    '''

    def setUp(self):
        '''
        setup test environment for deep_data_mining_13014
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
        test_card = event_deep_data_mining_13014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_process_automation_13023(unittest.TestCase):
    '''
    testing play functionality of process_automation
    Cost: 0
    Text: Gain 2 credits and draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for process_automation_13023
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
        test_card = event_process_automation_13023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_security_leak_14009(unittest.TestCase):
    '''
    testing play functionality of security_leak
    Cost: 0
    Text: This card is not trashed until another current is played or an agenda is scored. As an additional cost to advance a card, the Corp must pay 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for security_leak_14009
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
        test_card = event_security_leak_14009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_demolition_run_20002(unittest.TestCase):
    '''
    testing play functionality of demolition_run
    Cost: 2
    Text: Run HQ or R&D. Access -> 0 credits: Trash the card you are accessing.
    '''

    def setUp(self):
        '''
        setup test environment for demolition_run_20002
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
        test_card = event_demolition_run_20002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_retrieval_run_20003(unittest.TestCase):
    '''
    testing play functionality of retrieval_run
    Cost: 3
    Text: Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for retrieval_run_20003
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
        test_card = event_retrieval_run_20003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_singularity_20004(unittest.TestCase):
    '''
    testing play functionality of singularity
    Cost: 4
    Text: As an additional cost to play this event, spend click. Run a remote server. If successful, instead of breaching that server, trash all cards installed in the root of that server.
    '''

    def setUp(self):
        '''
        setup test environment for singularity_20004
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
        test_card = event_singularity_20004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_stimhack_20005(unittest.TestCase):
    '''
    testing play functionality of stimhack
    Cost: 0
    Text: Place 9 credits on this event, then run any server. During that run, hosted credits are considered to be in your credit pool. When that run ends, suffer 1 core damage. This damage cannot be prevented.
    '''

    def setUp(self):
        '''
        setup test environment for stimhack_20005
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
        test_card = event_stimhack_20005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_easy_mark_20020(unittest.TestCase):
    '''
    testing play functionality of easy_mark
    Cost: 0
    Text: Gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for easy_mark_20020
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
        test_card = event_easy_mark_20020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_emergency_shutdown_20021(unittest.TestCase):
    '''
    testing play functionality of emergency_shutdown
    Cost: 0
    Text: Play only if you made a successful run on HQ this turn. Derez 1 installed piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for emergency_shutdown_20021
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
        test_card = event_emergency_shutdown_20021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_forged_activation_orders_20022(unittest.TestCase):
    '''
    testing play functionality of forged_activation_orders
    Cost: 1
    Text: Choose 1 unrezzed piece of ice. The Corp may rez that ice. If they do not, they trash it.
    '''

    def setUp(self):
        '''
        setup test environment for forged_activation_orders_20022
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
        test_card = event_forged_activation_orders_20022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_inside_job_20023(unittest.TestCase):
    '''
    testing play functionality of inside_job
    Cost: 2
    Text: Run any server. The first time this run you encounter a piece of ice, bypass it.
    '''

    def setUp(self):
        '''
        setup test environment for inside_job_20023
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
        test_card = event_inside_job_20023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_special_order_20024(unittest.TestCase):
    '''
    testing play functionality of special_order
    Cost: 1
    Text: Search your stack for an icebreaker, reveal it, and add it to your grip. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for special_order_20024
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
        test_card = event_special_order_20024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_diesel_20038(unittest.TestCase):
    '''
    testing play functionality of diesel
    Cost: 0
    Text: Draw 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for diesel_20038
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
        test_card = event_diesel_20038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_indexing_20039(unittest.TestCase):
    '''
    testing play functionality of indexing
    Cost: 0
    Text: Run R&D. If successful, instead of breaching R&D, you may look at the top 5 cards of R&D and arrange them in any order.
    '''

    def setUp(self):
        '''
        setup test environment for indexing_20039
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
        test_card = event_indexing_20039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_modded_20040(unittest.TestCase):
    '''
    testing play functionality of modded
    Cost: 0
    Text: Install a program or piece of hardware, lowering the install cost by 3.
    '''

    def setUp(self):
        '''
        setup test environment for modded_20040
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
        test_card = event_modded_20040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_notoriety_20041(unittest.TestCase):
    '''
    testing play functionality of notoriety
    Cost: 1
    Text: Play only if you made a successful run on R&D, HQ, and Archives this turn. Add Notoriety to your score area as an agenda worth 1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for notoriety_20041
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
        test_card = event_notoriety_20041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_test_run_20042(unittest.TestCase):
    '''
    testing play functionality of test_run
    Cost: 3
    Text: Search either your stack or your heap for 1 program. (Shuffle your stack if you searched it.) Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for test_run_20042
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
        test_card = event_test_run_20042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_makers_eye_20043(unittest.TestCase):
    '''
    testing play functionality of the_makers_eye
    Cost: 2
    Text: Run R&D. If successful, access 2 additional cards when you breach R&D.
    '''

    def setUp(self):
        '''
        setup test environment for the_makers_eye_20043
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
        test_card = event_the_makers_eye_20043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tinkering_20044(unittest.TestCase):
    '''
    testing play functionality of tinkering
    Cost: 0
    Text: Choose a piece of ice. That ice gains sentry, code gate, and barrier until the end of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for tinkering_20044
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
        test_card = event_tinkering_20044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_infiltration_20055(unittest.TestCase):
    '''
    testing play functionality of infiltration
    Cost: 0
    Text: Gain 2 credits or expose 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for infiltration_20055
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
        test_card = event_infiltration_20055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sure_gamble_20056(unittest.TestCase):
    '''
    testing play functionality of sure_gamble
    Cost: 5
    Text: Gain 9 credits.
    '''

    def setUp(self):
        '''
        setup test environment for sure_gamble_20056
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
        test_card = event_sure_gamble_20056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_by_any_means_21001(unittest.TestCase):
    '''
    testing play functionality of by_any_means
    Cost: 2
    Text: Play only as your first click. For the remainder of the turn, whenever you access a card not in Archives, trash it and suffer 1 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for by_any_means_21001
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
        test_card = event_by_any_means_21001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_credit_kiting_21023(unittest.TestCase):
    '''
    testing play functionality of credit_kiting
    Cost: 0
    Text: Play only if you made a successful run on a central server this turn. Install a card from your grip, lowering its install cost by 8 credits, and take 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for credit_kiting_21023
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
        test_card = event_credit_kiting_21023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_emergent_creativity_21028(unittest.TestCase):
    '''
    testing play functionality of emergent_creativity
    Cost: 2
    Text: As an additional cost to play this event, spend click. Trash any number of programs and/or pieces of hardware from your grip. Search your stack for 1 program or piece of hardware. Install it, paying X credits less. X is equal to the total install cost of the trashed cards.
    '''

    def setUp(self):
        '''
        setup test environment for emergent_creativity_21028
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
        test_card = event_emergent_creativity_21028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_grant_21044(unittest.TestCase):
    '''
    testing play functionality of corporate_grant
    Cost: 1
    Text: This card is not trashed until another current is played or an agenda is scored. The first time you install a card each turn, the Corp loses 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_grant_21044
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
        test_card = event_corporate_grant_21044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marathon_21046(unittest.TestCase):
    '''
    testing play functionality of marathon
    Cost: 1
    Text: Make a run on a remote server. When the run ends, gain click and add Marathon to your grip instead of trashing it if the run was successful. You may not make another run on that server for the remainder of this turn.
    '''

    def setUp(self):
        '''
        setup test environment for marathon_21046
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
        test_card = event_marathon_21046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_white_hat_21048(unittest.TestCase):
    '''
    testing play functionality of white_hat
    Cost: 0
    Text: Play only if you made a successful run on a central server this turn. Force the Corp to "Trace[3]. If unsuccessful, reveal all cards in HQ. The Runner may choose up to 2 of the revealed cards. Shuffle those cards into R&D."
    '''

    def setUp(self):
        '''
        setup test environment for white_hat_21048
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
        test_card = event_white_hat_21048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_glut_cipher_21061(unittest.TestCase):
    '''
    testing play functionality of glut_cipher
    Cost: 2
    Text: Run Archives. If successful, instead of breaching Archives, the Corp adds exactly 5 cards from Archives to HQ, if able. If they do, they trash 5 cards from HQ at random.
    '''

    def setUp(self):
        '''
        setup test environment for glut_cipher_21061
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
        test_card = event_glut_cipher_21061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_falsified_credentials_21064(unittest.TestCase):
    '''
    testing play functionality of falsified_credentials
    Cost: 1
    Text: Name a card type. Expose a card in a remote server, then gain 5 credits if the exposed card has the named card type.
    '''

    def setUp(self):
        '''
        setup test environment for falsified_credentials_21064
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
        test_card = event_falsified_credentials_21064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_because_i_can_21066(unittest.TestCase):
    '''
    testing play functionality of because_i_can
    Cost: 0
    Text: Run a remote server. If successful, instead of breaching that server, you may force the Corp to shuffle all cards in the root of that server into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for because_i_can_21066
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
        test_card = event_because_i_can_21066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_contaminate_21083(unittest.TestCase):
    '''
    testing play functionality of contaminate
    Cost: 1
    Text: Place 3 virus counters on an installed Runner card with no hosted virus counters.
    '''

    def setUp(self):
        '''
        setup test environment for contaminate_21083
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
        test_card = event_contaminate_21083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_embezzle_21084(unittest.TestCase):
    '''
    testing play functionality of embezzle
    Cost: 1
    Text: Run HQ. If successful, instead of breaching HQ, name asset, ice, operation or upgrade, then reveal 2 cards from HQ at random. Trash each revealed card that has the named type, then gain 4 credits for each card trashed this way.
    '''

    def setUp(self):
        '''
        setup test environment for embezzle_21084
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
        test_card = event_embezzle_21084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_compile_21088(unittest.TestCase):
    '''
    testing play functionality of compile
    Cost: 2
    Text: Make a run. The first time you encounter a piece of ice during this run, you may search your stack or heap for a program and install it, ignoring all costs. When the run ends, add that program to the bottom of your stack if it is still installed.
    '''

    def setUp(self):
        '''
        setup test environment for compile_21088
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
        test_card = event_compile_21088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_diversion_of_funds_21105(unittest.TestCase):
    '''
    testing play functionality of diversion_of_funds
    Cost: 1
    Text: As an additional cost to play this event, spend click. Run HQ. If successful, instead of breaching HQ, you may force the Corp to lose up to 5 credits, then you gain 1 credit for each credit lost.
    '''

    def setUp(self):
        '''
        setup test environment for diversion_of_funds_21105
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
        test_card = event_diversion_of_funds_21105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_black_hat_21110(unittest.TestCase):
    '''
    testing play functionality of black_hat
    Cost: 2
    Text: The Corp must trace[4]. If unsuccessful, for the remainder of the turn, access 2 additional cards whenever you breach HQ or R&D.
    '''

    def setUp(self):
        '''
        setup test environment for black_hat_21110
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
        test_card = event_black_hat_21110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_divide_and_conquer_22002(unittest.TestCase):
    '''
    testing play functionality of divide_and_conquer
    Cost: 3
    Text: Run Archives. If successful, after breaching Archives, breach HQ, then breach R&D. You cannot access cards in the root of HQ or R&D during these breaches.
    '''

    def setUp(self):
        '''
        setup test environment for divide_and_conquer_22002
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
        test_card = event_divide_and_conquer_22002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_guinea_pig_22003(unittest.TestCase):
    '''
    testing play functionality of guinea_pig
    Cost: 4
    Text: Trash your grip. Gain 10 credits.
    '''

    def setUp(self):
        '''
        setup test environment for guinea_pig_22003
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
        test_card = event_guinea_pig_22003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hot_pursuit_22009(unittest.TestCase):
    '''
    testing play functionality of hot_pursuit
    Cost: 2
    Text: Make a run on HQ. If successful, gain 9 credits and take 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for hot_pursuit_22009
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
        test_card = event_hot_pursuit_22009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_insight_22016(unittest.TestCase):
    '''
    testing play functionality of insight
    Cost: 0
    Text: As an additional cost to play this event, spend click. The Corp may look at the top 4 cards of R&D and arrange them in any order. Reveal the top 4 cards of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for insight_22016
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
        test_card = event_insight_22016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reboot_22023(unittest.TestCase):
    '''
    testing play functionality of reboot
    Cost: 1
    Text: Run Archives. If successful, instead of breaching Archives, install up to 5 cards from your heap facedown. Remove this event from the game.
    '''

    def setUp(self):
        '''
        setup test environment for reboot_22023
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
        test_card = event_reboot_22023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_office_supplies_22024(unittest.TestCase):
    '''
    testing play functionality of office_supplies
    Cost: 4
    Text: Reduce the play cost of Office Supplies by 1 for each link you have. Gain 4 credits or draw 4 cards.
    '''

    def setUp(self):
        '''
        setup test environment for office_supplies_22024
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
        test_card = event_office_supplies_22024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_labor_rights_23001(unittest.TestCase):
    '''
    testing play functionality of labor_rights
    Cost: 0
    Text: Trash the top 3 cards of your stack. Shuffle 3 cards from your heap into your stack. Draw 1 card. Remove this event from the game instead of trashing it.
    '''

    def setUp(self):
        '''
        setup test environment for labor_rights_23001
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
        test_card = event_labor_rights_23001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_watch_the_world_burn_23100(unittest.TestCase):
    '''
    testing play functionality of watch_the_world_burn
    Cost: 3
    Text: After you resolve this event, end your action phase. Make a run on a remote server. If successful, remove the first non-agenda card that you access from the game. Until the game ends, whenever you access a copy of that card, remove it from the game. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for watch_the_world_burn_23100
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
        test_card = event_watch_the_world_burn_23100()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_queens_gambit_25003(unittest.TestCase):
    '''
    testing play functionality of queens_gambit
    Cost: 0
    Text: As an additional cost to play this event, spend click. Place up to 3 advancement counters on 1 unrezzed card in the root of a remote server. Gain 2 credits for each counter placed this way. You cannot access that card for the remainder of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for queens_gambit_25003
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
        test_card = event_queens_gambit_25003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_quest_completed_25004(unittest.TestCase):
    '''
    testing play functionality of quest_completed
    Cost: 0
    Text: Play only if you made a successful run on R&D, HQ, and Archives this turn. Access 1 installed card (non-ice).
    '''

    def setUp(self):
        '''
        setup test environment for quest_completed_25004
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
        test_card = event_quest_completed_25004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_retrieval_run_25005(unittest.TestCase):
    '''
    testing play functionality of retrieval_run
    Cost: 3
    Text: Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for retrieval_run_25005
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
        test_card = event_retrieval_run_25005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_run_amok_25006(unittest.TestCase):
    '''
    testing play functionality of run_amok
    Cost: 3
    Text: Make a run. When the run ends, trash 1 piece of ice that was rezzed during this run.
    '''

    def setUp(self):
        '''
        setup test environment for run_amok_25006
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
        test_card = event_run_amok_25006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_stimhack_25007(unittest.TestCase):
    '''
    testing play functionality of stimhack
    Cost: 0
    Text: Place 9 credits on this event, then run any server. During that run, hosted credits are considered to be in your credit pool. When that run ends, suffer 1 core damage. This damage cannot be prevented.
    '''

    def setUp(self):
        '''
        setup test environment for stimhack_25007
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
        test_card = event_stimhack_25007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_career_fair_25022(unittest.TestCase):
    '''
    testing play functionality of career_fair
    Cost: 0
    Text: Install 1 resource from your grip, paying 3 credits less.
    '''

    def setUp(self):
        '''
        setup test environment for career_fair_25022
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
        test_card = event_career_fair_25022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_easy_mark_25023(unittest.TestCase):
    '''
    testing play functionality of easy_mark
    Cost: 0
    Text: Gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for easy_mark_25023
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
        test_card = event_easy_mark_25023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_emergency_shutdown_25024(unittest.TestCase):
    '''
    testing play functionality of emergency_shutdown
    Cost: 0
    Text: Play only if you made a successful run on HQ this turn. Derez 1 installed piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for emergency_shutdown_25024
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
        test_card = event_emergency_shutdown_25024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hostage_25025(unittest.TestCase):
    '''
    testing play functionality of hostage
    Cost: 1
    Text: As an additional cost to play this event, spend click. Search your stack for a connection, reveal it, and add it to your grip. You may install that connection (paying its install cost). Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for hostage_25025
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
        test_card = event_hostage_25025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_inside_job_25026(unittest.TestCase):
    '''
    testing play functionality of inside_job
    Cost: 2
    Text: Run any server. The first time this run you encounter a piece of ice, bypass it.
    '''

    def setUp(self):
        '''
        setup test environment for inside_job_25026
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
        test_card = event_inside_job_25026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_legwork_25027(unittest.TestCase):
    '''
    testing play functionality of legwork
    Cost: 2
    Text: Run HQ. If successful, access 2 additional cards when you breach HQ.
    '''

    def setUp(self):
        '''
        setup test environment for legwork_25027
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
        test_card = event_legwork_25027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_networking_25028(unittest.TestCase):
    '''
    testing play functionality of networking
    Cost: 0
    Text: Remove 1 tag. Then, you may pay 1 credit to add this event to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for networking_25028
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
        test_card = event_networking_25028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spear_phishing_25029(unittest.TestCase):
    '''
    testing play functionality of spear_phishing
    Cost: 2
    Text: Make a run. When you encounter the innermost piece of ice protecting that server, bypass it.
    '''

    def setUp(self):
        '''
        setup test environment for spear_phishing_25029
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
        test_card = event_spear_phishing_25029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_special_order_25030(unittest.TestCase):
    '''
    testing play functionality of special_order
    Cost: 1
    Text: Search your stack for an icebreaker, reveal it, and add it to your grip. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for special_order_25030
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
        test_card = event_special_order_25030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_diesel_25042(unittest.TestCase):
    '''
    testing play functionality of diesel
    Cost: 0
    Text: Draw 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for diesel_25042
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
        test_card = event_diesel_25042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_modded_25043(unittest.TestCase):
    '''
    testing play functionality of modded
    Cost: 0
    Text: Install a program or piece of hardware, lowering the install cost by 3.
    '''

    def setUp(self):
        '''
        setup test environment for modded_25043
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
        test_card = event_modded_25043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_notoriety_25044(unittest.TestCase):
    '''
    testing play functionality of notoriety
    Cost: 1
    Text: Play only if you made a successful run on R&D, HQ, and Archives this turn. Add Notoriety to your score area as an agenda worth 1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for notoriety_25044
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
        test_card = event_notoriety_25044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_test_run_25045(unittest.TestCase):
    '''
    testing play functionality of test_run
    Cost: 3
    Text: Search either your stack or your heap for 1 program. (Shuffle your stack if you searched it.) Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for test_run_25045
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
        test_card = event_test_run_25045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_makers_eye_25046(unittest.TestCase):
    '''
    testing play functionality of the_makers_eye
    Cost: 2
    Text: Run R&D. If successful, access 2 additional cards when you breach R&D.
    '''

    def setUp(self):
        '''
        setup test environment for the_makers_eye_25046
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
        test_card = event_the_makers_eye_25046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tinkering_25047(unittest.TestCase):
    '''
    testing play functionality of tinkering
    Cost: 0
    Text: Choose a piece of ice. That ice gains sentry, code gate, and barrier until the end of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for tinkering_25047
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
        test_card = event_tinkering_25047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sure_gamble_25059(unittest.TestCase):
    '''
    testing play functionality of sure_gamble
    Cost: 5
    Text: Gain 9 credits.
    '''

    def setUp(self):
        '''
        setup test environment for sure_gamble_25059
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
        test_card = event_sure_gamble_25059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dirty_laundry_25060(unittest.TestCase):
    '''
    testing play functionality of dirty_laundry
    Cost: 2
    Text: Run any server. When that run ends, if it was successful, gain 5 credits.
    '''

    def setUp(self):
        '''
        setup test environment for dirty_laundry_25060
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
        test_card = event_dirty_laundry_25060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_isolation_26001(unittest.TestCase):
    '''
    testing play functionality of isolation
    Cost: 2
    Text: As an additional cost to play this event, trash an installed resource. Gain 7 credits.
    '''

    def setUp(self):
        '''
        setup test environment for isolation_26001
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
        test_card = event_isolation_26001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_always_have_a_backup_plan_26011(unittest.TestCase):
    '''
    testing play functionality of always_have_a_backup_plan
    Cost: 2
    Text: Run any server. When that run ends, if it was unsuccessful, you may run that server again, ignoring any additional costs to run. During the second run, when you encounter the last ice you encountered in the first run, bypass it.
    '''

    def setUp(self):
        '''
        setup test environment for always_have_a_backup_plan_26011
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
        test_card = event_always_have_a_backup_plan_26011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_blueberry_diesel_26012(unittest.TestCase):
    '''
    testing play functionality of blueberry_diesel
    Cost: 0
    Text: Look at the top 2 cards of your stack. You may add 1 of those cards to the bottom of your stack. Draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for blueberry_diesel_26012
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
        test_card = event_blueberry_diesel_26012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_in_the_groove_26020(unittest.TestCase):
    '''
    testing play functionality of in_the_groove
    Cost: 0
    Text: Play only as your first click. Whenever you install a card with a printed install cost of 1 or greater this turn, draw 1 card or gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for in_the_groove_26020
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
        test_card = event_in_the_groove_26020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_khusyuk_26021(unittest.TestCase):
    '''
    testing play functionality of khusyuk
    Cost: 3
    Text: Run R&D. If successful, instead of breaching R&D, choose a number greater than 0. For each installed card you have with a printed install cost matching that number, reveal 1 card from the top of R&D (max 6). Access 1 of the revealed cards, then the Corp shuffles R&D.
    '''

    def setUp(self):
        '''
        setup test environment for khusyuk_26021
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
        test_card = event_khusyuk_26021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spec_work_26022(unittest.TestCase):
    '''
    testing play functionality of spec_work
    Cost: 1
    Text: As an additional cost to play this event, trash an installed program. Gain 4 credits and draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for spec_work_26022
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
        test_card = event_spec_work_26022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_direct_access_26028(unittest.TestCase):
    '''
    testing play functionality of direct_access
    Cost: 1
    Text: While you are resolving this event, each player's identity loses all abilities. Run any server. When that run ends, you may shuffle this event into your stack.
    '''

    def setUp(self):
        '''
        setup test environment for direct_access_26028
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
        test_card = event_direct_access_26028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rejig_26029(unittest.TestCase):
    '''
    testing play functionality of rejig
    Cost: 0
    Text: Add an installed program or piece of hardware to your grip. If you do, you may install a program or piece of hardware, paying X credits less. X is equal to the printed install cost of the uninstalled card.
    '''

    def setUp(self):
        '''
        setup test environment for rejig_26029
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
        test_card = event_rejig_26029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_moshing_26067(unittest.TestCase):
    '''
    testing play functionality of moshing
    Cost: 0
    Text: As an additional cost to play this event, trash 3 cards from your grip. Draw 3 cards and gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for moshing_26067
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
        test_card = event_moshing_26067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bravado_26074(unittest.TestCase):
    '''
    testing play functionality of bravado
    Cost: 3
    Text: Run a server protected by ice. When that run ends, gain 6 credits, plus 1 credit for each piece of ice you passed during that run.
    '''

    def setUp(self):
        '''
        setup test environment for bravado_26074
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
        test_card = event_bravado_26074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_harmony_ar_therapy_26083(unittest.TestCase):
    '''
    testing play functionality of harmony_ar_therapy
    Cost: 2
    Text: Search your heap for up to 5 cards with different names. Shuffle those cards into your stack. Remove this card from the game instead of trashing it.
    '''

    def setUp(self):
        '''
        setup test environment for harmony_ar_therapy_26083
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
        test_card = event_harmony_ar_therapy_26083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_labor_rights_28001(unittest.TestCase):
    '''
    testing play functionality of labor_rights
    Cost: 0
    Text: Trash the top 3 cards of your stack. Shuffle 3 cards from your heap into your stack. Draw 1 card. Remove this event from the game instead of trashing it.
    '''

    def setUp(self):
        '''
        setup test environment for labor_rights_28001
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
        test_card = event_labor_rights_28001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_indexing_29005(unittest.TestCase):
    '''
    testing play functionality of indexing
    Cost: 0
    Text: Run R&D. If successful, instead of breaching R&D, you may look at the top 5 cards of R&D and arrange them in any order.
    '''

    def setUp(self):
        '''
        setup test environment for indexing_29005
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
        test_card = event_indexing_29005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lucky_find_29007(unittest.TestCase):
    '''
    testing play functionality of lucky_find
    Cost: 3
    Text: As an additional cost to play this event, spend click. Gain 9 credits.
    '''

    def setUp(self):
        '''
        setup test environment for lucky_find_29007
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
        test_card = event_lucky_find_29007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wildcat_strike_30002(unittest.TestCase):
    '''
    testing play functionality of wildcat_strike
    Cost: 2
    Text: Resolve 1 of the following of the Corp's choice: * Gain 6 credits. * Draw 4 cards.
    '''

    def setUp(self):
        '''
        setup test environment for wildcat_strike_30002
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
        test_card = event_wildcat_strike_30002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mutual_favor_30011(unittest.TestCase):
    '''
    testing play functionality of mutual_favor
    Cost: 0
    Text: Search your stack for 1 icebreaker program and reveal it. (Shuffle your stack after searching it.) If you made a successful run this turn, you may install it. If you do not, add it to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for mutual_favor_30011
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
        test_card = event_mutual_favor_30011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tread_lightly_30012(unittest.TestCase):
    '''
    testing play functionality of tread_lightly
    Cost: 1
    Text: Run any server. During that run, the rez cost of each piece of ice is increased by 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for tread_lightly_30012
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
        test_card = event_tread_lightly_30012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_creative_commission_30020(unittest.TestCase):
    '''
    testing play functionality of creative_commission
    Cost: 1
    Text: Gain 5 credits. If you have any click remaining, lose click.
    '''

    def setUp(self):
        '''
        setup test environment for creative_commission_30020
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
        test_card = event_creative_commission_30020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vrcation_30021(unittest.TestCase):
    '''
    testing play functionality of vrcation
    Cost: 1
    Text: Draw 4 cards. If you have any click remaining, lose click.
    '''

    def setUp(self):
        '''
        setup test environment for vrcation_30021
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
        test_card = event_vrcation_30021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_jailbreak_30028(unittest.TestCase):
    '''
    testing play functionality of jailbreak
    Cost: 0
    Text: Run HQ or R&D. If successful, draw 1 card and when you breach the attacked server, access 1 additional card.
    '''

    def setUp(self):
        '''
        setup test environment for jailbreak_30028
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
        test_card = event_jailbreak_30028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_overclock_30029(unittest.TestCase):
    '''
    testing play functionality of overclock
    Cost: 1
    Text: Place 5 credits on this event, then run any server. You can spend hosted credits during that run.
    '''

    def setUp(self):
        '''
        setup test environment for overclock_30029
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
        test_card = event_overclock_30029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sure_gamble_30030(unittest.TestCase):
    '''
    testing play functionality of sure_gamble
    Cost: 5
    Text: Gain 9 credits.
    '''

    def setUp(self):
        '''
        setup test environment for sure_gamble_30030
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
        test_card = event_sure_gamble_30030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_en_passant_31003(unittest.TestCase):
    '''
    testing play functionality of en_passant
    Cost: 0
    Text: Play only if you made a successful run this turn. Trash 1 unrezzed piece of ice you passed during your last run.
    '''

    def setUp(self):
        '''
        setup test environment for en_passant_31003
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
        test_card = event_en_passant_31003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_retrieval_run_31004(unittest.TestCase):
    '''
    testing play functionality of retrieval_run
    Cost: 3
    Text: Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for retrieval_run_31004
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
        test_card = event_retrieval_run_31004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_career_fair_31015(unittest.TestCase):
    '''
    testing play functionality of career_fair
    Cost: 0
    Text: Install 1 resource from your grip, paying 3 credits less.
    '''

    def setUp(self):
        '''
        setup test environment for career_fair_31015
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
        test_card = event_career_fair_31015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_emergency_shutdown_31016(unittest.TestCase):
    '''
    testing play functionality of emergency_shutdown
    Cost: 0
    Text: Play only if you made a successful run on HQ this turn. Derez 1 installed piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for emergency_shutdown_31016
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
        test_card = event_emergency_shutdown_31016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_forged_activation_orders_31017(unittest.TestCase):
    '''
    testing play functionality of forged_activation_orders
    Cost: 1
    Text: Choose 1 unrezzed piece of ice. The Corp may rez that ice. If they do not, they trash it.
    '''

    def setUp(self):
        '''
        setup test environment for forged_activation_orders_31017
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
        test_card = event_forged_activation_orders_31017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_inside_job_31018(unittest.TestCase):
    '''
    testing play functionality of inside_job
    Cost: 2
    Text: Run any server. The first time this run you encounter a piece of ice, bypass it.
    '''

    def setUp(self):
        '''
        setup test environment for inside_job_31018
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
        test_card = event_inside_job_31018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_legwork_31019(unittest.TestCase):
    '''
    testing play functionality of legwork
    Cost: 2
    Text: Run HQ. If successful, access 2 additional cards when you breach HQ.
    '''

    def setUp(self):
        '''
        setup test environment for legwork_31019
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
        test_card = event_legwork_31019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_networking_31020(unittest.TestCase):
    '''
    testing play functionality of networking
    Cost: 0
    Text: Remove 1 tag. Then, you may pay 1 credit to add this event to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for networking_31020
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
        test_card = event_networking_31020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_diesel_31027(unittest.TestCase):
    '''
    testing play functionality of diesel
    Cost: 0
    Text: Draw 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for diesel_31027
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
        test_card = event_diesel_31027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_test_run_31028(unittest.TestCase):
    '''
    testing play functionality of test_run
    Cost: 3
    Text: Search either your stack or your heap for 1 program. (Shuffle your stack if you searched it.) Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for test_run_31028
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
        test_card = event_test_run_31028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_makers_eye_31029(unittest.TestCase):
    '''
    testing play functionality of the_makers_eye
    Cost: 2
    Text: Run R&D. If successful, access 2 additional cards when you breach R&D.
    '''

    def setUp(self):
        '''
        setup test environment for the_makers_eye_31029
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
        test_card = event_the_makers_eye_31029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dirty_laundry_31037(unittest.TestCase):
    '''
    testing play functionality of dirty_laundry
    Cost: 2
    Text: Run any server. When that run ends, if it was successful, gain 5 credits.
    '''

    def setUp(self):
        '''
        setup test environment for dirty_laundry_31037
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
        test_card = event_dirty_laundry_31037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_deep_dive_32003(unittest.TestCase):
    '''
    testing play functionality of deep_dive
    Cost: 2
    Text: Play only if you made a successful run on HQ, R&D, and Archives this turn. The Corp must set aside the top 8 cards of R&D faceup. Access 1 of those cards. You may spend click to access another 1 of those cards. Then, the Corp shuffles the set-aside cards into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for deep_dive_32003
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
        test_card = event_deep_dive_32003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chastushka_33002(unittest.TestCase):
    '''
    testing play functionality of chastushka
    Cost: 3
    Text: Run HQ. If successful, instead of breaching HQ, sabotage 4. (The Corp trashes 4 cards of their choice from HQ and/or the top of R&D.)
    '''

    def setUp(self):
        '''
        setup test environment for chastushka_33002
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
        test_card = event_chastushka_33002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_running_hot_33003(unittest.TestCase):
    '''
    testing play functionality of running_hot
    Cost: 1
    Text: As an additional cost to play this event, suffer 1 core damage. Gain clickclickclick.
    '''

    def setUp(self):
        '''
        setup test environment for running_hot_33003
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
        test_card = event_running_hot_33003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_steelskin_scarring_33004(unittest.TestCase):
    '''
    testing play functionality of steelskin_scarring
    Cost: 1
    Text: Draw 3 cards. When this event is trashed from your grip or stack, you may draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for steelskin_scarring_33004
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
        test_card = event_steelskin_scarring_33004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_carpe_diem_33012(unittest.TestCase):
    '''
    testing play functionality of carpe_diem
    Cost: 1
    Text: Identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) Gain 4 credits. You may run your mark.
    '''

    def setUp(self):
        '''
        setup test environment for carpe_diem_33012
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
        test_card = event_carpe_diem_33012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pinhole_threading_33013(unittest.TestCase):
    '''
    testing play functionality of pinhole_threading
    Cost: 1
    Text: Run any server. If successful, instead of breaching the attacked server, access 1 card in the root of another server. If that card is an agenda, you cannot steal or trash it during this access.
    '''

    def setUp(self):
        '''
        setup test environment for pinhole_threading_33013
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
        test_card = event_pinhole_threading_33013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_deep_dive_33022(unittest.TestCase):
    '''
    testing play functionality of deep_dive
    Cost: 2
    Text: Play only if you made a successful run on HQ, R&D, and Archives this turn. The Corp must set aside the top 8 cards of R&D faceup. Access 1 of those cards. You may spend click to access another 1 of those cards. Then, the Corp shuffles the set-aside cards into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for deep_dive_33022
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
        test_card = event_deep_dive_33022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_into_the_depths_33023(unittest.TestCase):
    '''
    testing play functionality of into_the_depths
    Cost: 1
    Text: Run any server. If successful, for each time you passed ice this run, resolve 1 of the following that you have not yet resolved this run: * Gain 4 credits. * Search your stack for a program. Install it. (Shuffle your stack after searching it.) * Charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)
    '''

    def setUp(self):
        '''
        setup test environment for into_the_depths_33023
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
        test_card = event_into_the_depths_33023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rigging_up_33024(unittest.TestCase):
    '''
    testing play functionality of rigging_up
    Cost: 0
    Text: Install 1 program or piece of hardware from your grip, paying 3 credits less. You may charge that card if able. (If it has a power counter on it, add another.)
    '''

    def setUp(self):
        '''
        setup test environment for rigging_up_33024
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
        test_card = event_rigging_up_33024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_finality_33066(unittest.TestCase):
    '''
    testing play functionality of finality
    Cost: 2
    Text: As an additional cost to play this event, suffer 1 core damage. Run R&D. If successful, access 3 additional cards when you breach R&D.
    '''

    def setUp(self):
        '''
        setup test environment for finality_33066
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
        test_card = event_finality_33066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_katorga_breakout_33067(unittest.TestCase):
    '''
    testing play functionality of katorga_breakout
    Cost: 2
    Text: Run any server. If successful, add 1 card from your heap to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for katorga_breakout_33067
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
        test_card = event_katorga_breakout_33067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_raindrops_cut_stone_33068(unittest.TestCase):
    '''
    testing play functionality of raindrops_cut_stone
    Cost: 1
    Text: Run any server. Whenever a subroutine resolves during that run (including a subroutine that ends the run), place 1 power counter on this event. When that run ends, draw 1 card for each hosted power counter and gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for raindrops_cut_stone_33068
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
        test_card = event_raindrops_cut_stone_33068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_concerto_33075(unittest.TestCase):
    '''
    testing play functionality of concerto
    Cost: 0
    Text: Reveal the top card of your stack and place credits equal to its printed play or install cost on this event. Add the revealed card to your grip. Run any server. You can spend hosted credits during that run.
    '''

    def setUp(self):
        '''
        setup test environment for concerto_33075
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
        test_card = event_concerto_33075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reprise_33076(unittest.TestCase):
    '''
    testing play functionality of reprise
    Cost: 2
    Text: Play only if you stole an agenda this turn. Add 1 installed Corp card to HQ. You may run any server.
    '''

    def setUp(self):
        '''
        setup test environment for reprise_33076
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
        test_card = event_reprise_33076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spark_of_inspiration_33084(unittest.TestCase):
    '''
    testing play functionality of spark_of_inspiration
    Cost: 3
    Text: Set aside cards from the top of your stack faceup until you set aside a program. You may install that program, paying 10 credits less. Shuffle the set-aside cards into your stack.
    '''

    def setUp(self):
        '''
        setup test environment for spark_of_inspiration_33084
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
        test_card = event_spark_of_inspiration_33084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")
