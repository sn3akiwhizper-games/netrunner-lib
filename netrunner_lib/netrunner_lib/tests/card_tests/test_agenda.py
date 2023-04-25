
'''
test cases for card classes of type agenda
'''
import unittest

from netrunner_lib.cards._base_card_classes import Agenda
from netrunner_lib.cards.agenda import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
class Test_accelerated_beta_test_01055(unittest.TestCase):
    '''
    testing play functionality of accelerated_beta_test
    Cost: *card has no cost*
    Text: When you score Accelerated Beta Test, you may look at the top 3 cards of R&D. If any of those cards are ice, you may install and rez them, ignoring all costs. Trash the rest of the cards you looked at.
    '''

    def setUp(self):
        '''
        setup test environment for accelerated_beta_test_01055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_accelerated_beta_test_01055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nisei_mk_ii_01068(unittest.TestCase):
    '''
    testing play functionality of nisei_mk_ii
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: End the run.
    '''

    def setUp(self):
        '''
        setup test environment for nisei_mk_ii_01068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_nisei_mk_ii_01068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_astroscript_pilot_program_01081(unittest.TestCase):
    '''
    testing play functionality of astroscript_pilot_program
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: Place 1 advancement counter on an installed card you can advance. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for astroscript_pilot_program_01081
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_astroscript_pilot_program_01081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_breaking_news_01082(unittest.TestCase):
    '''
    testing play functionality of breaking_news
    Cost: *card has no cost*
    Text: When you score Breaking News, give the Runner 2 tags. When the turn on which you scored Breaking News ends, the Runner loses 2 tags.
    '''

    def setUp(self):
        '''
        setup test environment for breaking_news_01082
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_breaking_news_01082()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hostile_takeover_01094(unittest.TestCase):
    '''
    testing play functionality of hostile_takeover
    Cost: *card has no cost*
    Text: When you score this agenda, gain 7 credits and take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for hostile_takeover_01094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_hostile_takeover_01094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_posted_bounty_01095(unittest.TestCase):
    '''
    testing play functionality of posted_bounty
    Cost: *card has no cost*
    Text: When you score Posted Bounty, you may forfeit it to give the Runner 1 tag and take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for posted_bounty_01095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_posted_bounty_01095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_priority_requisition_01106(unittest.TestCase):
    '''
    testing play functionality of priority_requisition
    Cost: *card has no cost*
    Text: When you score Priority Requisition, you may rez a piece of ice ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for priority_requisition_01106
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_priority_requisition_01106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_private_security_force_01107(unittest.TestCase):
    '''
    testing play functionality of private_security_force
    Cost: *card has no cost*
    Text: If the Runner is tagged, Private Security Force gains: "click: Do 1 meat damage."
    '''

    def setUp(self):
        '''
        setup test environment for private_security_force_01107
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_private_security_force_01107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mandatory_upgrades_02011(unittest.TestCase):
    '''
    testing play functionality of mandatory_upgrades
    Cost: *card has no cost*
    Text: You have 1 additional click to spend each turn.
    '''

    def setUp(self):
        '''
        setup test environment for mandatory_upgrades_02011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_mandatory_upgrades_02011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_braintrust_02014(unittest.TestCase):
    '''
    testing play functionality of braintrust
    Cost: *card has no cost*
    Text: When you score Braintrust, place 1 agenda counter on it for every 2 advancement tokens on it over 3. The rez cost of all ice is lowered by 1 for each agenda counter on Braintrust.
    '''

    def setUp(self):
        '''
        setup test environment for braintrust_02014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_braintrust_02014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_restructured_datapool_02016(unittest.TestCase):
    '''
    testing play functionality of restructured_datapool
    Cost: *card has no cost*
    Text: click: Trace[2]. If successful, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for restructured_datapool_02016
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_restructured_datapool_02016()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_atlas_02018(unittest.TestCase):
    '''
    testing play functionality of project_atlas
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Search R&D for 1 card and reveal it. Add it to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for project_atlas_02018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_atlas_02018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fetal_ai_02032(unittest.TestCase):
    '''
    testing play functionality of fetal_ai
    Cost: *card has no cost*
    Text: While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda anywhere except in Archives, do 2 net damage. As an additional cost to steal this agenda, the Runner must pay 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for fetal_ai_02032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_fetal_ai_02032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_executive_retreat_02039(unittest.TestCase):
    '''
    testing play functionality of executive_retreat
    Cost: *card has no cost*
    Text: When you score Executive Retreat, place 1 agenda counter on it and shuffle HQ into R&D. click, hosted agenda counter: Draw 5 cards.
    '''

    def setUp(self):
        '''
        setup test environment for executive_retreat_02039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_executive_retreat_02039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_vitruvius_02051(unittest.TestCase):
    '''
    testing play functionality of project_vitruvius
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Add 1 card from Archives to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for project_vitruvius_02051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_vitruvius_02051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_government_contracts_02077(unittest.TestCase):
    '''
    testing play functionality of government_contracts
    Cost: *card has no cost*
    Text: click, click: Gain 4 credits.
    '''

    def setUp(self):
        '''
        setup test environment for government_contracts_02077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_government_contracts_02077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_false_lead_02080(unittest.TestCase):
    '''
    testing play functionality of false_lead
    Cost: *card has no cost*
    Text: Forfeit this agenda: If the Runner has 2 or more click remaining, they lose click click.
    '''

    def setUp(self):
        '''
        setup test environment for false_lead_02080
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_false_lead_02080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_beale_02115(unittest.TestCase):
    '''
    testing play functionality of project_beale
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3. This agenda is worth 1 more agenda point for each hosted agenda counter.
    '''

    def setUp(self):
        '''
        setup test environment for project_beale_02115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_beale_02115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_war_02120(unittest.TestCase):
    '''
    testing play functionality of corporate_war
    Cost: *card has no cost*
    Text: If you have at least 7 credits when you score Corporate War, gain 7 credits; otherwise, lose all credits in your credit pool.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_war_02120
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_corporate_war_02120()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_director_haas_pet_project_03004(unittest.TestCase):
    '''
    testing play functionality of director_haas_pet_project
    Cost: *card has no cost*
    Text: When you score this agenda, you may create a new remote server by installing up to 3 cards from HQ and/or Archives in the root of and/or protecting that server, ignoring all install costs. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for director_haas_pet_project_03004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_director_haas_pet_project_03004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_efficiency_committee_03005(unittest.TestCase):
    '''
    testing play functionality of efficiency_committee
    Cost: *card has no cost*
    Text: Place 3 agenda counters on Efficiency Committee when you score it. click, hosted agenda counter: Gain click click. You cannot advance cards for the remainder of this turn.
    '''

    def setUp(self):
        '''
        setup test environment for efficiency_committee_03005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_efficiency_committee_03005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_wotan_03006(unittest.TestCase):
    '''
    testing play functionality of project_wotan
    Cost: *card has no cost*
    Text: Place 3 agenda counters on Project Wotan when you score it. Hosted agenda counter: Choose a rezzed piece of bioroid ice currently being approached. For the remainder of this run, that ice gains "Subroutine End the run." after all its other subroutines.
    '''

    def setUp(self):
        '''
        setup test environment for project_wotan_03006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_wotan_03006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sentinel_defense_program_03007(unittest.TestCase):
    '''
    testing play functionality of sentinel_defense_program
    Cost: *card has no cost*
    Text: Whenever the Runner suffers at least 1 core damage, do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for sentinel_defense_program_03007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_sentinel_defense_program_03007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_gila_hands_arcology_03023(unittest.TestCase):
    '''
    testing play functionality of gila_hands_arcology
    Cost: *card has no cost*
    Text: click, click: Gain 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for gila_hands_arcology_03023
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_gila_hands_arcology_03023()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_ares_04010(unittest.TestCase):
    '''
    testing play functionality of project_ares
    Cost: *card has no cost*
    Text: When you score this agenda, the Runner trashes 1 of their installed cards for each hosted advancement counter past 4. If the Runner trashes at least 1 card this way, take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for project_ares_04010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_ares_04010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_character_assassination_04014(unittest.TestCase):
    '''
    testing play functionality of character_assassination
    Cost: *card has no cost*
    Text: When you score Character Assassination, trash 1 resource (cannot be prevented).
    '''

    def setUp(self):
        '''
        setup test environment for character_assassination_04014
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_character_assassination_04014()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_geothermal_fracking_04017(unittest.TestCase):
    '''
    testing play functionality of geothermal_fracking
    Cost: *card has no cost*
    Text: Place 2 agenda counters on Geothermal Fracking when you score it. click, hosted agenda counter: Gain 7 credits and take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for geothermal_fracking_04017
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_geothermal_fracking_04017()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_clone_retirement_04032(unittest.TestCase):
    '''
    testing play functionality of clone_retirement
    Cost: *card has no cost*
    Text: When you score Clone Retirement, you may remove 1 bad publicity. When the Runner steals Clone Retirement, the Corp takes 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for clone_retirement_04032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_clone_retirement_04032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_cleaners_04036(unittest.TestCase):
    '''
    testing play functionality of the_cleaners
    Cost: *card has no cost*
    Text: Interrupt -> Whenever you would do meat damage, increase that damage by 1.
    '''

    def setUp(self):
        '''
        setup test environment for the_cleaners_04036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_the_cleaners_04036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_profiteering_04039(unittest.TestCase):
    '''
    testing play functionality of profiteering
    Cost: *card has no cost*
    Text: When you score Profiteering, take up to 3 bad publicity. Gain 5 credits for each bad publicity taken.
    '''

    def setUp(self):
        '''
        setup test environment for profiteering_04039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_profiteering_04039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_unorthodox_predictions_04053(unittest.TestCase):
    '''
    testing play functionality of unorthodox_predictions
    Cost: *card has no cost*
    Text: When you score Unorthodox Predictions, choose sentry, code gate or barrier. Subroutines on ice of the chosen type cannot be broken until the beginning of your next turn.
    '''

    def setUp(self):
        '''
        setup test environment for unorthodox_predictions_04053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_unorthodox_predictions_04053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tgtbt_04075(unittest.TestCase):
    '''
    testing play functionality of tgtbt
    Cost: *card has no cost*
    Text: While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, give them 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for tgtbt_04075
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_tgtbt_04075()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_veterans_program_04080(unittest.TestCase):
    '''
    testing play functionality of veterans_program
    Cost: *card has no cost*
    Text: When you score Veterans Program, you may remove up to 2 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for veterans_program_04080
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_veterans_program_04080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_market_research_04095(unittest.TestCase):
    '''
    testing play functionality of market_research
    Cost: *card has no cost*
    Text: If the Runner is tagged when you score Market Research, place 1 agenda counter on it. Market Research is worth 1 additional agenda point while it has an agenda counter on it.
    '''

    def setUp(self):
        '''
        setup test environment for market_research_04095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_market_research_04095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vulcan_coverup_04098(unittest.TestCase):
    '''
    testing play functionality of vulcan_coverup
    Cost: *card has no cost*
    Text: When you score Vulcan Coverup, do 2 meat damage. When the Runner steals Vulcan Coverup, take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for vulcan_coverup_04098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_vulcan_coverup_04098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_napd_contract_04119(unittest.TestCase):
    '''
    testing play functionality of napd_contract
    Cost: *card has no cost*
    Text: The advancement requirement of NAPD Contract is increased by 1 for each bad publicity the Corp has. As an additional cost to steal NAPD Contract, the Runner must pay 4 credits.
    '''

    def setUp(self):
        '''
        setup test environment for napd_contract_04119
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_napd_contract_04119()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_house_of_knives_05004(unittest.TestCase):
    '''
    testing play functionality of house_of_knives
    Cost: *card has no cost*
    Text: When you score this agenda, place 3 agenda counters on it. Hosted agenda counter: Do 1 net damage. Use this ability only during a run and only once per run.
    '''

    def setUp(self):
        '''
        setup test environment for house_of_knives_05004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_house_of_knives_05004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_medical_breakthrough_05005(unittest.TestCase):
    '''
    testing play functionality of medical_breakthrough
    Cost: *card has no cost*
    Text: Lower the advancement requirement of each Medical Breakthrough by 1. This ability is active even while Medical Breakthrough is in the Runner's score area.
    '''

    def setUp(self):
        '''
        setup test environment for medical_breakthrough_05005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_medical_breakthrough_05005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_philotic_entanglement_05006(unittest.TestCase):
    '''
    testing play functionality of philotic_entanglement
    Cost: *card has no cost*
    Text: When you score Philotic Entanglement, do 1 net damage for each agenda in the Runner's score area. Limit 1 Philotic Entanglement per deck.
    '''

    def setUp(self):
        '''
        setup test environment for philotic_entanglement_05006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_philotic_entanglement_05006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_future_perfect_05007(unittest.TestCase):
    '''
    testing play functionality of the_future_perfect
    Cost: *card has no cost*
    Text: When the Runner accesses The Future Perfect, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, prevent The Future Perfect from being stolen. Ignore this ability if the Runner accesses The Future Perfect while it is installed.
    '''

    def setUp(self):
        '''
        setup test environment for the_future_perfect_05007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_the_future_perfect_05007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_domestic_sleepers_06001(unittest.TestCase):
    '''
    testing play functionality of domestic_sleepers
    Cost: *card has no cost*
    Text: click,click,click: Place 1 agenda counter on Domestic Sleepers. Domestic Sleepers is worth 1 agenda point while it has at least 1 agenda counter on it.
    '''

    def setUp(self):
        '''
        setup test environment for domestic_sleepers_06001
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_domestic_sleepers_06001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_encrypted_portals_06024(unittest.TestCase):
    '''
    testing play functionality of encrypted_portals
    Cost: *card has no cost*
    Text: All code gate ice have +1 strength. When you score Encrypted Portals, gain 1 credit for each rezzed code gate.
    '''

    def setUp(self):
        '''
        setup test environment for encrypted_portals_06024
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_encrypted_portals_06024()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_eden_fragment_06030(unittest.TestCase):
    '''
    testing play functionality of eden_fragment
    Cost: *card has no cost*
    Text: Ignore the install cost of the first piece of ice you install each turn. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for eden_fragment_06030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_eden_fragment_06030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_chronos_project_06049(unittest.TestCase):
    '''
    testing play functionality of chronos_project
    Cost: *card has no cost*
    Text: When you score this agenda, the Runner removes all cards in the heap from the game.
    '''

    def setUp(self):
        '''
        setup test environment for chronos_project_06049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_chronos_project_06049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_labyrinthine_servers_06063(unittest.TestCase):
    '''
    testing play functionality of labyrinthine_servers
    Cost: *card has no cost*
    Text: Place 2 power counters on Labyrinthine Servers when you score it. Hosted power counter: Prevent the Runner from jacking out. The Runner cannot jack out for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for labyrinthine_servers_06063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_labyrinthine_servers_06063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hades_fragment_06071(unittest.TestCase):
    '''
    testing play functionality of hades_fragment
    Cost: *card has no cost*
    Text: When your turn begins, you may add 1 card from Archives to the bottom of R&D. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for hades_fragment_06071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_hades_fragment_06071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bifrost_array_06081(unittest.TestCase):
    '''
    testing play functionality of bifrost_array
    Cost: *card has no cost*
    Text: When you score Bifrost Array, you may trigger the "when scored" ability of another agenda that is not a copy of Bifrost Array in your score area.
    '''

    def setUp(self):
        '''
        setup test environment for bifrost_array_06081
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_bifrost_array_06081()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_license_acquisition_06085(unittest.TestCase):
    '''
    testing play functionality of license_acquisition
    Cost: *card has no cost*
    Text: When you score this agenda, you may reveal 1 asset or upgrade in HQ or Archives. Install and rez that card, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for license_acquisition_06085
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_license_acquisition_06085()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_superior_cyberwalls_06087(unittest.TestCase):
    '''
    testing play functionality of superior_cyberwalls
    Cost: *card has no cost*
    Text: All barrier ice have +1 strength. When you score Superior Cyberwalls, gain 1 credit for each rezzed barrier.
    '''

    def setUp(self):
        '''
        setup test environment for superior_cyberwalls_06087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_superior_cyberwalls_06087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_helium3_deposit_06101(unittest.TestCase):
    '''
    testing play functionality of helium3_deposit
    Cost: *card has no cost*
    Text: When you score Helium-3 Deposit, place up to 2 power counters on a card with at least 1 power counter on it.
    '''

    def setUp(self):
        '''
        setup test environment for helium3_deposit_06101
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_helium3_deposit_06101()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_utopia_fragment_06110(unittest.TestCase):
    '''
    testing play functionality of utopia_fragment
    Cost: *card has no cost*
    Text: As an additional cost to steal an agenda, the Runner must pay 2 credits for each advancement token on that agenda. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for utopia_fragment_06110
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_utopia_fragment_06110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_firmware_updates_07004(unittest.TestCase):
    '''
    testing play functionality of firmware_updates
    Cost: *card has no cost*
    Text: Place 3 agenda counters on Firmware Updates when you score it. Hosted agenda counter: Place 1 advancement token on a piece of ice that can be advanced. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for firmware_updates_07004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_firmware_updates_07004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_glenn_station_07005(unittest.TestCase):
    '''
    testing play functionality of glenn_station
    Cost: *card has no cost*
    Text: Glenn Station can host a single card. click: Host a card from HQ facedown on Glenn Station. click: Add a card on Glenn Station to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for glenn_station_07005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_glenn_station_07005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_government_takeover_07006(unittest.TestCase):
    '''
    testing play functionality of government_takeover
    Cost: *card has no cost*
    Text: click: Gain 3 credits. Limit 1 Government Takeover per deck.
    '''

    def setUp(self):
        '''
        setup test environment for government_takeover_07006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_government_takeover_07006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_highrisk_investment_07007(unittest.TestCase):
    '''
    testing play functionality of highrisk_investment
    Cost: *card has no cost*
    Text: Place 1 agenda counter on High-Risk Investment when you score it. click, hosted agenda counter: Gain 1 credit for each credit in the Runner's credit pool.
    '''

    def setUp(self):
        '''
        setup test environment for highrisk_investment_07007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_highrisk_investment_07007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_genetic_resequencing_08013(unittest.TestCase):
    '''
    testing play functionality of genetic_resequencing
    Cost: *card has no cost*
    Text: When you score Genetic Resequencing, you may place 1 agenda counter on an agenda in your score area.
    '''

    def setUp(self):
        '''
        setup test environment for genetic_resequencing_08013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_genetic_resequencing_08013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_research_grant_08032(unittest.TestCase):
    '''
    testing play functionality of research_grant
    Cost: *card has no cost*
    Text: When you score Research Grant, you may score another copy of Research Grant that is installed.
    '''

    def setUp(self):
        '''
        setup test environment for research_grant_08032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_research_grant_08032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_selfdestruct_chips_08051(unittest.TestCase):
    '''
    testing play functionality of selfdestruct_chips
    Cost: *card has no cost*
    Text: The Runner's maximum hand size is reduced by 1.
    '''

    def setUp(self):
        '''
        setup test environment for selfdestruct_chips_08051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_selfdestruct_chips_08051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_oaktown_renovation_08058(unittest.TestCase):
    '''
    testing play functionality of oaktown_renovation
    Cost: *card has no cost*
    Text: Install only faceup. (This agenda is neither rezzed nor unrezzed.) Whenever you advance this agenda, gain 2 credits. If there are 5 or more hosted advancement counters (including the counter just placed), gain 3 credits instead.
    '''

    def setUp(self):
        '''
        setup test environment for oaktown_renovation_08058
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_oaktown_renovation_08058()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_underway_renovation_08077(unittest.TestCase):
    '''
    testing play functionality of underway_renovation
    Cost: *card has no cost*
    Text: Install Underway Renovation faceup. Whenever you advance Underway Renovation, trash the top card of the Runner's stack (or top 2 cards instead if there are 4 or more advancement tokens on Underway Renovation).
    '''

    def setUp(self):
        '''
        setup test environment for underway_renovation_08077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_underway_renovation_08077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_award_bait_08093(unittest.TestCase):
    '''
    testing play functionality of award_bait
    Cost: *card has no cost*
    Text: While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, you may place up to 2 advancement counters on 1 installed card you can advance.
    '''

    def setUp(self):
        '''
        setup test environment for award_bait_08093
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_award_bait_08093()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_explodeapalooza_08094(unittest.TestCase):
    '''
    testing play functionality of explodeapalooza
    Cost: *card has no cost*
    Text: While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, you may gain 5 credits.
    '''

    def setUp(self):
        '''
        setup test environment for explodeapalooza_08094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_explodeapalooza_08094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hollywood_renovation_08098(unittest.TestCase):
    '''
    testing play functionality of hollywood_renovation
    Cost: *card has no cost*
    Text: Install Hollywood Renovation faceup. Whenever you advance Hollywood Renovation, you may place 1 advancement token on another card that can be advanced (or 2 advancement tokens instead if there are 6 or more advancement tokens on Hollywood Renovation).
    '''

    def setUp(self):
        '''
        setup test environment for hollywood_renovation_08098
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_hollywood_renovation_08098()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vanity_project_08100(unittest.TestCase):
    '''
    testing play functionality of vanity_project
    Cost: *card has no cost*
    Text: *no card text*
    '''

    def setUp(self):
        '''
        setup test environment for vanity_project_08100
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_vanity_project_08100()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ancestral_imager_08112(unittest.TestCase):
    '''
    testing play functionality of ancestral_imager
    Cost: *card has no cost*
    Text: Whenever the Runner jacks out, do 1 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for ancestral_imager_08112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_ancestral_imager_08112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_future_is_now_08120(unittest.TestCase):
    '''
    testing play functionality of the_future_is_now
    Cost: *card has no cost*
    Text: When you score The Future is Now, search R&D for a card and add it to HQ. Shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for the_future_is_now_08120
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_the_future_is_now_08120()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_15_minutes_09004(unittest.TestCase):
    '''
    testing play functionality of 15_minutes
    Cost: *card has no cost*
    Text: click: Shuffle 15 Minutes into R&D. The Corp can trigger this ability while 15 Minutes is in the Runner's score area. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for 15_minutes_09004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_15_minutes_09004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_improved_tracers_09005(unittest.TestCase):
    '''
    testing play functionality of improved_tracers
    Cost: *card has no cost*
    Text: All tracer ice have +1 strength. The base trace strength of each subroutine is increased by 1.
    '''

    def setUp(self):
        '''
        setup test environment for improved_tracers_09005
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_improved_tracers_09005()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_rebranding_team_09006(unittest.TestCase):
    '''
    testing play functionality of rebranding_team
    Cost: *card has no cost*
    Text: All assets gain advertisement.
    '''

    def setUp(self):
        '''
        setup test environment for rebranding_team_09006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_rebranding_team_09006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_quantum_predictive_model_09007(unittest.TestCase):
    '''
    testing play functionality of quantum_predictive_model
    Cost: *card has no cost*
    Text: While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda while they are tagged, add it to your score area.
    '''

    def setUp(self):
        '''
        setup test environment for quantum_predictive_model_09007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_quantum_predictive_model_09007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_global_food_initiative_09026(unittest.TestCase):
    '''
    testing play functionality of global_food_initiative
    Cost: *card has no cost*
    Text: Global Food Initiative is worth 1 fewer agenda point while in the Runner's score area.
    '''

    def setUp(self):
        '''
        setup test environment for global_food_initiative_09026
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_global_food_initiative_09026()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_advanced_concept_hopper_10011(unittest.TestCase):
    '''
    testing play functionality of advanced_concept_hopper
    Cost: *card has no cost*
    Text: The first time the Runner initiates a run each turn, you may draw 1 card or gain 1 credit.
    '''

    def setUp(self):
        '''
        setup test environment for advanced_concept_hopper_10011
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_advanced_concept_hopper_10011()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_remote_data_farm_10033(unittest.TestCase):
    '''
    testing play functionality of remote_data_farm
    Cost: *card has no cost*
    Text: Your maximum hand size is increased by 2.
    '''

    def setUp(self):
        '''
        setup test environment for remote_data_farm_10033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_remote_data_farm_10033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_new_construction_10035(unittest.TestCase):
    '''
    testing play functionality of new_construction
    Cost: *card has no cost*
    Text: Install only faceup. (This agenda is neither rezzed nor unrezzed.) Whenever you advance this agenda, you may install 1 card from HQ in the root of a new server. If there are 5 or more hosted advancement counters, rez that card, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for new_construction_10035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_new_construction_10035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_sales_team_10037(unittest.TestCase):
    '''
    testing play functionality of corporate_sales_team
    Cost: *card has no cost*
    Text: When you score Corporate Sales Team, place 10 credits on it. When each player's turn begins, take 1 credit from Corporate Sales Team.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_sales_team_10037
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_corporate_sales_team_10037()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_voting_machine_initiative_10048(unittest.TestCase):
    '''
    testing play functionality of voting_machine_initiative
    Cost: *card has no cost*
    Text: Place 3 agenda counters on Voting Machine Initiative when you score it. When the Runner's turn begins, you may spend 1 hosted agenda counter. If you do, the Runner loses click, if able.
    '''

    def setUp(self):
        '''
        setup test environment for voting_machine_initiative_10048
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_voting_machine_initiative_10048()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_personality_profiles_10066(unittest.TestCase):
    '''
    testing play functionality of personality_profiles
    Cost: *card has no cost*
    Text: Whenever the Runner searches the stack or installs a card from the heap, they trash 1 card from the grip at random.
    '''

    def setUp(self):
        '''
        setup test environment for personality_profiles_10066
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_personality_profiles_10066()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_dedicated_neural_net_10088(unittest.TestCase):
    '''
    testing play functionality of dedicated_neural_net
    Cost: *card has no cost*
    Text: The first time there is a successful run on HQ each turn, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, you choose which cards the Runner accesses from HQ for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for dedicated_neural_net_10088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_dedicated_neural_net_10088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_puppet_master_10090(unittest.TestCase):
    '''
    testing play functionality of puppet_master
    Cost: *card has no cost*
    Text: Whenever the Runner makes a successful run, you may place 1 advancement token on a card that can be advanced.
    '''

    def setUp(self):
        '''
        setup test environment for puppet_master_10090
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_puppet_master_10090()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_improved_protein_source_10105(unittest.TestCase):
    '''
    testing play functionality of improved_protein_source
    Cost: *card has no cost*
    Text: When Improved Protein Source is scored or stolen, the Runner gains 4 credits.
    '''

    def setUp(self):
        '''
        setup test environment for improved_protein_source_10105
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_improved_protein_source_10105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_merger_10114(unittest.TestCase):
    '''
    testing play functionality of merger
    Cost: *card has no cost*
    Text: Merger is worth 1 additional agenda point while in the Runner's score area.
    '''

    def setUp(self):
        '''
        setup test environment for merger_10114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_merger_10114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_crisis_management_11018(unittest.TestCase):
    '''
    testing play functionality of crisis_management
    Cost: *card has no cost*
    Text: If the Runner is tagged, Crisis Management gains "When your turn begins, do 1 meat damage."
    '''

    def setUp(self):
        '''
        setup test environment for crisis_management_11018
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_crisis_management_11018()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_kusanagi_11052(unittest.TestCase):
    '''
    testing play functionality of project_kusanagi
    Cost: *card has no cost*
    Text: When you score Project Kusanagi, place 1 agenda counter on it for each advancement token on it over 2. Hosted agenda counter: Choose 1 piece of ice to gain "Subroutine Do 1 net damage." after all its other subroutines for the remainder of this run.
    '''

    def setUp(self):
        '''
        setup test environment for project_kusanagi_11052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_kusanagi_11052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_show_of_force_11099(unittest.TestCase):
    '''
    testing play functionality of show_of_force
    Cost: *card has no cost*
    Text: When you score Show of Force, do 2 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for show_of_force_11099
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_show_of_force_11099()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sensor_net_activation_11110(unittest.TestCase):
    '''
    testing play functionality of sensor_net_activation
    Cost: *card has no cost*
    Text: Place 1 agenda counter on Sensor Net Activation when you score it. Hosted agenda counter: Rez a bioroid, ignoring all costs. When the turn ends, derez that bioroid.
    '''

    def setUp(self):
        '''
        setup test environment for sensor_net_activation_11110
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_sensor_net_activation_11110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_net_quarantine_11114(unittest.TestCase):
    '''
    testing play functionality of net_quarantine
    Cost: *card has no cost*
    Text: For the first trace each turn, the Runner's link is treated as 0. (They can still increase their link strength by spending credits.) Whenever the Runner spends credits to increase their link strength, gain 1 credit for every 2 credits they spent.
    '''

    def setUp(self):
        '''
        setup test environment for net_quarantine_11114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_net_quarantine_11114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_next_wave_2_12009(unittest.TestCase):
    '''
    testing play functionality of next_wave_2
    Cost: *card has no cost*
    Text: When you score this agenda, if there is a rezzed piece of NEXT ice, you may do 1 core damage.
    '''

    def setUp(self):
        '''
        setup test environment for next_wave_2_12009
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_next_wave_2_12009()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_obokata_protocol_12070(unittest.TestCase):
    '''
    testing play functionality of obokata_protocol
    Cost: *card has no cost*
    Text: As an additional cost to steal Obokata Protocol, the Runner must suffer 4 net damage.
    '''

    def setUp(self):
        '''
        setup test environment for obokata_protocol_12070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_obokata_protocol_12070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_escalate_vitriol_12073(unittest.TestCase):
    '''
    testing play functionality of escalate_vitriol
    Cost: *card has no cost*
    Text: click: Gain 1 credit for each tag the Runner has. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for escalate_vitriol_12073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_escalate_vitriol_12073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_reeducation_12074(unittest.TestCase):
    '''
    testing play functionality of reeducation
    Cost: *card has no cost*
    Text: When you score this agenda, you may add X cards from HQ to the bottom of R&D to draw X cards. The Runner adds X cards from the grip at random to the bottom of the stack, if able.
    '''

    def setUp(self):
        '''
        setup test environment for reeducation_12074
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_reeducation_12074()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_meteor_mining_12076(unittest.TestCase):
    '''
    testing play functionality of meteor_mining
    Cost: *card has no cost*
    Text: When you score Meteor Mining, you may gain 7 credits. If the Runner has at least 2 tags, you may do 7 meat damage instead.
    '''

    def setUp(self):
        '''
        setup test environment for meteor_mining_12076
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_meteor_mining_12076()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_standoff_12077(unittest.TestCase):
    '''
    testing play functionality of standoff
    Cost: *card has no cost*
    Text: When you score this agenda, the Runner may trash 1 of their installed cards. If they do not, draw 1 card and gain 5 credits. Otherwise, you may trash 1 of your installed cards to repeat this process.
    '''

    def setUp(self):
        '''
        setup test environment for standoff_12077
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_standoff_12077()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_mandatory_seed_replacement_12092(unittest.TestCase):
    '''
    testing play functionality of mandatory_seed_replacement
    Cost: *card has no cost*
    Text: When you score Mandatory Seed Replacement, rearrange any number of ice protecting all servers.
    '''

    def setUp(self):
        '''
        setup test environment for mandatory_seed_replacement_12092
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_mandatory_seed_replacement_12092()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_water_monopoly_12093(unittest.TestCase):
    '''
    testing play functionality of water_monopoly
    Cost: *card has no cost*
    Text: The install cost of each non-virtual resource is increased by 1.
    '''

    def setUp(self):
        '''
        setup test environment for water_monopoly_12093
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_water_monopoly_12093()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cfc_excavation_contract_12110(unittest.TestCase):
    '''
    testing play functionality of cfc_excavation_contract
    Cost: *card has no cost*
    Text: When you score CFC Excavation Contract, gain 2 credits for each rezzed bioroid.
    '''

    def setUp(self):
        '''
        setup test environment for cfc_excavation_contract_12110
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_cfc_excavation_contract_12110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_arenhanced_security_12115(unittest.TestCase):
    '''
    testing play functionality of arenhanced_security
    Cost: *card has no cost*
    Text: The first time each turn the Runner trashes a Corp card, give them 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for arenhanced_security_12115
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_arenhanced_security_12115()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_brain_rewiring_13029(unittest.TestCase):
    '''
    testing play functionality of brain_rewiring
    Cost: *card has no cost*
    Text: When you score this agenda, you may pay X credits. If you do, the Runner adds X cards from the grip at random to the bottom of the stack, then draws 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for brain_rewiring_13029
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_brain_rewiring_13029()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_elective_upgrade_13030(unittest.TestCase):
    '''
    testing play functionality of elective_upgrade
    Cost: *card has no cost*
    Text: Place 2 agenda counters on Elective Upgrade when you score it. click, hosted agenda counter: Gain click click. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for elective_upgrade_13030
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_elective_upgrade_13030()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_successful_field_test_13031(unittest.TestCase):
    '''
    testing play functionality of successful_field_test
    Cost: *card has no cost*
    Text: When you score Successful Field Test, install any number of cards from HQ, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for successful_field_test_13031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_successful_field_test_13031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_armored_servers_13042(unittest.TestCase):
    '''
    testing play functionality of armored_servers
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: For the remainder of this run, the Runner must trash 1 card from the grip as an additional cost to jack out or break a subroutine. Use this ability only during a run.
    '''

    def setUp(self):
        '''
        setup test environment for armored_servers_13042
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_armored_servers_13042()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_illicit_sales_13043(unittest.TestCase):
    '''
    testing play functionality of illicit_sales
    Cost: *card has no cost*
    Text: When you score Illicit Sales, you may take 1 bad publicity. Gain 3 credits for each bad publicity that you have.
    '''

    def setUp(self):
        '''
        setup test environment for illicit_sales_13043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_illicit_sales_13043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_graft_13044(unittest.TestCase):
    '''
    testing play functionality of graft
    Cost: *card has no cost*
    Text: When you score Graft, you may search your deck for up to 3 cards, reveal them, and add them to HQ. Shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for graft_13044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_graft_13044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paper_trail_13053(unittest.TestCase):
    '''
    testing play functionality of paper_trail
    Cost: *card has no cost*
    Text: When you score Paper Trail, Trace[6]. If successful, trash all connection and job resources.
    '''

    def setUp(self):
        '''
        setup test environment for paper_trail_13053
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_paper_trail_13053()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_evidence_collection_14000(unittest.TestCase):
    '''
    testing play functionality of evidence_collection
    Cost: *card has no cost*
    Text: When you win a game with Evidence Collection in your score area, reveal set 2.
    '''

    def setUp(self):
        '''
        setup test environment for evidence_collection_14000
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_evidence_collection_14000()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_evidence_collection_2_14001(unittest.TestCase):
    '''
    testing play functionality of evidence_collection_2
    Cost: *card has no cost*
    Text: When you win a game with Evidence Collection in your score area, reveal set 5.
    '''

    def setUp(self):
        '''
        setup test environment for evidence_collection_2_14001
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_evidence_collection_2_14001()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_evidence_collection_3_14002(unittest.TestCase):
    '''
    testing play functionality of evidence_collection_3
    Cost: *card has no cost*
    Text: When you win a game with Evidence Collection in your score area, reveal set 8.
    '''

    def setUp(self):
        '''
        setup test environment for evidence_collection_3_14002
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_evidence_collection_3_14002()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_evidence_collection_4_14003(unittest.TestCase):
    '''
    testing play functionality of evidence_collection_4
    Cost: *card has no cost*
    Text: Evidence Collection is worth 1 fewer agenda point while in the Runner's score area.
    '''

    def setUp(self):
        '''
        setup test environment for evidence_collection_4_14003
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_evidence_collection_4_14003()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_oversight_a_14012(unittest.TestCase):
    '''
    testing play functionality of corporate_oversight_a
    Cost: *card has no cost*
    Text: When you score Corporate Oversight, you may search R&D for a piece of ice. Install and rez it protecting a remote server, ignoring all costs. Shuffle R&D. If you win a game with Corporate Oversight in your score area, destroy it.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_oversight_a_14012
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_corporate_oversight_a_14012()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_corporate_oversight_b_14013(unittest.TestCase):
    '''
    testing play functionality of corporate_oversight_b
    Cost: *card has no cost*
    Text: When you score Corporate Oversight, you may search R&D for a piece of ice. Install and rez it protecting a central server, ignoring all costs. Shuffle R&D. If you win a game with Corporate Oversight in your score area, destroy it.
    '''

    def setUp(self):
        '''
        setup test environment for corporate_oversight_b_14013
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_corporate_oversight_b_14013()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_ares_20062(unittest.TestCase):
    '''
    testing play functionality of project_ares
    Cost: *card has no cost*
    Text: When you score this agenda, the Runner trashes 1 of their installed cards for each hosted advancement counter past 4. If the Runner trashes at least 1 card this way, take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for project_ares_20062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_ares_20062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_vitruvius_20063(unittest.TestCase):
    '''
    testing play functionality of project_vitruvius
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Add 1 card from Archives to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for project_vitruvius_20063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_vitruvius_20063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hostile_takeover_20078(unittest.TestCase):
    '''
    testing play functionality of hostile_takeover
    Cost: *card has no cost*
    Text: When you score this agenda, gain 7 credits and take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for hostile_takeover_20078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_hostile_takeover_20078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_atlas_20079(unittest.TestCase):
    '''
    testing play functionality of project_atlas
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Search R&D for 1 card and reveal it. Add it to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for project_atlas_20079
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_atlas_20079()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_the_cleaners_20080(unittest.TestCase):
    '''
    testing play functionality of the_cleaners
    Cost: *card has no cost*
    Text: Interrupt -> Whenever you would do meat damage, increase that damage by 1.
    '''

    def setUp(self):
        '''
        setup test environment for the_cleaners_20080
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_the_cleaners_20080()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_braintrust_20094(unittest.TestCase):
    '''
    testing play functionality of braintrust
    Cost: *card has no cost*
    Text: When you score Braintrust, place 1 agenda counter on it for every 2 advancement tokens on it over 3. The rez cost of all ice is lowered by 1 for each agenda counter on Braintrust.
    '''

    def setUp(self):
        '''
        setup test environment for braintrust_20094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_braintrust_20094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nisei_mk_ii_20095(unittest.TestCase):
    '''
    testing play functionality of nisei_mk_ii
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: End the run.
    '''

    def setUp(self):
        '''
        setup test environment for nisei_mk_ii_20095
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_nisei_mk_ii_20095()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_beale_20110(unittest.TestCase):
    '''
    testing play functionality of project_beale
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3. This agenda is worth 1 more agenda point for each hosted agenda counter.
    '''

    def setUp(self):
        '''
        setup test environment for project_beale_20110
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_beale_20110()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tgtbt_20111(unittest.TestCase):
    '''
    testing play functionality of tgtbt
    Cost: *card has no cost*
    Text: While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, give them 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for tgtbt_20111
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_tgtbt_20111()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_false_lead_20124(unittest.TestCase):
    '''
    testing play functionality of false_lead
    Cost: *card has no cost*
    Text: Forfeit this agenda: If the Runner has 2 or more click remaining, they lose click click.
    '''

    def setUp(self):
        '''
        setup test environment for false_lead_20124
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_false_lead_20124()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_priority_requisition_20125(unittest.TestCase):
    '''
    testing play functionality of priority_requisition
    Cost: *card has no cost*
    Text: When you score Priority Requisition, you may rez a piece of ice ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for priority_requisition_20125
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_priority_requisition_20125()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_private_security_force_20126(unittest.TestCase):
    '''
    testing play functionality of private_security_force
    Cost: *card has no cost*
    Text: If the Runner is tagged, Private Security Force gains: "click: Do 1 meat damage."
    '''

    def setUp(self):
        '''
        setup test environment for private_security_force_20126
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_private_security_force_20126()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ikawah_project_21010(unittest.TestCase):
    '''
    testing play functionality of ikawah_project
    Cost: *card has no cost*
    Text: As an additional cost to steal Ikawah Project, the Runner must spend click and 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for ikawah_project_21010
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_ikawah_project_21010()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bacterial_programming_21033(unittest.TestCase):
    '''
    testing play functionality of bacterial_programming
    Cost: *card has no cost*
    Text: When Bacterial Programming is scored or stolen, you may look at the top 7 cards of R&D, add any number of them to HQ, trash any number of them, and arrange the rest in any order.
    '''

    def setUp(self):
        '''
        setup test environment for bacterial_programming_21033
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_bacterial_programming_21033()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ssl_endorsement_21038(unittest.TestCase):
    '''
    testing play functionality of ssl_endorsement
    Cost: *card has no cost*
    Text: When this agenda is scored or stolen, place 9 credits on it. When the Corp's turn begins, they may take 3 credits from this agenda. This ability is active even while this agenda is in the Runner's score area.
    '''

    def setUp(self):
        '''
        setup test environment for ssl_endorsement_21038
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_ssl_endorsement_21038()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_degree_mill_21055(unittest.TestCase):
    '''
    testing play functionality of degree_mill
    Cost: *card has no cost*
    Text: As an additional cost to steal Degree Mill, the Runner must shuffle 2 installed Runner cards into the stack.
    '''

    def setUp(self):
        '''
        setup test environment for degree_mill_21055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_degree_mill_21055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_armed_intimidation_21057(unittest.TestCase):
    '''
    testing play functionality of armed_intimidation
    Cost: *card has no cost*
    Text: When you score Armed Intimidation, the Runner must either suffer 5 meat damage or take 2 tags.
    '''

    def setUp(self):
        '''
        setup test environment for armed_intimidation_21057
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_armed_intimidation_21057()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_city_works_project_21078(unittest.TestCase):
    '''
    testing play functionality of city_works_project
    Cost: *card has no cost*
    Text: Install City Works Project faceup. When the Runner accesses City Works Project while it is installed, do 2 meat damage and 1 additional meat damage for each advancement token on it.
    '''

    def setUp(self):
        '''
        setup test environment for city_works_project_21078
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_city_works_project_21078()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_remote_enforcement_21091(unittest.TestCase):
    '''
    testing play functionality of remote_enforcement
    Cost: *card has no cost*
    Text: When you score Remote Enforcement, you may search R&D for a piece of ice, install it protecting a remote server (paying its install cost), and rez it, ignoring its rez cost, then shuffle R&D.
    '''

    def setUp(self):
        '''
        setup test environment for remote_enforcement_21091
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_remote_enforcement_21091()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_viral_weaponization_21094(unittest.TestCase):
    '''
    testing play functionality of viral_weaponization
    Cost: *card has no cost*
    Text: When the turn on which you scored Viral Weaponization ends, do 1 net damage for each card in the grip.
    '''

    def setUp(self):
        '''
        setup test environment for viral_weaponization_21094
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_viral_weaponization_21094()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_better_citizen_program_21116(unittest.TestCase):
    '''
    testing play functionality of better_citizen_program
    Cost: *card has no cost*
    Text: The first time the Runner plays a run event or installs an icebreaker program each turn, you may give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for better_citizen_program_21116
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_better_citizen_program_21116()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hyperloop_extension_22027(unittest.TestCase):
    '''
    testing play functionality of hyperloop_extension
    Cost: *card has no cost*
    Text: When Hyperloop Extension is scored or stolen, the Corp gains 3 credits.
    '''

    def setUp(self):
        '''
        setup test environment for hyperloop_extension_22027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_hyperloop_extension_22027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_jumon_22035(unittest.TestCase):
    '''
    testing play functionality of jumon
    Cost: *card has no cost*
    Text: When your turn ends, place 2 advancement counters on 1 card in the root of a remote server.
    '''

    def setUp(self):
        '''
        setup test environment for jumon_22035
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_jumon_22035()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fly_on_the_wall_22043(unittest.TestCase):
    '''
    testing play functionality of fly_on_the_wall
    Cost: *card has no cost*
    Text: When you score Fly on the Wall, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for fly_on_the_wall_22043
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_fly_on_the_wall_22043()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_broad_daylight_22051(unittest.TestCase):
    '''
    testing play functionality of broad_daylight
    Cost: *card has no cost*
    Text: When you score Broad Daylight, you may take 1 bad publicity. Place 1 agenda counter on Broad Daylight for each bad publicity you have. click, hosted agenda counter: Do 2 meat damage. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for broad_daylight_22051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_broad_daylight_22051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_timely_public_release_23027(unittest.TestCase):
    '''
    testing play functionality of timely_public_release
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: Install 1 piece of ice from HQ or Archives in any position protecting a server, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for timely_public_release_23027
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_timely_public_release_23027()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_vitruvius_25068(unittest.TestCase):
    '''
    testing play functionality of project_vitruvius
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Add 1 card from Archives to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for project_vitruvius_25068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_vitruvius_25068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_successful_field_test_25069(unittest.TestCase):
    '''
    testing play functionality of successful_field_test
    Cost: *card has no cost*
    Text: When you score Successful Field Test, install any number of cards from HQ, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for successful_field_test_25069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_successful_field_test_25069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_fetal_ai_25086(unittest.TestCase):
    '''
    testing play functionality of fetal_ai
    Cost: *card has no cost*
    Text: While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda anywhere except in Archives, do 2 net damage. As an additional cost to steal this agenda, the Runner must pay 2 credits.
    '''

    def setUp(self):
        '''
        setup test environment for fetal_ai_25086
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_fetal_ai_25086()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nisei_mk_ii_25087(unittest.TestCase):
    '''
    testing play functionality of nisei_mk_ii
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: End the run.
    '''

    def setUp(self):
        '''
        setup test environment for nisei_mk_ii_25087
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_nisei_mk_ii_25087()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_philotic_entanglement_25088(unittest.TestCase):
    '''
    testing play functionality of philotic_entanglement
    Cost: *card has no cost*
    Text: When you score Philotic Entanglement, do 1 net damage for each agenda in the Runner's score area. Limit 1 Philotic Entanglement per deck.
    '''

    def setUp(self):
        '''
        setup test environment for philotic_entanglement_25088
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_philotic_entanglement_25088()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_explodeapalooza_25106(unittest.TestCase):
    '''
    testing play functionality of explodeapalooza
    Cost: *card has no cost*
    Text: While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, you may gain 5 credits.
    '''

    def setUp(self):
        '''
        setup test environment for explodeapalooza_25106
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_explodeapalooza_25106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_beale_25107(unittest.TestCase):
    '''
    testing play functionality of project_beale
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3. This agenda is worth 1 more agenda point for each hosted agenda counter.
    '''

    def setUp(self):
        '''
        setup test environment for project_beale_25107
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_beale_25107()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hostile_takeover_25124(unittest.TestCase):
    '''
    testing play functionality of hostile_takeover
    Cost: *card has no cost*
    Text: When you score this agenda, gain 7 credits and take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for hostile_takeover_25124
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_hostile_takeover_25124()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_oaktown_renovation_25125(unittest.TestCase):
    '''
    testing play functionality of oaktown_renovation
    Cost: *card has no cost*
    Text: Install only faceup. (This agenda is neither rezzed nor unrezzed.) Whenever you advance this agenda, gain 2 credits. If there are 5 or more hosted advancement counters (including the counter just placed), gain 3 credits instead.
    '''

    def setUp(self):
        '''
        setup test environment for oaktown_renovation_25125
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_oaktown_renovation_25125()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_atlas_25126(unittest.TestCase):
    '''
    testing play functionality of project_atlas
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Search R&D for 1 card and reveal it. Add it to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for project_atlas_25126
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_atlas_25126()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_paper_trail_25140(unittest.TestCase):
    '''
    testing play functionality of paper_trail
    Cost: *card has no cost*
    Text: When you score Paper Trail, Trace[6]. If successful, trash all connection and job resources.
    '''

    def setUp(self):
        '''
        setup test environment for paper_trail_25140
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_paper_trail_25140()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_priority_requisition_25141(unittest.TestCase):
    '''
    testing play functionality of priority_requisition
    Cost: *card has no cost*
    Text: When you score Priority Requisition, you may rez a piece of ice ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for priority_requisition_25141
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_priority_requisition_25141()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_architect_deployment_test_26032(unittest.TestCase):
    '''
    testing play functionality of architect_deployment_test
    Cost: *card has no cost*
    Text: When you score this agenda, look at the top 5 cards of R&D. You may install and rez 1 of those cards, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for architect_deployment_test_26032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_architect_deployment_test_26032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_yagiuda_26040(unittest.TestCase):
    '''
    testing play functionality of project_yagiuda
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Swap 1 card from HQ with 1 card in the root of or protecting the attacked server. The Runner may jack out. Use this ability only during a run.
    '''

    def setUp(self):
        '''
        setup test environment for project_yagiuda_26040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_yagiuda_26040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sting_26041(unittest.TestCase):
    '''
    testing play functionality of sting
    Cost: *card has no cost*
    Text: When a player scores or steals this agenda, do X net damage. X is equal to the number of copies of Sting! in the other player's score area plus 1.
    '''

    def setUp(self):
        '''
        setup test environment for sting_26041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_sting_26041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_remastered_edition_26047(unittest.TestCase):
    '''
    testing play functionality of remastered_edition
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: Place 1 advancement token on an installed card.
    '''

    def setUp(self):
        '''
        setup test environment for remastered_edition_26047
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_remastered_edition_26047()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_divested_trust_26055(unittest.TestCase):
    '''
    testing play functionality of divested_trust
    Cost: *card has no cost*
    Text: Whenever the Runner steals another agenda, you may forfeit this agenda to gain 5 credits and add the stolen agenda to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for divested_trust_26055
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_divested_trust_26055()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_sds_drone_deployment_26056(unittest.TestCase):
    '''
    testing play functionality of sds_drone_deployment
    Cost: *card has no cost*
    Text: As an additional cost to steal this agenda, the Runner must trash an installed program. When you score this agenda, trash an installed program.
    '''

    def setUp(self):
        '''
        setup test environment for sds_drone_deployment_26056
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_sds_drone_deployment_26056()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_vulnerability_audit_26063(unittest.TestCase):
    '''
    testing play functionality of vulnerability_audit
    Cost: *card has no cost*
    Text: You cannot score this agenda if you installed it this turn.
    '''

    def setUp(self):
        '''
        setup test environment for vulnerability_audit_26063
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_vulnerability_audit_26063()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_megaprix_qualifier_26096(unittest.TestCase):
    '''
    testing play functionality of megaprix_qualifier
    Cost: *card has no cost*
    Text: If there is another copy of Megaprix Qualifier in either player's score area when you score this agenda, place 1 agenda counter on this agenda. This agenda is worth 1 more agenda point while it has a hosted agenda counter.
    '''

    def setUp(self):
        '''
        setup test environment for megaprix_qualifier_26096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_megaprix_qualifier_26096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_vacheron_26097(unittest.TestCase):
    '''
    testing play functionality of project_vacheron
    Cost: *card has no cost*
    Text: Interrupt -> When this agenda would be added to the Runner's score area from anywhere except Archives, instead it is added to their score area with 4 hosted agenda counters. While this agenda is in the Runner's score area with 1 or more hosted agenda counters, it is worth 0 agenda points and gains "When the Runner's turn begins, remove 1 hosted agenda counter."
    '''

    def setUp(self):
        '''
        setup test environment for project_vacheron_26097
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_vacheron_26097()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_flower_sermon_26106(unittest.TestCase):
    '''
    testing play functionality of flower_sermon
    Cost: *card has no cost*
    Text: When you score this agenda, place 5 agenda counters on it. Hosted agenda counter: Reveal the top card of R&D. Draw 2 cards. Add 1 card from HQ to the top of R&D. Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for flower_sermon_26106
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_flower_sermon_26106()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_bellona_26114(unittest.TestCase):
    '''
    testing play functionality of bellona
    Cost: *card has no cost*
    Text: As an additional cost to steal this agenda, the Runner must pay 5 credits. When you score this agenda, gain 5 credits.
    '''

    def setUp(self):
        '''
        setup test environment for bellona_26114
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_bellona_26114()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_transport_monopoly_26121(unittest.TestCase):
    '''
    testing play functionality of transport_monopoly
    Cost: *card has no cost*
    Text: When you score this agenda, place 2 agenda counters on it. Hosted agenda counter: This run cannot be declared successful. (This effect does not cause the run to become unsuccessful.) Use this ability only once per turn.
    '''

    def setUp(self):
        '''
        setup test environment for transport_monopoly_26121
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_transport_monopoly_26121()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_cyberdex_sandbox_26128(unittest.TestCase):
    '''
    testing play functionality of cyberdex_sandbox
    Cost: *card has no cost*
    Text: The first time each turn you purge virus counters, gain 4 credits. When you score this agenda, you may purge virus counters.
    '''

    def setUp(self):
        '''
        setup test environment for cyberdex_sandbox_26128
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_cyberdex_sandbox_26128()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_false_lead_26129(unittest.TestCase):
    '''
    testing play functionality of false_lead
    Cost: *card has no cost*
    Text: Forfeit this agenda: If the Runner has 2 or more click remaining, they lose click click.
    '''

    def setUp(self):
        '''
        setup test environment for false_lead_26129
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_false_lead_26129()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_megaprix_qualifier_27004(unittest.TestCase):
    '''
    testing play functionality of megaprix_qualifier
    Cost: *card has no cost*
    Text: If there is another copy of Megaprix Qualifier in either player's score area when you score this agenda, place 1 agenda counter on this agenda. This agenda is worth 1 more agenda point while it has a hosted agenda counter.
    '''

    def setUp(self):
        '''
        setup test environment for megaprix_qualifier_27004
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_megaprix_qualifier_27004()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_timely_public_release_28006(unittest.TestCase):
    '''
    testing play functionality of timely_public_release
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: Install 1 piece of ice from HQ or Archives in any position protecting a server, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for timely_public_release_28006
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_timely_public_release_28006()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_luminal_transubstantiation_30036(unittest.TestCase):
    '''
    testing play functionality of luminal_transubstantiation
    Cost: *card has no cost*
    Text: When you score this agenda, gain click click click. You cannot score agendas for the remainder of the turn. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for luminal_transubstantiation_30036
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_luminal_transubstantiation_30036()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_longevity_serum_30044(unittest.TestCase):
    '''
    testing play functionality of longevity_serum
    Cost: *card has no cost*
    Text: When you score this agenda, trash any number of cards from HQ. Shuffle up to 3 cards from Archives into R&D. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for longevity_serum_30044
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_longevity_serum_30044()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_tomorrows_headline_30052(unittest.TestCase):
    '''
    testing play functionality of tomorrows_headline
    Cost: *card has no cost*
    Text: When this agenda is scored or stolen, give the Runner 1 tag. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for tomorrows_headline_30052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_tomorrows_headline_30052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_above_the_law_30060(unittest.TestCase):
    '''
    testing play functionality of above_the_law
    Cost: *card has no cost*
    Text: When you score this agenda, you may trash 1 installed resource. Limit 1 per deck.
    '''

    def setUp(self):
        '''
        setup test environment for above_the_law_30060
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_above_the_law_30060()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_offworld_office_30067(unittest.TestCase):
    '''
    testing play functionality of offworld_office
    Cost: *card has no cost*
    Text: When you score this agenda, gain 7 credits.
    '''

    def setUp(self):
        '''
        setup test environment for offworld_office_30067
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_offworld_office_30067()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_orbital_superiority_30068(unittest.TestCase):
    '''
    testing play functionality of orbital_superiority
    Cost: *card has no cost*
    Text: When you score this agenda, if the Runner is tagged, do 4 meat damage; otherwise, give the Runner 1 tag.
    '''

    def setUp(self):
        '''
        setup test environment for orbital_superiority_30068
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_orbital_superiority_30068()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_send_a_message_30069(unittest.TestCase):
    '''
    testing play functionality of send_a_message
    Cost: *card has no cost*
    Text: When this agenda is scored or stolen, you may rez 1 installed piece of ice, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for send_a_message_30069
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_send_a_message_30069()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_superconducting_hub_30070(unittest.TestCase):
    '''
    testing play functionality of superconducting_hub
    Cost: *card has no cost*
    Text: When you score this agenda, you may draw 2 cards. You get +2 maximum hand size.
    '''

    def setUp(self):
        '''
        setup test environment for superconducting_hub_30070
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_superconducting_hub_30070()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_vitruvius_31041(unittest.TestCase):
    '''
    testing play functionality of project_vitruvius
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Add 1 card from Archives to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for project_vitruvius_31041
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_vitruvius_31041()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_house_of_knives_31051(unittest.TestCase):
    '''
    testing play functionality of house_of_knives
    Cost: *card has no cost*
    Text: When you score this agenda, place 3 agenda counters on it. Hosted agenda counter: Do 1 net damage. Use this ability only during a run and only once per run.
    '''

    def setUp(self):
        '''
        setup test environment for house_of_knives_31051
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_house_of_knives_31051()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_nisei_mk_ii_31052(unittest.TestCase):
    '''
    testing play functionality of nisei_mk_ii
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: End the run.
    '''

    def setUp(self):
        '''
        setup test environment for nisei_mk_ii_31052
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_nisei_mk_ii_31052()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_license_acquisition_31061(unittest.TestCase):
    '''
    testing play functionality of license_acquisition
    Cost: *card has no cost*
    Text: When you score this agenda, you may reveal 1 asset or upgrade in HQ or Archives. Install and rez that card, ignoring all costs.
    '''

    def setUp(self):
        '''
        setup test environment for license_acquisition_31061
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_license_acquisition_31061()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_beale_31062(unittest.TestCase):
    '''
    testing play functionality of project_beale
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3. This agenda is worth 1 more agenda point for each hosted agenda counter.
    '''

    def setUp(self):
        '''
        setup test environment for project_beale_31062
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_beale_31062()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hostile_takeover_31071(unittest.TestCase):
    '''
    testing play functionality of hostile_takeover
    Cost: *card has no cost*
    Text: When you score this agenda, gain 7 credits and take 1 bad publicity.
    '''

    def setUp(self):
        '''
        setup test environment for hostile_takeover_31071
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_hostile_takeover_31071()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_oaktown_renovation_31072(unittest.TestCase):
    '''
    testing play functionality of oaktown_renovation
    Cost: *card has no cost*
    Text: Install only faceup. (This agenda is neither rezzed nor unrezzed.) Whenever you advance this agenda, gain 2 credits. If there are 5 or more hosted advancement counters (including the counter just placed), gain 3 credits instead.
    '''

    def setUp(self):
        '''
        setup test environment for oaktown_renovation_31072
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_oaktown_renovation_31072()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_project_atlas_31073(unittest.TestCase):
    '''
    testing play functionality of project_atlas
    Cost: *card has no cost*
    Text: When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Search R&D for 1 card and reveal it. Add it to HQ.
    '''

    def setUp(self):
        '''
        setup test environment for project_atlas_31073
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_project_atlas_31073()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_azef_protocol_32007(unittest.TestCase):
    '''
    testing play functionality of azef_protocol
    Cost: *card has no cost*
    Text: As an additional cost to score this agenda, trash 1 of your other installed cards. When you score this agenda, do 2 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for azef_protocol_32007
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_azef_protocol_32007()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_elivagar_bifurcation_33031(unittest.TestCase):
    '''
    testing play functionality of elivagar_bifurcation
    Cost: *card has no cost*
    Text: When you score this agenda, you may derez 1 installed card.
    '''

    def setUp(self):
        '''
        setup test environment for elivagar_bifurcation_33031
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_elivagar_bifurcation_33031()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_midnight3_arcology_33032(unittest.TestCase):
    '''
    testing play functionality of midnight3_arcology
    Cost: *card has no cost*
    Text: When you score this agenda, draw 3 cards. Skip your discard step this turn.
    '''

    def setUp(self):
        '''
        setup test environment for midnight3_arcology_33032
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_midnight3_arcology_33032()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_blood_in_the_water_33039(unittest.TestCase):
    '''
    testing play functionality of blood_in_the_water
    Cost: *card has no cost*
    Text: X is equal to the number of cards in the Runner's grip.
    '''

    def setUp(self):
        '''
        setup test environment for blood_in_the_water_33039
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_blood_in_the_water_33039()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_regenesis_33040(unittest.TestCase):
    '''
    testing play functionality of regenesis
    Cost: *card has no cost*
    Text: When you score this agenda, if no Corp cards have been added to Archives this turn, you may reveal 1 facedown agenda in Archives and add it to your score area.
    '''

    def setUp(self):
        '''
        setup test environment for regenesis_33040
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_regenesis_33040()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_artificial_cryptocrash_33049(unittest.TestCase):
    '''
    testing play functionality of artificial_cryptocrash
    Cost: *card has no cost*
    Text: When you score this agenda, the Runner loses 7 credits.
    '''

    def setUp(self):
        '''
        setup test environment for artificial_cryptocrash_33049
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_artificial_cryptocrash_33049()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_azef_protocol_33058(unittest.TestCase):
    '''
    testing play functionality of azef_protocol
    Cost: *card has no cost*
    Text: As an additional cost to score this agenda, trash 1 of your other installed cards. When you score this agenda, do 2 meat damage.
    '''

    def setUp(self):
        '''
        setup test environment for azef_protocol_33058
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_azef_protocol_33058()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_ontological_dependence_33096(unittest.TestCase):
    '''
    testing play functionality of ontological_dependence
    Cost: *card has no cost*
    Text: This agenda gets -1 advancement requirement for each core damage the Runner has taken this game.
    '''

    def setUp(self):
        '''
        setup test environment for ontological_dependence_33096
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_ontological_dependence_33096()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_hybrid_release_33105(unittest.TestCase):
    '''
    testing play functionality of hybrid_release
    Cost: *card has no cost*
    Text: When you score this agenda, you may install 1 facedown card from Archives.
    '''

    def setUp(self):
        '''
        setup test environment for hybrid_release_33105
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_hybrid_release_33105()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_freedom_of_information_33112(unittest.TestCase):
    '''
    testing play functionality of freedom_of_information
    Cost: *card has no cost*
    Text: This agenda gets -1 advancement requirement for each tag the Runner has.
    '''

    def setUp(self):
        '''
        setup test environment for freedom_of_information_33112
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_freedom_of_information_33112()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_posttruth_dividend_33113(unittest.TestCase):
    '''
    testing play functionality of posttruth_dividend
    Cost: *card has no cost*
    Text: When you score this agenda, you may draw 1 card.
    '''

    def setUp(self):
        '''
        setup test environment for posttruth_dividend_33113
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_posttruth_dividend_33113()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_regulatory_capture_33120(unittest.TestCase):
    '''
    testing play functionality of regulatory_capture
    Cost: *card has no cost*
    Text: For each bad publicity you have up to 4, this agenda gets -1 advancement requirement.
    '''

    def setUp(self):
        '''
        setup test environment for regulatory_capture_33120
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_regulatory_capture_33120()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")

######################
class Test_kimberlite_field_33121(unittest.TestCase):
    '''
    testing play functionality of kimberlite_field
    Cost: *card has no cost*
    Text: When you score this agenda, you may trash 1 of your rezzed cards. If you do, trash 1 installed Runner card with a printed install cost equal to or less than the printed rez cost of the Corp card you trashed.
    '''

    def setUp(self):
        '''
        setup test environment for kimberlite_field_33121
        '''
        #create player with an appropriate test deck
        self.runner_player = Runner("runner1","empty-test-deck-runner.o8d")
        self.corpo_player = Corpo("corpo1","empty-test-deck-corpo.o8d")
        #create test game state for the proper type
        self.test_game_environment = NetrunnerGame(self.corpo_player,self.runner_player)
    
    def test_play_card(self):
        '''
        TODO
        '''
        test_card = agenda_kimberlite_field_33121()
        test_card.play(self.test_game_environment.PLAYER,self.test_game_environment)
        self.assert_(False,"test yet to be implemented")
