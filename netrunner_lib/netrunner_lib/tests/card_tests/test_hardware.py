
'''
test cases for card classes of type hardware
'''
import unittest

from netrunner_lib.cards._base_card_classes import Hardware
from netrunner_lib.cards.hardware import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
class Test_cyberfeeder_01005(unittest.TestCase):
    '''
    testing play functionality of cyberfeeder
    Cost: 2
    Text: 1 recurring credit Use this credit to pay for using icebreakers or for installing virus programs.
    '''

    def setUp(self):
        '''
        setup test environment for cyberfeeder_01005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_cyberfeeder_01005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_grimoire_01006(unittest.TestCase):
    '''
    testing play functionality of grimoire
    Cost: 3
    Text: +2 mu Whenever you install a virus program, place 1 virus counter on that program. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for grimoire_01006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_grimoire_01006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lemuria_codecracker_01023(unittest.TestCase):
    '''
    testing play functionality of lemuria_codecracker
    Cost: 1
    Text: click, 1 credit: Expose 1 card. Use this ability only if you have made a successful run on HQ this turn.
    '''

    def setUp(self):
        '''
        setup test environment for lemuria_codecracker_01023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_lemuria_codecracker_01023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_desperado_01024(unittest.TestCase):
    '''
    testing play functionality of desperado
    Cost: 3
    Text: +1 mu Gain 1 credit whenever you make a successful run. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for desperado_01024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_desperado_01024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_akamatsu_mem_chip_01038(unittest.TestCase):
    '''
    testing play functionality of akamatsu_mem_chip
    Cost: 1
    Text: +1 mu
    '''

    def setUp(self):
        '''
        setup test environment for akamatsu_mem_chip_01038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_akamatsu_mem_chip_01038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rabbit_hole_01039(unittest.TestCase):
    '''
    testing play functionality of rabbit_hole
    Cost: 2
    Text: +1 link When Rabbit Hole is installed, you may search your stack for another copy of Rabbit Hole and install it by paying its install cost. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for rabbit_hole_01039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_rabbit_hole_01039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_personal_touch_01040(unittest.TestCase):
    '''
    testing play functionality of the_personal_touch
    Cost: 2
    Text: Install The Personal Touch only on an icebreaker. Host icebreaker has +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for the_personal_touch_01040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_the_personal_touch_01040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_toolbox_01041(unittest.TestCase):
    '''
    testing play functionality of the_toolbox
    Cost: 9
    Text: +2 mu +2 link 2 recurring credits Use these credits to pay for using icebreakers. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for the_toolbox_01041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_the_toolbox_01041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spinal_modem_02002(unittest.TestCase):
    '''
    testing play functionality of spinal_modem
    Cost: 4
    Text: +1 mu, 2 recurring credits You can spend hosted credits to use icebreakers. Whenever there is a successful trace during a run, suffer 1 core damage. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for spinal_modem_02002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_spinal_modem_02002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cortez_chip_02005(unittest.TestCase):
    '''
    testing play functionality of cortez_chip
    Cost: 0
    Text: trash: Choose a piece of ice. The Corp must pay 2 credits as an additional cost to rez that ice until the end of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for cortez_chip_02005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_cortez_chip_02005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_plascrete_carapace_02009(unittest.TestCase):
    '''
    testing play functionality of plascrete_carapace
    Cost: 3
    Text: Place 4 power counters on Plascrete Carapace when it is installed. When there are no power counters left on Plascrete Carapace, trash it. Hosted power counter: Prevent 1 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for plascrete_carapace_02009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_plascrete_carapace_02009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_e3_feedback_implants_02024(unittest.TestCase):
    '''
    testing play functionality of e3_feedback_implants
    Cost: 2
    Text: Whenever you break a subroutine on a piece of ice, you may pay 1 credit to break 1 subroutine on that ice.
    '''

    def setUp(self):
        '''
        setup test environment for e3_feedback_implants_02024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_e3_feedback_implants_02024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dyson_mem_chip_02028(unittest.TestCase):
    '''
    testing play functionality of dyson_mem_chip
    Cost: 3
    Text: +1 mu, +1 link
    '''

    def setUp(self):
        '''
        setup test environment for dyson_mem_chip_02028
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_dyson_mem_chip_02028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_muresh_bodysuit_02044(unittest.TestCase):
    '''
    testing play functionality of muresh_bodysuit
    Cost: 1
    Text: Interrupt -> The first time each turn you would suffer meat damage, prevent 1 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for muresh_bodysuit_02044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_muresh_bodysuit_02044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dinosaurus_02048(unittest.TestCase):
    '''
    testing play functionality of dinosaurus
    Cost: 5
    Text: Dinosaurus can host a single non-AI icebreaker. The memory cost of the hosted icebreaker does not count against your memory limit. Hosted icebreaker has +2 strength. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for dinosaurus_02048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_dinosaurus_02048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_doppelganger_02064(unittest.TestCase):
    '''
    testing play functionality of doppelganger
    Cost: 3
    Text: +1 mu Once per turn, you may immediately make another run when a successful run ends. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for doppelganger_02064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_doppelganger_02064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hq_interface_02085(unittest.TestCase):
    '''
    testing play functionality of hq_interface
    Cost: 4
    Text: Whenever you breach HQ, access 1 additional card.
    '''

    def setUp(self):
        '''
        setup test environment for hq_interface_02085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_hq_interface_02085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_replicator_02088(unittest.TestCase):
    '''
    testing play functionality of replicator
    Cost: 2
    Text: Whenever you install a piece of hardware (including Replicator), you may search your stack for another copy of that hardware, reveal it, and add it your grip. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for replicator_02088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_replicator_02088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rd_interface_02107(unittest.TestCase):
    '''
    testing play functionality of rd_interface
    Cost: 4
    Text: Whenever you breach R&D, access 1 additional card.
    '''

    def setUp(self):
        '''
        setup test environment for rd_interface_02107
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_rd_interface_02107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_monolith_03036(unittest.TestCase):
    '''
    testing play functionality of monolith
    Cost: 18
    Text: +3 mu When you install this hardware, install up to 3 programs from your grip, paying 4 credits less for each. Interrupt -> Trash 1 program from your grip: Prevent 1 core damage or 1 net damage. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for monolith_03036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_monolith_03036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_feedback_filter_03037(unittest.TestCase):
    '''
    testing play functionality of feedback_filter
    Cost: 2
    Text: Interrupt -> 3 credits: Prevent 1 net damage. Interrupt -> trash: Prevent up to 2 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for feedback_filter_03037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_feedback_filter_03037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_clone_chip_03038(unittest.TestCase):
    '''
    testing play functionality of clone_chip
    Cost: 1
    Text: trash: Install a program from your heap (paying the install cost).
    '''

    def setUp(self):
        '''
        setup test environment for clone_chip_03038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_clone_chip_03038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_omnidrive_03039(unittest.TestCase):
    '''
    testing play functionality of omnidrive
    Cost: 3
    Text: Omni-drive can host a single program of 1 mu or less. The memory cost of the hosted program does not count against your memory limit. 1 recurring credit Use this credit to pay for using the hosted program.
    '''

    def setUp(self):
        '''
        setup test environment for omnidrive_03039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_omnidrive_03039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lockpick_04006(unittest.TestCase):
    '''
    testing play functionality of lockpick
    Cost: 1
    Text: 1 recurring credit Use this credit to pay for using decoders.
    '''

    def setUp(self):
        '''
        setup test environment for lockpick_04006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_lockpick_04006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_record_reconstructor_04028(unittest.TestCase):
    '''
    testing play functionality of record_reconstructor
    Cost: 0
    Text: Whenever you make a successful run on Archives, instead of breaching Archives, you may add 1 faceup card from Archives to the top of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for record_reconstructor_04028
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_record_reconstructor_04028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_prepaid_voicepad_04029(unittest.TestCase):
    '''
    testing play functionality of prepaid_voicepad
    Cost: 2
    Text: 1 recurring credit (When you install this card and before your turn begins, refill to 1 hosted credit.) You can spend hosted credits to play events.
    '''

    def setUp(self):
        '''
        setup test environment for prepaid_voicepad_04029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_prepaid_voicepad_04029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_deep_red_04042(unittest.TestCase):
    '''
    testing play functionality of deep_red
    Cost: 2
    Text: +3 mu Use the MU on Deep Red only for Caissa programs. Whenever you install a Caissa program, you may trigger its click ability without spending click. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for deep_red_04042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_deep_red_04042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_llds_processor_04066(unittest.TestCase):
    '''
    testing play functionality of llds_processor
    Cost: 1
    Text: Whenever you install an icebreaker, that icebreaker has +1 strength until the end of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for llds_processor_04066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_llds_processor_04066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_capstone_04068(unittest.TestCase):
    '''
    testing play functionality of capstone
    Cost: 2
    Text: click: Trash any number of cards from your grip. For each trashed card of which you have another copy installed, draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for capstone_04068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_capstone_04068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_blackguard_04085(unittest.TestCase):
    '''
    testing play functionality of blackguard
    Cost: 11
    Text: +2 mu Whenever you expose a card, the Corp must rez it by paying its rez cost, if able. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for blackguard_04085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_blackguard_04085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cybersolutions_mem_chip_04086(unittest.TestCase):
    '''
    testing play functionality of cybersolutions_mem_chip
    Cost: 4
    Text: +2 mu
    '''

    def setUp(self):
        '''
        setup test environment for cybersolutions_mem_chip_04086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_cybersolutions_mem_chip_04086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dyson_fractal_generator_04103(unittest.TestCase):
    '''
    testing play functionality of dyson_fractal_generator
    Cost: 1
    Text: 1 recurring credit Use this credit to pay for using fracters.
    '''

    def setUp(self):
        '''
        setup test environment for dyson_fractal_generator_04103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_dyson_fractal_generator_04103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_silencer_04104(unittest.TestCase):
    '''
    testing play functionality of silencer
    Cost: 1
    Text: 1 recurring credit Use this credit to pay for using killers.
    '''

    def setUp(self):
        '''
        setup test environment for silencer_04104
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_silencer_04104()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_logos_05037(unittest.TestCase):
    '''
    testing play functionality of logos
    Cost: 4
    Text: +1 mu Your maximum hand size is increased by 1. Whenever the Corp scores an agenda, you may search your stack for a card and add it to your grip. Shuffle your stack. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for logos_05037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_logos_05037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_public_terminal_05038(unittest.TestCase):
    '''
    testing play functionality of public_terminal
    Cost: 1
    Text: 1 recurring credit Use this credit to play run events.
    '''

    def setUp(self):
        '''
        setup test environment for public_terminal_05038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_public_terminal_05038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_unregistered_sw_35_05039(unittest.TestCase):
    '''
    testing play functionality of unregistered_sw_35
    Cost: 1
    Text: Use this hardware only if you have made a successful run on HQ this turn. click click: Trash 1 rezzed bioroid, clone, executive, or sysop in the root of a remote server.
    '''

    def setUp(self):
        '''
        setup test environment for unregistered_sw_35_05039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_unregistered_sw_35_05039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_window_05040(unittest.TestCase):
    '''
    testing play functionality of window
    Cost: 2
    Text: click: Draw 1 card from the bottom of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for window_05040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_window_05040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_qcoherence_chip_05052(unittest.TestCase):
    '''
    testing play functionality of qcoherence_chip
    Cost: 0
    Text: +1 mu When an installed program is trashed, trash this hardware.
    '''

    def setUp(self):
        '''
        setup test environment for qcoherence_chip_05052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_qcoherence_chip_05052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_boxe_06055(unittest.TestCase):
    '''
    testing play functionality of boxe
    Cost: 4
    Text: +2 mu Your maximum hand size is increased by 2. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for boxe_06055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_boxe_06055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_autoscripter_06076(unittest.TestCase):
    '''
    testing play functionality of autoscripter
    Cost: 3
    Text: The first time you install a program from your grip during your turn, gain click. Trash Autoscripter if you make an unsuccessful run.
    '''

    def setUp(self):
        '''
        setup test environment for autoscripter_06076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_autoscripter_06076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_astrolabe_06079(unittest.TestCase):
    '''
    testing play functionality of astrolabe
    Cost: 1
    Text: +1 mu Draw 1 card whenever the Corp creates a server. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for astrolabe_06079
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_astrolabe_06079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ekomind_06093(unittest.TestCase):
    '''
    testing play functionality of ekomind
    Cost: 2
    Text: Your memory limit is equal to the number of cards in your grip. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for ekomind_06093
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_ekomind_06093()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cybsoft_macrodrive_06098(unittest.TestCase):
    '''
    testing play functionality of cybsoft_macrodrive
    Cost: 2
    Text: 1 recurring credit Use this credit to install programs.
    '''

    def setUp(self):
        '''
        setup test environment for cybsoft_macrodrive_06098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_cybsoft_macrodrive_06098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_archives_interface_07044(unittest.TestCase):
    '''
    testing play functionality of archives_interface
    Cost: 3
    Text: Interrupt -> Whenever you would access a card in Archives, you may instead remove it from the game. Use this ability only once each time you breach Archives.
    '''

    def setUp(self):
        '''
        setup test environment for archives_interface_07044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_archives_interface_07044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chop_bot_3000_07045(unittest.TestCase):
    '''
    testing play functionality of chop_bot_3000
    Cost: 1
    Text: When your turn begins, you may trash another of your installed cards. If you do, draw 1 card or remove 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for chop_bot_3000_07045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_chop_bot_3000_07045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_memstrips_07046(unittest.TestCase):
    '''
    testing play functionality of memstrips
    Cost: 3
    Text: +3 mu Use the MU on MemStrips only for virus programs.
    '''

    def setUp(self):
        '''
        setup test environment for memstrips_07046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_memstrips_07046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vigil_07047(unittest.TestCase):
    '''
    testing play functionality of vigil
    Cost: 2
    Text: +1 mu When your turn begins, if the Corp has cards in HQ equal to their maximum hand size, draw 1 card. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for vigil_07047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_vigil_07047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_qianju_pt_07054(unittest.TestCase):
    '''
    testing play functionality of qianju_pt
    Cost: 2
    Text: When your turn begins, you may lose click. If you do, prevent the first tag you would take until your next turn begins.
    '''

    def setUp(self):
        '''
        setup test environment for qianju_pt_07054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_qianju_pt_07054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dorm_computer_08024(unittest.TestCase):
    '''
    testing play functionality of dorm_computer
    Cost: 0
    Text: Place 4 power counters on Dorm Computer when you install it. click, hosted power counter: Make a run. Avoid all tags for the remainder of the run.
    '''

    def setUp(self):
        '''
        setup test environment for dorm_computer_08024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_dorm_computer_08024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_comet_08027(unittest.TestCase):
    '''
    testing play functionality of comet
    Cost: 4
    Text: +1 mu The first time you play an event each turn, you may play another event (without spending a click) after the first one resolves. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for comet_08027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_comet_08027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_skulljack_08042(unittest.TestCase):
    '''
    testing play functionality of skulljack
    Cost: 2
    Text: When you install this hardware, suffer 1 core damage. The trash cost of each Corp card is lowered by 1.
    '''

    def setUp(self):
        '''
        setup test environment for skulljack_08042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_skulljack_08042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_turntable_08043(unittest.TestCase):
    '''
    testing play functionality of turntable
    Cost: 2
    Text: +1 mu Whenever you steal an agenda, you may swap that agenda with an agenda in the Corp's score area. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for turntable_08043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_turntable_08043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_titanium_ribs_08045(unittest.TestCase):
    '''
    testing play functionality of titanium_ribs
    Cost: 1
    Text: When you install Titanium Ribs, suffer 2 meat damage. You choose the card(s) from your grip to trash whenever you take damage (including the damage taken by installing Titanium Ribs).
    '''

    def setUp(self):
        '''
        setup test environment for titanium_ribs_08045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_titanium_ribs_08045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_netready_eyes_08047(unittest.TestCase):
    '''
    testing play functionality of netready_eyes
    Cost: 0
    Text: When you install Net-Ready Eyes, suffer 2 meat damage. Whenever you initiate a run, choose an icebreaker. That icebreaker has +1 strength for the remainder of the run.
    '''

    def setUp(self):
        '''
        setup test environment for netready_eyes_08047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_netready_eyes_08047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_brain_cage_08049(unittest.TestCase):
    '''
    testing play functionality of brain_cage
    Cost: 1
    Text: You get +3 maximum hand size. When you install this hardware, suffer 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for brain_cage_08049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_brain_cage_08049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_forger_08065(unittest.TestCase):
    '''
    testing play functionality of forger
    Cost: 1
    Text: +1 link Interrupt -> trash: Prevent 1 tag. trash: Remove 1 tag. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for forger_08065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_forger_08065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bookmark_08106(unittest.TestCase):
    '''
    testing play functionality of bookmark
    Cost: 0
    Text: click: Host up to 3 cards from your grip facedown on this hardware (you may look at these cards at any time). click: Add all hosted cards to your grip. trash: Add all hosted cards to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for bookmark_08106
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_bookmark_08106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_heartbeat_09032(unittest.TestCase):
    '''
    testing play functionality of heartbeat
    Cost: 2
    Text: +1 mu Trash an installed card: Prevent 1 damage. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for heartbeat_09032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_heartbeat_09032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_brain_chip_09039(unittest.TestCase):
    '''
    testing play functionality of brain_chip
    Cost: 2
    Text: +X mu Your maximum hand size is increased by X. X is equal to the number of agenda points you have. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for brain_chip_09039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_brain_chip_09039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_security_chip_09046(unittest.TestCase):
    '''
    testing play functionality of security_chip
    Cost: 0
    Text: trash: Choose an icebreaker (or any number of cloud icebreakers). Each chosen icebreaker has +1 strength for each link you have for the remainder of this run. Use this ability only during a run.
    '''

    def setUp(self):
        '''
        setup test environment for security_chip_09046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_security_chip_09046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_security_nexus_09047(unittest.TestCase):
    '''
    testing play functionality of security_nexus
    Cost: 8
    Text: +1 mu +1 link Once per turn, when you encounter a piece of ice, you may force the Corp to "Trace[5]. If successful, give the Runner 1 tag and end the run. If unsuccessful, the Runner bypasses the currently encountered ice." Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for security_nexus_09047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_security_nexus_09047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ramujanreliant_550_bmi_10002(unittest.TestCase):
    '''
    testing play functionality of ramujanreliant_550_bmi
    Cost: 1
    Text: Interrupt -> trash: Prevent up to X core damage or net damage. Trash cards from the top of your stack equal to the amount of damage prevented. X is equal to the number of other installed copies of Ramujan-reliant 550 BMI plus 1. Limit 6 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for ramujanreliant_550_bmi_10002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_ramujanreliant_550_bmi_10002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_maya_10007(unittest.TestCase):
    '''
    testing play functionality of maya
    Cost: 3
    Text: +2 mu Once per turn, immediately after you access a card from R&D, you may add that card to the bottom of R&D. If you do, take 1 tag. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for maya_10007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_maya_10007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_emp_device_10020(unittest.TestCase):
    '''
    testing play functionality of emp_device
    Cost: 1
    Text: trash: The Corp cannot rez more than 1 piece of ice for the remainder of this run. Use this ability only during a run.
    '''

    def setUp(self):
        '''
        setup test environment for emp_device_10020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_emp_device_10020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_netchip_10024(unittest.TestCase):
    '''
    testing play functionality of netchip
    Cost: 1
    Text: NetChip can host a program with a memory cost less than or equal to the number of copies of NetChip installed. The memory cost of the hosted program does not count against your memory limit. Limit 6 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for netchip_10024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_netchip_10024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reflection_10041(unittest.TestCase):
    '''
    testing play functionality of reflection
    Cost: 2
    Text: +1 mu +1 link Whenever you jack out, the Corp reveals 1 card from HQ at random. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for reflection_10041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_reflection_10041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spy_camera_10042(unittest.TestCase):
    '''
    testing play functionality of spy_camera
    Cost: 0
    Text: click: Look at the top X cards of your stack and arrange them in any order. X is the number of copies of Spy Camera installed. trash: Look at the top card of R&D. Limit 6 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for spy_camera_10042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_spy_camera_10042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sports_hopper_10064(unittest.TestCase):
    '''
    testing play functionality of sports_hopper
    Cost: 3
    Text: +1 link trash: Draw 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for sports_hopper_10064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_sports_hopper_10064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gpi_net_tap_11003(unittest.TestCase):
    '''
    testing play functionality of gpi_net_tap
    Cost: 3
    Text: Whenever you approach a piece of ice, you may expose it. You may then trash GPI Net Tap to jack out.
    '''

    def setUp(self):
        '''
        setup test environment for gpi_net_tap_11003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_gpi_net_tap_11003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mirror_11005(unittest.TestCase):
    '''
    testing play functionality of mirror
    Cost: 3
    Text: +2 mu Whenever you make a successful run on R&D, you may replace 1 spent recurring credit. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for mirror_11005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_mirror_11005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_obelus_11041(unittest.TestCase):
    '''
    testing play functionality of obelus
    Cost: 4
    Text: +1 mu You get +1 maximum hand size for each tag you have. The first time each turn a successful run on HQ or R&D ends, draw 1 card for each time you accessed a card during that run. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for obelus_11041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_obelus_11041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_gauntlet_11063(unittest.TestCase):
    '''
    testing play functionality of the_gauntlet
    Cost: 5
    Text: +2 mu Whenever you breach HQ during a run, access 1 additional card for each piece of ice protecting HQ that you fully broke during that run. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for the_gauntlet_11063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_the_gauntlet_11063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_top_hat_11067(unittest.TestCase):
    '''
    testing play functionality of top_hat
    Cost: 0
    Text: Whenever you make a successful run on R&D, instead of breaching R&D, you may choose 1 of the top 5 cards in R&D and access it.
    '''

    def setUp(self):
        '''
        setup test environment for top_hat_11067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_top_hat_11067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sifr_11101(unittest.TestCase):
    '''
    testing play functionality of sifr
    Cost: 5
    Text: +2 mu Once per turn, when you encounter a piece of ice, you may reduce your maximum hand size by 1 until the beginning of your next turn. If you do, the strength of that ice is lowered to 0 for the remainder of the encounter. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for sifr_11101
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_sifr_11101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_recon_drone_11103(unittest.TestCase):
    '''
    testing play functionality of recon_drone
    Cost: 1
    Text: X credits,trash: Prevent X damage from a card currently being accessed.
    '''

    def setUp(self):
        '''
        setup test environment for recon_drone_11103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_recon_drone_11103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_maw_12002(unittest.TestCase):
    '''
    testing play functionality of maw
    Cost: 6
    Text: +2 mu The first time each turn you access a card not in Archives and do not steal or trash it, the Corp must trash 1 card from HQ at random. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for maw_12002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_maw_12002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_severnius_stim_implant_12021(unittest.TestCase):
    '''
    testing play functionality of severnius_stim_implant
    Cost: 2
    Text: click: Trash 2 or more cards from your grip. Run HQ or R&D. Whenever you breach that server during this run, access 1 additional card for every 2 cards you trashed.
    '''

    def setUp(self):
        '''
        setup test environment for severnius_stim_implant_12021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_severnius_stim_implant_12021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rubicon_switch_12043(unittest.TestCase):
    '''
    testing play functionality of rubicon_switch
    Cost: 3
    Text: click, X credits: Derez 1 piece of ice with printed rez cost X credits that was rezzed this turn. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for rubicon_switch_12043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_rubicon_switch_12043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_adjusted_matrix_12046(unittest.TestCase):
    '''
    testing play functionality of adjusted_matrix
    Cost: 5
    Text: Install only on an icebreaker. Host icebreaker gains AI and "Interface -> Lose click: Break 1 subroutine."
    '''

    def setUp(self):
        '''
        setup test environment for adjusted_matrix_12046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_adjusted_matrix_12046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dedicated_processor_12047(unittest.TestCase):
    '''
    testing play functionality of dedicated_processor
    Cost: 2
    Text: Install Dedicated Processor on a non-AI icebreaker. Host icebreaker gains "2 credits: +4 strength."
    '''

    def setUp(self):
        '''
        setup test environment for dedicated_processor_12047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_dedicated_processor_12047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_maui_12063(unittest.TestCase):
    '''
    testing play functionality of maui
    Cost: 5
    Text: +2 mu X recurring credits Use these credits during runs on HQ. X is the number of pieces of ice protecting HQ. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for maui_12063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_maui_12063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_daredevil_12066(unittest.TestCase):
    '''
    testing play functionality of daredevil
    Cost: 5
    Text: +2 mu The first time you initiate a run on a server protected by 2 or more pieces of ice each turn, draw 2 cards. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for daredevil_12066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_daredevil_12066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_respirocytes_12102(unittest.TestCase):
    '''
    testing play functionality of respirocytes
    Cost: 0
    Text: When you install this hardware, suffer 1 meat damage. The first time each turn you have no cards in your grip, draw 1 card and place 1 power counter on this hardware. When this hardware has 3 or more hosted power counters, trash it.
    '''

    def setUp(self):
        '''
        setup test environment for respirocytes_12102
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_respirocytes_12102()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_polyhistor_13005(unittest.TestCase):
    '''
    testing play functionality of polyhistor
    Cost: 4
    Text: +1 mu, +1 link The first time each turn you pass all of the ice protecting HQ, you may draw 1 card to force the Corp to draw 1 card. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for polyhistor_13005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_polyhistor_13005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_llds_memory_diamond_13015(unittest.TestCase):
    '''
    testing play functionality of llds_memory_diamond
    Cost: 4
    Text: +1 mu, +1 link Your maximum hand size is increased by 1.
    '''

    def setUp(self):
        '''
        setup test environment for llds_memory_diamond_13015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_llds_memory_diamond_13015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ubax_13016(unittest.TestCase):
    '''
    testing play functionality of ubax
    Cost: 5
    Text: +1 mu When your turn begins, draw 1 card. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for ubax_13016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_ubax_13016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bmi_buffer_14020(unittest.TestCase):
    '''
    testing play functionality of bmi_buffer
    Cost: 3
    Text: Whenever a program is trashed from your grip, host it on BMI Buffer instead of adding it to your heap. click click: Install 1 hosted program (paying all costs).
    '''

    def setUp(self):
        '''
        setup test environment for bmi_buffer_14020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_bmi_buffer_14020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bmi_buffer_2_14021(unittest.TestCase):
    '''
    testing play functionality of bmi_buffer_2
    Cost: 3
    Text: Whenever a program is trashed from your grip, host it on BMI Buffer instead of adding it to your heap. click click: Install 1 hosted program, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for bmi_buffer_2_14021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_bmi_buffer_2_14021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cyberfeeder_20006(unittest.TestCase):
    '''
    testing play functionality of cyberfeeder
    Cost: 2
    Text: 1 recurring credit Use this credit to pay for using icebreakers or for installing virus programs.
    '''

    def setUp(self):
        '''
        setup test environment for cyberfeeder_20006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_cyberfeeder_20006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spinal_modem_20007(unittest.TestCase):
    '''
    testing play functionality of spinal_modem
    Cost: 4
    Text: +1 mu, 2 recurring credits You can spend hosted credits to use icebreakers. Whenever there is a successful trace during a run, suffer 1 core damage. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for spinal_modem_20007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_spinal_modem_20007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_doppelganger_20025(unittest.TestCase):
    '''
    testing play functionality of doppelganger
    Cost: 3
    Text: +1 mu Once per turn, you may immediately make another run when a successful run ends. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for doppelganger_20025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_doppelganger_20025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hq_interface_20026(unittest.TestCase):
    '''
    testing play functionality of hq_interface
    Cost: 4
    Text: Whenever you breach HQ, access 1 additional card.
    '''

    def setUp(self):
        '''
        setup test environment for hq_interface_20026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_hq_interface_20026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dinosaurus_20045(unittest.TestCase):
    '''
    testing play functionality of dinosaurus
    Cost: 5
    Text: Dinosaurus can host a single non-AI icebreaker. The memory cost of the hosted icebreaker does not count against your memory limit. Hosted icebreaker has +2 strength. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for dinosaurus_20045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_dinosaurus_20045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rabbit_hole_20046(unittest.TestCase):
    '''
    testing play functionality of rabbit_hole
    Cost: 2
    Text: +1 link When Rabbit Hole is installed, you may search your stack for another copy of Rabbit Hole and install it by paying its install cost. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for rabbit_hole_20046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_rabbit_hole_20046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_personal_touch_20047(unittest.TestCase):
    '''
    testing play functionality of the_personal_touch
    Cost: 2
    Text: Install The Personal Touch only on an icebreaker. Host icebreaker has +1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for the_personal_touch_20047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_the_personal_touch_20047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dyson_mem_chip_20057(unittest.TestCase):
    '''
    testing play functionality of dyson_mem_chip
    Cost: 3
    Text: +1 mu, +1 link
    '''

    def setUp(self):
        '''
        setup test environment for dyson_mem_chip_20057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_dyson_mem_chip_20057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zamba_21003(unittest.TestCase):
    '''
    testing play functionality of zamba
    Cost: 4
    Text: +2 mu Whenever a Corp card is exposed, you may gain 1 credit. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for zamba_21003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_zamba_21003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cyberdelia_21006(unittest.TestCase):
    '''
    testing play functionality of cyberdelia
    Cost: 3
    Text: +1 mu The first time each turn you fully break a piece of ice, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for cyberdelia_21006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_cyberdelia_21006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_acacia_21021(unittest.TestCase):
    '''
    testing play functionality of acacia
    Cost: 1
    Text: Whenever the Corp purges virus counters, you may gain 1 credit for each virus counter removed and trash Acacia.
    '''

    def setUp(self):
        '''
        setup test environment for acacia_21021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_acacia_21021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_friday_chip_21042(unittest.TestCase):
    '''
    testing play functionality of friday_chip
    Cost: 2
    Text: Whenever you trash a Corp card, you may place 1 virus counter on Friday Chip. When your turn begins, you may move 1 hosted virus counter to a virus program.
    '''

    def setUp(self):
        '''
        setup test environment for friday_chip_21042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_friday_chip_21042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_knobkierie_21062(unittest.TestCase):
    '''
    testing play functionality of knobkierie
    Cost: 5
    Text: +3 mu Use the MU on Knobkierie only for virus programs. The first time you make a successful run each turn, you may place 1 virus counter on an installed virus program. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for knobkierie_21062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_knobkierie_21062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gebrselassie_21087(unittest.TestCase):
    '''
    testing play functionality of gebrselassie
    Cost: 1
    Text: click: Host this hardware on an installed non-AI icebreaker. Abilities that increase host icebreaker's strength last for the remainder of the turn (instead of any shorter duration).
    '''

    def setUp(self):
        '''
        setup test environment for gebrselassie_21087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_gebrselassie_21087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zer0_21101(unittest.TestCase):
    '''
    testing play functionality of zer0
    Cost: 1
    Text: click, suffer 1 net damage: Gain 1 credit and draw 2 cards. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for zer0_21101
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_zer0_21101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hippo_21103(unittest.TestCase):
    '''
    testing play functionality of hippo
    Cost: 2
    Text: The first time each turn you fully break the outermost piece of ice protecting the attacked server during a run, you may remove this hardware from the game to trash that ice.
    '''

    def setUp(self):
        '''
        setup test environment for hippo_21103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_hippo_21103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_flameout_21109(unittest.TestCase):
    '''
    testing play functionality of flameout
    Cost: 2
    Text: Flame-out can host a single program. When you install Flame-out, place 9 credits on it. Use these credits to pay for using hosted program. When a turn ends in which you used credits on Flame-out, trash hosted program.
    '''

    def setUp(self):
        '''
        setup test environment for flameout_21109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_flameout_21109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_patchwork_22004(unittest.TestCase):
    '''
    testing play functionality of patchwork
    Cost: 4
    Text: +1 mu Interrupt -> Whenever you would play or install a card, you may trash 1 card from your grip. If you do, instead play or install that card paying 2 credits less. Use this ability only once per turn. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for patchwork_22004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_patchwork_22004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hijacked_router_22005(unittest.TestCase):
    '''
    testing play functionality of hijacked_router
    Cost: 2
    Text: Whenever the Corp creates a server, they lose 1 credit. Whenever you make a successful run on Archives, you may trash this hardware. If you do, the Corp loses 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for hijacked_router_22005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_hijacked_router_22005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paragon_22010(unittest.TestCase):
    '''
    testing play functionality of paragon
    Cost: 3
    Text: +1 mu The first time you make a successful run each turn, you may gain 1 credit and look at the top card of your stack. If you do, you may add that card to the bottom of your stack. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for paragon_22010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_paragon_22010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_minds_eye_22017(unittest.TestCase):
    '''
    testing play functionality of minds_eye
    Cost: 3
    Text: +1 mu Whenever you make a successful run on R&D, you may place 1 power counter on this hardware. click, 3 hosted power counters: Breach R&D. You cannot access cards in the root of R&D during this breach. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for minds_eye_22017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_minds_eye_22017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mache_22018(unittest.TestCase):
    '''
    testing play functionality of mache
    Cost: 1
    Text: The first time you trash an accessed card each turn, you may place power counters on Mache equal to that card's trash cost. 3 hosted power counters: Draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for mache_22018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_mache_22018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cyberfeeder_25008(unittest.TestCase):
    '''
    testing play functionality of cyberfeeder
    Cost: 2
    Text: 1 recurring credit Use this credit to pay for using icebreakers or for installing virus programs.
    '''

    def setUp(self):
        '''
        setup test environment for cyberfeeder_25008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_cyberfeeder_25008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_patchwork_25009(unittest.TestCase):
    '''
    testing play functionality of patchwork
    Cost: 4
    Text: +1 mu Interrupt -> Whenever you would play or install a card, you may trash 1 card from your grip. If you do, instead play or install that card paying 2 credits less. Use this ability only once per turn. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for patchwork_25009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_patchwork_25009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hq_interface_25031(unittest.TestCase):
    '''
    testing play functionality of hq_interface
    Cost: 4
    Text: Whenever you breach HQ, access 1 additional card.
    '''

    def setUp(self):
        '''
        setup test environment for hq_interface_25031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_hq_interface_25031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paragon_25032(unittest.TestCase):
    '''
    testing play functionality of paragon
    Cost: 3
    Text: +1 mu The first time you make a successful run each turn, you may gain 1 credit and look at the top card of your stack. If you do, you may add that card to the bottom of your stack. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for paragon_25032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_paragon_25032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_akamatsu_mem_chip_25048(unittest.TestCase):
    '''
    testing play functionality of akamatsu_mem_chip
    Cost: 1
    Text: +1 mu
    '''

    def setUp(self):
        '''
        setup test environment for akamatsu_mem_chip_25048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_akamatsu_mem_chip_25048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dinosaurus_25049(unittest.TestCase):
    '''
    testing play functionality of dinosaurus
    Cost: 5
    Text: Dinosaurus can host a single non-AI icebreaker. The memory cost of the hosted icebreaker does not count against your memory limit. Hosted icebreaker has +2 strength. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for dinosaurus_25049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_dinosaurus_25049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rd_interface_25050(unittest.TestCase):
    '''
    testing play functionality of rd_interface
    Cost: 4
    Text: Whenever you breach R&D, access 1 additional card.
    '''

    def setUp(self):
        '''
        setup test environment for rd_interface_25050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_rd_interface_25050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_demolisher_26002(unittest.TestCase):
    '''
    testing play functionality of demolisher
    Cost: 4
    Text: +1 mu The trash cost of each Corp card is lowered by 1. The first time each turn you trash a Corp card, gain 1 credit. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for demolisher_26002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_demolisher_26002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_flip_switch_26013(unittest.TestCase):
    '''
    testing play functionality of flip_switch
    Cost: 1
    Text: You cannot use this hardware during the Corp's turn. trash: Jack out. trash: Remove 1 tag. Interrupt -> trash: Reduce the base trace strength of a trace to 0.
    '''

    def setUp(self):
        '''
        setup test environment for flip_switch_26013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_flip_switch_26013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lucky_charm_26014(unittest.TestCase):
    '''
    testing play functionality of lucky_charm
    Cost: 1
    Text: Remove this hardware from the game: Prevent a Corp card ability from ending the run. Use this ability only if you made a successful run on HQ this turn.
    '''

    def setUp(self):
        '''
        setup test environment for lucky_charm_26014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_lucky_charm_26014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_masterwork_v37_26015(unittest.TestCase):
    '''
    testing play functionality of masterwork_v37
    Cost: 2
    Text: +1 mu. The first time each turn you install a piece of hardware, draw 1 card. Whenever a run begins, you may install a piece of hardware, paying 1 credit more. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for masterwork_v37_26015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_masterwork_v37_26015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_supercorridor_26023(unittest.TestCase):
    '''
    testing play functionality of supercorridor
    Cost: 4
    Text: +2 mu You have +1 maximum hand size. When your turn ends, if you and the Corp have the same number of credits, you may gain 2 credits. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for supercorridor_26023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_supercorridor_26023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_devil_charm_26068(unittest.TestCase):
    '''
    testing play functionality of devil_charm
    Cost: 1
    Text: Whenever you encounter a piece of ice, you may remove this hardware from the game. If you do, that ice gets -6 strength for the remainder of the run.
    '''

    def setUp(self):
        '''
        setup test environment for devil_charm_26068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_devil_charm_26068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gachapon_26069(unittest.TestCase):
    '''
    testing play functionality of gachapon
    Cost: 0
    Text: trash: Set aside the top 6 cards of your stack. You may install 1 program or virtual resource from among the set aside cards, paying 2 credits less. Shuffle 3 of the remaining cards into your stack, then remove the rest from the game.
    '''

    def setUp(self):
        '''
        setup test environment for gachapon_26069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_gachapon_26069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_keiko_26070(unittest.TestCase):
    '''
    testing play functionality of keiko
    Cost: 3
    Text: +2 mu The first time each turn you spend credits from or install a companion, gain 1 credit. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for keiko_26070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_keiko_26070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_boomerang_26075(unittest.TestCase):
    '''
    testing play functionality of boomerang
    Cost: 2
    Text: When you install this hardware, choose an installed piece of ice. Use this hardware only during encounters with that ice. trash: Break up to 2 subroutines. When this run ends, if it is successful, you may shuffle a copy of Boomerang from your heap into your stack.
    '''

    def setUp(self):
        '''
        setup test environment for boomerang_26075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_boomerang_26075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mu_safecracker_26076(unittest.TestCase):
    '''
    testing play functionality of mu_safecracker
    Cost: 2
    Text: Use this hardware only by spending credits from stealth cards. Whenever you make a successful run on HQ, you may pay 1 credit to access 1 additional card when you breach HQ. Whenever you make a successful run on R&D, you may pay 2 credits to access 1 additional card when you breach R&D.
    '''

    def setUp(self):
        '''
        setup test environment for mu_safecracker_26076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_mu_safecracker_26076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_prognostic_qloop_26077(unittest.TestCase):
    '''
    testing play functionality of prognostic_qloop
    Cost: 1
    Text: The first time each turn a run begins, you may look at the top 2 cards of your stack. 1 credit: Reveal the top card of your stack. You may install that card if it is a program or piece of hardware. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for prognostic_qloop_26077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_prognostic_qloop_26077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_swift_26078(unittest.TestCase):
    '''
    testing play functionality of swift
    Cost: 2
    Text: +1 mu The first time each turn you play a run event, gain click. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for swift_26078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_swift_26078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aniccam_26084(unittest.TestCase):
    '''
    testing play functionality of aniccam
    Cost: 3
    Text: +1 mu The first time each turn an event is trashed (from any location), draw 1 card. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for aniccam_26084
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_aniccam_26084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_simulchip_26085(unittest.TestCase):
    '''
    testing play functionality of simulchip
    Cost: 1
    Text: If no installed programs have been trashed this turn, you must trash 1 installed program as an additional cost to use this hardware. trash: Install 1 program from your heap, paying 3 credits less.
    '''

    def setUp(self):
        '''
        setup test environment for simulchip_26085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_simulchip_26085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_buffer_drive_26093(unittest.TestCase):
    '''
    testing play functionality of buffer_drive
    Cost: 3
    Text: The first time each turn 1 or more cards are trashed from your grip or stack, you may add 1 of those cards to the bottom of your stack. Remove this hardware from the game: Add 1 card from your heap to the top of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for buffer_drive_26093
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_buffer_drive_26093()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_swift_27002(unittest.TestCase):
    '''
    testing play functionality of swift
    Cost: 2
    Text: +1 mu The first time each turn you play a run event, gain click. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for swift_27002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_swift_27002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_e3_feedback_implants_29003(unittest.TestCase):
    '''
    testing play functionality of e3_feedback_implants
    Cost: 2
    Text: Whenever you break a subroutine on a piece of ice, you may pay 1 credit to break 1 subroutine on that ice.
    '''

    def setUp(self):
        '''
        setup test environment for e3_feedback_implants_29003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_e3_feedback_implants_29003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_prepaid_voicepad_29008(unittest.TestCase):
    '''
    testing play functionality of prepaid_voicepad
    Cost: 2
    Text: 1 recurring credit (When you install this card and before your turn begins, refill to 1 hosted credit.) You can spend hosted credits to play events.
    '''

    def setUp(self):
        '''
        setup test environment for prepaid_voicepad_29008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_prepaid_voicepad_29008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_carnivore_30003(unittest.TestCase):
    '''
    testing play functionality of carnivore
    Cost: 4
    Text: +1 mu Access -> Trash 2 cards from your grip: Trash the card you are accessing. Use this ability only once per turn. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for carnivore_30003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_carnivore_30003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_docklands_pass_30013(unittest.TestCase):
    '''
    testing play functionality of docklands_pass
    Cost: 2
    Text: The first time each turn you breach HQ, access 1 additional card.
    '''

    def setUp(self):
        '''
        setup test environment for docklands_pass_30013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_docklands_pass_30013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pennyshaver_30014(unittest.TestCase):
    '''
    testing play functionality of pennyshaver
    Cost: 3
    Text: +1 mu Whenever you make a successful run, place 1 credit on this hardware. click: Place 1 credit on this hardware, then take all credits from it. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for pennyshaver_30014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_pennyshaver_30014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dzmz_optimizer_30022(unittest.TestCase):
    '''
    testing play functionality of dzmz_optimizer
    Cost: 2
    Text: +1 mu The first program you install each turn costs 1 credit less to install.
    '''

    def setUp(self):
        '''
        setup test environment for dzmz_optimizer_30022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_dzmz_optimizer_30022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pantograph_30023(unittest.TestCase):
    '''
    testing play functionality of pantograph
    Cost: 2
    Text: +1 mu Whenever an agenda is scored or stolen, gain 1 credit. Then, you may install 1 card from your grip. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for pantograph_30023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_pantograph_30023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_t400_memory_diamond_30031(unittest.TestCase):
    '''
    testing play functionality of t400_memory_diamond
    Cost: 2
    Text: +1 mu You get +1 maximum hand size.
    '''

    def setUp(self):
        '''
        setup test environment for t400_memory_diamond_30031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_t400_memory_diamond_30031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_prepaid_voicepad_31038(unittest.TestCase):
    '''
    testing play functionality of prepaid_voicepad
    Cost: 2
    Text: 1 recurring credit (When you install this card and before your turn begins, refill to 1 hosted credit.) You can spend hosted credits to play events.
    '''

    def setUp(self):
        '''
        setup test environment for prepaid_voicepad_31038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_prepaid_voicepad_31038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ghosttongue_33005(unittest.TestCase):
    '''
    testing play functionality of ghosttongue
    Cost: 2
    Text: When you install this hardware, suffer 1 core damage. The play cost of each event is lowered by 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for ghosttongue_33005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_ghosttongue_33005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_marrow_33006(unittest.TestCase):
    '''
    testing play functionality of marrow
    Cost: 2
    Text: +1mu You get +3 maximum hand size. When you install this hardware, suffer 1 core damage. Whenever the Corp scores an agenda, sabotage 1. (The Corp trashes 1 card of their choice from HQ or the top of R&D.) Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for marrow_33006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_marrow_33006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_panweave_33014(unittest.TestCase):
    '''
    testing play functionality of panweave
    Cost: 2
    Text: When you install this hardware, suffer 1 meat damage. The first time each turn you make a successful run on HQ, the Corp loses 1 credit. If they do, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for panweave_33014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_panweave_33014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_virtuoso_33015(unittest.TestCase):
    '''
    testing play functionality of virtuoso
    Cost: 4
    Text: +1mu When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) The first time each turn you make a successful run on your mark, if that server is HQ, access 1 additional card when you breach HQ. Otherwise, breach HQ when the run ends. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for virtuoso_33015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_virtuoso_33015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_endurance_33025(unittest.TestCase):
    '''
    testing play functionality of endurance
    Cost: 8
    Text: +2mu When you install this hardware, place 3 power counters on it. The first time each turn you make a successful run, place 1 power counter on this hardware. 2 hosted power counters: Break up to 2 subroutines. Limit 1 console per player.
    '''

    def setUp(self):
        '''
        setup test environment for endurance_33025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_endurance_33025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_time_bomb_33069(unittest.TestCase):
    '''
    testing play functionality of time_bomb
    Cost: 1
    Text: Install only if you made a successful run on a central server this turn. When you install this hardware, place 1 power counter on it. When your turn begins, if there are 3 or more hosted power counters, trash this hardware and sabotage 3. (The Corp trashes 3 cards of their choice from HQ and/or the top of R&D.) Otherwise, place 1 power counter on this hardware.
    '''

    def setUp(self):
        '''
        setup test environment for time_bomb_33069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_time_bomb_33069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_poison_vial_33077(unittest.TestCase):
    '''
    testing play functionality of poison_vial
    Cost: 2
    Text: When you install this hardware, load 3 power counters onto it. When it is empty, trash it. Hosted power counter: Break up to 2 subroutines. Use this ability only if you have already broken a subroutine during this encounter.
    '''

    def setUp(self):
        '''
        setup test environment for poison_vial_33077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_poison_vial_33077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wake_implant_v2ajrj_33078(unittest.TestCase):
    '''
    testing play functionality of wake_implant_v2ajrj
    Cost: 1
    Text: When you install this hardware, suffer 1 meat damage. Whenever you make a successful run on HQ, place 1 power counter on this hardware. Whenever you breach R&D, you may remove up to 3 hosted power counters to access that many additional cards.
    '''

    def setUp(self):
        '''
        setup test environment for wake_implant_v2ajrj_33078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_wake_implant_v2ajrj_33078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zenit_chip_jz2mj_33079(unittest.TestCase):
    '''
    testing play functionality of zenit_chip_jz2mj
    Cost: 1
    Text: When you install this hardware, suffer 1 core damage. The first time each turn you make a successful run on a central server, draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for zenit_chip_jz2mj_33079
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_zenit_chip_jz2mj_33079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hippocampic_mechanocytes_33085(unittest.TestCase):
    '''
    testing play functionality of hippocampic_mechanocytes
    Cost: 0
    Text: When you install this hardware, place 2 power counters on it and suffer 1 meat damage. You get +1 maximum hand size for each hosted power counter.
    '''

    def setUp(self):
        '''
        setup test environment for hippocampic_mechanocytes_33085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_hippocampic_mechanocytes_33085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_basilar_synthgland_2kvj_33086(unittest.TestCase):
    '''
    testing play functionality of basilar_synthgland_2kvj
    Cost: 1
    Text: When you install this hardware, suffer 2 core damage. You get +1 allotted click for each of your turns.
    '''

    def setUp(self):
        '''
        setup test environment for basilar_synthgland_2kvj_33086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = hardware_basilar_synthgland_2kvj_33086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")
