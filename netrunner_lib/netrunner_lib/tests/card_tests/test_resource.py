
'''
test cases for card classes of type resource
'''
import unittest

from netrunner_lib.cards._base_card_classes import Resource
from netrunner_lib.cards.resource import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
class Test_ice_carver_01015(unittest.TestCase):
    '''
    testing play functionality of ice_carver
    Cost: 3
    Text: While you are encountering a piece of ice, it gets -1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for ice_carver_01015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_ice_carver_01015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wyldside_01016(unittest.TestCase):
    '''
    testing play functionality of wyldside
    Cost: 3
    Text: When your turn begins, draw 2 cards and lose click.
    '''

    def setUp(self):
        '''
        setup test environment for wyldside_01016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_wyldside_01016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bank_job_01029(unittest.TestCase):
    '''
    testing play functionality of bank_job
    Cost: 1
    Text: When you install this resource, load 8 credits on it. When it is empty, trash it. Whenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for bank_job_01029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_bank_job_01029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crash_space_01030(unittest.TestCase):
    '''
    testing play functionality of crash_space
    Cost: 2
    Text: 2 recurring credits Use these credits to pay for removing tags. trash: Prevent up to 3 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for crash_space_01030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_crash_space_01030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_dealer_01031(unittest.TestCase):
    '''
    testing play functionality of data_dealer
    Cost: 0
    Text: click, forfeit 1 agenda: Gain 9 credits.
    '''

    def setUp(self):
        '''
        setup test environment for data_dealer_01031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_data_dealer_01031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_decoy_01032(unittest.TestCase):
    '''
    testing play functionality of decoy
    Cost: 1
    Text: trash: Avoid receiving 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for decoy_01032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_decoy_01032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aesops_pawnshop_01047(unittest.TestCase):
    '''
    testing play functionality of aesops_pawnshop
    Cost: 1
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for aesops_pawnshop_01047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_aesops_pawnshop_01047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sacrificial_construct_01048(unittest.TestCase):
    '''
    testing play functionality of sacrificial_construct
    Cost: 0
    Text: trash: Prevent an installed program or an installed piece of hardware from being trashed.
    '''

    def setUp(self):
        '''
        setup test environment for sacrificial_construct_01048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_sacrificial_construct_01048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_access_to_globalsec_01052(unittest.TestCase):
    '''
    testing play functionality of access_to_globalsec
    Cost: 1
    Text: +1 link
    '''

    def setUp(self):
        '''
        setup test environment for access_to_globalsec_01052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_access_to_globalsec_01052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_armitage_codebusting_01053(unittest.TestCase):
    '''
    testing play functionality of armitage_codebusting
    Cost: 1
    Text: Place 12 credits from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it. click: Take 2 credits from Armitage Codebusting.
    '''

    def setUp(self):
        '''
        setup test environment for armitage_codebusting_01053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_armitage_codebusting_01053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_helpful_ai_02008(unittest.TestCase):
    '''
    testing play functionality of the_helpful_ai
    Cost: 2
    Text: +1 link trash: Choose an icebreaker. That icebreaker has +2 strength until the end of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for the_helpful_ai_02008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_helpful_ai_02008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_liberated_account_02022(unittest.TestCase):
    '''
    testing play functionality of liberated_account
    Cost: 6
    Text: When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for liberated_account_02022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_liberated_account_02022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_compromised_employee_02025(unittest.TestCase):
    '''
    testing play functionality of compromised_employee
    Cost: 2
    Text: 1 recurring credit Use this credit during traces. Gain 1 credit whenever the Corp rezzes a piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for compromised_employee_02025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_compromised_employee_02025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_joshua_b_02042(unittest.TestCase):
    '''
    testing play functionality of joshua_b
    Cost: 1
    Text: When your turn begins, you may gain click. If you do, take 1 tag when this turn ends.
    '''

    def setUp(self):
        '''
        setup test environment for joshua_b_02042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_joshua_b_02042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_personal_workshop_02049(unittest.TestCase):
    '''
    testing play functionality of personal_workshop
    Cost: 1
    Text: click: Host a program or piece of hardware from your grip on Personal Workshop and place power counters on it equal to its install cost. 1 credit: Remove 1 power counter from a hosted card. When your turn begins, remove 1 power counter from a hosted card. When there are no power counters left on a hosted card, install it, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for personal_workshop_02049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_personal_workshop_02049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_public_sympathy_02050(unittest.TestCase):
    '''
    testing play functionality of public_sympathy
    Cost: 2
    Text: Your maximum hand size is increased by 2.
    '''

    def setUp(self):
        '''
        setup test environment for public_sympathy_02050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_public_sympathy_02050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_scrubber_02063(unittest.TestCase):
    '''
    testing play functionality of scrubber
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.
    '''

    def setUp(self):
        '''
        setup test environment for scrubber_02063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_scrubber_02063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_allnighter_02067(unittest.TestCase):
    '''
    testing play functionality of allnighter
    Cost: 0
    Text: click, trash: Gain click click.
    '''

    def setUp(self):
        '''
        setup test environment for allnighter_02067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_allnighter_02067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_inside_man_02068(unittest.TestCase):
    '''
    testing play functionality of inside_man
    Cost: 3
    Text: 2 recurring credits Use these credits to install hardware.
    '''

    def setUp(self):
        '''
        setup test environment for inside_man_02068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_inside_man_02068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_underworld_contact_02069(unittest.TestCase):
    '''
    testing play functionality of underworld_contact
    Cost: 2
    Text: When your turn begins, gain 1 credit if you have at least 2 link.
    '''

    def setUp(self):
        '''
        setup test environment for underworld_contact_02069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_underworld_contact_02069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_xanadu_02082(unittest.TestCase):
    '''
    testing play functionality of xanadu
    Cost: 3
    Text: The rez cost of each piece of ice is increased by 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for xanadu_02082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_xanadu_02082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kati_jones_02091(unittest.TestCase):
    '''
    testing play functionality of kati_jones
    Cost: 2
    Text: You cannot use Kati Jones more than once per turn. click: Place 3 credits from the bank on Kati Jones. click: Take all credits from Kati Jones.
    '''

    def setUp(self):
        '''
        setup test environment for kati_jones_02091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_kati_jones_02091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_leak_reversal_02103(unittest.TestCase):
    '''
    testing play functionality of data_leak_reversal
    Cost: 0
    Text: Install only if you made a successful run on a central server this turn. If you are tagged, Data Leak Reversal gains "click: The Corp trashes the top card of R&D."
    '''

    def setUp(self):
        '''
        setup test environment for data_leak_reversal_02103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_data_leak_reversal_02103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mr_li_02105(unittest.TestCase):
    '''
    testing play functionality of mr_li
    Cost: 3
    Text: click: Draw 2 cards. When you do, add 1 of those cards to the bottom of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for mr_li_02105
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_mr_li_02105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_new_angeles_city_hall_02109(unittest.TestCase):
    '''
    testing play functionality of new_angeles_city_hall
    Cost: 1
    Text: 2 credits: Avoid 1 tag. Trash New Angeles City Hall when you steal an agenda.
    '''

    def setUp(self):
        '''
        setup test environment for new_angeles_city_hall_02109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_new_angeles_city_hall_02109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_professional_contacts_03049(unittest.TestCase):
    '''
    testing play functionality of professional_contacts
    Cost: 5
    Text: click: Gain 1 credit and draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for professional_contacts_03049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_professional_contacts_03049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_borrowed_satellite_03050(unittest.TestCase):
    '''
    testing play functionality of borrowed_satellite
    Cost: 3
    Text: +1 link Your maximum hand size is increased by 1.
    '''

    def setUp(self):
        '''
        setup test environment for borrowed_satellite_03050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_borrowed_satellite_03050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ice_analyzer_03051(unittest.TestCase):
    '''
    testing play functionality of ice_analyzer
    Cost: 0
    Text: Whenever the Corp rezzes a piece of ice, place 1 credit on Ice Analyzer. You may use credits on Ice Analyzer to install programs.
    '''

    def setUp(self):
        '''
        setup test environment for ice_analyzer_03051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_ice_analyzer_03051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_daily_casts_03053(unittest.TestCase):
    '''
    testing play functionality of daily_casts
    Cost: 3
    Text: When you install this resource, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for daily_casts_03053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_daily_casts_03053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_same_old_thing_03054(unittest.TestCase):
    '''
    testing play functionality of same_old_thing
    Cost: 0
    Text: click, click, trash: Play an event from your heap (paying its play cost).
    '''

    def setUp(self):
        '''
        setup test environment for same_old_thing_03054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_same_old_thing_03054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_source_03055(unittest.TestCase):
    '''
    testing play functionality of the_source
    Cost: 2
    Text: The advancement requirement of all agendas is increased by 1. As an additional cost to steal an agenda, you must pay 3 credits. Trash The Source when an agenda is scored or stolen.
    '''

    def setUp(self):
        '''
        setup test environment for the_source_03055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_source_03055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_motivation_04008(unittest.TestCase):
    '''
    testing play functionality of motivation
    Cost: 0
    Text: When your turn begins, you may look at the top card of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for motivation_04008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_motivation_04008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_john_masanori_04009(unittest.TestCase):
    '''
    testing play functionality of john_masanori
    Cost: 2
    Text: The first time you make a successful run each turn, draw 1 card. The first time you make an unsuccessful run each turn, take 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for john_masanori_04009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_john_masanori_04009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hard_at_work_04023(unittest.TestCase):
    '''
    testing play functionality of hard_at_work
    Cost: 5
    Text: When your turn begins, gain 2 credits and lose click.
    '''

    def setUp(self):
        '''
        setup test environment for hard_at_work_04023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_hard_at_work_04023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_grifter_04046(unittest.TestCase):
    '''
    testing play functionality of grifter
    Cost: 2
    Text: When your turn ends, gain 1 credit if you made a successful run this turn; otherwise, trash Grifter.
    '''

    def setUp(self):
        '''
        setup test environment for grifter_04046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_grifter_04046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_woman_in_the_red_dress_04048(unittest.TestCase):
    '''
    testing play functionality of woman_in_the_red_dress
    Cost: 3
    Text: When your turn begins, reveal the top card of R&D. The Corp may draw that card.
    '''

    def setUp(self):
        '''
        setup test environment for woman_in_the_red_dress_04048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_woman_in_the_red_dress_04048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_raymond_flint_04049(unittest.TestCase):
    '''
    testing play functionality of raymond_flint
    Cost: 2
    Text: Whenever the Corp takes bad publicity, breach HQ. You cannot access cards in the root of HQ during this breach. trash: Expose 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for raymond_flint_04049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_raymond_flint_04049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_activist_support_04062(unittest.TestCase):
    '''
    testing play functionality of activist_support
    Cost: 1
    Text: When the Corp's turn begins, take 1 tag if you have no tags. When your turn begins, give the Corp 1 bad publicity if they have no bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for activist_support_04062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_activist_support_04062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_starlight_crusade_funding_04069(unittest.TestCase):
    '''
    testing play functionality of starlight_crusade_funding
    Cost: 1
    Text: When your turn begins, lose click. Ignore any additional costs on each double event you play.
    '''

    def setUp(self):
        '''
        setup test environment for starlight_crusade_funding_04069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_starlight_crusade_funding_04069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tallie_perrault_04083(unittest.TestCase):
    '''
    testing play functionality of tallie_perrault
    Cost: 2
    Text: Whenever a gray ops or black ops operation is trashed after resolving, you may give the Corp 1 bad publicity and take 1 tag. trash: Draw 1 card for each bad publicity the Corp has.
    '''

    def setUp(self):
        '''
        setup test environment for tallie_perrault_04083
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_tallie_perrault_04083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fall_guy_04106(unittest.TestCase):
    '''
    testing play functionality of fall_guy
    Cost: 0
    Text: trash: Prevent another installed resource from being trashed. trash: Gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for fall_guy_04106
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_fall_guy_04106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_security_testing_05048(unittest.TestCase):
    '''
    testing play functionality of security_testing
    Cost: 0
    Text: When your turn begins, you may choose a server. The first time each turn you make a successful run on the chosen server, instead of breaching it, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for security_testing_05048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_security_testing_05048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_theophilius_bagbiter_05049(unittest.TestCase):
    '''
    testing play functionality of theophilius_bagbiter
    Cost: 3
    Text: When you install Theophilius Bagbiter, lose all credits in your credit pool. Your maximum hand size is equal to the number of credits in your credit pool.
    '''

    def setUp(self):
        '''
        setup test environment for theophilius_bagbiter_05049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_theophilius_bagbiter_05049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_trimaf_contact_05050(unittest.TestCase):
    '''
    testing play functionality of trimaf_contact
    Cost: 2
    Text: You cannot use Tri-maf Contact more than once per turn. click: Gain 2 credits. When Tri-maf Contact is trashed, suffer 3 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for trimaf_contact_05050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_trimaf_contact_05050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_oracle_may_05054(unittest.TestCase):
    '''
    testing play functionality of oracle_may
    Cost: 1
    Text: You cannot use Oracle May more than once per turn. click: Name a card type. Reveal the top card of your stack. If the revealed card is of the named type, draw it and gain 2 credits. Otherwise, trash it.
    '''

    def setUp(self):
        '''
        setup test environment for oracle_may_05054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_oracle_may_05054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_donut_taganes_05055(unittest.TestCase):
    '''
    testing play functionality of donut_taganes
    Cost: 3
    Text: The play cost of operations and events is increased by 1.
    '''

    def setUp(self):
        '''
        setup test environment for donut_taganes_05055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_donut_taganes_05055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_power_tap_06016(unittest.TestCase):
    '''
    testing play functionality of power_tap
    Cost: 2
    Text: Gain 1 credit whenever a trace is initiated.
    '''

    def setUp(self):
        '''
        setup test environment for power_tap_06016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_power_tap_06016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_eden_shard_06020(unittest.TestCase):
    '''
    testing play functionality of eden_shard
    Cost: 7
    Text: Whenever you make a successful run on R&D, instead of breaching R&D, you may install this resource from your grip, ignoring all costs. trash: The Corp draws 2 cards. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for eden_shard_06020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_eden_shard_06020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ghost_runner_06040(unittest.TestCase):
    '''
    testing play functionality of ghost_runner
    Cost: 1
    Text: Place 3 credits on Ghost Runner when it is installed. When there are no credits left on Ghost Runner, trash it. You can use the credits on Ghost Runner during a run.
    '''

    def setUp(self):
        '''
        setup test environment for ghost_runner_06040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_ghost_runner_06040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_duggars_06054(unittest.TestCase):
    '''
    testing play functionality of duggars
    Cost: 2
    Text: click,click,click,click: Draw 10 cards.
    '''

    def setUp(self):
        '''
        setup test environment for duggars_06054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_duggars_06054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_supplier_06056(unittest.TestCase):
    '''
    testing play functionality of the_supplier
    Cost: 3
    Text: click: Host a resource or piece of hardware from your grip on The Supplier. When your turn begins, you may install a hosted card, lowering the install cost by 2.
    '''

    def setUp(self):
        '''
        setup test environment for the_supplier_06056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_supplier_06056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_order_of_sol_06058(unittest.TestCase):
    '''
    testing play functionality of order_of_sol
    Cost: 2
    Text: The first time you have no credits in your credit pool each turn, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for order_of_sol_06058
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_order_of_sol_06058()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hades_shard_06059(unittest.TestCase):
    '''
    testing play functionality of hades_shard
    Cost: 7
    Text: Whenever you make a successful run on Archives, instead of breaching Archives, you may install this resource from your grip, ignoring all costs. trash: Breach Archives. You cannot access cards in the root of Archives during this breach. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for hades_shard_06059
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_hades_shard_06059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rachel_beckman_06060(unittest.TestCase):
    '''
    testing play functionality of rachel_beckman
    Cost: 8
    Text: You get +1 allotted click for each of your turns. If you are tagged, trash this resource.
    '''

    def setUp(self):
        '''
        setup test environment for rachel_beckman_06060
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_rachel_beckman_06060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fester_06075(unittest.TestCase):
    '''
    testing play functionality of fester
    Cost: 1
    Text: Whenever the Corp purges virus counters, if the Corp has at least 2 credits, they lose 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for fester_06075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_fester_06075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_angel_arena_06080(unittest.TestCase):
    '''
    testing play functionality of angel_arena
    Cost: None
    Text: Place X power counters on Angel Arena when it is installed. When there are no power counters left on Angel Arena, trash it. Hosted power counter: Reveal the top card of your stack. You may add that card to the bottom of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for angel_arena_06080
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_angel_arena_06080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_zona_sul_shipping_06097(unittest.TestCase):
    '''
    testing play functionality of zona_sul_shipping
    Cost: 2
    Text: Place 1 credit on Zona Sul Shipping when your turn begins. click: Take all credits from Zona Sul Shipping. Trash Zona Sul Shipping if you are tagged.
    '''

    def setUp(self):
        '''
        setup test environment for zona_sul_shipping_06097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_zona_sul_shipping_06097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_utopia_shard_06100(unittest.TestCase):
    '''
    testing play functionality of utopia_shard
    Cost: 7
    Text: Whenever you make a successful run on HQ, instead of breaching HQ, you may install this resource from your grip, ignoring all costs. trash: The Corp discards 2 cards from HQ at random. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for utopia_shard_06100
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_utopia_shard_06100()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_earthrise_hotel_06120(unittest.TestCase):
    '''
    testing play functionality of earthrise_hotel
    Cost: 4
    Text: When you install this resource, load 3 power counters onto it. When it is empty, trash it. When your turn begins, remove 1 hosted power counter and draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for earthrise_hotel_06120
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_earthrise_hotel_06120()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_human_first_07048(unittest.TestCase):
    '''
    testing play functionality of human_first
    Cost: 1
    Text: Whenever an agenda is scored or stolen, gain credits equal to the agenda points on that agenda.
    '''

    def setUp(self):
        '''
        setup test environment for human_first_07048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_human_first_07048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_investigative_journalism_07049(unittest.TestCase):
    '''
    testing play functionality of investigative_journalism
    Cost: 0
    Text: Install only if the Corp has at least 1 bad publicity. click,click,click,click,trash: Give the Corp 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for investigative_journalism_07049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_investigative_journalism_07049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sacrificial_clone_07050(unittest.TestCase):
    '''
    testing play functionality of sacrificial_clone
    Cost: 3
    Text: trash: Prevent all damage. Trash all installed hardware, all installed non-virtual resources, and all cards in your grip. Lose all credits in your credit pool. Remove all tags.
    '''

    def setUp(self):
        '''
        setup test environment for sacrificial_clone_07050
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_sacrificial_clone_07050()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_stim_dealer_07051(unittest.TestCase):
    '''
    testing play functionality of stim_dealer
    Cost: 4
    Text: When your turn begins, if there are 2 or more hosted power counters, remove all of them and suffer 1 core damage. This damage cannot be prevented. Otherwise, place 1 power counter on this resource and gain click.
    '''

    def setUp(self):
        '''
        setup test environment for stim_dealer_07051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_stim_dealer_07051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_virus_breeding_ground_07052(unittest.TestCase):
    '''
    testing play functionality of virus_breeding_ground
    Cost: 2
    Text: When your turn begins, place 1 virus counter on Virus Breeding Ground. click: Move 1 virus counter on Virus Breeding Ground to another card with at least 1 virus counter on it.
    '''

    def setUp(self):
        '''
        setup test environment for virus_breeding_ground_07052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_virus_breeding_ground_07052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_folding_07055(unittest.TestCase):
    '''
    testing play functionality of data_folding
    Cost: 3
    Text: When your turn begins, gain 1 credit if you have 2 or more unused MU.
    '''

    def setUp(self):
        '''
        setup test environment for data_folding_07055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_data_folding_07055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paige_piper_08002(unittest.TestCase):
    '''
    testing play functionality of paige_piper
    Cost: 0
    Text: The first time you install a card each turn (including Paige Piper), you may search your stack for any number of copies of that card and add them to your heap. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for paige_piper_08002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_paige_piper_08002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_adjusted_chronotype_08003(unittest.TestCase):
    '''
    testing play functionality of adjusted_chronotype
    Cost: 3
    Text: The first time each turn you lose click except by paying the trigger cost of a paid ability, gain click.
    '''

    def setUp(self):
        '''
        setup test environment for adjusted_chronotype_08003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_adjusted_chronotype_08003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_enhanced_vision_08005(unittest.TestCase):
    '''
    testing play functionality of enhanced_vision
    Cost: 1
    Text: The first time you make a successful run each turn, the Corp reveals 1 card at random from HQ.
    '''

    def setUp(self):
        '''
        setup test environment for enhanced_vision_08005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_enhanced_vision_08005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gene_conditioning_shoppe_08006(unittest.TestCase):
    '''
    testing play functionality of gene_conditioning_shoppe
    Cost: 2
    Text: Genetics also trigger the second time each turn their trigger condition is met.
    '''

    def setUp(self):
        '''
        setup test environment for gene_conditioning_shoppe_08006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_gene_conditioning_shoppe_08006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_synthetic_blood_08007(unittest.TestCase):
    '''
    testing play functionality of synthetic_blood
    Cost: 3
    Text: The first time you take damage each turn, draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for synthetic_blood_08007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_synthetic_blood_08007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_symmetrical_visage_08009(unittest.TestCase):
    '''
    testing play functionality of symmetrical_visage
    Cost: 2
    Text: The first time you spend click to draw 1 card (not through a card ability) each turn, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for symmetrical_visage_08009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_symmetrical_visage_08009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_offcampus_apartment_08022(unittest.TestCase):
    '''
    testing play functionality of offcampus_apartment
    Cost: 0
    Text: Off-Campus Apartment can host any number of connections. Whenever you install a connection on Off-Campus Apartment, draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for offcampus_apartment_08022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_offcampus_apartment_08022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_london_library_08029(unittest.TestCase):
    '''
    testing play functionality of london_library
    Cost: 3
    Text: Trash all programs hosted on London Library when your turn ends. click: Install a non-virus program from your grip on London Library, ignoring the install cost. click: Add a program on London Library to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for london_library_08029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_london_library_08029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tyson_observatory_08030(unittest.TestCase):
    '''
    testing play functionality of tyson_observatory
    Cost: 2
    Text: click, click: Search your stack for a piece of hardware, reveal it, and add it to your grip. Shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for tyson_observatory_08030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_tyson_observatory_08030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_beach_party_08031(unittest.TestCase):
    '''
    testing play functionality of beach_party
    Cost: 0
    Text: When your turn begins, lose click. Your maximum hand size is increased by 5.
    '''

    def setUp(self):
        '''
        setup test environment for beach_party_08031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_beach_party_08031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chrome_parlor_08044(unittest.TestCase):
    '''
    testing play functionality of chrome_parlor
    Cost: 1
    Text: Interrupt -> Whenever you would suffer damage from a "when installed" ability on a piece of cybernetic hardware, prevent all of that damage.
    '''

    def setUp(self):
        '''
        setup test environment for chrome_parlor_08044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_chrome_parlor_08044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_street_peddler_08062(unittest.TestCase):
    '''
    testing play functionality of street_peddler
    Cost: 0
    Text: When you install Street Peddler, host the top 3 cards of your stack facedown on Street Peddler (you may look at these cards at any time). trash: Install 1 card hosted on Street Peddler, lowering its install cost by 1.
    '''

    def setUp(self):
        '''
        setup test environment for street_peddler_08062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_street_peddler_08062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gang_sign_08067(unittest.TestCase):
    '''
    testing play functionality of gang_sign
    Cost: 1
    Text: Whenever the Corp scores an agenda, breach HQ. You cannot access cards in the root of HQ during this breach.
    '''

    def setUp(self):
        '''
        setup test environment for gang_sign_08067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_gang_sign_08067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_muertos_gang_member_08068(unittest.TestCase):
    '''
    testing play functionality of muertos_gang_member
    Cost: 0
    Text: When you install Muertos Gang Member, the Corp must derez a card. When Muertos Gang Member is uninstalled, the Corp may rez a card, ignoring the rez cost. trash: Draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for muertos_gang_member_08068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_muertos_gang_member_08068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_spoilers_08082(unittest.TestCase):
    '''
    testing play functionality of spoilers
    Cost: 1
    Text: Whenever the Corp scores an agenda, they trash the top card of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for spoilers_08082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_spoilers_08082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_drug_dealer_08083(unittest.TestCase):
    '''
    testing play functionality of drug_dealer
    Cost: 1
    Text: When your turn begins, lose 1 credit. When the Corp's turn begins, draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for drug_dealer_08083
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_drug_dealer_08083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rolodex_08084(unittest.TestCase):
    '''
    testing play functionality of rolodex
    Cost: 0
    Text: When you install Rolodex, look at the top 5 cards of your stack and arrange them in any order. When Rolodex is trashed, trash the top 3 cards of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for rolodex_08084
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_rolodex_08084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fan_site_08085(unittest.TestCase):
    '''
    testing play functionality of fan_site
    Cost: 0
    Text: Whenever the Corp scores an agenda, add Fan Site to your score area as an agenda worth 0 agenda points.
    '''

    def setUp(self):
        '''
        setup test environment for fan_site_08085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_fan_site_08085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_film_critic_08086(unittest.TestCase):
    '''
    testing play functionality of film_critic
    Cost: 1
    Text: Film Critic can host a single agenda. Whenever you access an agenda, you may host that agenda on Film Critic (the agenda is no longer being accessed and is uninstalled). click,click: Add an agenda hosted on Film Critic to your score area.
    '''

    def setUp(self):
        '''
        setup test environment for film_critic_08086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_film_critic_08086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paparazzi_08087(unittest.TestCase):
    '''
    testing play functionality of paparazzi
    Cost: 0
    Text: You are tagged. Prevent all meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for paparazzi_08087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_paparazzi_08087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ddos_08103(unittest.TestCase):
    '''
    testing play functionality of ddos
    Cost: 3
    Text: trash: The Corp cannot rez the outermost piece of ice during a run on any server this turn.
    '''

    def setUp(self):
        '''
        setup test environment for ddos_08103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_ddos_08103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wireless_net_pavilion_08108(unittest.TestCase):
    '''
    testing play functionality of wireless_net_pavilion
    Cost: 1
    Text: As an additional cost to take the basic action to trash 1 installed resource, the Corp must pay 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for wireless_net_pavilion_08108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_wireless_net_pavilion_08108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hunting_grounds_09035(unittest.TestCase):
    '''
    testing play functionality of hunting_grounds
    Cost: 2
    Text: Once per turn, prevent a "when encountered" ability on a piece of ice. trash: Install the top 3 cards of your stack facedown.
    '''

    def setUp(self):
        '''
        setup test environment for hunting_grounds_09035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_hunting_grounds_09035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_wasteland_09036(unittest.TestCase):
    '''
    testing play functionality of wasteland
    Cost: 2
    Text: The first time each turn you trash 1 of your installed cards, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for wasteland_09036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_wasteland_09036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_always_be_running_09041(unittest.TestCase):
    '''
    testing play functionality of always_be_running
    Cost: 0
    Text: The first click you spend each turn must be spent to play a run event or take the basic action to run a server. Lose click click: Break 1 subroutine. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for always_be_running_09041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_always_be_running_09041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dr_lovegood_09042(unittest.TestCase):
    '''
    testing play functionality of dr_lovegood
    Cost: 2
    Text: When your turn begins, choose 1 of your installed cards. That card loses its printed abilities for the remainder of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for dr_lovegood_09042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_dr_lovegood_09042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_neutralize_all_threats_09043(unittest.TestCase):
    '''
    testing play functionality of neutralize_all_threats
    Cost: 0
    Text: The first time each turn you access a card with a trash cost, reveal it. You must trash that card by paying its trash cost, if able. Whenever you breach HQ, access 1 additional card.
    '''

    def setUp(self):
        '''
        setup test environment for neutralize_all_threats_09043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_neutralize_all_threats_09043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_safety_first_09044(unittest.TestCase):
    '''
    testing play functionality of safety_first
    Cost: 0
    Text: Your maximum hand size is reduced by 2. When your turn ends, draw 1 card if you do not have cards in your grip equal to or greater than your maximum hand size.
    '''

    def setUp(self):
        '''
        setup test environment for safety_first_09044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_safety_first_09044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_globalsec_security_clearance_09051(unittest.TestCase):
    '''
    testing play functionality of globalsec_security_clearance
    Cost: 2
    Text: Install only if you have at least 2 link. When your turn begins, you may lose click. If you do, look at the top card of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for globalsec_security_clearance_09051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_globalsec_security_clearance_09051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_jak_sinclair_09052(unittest.TestCase):
    '''
    testing play functionality of jak_sinclair
    Cost: 3
    Text: Reduce the cost to install Jak Sinclair by 1 for each link you have. When your turn begins, you may make a run. You cannot use programs during this run.
    '''

    def setUp(self):
        '''
        setup test environment for jak_sinclair_09052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_jak_sinclair_09052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_technical_writer_09055(unittest.TestCase):
    '''
    testing play functionality of technical_writer
    Cost: 0
    Text: Whenever you install a piece of hardware or a program, place 1 credit from the bank on Technical Writer. click,trash: Take all credits from Technical Writer.
    '''

    def setUp(self):
        '''
        setup test environment for technical_writer_09055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_technical_writer_09055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_street_magic_10003(unittest.TestCase):
    '''
    testing play functionality of street_magic
    Cost: 0
    Text: Unbroken subroutines resolve in the order of your choice.
    '''

    def setUp(self):
        '''
        setup test environment for street_magic_10003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_street_magic_10003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_artist_colony_10009(unittest.TestCase):
    '''
    testing play functionality of artist_colony
    Cost: 0
    Text: Forfeit 1 agenda: Search your stack for 1 program, resource, or piece of hardware. Install that card.
    '''

    def setUp(self):
        '''
        setup test environment for artist_colony_10009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_artist_colony_10009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chatterjee_university_10010(unittest.TestCase):
    '''
    testing play functionality of chatterjee_university
    Cost: 1
    Text: click: Place 1 power counter on Chatterjee University. click: Install a program from your grip, lowering the install cost by 1 for each power counter on Chatterjee University. Remove 1 hosted power counter.
    '''

    def setUp(self):
        '''
        setup test environment for chatterjee_university_10010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_chatterjee_university_10010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tech_trader_10023(unittest.TestCase):
    '''
    testing play functionality of tech_trader
    Cost: 1
    Text: Whenever you use a trash ability, gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for tech_trader_10023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_tech_trader_10023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_political_operative_10043(unittest.TestCase):
    '''
    testing play functionality of political_operative
    Cost: 1
    Text: Install only if you made a successful run on HQ this turn. trash, X credits: Trash 1 rezzed card with trash cost equal to X.
    '''

    def setUp(self):
        '''
        setup test environment for political_operative_10043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_political_operative_10043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_akshara_sareen_10046(unittest.TestCase):
    '''
    testing play functionality of akshara_sareen
    Cost: 0
    Text: Each player gets +1 allotted click for each of their turns.
    '''

    def setUp(self):
        '''
        setup test environment for akshara_sareen_10046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_akshara_sareen_10046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_councilman_10047(unittest.TestCase):
    '''
    testing play functionality of councilman
    Cost: 0
    Text: Whenever the Corp rezzes an asset or upgrade, you may pay credits equal to its rez cost and trash Councilman. If you do, derez that asset or upgrade. The Corp cannot rez it for the remainder of this turn.
    '''

    def setUp(self):
        '''
        setup test environment for councilman_10047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_councilman_10047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_salsette_slums_10059(unittest.TestCase):
    '''
    testing play functionality of salsette_slums
    Cost: 2
    Text: Access -> Pay the trash cost of the card you are accessing: Remove it from the game. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for salsette_slums_10059
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_salsette_slums_10059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_patron_10063(unittest.TestCase):
    '''
    testing play functionality of patron
    Cost: 3
    Text: When your turn begins, you may choose a server. The first time each turn you make a successful run on the chosen server, instead of breaching it, draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for patron_10063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_patron_10063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bazaar_10065(unittest.TestCase):
    '''
    testing play functionality of bazaar
    Cost: 1
    Text: Whenever you install a piece of hardware from your grip, you may install another copy of that hardware from your grip (paying all costs).
    '''

    def setUp(self):
        '''
        setup test environment for bazaar_10065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_bazaar_10065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_emptied_mind_10078(unittest.TestCase):
    '''
    testing play functionality of emptied_mind
    Cost: 0
    Text: When your turn begins, gain click if you have no cards in your grip.
    '''

    def setUp(self):
        '''
        setup test environment for emptied_mind_10078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_emptied_mind_10078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_liberated_chela_10081(unittest.TestCase):
    '''
    testing play functionality of liberated_chela
    Cost: 0
    Text: click click click click click, forfeit an agenda: The Corp may forfeit an agenda to remove this resource from the game. If they do not, add this resource to your score area as an agenda worth 2 agenda points.
    '''

    def setUp(self):
        '''
        setup test environment for liberated_chela_10081
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_liberated_chela_10081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_temple_of_the_liberated_mind_10082(unittest.TestCase):
    '''
    testing play functionality of temple_of_the_liberated_mind
    Cost: 2
    Text: click: Place 1 power counter on Temple of the Liberated Mind. Hosted power counter: Gain click. Use this ability only on your turn and only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for temple_of_the_liberated_mind_10082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_temple_of_the_liberated_mind_10082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_guru_davinder_10084(unittest.TestCase):
    '''
    testing play functionality of guru_davinder
    Cost: 1
    Text: Prevent all net and meat damage. Whenever Guru Davinder prevents at least 1 net or meat damage, trash him unless you pay 4 credits.
    '''

    def setUp(self):
        '''
        setup test environment for guru_davinder_10084
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_guru_davinder_10084()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_turning_wheel_10085(unittest.TestCase):
    '''
    testing play functionality of the_turning_wheel
    Cost: 2
    Text: Whenever a run on HQ or R&D ends, place 1 power counter on this resource if you stole no agendas during that run. 2 hosted power counters: Choose HQ or R&D. For the remainder of this run, access 1 additional card whenever you breach that server.
    '''

    def setUp(self):
        '''
        setup test environment for the_turning_wheel_10085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_turning_wheel_10085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bhagat_10098(unittest.TestCase):
    '''
    testing play functionality of bhagat
    Cost: 3
    Text: The first time you make a successful run on HQ each turn, force the Corp to trash the top card of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for bhagat_10098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_bhagat_10098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_black_file_10099(unittest.TestCase):
    '''
    testing play functionality of the_black_file
    Cost: 5
    Text: The Corp cannot win the game except if you are flatlined. When your turn begins, place 1 power counter on this resource. If there are 3 or more hosted power counters, remove this resource from the game. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for the_black_file_10099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_black_file_10099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hernando_cortez_11004(unittest.TestCase):
    '''
    testing play functionality of hernando_cortez
    Cost: 2
    Text: If the Corp has at least 10 credits, as an additional cost to rez each piece of ice, the Corp must spend credits equal to the number of subroutines on that ice.
    '''

    def setUp(self):
        '''
        setup test environment for hernando_cortez_11004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_hernando_cortez_11004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_temujin_contract_11026(unittest.TestCase):
    '''
    testing play functionality of temujin_contract
    Cost: 4
    Text: Choose a server and place 20 credits from the bank on Temujin Contract when you install it. When there are no credits left on Temujin Contract, trash it. Whenever you make a successful run on the chosen server, take 4 credits from Temujin Contract.
    '''

    def setUp(self):
        '''
        setup test environment for temujin_contract_11026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_temujin_contract_11026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_algo_trading_11029(unittest.TestCase):
    '''
    testing play functionality of algo_trading
    Cost: 0
    Text: When your turn begins, you may move up to 3 credits from your credit pool to Algo Trading. When your turn begins, place 2 credits on Algo Trading from the bank if there are at least 6 credits on it. click,trash: Take all credits from Algo Trading.
    '''

    def setUp(self):
        '''
        setup test environment for algo_trading_11029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_algo_trading_11029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_beth_kilrainchang_11030(unittest.TestCase):
    '''
    testing play functionality of beth_kilrainchang
    Cost: 2
    Text: If the Corp has 5-9 credits when your turn begins, gain 1 credit. If the Corp has 10-14 credits when your turn begins, draw 1 card. If the Corp has at least 15 credits when your turn begins, gain click.
    '''

    def setUp(self):
        '''
        setup test environment for beth_kilrainchang_11030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_beth_kilrainchang_11030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_net_mercur_11046(unittest.TestCase):
    '''
    testing play functionality of net_mercur
    Cost: 3
    Text: The first time you spend at least 1 credit from a stealth card each run, place 1 credit on Net Mercur or draw 1 card. Use credits on Net Mercur for anything.
    '''

    def setUp(self):
        '''
        setup test environment for net_mercur_11046
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_net_mercur_11046()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_find_the_truth_11047(unittest.TestCase):
    '''
    testing play functionality of find_the_truth
    Cost: 0
    Text: Whenever you draw a card, reveal that card. The first time each turn you make a successful run, you may look at the top card of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for find_the_truth_11047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_find_the_truth_11047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_first_responders_11048(unittest.TestCase):
    '''
    testing play functionality of first_responders
    Cost: 2
    Text: 2 credits: Draw 1 card. Use this ability only if you have suffered damage from a Corp card ability this turn.
    '''

    def setUp(self):
        '''
        setup test environment for first_responders_11048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_first_responders_11048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_blockade_runner_11065(unittest.TestCase):
    '''
    testing play functionality of blockade_runner
    Cost: 1
    Text: click,click: Draw 3 cards. Shuffle 1 card from your grip into your stack.
    '''

    def setUp(self):
        '''
        setup test environment for blockade_runner_11065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_blockade_runner_11065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_citadel_sanctuary_11070(unittest.TestCase):
    '''
    testing play functionality of citadel_sanctuary
    Cost: 2
    Text: If you are tagged when your turn ends, force the Corp to "Trace[1]. If unsuccessful, the Runner removes 1 tag." trash,trash all cards in your grip: Prevent all meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for citadel_sanctuary_11070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_citadel_sanctuary_11070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aaron_marron_11106(unittest.TestCase):
    '''
    testing play functionality of aaron_marron
    Cost: 2
    Text: Whenever an agenda is scored or stolen, place 2 power counters on Aaron Marron. Hosted power counter: Remove 1 tag and draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for aaron_marron_11106
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_aaron_marron_11106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_archivist_12003(unittest.TestCase):
    '''
    testing play functionality of the_archivist
    Cost: 1
    Text: +1 link Whenever the Corp scores an initiative or security agenda, force the Corp to "Trace[1]. If unsuccessful, take 1 bad publicity."
    '''

    def setUp(self):
        '''
        setup test environment for the_archivist_12003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_archivist_12003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_biomodeled_network_12006(unittest.TestCase):
    '''
    testing play functionality of biomodeled_network
    Cost: 1
    Text: trash: Prevent all but 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for biomodeled_network_12006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_biomodeled_network_12006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_network_exchange_12007(unittest.TestCase):
    '''
    testing play functionality of network_exchange
    Cost: 2
    Text: The install cost of each piece of ice that is not installed in the innermost position is increased by 1.
    '''

    def setUp(self):
        '''
        setup test environment for network_exchange_12007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_network_exchange_12007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_clan_vengeance_12022(unittest.TestCase):
    '''
    testing play functionality of clan_vengeance
    Cost: 3
    Text: Whenever you suffer any amount of damage, place 1 power counter on Clan Vengeance. trash: Trash 1 card from HQ at random for each power counter on Clan Vengeance.
    '''

    def setUp(self):
        '''
        setup test environment for clan_vengeance_12022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_clan_vengeance_12022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_counter_surveillance_12023(unittest.TestCase):
    '''
    testing play functionality of counter_surveillance
    Cost: 1
    Text: click, trash: Run any server. If successful, instead of breaching the attacked server, pay X credits if able, where X is equal to the number of tags you have. If you do, choose a number less than or equal to X. Access that many cards in and/or in the root of the attacked server. (If you cannot pay, you will not access anything.)
    '''

    def setUp(self):
        '''
        setup test environment for counter_surveillance_12023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_counter_surveillance_12023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aeneas_informant_12044(unittest.TestCase):
    '''
    testing play functionality of aeneas_informant
    Cost: 0
    Text: Whenever you access a card with a trash cost not in Archives and do not trash it, you may reveal it and gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for aeneas_informant_12044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_aeneas_informant_12044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rosetta_20_12045(unittest.TestCase):
    '''
    testing play functionality of rosetta_20
    Cost: 3
    Text: click, remove an installed program from the game: Search your stack for a non-virus program, shuffle your stack, then install that program, lowering the install cost by the cost of the program removed from the game.
    '''

    def setUp(self):
        '''
        setup test environment for rosetta_20_12045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_rosetta_20_12045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dadiana_chacon_12049(unittest.TestCase):
    '''
    testing play functionality of dadiana_chacon
    Cost: 0
    Text: When your turn begins, gain 1 credit if you have fewer than 6 credits. Whenever you have 0 credits, trash Dadiana Chacon and take 3 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for dadiana_chacon_12049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_dadiana_chacon_12049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_jarogniew_mercs_12062(unittest.TestCase):
    '''
    testing play functionality of jarogniew_mercs
    Cost: 0
    Text: When you install Jarogniew Mercs, take 1 tag. Place 3 power counters on Jarogniew Mercs, and 1 additional power counter for each tag you have. When there are no power counters left on Jarogniew Mercs, trash it. The Corp cannot trash Jarogniew Mercs while there is another resource installed. Hosted power counter: Prevent 1 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for jarogniew_mercs_12062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_jarogniew_mercs_12062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bug_out_bag_12064(unittest.TestCase):
    '''
    testing play functionality of bug_out_bag
    Cost: None
    Text: When you install this resource, place X power counters on it. When your turn ends, if you have no cards in your grip, draw 1 card for each hosted power counter, then trash this resource.
    '''

    def setUp(self):
        '''
        setup test environment for bug_out_bag_12064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_bug_out_bag_12064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_keros_mcintyre_12065(unittest.TestCase):
    '''
    testing play functionality of keros_mcintyre
    Cost: 2
    Text: The first time you derez a piece of ice each turn, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for keros_mcintyre_12065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_keros_mcintyre_12065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bloo_moose_12089(unittest.TestCase):
    '''
    testing play functionality of bloo_moose
    Cost: 4
    Text: When your turn begins, you may remove 1 card in the heap from the game. If you do, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for bloo_moose_12089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_bloo_moose_12089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_salvaged_vanadis_armory_12103(unittest.TestCase):
    '''
    testing play functionality of salvaged_vanadis_armory
    Cost: 0
    Text: trash: The Corp trashes the top X cards of R&D. X is equal to the amount of damage you have suffered this turn. Use this ability only during the next paid ability window after suffering any amount of damage.
    '''

    def setUp(self):
        '''
        setup test environment for salvaged_vanadis_armory_12103
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_salvaged_vanadis_armory_12103()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_caldera_12105(unittest.TestCase):
    '''
    testing play functionality of caldera
    Cost: 3
    Text: Interrupt -> 3 credits: Prevent 1 core damage or 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for caldera_12105
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_caldera_12105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dummy_box_12108(unittest.TestCase):
    '''
    testing play functionality of dummy_box
    Cost: 1
    Text: Trash a card from your grip: Prevent an installed card of the same type from being trashed by the Corp.
    '''

    def setUp(self):
        '''
        setup test environment for dummy_box_12108
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_dummy_box_12108()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_defector_12109(unittest.TestCase):
    '''
    testing play functionality of corporate_defector
    Cost: 0
    Text: Whenever the Corp draws a card with the basic action, reveal that card.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_defector_12109
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_corporate_defector_12109()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_charlatan_13010(unittest.TestCase):
    '''
    testing play functionality of charlatan
    Cost: 5
    Text: click click: Run any server. The first time you approach a rezzed piece of ice during this run, you may pay credits equal to the strength of that ice. If you do, when you encounter that ice after this approach, bypass it.
    '''

    def setUp(self):
        '''
        setup test environment for charlatan_13010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_charlatan_13010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_maxwell_james_13011(unittest.TestCase):
    '''
    testing play functionality of maxwell_james
    Cost: 1
    Text: +1 link trash: Derez a piece of ice protecting a remote server. Use this ability only during the next paid ability window after a successful run on HQ ends.
    '''

    def setUp(self):
        '''
        setup test environment for maxwell_james_13011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_maxwell_james_13011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_levy_advanced_research_lab_13021(unittest.TestCase):
    '''
    testing play functionality of levy_advanced_research_lab
    Cost: 4
    Text: click: Reveal the top 4 cards of your stack. If any of those cards are programs, you may add 1 to your grip. Add the rest of the cards to the bottom of your stack in any order.
    '''

    def setUp(self):
        '''
        setup test environment for levy_advanced_research_lab_13021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_levy_advanced_research_lab_13021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_laguna_velasco_district_13022(unittest.TestCase):
    '''
    testing play functionality of laguna_velasco_district
    Cost: 5
    Text: Whenever you take the basic action to draw cards, increase the number of cards you draw by 1.
    '''

    def setUp(self):
        '''
        setup test environment for laguna_velasco_district_13022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_laguna_velasco_district_13022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_officer_frank_13024(unittest.TestCase):
    '''
    testing play functionality of officer_frank
    Cost: 0
    Text: trash, 1 credit: The Corp trashes 2 cards from HQ at random. Use this ability only if you suffered meat damage this turn.
    '''

    def setUp(self):
        '''
        setup test environment for officer_frank_13024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_officer_frank_13024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dean_lister_13025(unittest.TestCase):
    '''
    testing play functionality of dean_lister
    Cost: 2
    Text: trash: Choose an icebreaker. Until the end of the run, that icebreaker has +1 strength for each card in your grip.
    '''

    def setUp(self):
        '''
        setup test environment for dean_lister_13025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_dean_lister_13025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_biometric_spoofing_13026(unittest.TestCase):
    '''
    testing play functionality of biometric_spoofing
    Cost: 2
    Text: trash: Prevent 2 damage.
    '''

    def setUp(self):
        '''
        setup test environment for biometric_spoofing_13026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_biometric_spoofing_13026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_shadow_net_13027(unittest.TestCase):
    '''
    testing play functionality of the_shadow_net
    Cost: 0
    Text: click, forfeit an agenda: Play an event from your heap, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for the_shadow_net_13027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_shadow_net_13027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_investigator_inez_delgado_14014(unittest.TestCase):
    '''
    testing play functionality of investigator_inez_delgado
    Cost: 0
    Text: When you win a game with Investigator Inez Delgado in your score area, reveal set 2. Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Expose all cards in a remote server. Use this only if you have stolean an agenda this turn.
    '''

    def setUp(self):
        '''
        setup test environment for investigator_inez_delgado_14014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_investigator_inez_delgado_14014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_investigator_inez_delgado_2_14015(unittest.TestCase):
    '''
    testing play functionality of investigator_inez_delgado_2
    Cost: 0
    Text: When you win a game with Investigator Inez Delgado in your score area, reveal set 5. Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Reveal the top 3 cards in R&D. Use this only if you have stolean an agenda this turn.
    '''

    def setUp(self):
        '''
        setup test environment for investigator_inez_delgado_2_14015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_investigator_inez_delgado_2_14015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_investigator_inez_delgado_3_14016(unittest.TestCase):
    '''
    testing play functionality of investigator_inez_delgado_3
    Cost: 0
    Text: When you win a game with Investigator Inez Delgado in your score area, reveal set 8. Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Reveal each card in HQ. Use this only if you have stolean an agenda this turn.
    '''

    def setUp(self):
        '''
        setup test environment for investigator_inez_delgado_3_14016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_investigator_inez_delgado_3_14016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_investigator_inez_delgado_4_14017(unittest.TestCase):
    '''
    testing play functionality of investigator_inez_delgado_4
    Cost: 0
    Text: Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Reveal each card in HQ and the top card of R&D. Use this only if you have stolean an agenda this turn.
    '''

    def setUp(self):
        '''
        setup test environment for investigator_inez_delgado_4_14017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_investigator_inez_delgado_4_14017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_shadow_team_14022(unittest.TestCase):
    '''
    testing play functionality of shadow_team
    Cost: 0
    Text: Whenever you draw a Shadow Team, immediately install it. Whenever you initiate a run, trash a card from your grip, if able. When you make a successful run on a central server, destroy Shadow Team.
    '''

    def setUp(self):
        '''
        setup test environment for shadow_team_14022
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_shadow_team_14022()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_masque_a_14024(unittest.TestCase):
    '''
    testing play functionality of the_masque_a
    Cost: 1
    Text: click,trash: Make a run and gain click. If successful, draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for the_masque_a_14024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_masque_a_14024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_masque_b_14025(unittest.TestCase):
    '''
    testing play functionality of the_masque_b
    Cost: 1
    Text: click,trash: Make a run and gain click. If that run is successful when it ends, you may immediately make another run on another server.
    '''

    def setUp(self):
        '''
        setup test environment for the_masque_b_14025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_masque_b_14025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ice_carver_20015(unittest.TestCase):
    '''
    testing play functionality of ice_carver
    Cost: 3
    Text: While you are encountering a piece of ice, it gets -1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for ice_carver_20015
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_ice_carver_20015()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_liberated_account_20016(unittest.TestCase):
    '''
    testing play functionality of liberated_account
    Cost: 6
    Text: When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for liberated_account_20016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_liberated_account_20016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_scrubber_20017(unittest.TestCase):
    '''
    testing play functionality of scrubber
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.
    '''

    def setUp(self):
        '''
        setup test environment for scrubber_20017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_scrubber_20017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_xanadu_20018(unittest.TestCase):
    '''
    testing play functionality of xanadu
    Cost: 3
    Text: The rez cost of each piece of ice is increased by 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for xanadu_20018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_xanadu_20018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bank_job_20033(unittest.TestCase):
    '''
    testing play functionality of bank_job
    Cost: 1
    Text: When you install this resource, load 8 credits on it. When it is empty, trash it. Whenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for bank_job_20033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_bank_job_20033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crash_space_20034(unittest.TestCase):
    '''
    testing play functionality of crash_space
    Cost: 2
    Text: 2 recurring credits Use these credits to pay for removing tags. trash: Prevent up to 3 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for crash_space_20034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_crash_space_20034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fall_guy_20035(unittest.TestCase):
    '''
    testing play functionality of fall_guy
    Cost: 0
    Text: trash: Prevent another installed resource from being trashed. trash: Gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for fall_guy_20035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_fall_guy_20035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mr_li_20036(unittest.TestCase):
    '''
    testing play functionality of mr_li
    Cost: 3
    Text: click: Draw 2 cards. When you do, add 1 of those cards to the bottom of your stack.
    '''

    def setUp(self):
        '''
        setup test environment for mr_li_20036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_mr_li_20036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aesops_pawnshop_20052(unittest.TestCase):
    '''
    testing play functionality of aesops_pawnshop
    Cost: 1
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for aesops_pawnshop_20052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_aesops_pawnshop_20052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_allnighter_20053(unittest.TestCase):
    '''
    testing play functionality of allnighter
    Cost: 0
    Text: click, trash: Gain click click.
    '''

    def setUp(self):
        '''
        setup test environment for allnighter_20053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_allnighter_20053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sacrificial_construct_20054(unittest.TestCase):
    '''
    testing play functionality of sacrificial_construct
    Cost: 0
    Text: trash: Prevent an installed program or an installed piece of hardware from being trashed.
    '''

    def setUp(self):
        '''
        setup test environment for sacrificial_construct_20054
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_sacrificial_construct_20054()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_armitage_codebusting_20059(unittest.TestCase):
    '''
    testing play functionality of armitage_codebusting
    Cost: 1
    Text: Place 12 credits from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it. click: Take 2 credits from Armitage Codebusting.
    '''

    def setUp(self):
        '''
        setup test environment for armitage_codebusting_20059
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_armitage_codebusting_20059()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_underworld_contact_20060(unittest.TestCase):
    '''
    testing play functionality of underworld_contact
    Cost: 2
    Text: When your turn begins, gain 1 credit if you have at least 2 link.
    '''

    def setUp(self):
        '''
        setup test environment for underworld_contact_20060
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_underworld_contact_20060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_lewi_guilherme_21005(unittest.TestCase):
    '''
    testing play functionality of lewi_guilherme
    Cost: 0
    Text: When your turn begins, either lose 1 credit or trash Lewi Guilherme. The Corp's maximum hand size is reduced by 1.
    '''

    def setUp(self):
        '''
        setup test environment for lewi_guilherme_21005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_lewi_guilherme_21005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_assimilator_21008(unittest.TestCase):
    '''
    testing play functionality of assimilator
    Cost: 5
    Text: click,click: Turn one of your facedown installed cards faceup. If that card is an event, trash it.
    '''

    def setUp(self):
        '''
        setup test environment for assimilator_21008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_assimilator_21008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kongamato_21027(unittest.TestCase):
    '''
    testing play functionality of kongamato
    Cost: 1
    Text: trash: Break the first subroutine on the encountered piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for kongamato_21027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_kongamato_21027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crypt_21043(unittest.TestCase):
    '''
    testing play functionality of crypt
    Cost: 0
    Text: Whenever you make a successful run on Archives, you may place 1 virus counter on Crypt. click, trash, 3 hosted virus counters: Search your stack for a virus program and install it (paying its install cost), then shuffle your stack.
    '''

    def setUp(self):
        '''
        setup test environment for crypt_21043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_crypt_21043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_no_one_home_21045(unittest.TestCase):
    '''
    testing play functionality of no_one_home
    Cost: 0
    Text: The first time you would take any number of tags or suffer any amount of net damage each turn, you may trash No One Home to force the Corp to "Trace[0]. If unsuccessful, the Runner avoids any number of tags or prevents any amount of net damage."
    '''

    def setUp(self):
        '''
        setup test environment for no_one_home_21045
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_no_one_home_21045()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gbahali_21047(unittest.TestCase):
    '''
    testing play functionality of gbahali
    Cost: 2
    Text: trash: Break the last subroutine on the encountered piece of ice.
    '''

    def setUp(self):
        '''
        setup test environment for gbahali_21047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_gbahali_21047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rogue_trading_21065(unittest.TestCase):
    '''
    testing play functionality of rogue_trading
    Cost: 0
    Text: Place 18 credits from the bank on Rogue Trading when it is installed. When there are no credits left on Rogue Trading, trash it. click, click: Take 6 credits from Rogue Trading and take 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for rogue_trading_21065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_rogue_trading_21065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_slipstream_21085(unittest.TestCase):
    '''
    testing play functionality of slipstream
    Cost: 0
    Text: Whenever you pass a rezzed piece of ice, you may trash this resource. If you do, choose 1 piece of ice protecting a central server in the same position as the passed ice. Move to that ice and approach it. You may jack out.
    '''

    def setUp(self):
        '''
        setup test environment for slipstream_21085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_slipstream_21085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_logic_bomb_21089(unittest.TestCase):
    '''
    testing play functionality of logic_bomb
    Cost: 0
    Text: trash: Bypass a piece of ice you are currently encountering. Lose any remaining clicks.
    '''

    def setUp(self):
        '''
        setup test environment for logic_bomb_21089
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_logic_bomb_21089()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_jackpot_21090(unittest.TestCase):
    '''
    testing play functionality of jackpot
    Cost: 0
    Text: When your turn begins, you may place 1 credit on Jackpot!. Whenever an agenda is added to your score area, you may take any number of credits from Jackpot!. If you do, trash Jackpot!.
    '''

    def setUp(self):
        '''
        setup test environment for jackpot_21090
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_jackpot_21090()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_pad_tap_21106(unittest.TestCase):
    '''
    testing play functionality of pad_tap
    Cost: 0
    Text: The first time the Corp gains credits through a card ability each turn, you may gain 1 credit. click, 3 credits: Trash PAD Tap. Only the Corp can use this ability.
    '''

    def setUp(self):
        '''
        setup test environment for pad_tap_21106
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_pad_tap_21106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reclaim_21107(unittest.TestCase):
    '''
    testing play functionality of reclaim
    Cost: 0
    Text: click, trash, trash a card from your grip: Install a program, piece of hardware, or virtual resource from your heap, paying its install cost.
    '''

    def setUp(self):
        '''
        setup test environment for reclaim_21107
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_reclaim_21107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kasi_string_21111(unittest.TestCase):
    '''
    testing play functionality of kasi_string
    Cost: 1
    Text: The first time each turn a successful run on a remote server ends, if you breached the server but stole no agendas, you may place 1 power counter on this resource. When this resource has 4 or more hosted power counters, add it to your score area as an agenda worth 1 agenda point.
    '''

    def setUp(self):
        '''
        setup test environment for kasi_string_21111
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_kasi_string_21111()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_district_99_22007(unittest.TestCase):
    '''
    testing play functionality of district_99
    Cost: 3
    Text: The first time each turn a program or a piece of hardware is trashed (from any location), you may place 1 power counter on District 99. click, 3 hosted power counters: Add a card that matches the faction of your identity from your heap to your grip.
    '''

    def setUp(self):
        '''
        setup test environment for district_99_22007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_district_99_22007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_thunder_art_gallery_22013(unittest.TestCase):
    '''
    testing play functionality of thunder_art_gallery
    Cost: 3
    Text: The first time you avoid or remove a tag each turn, you may install a card from your grip, lowering its install cost by 1.
    '''

    def setUp(self):
        '''
        setup test environment for thunder_art_gallery_22013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_thunder_art_gallery_22013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_miss_bones_22014(unittest.TestCase):
    '''
    testing play functionality of miss_bones
    Cost: 2
    Text: Place 12 credits from the bank on Miss Bones when she is installed. When there are no credits left on Miss Bones, trash her. Use these credits to trash installed cards.
    '''

    def setUp(self):
        '''
        setup test environment for miss_bones_22014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_miss_bones_22014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_psych_mike_22021(unittest.TestCase):
    '''
    testing play functionality of psych_mike
    Cost: 1
    Text: The first time each turn a successful run on R&D ends, you may gain 1 credit for each time you accessed a card in R&D during that run.
    '''

    def setUp(self):
        '''
        setup test environment for psych_mike_22021
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_psych_mike_22021()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dj_fenris_22025(unittest.TestCase):
    '''
    testing play functionality of dj_fenris
    Cost: 3
    Text: Host a g-mod identity that does not match the faction of your identity on DJ Fenris when he is installed. Remove hosted identity from the game if DJ Fenris is uninstalled. DJ Fenris gains the text of hosted identity. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for dj_fenris_22025
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_dj_fenris_22025()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crowdfunding_23013(unittest.TestCase):
    '''
    testing play functionality of crowdfunding
    Cost: 0
    Text: When you install this resource, load 3 credits onto it. When it is empty, trash it and draw 1 card. When your turn begins, take 1 credit from this resource. When your turn ends, if you made at least 3 successful runs this turn and this card is in your heap, you may install it, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for crowdfunding_23013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_crowdfunding_23013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ice_carver_25016(unittest.TestCase):
    '''
    testing play functionality of ice_carver
    Cost: 3
    Text: While you are encountering a piece of ice, it gets -1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for ice_carver_25016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_ice_carver_25016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_liberated_account_25017(unittest.TestCase):
    '''
    testing play functionality of liberated_account
    Cost: 6
    Text: When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for liberated_account_25017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_liberated_account_25017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_scrubber_25018(unittest.TestCase):
    '''
    testing play functionality of scrubber
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.
    '''

    def setUp(self):
        '''
        setup test environment for scrubber_25018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_scrubber_25018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_xanadu_25019(unittest.TestCase):
    '''
    testing play functionality of xanadu
    Cost: 3
    Text: The rez cost of each piece of ice is increased by 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for xanadu_25019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_xanadu_25019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bank_job_25038(unittest.TestCase):
    '''
    testing play functionality of bank_job
    Cost: 1
    Text: When you install this resource, load 8 credits on it. When it is empty, trash it. Whenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for bank_job_25038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_bank_job_25038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_data_dealer_25039(unittest.TestCase):
    '''
    testing play functionality of data_dealer
    Cost: 0
    Text: click, forfeit 1 agenda: Gain 9 credits.
    '''

    def setUp(self):
        '''
        setup test environment for data_dealer_25039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_data_dealer_25039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aesops_pawnshop_25056(unittest.TestCase):
    '''
    testing play functionality of aesops_pawnshop
    Cost: 1
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for aesops_pawnshop_25056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_aesops_pawnshop_25056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ice_analyzer_25057(unittest.TestCase):
    '''
    testing play functionality of ice_analyzer
    Cost: 0
    Text: Whenever the Corp rezzes a piece of ice, place 1 credit on Ice Analyzer. You may use credits on Ice Analyzer to install programs.
    '''

    def setUp(self):
        '''
        setup test environment for ice_analyzer_25057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_ice_analyzer_25057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_professional_contacts_25058(unittest.TestCase):
    '''
    testing play functionality of professional_contacts
    Cost: 5
    Text: click: Gain 1 credit and draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for professional_contacts_25058
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_professional_contacts_25058()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_armitage_codebusting_25062(unittest.TestCase):
    '''
    testing play functionality of armitage_codebusting
    Cost: 1
    Text: Place 12 credits from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it. click: Take 2 credits from Armitage Codebusting.
    '''

    def setUp(self):
        '''
        setup test environment for armitage_codebusting_25062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_armitage_codebusting_25062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_earthrise_hotel_25063(unittest.TestCase):
    '''
    testing play functionality of earthrise_hotel
    Cost: 4
    Text: When you install this resource, load 3 power counters onto it. When it is empty, trash it. When your turn begins, remove 1 hosted power counter and draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for earthrise_hotel_25063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_earthrise_hotel_25063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_john_masanori_25064(unittest.TestCase):
    '''
    testing play functionality of john_masanori
    Cost: 2
    Text: The first time you make a successful run each turn, draw 1 card. The first time you make an unsuccessful run each turn, take 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for john_masanori_25064
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_john_masanori_25064()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kati_jones_25065(unittest.TestCase):
    '''
    testing play functionality of kati_jones
    Cost: 2
    Text: You cannot use Kati Jones more than once per turn. click: Place 3 credits from the bank on Kati Jones. click: Take all credits from Kati Jones.
    '''

    def setUp(self):
        '''
        setup test environment for kati_jones_25065
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_kati_jones_25065()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_climactic_showdown_26006(unittest.TestCase):
    '''
    testing play functionality of climactic_showdown
    Cost: 2
    Text: When your turn begins, remove this resource from the game. Choose a server protected by ice. The Corp may trash 1 piece of ice protecting that server. If they do not, the first time this turn you breach either R&D or HQ, access 2 additional cards.
    '''

    def setUp(self):
        '''
        setup test environment for climactic_showdown_26006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_climactic_showdown_26006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fencer_fueno_26007(unittest.TestCase):
    '''
    testing play functionality of fencer_fueno
    Cost: 0
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Whenever you make a successful run, you may spend hosted credits for the remainder of that run. When your turn ends, if there are 3 or more hosted credits, you must pay 1 credit or trash this resource.
    '''

    def setUp(self):
        '''
        setup test environment for fencer_fueno_26007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_fencer_fueno_26007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_nihilist_26008(unittest.TestCase):
    '''
    testing play functionality of the_nihilist
    Cost: 4
    Text: The first time each turn you install a virus program, place 2 virus counters on this resource. When your turn begins, you may remove any 2 virus counters from your installed cards. If you do, draw 2 cards unless the Corp trashes the top card of R&D.
    '''

    def setUp(self):
        '''
        setup test environment for the_nihilist_26008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_nihilist_26008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_trickster_taka_26009(unittest.TestCase):
    '''
    testing play functionality of trickster_taka
    Cost: 1
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to use programs during runs. When your turn ends, if there are 3 or more hosted credits, you must take 1 tag or trash this resource.
    '''

    def setUp(self):
        '''
        setup test environment for trickster_taka_26009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_trickster_taka_26009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_baklan_bochkin_26017(unittest.TestCase):
    '''
    testing play functionality of baklan_bochkin
    Cost: 2
    Text: The first time each run you encounter a piece of ice, place 1 power counter on this resource. trash: Derez the ice you are encountering if its strength is equal to or less than the number of hosted power counters. Take 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for baklan_bochkin_26017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_baklan_bochkin_26017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_class_act_26018(unittest.TestCase):
    '''
    testing play functionality of the_class_act
    Cost: 4
    Text: When your discard phase ends, if you installed this resource this turn, draw 4 cards. Interrupt -> The first time each turn you would draw any number of cards, look at the top X cards of your stack. Add 1 of those cards to the bottom of your stack. X is equal to the number of cards you will draw plus 1.
    '''

    def setUp(self):
        '''
        setup test environment for the_class_act_26018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_class_act_26018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_artist_26027(unittest.TestCase):
    '''
    testing play functionality of the_artist
    Cost: 4
    Text: Use each ability on this resource only once per turn. click: Gain 2 credits. click: Install a program or piece of hardware, paying 1 credit less.
    '''

    def setUp(self):
        '''
        setup test environment for the_artist_26027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_artist_26027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_whistleblower_26030(unittest.TestCase):
    '''
    testing play functionality of whistleblower
    Cost: 2
    Text: Whenever you make a successful run, you may trash this resource to name an agenda. The next time this run you access a copy of the named agenda, steal it, ignoring all costs. (You are no longer accessing it.)
    '''

    def setUp(self):
        '''
        setup test environment for whistleblower_26030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_whistleblower_26030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mystic_maemi_26072(unittest.TestCase):
    '''
    testing play functionality of mystic_maemi
    Cost: 1
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to play events. When your turn ends, if there are 3 or more hosted credits, you must trash 1 card from your grip at random or trash this resource.
    '''

    def setUp(self):
        '''
        setup test environment for mystic_maemi_26072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_mystic_maemi_26072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paladin_poemu_26073(unittest.TestCase):
    '''
    testing play functionality of paladin_poemu
    Cost: 1
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to install non-connection cards. When your turn ends, if there are 3 or more hosted credits, you must trash 1 of your installed cards.
    '''

    def setUp(self):
        '''
        setup test environment for paladin_poemu_26073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_paladin_poemu_26073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_penumbral_toolkit_26081(unittest.TestCase):
    '''
    testing play functionality of penumbral_toolkit
    Cost: 2
    Text: This card costs 2 credits less to install if you made a successful run on HQ this turn. When you install this resource, load 4 credits onto it. When it is empty, trash it. Spend hosted credits during runs.
    '''

    def setUp(self):
        '''
        setup test environment for penumbral_toolkit_26081
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_penumbral_toolkit_26081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_back_26082(unittest.TestCase):
    '''
    testing play functionality of the_back
    Cost: 1
    Text: The first time each turn you use hardware during a run, place 1 power counter on this resource. click, remove this resource from the game: Shuffle up to X cards with trash abilities from your heap into your stack. X is double the number of hosted power counters.
    '''

    def setUp(self):
        '''
        setup test environment for the_back_26082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_back_26082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cybertrooper_talut_26091(unittest.TestCase):
    '''
    testing play functionality of cybertrooper_talut
    Cost: 2
    Text: +1 link Whenever you install a non-AI icebreaker, that icebreaker gets +2 strength for the remainder of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for cybertrooper_talut_26091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_cybertrooper_talut_26091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paules_cafe_26092(unittest.TestCase):
    '''
    testing play functionality of paules_cafe
    Cost: 1
    Text: click: Host 1 program or piece of hardware from your grip on this resource. 1 credit: Install 1 hosted card. The first card you install this way during each of your turns costs 1 credit less to install for each unique () connection you have installed.
    '''

    def setUp(self):
        '''
        setup test environment for paules_cafe_26092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_paules_cafe_26092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_daily_casts_26094(unittest.TestCase):
    '''
    testing play functionality of daily_casts
    Cost: 3
    Text: When you install this resource, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for daily_casts_26094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_daily_casts_26094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dreamnet_26095(unittest.TestCase):
    '''
    testing play functionality of dreamnet
    Cost: 3
    Text: The first time each turn you make a successful run, draw 1 card. If you have at least 2 link or your identity is digital, also gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for dreamnet_26095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_dreamnet_26095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mystic_maemi_27001(unittest.TestCase):
    '''
    testing play functionality of mystic_maemi
    Cost: 1
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to play events. When your turn ends, if there are 3 or more hosted credits, you must trash 1 card from your grip at random or trash this resource.
    '''

    def setUp(self):
        '''
        setup test environment for mystic_maemi_27001
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_mystic_maemi_27001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cybertrooper_talut_27003(unittest.TestCase):
    '''
    testing play functionality of cybertrooper_talut
    Cost: 2
    Text: +1 link Whenever you install a non-AI icebreaker, that icebreaker gets +2 strength for the remainder of the turn.
    '''

    def setUp(self):
        '''
        setup test environment for cybertrooper_talut_27003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_cybertrooper_talut_27003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crowdfunding_28002(unittest.TestCase):
    '''
    testing play functionality of crowdfunding
    Cost: 0
    Text: When you install this resource, load 3 credits onto it. When it is empty, trash it and draw 1 card. When your turn begins, take 1 credit from this resource. When your turn ends, if you made at least 3 successful runs this turn and this card is in your heap, you may install it, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for crowdfunding_28002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_crowdfunding_28002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cookbook_30009(unittest.TestCase):
    '''
    testing play functionality of cookbook
    Cost: 1
    Text: Whenever you install a virus program, you may place 1 virus counter on it.
    '''

    def setUp(self):
        '''
        setup test environment for cookbook_30009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_cookbook_30009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_red_team_30018(unittest.TestCase):
    '''
    testing play functionality of red_team
    Cost: 5
    Text: When you install this resource, load 12 credits onto it. When it is empty, trash it. click: Run a central server you have not run this turn. If successful, take 3 credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for red_team_30018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_red_team_30018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_telework_contract_30027(unittest.TestCase):
    '''
    testing play functionality of telework_contract
    Cost: 1
    Text: When you install this resource, load 9 credits onto it. When it is empty, trash it. click: Take 3 credits from this resource. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for telework_contract_30027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_telework_contract_30027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_smartware_distributor_30033(unittest.TestCase):
    '''
    testing play functionality of smartware_distributor
    Cost: 0
    Text: click: Place 3 credits on this resource. When your turn begins, take 1 credit from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for smartware_distributor_30033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_smartware_distributor_30033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_verbal_plasticity_30034(unittest.TestCase):
    '''
    testing play functionality of verbal_plasticity
    Cost: 3
    Text: The first time each turn you take the basic action to draw 1 card, instead draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for verbal_plasticity_30034
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_verbal_plasticity_30034()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ice_carver_31009(unittest.TestCase):
    '''
    testing play functionality of ice_carver
    Cost: 3
    Text: While you are encountering a piece of ice, it gets -1 strength.
    '''

    def setUp(self):
        '''
        setup test environment for ice_carver_31009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_ice_carver_31009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_liberated_account_31010(unittest.TestCase):
    '''
    testing play functionality of liberated_account
    Cost: 6
    Text: When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.
    '''

    def setUp(self):
        '''
        setup test environment for liberated_account_31010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_liberated_account_31010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_scrubber_31011(unittest.TestCase):
    '''
    testing play functionality of scrubber
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.
    '''

    def setUp(self):
        '''
        setup test environment for scrubber_31011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_scrubber_31011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_xanadu_31012(unittest.TestCase):
    '''
    testing play functionality of xanadu
    Cost: 3
    Text: The rez cost of each piece of ice is increased by 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for xanadu_31012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_xanadu_31012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_security_testing_31024(unittest.TestCase):
    '''
    testing play functionality of security_testing
    Cost: 0
    Text: When your turn begins, you may choose a server. The first time each turn you make a successful run on the chosen server, instead of breaching it, gain 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for security_testing_31024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_security_testing_31024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_aesops_pawnshop_31035(unittest.TestCase):
    '''
    testing play functionality of aesops_pawnshop
    Cost: 1
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for aesops_pawnshop_31035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_aesops_pawnshop_31035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_professional_contacts_31036(unittest.TestCase):
    '''
    testing play functionality of professional_contacts
    Cost: 5
    Text: click: Gain 1 credit and draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for professional_contacts_31036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_professional_contacts_31036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_earthrise_hotel_31039(unittest.TestCase):
    '''
    testing play functionality of earthrise_hotel
    Cost: 4
    Text: When you install this resource, load 3 power counters onto it. When it is empty, trash it. When your turn begins, remove 1 hosted power counter and draw 2 cards.
    '''

    def setUp(self):
        '''
        setup test environment for earthrise_hotel_31039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_earthrise_hotel_31039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_light_the_fire_32001(unittest.TestCase):
    '''
    testing play functionality of light_the_fire
    Cost: 1
    Text: click, trash, suffer 1 core damage: Run a remote server. During that run, cards in the root of the attacked server lose all abilities. When that run is successful, trash all cards in the root of the attacked server.
    '''

    def setUp(self):
        '''
        setup test environment for light_the_fire_32001
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_light_the_fire_32001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_avgustina_ivanovskaya_33008(unittest.TestCase):
    '''
    testing play functionality of avgustina_ivanovskaya
    Cost: 1
    Text: The first time each turn you install a virus program, sabotage 1. (The Corp trashes 1 card of their choice from HQ or the top of R&D.)
    '''

    def setUp(self):
        '''
        setup test environment for avgustina_ivanovskaya_33008
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_avgustina_ivanovskaya_33008()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_light_the_fire_33009(unittest.TestCase):
    '''
    testing play functionality of light_the_fire
    Cost: 1
    Text: click, trash, suffer 1 core damage: Run a remote server. During that run, cards in the root of the attacked server lose all abilities. When that run is successful, trash all cards in the root of the attacked server.
    '''

    def setUp(self):
        '''
        setup test environment for light_the_fire_33009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_light_the_fire_33009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_twinning_33010(unittest.TestCase):
    '''
    testing play functionality of the_twinning
    Cost: 3
    Text: The first time each turn you spend credits from an installed card, place 1 power counter on this resource. Whenever you breach HQ or R&D, you may remove up to 2 hosted power counters to access that many additional cards.
    '''

    def setUp(self):
        '''
        setup test environment for the_twinning_33010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_the_twinning_33010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_backstitching_33019(unittest.TestCase):
    '''
    testing play functionality of backstitching
    Cost: 2
    Text: When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) Whenever you encounter a piece of ice during a run on your mark, you may trash this resource to bypass that ice.
    '''

    def setUp(self):
        '''
        setup test environment for backstitching_33019
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_backstitching_33019()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_no_free_lunch_33020(unittest.TestCase):
    '''
    testing play functionality of no_free_lunch
    Cost: 0
    Text: trash: Gain 3 credits. trash: Remove 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for no_free_lunch_33020
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_no_free_lunch_33020()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_daeg_first_netcat_33028(unittest.TestCase):
    '''
    testing play functionality of daeg_first_netcat
    Cost: 1
    Text: Whenever an agenda is scored or stolen, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)
    '''

    def setUp(self):
        '''
        setup test environment for daeg_first_netcat_33028
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_daeg_first_netcat_33028()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_environmental_testing_33029(unittest.TestCase):
    '''
    testing play functionality of environmental_testing
    Cost: 3
    Text: Whenever you install a program or piece of hardware, place 1 power counter on this resource. When there are 4 or more hosted power counters, trash this resource and gain 9 credits.
    '''

    def setUp(self):
        '''
        setup test environment for environmental_testing_33029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_environmental_testing_33029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_stoneship_chart_room_33030(unittest.TestCase):
    '''
    testing play functionality of stoneship_chart_room
    Cost: 0
    Text: trash: Draw 2 cards. trash: Charge 1 of your installed cards.
    '''

    def setUp(self):
        '''
        setup test environment for stoneship_chart_room_33030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_stoneship_chart_room_33030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tsakhia_bankhar_gantulga_33074(unittest.TestCase):
    '''
    testing play functionality of tsakhia_bankhar_gantulga
    Cost: 1
    Text: When your turn begins, you may choose a server. During the first encounter each turn with a piece of ice protecting the chosen server, whenever the Corp would resolve a subroutine, instead they resolve Subroutine Do 1 net damage..
    '''

    def setUp(self):
        '''
        setup test environment for tsakhia_bankhar_gantulga_33074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_tsakhia_bankhar_gantulga_33074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_asmund_pudlat_33082(unittest.TestCase):
    '''
    testing play functionality of asmund_pudlat
    Cost: 2
    Text: When you install this resource, search your stack for up to 2 virus or weapon cards with different names. Host those cards faceup on this resource. (They are not installed.) When your turn begins, you may add 1 hosted card to your grip. If there are no more hosted cards, trash this resource.
    '''

    def setUp(self):
        '''
        setup test environment for asmund_pudlat_33082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_asmund_pudlat_33082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_info_bounty_33083(unittest.TestCase):
    '''
    testing play functionality of info_bounty
    Cost: 2
    Text: When your turn begins, identify your mark. (If you don't have a mark, a random central server becomes your mark for this turn.) The first time each turn a run on your mark ends, gain 2 credits if you breached that server during that run.
    '''

    def setUp(self):
        '''
        setup test environment for info_bounty_33083
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_info_bounty_33083()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dr_nuka_vrolyck_33092(unittest.TestCase):
    '''
    testing play functionality of dr_nuka_vrolyck
    Cost: 1
    Text: When you install this resource, load 2 power counters onto it. When it is empty, trash it. click, hosted power counter: Draw 3 cards.
    '''

    def setUp(self):
        '''
        setup test environment for dr_nuka_vrolyck_33092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = resource_dr_nuka_vrolyck_33092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")
