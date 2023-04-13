
'''
test cases for card classes of type agenda
'''
from netrunner_lib.cards._base_card_classes import Agenda
from netrunner_lib.cards.agenda import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
def test_agenda_accelerated_beta_test_01055():
    '''
    testing functionality of accelerated_beta_test
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_accelerated_beta_test_01055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_nisei_mk_ii_01068():
    '''
    testing functionality of nisei_mk_ii
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_nisei_mk_ii_01068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_astroscript_pilot_program_01081():
    '''
    testing functionality of astroscript_pilot_program
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_astroscript_pilot_program_01081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_breaking_news_01082():
    '''
    testing functionality of breaking_news
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_breaking_news_01082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_hostile_takeover_01094():
    '''
    testing functionality of hostile_takeover
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_hostile_takeover_01094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_posted_bounty_01095():
    '''
    testing functionality of posted_bounty
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_posted_bounty_01095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_priority_requisition_01106():
    '''
    testing functionality of priority_requisition
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_priority_requisition_01106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_private_security_force_01107():
    '''
    testing functionality of private_security_force
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_private_security_force_01107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_mandatory_upgrades_02011():
    '''
    testing functionality of mandatory_upgrades
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_mandatory_upgrades_02011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_braintrust_02014():
    '''
    testing functionality of braintrust
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_braintrust_02014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_restructured_datapool_02016():
    '''
    testing functionality of restructured_datapool
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_restructured_datapool_02016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_atlas_02018():
    '''
    testing functionality of project_atlas
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_atlas_02018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_fetal_ai_02032():
    '''
    testing functionality of fetal_ai
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_fetal_ai_02032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_executive_retreat_02039():
    '''
    testing functionality of executive_retreat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_executive_retreat_02039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_vitruvius_02051():
    '''
    testing functionality of project_vitruvius
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_vitruvius_02051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_government_contracts_02077():
    '''
    testing functionality of government_contracts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_government_contracts_02077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_false_lead_02080():
    '''
    testing functionality of false_lead
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_false_lead_02080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_beale_02115():
    '''
    testing functionality of project_beale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_beale_02115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_corporate_war_02120():
    '''
    testing functionality of corporate_war
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_corporate_war_02120()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_director_haas_pet_project_03004():
    '''
    testing functionality of director_haas_pet_project
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_director_haas_pet_project_03004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_efficiency_committee_03005():
    '''
    testing functionality of efficiency_committee
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_efficiency_committee_03005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_wotan_03006():
    '''
    testing functionality of project_wotan
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_wotan_03006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_sentinel_defense_program_03007():
    '''
    testing functionality of sentinel_defense_program
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_sentinel_defense_program_03007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_gila_hands_arcology_03023():
    '''
    testing functionality of gila_hands_arcology
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_gila_hands_arcology_03023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_ares_04010():
    '''
    testing functionality of project_ares
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_ares_04010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_character_assassination_04014():
    '''
    testing functionality of character_assassination
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_character_assassination_04014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_geothermal_fracking_04017():
    '''
    testing functionality of geothermal_fracking
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_geothermal_fracking_04017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_clone_retirement_04032():
    '''
    testing functionality of clone_retirement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_clone_retirement_04032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_the_cleaners_04036():
    '''
    testing functionality of the_cleaners
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_the_cleaners_04036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_profiteering_04039():
    '''
    testing functionality of profiteering
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_profiteering_04039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_unorthodox_predictions_04053():
    '''
    testing functionality of unorthodox_predictions
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_unorthodox_predictions_04053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_tgtbt_04075():
    '''
    testing functionality of tgtbt
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_tgtbt_04075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_veterans_program_04080():
    '''
    testing functionality of veterans_program
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_veterans_program_04080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_market_research_04095():
    '''
    testing functionality of market_research
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_market_research_04095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_vulcan_coverup_04098():
    '''
    testing functionality of vulcan_coverup
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_vulcan_coverup_04098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_napd_contract_04119():
    '''
    testing functionality of napd_contract
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_napd_contract_04119()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_house_of_knives_05004():
    '''
    testing functionality of house_of_knives
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_house_of_knives_05004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_medical_breakthrough_05005():
    '''
    testing functionality of medical_breakthrough
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_medical_breakthrough_05005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_philotic_entanglement_05006():
    '''
    testing functionality of philotic_entanglement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_philotic_entanglement_05006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_the_future_perfect_05007():
    '''
    testing functionality of the_future_perfect
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_the_future_perfect_05007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_domestic_sleepers_06001():
    '''
    testing functionality of domestic_sleepers
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_domestic_sleepers_06001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_encrypted_portals_06024():
    '''
    testing functionality of encrypted_portals
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_encrypted_portals_06024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_eden_fragment_06030():
    '''
    testing functionality of eden_fragment
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_eden_fragment_06030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_chronos_project_06049():
    '''
    testing functionality of chronos_project
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_chronos_project_06049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_labyrinthine_servers_06063():
    '''
    testing functionality of labyrinthine_servers
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_labyrinthine_servers_06063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_hades_fragment_06071():
    '''
    testing functionality of hades_fragment
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_hades_fragment_06071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_bifrost_array_06081():
    '''
    testing functionality of bifrost_array
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_bifrost_array_06081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_license_acquisition_06085():
    '''
    testing functionality of license_acquisition
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_license_acquisition_06085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_superior_cyberwalls_06087():
    '''
    testing functionality of superior_cyberwalls
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_superior_cyberwalls_06087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_helium3_deposit_06101():
    '''
    testing functionality of helium3_deposit
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_helium3_deposit_06101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_utopia_fragment_06110():
    '''
    testing functionality of utopia_fragment
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_utopia_fragment_06110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_firmware_updates_07004():
    '''
    testing functionality of firmware_updates
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_firmware_updates_07004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_glenn_station_07005():
    '''
    testing functionality of glenn_station
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_glenn_station_07005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_government_takeover_07006():
    '''
    testing functionality of government_takeover
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_government_takeover_07006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_highrisk_investment_07007():
    '''
    testing functionality of highrisk_investment
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_highrisk_investment_07007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_genetic_resequencing_08013():
    '''
    testing functionality of genetic_resequencing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_genetic_resequencing_08013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_research_grant_08032():
    '''
    testing functionality of research_grant
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_research_grant_08032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_selfdestruct_chips_08051():
    '''
    testing functionality of selfdestruct_chips
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_selfdestruct_chips_08051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_oaktown_renovation_08058():
    '''
    testing functionality of oaktown_renovation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_oaktown_renovation_08058()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_underway_renovation_08077():
    '''
    testing functionality of underway_renovation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_underway_renovation_08077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_award_bait_08093():
    '''
    testing functionality of award_bait
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_award_bait_08093()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_explodeapalooza_08094():
    '''
    testing functionality of explodeapalooza
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_explodeapalooza_08094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_hollywood_renovation_08098():
    '''
    testing functionality of hollywood_renovation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_hollywood_renovation_08098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_vanity_project_08100():
    '''
    testing functionality of vanity_project
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_vanity_project_08100()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_ancestral_imager_08112():
    '''
    testing functionality of ancestral_imager
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_ancestral_imager_08112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_the_future_is_now_08120():
    '''
    testing functionality of the_future_is_now
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_the_future_is_now_08120()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_15_minutes_09004():
    '''
    testing functionality of 15_minutes
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_15_minutes_09004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_improved_tracers_09005():
    '''
    testing functionality of improved_tracers
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_improved_tracers_09005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_rebranding_team_09006():
    '''
    testing functionality of rebranding_team
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_rebranding_team_09006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_quantum_predictive_model_09007():
    '''
    testing functionality of quantum_predictive_model
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_quantum_predictive_model_09007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_global_food_initiative_09026():
    '''
    testing functionality of global_food_initiative
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_global_food_initiative_09026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_advanced_concept_hopper_10011():
    '''
    testing functionality of advanced_concept_hopper
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_advanced_concept_hopper_10011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_remote_data_farm_10033():
    '''
    testing functionality of remote_data_farm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_remote_data_farm_10033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_new_construction_10035():
    '''
    testing functionality of new_construction
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_new_construction_10035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_corporate_sales_team_10037():
    '''
    testing functionality of corporate_sales_team
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_corporate_sales_team_10037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_voting_machine_initiative_10048():
    '''
    testing functionality of voting_machine_initiative
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_voting_machine_initiative_10048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_personality_profiles_10066():
    '''
    testing functionality of personality_profiles
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_personality_profiles_10066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_dedicated_neural_net_10088():
    '''
    testing functionality of dedicated_neural_net
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_dedicated_neural_net_10088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_puppet_master_10090():
    '''
    testing functionality of puppet_master
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_puppet_master_10090()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_improved_protein_source_10105():
    '''
    testing functionality of improved_protein_source
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_improved_protein_source_10105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_merger_10114():
    '''
    testing functionality of merger
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_merger_10114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_crisis_management_11018():
    '''
    testing functionality of crisis_management
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_crisis_management_11018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_kusanagi_11052():
    '''
    testing functionality of project_kusanagi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_kusanagi_11052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_show_of_force_11099():
    '''
    testing functionality of show_of_force
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_show_of_force_11099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_sensor_net_activation_11110():
    '''
    testing functionality of sensor_net_activation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_sensor_net_activation_11110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_net_quarantine_11114():
    '''
    testing functionality of net_quarantine
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_net_quarantine_11114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_next_wave_2_12009():
    '''
    testing functionality of next_wave_2
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_next_wave_2_12009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_obokata_protocol_12070():
    '''
    testing functionality of obokata_protocol
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_obokata_protocol_12070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_escalate_vitriol_12073():
    '''
    testing functionality of escalate_vitriol
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_escalate_vitriol_12073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_reeducation_12074():
    '''
    testing functionality of reeducation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_reeducation_12074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_meteor_mining_12076():
    '''
    testing functionality of meteor_mining
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_meteor_mining_12076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_standoff_12077():
    '''
    testing functionality of standoff
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_standoff_12077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_mandatory_seed_replacement_12092():
    '''
    testing functionality of mandatory_seed_replacement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_mandatory_seed_replacement_12092()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_water_monopoly_12093():
    '''
    testing functionality of water_monopoly
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_water_monopoly_12093()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_cfc_excavation_contract_12110():
    '''
    testing functionality of cfc_excavation_contract
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_cfc_excavation_contract_12110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_arenhanced_security_12115():
    '''
    testing functionality of arenhanced_security
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_arenhanced_security_12115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_brain_rewiring_13029():
    '''
    testing functionality of brain_rewiring
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_brain_rewiring_13029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_elective_upgrade_13030():
    '''
    testing functionality of elective_upgrade
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_elective_upgrade_13030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_successful_field_test_13031():
    '''
    testing functionality of successful_field_test
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_successful_field_test_13031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_armored_servers_13042():
    '''
    testing functionality of armored_servers
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_armored_servers_13042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_illicit_sales_13043():
    '''
    testing functionality of illicit_sales
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_illicit_sales_13043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_graft_13044():
    '''
    testing functionality of graft
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_graft_13044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_paper_trail_13053():
    '''
    testing functionality of paper_trail
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_paper_trail_13053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_evidence_collection_14000():
    '''
    testing functionality of evidence_collection
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_evidence_collection_14000()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_evidence_collection_2_14001():
    '''
    testing functionality of evidence_collection_2
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_evidence_collection_2_14001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_evidence_collection_3_14002():
    '''
    testing functionality of evidence_collection_3
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_evidence_collection_3_14002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_evidence_collection_4_14003():
    '''
    testing functionality of evidence_collection_4
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_evidence_collection_4_14003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_corporate_oversight_a_14012():
    '''
    testing functionality of corporate_oversight_a
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_corporate_oversight_a_14012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_corporate_oversight_b_14013():
    '''
    testing functionality of corporate_oversight_b
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_corporate_oversight_b_14013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_ares_20062():
    '''
    testing functionality of project_ares
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_ares_20062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_vitruvius_20063():
    '''
    testing functionality of project_vitruvius
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_vitruvius_20063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_hostile_takeover_20078():
    '''
    testing functionality of hostile_takeover
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_hostile_takeover_20078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_atlas_20079():
    '''
    testing functionality of project_atlas
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_atlas_20079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_the_cleaners_20080():
    '''
    testing functionality of the_cleaners
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_the_cleaners_20080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_braintrust_20094():
    '''
    testing functionality of braintrust
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_braintrust_20094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_nisei_mk_ii_20095():
    '''
    testing functionality of nisei_mk_ii
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_nisei_mk_ii_20095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_beale_20110():
    '''
    testing functionality of project_beale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_beale_20110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_tgtbt_20111():
    '''
    testing functionality of tgtbt
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_tgtbt_20111()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_false_lead_20124():
    '''
    testing functionality of false_lead
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_false_lead_20124()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_priority_requisition_20125():
    '''
    testing functionality of priority_requisition
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_priority_requisition_20125()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_private_security_force_20126():
    '''
    testing functionality of private_security_force
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_private_security_force_20126()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_ikawah_project_21010():
    '''
    testing functionality of ikawah_project
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_ikawah_project_21010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_bacterial_programming_21033():
    '''
    testing functionality of bacterial_programming
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_bacterial_programming_21033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_ssl_endorsement_21038():
    '''
    testing functionality of ssl_endorsement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_ssl_endorsement_21038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_degree_mill_21055():
    '''
    testing functionality of degree_mill
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_degree_mill_21055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_armed_intimidation_21057():
    '''
    testing functionality of armed_intimidation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_armed_intimidation_21057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_city_works_project_21078():
    '''
    testing functionality of city_works_project
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_city_works_project_21078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_remote_enforcement_21091():
    '''
    testing functionality of remote_enforcement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_remote_enforcement_21091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_viral_weaponization_21094():
    '''
    testing functionality of viral_weaponization
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_viral_weaponization_21094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_better_citizen_program_21116():
    '''
    testing functionality of better_citizen_program
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_better_citizen_program_21116()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_hyperloop_extension_22027():
    '''
    testing functionality of hyperloop_extension
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_hyperloop_extension_22027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_jumon_22035():
    '''
    testing functionality of jumon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_jumon_22035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_fly_on_the_wall_22043():
    '''
    testing functionality of fly_on_the_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_fly_on_the_wall_22043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_broad_daylight_22051():
    '''
    testing functionality of broad_daylight
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_broad_daylight_22051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_timely_public_release_23027():
    '''
    testing functionality of timely_public_release
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_timely_public_release_23027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_vitruvius_25068():
    '''
    testing functionality of project_vitruvius
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_vitruvius_25068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_successful_field_test_25069():
    '''
    testing functionality of successful_field_test
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_successful_field_test_25069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_fetal_ai_25086():
    '''
    testing functionality of fetal_ai
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_fetal_ai_25086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_nisei_mk_ii_25087():
    '''
    testing functionality of nisei_mk_ii
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_nisei_mk_ii_25087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_philotic_entanglement_25088():
    '''
    testing functionality of philotic_entanglement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_philotic_entanglement_25088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_explodeapalooza_25106():
    '''
    testing functionality of explodeapalooza
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_explodeapalooza_25106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_beale_25107():
    '''
    testing functionality of project_beale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_beale_25107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_hostile_takeover_25124():
    '''
    testing functionality of hostile_takeover
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_hostile_takeover_25124()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_oaktown_renovation_25125():
    '''
    testing functionality of oaktown_renovation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_oaktown_renovation_25125()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_atlas_25126():
    '''
    testing functionality of project_atlas
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_atlas_25126()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_paper_trail_25140():
    '''
    testing functionality of paper_trail
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_paper_trail_25140()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_priority_requisition_25141():
    '''
    testing functionality of priority_requisition
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_priority_requisition_25141()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_architect_deployment_test_26032():
    '''
    testing functionality of architect_deployment_test
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_architect_deployment_test_26032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_yagiuda_26040():
    '''
    testing functionality of project_yagiuda
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_yagiuda_26040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_sting_26041():
    '''
    testing functionality of sting
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_sting_26041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_remastered_edition_26047():
    '''
    testing functionality of remastered_edition
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_remastered_edition_26047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_divested_trust_26055():
    '''
    testing functionality of divested_trust
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_divested_trust_26055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_sds_drone_deployment_26056():
    '''
    testing functionality of sds_drone_deployment
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_sds_drone_deployment_26056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_vulnerability_audit_26063():
    '''
    testing functionality of vulnerability_audit
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_vulnerability_audit_26063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_megaprix_qualifier_26096():
    '''
    testing functionality of megaprix_qualifier
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_megaprix_qualifier_26096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_vacheron_26097():
    '''
    testing functionality of project_vacheron
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_vacheron_26097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_flower_sermon_26106():
    '''
    testing functionality of flower_sermon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_flower_sermon_26106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_bellona_26114():
    '''
    testing functionality of bellona
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_bellona_26114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_transport_monopoly_26121():
    '''
    testing functionality of transport_monopoly
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_transport_monopoly_26121()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_cyberdex_sandbox_26128():
    '''
    testing functionality of cyberdex_sandbox
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_cyberdex_sandbox_26128()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_false_lead_26129():
    '''
    testing functionality of false_lead
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_false_lead_26129()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_megaprix_qualifier_27004():
    '''
    testing functionality of megaprix_qualifier
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_megaprix_qualifier_27004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_timely_public_release_28006():
    '''
    testing functionality of timely_public_release
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_timely_public_release_28006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_luminal_transubstantiation_30036():
    '''
    testing functionality of luminal_transubstantiation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_luminal_transubstantiation_30036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_longevity_serum_30044():
    '''
    testing functionality of longevity_serum
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_longevity_serum_30044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_tomorrows_headline_30052():
    '''
    testing functionality of tomorrows_headline
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_tomorrows_headline_30052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_above_the_law_30060():
    '''
    testing functionality of above_the_law
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_above_the_law_30060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_offworld_office_30067():
    '''
    testing functionality of offworld_office
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_offworld_office_30067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_orbital_superiority_30068():
    '''
    testing functionality of orbital_superiority
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_orbital_superiority_30068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_send_a_message_30069():
    '''
    testing functionality of send_a_message
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_send_a_message_30069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_superconducting_hub_30070():
    '''
    testing functionality of superconducting_hub
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_superconducting_hub_30070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_vitruvius_31041():
    '''
    testing functionality of project_vitruvius
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_vitruvius_31041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_house_of_knives_31051():
    '''
    testing functionality of house_of_knives
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_house_of_knives_31051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_nisei_mk_ii_31052():
    '''
    testing functionality of nisei_mk_ii
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_nisei_mk_ii_31052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_license_acquisition_31061():
    '''
    testing functionality of license_acquisition
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_license_acquisition_31061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_beale_31062():
    '''
    testing functionality of project_beale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_beale_31062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_hostile_takeover_31071():
    '''
    testing functionality of hostile_takeover
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_hostile_takeover_31071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_oaktown_renovation_31072():
    '''
    testing functionality of oaktown_renovation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_oaktown_renovation_31072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_project_atlas_31073():
    '''
    testing functionality of project_atlas
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_project_atlas_31073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_azef_protocol_32007():
    '''
    testing functionality of azef_protocol
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_azef_protocol_32007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_elivagar_bifurcation_33031():
    '''
    testing functionality of elivagar_bifurcation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_elivagar_bifurcation_33031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_midnight3_arcology_33032():
    '''
    testing functionality of midnight3_arcology
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_midnight3_arcology_33032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_blood_in_the_water_33039():
    '''
    testing functionality of blood_in_the_water
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_blood_in_the_water_33039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_regenesis_33040():
    '''
    testing functionality of regenesis
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_regenesis_33040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_artificial_cryptocrash_33049():
    '''
    testing functionality of artificial_cryptocrash
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_artificial_cryptocrash_33049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_azef_protocol_33058():
    '''
    testing functionality of azef_protocol
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_azef_protocol_33058()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_ontological_dependence_33096():
    '''
    testing functionality of ontological_dependence
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_ontological_dependence_33096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_hybrid_release_33105():
    '''
    testing functionality of hybrid_release
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_hybrid_release_33105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_freedom_of_information_33112():
    '''
    testing functionality of freedom_of_information
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_freedom_of_information_33112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_posttruth_dividend_33113():
    '''
    testing functionality of posttruth_dividend
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_posttruth_dividend_33113()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_regulatory_capture_33120():
    '''
    testing functionality of regulatory_capture
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_regulatory_capture_33120()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_agenda_kimberlite_field_33121():
    '''
    testing functionality of kimberlite_field
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("agenda")

    test_card = agenda_kimberlite_field_33121()
    test_card.play(test_game_environment.runner,test_game_environment)
