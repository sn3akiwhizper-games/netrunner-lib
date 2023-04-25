
'''
test cases for card classes of type program
'''
import unittest

from netrunner_lib.cards._base_card_classes import Program
from netrunner_lib.cards.program import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
class Test_corroder_01007(unittest.TestCase):
    '''
    testing play functionality of corroder
    Cost: 2
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for corroder_01007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_corroder_01007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_datasucker_01008(unittest.TestCase):
    '''
    testing play functionality of datasucker
    Cost: 1
    Text: Whenever you make a successful run on a central server, place 1 virus counter on Datasucker. Hosted virus counter: Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.
    '''

    def setUp(self):
        '''
        setup test environment for datasucker_01008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_datasucker_01008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_djinn_01009(unittest.TestCase):
    '''
    testing play functionality of djinn
    Cost: 2
    Text: Djinn can host up to 3 mu of non-icebreaker programs. The memory costs of hosted programs do not count against your memory limit. click, 1 credit: Search your stack for a virus program, reveal it, and add it to your grip. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for djinn_01009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_djinn_01009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_medium_01010(unittest.TestCase):
    '''
    testing play functionality of medium
    Cost: 3
    Text: Whenever you make a successful run on R&D, place 1 virus counter on this program. Whenever you breach R&D, choose a number less than the number of hosted virus counters. Access that many additional cards.
    '''

    def setUp(self):
        '''
        setup test environment for medium_01010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_medium_01010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mimic_01011(unittest.TestCase):
    '''
    testing play functionality of mimic
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for mimic_01011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_mimic_01011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_parasite_01012(unittest.TestCase):
    '''
    testing play functionality of parasite
    Cost: 2
    Text: Install only on a rezzed piece of ice. When your turn begins, place 1 virus counter on this program. Host ice gets -1 strength for each hosted virus counter. When the strength of host ice is 0 or less, trash it.
    '''

    def setUp(self):
        '''
        setup test environment for parasite_01012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_parasite_01012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wyrm_01013(unittest.TestCase):
    '''
    testing play functionality of wyrm
    Cost: 1
    Text: Interface -> 3 credits: Break 1 subroutine on a piece of ice with 0 or less strength. Interface -> 1 credit: The ice you are encountering gets -1 strength for the remainder of this encounter. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for wyrm_01013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_wyrm_01013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_yog0_01014(unittest.TestCase):
    '''
    testing play functionality of yog0
    Cost: 5
    Text: Interface -> 0 credits: Break 1 code gate subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for yog0_01014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_yog0_01014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aurora_01025(unittest.TestCase):
    '''
    testing play functionality of aurora
    Cost: 3
    Text: Interface -> 2 credits: Break 1 barrier subroutine. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for aurora_01025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_aurora_01025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_femme_fatale_01026(unittest.TestCase):
    '''
    testing play functionality of femme_fatale
    Cost: 9
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.
    '''

    def setUp(self):
        '''
        setup test environment for femme_fatale_01026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_femme_fatale_01026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ninja_01027(unittest.TestCase):
    '''
    testing play functionality of ninja
    Cost: 4
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +5 strength.
    '''

    def setUp(self):
        '''
        setup test environment for ninja_01027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_ninja_01027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sneakdoor_beta_01028(unittest.TestCase):
    '''
    testing play functionality of sneakdoor_beta
    Cost: 4
    Text: click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.
    '''

    def setUp(self):
        '''
        setup test environment for sneakdoor_beta_01028
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sneakdoor_beta_01028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_battering_ram_01042(unittest.TestCase):
    '''
    testing play functionality of battering_ram
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 1 credit: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for battering_ram_01042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_battering_ram_01042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gordian_blade_01043(unittest.TestCase):
    '''
    testing play functionality of gordian_blade
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for gordian_blade_01043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gordian_blade_01043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_magnum_opus_01044(unittest.TestCase):
    '''
    testing play functionality of magnum_opus
    Cost: 5
    Text: click: Gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for magnum_opus_01044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_magnum_opus_01044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_net_shield_01045(unittest.TestCase):
    '''
    testing play functionality of net_shield
    Cost: 2
    Text: Interrupt -> The first time each turn you would suffer net damage, you may pay 1 credit to prevent 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for net_shield_01045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_net_shield_01045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pipeline_01046(unittest.TestCase):
    '''
    testing play functionality of pipeline
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for pipeline_01046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_pipeline_01046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crypsis_01051(unittest.TestCase):
    '''
    testing play functionality of crypsis
    Cost: 5
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. click: Place 1 virus counter on this program. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for crypsis_01051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_crypsis_01051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_imp_02003(unittest.TestCase):
    '''
    testing play functionality of imp
    Cost: 2
    Text: When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for imp_02003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_imp_02003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_morning_star_02004(unittest.TestCase):
    '''
    testing play functionality of morning_star
    Cost: 8
    Text: Interface -> 1 credit: Break any number of barrier subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for morning_star_02004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_morning_star_02004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_peacock_02006(unittest.TestCase):
    '''
    testing play functionality of peacock
    Cost: 3
    Text: Interface -> 2 credits: Break 1 code gate subroutine. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for peacock_02006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_peacock_02006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zu13_key_master_02007(unittest.TestCase):
    '''
    testing play functionality of zu13_key_master
    Cost: 1
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for zu13_key_master_02007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_zu13_key_master_02007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_snowball_02027(unittest.TestCase):
    '''
    testing play functionality of snowball
    Cost: 4
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength. Whenever you use this program to break a subroutine, this program gets +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for snowball_02027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_snowball_02027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nerve_agent_02041(unittest.TestCase):
    '''
    testing play functionality of nerve_agent
    Cost: 3
    Text: Whenever you make a successful run on HQ, place 1 virus counter on this program. Whenever you breach HQ, choose a number less than the number of hosted virus counters. Access that many additional cards.
    '''

    def setUp(self):
        '''
        setup test environment for nerve_agent_02041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_nerve_agent_02041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_snitch_02045(unittest.TestCase):
    '''
    testing play functionality of snitch
    Cost: 3
    Text: Once per run, you may expose an unrezzed piece of ice when you approach it. You may then jack out.
    '''

    def setUp(self):
        '''
        setup test environment for snitch_02045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_snitch_02045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_disrupter_02061(unittest.TestCase):
    '''
    testing play functionality of disrupter
    Cost: 1
    Text: Interrupt -> trash: Reduce the base trace strength of a trace to 0.
    '''

    def setUp(self):
        '''
        setup test environment for disrupter_02061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_disrupter_02061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_force_of_nature_02062(unittest.TestCase):
    '''
    testing play functionality of force_of_nature
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for force_of_nature_02062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_force_of_nature_02062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crescentus_02065(unittest.TestCase):
    '''
    testing play functionality of crescentus
    Cost: 1
    Text: trash: Derez 1 piece of ice you fully broke during this encounter.
    '''

    def setUp(self):
        '''
        setup test environment for crescentus_02065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_crescentus_02065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_deus_x_02066(unittest.TestCase):
    '''
    testing play functionality of deus_x
    Cost: 3
    Text: Interface -> trash: Break any number of AP subroutines. Interrupt -> trash: Prevent any amount of net damage.
    '''

    def setUp(self):
        '''
        setup test environment for deus_x_02066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_deus_x_02066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pheromones_02086(unittest.TestCase):
    '''
    testing play functionality of pheromones
    Cost: 2
    Text: X recurring credits Use these credits during runs on HQ. X is the number of virus counters on Pheromones. Whenever you make a successful run on HQ, place 1 virus counter on Pheromones.
    '''

    def setUp(self):
        '''
        setup test environment for pheromones_02086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_pheromones_02086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_creeper_02089(unittest.TestCase):
    '''
    testing play functionality of creeper
    Cost: 5
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break 1 sentry subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for creeper_02089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_creeper_02089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_darwin_02102(unittest.TestCase):
    '''
    testing play functionality of darwin
    Cost: 3
    Text: Interface -> 2 credits: Break 1 subroutine. X is equal to the number of hosted virus counters. When your turn begins, you may pay 1 credit to place 1 virus counter on this program.
    '''

    def setUp(self):
        '''
        setup test environment for darwin_02102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_darwin_02102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_faerie_02104(unittest.TestCase):
    '''
    testing play functionality of faerie
    Cost: 0
    Text: Interface -> 0 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for faerie_02104
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_faerie_02104()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_deep_thought_02108(unittest.TestCase):
    '''
    testing play functionality of deep_thought
    Cost: 1
    Text: Whenever you make a successful run on R&D, place 1 virus counter on Deep Thought. If there are at least 3 virus counters on Deep Thought, it gains "When your turn begins, you may look at the top card of R&D."
    '''

    def setUp(self):
        '''
        setup test environment for deep_thought_02108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_deep_thought_02108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_atman_03040(unittest.TestCase):
    '''
    testing play functionality of atman
    Cost: 3
    Text: When you install this program, you may pay X credits to place X power counters on it. This program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength. Interface -> 1 credit: Break 1 subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for atman_03040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_atman_03040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cloak_03041(unittest.TestCase):
    '''
    testing play functionality of cloak
    Cost: 1
    Text: 1 recurring credit Use this credit to pay for using icebreakers.
    '''

    def setUp(self):
        '''
        setup test environment for cloak_03041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cloak_03041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dagger_03042(unittest.TestCase):
    '''
    testing play functionality of dagger
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 1 credit: +5 strength. Use this ability only by spending a credit from a stealth card.
    '''

    def setUp(self):
        '''
        setup test environment for dagger_03042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_dagger_03042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chakana_03043(unittest.TestCase):
    '''
    testing play functionality of chakana
    Cost: 2
    Text: Whenever you make a successful run on R&D, place 1 virus counter on Chakana. If there are at least 3 virus counters on Chakana, the advancement requirement of all agendas is increased by 1.
    '''

    def setUp(self):
        '''
        setup test environment for chakana_03043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_chakana_03043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cybercypher_03044(unittest.TestCase):
    '''
    testing play functionality of cybercypher
    Cost: 2
    Text: When you install this program, choose a server. Use this program only during runs on the chosen server. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for cybercypher_03044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cybercypher_03044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paricia_03045(unittest.TestCase):
    '''
    testing play functionality of paricia
    Cost: 0
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs of assets.
    '''

    def setUp(self):
        '''
        setup test environment for paricia_03045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_paricia_03045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_selfmodifying_code_03046(unittest.TestCase):
    '''
    testing play functionality of selfmodifying_code
    Cost: 0
    Text: 2 credits, trash: Search your stack for a program. Install it.
    '''

    def setUp(self):
        '''
        setup test environment for selfmodifying_code_03046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_selfmodifying_code_03046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sahasrara_03047(unittest.TestCase):
    '''
    testing play functionality of sahasrara
    Cost: 2
    Text: 2 recurring credits Use these credits to install programs (you cannot use Sahasrara to install a program that trashes Sahasrara).
    '''

    def setUp(self):
        '''
        setup test environment for sahasrara_03047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sahasrara_03047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_inti_03048(unittest.TestCase):
    '''
    testing play functionality of inti
    Cost: 0
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 2 credits: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for inti_03048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_inti_03048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pawn_04002(unittest.TestCase):
    '''
    testing play functionality of pawn
    Cost: 0
    Text: click: Host this program on the outermost piece of ice protecting a central server. Whenever you make a successful run while this program is hosted on a piece of ice, host it on the next inward piece of ice. If you cannot, trash this program and install 1 other Caissa program from your grip or heap, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for pawn_04002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_pawn_04002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rook_04003(unittest.TestCase):
    '''
    testing play functionality of rook
    Cost: 2
    Text: While this program is hosted on ice, the rez cost of each piece of ice protecting this server is increased by 2. click: Host this program on a piece of ice that is not hosting a Caissa program. If this program is hosted on ice, its click ability can only be used to host it on ice protecting the same server or in the same position as its current host ice. (Count positions from the innermost ice.)
    '''

    def setUp(self):
        '''
        setup test environment for rook_04003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_rook_04003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gorman_drip_v1_04005(unittest.TestCase):
    '''
    testing play functionality of gorman_drip_v1
    Cost: 1
    Text: Whenever the Corp spends a click to draw 1 card or gain 1 credit (not through a card ability), place 1 virus counter on Gorman Drip v1. click, trash: Gain 1 credit for each virus counter on Gorman Drip v1.
    '''

    def setUp(self):
        '''
        setup test environment for gorman_drip_v1_04005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gorman_drip_v1_04005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_false_echo_04007(unittest.TestCase):
    '''
    testing play functionality of false_echo
    Cost: 1
    Text: Whenever you pass a piece of unrezzed ice, you may trash False Echo. If you do, the Corp must rez that ice or add it to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for false_echo_04007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_false_echo_04007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bishop_04021(unittest.TestCase):
    '''
    testing play functionality of bishop
    Cost: 0
    Text: Host ice gets -2 strength. click: Host this program on a piece of ice that is not hosting a Caissa program. If this program is hosted on ice protecting a central server, its click ability can only be used to host it on ice protecting a remote server. If this program is hosted on ice protecting a remote server, its click ability can only be used to host it on ice protecting a central server.
    '''

    def setUp(self):
        '''
        setup test environment for bishop_04021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_bishop_04021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_scheherazade_04022(unittest.TestCase):
    '''
    testing play functionality of scheherazade
    Cost: 0
    Text: Scheherazade can host any number of programs. Whenever you install a program on Scheherazade, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for scheherazade_04022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_scheherazade_04022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_copycat_04025(unittest.TestCase):
    '''
    testing play functionality of copycat
    Cost: 1
    Text: Whenever you pass a piece of ice, you may trash Copycat. If you do, choose another rezzed copy of that piece of ice protecting any server. The run continues as if you had just passed the chosen piece of ice (you are now running from the new position).
    '''

    def setUp(self):
        '''
        setup test environment for copycat_04025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_copycat_04025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_leviathan_04026(unittest.TestCase):
    '''
    testing play functionality of leviathan
    Cost: 6
    Text: Interface -> 3 credits: Break up to 3 code gate subroutines. 3 credits: +5 strength.
    '''

    def setUp(self):
        '''
        setup test environment for leviathan_04026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_leviathan_04026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_knight_04043(unittest.TestCase):
    '''
    testing play functionality of knight
    Cost: 2
    Text: Interface -> 2 credits: Break 1 subroutine on host ice. click: Host this program on a piece of ice that is not hosting a Caissa program. If this program is hosted on ice, its click ability cannot be used to host it on the next inward or outward piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for knight_04043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_knight_04043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_expert_schedule_analyzer_04045(unittest.TestCase):
    '''
    testing play functionality of expert_schedule_analyzer
    Cost: 1
    Text: click: Run HQ. If successful, instead of breaching HQ, you may reveal all cards in HQ.
    '''

    def setUp(self):
        '''
        setup test environment for expert_schedule_analyzer_04045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_expert_schedule_analyzer_04045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_torch_04047(unittest.TestCase):
    '''
    testing play functionality of torch
    Cost: 9
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for torch_04047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_torch_04047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_keyhole_04061(unittest.TestCase):
    '''
    testing play functionality of keyhole
    Cost: 4
    Text: click: Run R&D. If successful, instead of breaching R&D, look at the top 3 cards of R&D. Trash 1 of those cards, then the Corp shuffles R&D.
    '''

    def setUp(self):
        '''
        setup test environment for keyhole_04061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_keyhole_04061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_garrote_04065(unittest.TestCase):
    '''
    testing play functionality of garrote
    Cost: 7
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for garrote_04065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_garrote_04065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sharpshooter_04067(unittest.TestCase):
    '''
    testing play functionality of sharpshooter
    Cost: 1
    Text: Interface -> trash: Break any number of destroyer subroutines. 1 credit: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for sharpshooter_04067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sharpshooter_04067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hemorrhage_04082(unittest.TestCase):
    '''
    testing play functionality of hemorrhage
    Cost: 3
    Text: Whenever you make a successful run, place 1 virus counter on Hemorrhage. click, 2 hosted virus counters: The Corp trashes 1 card from HQ.
    '''

    def setUp(self):
        '''
        setup test environment for hemorrhage_04082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_hemorrhage_04082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_alpha_04087(unittest.TestCase):
    '''
    testing play functionality of alpha
    Cost: 7
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. This program can only interface with the outermost piece of ice protecting a server.
    '''

    def setUp(self):
        '''
        setup test environment for alpha_04087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_alpha_04087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_omega_04088(unittest.TestCase):
    '''
    testing play functionality of omega
    Cost: 7
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. This program can only interface with the innermost piece of ice protecting a server.
    '''

    def setUp(self):
        '''
        setup test environment for omega_04088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_omega_04088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_savoirfaire_04105(unittest.TestCase):
    '''
    testing play functionality of savoirfaire
    Cost: 0
    Text: You cannot use Savoir-faire more than once each turn. 2 credits: Install a program from your grip, paying the install cost.
    '''

    def setUp(self):
        '''
        setup test environment for savoirfaire_04105
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_savoirfaire_04105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paintbrush_04108(unittest.TestCase):
    '''
    testing play functionality of paintbrush
    Cost: 3
    Text: click: Choose a rezzed piece of ice. That ice gains sentry, code gate or barrier until the end of the next run this turn.
    '''

    def setUp(self):
        '''
        setup test environment for paintbrush_04108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_paintbrush_04108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_alias_05041(unittest.TestCase):
    '''
    testing play functionality of alias
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +3 strength. This program cannot interface with ice protecting a remote server.
    '''

    def setUp(self):
        '''
        setup test environment for alias_05041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_alias_05041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_breach_05042(unittest.TestCase):
    '''
    testing play functionality of breach
    Cost: 2
    Text: Interface -> 2 credits: Break up to 3 barrier subroutines. 2 credits: +4 strength. This program cannot interface with ice protecting a remote server.
    '''

    def setUp(self):
        '''
        setup test environment for breach_05042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_breach_05042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bug_05043(unittest.TestCase):
    '''
    testing play functionality of bug
    Cost: 0
    Text: Install only if you made a successful run on HQ this turn. Whenever the Corp draws a card, you may pay 2 credits to reveal that card.
    '''

    def setUp(self):
        '''
        setup test environment for bug_05043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_bug_05043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gingerbread_05044(unittest.TestCase):
    '''
    testing play functionality of gingerbread
    Cost: 2
    Text: Interface -> 1 credit: Break 1 tracer subroutine. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for gingerbread_05044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gingerbread_05044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_grappling_hook_05045(unittest.TestCase):
    '''
    testing play functionality of grappling_hook
    Cost: 2
    Text: trash: Break all but 1 subroutine on a piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for grappling_hook_05045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_grappling_hook_05045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_passport_05046(unittest.TestCase):
    '''
    testing play functionality of passport
    Cost: 1
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. This program cannot interface with ice protecting a remote server.
    '''

    def setUp(self):
        '''
        setup test environment for passport_05046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_passport_05046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_overmind_05053(unittest.TestCase):
    '''
    testing play functionality of overmind
    Cost: 4
    Text: When you install this program, place 1 power counter on it for each unused MU. (Place counters after this program's MU cost applies.) Interface -> Hosted power counter: Break 1 subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for overmind_05053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_overmind_05053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lamprey_06014(unittest.TestCase):
    '''
    testing play functionality of lamprey
    Cost: 1
    Text: Whenever you make a successful run on HQ, the Corp loses 1 credit. Trash Lamprey if the Corp purges virus counters.
    '''

    def setUp(self):
        '''
        setup test environment for lamprey_06014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_lamprey_06014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_leprechaun_06019(unittest.TestCase):
    '''
    testing play functionality of leprechaun
    Cost: 2
    Text: Leprechaun can host up to 2 programs. The memory costs of hosted programs do not count against your memory limit.
    '''

    def setUp(self):
        '''
        setup test environment for leprechaun_06019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_leprechaun_06019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_d4v1d_06033(unittest.TestCase):
    '''
    testing play functionality of d4v1d
    Cost: 3
    Text: Place 3 power counters on D4v1d when it is installed. Hosted power counter: Break ice subroutine on a piece of ice that has a strength of 5 or greater.
    '''

    def setUp(self):
        '''
        setup test environment for d4v1d_06033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_d4v1d_06033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cache_06037(unittest.TestCase):
    '''
    testing play functionality of cache
    Cost: 1
    Text: Place 3 virus counters on Cache when it is installed. Hosted virus counter: Gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for cache_06037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cache_06037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_llds_energy_regulator_06039(unittest.TestCase):
    '''
    testing play functionality of llds_energy_regulator
    Cost: 0
    Text: 3 credits or trash: Prevent an installed piece of hardware from being trashed.
    '''

    def setUp(self):
        '''
        setup test environment for llds_energy_regulator_06039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_llds_energy_regulator_06039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_blackat_06053(unittest.TestCase):
    '''
    testing play functionality of blackat
    Cost: 4
    Text: Interface -> 1 credit: Break 1 barrier subroutine. If you spent a credit from a stealth card to use this ability, instead break up to 3 barrier subroutines. 2 credits: +1 strength. If you spent at least 1 credit from a stealth card to use this ability, instead +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for blackat_06053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_blackat_06053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_refractor_06057(unittest.TestCase):
    '''
    testing play functionality of refractor
    Cost: 1
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +3 strength. Use this ability only by spending a credit from a stealth card.
    '''

    def setUp(self):
        '''
        setup test environment for refractor_06057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_refractor_06057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_origami_06074(unittest.TestCase):
    '''
    testing play functionality of origami
    Cost: 0
    Text: Your maximum hand size is increased by 1 for each copy of Origami installed.
    '''

    def setUp(self):
        '''
        setup test environment for origami_06074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_origami_06074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_switchblade_06077(unittest.TestCase):
    '''
    testing play functionality of switchblade
    Cost: 3
    Text: Interface -> 1 credit: Break any number of sentry subroutines. Use this ability only by spending a credit from a stealth card. 1 credit: +7 strength. Use this ability only by spending a credit from a stealth card.
    '''

    def setUp(self):
        '''
        setup test environment for switchblade_06077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_switchblade_06077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cerberus_cuj0_h3_06094(unittest.TestCase):
    '''
    testing play functionality of cerberus_cuj0_h3
    Cost: 3
    Text: When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 sentry subroutines. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for cerberus_cuj0_h3_06094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cerberus_cuj0_h3_06094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cerberus_rex_h2_06096(unittest.TestCase):
    '''
    testing play functionality of cerberus_rex_h2
    Cost: 3
    Text: When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for cerberus_rex_h2_06096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cerberus_rex_h2_06096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cerberus_lady_h1_06099(unittest.TestCase):
    '''
    testing play functionality of cerberus_lady_h1
    Cost: 4
    Text: When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 barrier subroutines. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for cerberus_lady_h1_06099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cerberus_lady_h1_06099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_incubator_06113(unittest.TestCase):
    '''
    testing play functionality of incubator
    Cost: 3
    Text: When your turn begins, place 1 virus counter on Incubator. click, trash: Move all virus counters from Incubator to another installed virus program.
    '''

    def setUp(self):
        '''
        setup test environment for incubator_06113
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_incubator_06113()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ixodidae_06114(unittest.TestCase):
    '''
    testing play functionality of ixodidae
    Cost: 1
    Text: Whenever the Corp loses at least 1 credit, gain 1 credit. Trash Ixodidae if the Corp purges virus counters.
    '''

    def setUp(self):
        '''
        setup test environment for ixodidae_06114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_ixodidae_06114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_collective_consciousness_06116(unittest.TestCase):
    '''
    testing play functionality of collective_consciousness
    Cost: 2
    Text: Draw 1 card whenever the Corp rezzes a piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for collective_consciousness_06116
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_collective_consciousness_06116()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sage_06117(unittest.TestCase):
    '''
    testing play functionality of sage
    Cost: 4
    Text: This program gets +1 strength for each unused MU. Interface -> 2 credits: Break 1 code gate or 1 barrier subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for sage_06117
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sage_06117()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_au_revoir_06119(unittest.TestCase):
    '''
    testing play functionality of au_revoir
    Cost: 1
    Text: Gain 1 credit whenever you jack out.
    '''

    def setUp(self):
        '''
        setup test environment for au_revoir_06119
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_au_revoir_06119()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_eater_07040(unittest.TestCase):
    '''
    testing play functionality of eater
    Cost: 4
    Text: Interface -> 1 credit: Break 1 subroutine. You cannot access cards for the remainder of this run. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for eater_07040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_eater_07040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gravedigger_07041(unittest.TestCase):
    '''
    testing play functionality of gravedigger
    Cost: 2
    Text: Whenever an installed Corp card is trashed, place 1 virus counter on Gravedigger. click, hosted virus counter: The Corp trashes the top card of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for gravedigger_07041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gravedigger_07041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hivemind_07042(unittest.TestCase):
    '''
    testing play functionality of hivemind
    Cost: 3
    Text: Place 1 virus counter on Hivemind when it is installed. Virus counters on Hivemind are considered to be hosted on all other virus programs for the purposes of card effects (and can be spent as if on them).
    '''

    def setUp(self):
        '''
        setup test environment for hivemind_07042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_hivemind_07042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_progenitor_07043(unittest.TestCase):
    '''
    testing play functionality of progenitor
    Cost: 0
    Text: You can install virus programs onto this program. Limit 1 hosted program. The memory cost of the hosted program does not count against your memory limit. Interrupt -> Whenever virus counters would be purged, prevent 1 virus counter on the hosted program from being removed.
    '''

    def setUp(self):
        '''
        setup test environment for progenitor_07043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_progenitor_07043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_clot_08001(unittest.TestCase):
    '''
    testing play functionality of clot
    Cost: 2
    Text: The Corp cannot score an agenda during the same turn they installed that agenda. When the Corp purges virus counters, trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for clot_08001
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_clot_08001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spike_08004(unittest.TestCase):
    '''
    testing play functionality of spike
    Cost: 1
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. This program gets +1 strength for each installed icebreaker. Interface -> trash: Break up to 3 barrier subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for spike_08004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_spike_08004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_study_guide_08028(unittest.TestCase):
    '''
    testing play functionality of study_guide
    Cost: 3
    Text: This program gets +1 strength for each hosted power counter. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: Place 1 power counter on this program.
    '''

    def setUp(self):
        '''
        setup test environment for study_guide_08028
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_study_guide_08028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crowbar_08046(unittest.TestCase):
    '''
    testing play functionality of crowbar
    Cost: 1
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. This program gets +1 strength for each installed icebreaker. Interface -> trash: Break up to 3 code gate subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for crowbar_08046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_crowbar_08046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_analog_dreamers_08048(unittest.TestCase):
    '''
    testing play functionality of analog_dreamers
    Cost: 2
    Text: click: Run R&D. If successful, instead of breaching R&D, you may choose 1 unrezzed non-ice card with no advancement counters on it. The Corp shuffles that card into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for analog_dreamers_08048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_analog_dreamers_08048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_faust_08061(unittest.TestCase):
    '''
    testing play functionality of faust
    Cost: 3
    Text: Interface -> Trash a card from your grip: Break 1 subroutine. Trash a card from your grip: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for faust_08061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_faust_08061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shiv_08066(unittest.TestCase):
    '''
    testing play functionality of shiv
    Cost: 0
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. This program gets +1 strength for each installed icebreaker. Interface -> trash: Break up to 3 sentry subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for shiv_08066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_shiv_08066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chameleon_08069(unittest.TestCase):
    '''
    testing play functionality of chameleon
    Cost: 2
    Text: When you install this program, choose barrier, code gate, or sentry. When your discard phase ends, add this program to your grip. Interface -> 1 credit: Break 1 subroutine on a piece of ice that has the chosen subtype.
    '''

    def setUp(self):
        '''
        setup test environment for chameleon_08069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_chameleon_08069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hyperdriver_08070(unittest.TestCase):
    '''
    testing play functionality of hyperdriver
    Cost: 1
    Text: When your turn begins, you may remove Hyperdriver from the game and gain click click click.
    '''

    def setUp(self):
        '''
        setup test environment for hyperdriver_08070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_hyperdriver_08070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_trope_08081(unittest.TestCase):
    '''
    testing play functionality of trope
    Cost: 1
    Text: When your turn begins, place 1 power counter on Trope. click, remove Trope from the game: Shuffle 1 card from your heap into your stack for each power counter on Trope.
    '''

    def setUp(self):
        '''
        setup test environment for trope_08081
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_trope_08081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_surfer_08102(unittest.TestCase):
    '''
    testing play functionality of surfer
    Cost: 2
    Text: 2 credits: Swap a piece of barrier ice currently being encountered with a piece of ice directly before or after it. The run continues from this new position. You are still encountering that ice.
    '''

    def setUp(self):
        '''
        setup test environment for surfer_08102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_surfer_08102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_davinci_08107(unittest.TestCase):
    '''
    testing play functionality of davinci
    Cost: 1
    Text: Whenever you make a successful run, place 1 power counter on DaVinci. trash: Install a card from your grip with an install cost equal to or less than the number of power counters on DaVinci, ignoring the install cost.
    '''

    def setUp(self):
        '''
        setup test environment for davinci_08107
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_davinci_08107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_endless_hunger_09033(unittest.TestCase):
    '''
    testing play functionality of endless_hunger
    Cost: 0
    Text: Interface -> Trash 1 installed card: Break 1 "Subroutine End the run." subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for endless_hunger_09033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_endless_hunger_09033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_harbinger_09034(unittest.TestCase):
    '''
    testing play functionality of harbinger
    Cost: 0
    Text: Interrupt -> When this program would be trashed, turn it facedown instead of adding it to your heap. (It is still considered trashed.)
    '''

    def setUp(self):
        '''
        setup test environment for harbinger_09034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_harbinger_09034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_multithreader_09040(unittest.TestCase):
    '''
    testing play functionality of multithreader
    Cost: 3
    Text: 2 recurring credits Use these credits to pay for using programs.
    '''

    def setUp(self):
        '''
        setup test environment for multithreader_09040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_multithreader_09040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gs_striker_m1_09048(unittest.TestCase):
    '''
    testing play functionality of gs_striker_m1
    Cost: 4
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break any number of code gate subroutines. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for gs_striker_m1_09048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gs_striker_m1_09048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gs_shrike_m2_09049(unittest.TestCase):
    '''
    testing play functionality of gs_shrike_m2
    Cost: 5
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break any number of sentry subroutines. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for gs_shrike_m2_09049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gs_shrike_m2_09049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gs_sherman_m3_09050(unittest.TestCase):
    '''
    testing play functionality of gs_sherman_m3
    Cost: 3
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break any number of barrier subroutines. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for gs_sherman_m3_09050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gs_sherman_m3_09050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mongoose_10005(unittest.TestCase):
    '''
    testing play functionality of mongoose
    Cost: 3
    Text: You cannot use this program to break subroutines on more than one ice per run. Interface -> 1 credit: Break up to 2 sentry subroutines. 2 credits: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for mongoose_10005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_mongoose_10005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_panchatantra_10008(unittest.TestCase):
    '''
    testing play functionality of panchatantra
    Cost: 2
    Text: Once per turn, when you encounter a piece of ice, you may have it gain 1 subtype of your choice that is not sentry, code gate, or barrier for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for panchatantra_10008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_panchatantra_10008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_diwan_10021(unittest.TestCase):
    '''
    testing play functionality of diwan
    Cost: 1
    Text: When you install this program, choose a server. As an additional cost to install a card in the root of or protecting that server, the Corp must pay 1 credit. When the Corp purges virus counters, trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for diwan_10021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_diwan_10021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sadyojata_10044(unittest.TestCase):
    '''
    testing play functionality of sadyojata
    Cost: 4
    Text: Interface -> 1 credit: Break 1 subroutine on a piece of ice with 3 or more subtypes. 1 credit: +1 strength. 2 credits: Swap this program with a deva program from your grip.
    '''

    def setUp(self):
        '''
        setup test environment for sadyojata_10044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sadyojata_10044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vamadeva_10061(unittest.TestCase):
    '''
    testing play functionality of vamadeva
    Cost: 6
    Text: Interface -> 1 credit: Break 1 subroutine on a piece of ice with exactly 1 subroutine. 1 credit: +1 strength. 2 credits: Swap this program with a deva program from your grip.
    '''

    def setUp(self):
        '''
        setup test environment for vamadeva_10061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_vamadeva_10061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_brahman_10062(unittest.TestCase):
    '''
    testing play functionality of brahman
    Cost: 4
    Text: Interface -> 1 credit: Break up to 2 subroutines. 2 credits: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, add 1 installed non-virus program to the top of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for brahman_10062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_brahman_10062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aghora_10097(unittest.TestCase):
    '''
    testing play functionality of aghora
    Cost: 5
    Text: Interface -> 1 credit: Break 1 subroutine on a piece of ice that has a rez cost of 5 or greater. 1 credit: +1 strength. 2 credits: Swap this program with a deva program from your grip.
    '''

    def setUp(self):
        '''
        setup test environment for aghora_10097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_aghora_10097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ankusa_10101(unittest.TestCase):
    '''
    testing play functionality of ankusa
    Cost: 6
    Text: Whenever this program fully breaks a barrier, add that barrier to HQ. Interface -> 2 credits: Break 1 barrier subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for ankusa_10101
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_ankusa_10101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dai_v_11006(unittest.TestCase):
    '''
    testing play functionality of dai_v
    Cost: 6
    Text: Interface -> 2 credits: Break all subroutines. Use this ability only by spending credits from stealth cards. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for dai_v_11006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_dai_v_11006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nfr_11023(unittest.TestCase):
    '''
    testing play functionality of nfr
    Cost: 3
    Text: Whenever this program fully breaks a piece of ice, place 1 power counter on this program. This program gets +1 strength for each power counter on it. Interface -> 1 credit: Break 1 barrier subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for nfr_11023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_nfr_11023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paperclip_11024(unittest.TestCase):
    '''
    testing play functionality of paperclip
    Cost: 4
    Text: Whenever you encounter a barrier, you may install this program from your heap. X credits: +X strength. Then, if this program can interface with the barrier you are encountering, break up to X subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for paperclip_11024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_paperclip_11024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_golden_11025(unittest.TestCase):
    '''
    testing play functionality of golden
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 sentry subroutines. 2 credits: +4 strength. 2 credits, add this program to your grip: Derez 1 sentry this program fully broke during this encounter.
    '''

    def setUp(self):
        '''
        setup test environment for golden_11025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_golden_11025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_black_orchestra_11042(unittest.TestCase):
    '''
    testing play functionality of black_orchestra
    Cost: 3
    Text: Whenever you encounter a code gate, you may install this program from your heap. 3 credits: +2 strength. Then, if this program can interface with the code gate you are encountering, break up to 2 subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for black_orchestra_11042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_black_orchestra_11042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_peregrine_11044(unittest.TestCase):
    '''
    testing play functionality of peregrine
    Cost: 5
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 3 credits: +3 strength. 2 credits, add this program to your grip: Derez 1 code gate this program fully broke during this encounter.
    '''

    def setUp(self):
        '''
        setup test environment for peregrine_11044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_peregrine_11044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_houdini_11045(unittest.TestCase):
    '''
    testing play functionality of houdini
    Cost: 2
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +4 strength for the remainder of this run. Use this ability only by spending at least 1 credit from a stealth card.
    '''

    def setUp(self):
        '''
        setup test environment for houdini_11045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_houdini_11045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_saker_11064(unittest.TestCase):
    '''
    testing play functionality of saker
    Cost: 4
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 2 credits: +2 strength. 2 credits, add this program to your grip: Derez 1 barrier this program fully broke during this encounter.
    '''

    def setUp(self):
        '''
        setup test environment for saker_11064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_saker_11064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_blackstone_11068(unittest.TestCase):
    '''
    testing play functionality of blackstone
    Cost: 4
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 3 credits: +4 strength for the remainder of this run. Use this ability only by spending at least 1 credit from a stealth card.
    '''

    def setUp(self):
        '''
        setup test environment for blackstone_11068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_blackstone_11068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mkultra_11081(unittest.TestCase):
    '''
    testing play functionality of mkultra
    Cost: 2
    Text: Whenever you encounter a sentry, you may install this program from your heap. 3 credits: +2 strength. Then, if this program can interface with the sentry you are encountering, break up to 2 subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for mkultra_11081
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_mkultra_11081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_equivocation_11084(unittest.TestCase):
    '''
    testing play functionality of equivocation
    Cost: 2
    Text: Whenever you make a successful run on R&D, you may reveal the top card of R&D. If you do, you may force the Corp to draw that card.
    '''

    def setUp(self):
        '''
        setup test environment for equivocation_11084
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_equivocation_11084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_misdirection_11085(unittest.TestCase):
    '''
    testing play functionality of misdirection
    Cost: 0
    Text: click, click, X credits: Remove X tags.
    '''

    def setUp(self):
        '''
        setup test environment for misdirection_11085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_misdirection_11085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reaver_11086(unittest.TestCase):
    '''
    testing play functionality of reaver
    Cost: 2
    Text: The first time you trash an installed card each turn, draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for reaver_11086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_reaver_11086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_baba_yaga_11088(unittest.TestCase):
    '''
    testing play functionality of baba_yaga
    Cost: 5
    Text: You may host any number of non-AI icebreaker programs on this program. This program gains the paid abilities of all hosted icebreaker programs.
    '''

    def setUp(self):
        '''
        setup test environment for baba_yaga_11088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_baba_yaga_11088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sunya_11102(unittest.TestCase):
    '''
    testing play functionality of sunya
    Cost: 3
    Text: Whenever this program fully breaks a piece of ice, place 1 power counter on this program. This program gets +1 strength for each power counter on it. Interface -> 2 credits: Break 1 sentry subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for sunya_11102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sunya_11102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tapwrm_11104(unittest.TestCase):
    '''
    testing play functionality of tapwrm
    Cost: 0
    Text: Install only if you made a successful run on a central server this turn. When your turn begins, gain 1 credit for every 5 credits in the Corp's credit pool. Trash Tapwrm if the Corp purges virus counters.
    '''

    def setUp(self):
        '''
        setup test environment for tapwrm_11104
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_tapwrm_11104()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tracker_11105(unittest.TestCase):
    '''
    testing play functionality of tracker
    Cost: 0
    Text: When your turn begins, you may choose a server. click, 2 credits: Run the chosen server. The first time a subroutine would resolve during that run, prevent it from resolving.
    '''

    def setUp(self):
        '''
        setup test environment for tracker_11105
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_tracker_11105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fawkes_11108(unittest.TestCase):
    '''
    testing play functionality of fawkes
    Cost: 5
    Text: Interface -> 1 credit: Break 1 sentry subroutine. X credits: +X strength for the remainder of this run. Use this ability only by spending at least 1 credit from a stealth card.
    '''

    def setUp(self):
        '''
        setup test environment for fawkes_11108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_fawkes_11108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_customized_secretary_12027(unittest.TestCase):
    '''
    testing play functionality of customized_secretary
    Cost: 2
    Text: When you install Customized Secretary reveal the top 5 cards of the stack. You may host any number of revealed programs from your stack on it. Shuffle your stack. click: Install a hosted program, paying all install costs.
    '''

    def setUp(self):
        '''
        setup test environment for customized_secretary_12027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_customized_secretary_12027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_berserker_12041(unittest.TestCase):
    '''
    testing play functionality of berserker
    Cost: 4
    Text: Whenever you encounter a barrier, for the remainder of that encounter this program gets +1 strength for each subroutine on that barrier. Interface -> 2 credits: Break up to 2 barrier subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for berserker_12041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_berserker_12041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_persephone_12042(unittest.TestCase):
    '''
    testing play functionality of persephone
    Cost: 5
    Text: Interface -> 2 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever you pass a sentry after encountering it, you may trash the top card of your stack. If you do, trash 1 card from the top of R&D for each subroutine on that sentry that resolved during that encounter.
    '''

    def setUp(self):
        '''
        setup test environment for persephone_12042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_persephone_12042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_inversificator_12048(unittest.TestCase):
    '''
    testing play functionality of inversificator
    Cost: 6
    Text: The first time each turn you pass a piece of ice after an encounter during which this program fully broke that ice, you may swap it with another installed piece of ice. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for inversificator_12048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_inversificator_12048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_massdriver_12067(unittest.TestCase):
    '''
    testing play functionality of massdriver
    Cost: 8
    Text: Whenever this program fully breaks a piece of ice, the first 3 subroutines of the next encounter this run do not resolve. Interface -> 2 credits: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for massdriver_12067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_massdriver_12067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_god_of_war_12082(unittest.TestCase):
    '''
    testing play functionality of god_of_war
    Cost: 4
    Text: When your turn begins, you may take 1 tag to place 2 virus counters on this program. Interface -> Hosted virus counter: Break 1 subroutine. 2 credits: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for god_of_war_12082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_god_of_war_12082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_flashbang_12085(unittest.TestCase):
    '''
    testing play functionality of flashbang
    Cost: 5
    Text: Interface -> 6 credits: Derez the sentry you are encountering. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for flashbang_12085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_flashbang_12085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_maven_12087(unittest.TestCase):
    '''
    testing play functionality of maven
    Cost: 5
    Text: This program gets +1 strength for each installed program. Interface -> 2 credits: Break 1 subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for maven_12087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_maven_12087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nanotk_12088(unittest.TestCase):
    '''
    testing play functionality of nanotk
    Cost: 4
    Text: During runs, this program gets +1 strength for each piece of ice protecting the attacked server. Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for nanotk_12088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_nanotk_12088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aumakua_12104(unittest.TestCase):
    '''
    testing play functionality of aumakua
    Cost: 3
    Text: This program gets +1 strength for each hosted virus counter. Whenever you expose a card, place 1 virus counter on this program. Whenever you finish breaching a server, if you did not steal or trash any accessed cards, place 1 virus counter on this program. Interface -> 1 credit: Break 1 subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for aumakua_12104
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_aumakua_12104()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_abagnale_13006(unittest.TestCase):
    '''
    testing play functionality of abagnale
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. trash: Bypass the code gate you are encountering.
    '''

    def setUp(self):
        '''
        setup test environment for abagnale_13006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_abagnale_13006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lustig_13007(unittest.TestCase):
    '''
    testing play functionality of lustig
    Cost: 5
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +5 strength. trash: Bypass the sentry you are encountering.
    '''

    def setUp(self):
        '''
        setup test environment for lustig_13007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_lustig_13007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_demara_13008(unittest.TestCase):
    '''
    testing play functionality of demara
    Cost: 4
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 2 credits: +3 strength. trash: Bypass the barrier you are encountering.
    '''

    def setUp(self):
        '''
        setup test environment for demara_13008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_demara_13008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mammon_13009(unittest.TestCase):
    '''
    testing play functionality of mammon
    Cost: 3
    Text: Interface -> Hosted power counter: Break 1 subroutine. 2 credits: +2 strength. When your turn begins, you may pay X credits to place X power counters on this program. When your turn ends, remove all hosted power counters.
    '''

    def setUp(self):
        '''
        setup test environment for mammon_13009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_mammon_13009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_adept_13017(unittest.TestCase):
    '''
    testing play functionality of adept
    Cost: 5
    Text: This program gets +1 strength for each unused MU. Interface -> 2 credits: Break 1 sentry or barrier subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for adept_13017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_adept_13017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_savant_13018(unittest.TestCase):
    '''
    testing play functionality of savant
    Cost: 4
    Text: This program gets +1 strength for each unused MU. Interface -> 2 credits: Break 1 sentry or 2 code gate subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for savant_13018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_savant_13018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_egret_13019(unittest.TestCase):
    '''
    testing play functionality of egret
    Cost: 2
    Text: Install only on a rezzed piece of ice. Host ice gains barrier, code gate, and sentry.
    '''

    def setUp(self):
        '''
        setup test environment for egret_13019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_egret_13019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dhegdheer_13020(unittest.TestCase):
    '''
    testing play functionality of dhegdheer
    Cost: 2
    Text: You can install other programs onto this program. Each program installed this way costs 1 credit less to install. Limit 1 hosted program. The memory cost of the hosted program does not count against your memory limit.
    '''

    def setUp(self):
        '''
        setup test environment for dhegdheer_13020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_dhegdheer_13020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_surveillance_network_key_14018(unittest.TestCase):
    '''
    testing play functionality of surveillance_network_key
    Cost: 2
    Text: Whenever the Corp spends click to draw 1 or more cards (including through a card ability), reveal the first card drawn.
    '''

    def setUp(self):
        '''
        setup test environment for surveillance_network_key_14018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_surveillance_network_key_14018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_surveillance_network_key_2_14019(unittest.TestCase):
    '''
    testing play functionality of surveillance_network_key_2
    Cost: 2
    Text: Whenever the Corp spends click to draw 1 or more cards (including through a card ability), reveal the first card drawn. 2 credits: For the remainder of this run, access 1 additional card whenever you access cards from HQ or R&D. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for surveillance_network_key_2_14019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_surveillance_network_key_2_14019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sneakdoor_prime_a_14026(unittest.TestCase):
    '''
    testing play functionality of sneakdoor_prime_a
    Cost: 6
    Text: click,click: Make a run on a remote server. If successful, instead treat it as a successful run on a central server.
    '''

    def setUp(self):
        '''
        setup test environment for sneakdoor_prime_a_14026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sneakdoor_prime_a_14026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sneakdoor_prime_b_14027(unittest.TestCase):
    '''
    testing play functionality of sneakdoor_prime_b
    Cost: 6
    Text: click,click: Make a run on a central server. If successful, instead treat it as a successful run on a remote server.
    '''

    def setUp(self):
        '''
        setup test environment for sneakdoor_prime_b_14027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sneakdoor_prime_b_14027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_darwin_20008(unittest.TestCase):
    '''
    testing play functionality of darwin
    Cost: 3
    Text: Interface -> 2 credits: Break 1 subroutine. X is equal to the number of hosted virus counters. When your turn begins, you may pay 1 credit to place 1 virus counter on this program.
    '''

    def setUp(self):
        '''
        setup test environment for darwin_20008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_darwin_20008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_datasucker_20009(unittest.TestCase):
    '''
    testing play functionality of datasucker
    Cost: 1
    Text: Whenever you make a successful run on a central server, place 1 virus counter on Datasucker. Hosted virus counter: Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.
    '''

    def setUp(self):
        '''
        setup test environment for datasucker_20009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_datasucker_20009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_force_of_nature_20010(unittest.TestCase):
    '''
    testing play functionality of force_of_nature
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for force_of_nature_20010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_force_of_nature_20010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_imp_20011(unittest.TestCase):
    '''
    testing play functionality of imp
    Cost: 2
    Text: When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for imp_20011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_imp_20011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hemorrhage_20012(unittest.TestCase):
    '''
    testing play functionality of hemorrhage
    Cost: 3
    Text: Whenever you make a successful run, place 1 virus counter on Hemorrhage. click, 2 hosted virus counters: The Corp trashes 1 card from HQ.
    '''

    def setUp(self):
        '''
        setup test environment for hemorrhage_20012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_hemorrhage_20012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mimic_20013(unittest.TestCase):
    '''
    testing play functionality of mimic
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for mimic_20013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_mimic_20013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_morning_star_20014(unittest.TestCase):
    '''
    testing play functionality of morning_star
    Cost: 8
    Text: Interface -> 1 credit: Break any number of barrier subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for morning_star_20014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_morning_star_20014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aurora_20027(unittest.TestCase):
    '''
    testing play functionality of aurora
    Cost: 3
    Text: Interface -> 2 credits: Break 1 barrier subroutine. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for aurora_20027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_aurora_20027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_faerie_20028(unittest.TestCase):
    '''
    testing play functionality of faerie
    Cost: 0
    Text: Interface -> 0 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for faerie_20028
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_faerie_20028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_femme_fatale_20029(unittest.TestCase):
    '''
    testing play functionality of femme_fatale
    Cost: 9
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.
    '''

    def setUp(self):
        '''
        setup test environment for femme_fatale_20029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_femme_fatale_20029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_peacock_20030(unittest.TestCase):
    '''
    testing play functionality of peacock
    Cost: 3
    Text: Interface -> 2 credits: Break 1 code gate subroutine. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for peacock_20030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_peacock_20030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pheromones_20031(unittest.TestCase):
    '''
    testing play functionality of pheromones
    Cost: 2
    Text: X recurring credits Use these credits during runs on HQ. X is the number of virus counters on Pheromones. Whenever you make a successful run on HQ, place 1 virus counter on Pheromones.
    '''

    def setUp(self):
        '''
        setup test environment for pheromones_20031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_pheromones_20031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sneakdoor_beta_20032(unittest.TestCase):
    '''
    testing play functionality of sneakdoor_beta
    Cost: 4
    Text: click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.
    '''

    def setUp(self):
        '''
        setup test environment for sneakdoor_beta_20032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sneakdoor_beta_20032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_battering_ram_20048(unittest.TestCase):
    '''
    testing play functionality of battering_ram
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 1 credit: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for battering_ram_20048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_battering_ram_20048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gordian_blade_20049(unittest.TestCase):
    '''
    testing play functionality of gordian_blade
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for gordian_blade_20049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gordian_blade_20049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_magnum_opus_20050(unittest.TestCase):
    '''
    testing play functionality of magnum_opus
    Cost: 5
    Text: click: Gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for magnum_opus_20050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_magnum_opus_20050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pipeline_20051(unittest.TestCase):
    '''
    testing play functionality of pipeline
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for pipeline_20051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_pipeline_20051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crypsis_20058(unittest.TestCase):
    '''
    testing play functionality of crypsis
    Cost: 5
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. click: Place 1 virus counter on this program. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for crypsis_20058
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_crypsis_20058()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_yusuf_21002(unittest.TestCase):
    '''
    testing play functionality of yusuf
    Cost: 1
    Text: Whenever you make a successful run, you may place 1 virus counter on this program. Interface -> Any virus counter: Break 1 barrier subroutine. Any virus counter: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for yusuf_21002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_yusuf_21002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_puffer_21004(unittest.TestCase):
    '''
    testing play functionality of puffer
    Cost: 4
    Text: This program gets +1 strength and costs +1 mu for each hosted power counter. Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. click: Place 1 power counter on this program or remove 1 hosted power counter.
    '''

    def setUp(self):
        '''
        setup test environment for puffer_21004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_puffer_21004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_upya_21007(unittest.TestCase):
    '''
    testing play functionality of upya
    Cost: 0
    Text: Whenever you make a successful run on R&D, you may place 1 power counter on Upya. click, 3 hosted power counters: Gain click click. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for upya_21007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_upya_21007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_plague_21022(unittest.TestCase):
    '''
    testing play functionality of plague
    Cost: 2
    Text: When you install Plague, choose a server. Whenever you make a successful run on the chosen server, you may place 2 virus counters on Plague.
    '''

    def setUp(self):
        '''
        setup test environment for plague_21022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_plague_21022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wari_21024(unittest.TestCase):
    '''
    testing play functionality of wari
    Cost: 1
    Text: The first time you make a successful run on HQ each turn, you may trash Wari to name sentry, code gate or barrier. Expose a piece of ice, then add it to HQ if it has the named subtype.
    '''

    def setUp(self):
        '''
        setup test environment for wari_21024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_wari_21024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_takobi_21026(unittest.TestCase):
    '''
    testing play functionality of takobi
    Cost: 2
    Text: Whenever you fully break a piece of ice, you may place 1 power counter on this program. 2 hosted power counters: Choose 1 installed non-AI icebreaker. That icebreaker gets +3 strength for the remainder of the current encounter.
    '''

    def setUp(self):
        '''
        setup test environment for takobi_21026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_takobi_21026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rng_key_21029(unittest.TestCase):
    '''
    testing play functionality of rng_key
    Cost: 0
    Text: The first time you make a successful run on HQ or R&D each turn, you may name a number. If you do, reveal the next card that you access this run. If it has a rez cost, play cost, or advancement requirement equal to the named number, either gain 3 credits or draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for rng_key_21029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_rng_key_21029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_exer_21041(unittest.TestCase):
    '''
    testing play functionality of exer
    Cost: 2
    Text: Whenever you breach R&D, access 1 additional card. When the Corp purges virus counters, trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for exer_21041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_exer_21041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nyashia_21067(unittest.TestCase):
    '''
    testing play functionality of nyashia
    Cost: 2
    Text: When you install this program, place 3 power counters on it. Whenever you breach R&D, you may remove 1 hosted power counter to access 1 additional card.
    '''

    def setUp(self):
        '''
        setup test environment for nyashia_21067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_nyashia_21067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_consume_21068(unittest.TestCase):
    '''
    testing play functionality of consume
    Cost: 2
    Text: Whenever you trash a Corp card, you may place 1 virus counter on Consume. click: Gain 2 credits for each hosted virus counter, then remove all virus counters from Consume.
    '''

    def setUp(self):
        '''
        setup test environment for consume_21068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_consume_21068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_trypano_21082(unittest.TestCase):
    '''
    testing play functionality of trypano
    Cost: 2
    Text: Install only on a piece of ice. When your turn begins, you may place 1 virus counter on this program. When there are 5 or more hosted virus counters, trash host ice.
    '''

    def setUp(self):
        '''
        setup test environment for trypano_21082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_trypano_21082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_laamb_21086(unittest.TestCase):
    '''
    testing play functionality of laamb
    Cost: 4
    Text: Whenever you encounter a piece of ice, you may pay 2 credits. If you do, it gains barrier for the remainder of that encounter. Use this ability only once per turn. Interface -> 2 credits: Break any number of barrier subroutines. 3 credits: +6 strength.
    '''

    def setUp(self):
        '''
        setup test environment for laamb_21086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_laamb_21086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_musaazi_21102(unittest.TestCase):
    '''
    testing play functionality of musaazi
    Cost: 1
    Text: Whenever you make a successful run, you may place 1 virus counter on this program. Interface -> Any virus counter: Break sentry subroutine. Any virus counter: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for musaazi_21102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_musaazi_21102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_amina_21104(unittest.TestCase):
    '''
    testing play functionality of amina
    Cost: 7
    Text: Interface -> 2 credits: Break up to 3 code gate subroutines. 2 credits: +3 strength. The first time each turn this program fully breaks a piece of ice, the Corp loses 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for amina_21104
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_amina_21104()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_engolo_21108(unittest.TestCase):
    '''
    testing play functionality of engolo
    Cost: 5
    Text: Whenever you encounter a piece of ice, you may pay 2 credits. If you do, it gains code gate for the remainder of that encounter. Use this ability only once per turn. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +4 strength.
    '''

    def setUp(self):
        '''
        setup test environment for engolo_21108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_engolo_21108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cradle_22006(unittest.TestCase):
    '''
    testing play functionality of cradle
    Cost: 4
    Text: This program gets -1 strength for each card in your grip. Interface -> 2 credits: Break any number of code gate subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for cradle_22006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cradle_22006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bankroll_22011(unittest.TestCase):
    '''
    testing play functionality of bankroll
    Cost: 1
    Text: Whenever you make a successful run, you may place 1 credit from the bank on Bankroll. trash: Take all credits from Bankroll.
    '''

    def setUp(self):
        '''
        setup test environment for bankroll_22011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_bankroll_22011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tycoon_22012(unittest.TestCase):
    '''
    testing play functionality of tycoon
    Cost: 1
    Text: Interface -> 1 credit: Break up to 2 barrier subroutines. 2 credits: +3 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, the Corp gains 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for tycoon_22012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_tycoon_22012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ika_22019(unittest.TestCase):
    '''
    testing play functionality of ika
    Cost: 0
    Text: 2 credits: Host this program on a piece of ice. Interface -> 1 credit: Break up to 2 subroutines on host sentry. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for ika_22019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_ika_22019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kyuban_22020(unittest.TestCase):
    '''
    testing play functionality of kyuban
    Cost: 0
    Text: Install only on a piece of ice. Whenever you pass host ice, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for kyuban_22020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_kyuban_22020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_algernon_22022(unittest.TestCase):
    '''
    testing play functionality of algernon
    Cost: 0
    Text: When your turn begins, you may pay 2 credits to gain click. If you do, trash Algernon when your turn ends if you did not make a successful run this turn.
    '''

    def setUp(self):
        '''
        setup test environment for algernon_22022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_algernon_22022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corroder_25010(unittest.TestCase):
    '''
    testing play functionality of corroder
    Cost: 2
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for corroder_25010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_corroder_25010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_datasucker_25011(unittest.TestCase):
    '''
    testing play functionality of datasucker
    Cost: 1
    Text: Whenever you make a successful run on a central server, place 1 virus counter on Datasucker. Hosted virus counter: Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.
    '''

    def setUp(self):
        '''
        setup test environment for datasucker_25011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_datasucker_25011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_force_of_nature_25012(unittest.TestCase):
    '''
    testing play functionality of force_of_nature
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for force_of_nature_25012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_force_of_nature_25012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_imp_25013(unittest.TestCase):
    '''
    testing play functionality of imp
    Cost: 2
    Text: When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for imp_25013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_imp_25013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lamprey_25014(unittest.TestCase):
    '''
    testing play functionality of lamprey
    Cost: 1
    Text: Whenever you make a successful run on HQ, the Corp loses 1 credit. Trash Lamprey if the Corp purges virus counters.
    '''

    def setUp(self):
        '''
        setup test environment for lamprey_25014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_lamprey_25014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mimic_25015(unittest.TestCase):
    '''
    testing play functionality of mimic
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for mimic_25015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_mimic_25015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_abagnale_25033(unittest.TestCase):
    '''
    testing play functionality of abagnale
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. trash: Bypass the code gate you are encountering.
    '''

    def setUp(self):
        '''
        setup test environment for abagnale_25033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_abagnale_25033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_demara_25034(unittest.TestCase):
    '''
    testing play functionality of demara
    Cost: 4
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 2 credits: +3 strength. trash: Bypass the barrier you are encountering.
    '''

    def setUp(self):
        '''
        setup test environment for demara_25034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_demara_25034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_faerie_25035(unittest.TestCase):
    '''
    testing play functionality of faerie
    Cost: 0
    Text: Interface -> 0 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for faerie_25035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_faerie_25035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_femme_fatale_25036(unittest.TestCase):
    '''
    testing play functionality of femme_fatale
    Cost: 9
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.
    '''

    def setUp(self):
        '''
        setup test environment for femme_fatale_25036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_femme_fatale_25036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sneakdoor_beta_25037(unittest.TestCase):
    '''
    testing play functionality of sneakdoor_beta
    Cost: 4
    Text: click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.
    '''

    def setUp(self):
        '''
        setup test environment for sneakdoor_beta_25037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sneakdoor_beta_25037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_atman_25051(unittest.TestCase):
    '''
    testing play functionality of atman
    Cost: 3
    Text: When you install this program, you may pay X credits to place X power counters on it. This program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength. Interface -> 1 credit: Break 1 subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for atman_25051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_atman_25051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_battering_ram_25052(unittest.TestCase):
    '''
    testing play functionality of battering_ram
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 1 credit: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for battering_ram_25052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_battering_ram_25052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_deus_x_25053(unittest.TestCase):
    '''
    testing play functionality of deus_x
    Cost: 3
    Text: Interface -> trash: Break any number of AP subroutines. Interrupt -> trash: Prevent any amount of net damage.
    '''

    def setUp(self):
        '''
        setup test environment for deus_x_25053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_deus_x_25053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gordian_blade_25054(unittest.TestCase):
    '''
    testing play functionality of gordian_blade
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for gordian_blade_25054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gordian_blade_25054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pipeline_25055(unittest.TestCase):
    '''
    testing play functionality of pipeline
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for pipeline_25055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_pipeline_25055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crypsis_25061(unittest.TestCase):
    '''
    testing play functionality of crypsis
    Cost: 5
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. click: Place 1 virus counter on this program. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for crypsis_25061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_crypsis_25061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chisel_26003(unittest.TestCase):
    '''
    testing play functionality of chisel
    Cost: 2
    Text: Install only on a piece of ice. Host ice gets -1 strength for each hosted virus counter. When you encounter host ice, if its strength is 0 or less, trash it. Otherwise, place 1 virus counter on this program.
    '''

    def setUp(self):
        '''
        setup test environment for chisel_26003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_chisel_26003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_stargate_26004(unittest.TestCase):
    '''
    testing play functionality of stargate
    Cost: 4
    Text: click: Run R&D. If successful, instead of breaching R&D, reveal the top 3 cards of R&D. Trash 1 of the revealed cards. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for stargate_26004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_stargate_26004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_utae_26005(unittest.TestCase):
    '''
    testing play functionality of utae
    Cost: 2
    Text: Interface -> X credits: Break X code gate subroutines. Use this ability only once per run. Interface -> 1 credit: Break 1 code gate subroutine. Use this ability only if you have 3 or more installed virtual resources. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for utae_26005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_utae_26005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bukhgalter_26016(unittest.TestCase):
    '''
    testing play functionality of bukhgalter
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 1 credit: +1 strength. The first time each turn this program fully breaks a piece of ice, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for bukhgalter_26016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_bukhgalter_26016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gauss_26024(unittest.TestCase):
    '''
    testing play functionality of gauss
    Cost: 2
    Text: When you install this program, it gets +3 strength for the remainder of the turn. Interface -> 1 credit: Break 1 barrier subroutine. 2 credits: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for gauss_26024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gauss_26024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pelangi_26025(unittest.TestCase):
    '''
    testing play functionality of pelangi
    Cost: 1
    Text: When you install this program, place 2 virus counters on it. Hosted virus counter: Choose an ice subtype. The ice you are encountering gains that subtype for the remainder of the encounter. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for pelangi_26025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_pelangi_26025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rezeki_26026(unittest.TestCase):
    '''
    testing play functionality of rezeki
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for rezeki_26026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_rezeki_26026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_odore_26071(unittest.TestCase):
    '''
    testing play functionality of odore
    Cost: 4
    Text: Interface -> 2 credits: Break any number of sentry subroutines. Interface -> 0 credits: Break 1 sentry subroutine. Use this ability only if you have 3 or more installed virtual resources. 3 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for odore_26071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_odore_26071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_afterimage_26079(unittest.TestCase):
    '''
    testing play functionality of afterimage
    Cost: 4
    Text: Whenever you encounter a sentry, you may pay 2 credits to bypass it. Use this ability only once per turn and only by spending credits from stealth cards. Interface -> 1 credit: Break up to 2 sentry subroutines. 1 credit: +2 strength. Use this ability only by spending a credit from a stealth card.
    '''

    def setUp(self):
        '''
        setup test environment for afterimage_26079
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_afterimage_26079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_makler_26080(unittest.TestCase):
    '''
    testing play functionality of makler
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 2 credits: +2 strength. The first time each turn this program fully breaks a piece of ice, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for makler_26080
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_makler_26080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cordyceps_26086(unittest.TestCase):
    '''
    testing play functionality of cordyceps
    Cost: 3
    Text: When you install this program, place 2 virus counters on it. Whenever you make a successful run on a central server, you may remove 1 hosted virus counter to swap a piece of ice protecting that server with another installed piece of ice. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for cordyceps_26086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cordyceps_26086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_euler_26087(unittest.TestCase):
    '''
    testing play functionality of euler
    Cost: 2
    Text: When you install this program, for the remainder of the turn it gains "Interface -> 0 credits: Break 1 code gate subroutine." Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for euler_26087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_euler_26087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mantle_26088(unittest.TestCase):
    '''
    testing play functionality of mantle
    Cost: 1
    Text: 1 recurring credit Spend hosted credits to use hardware and programs.
    '''

    def setUp(self):
        '''
        setup test environment for mantle_26088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_mantle_26088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_penrose_26089(unittest.TestCase):
    '''
    testing play functionality of penrose
    Cost: 3
    Text: When you install this program, for the remainder of the turn it gains "Interface -> 1 credit: Break 1 barrier subroutine." Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +3 strength. Use this ability only by spending a credit from a stealth card.
    '''

    def setUp(self):
        '''
        setup test environment for penrose_26089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_penrose_26089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_selfmodifying_code_26090(unittest.TestCase):
    '''
    testing play functionality of selfmodifying_code
    Cost: 0
    Text: 2 credits, trash: Search your stack for a program. Install it.
    '''

    def setUp(self):
        '''
        setup test environment for selfmodifying_code_26090
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_selfmodifying_code_26090()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_medium_29001(unittest.TestCase):
    '''
    testing play functionality of medium
    Cost: 3
    Text: Whenever you make a successful run on R&D, place 1 virus counter on this program. Whenever you breach R&D, choose a number less than the number of hosted virus counters. Access that many additional cards.
    '''

    def setUp(self):
        '''
        setup test environment for medium_29001
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_medium_29001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_parasite_29002(unittest.TestCase):
    '''
    testing play functionality of parasite
    Cost: 2
    Text: Install only on a rezzed piece of ice. When your turn begins, place 1 virus counter on this program. Host ice gets -1 strength for each hosted virus counter. When the strength of host ice is 0 or less, trash it.
    '''

    def setUp(self):
        '''
        setup test environment for parasite_29002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_parasite_29002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cache_29004(unittest.TestCase):
    '''
    testing play functionality of cache
    Cost: 1
    Text: Place 3 virus counters on Cache when it is installed. Hosted virus counter: Gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for cache_29004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cache_29004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cerberus_lady_h1_29006(unittest.TestCase):
    '''
    testing play functionality of cerberus_lady_h1
    Cost: 4
    Text: When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 barrier subroutines. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for cerberus_lady_h1_29006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cerberus_lady_h1_29006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_botulus_30004(unittest.TestCase):
    '''
    testing play functionality of botulus
    Cost: 2
    Text: Install only on a piece of ice. When you install this program and when your turn begins, place 1 virus counter on this program. Hosted virus counter: Break 1 subroutine on host ice.
    '''

    def setUp(self):
        '''
        setup test environment for botulus_30004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_botulus_30004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_buzzsaw_30005(unittest.TestCase):
    '''
    testing play functionality of buzzsaw
    Cost: 4
    Text: Interface -> 1 credit: Break up to 2 code gate subroutines. 3 credits: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for buzzsaw_30005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_buzzsaw_30005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cleaver_30006(unittest.TestCase):
    '''
    testing play functionality of cleaver
    Cost: 3
    Text: Interface -> 1 credit: Break up to 2 barrier subroutines. 2 credits: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for cleaver_30006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cleaver_30006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fermenter_30007(unittest.TestCase):
    '''
    testing play functionality of fermenter
    Cost: 1
    Text: When you install this program and when your turn begins, place 1 virus counter on this program. click, trash: Gain 2 credits for each hosted virus counter.
    '''

    def setUp(self):
        '''
        setup test environment for fermenter_30007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_fermenter_30007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_leech_30008(unittest.TestCase):
    '''
    testing play functionality of leech
    Cost: 1
    Text: Whenever you make a successful run on a central server, place 1 virus counter on this program. Hosted virus counter: The ice you are encountering gets -1 strength for the remainder of this encounter.
    '''

    def setUp(self):
        '''
        setup test environment for leech_30008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_leech_30008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_carmen_30015(unittest.TestCase):
    '''
    testing play functionality of carmen
    Cost: 5
    Text: If you made a successful run this turn, this program costs 2 credits less to install. Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for carmen_30015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_carmen_30015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marjanah_30016(unittest.TestCase):
    '''
    testing play functionality of marjanah
    Cost: 0
    Text: Interface -> 2 credits: Break 1 barrier subroutine. If you made a successful run this turn, this ability costs 1 credit less to use. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for marjanah_30016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_marjanah_30016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tranquilizer_30017(unittest.TestCase):
    '''
    testing play functionality of tranquilizer
    Cost: 2
    Text: Install only on a piece of ice. When you install this program and when your turn begins, place 1 virus counter on this program. Then, if there are 3 or more hosted virus counters, derez host ice.
    '''

    def setUp(self):
        '''
        setup test environment for tranquilizer_30017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_tranquilizer_30017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_conduit_30024(unittest.TestCase):
    '''
    testing play functionality of conduit
    Cost: 4
    Text: Whenever a successful run on R&D ends, you may place 1 virus counter on this program. click: Run R&D. If successful, access X additional cards when you breach R&D. X is equal to the number of hosted virus counters.
    '''

    def setUp(self):
        '''
        setup test environment for conduit_30024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_conduit_30024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_echelon_30025(unittest.TestCase):
    '''
    testing play functionality of echelon
    Cost: 3
    Text: This program gets +1 strength for each installed icebreaker (including this one). Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for echelon_30025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_echelon_30025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_unity_30026(unittest.TestCase):
    '''
    testing play functionality of unity
    Cost: 3
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for each installed icebreaker (including this one).
    '''

    def setUp(self):
        '''
        setup test environment for unity_30026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_unity_30026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mayfly_30032(unittest.TestCase):
    '''
    testing play functionality of mayfly
    Cost: 1
    Text: Interface -> 1 credit: Break 1 subroutine. When this run ends, trash this program. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for mayfly_30032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_mayfly_30032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_clot_31005(unittest.TestCase):
    '''
    testing play functionality of clot
    Cost: 2
    Text: The Corp cannot score an agenda during the same turn they installed that agenda. When the Corp purges virus counters, trash this program.
    '''

    def setUp(self):
        '''
        setup test environment for clot_31005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_clot_31005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corroder_31006(unittest.TestCase):
    '''
    testing play functionality of corroder
    Cost: 2
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for corroder_31006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_corroder_31006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_imp_31007(unittest.TestCase):
    '''
    testing play functionality of imp
    Cost: 2
    Text: When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for imp_31007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_imp_31007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mimic_31008(unittest.TestCase):
    '''
    testing play functionality of mimic
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for mimic_31008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_mimic_31008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_abagnale_31021(unittest.TestCase):
    '''
    testing play functionality of abagnale
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. trash: Bypass the code gate you are encountering.
    '''

    def setUp(self):
        '''
        setup test environment for abagnale_31021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_abagnale_31021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_femme_fatale_31022(unittest.TestCase):
    '''
    testing play functionality of femme_fatale
    Cost: 9
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.
    '''

    def setUp(self):
        '''
        setup test environment for femme_fatale_31022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_femme_fatale_31022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sneakdoor_beta_31023(unittest.TestCase):
    '''
    testing play functionality of sneakdoor_beta
    Cost: 4
    Text: click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.
    '''

    def setUp(self):
        '''
        setup test environment for sneakdoor_beta_31023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_sneakdoor_beta_31023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_atman_31030(unittest.TestCase):
    '''
    testing play functionality of atman
    Cost: 3
    Text: When you install this program, you may pay X credits to place X power counters on it. This program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength. Interface -> 1 credit: Break 1 subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for atman_31030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_atman_31030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chameleon_31031(unittest.TestCase):
    '''
    testing play functionality of chameleon
    Cost: 2
    Text: When you install this program, choose barrier, code gate, or sentry. When your discard phase ends, add this program to your grip. Interface -> 1 credit: Break 1 subroutine on a piece of ice that has the chosen subtype.
    '''

    def setUp(self):
        '''
        setup test environment for chameleon_31031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_chameleon_31031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_egret_31032(unittest.TestCase):
    '''
    testing play functionality of egret
    Cost: 2
    Text: Install only on a rezzed piece of ice. Host ice gains barrier, code gate, and sentry.
    '''

    def setUp(self):
        '''
        setup test environment for egret_31032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_egret_31032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gordian_blade_31033(unittest.TestCase):
    '''
    testing play functionality of gordian_blade
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for gordian_blade_31033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_gordian_blade_31033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paricia_31034(unittest.TestCase):
    '''
    testing play functionality of paricia
    Cost: 0
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs of assets.
    '''

    def setUp(self):
        '''
        setup test environment for paricia_31034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_paricia_31034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_revolver_32002(unittest.TestCase):
    '''
    testing play functionality of revolver
    Cost: 2
    Text: When you install this program, place 6 power counters on it. Interface -> trash or hosted power counter: Break 1 sentry subroutine. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for revolver_32002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_revolver_32002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_begemot_33007(unittest.TestCase):
    '''
    testing play functionality of begemot
    Cost: 5
    Text: When you install this program, suffer 1 core damage. This program gets +1 strength for each core damage you have taken this game. Interface -> 1 credit: Break any number of barrier subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for begemot_33007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_begemot_33007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cats_cradle_33016(unittest.TestCase):
    '''
    testing play functionality of cats_cradle
    Cost: 2
    Text: The rez cost of each piece of code gate ice is increased by 1 credit. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for cats_cradle_33016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cats_cradle_33016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cezve_33017(unittest.TestCase):
    '''
    testing play functionality of cezve
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits during runs on central servers.
    '''

    def setUp(self):
        '''
        setup test environment for cezve_33017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_cezve_33017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_revolver_33018(unittest.TestCase):
    '''
    testing play functionality of revolver
    Cost: 2
    Text: When you install this program, place 6 power counters on it. Interface -> trash or hosted power counter: Break 1 sentry subroutine. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for revolver_33018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_revolver_33018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hyperbaric_33026(unittest.TestCase):
    '''
    testing play functionality of hyperbaric
    Cost: 3
    Text: When you install this program, place 1 power counter on it. This program gets +1 strength for each hosted power counter. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: Place 1 power counter on this program.
    '''

    def setUp(self):
        '''
        setup test environment for hyperbaric_33026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_hyperbaric_33026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_propeller_33027(unittest.TestCase):
    '''
    testing play functionality of propeller
    Cost: 1
    Text: When you install this program, place 4 power counters on it. Interface -> 1 credit: Break 1 barrier subroutine. Hosted power counter: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for propeller_33027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_propeller_33027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_abaasy_33070(unittest.TestCase):
    '''
    testing play functionality of abaasy
    Cost: 2
    Text: The first time each turn this program fully breaks a piece of ice, you may trash 1 card from your grip to draw 1 card. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for abaasy_33070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_abaasy_33070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hush_33071(unittest.TestCase):
    '''
    testing play functionality of hush
    Cost: 1
    Text: Install only on a piece of ice. Host ice cannot gain abilities and loses all abilities except its printed subroutines. click: Host this program on another installed piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for hush_33071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_hush_33071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nga_33072(unittest.TestCase):
    '''
    testing play functionality of nga
    Cost: 2
    Text: When you install this program, load 3 power counters onto it. When it is empty, trash it. The first time each turn you make a successful run, you may remove 1 hosted power counter to sabotage 1. (The Corp trashes 1 card of their choice from HQ or the top of R&D.)
    '''

    def setUp(self):
        '''
        setup test environment for nga_33072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_nga_33072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_num_33073(unittest.TestCase):
    '''
    testing play functionality of num
    Cost: 4
    Text: Interface -> 2 credits: Break 1 sentry subroutine.
    '''

    def setUp(self):
        '''
        setup test environment for num_33073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_num_33073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tremolo_33080(unittest.TestCase):
    '''
    testing play functionality of tremolo
    Cost: 3
    Text: Interface -> 3 credits: Break up to 2 barrier subroutines. This ability costs 1 credit less to use for each installed piece of cybernetic hardware. 2 credits: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for tremolo_33080
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_tremolo_33080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tunnel_vision_33081(unittest.TestCase):
    '''
    testing play functionality of tunnel_vision
    Cost: 2
    Text: When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) Interface -> 2 credits: Break up to 2 subroutines on a piece of ice protecting your mark. 2 credits: +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for tunnel_vision_33081
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_tunnel_vision_33081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_flux_capacitor_33087(unittest.TestCase):
    '''
    testing play functionality of flux_capacitor
    Cost: 0
    Text: Install only on a piece of ice. The first time you break a subroutine during each encounter with host ice, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)
    '''

    def setUp(self):
        '''
        setup test environment for flux_capacitor_33087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_flux_capacitor_33087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nanuq_33088(unittest.TestCase):
    '''
    testing play functionality of nanuq
    Cost: 4
    Text: When this program is uninstalled, remove it from the game. When an agenda is scored or stolen, remove this program from the game. Interface -> 2 credits: Break up to 2 subroutines. 1 credit: +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for nanuq_33088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_nanuq_33088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_orca_33089(unittest.TestCase):
    '''
    testing play functionality of orca
    Cost: 10
    Text: The first time each turn this program fully breaks a piece of ice, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.) Interface -> 2 credits: Break any number of sentry subroutines. 2 credits: +3 strength.
    '''

    def setUp(self):
        '''
        setup test environment for orca_33089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_orca_33089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_k2cp_turbine_33090(unittest.TestCase):
    '''
    testing play functionality of k2cp_turbine
    Cost: 4
    Text: Each installed non-AI icebreaker gets +2 strength.
    '''

    def setUp(self):
        '''
        setup test environment for k2cp_turbine_33090
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_k2cp_turbine_33090()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_world_tree_33091(unittest.TestCase):
    '''
    testing play functionality of world_tree
    Cost: 6
    Text: The first time each turn you make a successful run, you may trash 1 of your other installed cards to search your stack for 1 card of the same type. (Shuffle your stack after searching it.) Install the card you found, paying 3 credits less.
    '''

    def setUp(self):
        '''
        setup test environment for world_tree_33091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_world_tree_33091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_matryoshka_33094(unittest.TestCase):
    '''
    testing play functionality of matryoshka
    Cost: 3
    Text: When your turn begins, turn each hosted card faceup. click: Host a copy of Matryoshka from your grip faceup on this program. (It is not installed.) Interface -> X{c}, turn 1 hosted copy of Matryoshka facedown: Break X subroutines. 1 credit: +1 strength. Limit 6 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for matryoshka_33094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = program_matryoshka_33094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")
