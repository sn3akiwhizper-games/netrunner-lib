
'''
test cases for card classes of type ice
'''
import unittest

from netrunner_lib.cards._base_card_classes import Ice
from netrunner_lib.cards.ice import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
class Test_heimdall_10_01061(unittest.TestCase):
    '''
    testing play functionality of heimdall_10
    Cost: 8
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for heimdall_10_01061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_heimdall_10_01061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ichi_10_01062(unittest.TestCase):
    '''
    testing play functionality of ichi_10
    Cost: 5
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for ichi_10_01062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ichi_10_01062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_viktor_10_01063(unittest.TestCase):
    '''
    testing play functionality of viktor_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for viktor_10_01063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_viktor_10_01063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rototurret_01064(unittest.TestCase):
    '''
    testing play functionality of rototurret
    Cost: 4
    Text: Subroutine Trash 1 installed program. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for rototurret_01064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_rototurret_01064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cell_portal_01074(unittest.TestCase):
    '''
    testing play functionality of cell_portal
    Cost: 5
    Text: Subroutine The Runner moves to the outermost position of the attacked server. They may jack out. Derez this ice.
    '''

    def setUp(self):
        '''
        setup test environment for cell_portal_01074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_cell_portal_01074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chum_01075(unittest.TestCase):
    '''
    testing play functionality of chum
    Cost: 1
    Text: Subroutine The next piece of ice the Runner encounters during this run gets +2 strength. When that encounter ends, if the Runner did not fully break that ice, do 3 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for chum_01075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_chum_01075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_mine_01076(unittest.TestCase):
    '''
    testing play functionality of data_mine
    Cost: 0
    Text: Subroutine Do 1 net damage. Trash Data Mine.
    '''

    def setUp(self):
        '''
        setup test environment for data_mine_01076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_data_mine_01076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_neural_katana_01077(unittest.TestCase):
    '''
    testing play functionality of neural_katana
    Cost: 4
    Text: Subroutine Do 3 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for neural_katana_01077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_neural_katana_01077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wall_of_thorns_01078(unittest.TestCase):
    '''
    testing play functionality of wall_of_thorns
    Cost: 8
    Text: Subroutine Do 2 net damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wall_of_thorns_01078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wall_of_thorns_01078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_raven_01088(unittest.TestCase):
    '''
    testing play functionality of data_raven
    Cost: 4
    Text: When the Runner encounters this ice, they must take 1 tag or end the run. Hosted power counter: Give the Runner 1 tag. Subroutine Trace[3]. If successful, place 1 power counter on this ice.
    '''

    def setUp(self):
        '''
        setup test environment for data_raven_01088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_data_raven_01088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_matrix_analyzer_01089(unittest.TestCase):
    '''
    testing play functionality of matrix_analyzer
    Cost: 1
    Text: When the Runner encounters Matrix Analyzer, you may pay 1 credit to place 1 advancement token on a card that can be advanced. Subroutine Trace[2]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for matrix_analyzer_01089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_matrix_analyzer_01089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tollbooth_01090(unittest.TestCase):
    '''
    testing play functionality of tollbooth
    Cost: 8
    Text: When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for tollbooth_01090
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tollbooth_01090()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_archer_01101(unittest.TestCase):
    '''
    testing play functionality of archer
    Cost: 4
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for archer_01101
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_archer_01101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hadrians_wall_01102(unittest.TestCase):
    '''
    testing play functionality of hadrians_wall
    Cost: 10
    Text: Hadrian's Wall can be advanced and has +1 strength for each advancement token on it. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hadrians_wall_01102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hadrians_wall_01102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ice_wall_01103(unittest.TestCase):
    '''
    testing play functionality of ice_wall
    Cost: 1
    Text: You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for ice_wall_01103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ice_wall_01103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shadow_01104(unittest.TestCase):
    '''
    testing play functionality of shadow
    Cost: 3
    Text: Shadow can be advanced and has +1 strength for each advancement token on it. Subroutine The Corp gains 2 credits. Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for shadow_01104
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_shadow_01104()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_enigma_01111(unittest.TestCase):
    '''
    testing play functionality of enigma
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for enigma_01111
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_enigma_01111()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hunter_01112(unittest.TestCase):
    '''
    testing play functionality of hunter
    Cost: 1
    Text: Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for hunter_01112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hunter_01112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wall_of_static_01113(unittest.TestCase):
    '''
    testing play functionality of wall_of_static
    Cost: 3
    Text: Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wall_of_static_01113
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wall_of_static_01113()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_janus_10_02012(unittest.TestCase):
    '''
    testing play functionality of janus_10
    Cost: 15
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine Do 1 core damage. Subroutine Do 1 core damage. Subroutine Do 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for janus_10_02012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_janus_10_02012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_snowflake_02015(unittest.TestCase):
    '''
    testing play functionality of snowflake
    Cost: 1
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. End the run if you and the Runner spent a different number of credits.
    '''

    def setUp(self):
        '''
        setup test environment for snowflake_02015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_snowflake_02015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tmi_02017(unittest.TestCase):
    '''
    testing play functionality of tmi
    Cost: 3
    Text: When you rez TMI, Trace[2]. If unsuccessful, derez TMI. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for tmi_02017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tmi_02017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_caduceus_02019(unittest.TestCase):
    '''
    testing play functionality of caduceus
    Cost: 3
    Text: Subroutine Trace[3]. If successful, the Corp gains 3 credits. Subroutine Trace[2]. If successful, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for caduceus_02019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_caduceus_02019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_draco_02020(unittest.TestCase):
    '''
    testing play functionality of draco
    Cost: 1
    Text: When you rez Draco, you may pay X credits to place X power counters on it. Draco has +1 strength for each power counter on it. Subroutine Trace[2]. If successful, give the Runner 1 tag and end the run.
    '''

    def setUp(self):
        '''
        setup test environment for draco_02020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_draco_02020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sherlock_10_02030(unittest.TestCase):
    '''
    testing play functionality of sherlock_10
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trace[4]. If successful, add 1 installed program to the top of the Runner's stack. Subroutine Trace[4]. If successful, add 1 installed program to the top of the Runner's stack.
    '''

    def setUp(self):
        '''
        setup test environment for sherlock_10_02030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sherlock_10_02030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sensei_02034(unittest.TestCase):
    '''
    testing play functionality of sensei
    Cost: 3
    Text: Subroutine For the remainder of this run, each piece of ice encountered except Sensei gains "Subroutine End the run" after all its other subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for sensei_02034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sensei_02034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_viper_02052(unittest.TestCase):
    '''
    testing play functionality of viper
    Cost: 3
    Text: Subroutine Trace[3]. If successful, the Runner loses click, if able. Subroutine Trace[3]. If successful, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for viper_02052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_viper_02052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_popup_window_02056(unittest.TestCase):
    '''
    testing play functionality of popup_window
    Cost: 0
    Text: When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for popup_window_02056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_popup_window_02056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_woodcutter_02057(unittest.TestCase):
    '''
    testing play functionality of woodcutter
    Cost: 4
    Text: Woodcutter can be advanced only while rezzed and gains "Subroutine Do 1 net damage." for each advancement token on it.
    '''

    def setUp(self):
        '''
        setup test environment for woodcutter_02057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_woodcutter_02057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chimera_02060(unittest.TestCase):
    '''
    testing play functionality of chimera
    Cost: 2
    Text: When you rez Chimera, choose sentry, code gate, or barrier. Chimera gains that subtype until derezzed. When a turn ends, derez Chimera. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for chimera_02060
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_chimera_02060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hourglass_02071(unittest.TestCase):
    '''
    testing play functionality of hourglass
    Cost: 5
    Text: Subroutine The Runner loses click, if able. Subroutine The Runner loses click, if able. Subroutine The Runner loses click, if able.
    '''

    def setUp(self):
        '''
        setup test environment for hourglass_02071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hourglass_02071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bullfrog_02073(unittest.TestCase):
    '''
    testing play functionality of bullfrog
    Cost: 3
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits and this ice is installed, move this ice to the outermost position protecting another server. (The run continues from this new position.)
    '''

    def setUp(self):
        '''
        setup test environment for bullfrog_02073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bullfrog_02073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_uroboros_02074(unittest.TestCase):
    '''
    testing play functionality of uroboros
    Cost: 6
    Text: Subroutine Trace[4]. If successful, the Runner cannot make another run this turn. Subroutine Trace[4]. If successful, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for uroboros_02074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_uroboros_02074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tyrant_02078(unittest.TestCase):
    '''
    testing play functionality of tyrant
    Cost: 7
    Text: Tyrant can be advanced only while rezzed and gains "Subroutine End the run." for each advancement token on it.
    '''

    def setUp(self):
        '''
        setup test environment for tyrant_02078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tyrant_02078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_whirlpool_02094(unittest.TestCase):
    '''
    testing play functionality of whirlpool
    Cost: 0
    Text: Subroutine The Runner cannot jack out for the remainder of this run. Trash Whirlpool.
    '''

    def setUp(self):
        '''
        setup test environment for whirlpool_02094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_whirlpool_02094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_hound_02096(unittest.TestCase):
    '''
    testing play functionality of data_hound
    Cost: 1
    Text: Subroutine Trace[2]. If successful, look at the top X cards of the stack, where X is equal to the amount by which your trace strength exceeded the Runner's link strength. Trash 1 of those cards and arrange the rest in any order.
    '''

    def setUp(self):
        '''
        setup test environment for data_hound_02096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_data_hound_02096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_salvage_02098(unittest.TestCase):
    '''
    testing play functionality of salvage
    Cost: 2
    Text: Salvage can be advanced only while rezzed and gains Subroutine Trace[2]. If successful, give the Runner 1 tag. for each advancement token on it.
    '''

    def setUp(self):
        '''
        setup test environment for salvage_02098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_salvage_02098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_eli_10_02110(unittest.TestCase):
    '''
    testing play functionality of eli_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for eli_10_02110
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_eli_10_02110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_flare_02117(unittest.TestCase):
    '''
    testing play functionality of flare
    Cost: 9
    Text: Subroutine Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.
    '''

    def setUp(self):
        '''
        setup test environment for flare_02117
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_flare_02117()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_burke_bugs_02119(unittest.TestCase):
    '''
    testing play functionality of burke_bugs
    Cost: 0
    Text: Subroutine Trace[0]. If successful, the Runner trashes 1 program.
    '''

    def setUp(self):
        '''
        setup test environment for burke_bugs_02119
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_burke_bugs_02119()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_heimdall_20_03015(unittest.TestCase):
    '''
    testing play functionality of heimdall_20
    Cost: 11
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine Do 1 core damage and end the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for heimdall_20_03015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_heimdall_20_03015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_howler_03016(unittest.TestCase):
    '''
    testing play functionality of howler
    Cost: 1
    Text: Subroutine You may install and rez a piece of bioroid ice from HQ or Archives, ignoring all costs, placing it directly behind Howler. If you do, derez that piece of ice and trash Howler after the run is completed.
    '''

    def setUp(self):
        '''
        setup test environment for howler_03016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_howler_03016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ichi_20_03017(unittest.TestCase):
    '''
    testing play functionality of ichi_20
    Cost: 8
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[3]. If successful, do 1 core damage and give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for ichi_20_03017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ichi_20_03017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_minelayer_03018(unittest.TestCase):
    '''
    testing play functionality of minelayer
    Cost: 1
    Text: Subroutine You may install a piece of ice from HQ as the outermost piece of ice protecting this server, ignoring all install costs.
    '''

    def setUp(self):
        '''
        setup test environment for minelayer_03018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_minelayer_03018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_viktor_20_03019(unittest.TestCase):
    '''
    testing play functionality of viktor_20
    Cost: 5
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Hosted power counter: Do 1 core damage. Subroutine Trace[2]. If successful, place 1 power counter on this ice. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for viktor_20_03019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_viktor_20_03019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zed_10_03020(unittest.TestCase):
    '''
    testing play functionality of zed_10
    Cost: 2
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine If the Runner has lost click to break a subroutine during this run, do 1 core damage. Subroutine If the Runner has lost click to break a subroutine during this run, do 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for zed_10_03020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_zed_10_03020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bastion_03026(unittest.TestCase):
    '''
    testing play functionality of bastion
    Cost: 4
    Text: Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for bastion_03026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bastion_03026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_datapike_03027(unittest.TestCase):
    '''
    testing play functionality of datapike
    Cost: 4
    Text: Subroutine The Runner must pay 2 credits, if able. If the Runner cannot pay 2 credits, end the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for datapike_03027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_datapike_03027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_next_bronze_04011(unittest.TestCase):
    '''
    testing play functionality of next_bronze
    Cost: 2
    Text: NEXT Bronze has +1 strength for each rezzed piece of NEXT ice. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for next_bronze_04011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_next_bronze_04011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_himitsubako_04013(unittest.TestCase):
    '''
    testing play functionality of himitsubako
    Cost: 2
    Text: 1 credit: Add Himitsu-Bako to HQ. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for himitsubako_04013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_himitsubako_04013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_swarm_04018(unittest.TestCase):
    '''
    testing play functionality of swarm
    Cost: 8
    Text: When you rez Swarm, take 1 bad publicity. Swarm can be advanced and gains "Subroutine Trash 1 program unless the Runner pays 3 credits." for each advancement token on it.
    '''

    def setUp(self):
        '''
        setup test environment for swarm_04018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_swarm_04018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_grim_04020(unittest.TestCase):
    '''
    testing play functionality of grim
    Cost: 5
    Text: When you rez Grim, take 1 bad publicity. Subroutine Trash 1 program.
    '''

    def setUp(self):
        '''
        setup test environment for grim_04020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_grim_04020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wotan_04030(unittest.TestCase):
    '''
    testing play functionality of wotan
    Cost: 14
    Text: Subroutine End the run unless the Runner spends click click. Subroutine End the run unless the Runner pays 3 credits. Subroutine End the run unless the Runner trashes 1 installed program. Subroutine End the run unless the Runner suffers 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for wotan_04030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wotan_04030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_swordsman_04033(unittest.TestCase):
    '''
    testing play functionality of swordsman
    Cost: 3
    Text: The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for swordsman_04033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_swordsman_04033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_muckraker_04035(unittest.TestCase):
    '''
    testing play functionality of muckraker
    Cost: 5
    Text: When you rez Muckraker, take 1 bad publicity. Subroutine Trace[1]. If successful, give the Runner 1 tag. Subroutine Trace[2]. If successful, give the Runner 1 tag. Subroutine Trace[3]. If successful, give the Runner 1 tag. Subroutine End the run if the Runner is tagged.
    '''

    def setUp(self):
        '''
        setup test environment for muckraker_04035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_muckraker_04035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hudson_10_04051(unittest.TestCase):
    '''
    testing play functionality of hudson_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner cannot access more than 1 card during this run. Subroutine The Runner cannot access more than 1 card during this run.
    '''

    def setUp(self):
        '''
        setup test environment for hudson_10_04051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hudson_10_04051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_snoop_04056(unittest.TestCase):
    '''
    testing play functionality of snoop
    Cost: 6
    Text: When the Runner encounters Snoop, reveal all cards in the Runner's grip. Hosted power counter: Reveal all cards in the Runner's grip. Trash 1 of those cards. Subroutine Trace[3]. If successful, place 1 power counter on Snoop.
    '''

    def setUp(self):
        '''
        setup test environment for snoop_04056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_snoop_04056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ireress_04057(unittest.TestCase):
    '''
    testing play functionality of ireress
    Cost: 0
    Text: Ireress gains "Subroutine The Runner loses 1 credit" for each bad publicity you have.
    '''

    def setUp(self):
        '''
        setup test environment for ireress_04057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ireress_04057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paper_wall_04059(unittest.TestCase):
    '''
    testing play functionality of paper_wall
    Cost: 0
    Text: When the Runner fully breaks this ice, trash it. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for paper_wall_04059
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_paper_wall_04059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fenris_04071(unittest.TestCase):
    '''
    testing play functionality of fenris
    Cost: 4
    Text: When you rez this ice, take 1 bad publicity. Subroutine Do 1 core damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for fenris_04071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_fenris_04071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tsurugi_04074(unittest.TestCase):
    '''
    testing play functionality of tsurugi
    Cost: 6
    Text: Subroutine End the run unless the Corp pays 1 credit. Subroutine Do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for tsurugi_04074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tsurugi_04074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rsvp_04077(unittest.TestCase):
    '''
    testing play functionality of rsvp
    Cost: 3
    Text: Subroutine The Runner cannot spend any credits for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for rsvp_04077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_rsvp_04077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_curtain_wall_04078(unittest.TestCase):
    '''
    testing play functionality of curtain_wall
    Cost: 14
    Text: If Curtain Wall is the outermost piece of ice protecting a server, it has +4 strength. Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for curtain_wall_04078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_curtain_wall_04078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_yagura_04093(unittest.TestCase):
    '''
    testing play functionality of yagura
    Cost: 1
    Text: Subroutine Look at the top card of R&D. You may add that card to the bottom of R&D. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for yagura_04093
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_yagura_04093()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wraparound_04096(unittest.TestCase):
    '''
    testing play functionality of wraparound
    Cost: 2
    Text: While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wraparound_04096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wraparound_04096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gyri_labyrinth_04110(unittest.TestCase):
    '''
    testing play functionality of gyri_labyrinth
    Cost: 2
    Text: Subroutine The Runner's maximum hand size is reduced by 2 until the beginning of the Corp's next turn.
    '''

    def setUp(self):
        '''
        setup test environment for gyri_labyrinth_04110
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_gyri_labyrinth_04110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shinobi_04115(unittest.TestCase):
    '''
    testing play functionality of shinobi
    Cost: 7
    Text: When you rez Shinobi, take 1 bad publicity. Subroutine Trace[1]. If successful, do 1 net damage. Subroutine Trace[2]. If successful, do 2 net damage. Subroutine Trace[3]. If successful, do 3 net damage and end the run.
    '''

    def setUp(self):
        '''
        setup test environment for shinobi_04115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_shinobi_04115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marker_04116(unittest.TestCase):
    '''
    testing play functionality of marker
    Cost: 0
    Text: Subroutine The next piece of ice the Runner encounters gains "Subroutine End the run." after all its other subroutines for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for marker_04116
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_marker_04116()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hive_04117(unittest.TestCase):
    '''
    testing play functionality of hive
    Cost: 5
    Text: This ice loses 1 of its printed "Subroutine End the run." subroutines for each agenda point in your score area. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hive_04117
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hive_04117()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_quandary_04120(unittest.TestCase):
    '''
    testing play functionality of quandary
    Cost: 1
    Text: Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for quandary_04120
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_quandary_04120()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_inazuma_05016(unittest.TestCase):
    '''
    testing play functionality of inazuma
    Cost: 3
    Text: Subroutine During the next encounter this run, the Runner cannot break subroutines on the encountered ice. Subroutine The Runner cannot jack out this run until after their next encounter with a piece of ice begins.
    '''

    def setUp(self):
        '''
        setup test environment for inazuma_05016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_inazuma_05016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_komainu_05017(unittest.TestCase):
    '''
    testing play functionality of komainu
    Cost: 5
    Text: When the Runner encounters this ice, it gains X "Subroutine Do 1 net damage." subroutines for the remainder of this run. X is equal to the number of cards in the grip.
    '''

    def setUp(self):
        '''
        setup test environment for komainu_05017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_komainu_05017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pup_05018(unittest.TestCase):
    '''
    testing play functionality of pup
    Cost: 1
    Text: Subroutine Do 1 net damage unless the Runner pays 1 credit. Subroutine Do 1 net damage unless the Runner pays 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for pup_05018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_pup_05018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shiro_05019(unittest.TestCase):
    '''
    testing play functionality of shiro
    Cost: 6
    Text: Subroutine Look at the top 3 cards of R&D and arrange them in any order. Subroutine You may pay 1 credit. If you do not, the Runner breaches R&D. They cannot access cards in the root of R&D during that breach.
    '''

    def setUp(self):
        '''
        setup test environment for shiro_05019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_shiro_05019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_susanoonomikoto_05020(unittest.TestCase):
    '''
    testing play functionality of susanoonomikoto
    Cost: 9
    Text: Subroutine If the attacked server is not Archives, the Runner moves to the outermost position of Archives instead of passing this ice. The Runner cannot jack out this run until after they encounter a piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for susanoonomikoto_05020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_susanoonomikoto_05020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_guard_05024(unittest.TestCase):
    '''
    testing play functionality of guard
    Cost: 4
    Text: Guard cannot be bypassed. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for guard_05024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_guard_05024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rainbow_05025(unittest.TestCase):
    '''
    testing play functionality of rainbow
    Cost: 3
    Text: Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for rainbow_05025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_rainbow_05025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_next_silver_06002(unittest.TestCase):
    '''
    testing play functionality of next_silver
    Cost: 3
    Text: NEXT Silver gains "Subroutine End the run." for each rezzed piece of NEXT ice.
    '''

    def setUp(self):
        '''
        setup test environment for next_silver_06002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_next_silver_06002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lotus_field_06003(unittest.TestCase):
    '''
    testing play functionality of lotus_field
    Cost: 5
    Text: The strength of this ice cannot be lowered. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for lotus_field_06003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_lotus_field_06003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_taurus_06009(unittest.TestCase):
    '''
    testing play functionality of taurus
    Cost: 5
    Text: Subroutine Trace[2]. If successful, trash 1 piece of hardware. If your trace strength is 5 or greater, trash 1 piece of hardware.
    '''

    def setUp(self):
        '''
        setup test environment for taurus_06009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_taurus_06009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mother_goddess_06010(unittest.TestCase):
    '''
    testing play functionality of mother_goddess
    Cost: 4
    Text: Mother Goddess gains the subtypes of all other rezzed ice. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for mother_goddess_06010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_mother_goddess_06010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_galahad_06011(unittest.TestCase):
    '''
    testing play functionality of galahad
    Cost: 2
    Text: When the Runner encounters Galahad, you may reveal up to 2 grail ice from HQ. For the remainder of this run, Galahad gains the subroutines of the revealed ice in the order of your choice. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for galahad_06011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_galahad_06011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_information_overload_06027(unittest.TestCase):
    '''
    testing play functionality of information_overload
    Cost: 6
    Text: When the Runner encounters this ice, Trace[1]. If successful, give them 1 tag. This ice gains "Subroutine The Runner trashes 1 of their installed cards." for each tag the Runner has.
    '''

    def setUp(self):
        '''
        setup test environment for information_overload_06027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_information_overload_06027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_iq_06041(unittest.TestCase):
    '''
    testing play functionality of iq
    Cost: 0
    Text: The rez cost of IQ is increased by 1 for each card in HQ. IQ has +1 strength for each card in HQ. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for iq_06041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_iq_06041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kitsune_06043(unittest.TestCase):
    '''
    testing play functionality of kitsune
    Cost: 2
    Text: Subroutine You may choose 1 card in HQ. If you do, the Runner breaches HQ. During this breach, the Runner cannot access cards in the root of HQ, and the first card they access must be the chosen card. When the breach ends, trash this ice.
    '''

    def setUp(self):
        '''
        setup test environment for kitsune_06043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_kitsune_06043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wendigo_06047(unittest.TestCase):
    '''
    testing play functionality of wendigo
    Cost: 2
    Text: Wendigo can be advanced. While Wendigo has an odd number of advancement tokens on it, it gains barrier and loses code gate. Subroutine Choose a program. The Runner cannot use the chosen program for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for wendigo_06047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wendigo_06047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lancelot_06051(unittest.TestCase):
    '''
    testing play functionality of lancelot
    Cost: 4
    Text: When the Runner encounters Lancelot, you may reveal up to 2 grail ice from HQ. For the remainder of this run, Lancelot gains the subroutines of the revealed ice in the order of your choice. Subroutine Trash 1 program.
    '''

    def setUp(self):
        '''
        setup test environment for lancelot_06051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_lancelot_06051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_architect_06061(unittest.TestCase):
    '''
    testing play functionality of architect
    Cost: 4
    Text: Players cannot trash this ice. Subroutine Look at the top 5 cards of R&D. You may install 1 of those cards, ignoring the install cost. Subroutine You may install 1 card from Archives or HQ.
    '''

    def setUp(self):
        '''
        setup test environment for architect_06061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_architect_06061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ashigaru_06064(unittest.TestCase):
    '''
    testing play functionality of ashigaru
    Cost: 9
    Text: Ashigaru gains "Subroutine End the run." for each card in HQ.
    '''

    def setUp(self):
        '''
        setup test environment for ashigaru_06064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ashigaru_06064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mamba_06065(unittest.TestCase):
    '''
    testing play functionality of mamba
    Cost: 6
    Text: Hosted power counter: Do 1 net damage. Use this ability only during a run. Subroutine Do 1 net damage. Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, place 1 power counter on Mamba.
    '''

    def setUp(self):
        '''
        setup test environment for mamba_06065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_mamba_06065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_universal_connectivity_fee_06067(unittest.TestCase):
    '''
    testing play functionality of universal_connectivity_fee
    Cost: 2
    Text: Subroutine If the Runner is not tagged, they lose 1 credit. If the Runner is tagged, they lose all credits in their credit pool and you trash this ice.
    '''

    def setUp(self):
        '''
        setup test environment for universal_connectivity_fee_06067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_universal_connectivity_fee_06067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_changeling_06069(unittest.TestCase):
    '''
    testing play functionality of changeling
    Cost: 5
    Text: Changeling can be advanced. While Changeling has an odd number of advancement tokens on it, it gains sentry and loses barrier. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for changeling_06069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_changeling_06069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sagittarius_06082(unittest.TestCase):
    '''
    testing play functionality of sagittarius
    Cost: 5
    Text: Subroutine Trace[2]. If successful, trash 1 program. If your trace strength is 5 or greater, trash 1 program.
    '''

    def setUp(self):
        '''
        setup test environment for sagittarius_06082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sagittarius_06082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gemini_06084(unittest.TestCase):
    '''
    testing play functionality of gemini
    Cost: 3
    Text: Subroutine Trace[2]. If successful, do 1 net damage. If your trace strength is 5 or greater, do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for gemini_06084
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_gemini_06084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lycan_06089(unittest.TestCase):
    '''
    testing play functionality of lycan
    Cost: 6
    Text: Lycan can be advanced. While Lycan has an odd number of advancement tokens on it, it gains code gate and loses sentry. Subroutine Trash 1 program.
    '''

    def setUp(self):
        '''
        setup test environment for lycan_06089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_lycan_06089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_merlin_06091(unittest.TestCase):
    '''
    testing play functionality of merlin
    Cost: 6
    Text: When the Runner encounters Merlin, you may reveal up to 2 grail ice from HQ. For the remainder of this run, Merlin gains the subroutines of the revealed ice in the order of your choice. Subroutine Do 2 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for merlin_06091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_merlin_06091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_errand_boy_06102(unittest.TestCase):
    '''
    testing play functionality of errand_boy
    Cost: 4
    Text: Subroutine The Corp gains 1 credit or draws 1 card. Subroutine The Corp gains 1 credit or draws 1 card. Subroutine The Corp gains 1 credit or draws 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for errand_boy_06102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_errand_boy_06102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_markus_10_06104(unittest.TestCase):
    '''
    testing play functionality of markus_10
    Cost: 4
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner trashes 1 of their installed cards. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for markus_10_06104
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_markus_10_06104()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_troll_06108(unittest.TestCase):
    '''
    testing play functionality of troll
    Cost: 1
    Text: When the Runner encounters Troll, Trace[2]. If successful, the Runner must lose click or end the run.
    '''

    def setUp(self):
        '''
        setup test environment for troll_06108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_troll_06108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_virgo_06109(unittest.TestCase):
    '''
    testing play functionality of virgo
    Cost: 4
    Text: Subroutine Trace[2]. If successful, give the Runner 1 tag. If your trace strength is 5 or greater, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for virgo_06109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_virgo_06109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_excalibur_06111(unittest.TestCase):
    '''
    testing play functionality of excalibur
    Cost: 2
    Text: Subroutine The Runner cannot make another run this turn.
    '''

    def setUp(self):
        '''
        setup test environment for excalibur_06111
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_excalibur_06111()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_asteroid_belt_07012(unittest.TestCase):
    '''
    testing play functionality of asteroid_belt
    Cost: 9
    Text: Asteroid Belt can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for asteroid_belt_07012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_asteroid_belt_07012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wormhole_07013(unittest.TestCase):
    '''
    testing play functionality of wormhole
    Cost: 9
    Text: Wormhole can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine Resolve a subroutine on another piece of rezzed ice.
    '''

    def setUp(self):
        '''
        setup test environment for wormhole_07013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wormhole_07013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nebula_07014(unittest.TestCase):
    '''
    testing play functionality of nebula
    Cost: 9
    Text: Nebula can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine Trash 1 program.
    '''

    def setUp(self):
        '''
        setup test environment for nebula_07014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_nebula_07014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_orion_07015(unittest.TestCase):
    '''
    testing play functionality of orion
    Cost: 15
    Text: Orion can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine Trash 1 program. Subroutine Resolve a subroutine on another piece of rezzed ice. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for orion_07015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_orion_07015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_builder_07016(unittest.TestCase):
    '''
    testing play functionality of builder
    Cost: 2
    Text: click: Move this piece of ice to the outermost position protecting any server. Subroutine Place 1 advancement token on a piece of ice protecting this server that can be advanced. Subroutine Place 1 advancement token on a piece of ice protecting this server that can be advanced.
    '''

    def setUp(self):
        '''
        setup test environment for builder_07016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_builder_07016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_checkpoint_07017(unittest.TestCase):
    '''
    testing play functionality of checkpoint
    Cost: 4
    Text: When you rez Checkpoint, take 1 bad publicity. Subroutine Trace[5]. If successful, do 3 meat damage when this run is successful.
    '''

    def setUp(self):
        '''
        setup test environment for checkpoint_07017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_checkpoint_07017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fire_wall_07018(unittest.TestCase):
    '''
    testing play functionality of fire_wall
    Cost: 5
    Text: Fire Wall can be advanced and gains +1 strength for each advancement token on it. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for fire_wall_07018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_fire_wall_07018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_searchlight_07019(unittest.TestCase):
    '''
    testing play functionality of searchlight
    Cost: 1
    Text: Searchlight can be advanced. X is the number of advancement tokens on Searchlight. Subroutine Trace[X]. If successful, give the Runner 1 tag. Subroutine Trace[X]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for searchlight_07019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_searchlight_07019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_next_gold_08011(unittest.TestCase):
    '''
    testing play functionality of next_gold
    Cost: 8
    Text: X is the number of rezzed NEXT ice. Subroutine Do X net damage. Subroutine Trash X programs.
    '''

    def setUp(self):
        '''
        setup test environment for next_gold_08011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_next_gold_08011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cortex_lock_08014(unittest.TestCase):
    '''
    testing play functionality of cortex_lock
    Cost: 2
    Text: Subroutine Do 1 net damage for each unused MU the Runner has.
    '''

    def setUp(self):
        '''
        setup test environment for cortex_lock_08014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_cortex_lock_08014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bandwidth_08016(unittest.TestCase):
    '''
    testing play functionality of bandwidth
    Cost: 0
    Text: Subroutine Give the Runner 1 tag. If this run is successful, the Runner removes 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for bandwidth_08016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bandwidth_08016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_negotiator_08019(unittest.TestCase):
    '''
    testing play functionality of negotiator
    Cost: 4
    Text: 2 credits: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Gain 2 credits. Subroutine Trash 1 installed program.
    '''

    def setUp(self):
        '''
        setup test environment for negotiator_08019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_negotiator_08019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_turing_08033(unittest.TestCase):
    '''
    testing play functionality of turing
    Cost: 4
    Text: Turing has +3 strength while protecting a remote server. The Runner cannot use AI programs to break subroutines on Turing. Subroutine End the run unless the Runner spends click click click.
    '''

    def setUp(self):
        '''
        setup test environment for turing_08033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_turing_08033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crick_08034(unittest.TestCase):
    '''
    testing play functionality of crick
    Cost: 1
    Text: Crick has +3 strength while protecting Archives. Subroutine Install a card from Archives (paying its install cost).
    '''

    def setUp(self):
        '''
        setup test environment for crick_08034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_crick_08034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gutenberg_08037(unittest.TestCase):
    '''
    testing play functionality of gutenberg
    Cost: 2
    Text: Gutenberg has +3 strength while protecting R&D. Subroutine Trace[7]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for gutenberg_08037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_gutenberg_08037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_meru_mati_08039(unittest.TestCase):
    '''
    testing play functionality of meru_mati
    Cost: 2
    Text: Meru Mati has +3 strength while protecting HQ. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for meru_mati_08039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_meru_mati_08039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lab_dog_08052(unittest.TestCase):
    '''
    testing play functionality of lab_dog
    Cost: 2
    Text: Subroutine The Runner trashes an installed piece of hardware. Trash Lab Dog.
    '''

    def setUp(self):
        '''
        setup test environment for lab_dog_08052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_lab_dog_08052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_clairvoyant_monitor_08055(unittest.TestCase):
    '''
    testing play functionality of clairvoyant_monitor
    Cost: 4
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, place 1 advancement token on an installed card and end the run.
    '''

    def setUp(self):
        '''
        setup test environment for clairvoyant_monitor_08055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_clairvoyant_monitor_08055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lockdown_08056(unittest.TestCase):
    '''
    testing play functionality of lockdown
    Cost: 0
    Text: Subroutine The Runner cannot draw cards for the remainder of this turn.
    '''

    def setUp(self):
        '''
        setup test environment for lockdown_08056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_lockdown_08056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_little_engine_08057(unittest.TestCase):
    '''
    testing play functionality of little_engine
    Cost: 5
    Text: Subroutine End the run. Subroutine End the run. Subroutine The Runner gains 5 credits.
    '''

    def setUp(self):
        '''
        setup test environment for little_engine_08057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_little_engine_08057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_quicksand_08060(unittest.TestCase):
    '''
    testing play functionality of quicksand
    Cost: 3
    Text: When the Runner encounters Quicksand, place 1 power counter on Quicksand. Quicksand has +1 strength for each power counter on it. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for quicksand_08060
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_quicksand_08060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pachinko_08076(unittest.TestCase):
    '''
    testing play functionality of pachinko
    Cost: 1
    Text: Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged.
    '''

    def setUp(self):
        '''
        setup test environment for pachinko_08076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_pachinko_08076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spiderweb_08079(unittest.TestCase):
    '''
    testing play functionality of spiderweb
    Cost: 4
    Text: Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for spiderweb_08079
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_spiderweb_08079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_enforcer_10_08089(unittest.TestCase):
    '''
    testing play functionality of enforcer_10
    Cost: 1
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Do 1 core damage. Subroutine Trash 1 installed console. Subroutine Trash all installed virtual resources.
    '''

    def setUp(self):
        '''
        setup test environment for enforcer_10_08089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_enforcer_10_08089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_its_a_trap_08090(unittest.TestCase):
    '''
    testing play functionality of its_a_trap
    Cost: 2
    Text: Whenever this ice is exposed, do 2 net damage. Subroutine The Runner trashes 1 of their installed cards. Trash this ice.
    '''

    def setUp(self):
        '''
        setup test environment for its_a_trap_08090
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_its_a_trap_08090()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tour_guide_08118(unittest.TestCase):
    '''
    testing play functionality of tour_guide
    Cost: 2
    Text: Tour Guide gains "Subroutine End the run." for each rezzed asset you have.
    '''

    def setUp(self):
        '''
        setup test environment for tour_guide_08118
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tour_guide_08118()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_archangel_09013(unittest.TestCase):
    '''
    testing play functionality of archangel
    Cost: 4
    Text: While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, you may pay 3 credits. If you do, they encounter it. Subroutine Trace[6]. If successful, add 1 installed Runner card to the grip.
    '''

    def setUp(self):
        '''
        setup test environment for archangel_09013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_archangel_09013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_news_hound_09014(unittest.TestCase):
    '''
    testing play functionality of news_hound
    Cost: 2
    Text: If a current is active, News Hound gains "Subroutine End the run." after all its other subroutines. Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for news_hound_09014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_news_hound_09014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_resistor_09015(unittest.TestCase):
    '''
    testing play functionality of resistor
    Cost: 0
    Text: Resistor has +1 strength for each tag the Runner has. Subroutine Trace[4]. If successful, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for resistor_09015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_resistor_09015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_special_offer_09016(unittest.TestCase):
    '''
    testing play functionality of special_offer
    Cost: 1
    Text: Subroutine The Corp gains 5 credits. Trash Special Offer.
    '''

    def setUp(self):
        '''
        setup test environment for special_offer_09016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_special_offer_09016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tldr_09017(unittest.TestCase):
    '''
    testing play functionality of tldr
    Cost: 1
    Text: Subroutine When the Runner encounters the next piece of ice during this run, that ice gains a second copy of each subroutine on it (after the original subroutine) for the remainder of the encounter.
    '''

    def setUp(self):
        '''
        setup test environment for tldr_09017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tldr_09017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_turnpike_09018(unittest.TestCase):
    '''
    testing play functionality of turnpike
    Cost: 2
    Text: When the Runner encounters this ice, they lose 1 credit. Subroutine Trace[5]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for turnpike_09018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_turnpike_09018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_assassin_09028(unittest.TestCase):
    '''
    testing play functionality of assassin
    Cost: 7
    Text: Subroutine Trace[5]. If successful, do 3 net damage. Subroutine Trace[4]. If successful, trash 1 program.
    '''

    def setUp(self):
        '''
        setup test environment for assassin_09028
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_assassin_09028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vikram_10_10012(unittest.TestCase):
    '''
    testing play functionality of vikram_10
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner cannot use programs for the remainder of this run. Subroutine Trace[4]. If successful, do 1 core damage. Subroutine Trace[4]. If successful, do 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for vikram_10_10012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_vikram_10_10012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_interrupt_0_10016(unittest.TestCase):
    '''
    testing play functionality of interrupt_0
    Cost: 2
    Text: Subroutine For the remainder of this run, as an additional cost to use an icebreaker ability to break subroutines, the Runner must pay 1 credit. Subroutine For the remainder of this run, as an additional cost to use an icebreaker ability to break subroutines, the Runner must pay 1 credit
    '''

    def setUp(self):
        '''
        setup test environment for interrupt_0_10016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_interrupt_0_10016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_harvester_10032(unittest.TestCase):
    '''
    testing play functionality of harvester
    Cost: 1
    Text: Subroutine The Runner draws 3 cards and then discards down to their maximum hand size. Subroutine The Runner draws 3 cards and then discards down to their maximum hand size.
    '''

    def setUp(self):
        '''
        setup test environment for harvester_10032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_harvester_10032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bailiff_10056(unittest.TestCase):
    '''
    testing play functionality of bailiff
    Cost: 2
    Text: Whenever the Runner breaks a subroutine on Bailiff, gain 1 credit. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for bailiff_10056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bailiff_10056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_upayoga_10069(unittest.TestCase):
    '''
    testing play functionality of upayoga
    Cost: 3
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, the Runner loses 2 credits. Subroutine Resolve a subroutine on a piece of rezzed psi ice.
    '''

    def setUp(self):
        '''
        setup test environment for upayoga_10069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_upayoga_10069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cobra_10074(unittest.TestCase):
    '''
    testing play functionality of cobra
    Cost: 4
    Text: Subroutine Trash 1 program. Subroutine Do 2 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for cobra_10074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_cobra_10074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_brainstorm_10086(unittest.TestCase):
    '''
    testing play functionality of brainstorm
    Cost: 9
    Text: When the Runner encounters this ice, it gains X "Subroutine Do 1 core damage." subroutines for the remainder of this run. X is equal to the number of cards in the grip.
    '''

    def setUp(self):
        '''
        setup test environment for brainstorm_10086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_brainstorm_10086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ravana_10_10087(unittest.TestCase):
    '''
    testing play functionality of ravana_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Resolve 1 subroutine on another rezzed bioroid ice. Subroutine Resolve 1 subroutine on another rezzed bioroid ice.
    '''

    def setUp(self):
        '''
        setup test environment for ravana_10_10087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ravana_10_10087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chetana_10089(unittest.TestCase):
    '''
    testing play functionality of chetana
    Cost: 4
    Text: Subroutine Each player gains 2 credits. Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, do 1 net damage for each card in the Runner's grip.
    '''

    def setUp(self):
        '''
        setup test environment for chetana_10089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_chetana_10089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_waiver_10091(unittest.TestCase):
    '''
    testing play functionality of waiver
    Cost: 5
    Text: Subroutine Trace[5]. If successful, the Runner reveals the grip. Trash each card revealed this way with a play or install cost of X or less. X is equal to the amount by which your trace strength exceeded the Runner's link strength.
    '''

    def setUp(self):
        '''
        setup test environment for waiver_10091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_waiver_10091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_red_tape_10093(unittest.TestCase):
    '''
    testing play functionality of red_tape
    Cost: 2
    Text: Subroutine All ice has +3 strength for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for red_tape_10093
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_red_tape_10093()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vanilla_10095(unittest.TestCase):
    '''
    testing play functionality of vanilla
    Cost: 0
    Text: Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for vanilla_10095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_vanilla_10095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_magnet_10103(unittest.TestCase):
    '''
    testing play functionality of magnet
    Cost: 3
    Text: When you rez this ice, choose 1 installed program hosted on a piece of ice. Move that program onto this ice. Each hosted program loses all abilities. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for magnet_10103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_magnet_10103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fairchild_10_11010(unittest.TestCase):
    '''
    testing play functionality of fairchild_10
    Cost: 1
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner must pay 1 credit or trash 1 of their installed cards. Subroutine The Runner must pay 1 credit or trash 1 of their installed cards.
    '''

    def setUp(self):
        '''
        setup test environment for fairchild_10_11010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_fairchild_10_11010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sherlock_20_11011(unittest.TestCase):
    '''
    testing play functionality of sherlock_20
    Cost: 7
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Trace[4]. If successful, add 1 installed program to the bottom of the Runner's stack. Subroutine Trace[4]. If successful, add 1 installed program to the bottom of the Runner's stack. Subroutine Give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for sherlock_20_11011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sherlock_20_11011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chrysalis_11013(unittest.TestCase):
    '''
    testing play functionality of chrysalis
    Cost: 3
    Text: While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, they encounter it. Subroutine Do 2 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for chrysalis_11013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_chrysalis_11013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fairchild_20_11031(unittest.TestCase):
    '''
    testing play functionality of fairchild_20
    Cost: 4
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine The Runner must pay 2 credits or trash 1 of their installed cards. Subroutine The Runner must pay 2 credits or trash 1 of their installed cards. Subroutine Do 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for fairchild_20_11031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_fairchild_20_11031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aiki_11032(unittest.TestCase):
    '''
    testing play functionality of aiki
    Cost: 1
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, the Runner draws 2 cards. Subroutine Do 1 net damage. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for aiki_11032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_aiki_11032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fairchild_30_11049(unittest.TestCase):
    '''
    testing play functionality of fairchild_30
    Cost: 6
    Text: Lose click click click: Break up to 3 subroutines on this ice. Only the Runner can use this ability. Subroutine The Runner must pay 3 credits or trash 1 of their installed cards. Subroutine The Runner must pay 3 credits or trash 1 of their installed cards. Subroutine Do 1 core damage or end the run.
    '''

    def setUp(self):
        '''
        setup test environment for fairchild_30_11049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_fairchild_30_11049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dna_tracker_11053(unittest.TestCase):
    '''
    testing play functionality of dna_tracker
    Cost: 8
    Text: Subroutine Do 1 net damage. The Runner loses 2 credits. Subroutine Do 1 net damage. The Runner loses 2 credits. Subroutine Do 1 net damage. The Runner loses 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for dna_tracker_11053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_dna_tracker_11053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_ward_11075(unittest.TestCase):
    '''
    testing play functionality of data_ward
    Cost: 6
    Text: When the Runner encounters this ice, they take 1 tag unless they pay 3 credits. Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged.
    '''

    def setUp(self):
        '''
        setup test environment for data_ward_11075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_data_ward_11075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bulwark_11078(unittest.TestCase):
    '''
    testing play functionality of bulwark
    Cost: 10
    Text: When you rez this ice, take 1 bad publicity. When the Runner encounters this ice, gain 2 credits if there is an installed AI program. Subroutine The Runner trashes 1 installed program. Subroutine Gain 2 credits. End the run. Subroutine Gain 2 credits. End the run.
    '''

    def setUp(self):
        '''
        setup test environment for bulwark_11078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bulwark_11078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fairchild_11089(unittest.TestCase):
    '''
    testing play functionality of fairchild
    Cost: 9
    Text: Subroutine End the run unless the Runner pays 4 credits. Subroutine End the run unless the Runner pays 4 credits. Subroutine End the run unless the Runner trashes 1 of their installed cards. Subroutine End the run unless the Runner suffers 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for fairchild_11089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_fairchild_11089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mind_game_11092(unittest.TestCase):
    '''
    testing play functionality of mind_game
    Cost: 0
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, choose another server. The Runner moves to the outermost position of that server instead of passing this ice. For the remainder of this run, the Runner must add 1 installed Runner card to the bottom of their stack as an additional cost to jack out. The Runner may jack out.
    '''

    def setUp(self):
        '''
        setup test environment for mind_game_11092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_mind_game_11092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ip_block_11094(unittest.TestCase):
    '''
    testing play functionality of ip_block
    Cost: 2
    Text: When the Runner encounters this ice, give them 1 tag if there is an installed AI program. Subroutine Trace[3]. If successful, give the Runner 1 tag. Subroutine End the run if the Runner is tagged.
    '''

    def setUp(self):
        '''
        setup test environment for ip_block_11094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ip_block_11094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_thoth_11095(unittest.TestCase):
    '''
    testing play functionality of thoth
    Cost: 7
    Text: When the Runner encounters this ice, give them 1 tag. Subroutine Trace[4]. If successful, do 1 net damage for each tag the Runner has. Subroutine Trace[4]. If successful, the Runner loses 1 credit for each tag they have.
    '''

    def setUp(self):
        '''
        setup test environment for thoth_11095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_thoth_11095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mausolus_11097(unittest.TestCase):
    '''
    testing play functionality of mausolus
    Cost: 4
    Text: You can advance this ice. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 3 credits. Subroutine Do 1 net damage. If there are 3 or more hosted advancement counters, instead do 3 net damage. Subroutine Give the Runner 1 tag. If there are 3 or more hosted advancement counters, instead give the Runner 1 tag and end the run.
    '''

    def setUp(self):
        '''
        setup test environment for mausolus_11097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_mausolus_11097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sapper_11098(unittest.TestCase):
    '''
    testing play functionality of sapper
    Cost: 3
    Text: While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, they encounter it. Subroutine Trash 1 installed program.
    '''

    def setUp(self):
        '''
        setup test environment for sapper_11098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sapper_11098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chiyashi_11112(unittest.TestCase):
    '''
    testing play functionality of chiyashi
    Cost: 12
    Text: Whenever the Runner breaks a subroutine on Chiyashi while there is an AI installed, trash the top 2 cards of the Runner's stack. Subroutine Do 2 net damage. Subroutine Do 2 net damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for chiyashi_11112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_chiyashi_11112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_herald_11115(unittest.TestCase):
    '''
    testing play functionality of herald
    Cost: 2
    Text: While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, they encounter it. Subroutine Gain 2 credits. Subroutine You may pay up to 2 credits to place that many advancement counters on 1 installed card you can advance.
    '''

    def setUp(self):
        '''
        setup test environment for herald_11115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_herald_11115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_veritas_11116(unittest.TestCase):
    '''
    testing play functionality of veritas
    Cost: 4
    Text: Subroutine The Corp gains 2 credits. Subroutine The Runner loses 2 credits. Subroutine Trace[2]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for veritas_11116
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_veritas_11116()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_macrophage_11119(unittest.TestCase):
    '''
    testing play functionality of macrophage
    Cost: 3
    Text: Subroutine Trace[4]. If successful, purge virus counters. Subroutine Trace[3]. If successful, trash 1 virus. Subroutine Trace[2]. If successful, remove a virus in the heap from the game. Subroutine Trace[1]. If successful, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for macrophage_11119
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_macrophage_11119()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tribunal_11120(unittest.TestCase):
    '''
    testing play functionality of tribunal
    Cost: 7
    Text: Subroutine The Runner trashes 1 of their installed cards. Subroutine The Runner trashes 1 of their installed cards. Subroutine The Runner trashes 1 of their installed cards.
    '''

    def setUp(self):
        '''
        setup test environment for tribunal_11120
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tribunal_11120()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zed_20_12010(unittest.TestCase):
    '''
    testing play functionality of zed_20
    Cost: 6
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed piece of hardware. Subroutine Trash 1 installed piece of hardware. Subroutine If the Runner has lost click to break a subroutine during this run, do 2 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for zed_20_12010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_zed_20_12010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kakugo_12013(unittest.TestCase):
    '''
    testing play functionality of kakugo
    Cost: 4
    Text: When the Runner passes Kakugo, do 1 net damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for kakugo_12013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_kakugo_12013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sync_bre_12015(unittest.TestCase):
    '''
    testing play functionality of sync_bre
    Cost: 4
    Text: Subroutine Trace[4]. If successful, give the Runner 1 tag. Subroutine Trace[2]. If successful, whenever the Runner breaches a server for the remainder of this run, they access 1 fewer card.
    '''

    def setUp(self):
        '''
        setup test environment for sync_bre_12015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sync_bre_12015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_seidr_adaptive_barrier_12029(unittest.TestCase):
    '''
    testing play functionality of seidr_adaptive_barrier
    Cost: 4
    Text: Seidr Adaptive Barrier has +1 strength for each piece of ice protecting this server. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for seidr_adaptive_barrier_12029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_seidr_adaptive_barrier_12029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nerine_20_12030(unittest.TestCase):
    '''
    testing play functionality of nerine_20
    Cost: 6
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. You may draw 1 card. Subroutine Do 1 core damage. You may draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for nerine_20_12030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_nerine_20_12030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bloom_12032(unittest.TestCase):
    '''
    testing play functionality of bloom
    Cost: 2
    Text: Subroutine You may install 1 piece of ice from HQ protecting another server, ignoring all costs. Subroutine You may install 1 piece of ice from HQ directly inward from this ice, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for bloom_12032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bloom_12032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_free_lunch_12035(unittest.TestCase):
    '''
    testing play functionality of free_lunch
    Cost: 3
    Text: Hosted power counter: The Runner loses 1 credit. Subroutine Place 1 power counter on Free Lunch. Subroutine Place 1 power counter on Free Lunch.
    '''

    def setUp(self):
        '''
        setup test environment for free_lunch_12035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_free_lunch_12035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_watchtower_12038(unittest.TestCase):
    '''
    testing play functionality of watchtower
    Cost: 4
    Text: Subroutine Search R&D for a card and add it to HQ. Shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for watchtower_12038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_watchtower_12038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_selfadapting_code_wall_12040(unittest.TestCase):
    '''
    testing play functionality of selfadapting_code_wall
    Cost: 3
    Text: The strength of Self-Adapting Code Wall cannot be lowered. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for selfadapting_code_wall_12040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_selfadapting_code_wall_12040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_next_opal_12050(unittest.TestCase):
    '''
    testing play functionality of next_opal
    Cost: 4
    Text: This ice gains "Subroutine You may install 1 card from HQ." for each rezzed piece of NEXT ice.
    '''

    def setUp(self):
        '''
        setup test environment for next_opal_12050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_next_opal_12050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_authenticator_12055(unittest.TestCase):
    '''
    testing play functionality of authenticator
    Cost: 2
    Text: When the Runner encounters this ice, they may take 1 tag to bypass it. Subroutine The Corp gains 2 credits. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for authenticator_12055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_authenticator_12055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_battlement_12057(unittest.TestCase):
    '''
    testing play functionality of battlement
    Cost: 3
    Text: Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for battlement_12057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_battlement_12057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_owl_12060(unittest.TestCase):
    '''
    testing play functionality of owl
    Cost: 2
    Text: Subroutine Add 1 installed program to the top of the stack.
    '''

    def setUp(self):
        '''
        setup test environment for owl_12060
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_owl_12060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_loki_12069(unittest.TestCase):
    '''
    testing play functionality of loki
    Cost: 6
    Text: When the Runner encounters this ice, choose another rezzed piece of ice. For the remainder of this run, this ice gains the subtypes of the chosen ice and gains the subroutines of that ice in order before all its other subroutines. Subroutine The Runner must either end the run or shuffle all cards from the grip into the stack.
    '''

    def setUp(self):
        '''
        setup test environment for loki_12069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_loki_12069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_miraju_12071(unittest.TestCase):
    '''
    testing play functionality of miraju
    Cost: 2
    Text: Whenever an encounter with this ice ends, if the Runner broke its printed subroutine, the Runner moves to the outermost position of Archives instead of passing this ice. They may jack out. Derez this ice. Subroutine You may draw 1 card. Then, shuffle 1 card from HQ into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for miraju_12071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_miraju_12071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_metamorph_12094(unittest.TestCase):
    '''
    testing play functionality of metamorph
    Cost: 3
    Text: Subroutine Swap 2 other installed pieces of ice or 2 of your installed non-ice cards.
    '''

    def setUp(self):
        '''
        setup test environment for metamorph_12094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_metamorph_12094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_loop_12095(unittest.TestCase):
    '''
    testing play functionality of data_loop
    Cost: 7
    Text: When the Runner encounters this ice, they add 2 cards from the grip to the top of the stack. Subroutine End the run if the Runner is tagged. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for data_loop_12095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_data_loop_12095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tithonium_12098(unittest.TestCase):
    '''
    testing play functionality of tithonium
    Cost: 9
    Text: You may forfeit an agenda to rez Tithonium instead of paying its rez cost. Tithonium cannot host cards. Subroutine Trash 1 program. Subroutine Trash 1 program. Subroutine Trash 1 resource and end the run.
    '''

    def setUp(self):
        '''
        setup test environment for tithonium_12098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tithonium_12098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sand_storm_12114(unittest.TestCase):
    '''
    testing play functionality of sand_storm
    Cost: 2
    Text: Subroutine If this ice is installed, move it to the outermost position protecting another server. (The run continues from this new position.) Trash this ice.
    '''

    def setUp(self):
        '''
        setup test environment for sand_storm_12114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sand_storm_12114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_conundrum_12120(unittest.TestCase):
    '''
    testing play functionality of conundrum
    Cost: 8
    Text: Conundrum has +3 strength if there is an installed AI. Subroutine The Runner trashes an installed program. Subroutine The Runner loses click, if able. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for conundrum_12120
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_conundrum_12120()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_eli_20_13034(unittest.TestCase):
    '''
    testing play functionality of eli_20
    Cost: 5
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine You may draw 1 card. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for eli_20_13034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_eli_20_13034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_executive_functioning_13035(unittest.TestCase):
    '''
    testing play functionality of executive_functioning
    Cost: 2
    Text: Subroutine Trace[4]. If successful, do 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for executive_functioning_13035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_executive_functioning_13035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_holmegaard_13036(unittest.TestCase):
    '''
    testing play functionality of holmegaard
    Cost: 7
    Text: Subroutine Trace[4]. If successful, the Runner cannot access cards or breach the attacked server for the remainder of this run. Subroutine Trash 1 installed icebreaker.
    '''

    def setUp(self):
        '''
        setup test environment for holmegaard_13036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_holmegaard_13036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tapestry_13037(unittest.TestCase):
    '''
    testing play functionality of tapestry
    Cost: 5
    Text: Subroutine The Runner loses click, if able. Subroutine The Corp may draw 1 card. Subroutine The Corp may add 1 card from HQ to the top of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for tapestry_13037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tapestry_13037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bloodletter_13047(unittest.TestCase):
    '''
    testing play functionality of bloodletter
    Cost: 3
    Text: Subroutine The Runner must trash either 1 installed program or the top 2 cards of the stack.
    '''

    def setUp(self):
        '''
        setup test environment for bloodletter_13047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bloodletter_13047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_colossus_13048(unittest.TestCase):
    '''
    testing play functionality of colossus
    Cost: 6
    Text: You can advance this ice. It has +1 strength for each hosted advancement token. Subroutine Give the Runner 1 tag. If there are 3 or more hosted advancement tokens, instead give the Runner 2 tags. Subroutine Trash 1 installed program. If there are 3 or more hosted advancement tokens, instead trash 1 installed program and 1 installed resource.
    '''

    def setUp(self):
        '''
        setup test environment for colossus_13048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_colossus_13048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hailstorm_13049(unittest.TestCase):
    '''
    testing play functionality of hailstorm
    Cost: 6
    Text: Subroutine Remove a card in the heap from the game. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hailstorm_13049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hailstorm_13049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hortum_13050(unittest.TestCase):
    '''
    testing play functionality of hortum
    Cost: 4
    Text: You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using AI programs. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 4 credits. Subroutine End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.
    '''

    def setUp(self):
        '''
        setup test environment for hortum_13050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hortum_13050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_weir_13056(unittest.TestCase):
    '''
    testing play functionality of weir
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine The Runner trashes 1 card from their grip.
    '''

    def setUp(self):
        '''
        setup test environment for weir_13056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_weir_13056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_machicolation_a_14010(unittest.TestCase):
    '''
    testing play functionality of machicolation_a
    Cost: 6
    Text: Subroutine Trash 1 program. Subroutine Trash 1 program. Subroutine Trash 1 piece of hardware. Subroutine The Runner loses 3 credits, if able. End the run.
    '''

    def setUp(self):
        '''
        setup test environment for machicolation_a_14010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_machicolation_a_14010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_machicolation_b_14011(unittest.TestCase):
    '''
    testing play functionality of machicolation_b
    Cost: 6
    Text: Subroutine Trash 1 resource. Subroutine Trash 1 resource. Subroutine Do 1 net damage. Subroutine The Runner loses click, if able. End the run.
    '''

    def setUp(self):
        '''
        setup test environment for machicolation_b_14011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_machicolation_b_14011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_heimdall_10_20066(unittest.TestCase):
    '''
    testing play functionality of heimdall_10
    Cost: 8
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for heimdall_10_20066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_heimdall_10_20066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hudson_10_20067(unittest.TestCase):
    '''
    testing play functionality of hudson_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner cannot access more than 1 card during this run. Subroutine The Runner cannot access more than 1 card during this run.
    '''

    def setUp(self):
        '''
        setup test environment for hudson_10_20067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hudson_10_20067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ichi_10_20068(unittest.TestCase):
    '''
    testing play functionality of ichi_10
    Cost: 5
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for ichi_10_20068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ichi_10_20068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rototurret_20069(unittest.TestCase):
    '''
    testing play functionality of rototurret
    Cost: 4
    Text: Subroutine Trash 1 installed program. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for rototurret_20069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_rototurret_20069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_viktor_10_20070(unittest.TestCase):
    '''
    testing play functionality of viktor_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for viktor_10_20070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_viktor_10_20070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_archer_20084(unittest.TestCase):
    '''
    testing play functionality of archer
    Cost: 4
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for archer_20084
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_archer_20084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_caduceus_20085(unittest.TestCase):
    '''
    testing play functionality of caduceus
    Cost: 3
    Text: Subroutine Trace[3]. If successful, the Corp gains 3 credits. Subroutine Trace[2]. If successful, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for caduceus_20085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_caduceus_20085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hadrians_wall_20086(unittest.TestCase):
    '''
    testing play functionality of hadrians_wall
    Cost: 10
    Text: Hadrian's Wall can be advanced and has +1 strength for each advancement token on it. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hadrians_wall_20086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hadrians_wall_20086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hive_20087(unittest.TestCase):
    '''
    testing play functionality of hive
    Cost: 5
    Text: This ice loses 1 of its printed "Subroutine End the run." subroutines for each agenda point in your score area. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hive_20087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hive_20087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ice_wall_20088(unittest.TestCase):
    '''
    testing play functionality of ice_wall
    Cost: 1
    Text: You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for ice_wall_20088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ice_wall_20088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shadow_20089(unittest.TestCase):
    '''
    testing play functionality of shadow
    Cost: 3
    Text: Shadow can be advanced and has +1 strength for each advancement token on it. Subroutine The Corp gains 2 credits. Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for shadow_20089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_shadow_20089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_himitsubako_20099(unittest.TestCase):
    '''
    testing play functionality of himitsubako
    Cost: 2
    Text: 1 credit: Add Himitsu-Bako to HQ. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for himitsubako_20099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_himitsubako_20099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_neural_katana_20100(unittest.TestCase):
    '''
    testing play functionality of neural_katana
    Cost: 4
    Text: Subroutine Do 3 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for neural_katana_20100
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_neural_katana_20100()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_swordsman_20101(unittest.TestCase):
    '''
    testing play functionality of swordsman
    Cost: 3
    Text: The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for swordsman_20101
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_swordsman_20101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wall_of_thorns_20102(unittest.TestCase):
    '''
    testing play functionality of wall_of_thorns
    Cost: 8
    Text: Subroutine Do 2 net damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wall_of_thorns_20102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wall_of_thorns_20102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_whirlpool_20103(unittest.TestCase):
    '''
    testing play functionality of whirlpool
    Cost: 0
    Text: Subroutine The Runner cannot jack out for the remainder of this run. Trash Whirlpool.
    '''

    def setUp(self):
        '''
        setup test environment for whirlpool_20103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_whirlpool_20103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_yagura_20104(unittest.TestCase):
    '''
    testing play functionality of yagura
    Cost: 1
    Text: Subroutine Look at the top card of R&D. You may add that card to the bottom of R&D. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for yagura_20104
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_yagura_20104()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_raven_20113(unittest.TestCase):
    '''
    testing play functionality of data_raven
    Cost: 4
    Text: When the Runner encounters this ice, they must take 1 tag or end the run. Hosted power counter: Give the Runner 1 tag. Subroutine Trace[3]. If successful, place 1 power counter on this ice.
    '''

    def setUp(self):
        '''
        setup test environment for data_raven_20113
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_data_raven_20113()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_flare_20114(unittest.TestCase):
    '''
    testing play functionality of flare
    Cost: 9
    Text: Subroutine Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.
    '''

    def setUp(self):
        '''
        setup test environment for flare_20114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_flare_20114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_popup_window_20115(unittest.TestCase):
    '''
    testing play functionality of popup_window
    Cost: 0
    Text: When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for popup_window_20115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_popup_window_20115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tollbooth_20116(unittest.TestCase):
    '''
    testing play functionality of tollbooth
    Cost: 8
    Text: When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for tollbooth_20116
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tollbooth_20116()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wraparound_20117(unittest.TestCase):
    '''
    testing play functionality of wraparound
    Cost: 2
    Text: While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wraparound_20117
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wraparound_20117()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_enigma_20129(unittest.TestCase):
    '''
    testing play functionality of enigma
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for enigma_20129
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_enigma_20129()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hunter_20130(unittest.TestCase):
    '''
    testing play functionality of hunter
    Cost: 1
    Text: Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for hunter_20130
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hunter_20130()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wall_of_static_20131(unittest.TestCase):
    '''
    testing play functionality of wall_of_static
    Cost: 3
    Text: Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wall_of_static_20131
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wall_of_static_20131()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_najja_10_21011(unittest.TestCase):
    '''
    testing play functionality of najja_10
    Cost: 2
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for najja_10_21011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_najja_10_21011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mganga_21013(unittest.TestCase):
    '''
    testing play functionality of mganga
    Cost: 1
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit or 2 credits. Reveal spent credits. If you and the Runner spend a different number of credits, do 2 net damage; otherwise do 1 net damage. Trash Mganga.
    '''

    def setUp(self):
        '''
        setup test environment for mganga_21013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_mganga_21013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nightdancer_21030(unittest.TestCase):
    '''
    testing play functionality of nightdancer
    Cost: 6
    Text: Subroutine The Runner loses click, if able. You have an additional click to spend during your next turn. Subroutine The Runner loses click, if able. You have an additional click to spend during your next turn.
    '''

    def setUp(self):
        '''
        setup test environment for nightdancer_21030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_nightdancer_21030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aimor_21032(unittest.TestCase):
    '''
    testing play functionality of aimor
    Cost: 0
    Text: Subroutine Trash the top 3 cards of the stack. Trash Aimor.
    '''

    def setUp(self):
        '''
        setup test environment for aimor_21032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_aimor_21032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_jua_21034(unittest.TestCase):
    '''
    testing play functionality of jua
    Cost: 2
    Text: When the Runner encounters this ice, they cannot install cards for the remainder of the turn. Subroutine Choose 2 installed Runner cards, if able. The Runner must add 1 of the chosen cards to the top of the stack.
    '''

    def setUp(self):
        '''
        setup test environment for jua_21034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_jua_21034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_next_sapphire_21050(unittest.TestCase):
    '''
    testing play functionality of next_sapphire
    Cost: 4
    Text: X is the number of rezzed NEXT ice. Subroutine Draw up to X cards. Subroutine Add up to X cards from Archives to HQ. Subroutine Shuffle up to X cards from HQ into R&D.
    '''

    def setUp(self):
        '''
        setup test environment for next_sapphire_21050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_next_sapphire_21050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_anansi_21051(unittest.TestCase):
    '''
    testing play functionality of anansi
    Cost: 8
    Text: Whenever an encounter with this ice ends, if the Runner did not fully break it, do 3 net damage. Subroutine Look at the top 5 cards of R&D and arrange them in any order. Subroutine You may draw 1 card. The Runner may pay 2 credits to draw 1 card. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for anansi_21051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_anansi_21051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sadaka_21073(unittest.TestCase):
    '''
    testing play functionality of sadaka
    Cost: 2
    Text: Subroutine Look at the top 3 cards of R&D and either arrange them in any order or shuffle R&D. You may draw 1 card. Subroutine You may trash 1 card in HQ. If you do, trash 1 resource. Trash Sadaka.
    '''

    def setUp(self):
        '''
        setup test environment for sadaka_21073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sadaka_21073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_endless_eula_21074(unittest.TestCase):
    '''
    testing play functionality of endless_eula
    Cost: 6
    Text: Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for endless_eula_21074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_endless_eula_21074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sandman_21075(unittest.TestCase):
    '''
    testing play functionality of sandman
    Cost: 5
    Text: Subroutine Add an installed Runner card to the grip. Subroutine Add an installed Runner card to the grip.
    '''

    def setUp(self):
        '''
        setup test environment for sandman_21075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sandman_21075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_oduduwa_21079(unittest.TestCase):
    '''
    testing play functionality of oduduwa
    Cost: 7
    Text: When the Runner encounters Oduduwa, place 1 advancement token on it. You may place X advancement tokens on another piece of ice. X is the number of advancement tokens on Oduduwa. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for oduduwa_21079
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_oduduwa_21079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kamali_10_21092(unittest.TestCase):
    '''
    testing play functionality of kamali_10
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage unless the Runner trashes 1 installed resource. Subroutine Do 1 core damage unless the Runner trashes 1 installed piece of hardware. Subroutine Do 1 core damage unless the Runner trashes 1 installed program.
    '''

    def setUp(self):
        '''
        setup test environment for kamali_10_21092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_kamali_10_21092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_envelope_21095(unittest.TestCase):
    '''
    testing play functionality of envelope
    Cost: 4
    Text: Subroutine Do 1 net damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for envelope_21095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_envelope_21095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_masvingo_21099(unittest.TestCase):
    '''
    testing play functionality of masvingo
    Cost: 3
    Text: Masvingo can be advanced. When you rez Masvingo, place 1 advancement token on it. Masvingo gains "Subroutine End the run." for each advancement token on it.
    '''

    def setUp(self):
        '''
        setup test environment for masvingo_21099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_masvingo_21099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_next_diamond_21112(unittest.TestCase):
    '''
    testing play functionality of next_diamond
    Cost: 10
    Text: This rez cost of this ice is lowered by 1 credit for each other rezzed piece of NEXT ice. Subroutine Do 1 core damage. Subroutine Do 1 core damage. Subroutine Trash 1 installed Runner card.
    '''

    def setUp(self):
        '''
        setup test environment for next_diamond_21112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_next_diamond_21112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mlinzi_21115(unittest.TestCase):
    '''
    testing play functionality of mlinzi
    Cost: 7
    Text: Subroutine Do 1 net damage unless the Runner trashes the top 2 cards of the stack. Subroutine Do 2 net damage unless the Runner trashes the top 3 cards of the stack. Subroutine Do 3 net damage unless the Runner trashes the top 4 cards of the stack.
    '''

    def setUp(self):
        '''
        setup test environment for mlinzi_21115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_mlinzi_21115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_surveyor_21118(unittest.TestCase):
    '''
    testing play functionality of surveyor
    Cost: 5
    Text: X is twice the number of ice protecting this server. Subroutine Trace[X]. If successful, give the Runner 2 tags. Subroutine Trace[X]. If successful, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for surveyor_21118
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_surveyor_21118()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_meridian_22028(unittest.TestCase):
    '''
    testing play functionality of meridian
    Cost: 3
    Text: Subroutine Gain 4 credits and end the run unless the Runner adds this ice to their score area as an agenda worth -1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for meridian_22028
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_meridian_22028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gatekeeper_22029(unittest.TestCase):
    '''
    testing play functionality of gatekeeper
    Cost: 3
    Text: Gatekeeper has +6 strength if you rezzed it this turn. Subroutine Draw up to 3 cards. Reveal up to 3 agendas in HQ and/or Archives, then shuffle those agendas into R&D. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for gatekeeper_22029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_gatekeeper_22029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_otoroshi_22038(unittest.TestCase):
    '''
    testing play functionality of otoroshi
    Cost: 2
    Text: Subroutine You may place up to 3 advancement counters on 1 card installed in the root of a remote server. If you do, the Runner accesses that card unless they pay 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for otoroshi_22038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_otoroshi_22038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_thimblerig_22039(unittest.TestCase):
    '''
    testing play functionality of thimblerig
    Cost: 2
    Text: When your turn begins and whenever the Runner passes this ice, you may swap this ice with another installed piece of ice. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for thimblerig_22039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_thimblerig_22039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_peeping_tom_22045(unittest.TestCase):
    '''
    testing play functionality of peeping_tom
    Cost: 4
    Text: When the Runner encounters this ice, choose a card type, then reveal all cards in the grip. For the remainder of this run, this ice gains "Subroutine End the run unless the Runner takes 1 tag." for each revealed card of the chosen type.
    '''

    def setUp(self):
        '''
        setup test environment for peeping_tom_22045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_peeping_tom_22045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hydra_22046(unittest.TestCase):
    '''
    testing play functionality of hydra
    Cost: 10
    Text: Subroutine Do 3 net damage if the Runner is tagged; otherwise, give the Runner 1 tag. Subroutine Gain 5 credits if the Runner is tagged; otherwise, give the Runner 1 tag. Subroutine End the run if the Runner is tagged; otherwise, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for hydra_22046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hydra_22046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_blockchain_22053(unittest.TestCase):
    '''
    testing play functionality of blockchain
    Cost: 7
    Text: Blockchain gains "Subroutine The Corp gains 1 credit and the Runner loses 1 credit." before all its other subroutines for every 2 faceup transaction operations in Archives. Subroutine The Corp gains 1 credit and the Runner loses 1 credit. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for blockchain_22053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_blockchain_22053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_formicary_22054(unittest.TestCase):
    '''
    testing play functionality of formicary
    Cost: 2
    Text: Whenever the Runner approaches a server, you may rez this ice. If you do, move this ice to the innermost position protecting the approached server. The Runner moves to this ice and encounters it. Subroutine End the run unless the Runner suffers 2 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for formicary_22054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_formicary_22054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_slot_machine_23045(unittest.TestCase):
    '''
    testing play functionality of slot_machine
    Cost: 3
    Text: When the Runner encounters this ice, they put the top card of the stack on the bottom, then you reveal the top 3 cards of the stack. Subroutine The Runner loses 3 credits. Subroutine If you revealed 2 or more cards that share a type when this encounter began, gain 3 credits. Subroutine If you revealed 3 or more cards that share a type when this encounter began, place 3 advancement tokens on an installed card.
    '''

    def setUp(self):
        '''
        setup test environment for slot_machine_23045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_slot_machine_23045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_border_control_23054(unittest.TestCase):
    '''
    testing play functionality of border_control
    Cost: 4
    Text: trash: End the run. Use this ability only during a run on this server. Subroutine Gain 1 credit for each piece of ice protecting this server. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for border_control_23054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_border_control_23054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_eli_10_25073(unittest.TestCase):
    '''
    testing play functionality of eli_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for eli_10_25073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_eli_10_25073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_heimdall_10_25074(unittest.TestCase):
    '''
    testing play functionality of heimdall_10
    Cost: 8
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for heimdall_10_25074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_heimdall_10_25074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ichi_10_25075(unittest.TestCase):
    '''
    testing play functionality of ichi_10
    Cost: 5
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for ichi_10_25075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ichi_10_25075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rototurret_25076(unittest.TestCase):
    '''
    testing play functionality of rototurret
    Cost: 4
    Text: Subroutine Trash 1 installed program. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for rototurret_25076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_rototurret_25076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_turing_25077(unittest.TestCase):
    '''
    testing play functionality of turing
    Cost: 4
    Text: Turing has +3 strength while protecting a remote server. The Runner cannot use AI programs to break subroutines on Turing. Subroutine End the run unless the Runner spends click click click.
    '''

    def setUp(self):
        '''
        setup test environment for turing_25077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_turing_25077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_viktor_10_25078(unittest.TestCase):
    '''
    testing play functionality of viktor_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for viktor_10_25078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_viktor_10_25078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_himitsubako_25093(unittest.TestCase):
    '''
    testing play functionality of himitsubako
    Cost: 2
    Text: 1 credit: Add Himitsu-Bako to HQ. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for himitsubako_25093
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_himitsubako_25093()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lotus_field_25094(unittest.TestCase):
    '''
    testing play functionality of lotus_field
    Cost: 5
    Text: The strength of this ice cannot be lowered. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for lotus_field_25094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_lotus_field_25094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_neural_katana_25095(unittest.TestCase):
    '''
    testing play functionality of neural_katana
    Cost: 4
    Text: Subroutine Do 3 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for neural_katana_25095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_neural_katana_25095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_swordsman_25096(unittest.TestCase):
    '''
    testing play functionality of swordsman
    Cost: 3
    Text: The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for swordsman_25096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_swordsman_25096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tsurugi_25097(unittest.TestCase):
    '''
    testing play functionality of tsurugi
    Cost: 6
    Text: Subroutine End the run unless the Corp pays 1 credit. Subroutine Do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for tsurugi_25097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tsurugi_25097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wall_of_thorns_25098(unittest.TestCase):
    '''
    testing play functionality of wall_of_thorns
    Cost: 8
    Text: Subroutine Do 2 net damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wall_of_thorns_25098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wall_of_thorns_25098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_yagura_25099(unittest.TestCase):
    '''
    testing play functionality of yagura
    Cost: 1
    Text: Subroutine Look at the top card of R&D. You may add that card to the bottom of R&D. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for yagura_25099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_yagura_25099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_raven_25112(unittest.TestCase):
    '''
    testing play functionality of data_raven
    Cost: 4
    Text: When the Runner encounters this ice, they must take 1 tag or end the run. Hosted power counter: Give the Runner 1 tag. Subroutine Trace[3]. If successful, place 1 power counter on this ice.
    '''

    def setUp(self):
        '''
        setup test environment for data_raven_25112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_data_raven_25112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_flare_25113(unittest.TestCase):
    '''
    testing play functionality of flare
    Cost: 9
    Text: Subroutine Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.
    '''

    def setUp(self):
        '''
        setup test environment for flare_25113
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_flare_25113()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_popup_window_25114(unittest.TestCase):
    '''
    testing play functionality of popup_window
    Cost: 0
    Text: When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for popup_window_25114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_popup_window_25114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tollbooth_25115(unittest.TestCase):
    '''
    testing play functionality of tollbooth
    Cost: 8
    Text: When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for tollbooth_25115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tollbooth_25115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wraparound_25116(unittest.TestCase):
    '''
    testing play functionality of wraparound
    Cost: 2
    Text: While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wraparound_25116
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wraparound_25116()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_archer_25130(unittest.TestCase):
    '''
    testing play functionality of archer
    Cost: 4
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for archer_25130
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_archer_25130()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_caduceus_25131(unittest.TestCase):
    '''
    testing play functionality of caduceus
    Cost: 3
    Text: Subroutine Trace[3]. If successful, the Corp gains 3 credits. Subroutine Trace[2]. If successful, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for caduceus_25131
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_caduceus_25131()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hadrians_wall_25132(unittest.TestCase):
    '''
    testing play functionality of hadrians_wall
    Cost: 10
    Text: Hadrian's Wall can be advanced and has +1 strength for each advancement token on it. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hadrians_wall_25132
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hadrians_wall_25132()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hortum_25133(unittest.TestCase):
    '''
    testing play functionality of hortum
    Cost: 4
    Text: You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using AI programs. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 4 credits. Subroutine End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.
    '''

    def setUp(self):
        '''
        setup test environment for hortum_25133
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hortum_25133()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ice_wall_25134(unittest.TestCase):
    '''
    testing play functionality of ice_wall
    Cost: 1
    Text: You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for ice_wall_25134
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ice_wall_25134()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spiderweb_25135(unittest.TestCase):
    '''
    testing play functionality of spiderweb
    Cost: 4
    Text: Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for spiderweb_25135
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_spiderweb_25135()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_enigma_25143(unittest.TestCase):
    '''
    testing play functionality of enigma
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for enigma_25143
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_enigma_25143()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hunter_25144(unittest.TestCase):
    '''
    testing play functionality of hunter
    Cost: 1
    Text: Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for hunter_25144
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hunter_25144()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wall_of_static_25145(unittest.TestCase):
    '''
    testing play functionality of wall_of_static
    Cost: 3
    Text: Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wall_of_static_25145
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wall_of_static_25145()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hagen_26035(unittest.TestCase):
    '''
    testing play functionality of hagen
    Cost: 4
    Text: This ice has -1 strength for each installed icebreaker. Subroutine Trash 1 program that is not a decoder, fracter, or killer. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hagen_26035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hagen_26035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_saisentan_26044(unittest.TestCase):
    '''
    testing play functionality of saisentan
    Cost: 5
    Text: When the Runner encounters this ice, choose a card type. For the remainder of the encounter, whenever you trash a card of that type with net damage from a subroutine on this ice, do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for saisentan_26044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_saisentan_26044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_congratulations_26050(unittest.TestCase):
    '''
    testing play functionality of congratulations
    Cost: 1
    Text: When the Runner passes this ice, gain 1 credit. Subroutine Gain 2 credits. The Runner gains 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for congratulations_26050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_congratulations_26050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_loot_box_26051(unittest.TestCase):
    '''
    testing play functionality of loot_box
    Cost: 0
    Text: Subroutine End the run unless the Runner pays 2 credits. Subroutine Reveal the top 3 cards of the stack. Add 1 of those cards to the grip and gain credits equal to its install or play cost. The Runner shuffles the stack. Trash this ice.
    '''

    def setUp(self):
        '''
        setup test environment for loot_box_26051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_loot_box_26051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_afshar_26058(unittest.TestCase):
    '''
    testing play functionality of afshar
    Cost: 3
    Text: While this ice is protecting HQ, the Runner cannot break more than 1 of its printed subroutines during each encounter. Subroutine The Runner loses 2 credits. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for afshar_26058
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_afshar_26058()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sandstone_26059(unittest.TestCase):
    '''
    testing play functionality of sandstone
    Cost: 3
    Text: When the Runner encounters this ice, place 1 virus counter on it. This ice has -1 strength for each hosted virus counter. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for sandstone_26059
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_sandstone_26059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_trebuchet_26060(unittest.TestCase):
    '''
    testing play functionality of trebuchet
    Cost: 7
    Text: When you rez this ice, take 1 bad publicity. Subroutine Trash 1 installed Runner card. Subroutine Trace[6]. If successful, the Runner cannot steal or trash Corp cards for the remainder of the run.
    '''

    def setUp(self):
        '''
        setup test environment for trebuchet_26060
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_trebuchet_26060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rime_26065(unittest.TestCase):
    '''
    testing play functionality of rime
    Cost: 0
    Text: During runs on this server, you can rez this ice any time you could rez non-ice cards. Each piece of ice protecting this server has +1 strength. Subroutine The Runner loses 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for rime_26065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_rime_26065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_drafter_26101(unittest.TestCase):
    '''
    testing play functionality of drafter
    Cost: 3
    Text: Subroutine You may add 1 card from Archives to HQ. Subroutine You may install 1 card from Archives or HQ, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for drafter_26101
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_drafter_26101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tyr_26102(unittest.TestCase):
    '''
    testing play functionality of tyr
    Cost: 10
    Text: Lose click: Break 1 subroutine on this ice. The Corp gets +1 allotted click for their next turn. Only the Runner can use this ability. Subroutine Do 2 core damage. Subroutine Trash 1 installed Runner card. Gain 3 credits. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for tyr_26102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tyr_26102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_engram_flush_26108(unittest.TestCase):
    '''
    testing play functionality of engram_flush
    Cost: 2
    Text: When the Runner encounters this ice, choose a card type. For the remainder of this encounter, whenever you reveal the grip with a subroutine on this ice, you may trash 1 revealed card of that type. Subroutine Reveal the grip. Subroutine Reveal the grip.
    '''

    def setUp(self):
        '''
        setup test environment for engram_flush_26108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_engram_flush_26108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_konjin_26109(unittest.TestCase):
    '''
    testing play functionality of konjin
    Cost: 3
    Text: When the Runner encounters this ice, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, you may force the Runner to encounter another rezzed piece of ice. (When that encounter ends, if the run has not ended, finish encountering this ice.)
    '''

    def setUp(self):
        '''
        setup test environment for konjin_26109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_konjin_26109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_f2p_26115(unittest.TestCase):
    '''
    testing play functionality of f2p
    Cost: 4
    Text: 2 credits: Break 1 subroutine on this ice. Only the Runner can use this ability, and only if they are not tagged. Subroutine Add 1 installed Runner card to the grip. Subroutine Give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for f2p_26115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_f2p_26115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gold_farmer_26116(unittest.TestCase):
    '''
    testing play functionality of gold_farmer
    Cost: 3
    Text: When the Runner breaks a printed subroutine on this ice, they lose 1 credit. Subroutine End the run unless the Runner pays 3 credits. Subroutine End the run unless the Runner pays 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for gold_farmer_26116
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_gold_farmer_26116()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_akhet_26123(unittest.TestCase):
    '''
    testing play functionality of akhet
    Cost: 3
    Text: You can advance this ice. While there are 3 or more hosted advancement tokens, this ice has +3 strength and the Runner cannot break more than 1 of its printed subroutines during each encounter. Subroutine Gain 1 credit. Place 1 advancement token on an installed card. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for akhet_26123
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_akhet_26123()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_colossus_26124(unittest.TestCase):
    '''
    testing play functionality of colossus
    Cost: 6
    Text: You can advance this ice. It has +1 strength for each hosted advancement token. Subroutine Give the Runner 1 tag. If there are 3 or more hosted advancement tokens, instead give the Runner 2 tags. Subroutine Trash 1 installed program. If there are 3 or more hosted advancement tokens, instead trash 1 installed program and 1 installed resource.
    '''

    def setUp(self):
        '''
        setup test environment for colossus_26124
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_colossus_26124()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_winchester_26125(unittest.TestCase):
    '''
    testing play functionality of winchester
    Cost: 4
    Text: While this ice is protecting HQ, it gains "Subroutine Trace[3]. If successful, end the run." after all its other subroutines. Subroutine Trace[4]. If successful, trash 1 installed program. Subroutine Trace[3]. If successful, trash 1 installed piece of hardware.
    '''

    def setUp(self):
        '''
        setup test environment for winchester_26125
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_winchester_26125()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_slot_machine_28004(unittest.TestCase):
    '''
    testing play functionality of slot_machine
    Cost: 3
    Text: When the Runner encounters this ice, they put the top card of the stack on the bottom, then you reveal the top 3 cards of the stack. Subroutine The Runner loses 3 credits. Subroutine If you revealed 2 or more cards that share a type when this encounter began, gain 3 credits. Subroutine If you revealed 3 or more cards that share a type when this encounter began, place 3 advancement tokens on an installed card.
    '''

    def setUp(self):
        '''
        setup test environment for slot_machine_28004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_slot_machine_28004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_border_control_28005(unittest.TestCase):
    '''
    testing play functionality of border_control
    Cost: 4
    Text: trash: End the run. Use this ability only during a run on this server. Subroutine Gain 1 credit for each piece of ice protecting this server. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for border_control_28005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_border_control_28005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_next_bronze_29009(unittest.TestCase):
    '''
    testing play functionality of next_bronze
    Cost: 2
    Text: NEXT Bronze has +1 strength for each rezzed piece of NEXT ice. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for next_bronze_29009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_next_bronze_29009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_next_silver_29010(unittest.TestCase):
    '''
    testing play functionality of next_silver
    Cost: 3
    Text: NEXT Silver gains "Subroutine End the run." for each rezzed piece of NEXT ice.
    '''

    def setUp(self):
        '''
        setup test environment for next_silver_29010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_next_silver_29010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_excalibur_29017(unittest.TestCase):
    '''
    testing play functionality of excalibur
    Cost: 2
    Text: Subroutine The Runner cannot make another run this turn.
    '''

    def setUp(self):
        '''
        setup test environment for excalibur_29017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_excalibur_29017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ansel_10_30038(unittest.TestCase):
    '''
    testing play functionality of ansel_10
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed Runner card. Subroutine You may install 1 card from HQ or Archives. Subroutine The Runner cannot steal or trash Corp cards for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for ansel_10_30038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ansel_10_30038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bran_10_30039(unittest.TestCase):
    '''
    testing play functionality of bran_10
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine You may install 1 piece of ice from HQ or Archives directly inward from this ice, ignoring all costs. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for bran_10_30039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bran_10_30039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_diviner_30046(unittest.TestCase):
    '''
    testing play functionality of diviner
    Cost: 2
    Text: Subroutine Do 1 net damage. If you trash a card with a printed play or install cost that is an odd number, end the run. (0 is not odd.)
    '''

    def setUp(self):
        '''
        setup test environment for diviner_30046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_diviner_30046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_karuna_30047(unittest.TestCase):
    '''
    testing play functionality of karuna
    Cost: 4
    Text: Subroutine Do 2 net damage. The Runner may jack out. Subroutine Do 2 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for karuna_30047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_karuna_30047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_funhouse_30054(unittest.TestCase):
    '''
    testing play functionality of funhouse
    Cost: 5
    Text: When the Runner encounters this ice, end the run unless the Runner takes 1 tag. Subroutine Give the Runner 1 tag unless they pay 4 credits.
    '''

    def setUp(self):
        '''
        setup test environment for funhouse_30054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_funhouse_30054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ping_30055(unittest.TestCase):
    '''
    testing play functionality of ping
    Cost: 2
    Text: When you rez this ice during a run against this server, give the Runner 1 tag. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for ping_30055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ping_30055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ballista_30062(unittest.TestCase):
    '''
    testing play functionality of ballista
    Cost: 5
    Text: Subroutine Trash 1 installed program or end the run.
    '''

    def setUp(self):
        '''
        setup test environment for ballista_30062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ballista_30062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pharos_30063(unittest.TestCase):
    '''
    testing play functionality of pharos
    Cost: 7
    Text: You can advance this ice. It gets +5 strength while there are 3 or more hosted advancement counters. Subroutine Give the Runner 1 tag. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for pharos_30063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_pharos_30063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_palisade_30072(unittest.TestCase):
    '''
    testing play functionality of palisade
    Cost: 3
    Text: While this ice is protecting a remote server, it gets +2 strength. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for palisade_30072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_palisade_30072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tithe_30073(unittest.TestCase):
    '''
    testing play functionality of tithe
    Cost: 1
    Text: Subroutine Do 1 net damage. Subroutine Gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for tithe_30073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tithe_30073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_whitespace_30074(unittest.TestCase):
    '''
    testing play functionality of whitespace
    Cost: 2
    Text: Subroutine The Runner loses 3 credits. Subroutine If the Runner has 6 credits or less, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for whitespace_30074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_whitespace_30074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_eli_10_31043(unittest.TestCase):
    '''
    testing play functionality of eli_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for eli_10_31043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_eli_10_31043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_magnet_31044(unittest.TestCase):
    '''
    testing play functionality of magnet
    Cost: 3
    Text: When you rez this ice, choose 1 installed program hosted on a piece of ice. Move that program onto this ice. Each hosted program loses all abilities. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for magnet_31044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_magnet_31044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ravana_10_31045(unittest.TestCase):
    '''
    testing play functionality of ravana_10
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Resolve 1 subroutine on another rezzed bioroid ice. Subroutine Resolve 1 subroutine on another rezzed bioroid ice.
    '''

    def setUp(self):
        '''
        setup test environment for ravana_10_31045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ravana_10_31045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rototurret_31046(unittest.TestCase):
    '''
    testing play functionality of rototurret
    Cost: 4
    Text: Subroutine Trash 1 installed program. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for rototurret_31046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_rototurret_31046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lotus_field_31055(unittest.TestCase):
    '''
    testing play functionality of lotus_field
    Cost: 5
    Text: The strength of this ice cannot be lowered. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for lotus_field_31055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_lotus_field_31055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_swordsman_31056(unittest.TestCase):
    '''
    testing play functionality of swordsman
    Cost: 3
    Text: The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for swordsman_31056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_swordsman_31056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_popup_window_31065(unittest.TestCase):
    '''
    testing play functionality of popup_window
    Cost: 0
    Text: When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for popup_window_31065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_popup_window_31065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tollbooth_31066(unittest.TestCase):
    '''
    testing play functionality of tollbooth
    Cost: 8
    Text: When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for tollbooth_31066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_tollbooth_31066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wraparound_31067(unittest.TestCase):
    '''
    testing play functionality of wraparound
    Cost: 2
    Text: While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for wraparound_31067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wraparound_31067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_archer_31075(unittest.TestCase):
    '''
    testing play functionality of archer
    Cost: 4
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for archer_31075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_archer_31075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hortum_31076(unittest.TestCase):
    '''
    testing play functionality of hortum
    Cost: 4
    Text: You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using AI programs. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 4 credits. Subroutine End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.
    '''

    def setUp(self):
        '''
        setup test environment for hortum_31076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hortum_31076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ice_wall_31077(unittest.TestCase):
    '''
    testing play functionality of ice_wall
    Cost: 1
    Text: You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for ice_wall_31077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ice_wall_31077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_enigma_31081(unittest.TestCase):
    '''
    testing play functionality of enigma
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for enigma_31081
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_enigma_31081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hakarl_10_32004(unittest.TestCase):
    '''
    testing play functionality of hakarl_10
    Cost: 5
    Text: When you rez this ice during a run against this server, you may derez another installed card. If you do, the Runner cannot use paid abilities printed on bioroid ice for the remainder of this turn. Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hakarl_10_32004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hakarl_10_32004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_anemone_32005(unittest.TestCase):
    '''
    testing play functionality of anemone
    Cost: 3
    Text: When you rez this ice during a run against this server, you may trash 1 card from HQ to do 2 net damage. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for anemone_32005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_anemone_32005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_echo_33035(unittest.TestCase):
    '''
    testing play functionality of echo
    Cost: 2
    Text: Whenever you rez a piece of harmonic ice, place 1 power counter on this ice. This ice gains "Subroutine End the run." for each hosted power counter.
    '''

    def setUp(self):
        '''
        setup test environment for echo_33035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_echo_33035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hakarl_10_33036(unittest.TestCase):
    '''
    testing play functionality of hakarl_10
    Cost: 5
    Text: When you rez this ice during a run against this server, you may derez another installed card. If you do, the Runner cannot use paid abilities printed on bioroid ice for the remainder of this turn. Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hakarl_10_33036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hakarl_10_33036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wave_33037(unittest.TestCase):
    '''
    testing play functionality of wave
    Cost: 2
    Text: When you rez this ice during a run against this server, you may search R&D for a piece of ice and reveal it. (Shuffle R&D after searching it.) Add that ice to HQ. Subroutine Gain 1 credit for each rezzed piece of harmonic ice.
    '''

    def setUp(self):
        '''
        setup test environment for wave_33037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_wave_33037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_anemone_33043(unittest.TestCase):
    '''
    testing play functionality of anemone
    Cost: 3
    Text: When you rez this ice during a run against this server, you may trash 1 card from HQ to do 2 net damage. Subroutine Do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for anemone_33043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_anemone_33043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bathynomus_33044(unittest.TestCase):
    '''
    testing play functionality of bathynomus
    Cost: 3
    Text: While this ice is protecting Archives, it gets +3 strength. Subroutine Do 3 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for bathynomus_33044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bathynomus_33044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ivik_33045(unittest.TestCase):
    '''
    testing play functionality of ivik
    Cost: 7
    Text: The rez cost of this ice is lowered by 1 credit for each rezzed piece of code gate ice. Subroutine Do 2 net damage. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for ivik_33045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_ivik_33045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mestnichestvo_33053(unittest.TestCase):
    '''
    testing play functionality of mestnichestvo
    Cost: 5
    Text: You can advance this ice. When the Runner encounters this ice, you may remove 1 hosted advancement counter. If you do, the Runner loses 3 credits. Subroutine The Runner loses 3 credits. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for mestnichestvo_33053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_mestnichestvo_33053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vasilisa_33054(unittest.TestCase):
    '''
    testing play functionality of vasilisa
    Cost: 2
    Text: When the Runner encounters this ice, you may pay 1 credit. If you do, place 1 advancement counter on an installed card you can advance. Subroutine Give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for vasilisa_33054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_vasilisa_33054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_envelopment_33060(unittest.TestCase):
    '''
    testing play functionality of envelopment
    Cost: 5
    Text: When you rez this ice, place 4 power counters on it. When your turn begins, remove 1 hosted power counter. This ice gains "Subroutine End the run." before its printed subroutine for each hosted power counter. Subroutine Trash this ice.
    '''

    def setUp(self):
        '''
        setup test environment for envelopment_33060
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_envelopment_33060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_maskirovka_33061(unittest.TestCase):
    '''
    testing play functionality of maskirovka
    Cost: 3
    Text: Subroutine Gain 2 credits. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for maskirovka_33061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_maskirovka_33061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_stavka_33062(unittest.TestCase):
    '''
    testing play functionality of stavka
    Cost: 4
    Text: When you rez this ice, you may trash 1 of your other installed cards. If you do, this ice gets +5 strength for the remainder of the run. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program.
    '''

    def setUp(self):
        '''
        setup test environment for stavka_33062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_stavka_33062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bloop_33098(unittest.TestCase):
    '''
    testing play functionality of bloop
    Cost: 3
    Text: As an additional cost to rez this ice, derez another piece of harmonic ice. Subroutine Do 1 core damage. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program.
    '''

    def setUp(self):
        '''
        setup test environment for bloop_33098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_bloop_33098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pulse_33099(unittest.TestCase):
    '''
    testing play functionality of pulse
    Cost: 3
    Text: When you rez this ice during a run against this server, the Runner loses click. Subroutine The Runner loses 1 credit for each rezzed piece of harmonic ice. Subroutine End the run unless the Runner spends click.
    '''

    def setUp(self):
        '''
        setup test environment for pulse_33099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_pulse_33099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hafrun_33108(unittest.TestCase):
    '''
    testing play functionality of hafrun
    Cost: 2
    Text: When you rez this ice during a run against this server, you may trash 1 card from HQ. If you do, choose 1 installed Runner card. That cards abilities cannot break subroutines for the remainder of that run. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for hafrun_33108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_hafrun_33108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vampyronassa_33109(unittest.TestCase):
    '''
    testing play functionality of vampyronassa
    Cost: 7
    Text: Subroutine The Runner loses 2 credits. Subroutine Gain 2 credits. Subroutine Do 2 net damage. Subroutine You may draw 1 or 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for vampyronassa_33109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_vampyronassa_33109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_klevetnik_33116(unittest.TestCase):
    '''
    testing play functionality of klevetnik
    Cost: 3
    Text: When you rez this ice during a run against this server, you may have the Runner gain 2 credits. If you do, choose 1 installed resource. That resource loses all abilities until your next turn ends. Subroutine End the run.
    '''

    def setUp(self):
        '''
        setup test environment for klevetnik_33116
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_klevetnik_33116()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_unsmiling_tsarevna_33117(unittest.TestCase):
    '''
    testing play functionality of unsmiling_tsarevna
    Cost: 4
    Text: When you rez this ice during a run against this server, you may have the Runner gain 2 credits. If you do, during each encounter with this ice for the remainder of that run, the Runner cannot break more than 1 of its printed subroutines. Subroutine Give the Runner 1 tag. Subroutine Do 2 net damage. Subroutine You may draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for unsmiling_tsarevna_33117
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_unsmiling_tsarevna_33117()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_anvil_33124(unittest.TestCase):
    '''
    testing play functionality of anvil
    Cost: 4
    Text: When the Runner encounters this ice, you may trash 1 of your other installed cards. If you do, the Runner cannot break this ice's printed subroutines for the remainder of this encounter. Subroutine Gain 1 credit. The Runner loses 1 credit. Subroutine The Runner trashes 1 of their installed cards.
    '''

    def setUp(self):
        '''
        setup test environment for anvil_33124
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = ice_anvil_33124()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")
