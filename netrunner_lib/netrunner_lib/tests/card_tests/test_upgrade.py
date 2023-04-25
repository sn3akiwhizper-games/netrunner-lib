
'''
test cases for card classes of type upgrade
'''
import unittest

from netrunner_lib.cards._base_card_classes import Upgrade
from netrunner_lib.cards.upgrade import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
class Test_corporate_troubleshooter_01065(unittest.TestCase):
    '''
    testing play functionality of corporate_troubleshooter
    Cost: 0
    Text: X credits, trash: Choose 1 rezzed piece of ice protecting this server. That ice gets +X strength for the remainder of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_troubleshooter_01065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_corporate_troubleshooter_01065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_experiential_data_01066(unittest.TestCase):
    '''
    testing play functionality of experiential_data
    Cost: 2
    Text: All ice protecting this server has +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for experiential_data_01066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_experiential_data_01066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_akitaro_watanabe_01079(unittest.TestCase):
    '''
    testing play functionality of akitaro_watanabe
    Cost: 1
    Text: The rez cost of ice protecting this server is lowered by 2.
    '''

    def setUp(self):
        '''
        setup test environment for akitaro_watanabe_01079
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_akitaro_watanabe_01079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_red_herrings_01091(unittest.TestCase):
    '''
    testing play functionality of red_herrings
    Cost: 1
    Text: Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must pay 5 credits. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)
    '''

    def setUp(self):
        '''
        setup test environment for red_herrings_01091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_red_herrings_01091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sansan_city_grid_01092(unittest.TestCase):
    '''
    testing play functionality of sansan_city_grid
    Cost: 6
    Text: Each agenda in the root of this server gets -1 advancement requirement. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for sansan_city_grid_01092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_sansan_city_grid_01092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_research_station_01105(unittest.TestCase):
    '''
    testing play functionality of research_station
    Cost: 2
    Text: Install only in the root of HQ. Your maximum hand size is +2.
    '''

    def setUp(self):
        '''
        setup test environment for research_station_01105
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_research_station_01105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ash_2x3zb9cy_02013(unittest.TestCase):
    '''
    testing play functionality of ash_2x3zb9cy
    Cost: 2
    Text: Whenever there is a successful run on this server, Trace[4]. If successful, the Runner cannot access any cards other than Ash 2X3ZB9CY for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for ash_2x3zb9cy_02013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_ash_2x3zb9cy_02013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chilo_city_grid_02036(unittest.TestCase):
    '''
    testing play functionality of chilo_city_grid
    Cost: 3
    Text: Whenever there is a successful trace during a run on this server, give the Runner 1 tag. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for chilo_city_grid_02036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_chilo_city_grid_02036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_amazon_industrial_zone_02038(unittest.TestCase):
    '''
    testing play functionality of amazon_industrial_zone
    Cost: 4
    Text: Whenever you install a piece of ice protecting this server, you may immediately rez it, lowering its rez cost by 3. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for amazon_industrial_zone_02038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_amazon_industrial_zone_02038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hokusai_grid_02095(unittest.TestCase):
    '''
    testing play functionality of hokusai_grid
    Cost: 2
    Text: Whenever the Runner makes a successful run on this server, do 1 net damage. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for hokusai_grid_02095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_hokusai_grid_02095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bernice_mai_02097(unittest.TestCase):
    '''
    testing play functionality of bernice_mai
    Cost: 0
    Text: Whenever there is a successful run on this server, Trace[5]. If successful, give the Runner 1 tag. If unsuccessful, trash Bernice Mai.
    '''

    def setUp(self):
        '''
        setup test environment for bernice_mai_02097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_bernice_mai_02097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_simone_diego_02099(unittest.TestCase):
    '''
    testing play functionality of simone_diego
    Cost: 4
    Text: 2 recurring credits You can spend hosted credits to take the basic action to advance cards in the root of or protecting this server.
    '''

    def setUp(self):
        '''
        setup test environment for simone_diego_02099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_simone_diego_02099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ruhr_valley_02111(unittest.TestCase):
    '''
    testing play functionality of ruhr_valley
    Cost: 6
    Text: As an additional cost to make a run on this server, the Runner must spend click. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for ruhr_valley_02111
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_ruhr_valley_02111()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_midori_02113(unittest.TestCase):
    '''
    testing play functionality of midori
    Cost: 0
    Text: Whenever the Runner approaches a piece of ice protecting this server, you may swap that ice with 1 piece of ice from HQ. (The new ice is installed unrezzed.) If you do, the Runner may jack out. Use this ability only once per run.
    '''

    def setUp(self):
        '''
        setup test environment for midori_02113
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_midori_02113()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_awakening_center_03021(unittest.TestCase):
    '''
    testing play functionality of awakening_center
    Cost: 2
    Text: Awakening Center can host bioroid ice (each piece is installed facedown, ignoring all install costs). Whenever the Runner passes all of the ice protecting this server, you may rez a piece of ice on Awakening Center, lowering the rez cost by 7 credits, to force the Runner to encounter it. Trash that ice after the run is completed.
    '''

    def setUp(self):
        '''
        setup test environment for awakening_center_03021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_awakening_center_03021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tyrs_hand_03022(unittest.TestCase):
    '''
    testing play functionality of tyrs_hand
    Cost: 1
    Text: Interrupt -> When a subroutine would be broken on a piece of bioroid ice protecting this server, you may rez this upgrade. Interrupt -> trash: Prevent 1 subroutine from being broken on a piece of bioroid ice protecting this server.
    '''

    def setUp(self):
        '''
        setup test environment for tyrs_hand_03022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_tyrs_hand_03022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_off_the_grid_04038(unittest.TestCase):
    '''
    testing play functionality of off_the_grid
    Cost: 6
    Text: Install only in a remote server. The Runner cannot initiate a run on this server. Whenever the Runner makes a successful run on HQ, trash Off the Grid.
    '''

    def setUp(self):
        '''
        setup test environment for off_the_grid_04038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_off_the_grid_04038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_panic_button_04072(unittest.TestCase):
    '''
    testing play functionality of panic_button
    Cost: 1
    Text: Install only in the root of HQ. 1 credit: Draw 1 card. Use this ability only during a run on HQ.
    '''

    def setUp(self):
        '''
        setup test environment for panic_button_04072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_panic_button_04072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_strongbox_04091(unittest.TestCase):
    '''
    testing play functionality of strongbox
    Cost: 3
    Text: Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must spend click. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)
    '''

    def setUp(self):
        '''
        setup test environment for strongbox_04091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_strongbox_04091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_caprice_nisei_04114(unittest.TestCase):
    '''
    testing play functionality of caprice_nisei
    Cost: 2
    Text: Whenever the Runner passes all of the ice protecting this server, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for caprice_nisei_04114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_caprice_nisei_04114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_neotokyo_grid_05021(unittest.TestCase):
    '''
    testing play functionality of neotokyo_grid
    Cost: 2
    Text: The first time each turn an advancement counter is placed on a card in the root of this server, gain 1 credit. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for neotokyo_grid_05021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_neotokyo_grid_05021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tori_hanzo_05022(unittest.TestCase):
    '''
    testing play functionality of tori_hanzo
    Cost: 3
    Text: Interrupt -> The first time you would do 1 or more net damage during each run against this server, instead you may pay 2 credits to do 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for tori_hanzo_05022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_tori_hanzo_05022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_midway_station_grid_06007(unittest.TestCase):
    '''
    testing play functionality of midway_station_grid
    Cost: 4
    Text: During runs on this server, the Runner must pay 1 credit as an additional cost to use an icebreaker ability to break subroutines. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for midway_station_grid_06007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_midway_station_grid_06007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_heinlein_grid_06023(unittest.TestCase):
    '''
    testing play functionality of heinlein_grid
    Cost: 3
    Text: Whenever the Runner loses or spends click during a run on this server, they lose all credits in their credit pool. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for heinlein_grid_06023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_heinlein_grid_06023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_willothewisp_06032(unittest.TestCase):
    '''
    testing play functionality of willothewisp
    Cost: 4
    Text: Whenever the Runner makes a successful run on this server, you may trash this upgrade. If you do, choose 1 installed icebreaker that was used to break at least 1 subroutine during this run. The Runner adds that icebreaker to the bottom of the stack.
    '''

    def setUp(self):
        '''
        setup test environment for willothewisp_06032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_willothewisp_06032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_port_anson_grid_06044(unittest.TestCase):
    '''
    testing play functionality of port_anson_grid
    Cost: 2
    Text: As an additional cost to jack out during a run on this server, the Runner must trash 1 installed program. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for port_anson_grid_06044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_port_anson_grid_06044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crisium_grid_06048(unittest.TestCase):
    '''
    testing play functionality of crisium_grid
    Cost: 3
    Text: Runs against this server cannot be declared successful. (This effect does not cause runs to become unsuccessful.) Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for crisium_grid_06048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_crisium_grid_06048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shell_corporation_06092(unittest.TestCase):
    '''
    testing play functionality of shell_corporation
    Cost: 2
    Text: You cannot use Shell Corporation more than once per turn. click: Place 3 credits on Shell Corporation. click: Take all credits from Shell Corporation.
    '''

    def setUp(self):
        '''
        setup test environment for shell_corporation_06092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_shell_corporation_06092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_selfdestruct_06112(unittest.TestCase):
    '''
    testing play functionality of selfdestruct
    Cost: 2
    Text: Remote server only. trash: Trash all cards installed in the root of or protecting this server. Trace[X], where X is equal to the number of cards trashed. If successful, do 3 net damage. Use this ability only during a run on this server.
    '''

    def setUp(self):
        '''
        setup test environment for selfdestruct_06112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_selfdestruct_06112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_satellite_grid_07023(unittest.TestCase):
    '''
    testing play functionality of satellite_grid
    Cost: 1
    Text: Each piece of ice protecting this server is considered to have 1 additional advancement token on it. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for satellite_grid_07023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_satellite_grid_07023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_twins_07024(unittest.TestCase):
    '''
    testing play functionality of the_twins
    Cost: 2
    Text: Whenever the Runner passes a rezzed piece of ice protecting this server, you may reveal and trash another copy of that ice from HQ to force the Runner to encounter the piece of ice just passed again.
    '''

    def setUp(self):
        '''
        setup test environment for the_twins_07024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_the_twins_07024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dedicated_technician_team_07026(unittest.TestCase):
    '''
    testing play functionality of dedicated_technician_team
    Cost: 1
    Text: 2 recurring credits Use these credits to install ice protecting this server.
    '''

    def setUp(self):
        '''
        setup test environment for dedicated_technician_team_07026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_dedicated_technician_team_07026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cyberdex_virus_suite_07027(unittest.TestCase):
    '''
    testing play functionality of cyberdex_virus_suite
    Cost: 3
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, you may purge virus counters. trash: Purge virus counters.
    '''

    def setUp(self):
        '''
        setup test environment for cyberdex_virus_suite_07027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_cyberdex_virus_suite_07027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_valley_grid_08015(unittest.TestCase):
    '''
    testing play functionality of valley_grid
    Cost: 3
    Text: Whenever the Runner fully breaks a piece of ice protecting this server, they get -1 maximum hand size until the beginning of your next turn. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for valley_grid_08015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_valley_grid_08015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_breaker_bay_grid_08040(unittest.TestCase):
    '''
    testing play functionality of breaker_bay_grid
    Cost: 0
    Text: The rez cost of each card in the root of this server is lowered by 5. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for breaker_bay_grid_08040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_breaker_bay_grid_08040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_oaktown_grid_08053(unittest.TestCase):
    '''
    testing play functionality of oaktown_grid
    Cost: 1
    Text: The trash cost of each card in the root of this server is increased by 3. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for oaktown_grid_08053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_oaktown_grid_08053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ryon_knight_08054(unittest.TestCase):
    '''
    testing play functionality of ryon_knight
    Cost: 2
    Text: trash: Do 1 core damage. Use this ability only during a run against this server and only if the Runner has no unspent click.
    '''

    def setUp(self):
        '''
        setup test environment for ryon_knight_08054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_ryon_knight_08054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marcus_batty_08074(unittest.TestCase):
    '''
    testing play functionality of marcus_batty
    Cost: 0
    Text: trash: You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, resolve 1 subroutine on a rezzed piece of ice protecting this server. Use this ability only during a run on this server.
    '''

    def setUp(self):
        '''
        setup test environment for marcus_batty_08074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_marcus_batty_08074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_underway_grid_08080(unittest.TestCase):
    '''
    testing play functionality of underway_grid
    Cost: 0
    Text: Ice protecting this server cannot be bypassed. Cards in the root of and/or protecting this server cannot be exposed. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for underway_grid_08080
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_underway_grid_08080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_old_hollywood_grid_08097(unittest.TestCase):
    '''
    testing play functionality of old_hollywood_grid
    Cost: 5
    Text: Persistent -> The Runner cannot steal agendas from this server or its root. Ignore this ability for any agenda the Runner has a copy of in their score area. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.) Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for old_hollywood_grid_08097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_old_hollywood_grid_08097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_product_placement_08115(unittest.TestCase):
    '''
    testing play functionality of product_placement
    Cost: 0
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for product_placement_08115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_product_placement_08115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_expo_grid_08119(unittest.TestCase):
    '''
    testing play functionality of expo_grid
    Cost: 0
    Text: When your turn begins, gain 1 credit if there is a rezzed asset installed in the root of this server. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for expo_grid_08119
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_expo_grid_08119()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_keegan_lane_09024(unittest.TestCase):
    '''
    testing play functionality of keegan_lane
    Cost: 0
    Text: trash, remove 1 tag: Trash 1 program. Use this ability only during a run on this server.
    '''

    def setUp(self):
        '''
        setup test environment for keegan_lane_09024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_keegan_lane_09024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rutherford_grid_09025(unittest.TestCase):
    '''
    testing play functionality of rutherford_grid
    Cost: 0
    Text: The base trace strength of each trace during a run on this server is increased by 2. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for rutherford_grid_09025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_rutherford_grid_09025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mumbad_city_grid_10014(unittest.TestCase):
    '''
    testing play functionality of mumbad_city_grid
    Cost: 3
    Text: Whenever the Runner passes a piece of ice protecting this server, you may swap that ice with another piece of ice protecting this server. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for mumbad_city_grid_10014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_mumbad_city_grid_10014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_disposable_hq_10034(unittest.TestCase):
    '''
    testing play functionality of disposable_hq
    Cost: 0
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, you may add any number of cards from HQ to the bottom of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for disposable_hq_10034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_disposable_hq_10034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_surat_city_grid_10057(unittest.TestCase):
    '''
    testing play functionality of surat_city_grid
    Cost: 2
    Text: Whenever you rez another card in the root of or protecting this server, you may rez 1 card, paying 2 credits less. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for surat_city_grid_10057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_surat_city_grid_10057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mumbad_virtual_tour_10076(unittest.TestCase):
    '''
    testing play functionality of mumbad_virtual_tour
    Cost: 0
    Text: This upgrade costs 0 influence if you have 7 or more assets in your deck. When the Runner accesses this upgrade while it is installed, they must trash it, if able.
    '''

    def setUp(self):
        '''
        setup test environment for mumbad_virtual_tour_10076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_mumbad_virtual_tour_10076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_navi_mumbai_city_grid_10110(unittest.TestCase):
    '''
    testing play functionality of navi_mumbai_city_grid
    Cost: 2
    Text: During runs on this server, the Runner cannot use paid abilities on their installed cards except for mid-access abilities and abilities on icebreakers. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for navi_mumbai_city_grid_10110
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_navi_mumbai_city_grid_10110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_georgia_emelyov_11014(unittest.TestCase):
    '''
    testing play functionality of georgia_emelyov
    Cost: 1
    Text: Whenever the Runner makes an unsuccessful run on this server, do 1 net damage. 2 credits: Move Georgia Emelyov to another server.
    '''

    def setUp(self):
        '''
        setup test environment for georgia_emelyov_11014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_georgia_emelyov_11014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_prisec_11040(unittest.TestCase):
    '''
    testing play functionality of prisec
    Cost: 0
    Text: If the Runner accesses Prisec while installed, you may pay 2 credits to give the Runner 1 tag and do 1 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for prisec_11040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_prisec_11040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_drone_screen_11076(unittest.TestCase):
    '''
    testing play functionality of drone_screen
    Cost: 1
    Text: If the Runner is tagged, Drone Screen gains "Whenever the Runner initiates a run on this server, Trace[3]. If successful, do 1 meat damage (cannot be prevented)."
    '''

    def setUp(self):
        '''
        setup test environment for drone_screen_11076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_drone_screen_11076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_manta_grid_11091(unittest.TestCase):
    '''
    testing play functionality of manta_grid
    Cost: 1
    Text: If the Runner has fewer than 6 credits or no unspent clicks when a successful run on this server ends, you have 1 additional click to spend your next turn. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for manta_grid_11091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_manta_grid_11091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nihongai_grid_11093(unittest.TestCase):
    '''
    testing play functionality of nihongai_grid
    Cost: 1
    Text: Whenever the Runner makes a successful run on this server, if they do not have at least 2 cards in the grip and 6 credits, you may look at the top 5 cards of R&D and swap 1 of those cards with 1 card in HQ. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for nihongai_grid_11093
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_nihongai_grid_11093()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bryan_stinson_11117(unittest.TestCase):
    '''
    testing play functionality of bryan_stinson
    Cost: 2
    Text: While the Runner has fewer than 6 credits, Bryan Stinson gains "click: Play a transaction operation from Archives, ignoring all costs. Remove that transaction from the game instead of trashing it."
    '''

    def setUp(self):
        '''
        setup test environment for bryan_stinson_11117
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_bryan_stinson_11117()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_defense_construct_12011(unittest.TestCase):
    '''
    testing play functionality of defense_construct
    Cost: 2
    Text: Defense Construct can be advanced. trash: Add 1 facedown card from Archives to HQ for each advancement token on Defense Construct. Use this ability only during a run on Archives.
    '''

    def setUp(self):
        '''
        setup test environment for defense_construct_12011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_defense_construct_12011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_oberth_protocol_12018(unittest.TestCase):
    '''
    testing play functionality of oberth_protocol
    Cost: 2
    Text: As an additional cost to rez this upgrade, forfeit 1 agenda. The first time each turn you advance a card in the root of or protecting this server, place 1 more advancement counter on that card.
    '''

    def setUp(self):
        '''
        setup test environment for oberth_protocol_12018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_oberth_protocol_12018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_khondi_plaza_12019(unittest.TestCase):
    '''
    testing play functionality of khondi_plaza
    Cost: 3
    Text: X recurring credits Use these credits to rez ice protecting this server. X is the number of remote servers.
    '''

    def setUp(self):
        '''
        setup test environment for khondi_plaza_12019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_khondi_plaza_12019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_signal_jamming_12020(unittest.TestCase):
    '''
    testing play functionality of signal_jamming
    Cost: 0
    Text: trash: Cards cannot be installed until the end of the run. Use this ability only during a run on this server.
    '''

    def setUp(self):
        '''
        setup test environment for signal_jamming_12020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_signal_jamming_12020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bamboo_dome_12053(unittest.TestCase):
    '''
    testing play functionality of bamboo_dome
    Cost: 1
    Text: Install only in the root of R&D. click: Reveal the top 3 cards of R&D. Secretly choose 1 to add to HQ. Return the others to the top of R&D, in any order. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for bamboo_dome_12053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_bamboo_dome_12053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ben_musashi_12054(unittest.TestCase):
    '''
    testing play functionality of ben_musashi
    Cost: 1
    Text: Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must suffer 2 net damage. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)
    '''

    def setUp(self):
        '''
        setup test environment for ben_musashi_12054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_ben_musashi_12054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_henry_phillips_12056(unittest.TestCase):
    '''
    testing play functionality of henry_phillips
    Cost: 2
    Text: Whenever the Runner breaks a subroutine during a run on this server, gain 2 credits if they are tagged.
    '''

    def setUp(self):
        '''
        setup test environment for henry_phillips_12056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_henry_phillips_12056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_warroid_tracker_12068(unittest.TestCase):
    '''
    testing play functionality of warroid_tracker
    Cost: 2
    Text: Whenever the Runner trashes at least 1 card from this server, from its root, or protecting it, Trace[4]. If successful, the Runner trashes 2 of their installed cards.
    '''

    def setUp(self):
        '''
        setup test environment for warroid_tracker_12068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_warroid_tracker_12068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_traffic_analyzer_12075(unittest.TestCase):
    '''
    testing play functionality of traffic_analyzer
    Cost: 0
    Text: Whenever you rez a piece of ice protecting this server, Trace[2]. If successful, the Corp gains 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for traffic_analyzer_12075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_traffic_analyzer_12075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_helheim_servers_12091(unittest.TestCase):
    '''
    testing play functionality of helheim_servers
    Cost: 2
    Text: Trash 1 card from HQ: All ice protecting this server has +2 strength until the end of the run. Use this ability only during a run on this server.
    '''

    def setUp(self):
        '''
        setup test environment for helheim_servers_12091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_helheim_servers_12091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fractal_threat_matrix_12119(unittest.TestCase):
    '''
    testing play functionality of fractal_threat_matrix
    Cost: 4
    Text: Each time all the subroutines are broken on a piece of ice protecting this server, trash the top 2 cards of the stack.
    '''

    def setUp(self):
        '''
        setup test environment for fractal_threat_matrix_12119
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_fractal_threat_matrix_12119()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_black_level_clearance_13039(unittest.TestCase):
    '''
    testing play functionality of black_level_clearance
    Cost: 4
    Text: Whenever the Runner makes a successful run on this server, they must either suffer 1 core damage or jack out. If the Runner jacks out this way, gain 5 credits, draw 1 card, and trash this upgrade.
    '''

    def setUp(self):
        '''
        setup test environment for black_level_clearance_13039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_black_level_clearance_13039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mason_bellamy_13040(unittest.TestCase):
    '''
    testing play functionality of mason_bellamy
    Cost: 2
    Text: Whenever an encounter with a piece of ice protecting this server ends, if the Runner broke at least 1 subroutine during that encounter, they lose click.
    '''

    def setUp(self):
        '''
        setup test environment for mason_bellamy_13040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_mason_bellamy_13040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_k_p_lynn_13052(unittest.TestCase):
    '''
    testing play functionality of k_p_lynn
    Cost: 1
    Text: Whenever the Runner passes all of the ice protecting this server, they must take 1 tag or end the run.
    '''

    def setUp(self):
        '''
        setup test environment for k_p_lynn_13052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_k_p_lynn_13052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ash_2x3zb9cy_20075(unittest.TestCase):
    '''
    testing play functionality of ash_2x3zb9cy
    Cost: 2
    Text: Whenever there is a successful run on this server, Trace[4]. If successful, the Runner cannot access any cards other than Ash 2X3ZB9CY for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for ash_2x3zb9cy_20075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_ash_2x3zb9cy_20075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_strongbox_20076(unittest.TestCase):
    '''
    testing play functionality of strongbox
    Cost: 3
    Text: Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must spend click. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)
    '''

    def setUp(self):
        '''
        setup test environment for strongbox_20076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_strongbox_20076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hokusai_grid_20108(unittest.TestCase):
    '''
    testing play functionality of hokusai_grid
    Cost: 2
    Text: Whenever the Runner makes a successful run on this server, do 1 net damage. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for hokusai_grid_20108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_hokusai_grid_20108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_red_herrings_20122(unittest.TestCase):
    '''
    testing play functionality of red_herrings
    Cost: 1
    Text: Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must pay 5 credits. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)
    '''

    def setUp(self):
        '''
        setup test environment for red_herrings_20122
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_red_herrings_20122()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bernice_mai_20123(unittest.TestCase):
    '''
    testing play functionality of bernice_mai
    Cost: 0
    Text: Whenever there is a successful run on this server, Trace[5]. If successful, give the Runner 1 tag. If unsuccessful, trash Bernice Mai.
    '''

    def setUp(self):
        '''
        setup test environment for bernice_mai_20123
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_bernice_mai_20123()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_calibration_testing_21017(unittest.TestCase):
    '''
    testing play functionality of calibration_testing
    Cost: 3
    Text: Remote server only. trash: Place 1 advancement counter on a card installed in the root of this server.
    '''

    def setUp(self):
        '''
        setup test environment for calibration_testing_21017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_calibration_testing_21017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_jinja_city_grid_21031(unittest.TestCase):
    '''
    testing play functionality of jinja_city_grid
    Cost: 1
    Text: Whenever you draw a piece of ice, you may reveal it and install it protecting this server, paying 4 credits less. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for jinja_city_grid_21031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_jinja_city_grid_21031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_forced_connection_21037(unittest.TestCase):
    '''
    testing play functionality of forced_connection
    Cost: 0
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, Trace[3]. If successful, give the Runner 2 tags.
    '''

    def setUp(self):
        '''
        setup test environment for forced_connection_21037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_forced_connection_21037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_code_replicator_21052(unittest.TestCase):
    '''
    testing play functionality of code_replicator
    Cost: 2
    Text: Whenever the Runner passes a rezzed piece of ice protecting this server, you may trash this upgrade. If you do, the Runner must approach that ice again. They may jack out.
    '''

    def setUp(self):
        '''
        setup test environment for code_replicator_21052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_code_replicator_21052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tempus_21071(unittest.TestCase):
    '''
    testing play functionality of tempus
    Cost: 0
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, Trace[3]. If successful, the Runner must lose click click or suffer 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for tempus_21071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_tempus_21071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bio_vault_21072(unittest.TestCase):
    '''
    testing play functionality of bio_vault
    Cost: 0
    Text: Install only in a remote server. Bio Vault can be advanced. trash, 2 hosted advancement tokens: End the run.
    '''

    def setUp(self):
        '''
        setup test environment for bio_vault_21072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_bio_vault_21072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mwanza_city_grid_21096(unittest.TestCase):
    '''
    testing play functionality of mwanza_city_grid
    Cost: 0
    Text: Root of HQ or R&D only. Whenever the Runner breaches this server, they access 3 additional cards. When the breach ends, gain 2 credits for each time the Runner accessed a card during that breach. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for mwanza_city_grid_21096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_mwanza_city_grid_21096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_intake_21098(unittest.TestCase):
    '''
    testing play functionality of intake
    Cost: 0
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, Trace[4]. If successful, add 1 installed program or virtual resource to the grip.
    '''

    def setUp(self):
        '''
        setup test environment for intake_21098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_intake_21098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_overseer_matrix_21100(unittest.TestCase):
    '''
    testing play functionality of overseer_matrix
    Cost: 1
    Text: Persistent -> Whenever the Runner trashes a card from this server or its root, you may pay 1 credit to give the Runner 1 tag. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)
    '''

    def setUp(self):
        '''
        setup test environment for overseer_matrix_21100
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_overseer_matrix_21100()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_giordano_memorial_field_22033(unittest.TestCase):
    '''
    testing play functionality of giordano_memorial_field
    Cost: 3
    Text: Whenever the Runner makes a successful run on this server, end the run unless they pay 2 credits for each agenda in their score area.
    '''

    def setUp(self):
        '''
        setup test environment for giordano_memorial_field_22033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_giordano_memorial_field_22033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_daruma_22041(unittest.TestCase):
    '''
    testing play functionality of daruma
    Cost: 1
    Text: When the Runner approaches this server, you may trash this upgrade. If you do, choose 1 card in the root of another server or 1 agenda, asset, or upgrade in HQ. Swap that card with 1 card in the root of this server. If you swap cards this way, the Runner may jack out.
    '''

    def setUp(self):
        '''
        setup test environment for daruma_22041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_daruma_22041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_arella_salvatore_22049(unittest.TestCase):
    '''
    testing play functionality of arella_salvatore
    Cost: 2
    Text: Whenever an agenda is scored from this server, you may install a card from HQ, ignoring all costs, and place 1 advancement token on it.
    '''

    def setUp(self):
        '''
        setup test environment for arella_salvatore_22049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_arella_salvatore_22049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_embolus_23011(unittest.TestCase):
    '''
    testing play functionality of embolus
    Cost: 2
    Text: When your turn begins, you may pay 1 credit to place 1 power counter on this upgrade. Whenever the Runner makes a successful run, remove 1 power counter from this upgrade. Hosted power counter: End the run. Use this ability only during a run on this server.
    '''

    def setUp(self):
        '''
        setup test environment for embolus_23011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_embolus_23011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hired_help_23101(unittest.TestCase):
    '''
    testing play functionality of hired_help
    Cost: 1
    Text: As an additional cost to run this server, the Runner must trash 1 agenda from their score area. Ignore this ability if the Runner made a successful run on HQ this turn. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for hired_help_23101
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_hired_help_23101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ash_2x3zb9cy_25082(unittest.TestCase):
    '''
    testing play functionality of ash_2x3zb9cy
    Cost: 2
    Text: Whenever there is a successful run on this server, Trace[4]. If successful, the Runner cannot access any cards other than Ash 2X3ZB9CY for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for ash_2x3zb9cy_25082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_ash_2x3zb9cy_25082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mason_bellamy_25083(unittest.TestCase):
    '''
    testing play functionality of mason_bellamy
    Cost: 2
    Text: Whenever an encounter with a piece of ice protecting this server ends, if the Runner broke at least 1 subroutine during that encounter, they lose click.
    '''

    def setUp(self):
        '''
        setup test environment for mason_bellamy_25083
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_mason_bellamy_25083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hokusai_grid_25103(unittest.TestCase):
    '''
    testing play functionality of hokusai_grid
    Cost: 2
    Text: Whenever the Runner makes a successful run on this server, do 1 net damage. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for hokusai_grid_25103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_hokusai_grid_25103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_product_placement_25120(unittest.TestCase):
    '''
    testing play functionality of product_placement
    Cost: 0
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for product_placement_25120
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_product_placement_25120()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_red_herrings_25121(unittest.TestCase):
    '''
    testing play functionality of red_herrings
    Cost: 1
    Text: Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must pay 5 credits. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)
    '''

    def setUp(self):
        '''
        setup test environment for red_herrings_25121
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_red_herrings_25121()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crisium_grid_25139(unittest.TestCase):
    '''
    testing play functionality of crisium_grid
    Cost: 3
    Text: Runs against this server cannot be declared successful. (This effect does not cause runs to become unsuccessful.) Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for crisium_grid_25139
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_crisium_grid_25139()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cold_site_server_26038(unittest.TestCase):
    '''
    testing play functionality of cold_site_server
    Cost: 0
    Text: click: Place 1 power counter on this upgrade. As an additional cost to run this server, the Runner must spend 1click and 1 credit for each hosted power counter. When your turn begins, remove all hosted power counters.
    '''

    def setUp(self):
        '''
        setup test environment for cold_site_server_26038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_cold_site_server_26038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_letheia_nisei_26046(unittest.TestCase):
    '''
    testing play functionality of letheia_nisei
    Cost: 1
    Text: The first time each run the Runner approaches this server, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, you may trash this upgrade. If you do, the Runner moves to the outermost position of this server. The Runner may jack out.
    '''

    def setUp(self):
        '''
        setup test environment for letheia_nisei_26046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_letheia_nisei_26046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_increased_drop_rates_26054(unittest.TestCase):
    '''
    testing play functionality of increased_drop_rates
    Cost: 0
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, remove 1 bad publicity unless they take 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for increased_drop_rates_26054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_increased_drop_rates_26054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reduced_service_26062(unittest.TestCase):
    '''
    testing play functionality of reduced_service
    Cost: 0
    Text: When you rez this upgrade, you may pay up to 4 credits to place that many power counters on it. As an additional cost to run this server, the Runner must pay 2 credits for each hosted power counter. Whenever the Runner makes a successful run on a central server, remove 1 hosted power counter.
    '''

    def setUp(self):
        '''
        setup test environment for reduced_service_26062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_reduced_service_26062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tranquility_home_grid_26105(unittest.TestCase):
    '''
    testing play functionality of tranquility_home_grid
    Cost: 1
    Text: Remote server only. The first time each turn you install a card in the root of this server, gain 2 credits or draw 1 card. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for tranquility_home_grid_26105
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_tranquility_home_grid_26105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_la_costa_grid_26112(unittest.TestCase):
    '''
    testing play functionality of la_costa_grid
    Cost: 3
    Text: Remote server only. When your turn begins, place 1 advancement counter on a card installed in the root of this server. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for la_costa_grid_26112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_la_costa_grid_26112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ganked_26119(unittest.TestCase):
    '''
    testing play functionality of ganked
    Cost: 0
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, you may trash it to choose a rezzed piece of ice protecting this server. The Runner encounters that ice.
    '''

    def setUp(self):
        '''
        setup test environment for ganked_26119
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_ganked_26119()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cayambe_grid_26127(unittest.TestCase):
    '''
    testing play functionality of cayambe_grid
    Cost: 3
    Text: When your turn begins, place 1 advancement token on a piece of ice protecting this server. Whenever the Runner approaches this server, end the run unless they pay 2 credits for each advanced piece of ice protecting this server. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for cayambe_grid_26127
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_cayambe_grid_26127()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_la_costa_grid_27005(unittest.TestCase):
    '''
    testing play functionality of la_costa_grid
    Cost: 3
    Text: Remote server only. When your turn begins, place 1 advancement counter on a card installed in the root of this server. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for la_costa_grid_27005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_la_costa_grid_27005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cayambe_grid_27007(unittest.TestCase):
    '''
    testing play functionality of cayambe_grid
    Cost: 3
    Text: When your turn begins, place 1 advancement token on a piece of ice protecting this server. Whenever the Runner approaches this server, end the run unless they pay 2 credits for each advanced piece of ice protecting this server. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for cayambe_grid_27007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_cayambe_grid_27007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_embolus_28003(unittest.TestCase):
    '''
    testing play functionality of embolus
    Cost: 2
    Text: When your turn begins, you may pay 1 credit to place 1 power counter on this upgrade. Whenever the Runner makes a successful run, remove 1 power counter from this upgrade. Hosted power counter: End the run. Use this ability only during a run on this server.
    '''

    def setUp(self):
        '''
        setup test environment for embolus_28003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_embolus_28003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sansan_city_grid_29014(unittest.TestCase):
    '''
    testing play functionality of sansan_city_grid
    Cost: 6
    Text: Each agenda in the root of this server gets -1 advancement requirement. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for sansan_city_grid_29014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_sansan_city_grid_29014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_manegarm_skunkworks_30042(unittest.TestCase):
    '''
    testing play functionality of manegarm_skunkworks
    Cost: 2
    Text: Whenever the Runner approaches this server, end the run unless they either spend click click or pay 5 credits.
    '''

    def setUp(self):
        '''
        setup test environment for manegarm_skunkworks_30042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_manegarm_skunkworks_30042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_anoetic_void_30050(unittest.TestCase):
    '''
    testing play functionality of anoetic_void
    Cost: 0
    Text: Whenever the Runner approaches this server, you may pay 2 credits and trash 2 cards from HQ. If you do, end the run.
    '''

    def setUp(self):
        '''
        setup test environment for anoetic_void_30050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_anoetic_void_30050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_amaze_amusements_30058(unittest.TestCase):
    '''
    testing play functionality of amaze_amusements
    Cost: 1
    Text: Persistent -> Whenever a run on this server ends, if the Runner stole any agendas during that run, give the Runner 2 tags. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)
    '''

    def setUp(self):
        '''
        setup test environment for amaze_amusements_30058
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_amaze_amusements_30058()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_malapert_data_vault_30066(unittest.TestCase):
    '''
    testing play functionality of malapert_data_vault
    Cost: 1
    Text: Whenever you score an agenda from this server, you may search R&D for 1 non-agenda card and reveal it. (Shuffle R&D after searching it.) Add that card to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for malapert_data_vault_30066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_malapert_data_vault_30066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_troubleshooter_31049(unittest.TestCase):
    '''
    testing play functionality of corporate_troubleshooter
    Cost: 0
    Text: X credits, trash: Choose 1 rezzed piece of ice protecting this server. That ice gets +X strength for the remainder of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_troubleshooter_31049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_corporate_troubleshooter_31049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hokusai_grid_31059(unittest.TestCase):
    '''
    testing play functionality of hokusai_grid
    Cost: 2
    Text: Whenever the Runner makes a successful run on this server, do 1 net damage. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for hokusai_grid_31059
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_hokusai_grid_31059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sansan_city_grid_31069(unittest.TestCase):
    '''
    testing play functionality of sansan_city_grid
    Cost: 6
    Text: Each agenda in the root of this server gets -1 advancement requirement. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for sansan_city_grid_31069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_sansan_city_grid_31069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crisium_grid_31079(unittest.TestCase):
    '''
    testing play functionality of crisium_grid
    Cost: 3
    Text: Runs against this server cannot be declared successful. (This effect does not cause runs to become unsuccessful.) Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for crisium_grid_31079
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_crisium_grid_31079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vladisibirsk_city_grid_32006(unittest.TestCase):
    '''
    testing play functionality of vladisibirsk_city_grid
    Cost: 3
    Text: You can advance this upgrade. 2 hosted advancement counters: Place 2 advancement counters on another card in the root of this server that you can advance. Use this ability only once per turn. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for vladisibirsk_city_grid_32006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_vladisibirsk_city_grid_32006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mavirus_33047(unittest.TestCase):
    '''
    testing play functionality of mavirus
    Cost: 3
    Text: While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, you may purge virus counters. If this upgrade is rezzed, do 1 net damage. trash: Purge virus counters.
    '''

    def setUp(self):
        '''
        setup test environment for mavirus_33047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_mavirus_33047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vladisibirsk_city_grid_33056(unittest.TestCase):
    '''
    testing play functionality of vladisibirsk_city_grid
    Cost: 3
    Text: You can advance this upgrade. 2 hosted advancement counters: Place 2 advancement counters on another card in the root of this server that you can advance. Use this ability only once per turn. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for vladisibirsk_city_grid_33056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_vladisibirsk_city_grid_33056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_djupstad_grid_33102(unittest.TestCase):
    '''
    testing play functionality of djupstad_grid
    Cost: 4
    Text: Whenever you score an agenda from the root of this server, do 1 core damage. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for djupstad_grid_33102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_djupstad_grid_33102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mr_hendrik_33103(unittest.TestCase):
    '''
    testing play functionality of mr_hendrik
    Cost: 0
    Text: When the Runner accesses this upgrade while it is installed, you may pay 2 credits to do 1 core damage. If the Runner has any click remaining, they may lose all their click to prevent this damage.
    '''

    def setUp(self):
        '''
        setup test environment for mr_hendrik_33103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_mr_hendrik_33103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nanisivik_grid_33111(unittest.TestCase):
    '''
    testing play functionality of nanisivik_grid
    Cost: 2
    Text: Whenever the Runner approaches this server, you may turn 1 facedown piece of ice in Archives faceup. If you do, resolve 1 subroutine on that ice. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for nanisivik_grid_33111
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_nanisivik_grid_33111()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_yakov_erikovich_avdakov_33126(unittest.TestCase):
    '''
    testing play functionality of yakov_erikovich_avdakov
    Cost: 2
    Text: Whenever a player trashes a card (including this upgrade) from the root of this server or protecting it, except during installation, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for yakov_erikovich_avdakov_33126
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_yakov_erikovich_avdakov_33126()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zato_city_grid_33127(unittest.TestCase):
    '''
    testing play functionality of zato_city_grid
    Cost: 3
    Text: Remote server only. Each piece of ice protecting this server gains When the Runner encounters this ice, choose 1 subroutine on it. You may trash this ice to resolve that subroutine.. Limit 1 region per server.
    '''

    def setUp(self):
        '''
        setup test environment for zato_city_grid_33127
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = upgrade_zato_city_grid_33127()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")
