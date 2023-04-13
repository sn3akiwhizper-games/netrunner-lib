
'''
test cases for card classes of type resource
'''
from netrunner_lib.cards._base_card_classes import Resource
from netrunner_lib.cards.resource import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
def test_resource_ice_carver_01015():
    '''
    testing functionality of ice_carver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_ice_carver_01015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_wyldside_01016():
    '''
    testing functionality of wyldside
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_wyldside_01016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_bank_job_01029():
    '''
    testing functionality of bank_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_bank_job_01029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_crash_space_01030():
    '''
    testing functionality of crash_space
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_crash_space_01030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_data_dealer_01031():
    '''
    testing functionality of data_dealer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_data_dealer_01031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_decoy_01032():
    '''
    testing functionality of decoy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_decoy_01032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_aesops_pawnshop_01047():
    '''
    testing functionality of aesops_pawnshop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_aesops_pawnshop_01047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_sacrificial_construct_01048():
    '''
    testing functionality of sacrificial_construct
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_sacrificial_construct_01048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_access_to_globalsec_01052():
    '''
    testing functionality of access_to_globalsec
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_access_to_globalsec_01052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_armitage_codebusting_01053():
    '''
    testing functionality of armitage_codebusting
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_armitage_codebusting_01053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_helpful_ai_02008():
    '''
    testing functionality of the_helpful_ai
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_helpful_ai_02008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_liberated_account_02022():
    '''
    testing functionality of liberated_account
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_liberated_account_02022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_compromised_employee_02025():
    '''
    testing functionality of compromised_employee
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_compromised_employee_02025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_joshua_b_02042():
    '''
    testing functionality of joshua_b
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_joshua_b_02042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_personal_workshop_02049():
    '''
    testing functionality of personal_workshop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_personal_workshop_02049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_public_sympathy_02050():
    '''
    testing functionality of public_sympathy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_public_sympathy_02050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_scrubber_02063():
    '''
    testing functionality of scrubber
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_scrubber_02063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_allnighter_02067():
    '''
    testing functionality of allnighter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_allnighter_02067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_inside_man_02068():
    '''
    testing functionality of inside_man
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_inside_man_02068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_underworld_contact_02069():
    '''
    testing functionality of underworld_contact
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_underworld_contact_02069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_xanadu_02082():
    '''
    testing functionality of xanadu
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_xanadu_02082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_kati_jones_02091():
    '''
    testing functionality of kati_jones
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_kati_jones_02091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_data_leak_reversal_02103():
    '''
    testing functionality of data_leak_reversal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_data_leak_reversal_02103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_mr_li_02105():
    '''
    testing functionality of mr_li
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_mr_li_02105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_new_angeles_city_hall_02109():
    '''
    testing functionality of new_angeles_city_hall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_new_angeles_city_hall_02109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_professional_contacts_03049():
    '''
    testing functionality of professional_contacts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_professional_contacts_03049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_borrowed_satellite_03050():
    '''
    testing functionality of borrowed_satellite
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_borrowed_satellite_03050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_ice_analyzer_03051():
    '''
    testing functionality of ice_analyzer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_ice_analyzer_03051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_daily_casts_03053():
    '''
    testing functionality of daily_casts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_daily_casts_03053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_same_old_thing_03054():
    '''
    testing functionality of same_old_thing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_same_old_thing_03054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_source_03055():
    '''
    testing functionality of the_source
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_source_03055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_motivation_04008():
    '''
    testing functionality of motivation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_motivation_04008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_john_masanori_04009():
    '''
    testing functionality of john_masanori
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_john_masanori_04009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_hard_at_work_04023():
    '''
    testing functionality of hard_at_work
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_hard_at_work_04023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_grifter_04046():
    '''
    testing functionality of grifter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_grifter_04046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_woman_in_the_red_dress_04048():
    '''
    testing functionality of woman_in_the_red_dress
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_woman_in_the_red_dress_04048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_raymond_flint_04049():
    '''
    testing functionality of raymond_flint
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_raymond_flint_04049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_activist_support_04062():
    '''
    testing functionality of activist_support
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_activist_support_04062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_starlight_crusade_funding_04069():
    '''
    testing functionality of starlight_crusade_funding
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_starlight_crusade_funding_04069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_tallie_perrault_04083():
    '''
    testing functionality of tallie_perrault
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_tallie_perrault_04083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_fall_guy_04106():
    '''
    testing functionality of fall_guy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_fall_guy_04106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_security_testing_05048():
    '''
    testing functionality of security_testing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_security_testing_05048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_theophilius_bagbiter_05049():
    '''
    testing functionality of theophilius_bagbiter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_theophilius_bagbiter_05049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_trimaf_contact_05050():
    '''
    testing functionality of trimaf_contact
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_trimaf_contact_05050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_oracle_may_05054():
    '''
    testing functionality of oracle_may
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_oracle_may_05054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_donut_taganes_05055():
    '''
    testing functionality of donut_taganes
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_donut_taganes_05055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_power_tap_06016():
    '''
    testing functionality of power_tap
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_power_tap_06016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_eden_shard_06020():
    '''
    testing functionality of eden_shard
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_eden_shard_06020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_ghost_runner_06040():
    '''
    testing functionality of ghost_runner
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_ghost_runner_06040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_duggars_06054():
    '''
    testing functionality of duggars
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_duggars_06054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_supplier_06056():
    '''
    testing functionality of the_supplier
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_supplier_06056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_order_of_sol_06058():
    '''
    testing functionality of order_of_sol
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_order_of_sol_06058()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_hades_shard_06059():
    '''
    testing functionality of hades_shard
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_hades_shard_06059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_rachel_beckman_06060():
    '''
    testing functionality of rachel_beckman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_rachel_beckman_06060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_fester_06075():
    '''
    testing functionality of fester
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_fester_06075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_angel_arena_06080():
    '''
    testing functionality of angel_arena
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_angel_arena_06080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_zona_sul_shipping_06097():
    '''
    testing functionality of zona_sul_shipping
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_zona_sul_shipping_06097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_utopia_shard_06100():
    '''
    testing functionality of utopia_shard
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_utopia_shard_06100()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_earthrise_hotel_06120():
    '''
    testing functionality of earthrise_hotel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_earthrise_hotel_06120()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_human_first_07048():
    '''
    testing functionality of human_first
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_human_first_07048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_investigative_journalism_07049():
    '''
    testing functionality of investigative_journalism
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_investigative_journalism_07049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_sacrificial_clone_07050():
    '''
    testing functionality of sacrificial_clone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_sacrificial_clone_07050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_stim_dealer_07051():
    '''
    testing functionality of stim_dealer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_stim_dealer_07051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_virus_breeding_ground_07052():
    '''
    testing functionality of virus_breeding_ground
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_virus_breeding_ground_07052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_data_folding_07055():
    '''
    testing functionality of data_folding
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_data_folding_07055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_paige_piper_08002():
    '''
    testing functionality of paige_piper
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_paige_piper_08002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_adjusted_chronotype_08003():
    '''
    testing functionality of adjusted_chronotype
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_adjusted_chronotype_08003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_enhanced_vision_08005():
    '''
    testing functionality of enhanced_vision
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_enhanced_vision_08005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_gene_conditioning_shoppe_08006():
    '''
    testing functionality of gene_conditioning_shoppe
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_gene_conditioning_shoppe_08006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_synthetic_blood_08007():
    '''
    testing functionality of synthetic_blood
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_synthetic_blood_08007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_symmetrical_visage_08009():
    '''
    testing functionality of symmetrical_visage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_symmetrical_visage_08009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_offcampus_apartment_08022():
    '''
    testing functionality of offcampus_apartment
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_offcampus_apartment_08022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_london_library_08029():
    '''
    testing functionality of london_library
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_london_library_08029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_tyson_observatory_08030():
    '''
    testing functionality of tyson_observatory
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_tyson_observatory_08030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_beach_party_08031():
    '''
    testing functionality of beach_party
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_beach_party_08031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_chrome_parlor_08044():
    '''
    testing functionality of chrome_parlor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_chrome_parlor_08044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_street_peddler_08062():
    '''
    testing functionality of street_peddler
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_street_peddler_08062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_gang_sign_08067():
    '''
    testing functionality of gang_sign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_gang_sign_08067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_muertos_gang_member_08068():
    '''
    testing functionality of muertos_gang_member
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_muertos_gang_member_08068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_spoilers_08082():
    '''
    testing functionality of spoilers
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_spoilers_08082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_drug_dealer_08083():
    '''
    testing functionality of drug_dealer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_drug_dealer_08083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_rolodex_08084():
    '''
    testing functionality of rolodex
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_rolodex_08084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_fan_site_08085():
    '''
    testing functionality of fan_site
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_fan_site_08085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_film_critic_08086():
    '''
    testing functionality of film_critic
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_film_critic_08086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_paparazzi_08087():
    '''
    testing functionality of paparazzi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_paparazzi_08087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_ddos_08103():
    '''
    testing functionality of ddos
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_ddos_08103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_wireless_net_pavilion_08108():
    '''
    testing functionality of wireless_net_pavilion
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_wireless_net_pavilion_08108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_hunting_grounds_09035():
    '''
    testing functionality of hunting_grounds
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_hunting_grounds_09035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_wasteland_09036():
    '''
    testing functionality of wasteland
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_wasteland_09036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_always_be_running_09041():
    '''
    testing functionality of always_be_running
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_always_be_running_09041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_dr_lovegood_09042():
    '''
    testing functionality of dr_lovegood
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_dr_lovegood_09042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_neutralize_all_threats_09043():
    '''
    testing functionality of neutralize_all_threats
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_neutralize_all_threats_09043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_safety_first_09044():
    '''
    testing functionality of safety_first
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_safety_first_09044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_globalsec_security_clearance_09051():
    '''
    testing functionality of globalsec_security_clearance
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_globalsec_security_clearance_09051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_jak_sinclair_09052():
    '''
    testing functionality of jak_sinclair
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_jak_sinclair_09052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_technical_writer_09055():
    '''
    testing functionality of technical_writer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_technical_writer_09055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_street_magic_10003():
    '''
    testing functionality of street_magic
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_street_magic_10003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_artist_colony_10009():
    '''
    testing functionality of artist_colony
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_artist_colony_10009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_chatterjee_university_10010():
    '''
    testing functionality of chatterjee_university
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_chatterjee_university_10010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_tech_trader_10023():
    '''
    testing functionality of tech_trader
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_tech_trader_10023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_political_operative_10043():
    '''
    testing functionality of political_operative
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_political_operative_10043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_akshara_sareen_10046():
    '''
    testing functionality of akshara_sareen
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_akshara_sareen_10046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_councilman_10047():
    '''
    testing functionality of councilman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_councilman_10047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_salsette_slums_10059():
    '''
    testing functionality of salsette_slums
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_salsette_slums_10059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_patron_10063():
    '''
    testing functionality of patron
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_patron_10063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_bazaar_10065():
    '''
    testing functionality of bazaar
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_bazaar_10065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_emptied_mind_10078():
    '''
    testing functionality of emptied_mind
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_emptied_mind_10078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_liberated_chela_10081():
    '''
    testing functionality of liberated_chela
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_liberated_chela_10081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_temple_of_the_liberated_mind_10082():
    '''
    testing functionality of temple_of_the_liberated_mind
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_temple_of_the_liberated_mind_10082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_guru_davinder_10084():
    '''
    testing functionality of guru_davinder
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_guru_davinder_10084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_turning_wheel_10085():
    '''
    testing functionality of the_turning_wheel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_turning_wheel_10085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_bhagat_10098():
    '''
    testing functionality of bhagat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_bhagat_10098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_black_file_10099():
    '''
    testing functionality of the_black_file
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_black_file_10099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_hernando_cortez_11004():
    '''
    testing functionality of hernando_cortez
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_hernando_cortez_11004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_temujin_contract_11026():
    '''
    testing functionality of temujin_contract
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_temujin_contract_11026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_algo_trading_11029():
    '''
    testing functionality of algo_trading
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_algo_trading_11029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_beth_kilrainchang_11030():
    '''
    testing functionality of beth_kilrainchang
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_beth_kilrainchang_11030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_net_mercur_11046():
    '''
    testing functionality of net_mercur
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_net_mercur_11046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_find_the_truth_11047():
    '''
    testing functionality of find_the_truth
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_find_the_truth_11047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_first_responders_11048():
    '''
    testing functionality of first_responders
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_first_responders_11048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_blockade_runner_11065():
    '''
    testing functionality of blockade_runner
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_blockade_runner_11065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_citadel_sanctuary_11070():
    '''
    testing functionality of citadel_sanctuary
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_citadel_sanctuary_11070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_aaron_marron_11106():
    '''
    testing functionality of aaron_marron
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_aaron_marron_11106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_archivist_12003():
    '''
    testing functionality of the_archivist
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_archivist_12003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_biomodeled_network_12006():
    '''
    testing functionality of biomodeled_network
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_biomodeled_network_12006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_network_exchange_12007():
    '''
    testing functionality of network_exchange
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_network_exchange_12007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_clan_vengeance_12022():
    '''
    testing functionality of clan_vengeance
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_clan_vengeance_12022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_counter_surveillance_12023():
    '''
    testing functionality of counter_surveillance
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_counter_surveillance_12023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_aeneas_informant_12044():
    '''
    testing functionality of aeneas_informant
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_aeneas_informant_12044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_rosetta_20_12045():
    '''
    testing functionality of rosetta_20
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_rosetta_20_12045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_dadiana_chacon_12049():
    '''
    testing functionality of dadiana_chacon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_dadiana_chacon_12049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_jarogniew_mercs_12062():
    '''
    testing functionality of jarogniew_mercs
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_jarogniew_mercs_12062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_bug_out_bag_12064():
    '''
    testing functionality of bug_out_bag
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_bug_out_bag_12064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_keros_mcintyre_12065():
    '''
    testing functionality of keros_mcintyre
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_keros_mcintyre_12065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_bloo_moose_12089():
    '''
    testing functionality of bloo_moose
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_bloo_moose_12089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_salvaged_vanadis_armory_12103():
    '''
    testing functionality of salvaged_vanadis_armory
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_salvaged_vanadis_armory_12103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_caldera_12105():
    '''
    testing functionality of caldera
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_caldera_12105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_dummy_box_12108():
    '''
    testing functionality of dummy_box
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_dummy_box_12108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_corporate_defector_12109():
    '''
    testing functionality of corporate_defector
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_corporate_defector_12109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_charlatan_13010():
    '''
    testing functionality of charlatan
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_charlatan_13010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_maxwell_james_13011():
    '''
    testing functionality of maxwell_james
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_maxwell_james_13011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_levy_advanced_research_lab_13021():
    '''
    testing functionality of levy_advanced_research_lab
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_levy_advanced_research_lab_13021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_laguna_velasco_district_13022():
    '''
    testing functionality of laguna_velasco_district
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_laguna_velasco_district_13022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_officer_frank_13024():
    '''
    testing functionality of officer_frank
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_officer_frank_13024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_dean_lister_13025():
    '''
    testing functionality of dean_lister
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_dean_lister_13025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_biometric_spoofing_13026():
    '''
    testing functionality of biometric_spoofing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_biometric_spoofing_13026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_shadow_net_13027():
    '''
    testing functionality of the_shadow_net
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_shadow_net_13027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_investigator_inez_delgado_14014():
    '''
    testing functionality of investigator_inez_delgado
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_investigator_inez_delgado_14014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_investigator_inez_delgado_2_14015():
    '''
    testing functionality of investigator_inez_delgado_2
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_investigator_inez_delgado_2_14015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_investigator_inez_delgado_3_14016():
    '''
    testing functionality of investigator_inez_delgado_3
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_investigator_inez_delgado_3_14016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_investigator_inez_delgado_4_14017():
    '''
    testing functionality of investigator_inez_delgado_4
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_investigator_inez_delgado_4_14017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_shadow_team_14022():
    '''
    testing functionality of shadow_team
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_shadow_team_14022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_masque_a_14024():
    '''
    testing functionality of the_masque_a
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_masque_a_14024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_masque_b_14025():
    '''
    testing functionality of the_masque_b
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_masque_b_14025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_ice_carver_20015():
    '''
    testing functionality of ice_carver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_ice_carver_20015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_liberated_account_20016():
    '''
    testing functionality of liberated_account
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_liberated_account_20016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_scrubber_20017():
    '''
    testing functionality of scrubber
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_scrubber_20017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_xanadu_20018():
    '''
    testing functionality of xanadu
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_xanadu_20018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_bank_job_20033():
    '''
    testing functionality of bank_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_bank_job_20033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_crash_space_20034():
    '''
    testing functionality of crash_space
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_crash_space_20034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_fall_guy_20035():
    '''
    testing functionality of fall_guy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_fall_guy_20035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_mr_li_20036():
    '''
    testing functionality of mr_li
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_mr_li_20036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_aesops_pawnshop_20052():
    '''
    testing functionality of aesops_pawnshop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_aesops_pawnshop_20052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_allnighter_20053():
    '''
    testing functionality of allnighter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_allnighter_20053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_sacrificial_construct_20054():
    '''
    testing functionality of sacrificial_construct
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_sacrificial_construct_20054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_armitage_codebusting_20059():
    '''
    testing functionality of armitage_codebusting
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_armitage_codebusting_20059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_underworld_contact_20060():
    '''
    testing functionality of underworld_contact
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_underworld_contact_20060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_lewi_guilherme_21005():
    '''
    testing functionality of lewi_guilherme
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_lewi_guilherme_21005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_assimilator_21008():
    '''
    testing functionality of assimilator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_assimilator_21008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_kongamato_21027():
    '''
    testing functionality of kongamato
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_kongamato_21027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_crypt_21043():
    '''
    testing functionality of crypt
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_crypt_21043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_no_one_home_21045():
    '''
    testing functionality of no_one_home
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_no_one_home_21045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_gbahali_21047():
    '''
    testing functionality of gbahali
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_gbahali_21047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_rogue_trading_21065():
    '''
    testing functionality of rogue_trading
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_rogue_trading_21065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_slipstream_21085():
    '''
    testing functionality of slipstream
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_slipstream_21085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_logic_bomb_21089():
    '''
    testing functionality of logic_bomb
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_logic_bomb_21089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_jackpot_21090():
    '''
    testing functionality of jackpot
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_jackpot_21090()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_pad_tap_21106():
    '''
    testing functionality of pad_tap
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_pad_tap_21106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_reclaim_21107():
    '''
    testing functionality of reclaim
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_reclaim_21107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_kasi_string_21111():
    '''
    testing functionality of kasi_string
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_kasi_string_21111()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_district_99_22007():
    '''
    testing functionality of district_99
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_district_99_22007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_thunder_art_gallery_22013():
    '''
    testing functionality of thunder_art_gallery
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_thunder_art_gallery_22013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_miss_bones_22014():
    '''
    testing functionality of miss_bones
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_miss_bones_22014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_psych_mike_22021():
    '''
    testing functionality of psych_mike
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_psych_mike_22021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_dj_fenris_22025():
    '''
    testing functionality of dj_fenris
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_dj_fenris_22025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_crowdfunding_23013():
    '''
    testing functionality of crowdfunding
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_crowdfunding_23013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_ice_carver_25016():
    '''
    testing functionality of ice_carver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_ice_carver_25016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_liberated_account_25017():
    '''
    testing functionality of liberated_account
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_liberated_account_25017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_scrubber_25018():
    '''
    testing functionality of scrubber
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_scrubber_25018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_xanadu_25019():
    '''
    testing functionality of xanadu
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_xanadu_25019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_bank_job_25038():
    '''
    testing functionality of bank_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_bank_job_25038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_data_dealer_25039():
    '''
    testing functionality of data_dealer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_data_dealer_25039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_aesops_pawnshop_25056():
    '''
    testing functionality of aesops_pawnshop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_aesops_pawnshop_25056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_ice_analyzer_25057():
    '''
    testing functionality of ice_analyzer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_ice_analyzer_25057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_professional_contacts_25058():
    '''
    testing functionality of professional_contacts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_professional_contacts_25058()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_armitage_codebusting_25062():
    '''
    testing functionality of armitage_codebusting
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_armitage_codebusting_25062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_earthrise_hotel_25063():
    '''
    testing functionality of earthrise_hotel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_earthrise_hotel_25063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_john_masanori_25064():
    '''
    testing functionality of john_masanori
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_john_masanori_25064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_kati_jones_25065():
    '''
    testing functionality of kati_jones
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_kati_jones_25065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_climactic_showdown_26006():
    '''
    testing functionality of climactic_showdown
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_climactic_showdown_26006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_fencer_fueno_26007():
    '''
    testing functionality of fencer_fueno
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_fencer_fueno_26007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_nihilist_26008():
    '''
    testing functionality of the_nihilist
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_nihilist_26008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_trickster_taka_26009():
    '''
    testing functionality of trickster_taka
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_trickster_taka_26009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_baklan_bochkin_26017():
    '''
    testing functionality of baklan_bochkin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_baklan_bochkin_26017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_class_act_26018():
    '''
    testing functionality of the_class_act
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_class_act_26018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_artist_26027():
    '''
    testing functionality of the_artist
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_artist_26027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_whistleblower_26030():
    '''
    testing functionality of whistleblower
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_whistleblower_26030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_mystic_maemi_26072():
    '''
    testing functionality of mystic_maemi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_mystic_maemi_26072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_paladin_poemu_26073():
    '''
    testing functionality of paladin_poemu
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_paladin_poemu_26073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_penumbral_toolkit_26081():
    '''
    testing functionality of penumbral_toolkit
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_penumbral_toolkit_26081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_back_26082():
    '''
    testing functionality of the_back
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_back_26082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_cybertrooper_talut_26091():
    '''
    testing functionality of cybertrooper_talut
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_cybertrooper_talut_26091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_paules_cafe_26092():
    '''
    testing functionality of paules_cafe
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_paules_cafe_26092()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_daily_casts_26094():
    '''
    testing functionality of daily_casts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_daily_casts_26094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_dreamnet_26095():
    '''
    testing functionality of dreamnet
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_dreamnet_26095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_mystic_maemi_27001():
    '''
    testing functionality of mystic_maemi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_mystic_maemi_27001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_cybertrooper_talut_27003():
    '''
    testing functionality of cybertrooper_talut
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_cybertrooper_talut_27003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_crowdfunding_28002():
    '''
    testing functionality of crowdfunding
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_crowdfunding_28002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_cookbook_30009():
    '''
    testing functionality of cookbook
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_cookbook_30009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_red_team_30018():
    '''
    testing functionality of red_team
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_red_team_30018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_telework_contract_30027():
    '''
    testing functionality of telework_contract
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_telework_contract_30027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_smartware_distributor_30033():
    '''
    testing functionality of smartware_distributor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_smartware_distributor_30033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_verbal_plasticity_30034():
    '''
    testing functionality of verbal_plasticity
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_verbal_plasticity_30034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_ice_carver_31009():
    '''
    testing functionality of ice_carver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_ice_carver_31009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_liberated_account_31010():
    '''
    testing functionality of liberated_account
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_liberated_account_31010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_scrubber_31011():
    '''
    testing functionality of scrubber
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_scrubber_31011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_xanadu_31012():
    '''
    testing functionality of xanadu
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_xanadu_31012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_security_testing_31024():
    '''
    testing functionality of security_testing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_security_testing_31024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_aesops_pawnshop_31035():
    '''
    testing functionality of aesops_pawnshop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_aesops_pawnshop_31035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_professional_contacts_31036():
    '''
    testing functionality of professional_contacts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_professional_contacts_31036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_earthrise_hotel_31039():
    '''
    testing functionality of earthrise_hotel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_earthrise_hotel_31039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_light_the_fire_32001():
    '''
    testing functionality of light_the_fire
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_light_the_fire_32001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_avgustina_ivanovskaya_33008():
    '''
    testing functionality of avgustina_ivanovskaya
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_avgustina_ivanovskaya_33008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_light_the_fire_33009():
    '''
    testing functionality of light_the_fire
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_light_the_fire_33009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_the_twinning_33010():
    '''
    testing functionality of the_twinning
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_the_twinning_33010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_backstitching_33019():
    '''
    testing functionality of backstitching
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_backstitching_33019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_no_free_lunch_33020():
    '''
    testing functionality of no_free_lunch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_no_free_lunch_33020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_daeg_first_netcat_33028():
    '''
    testing functionality of daeg_first_netcat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_daeg_first_netcat_33028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_environmental_testing_33029():
    '''
    testing functionality of environmental_testing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_environmental_testing_33029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_stoneship_chart_room_33030():
    '''
    testing functionality of stoneship_chart_room
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_stoneship_chart_room_33030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_tsakhia_bankhar_gantulga_33074():
    '''
    testing functionality of tsakhia_bankhar_gantulga
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_tsakhia_bankhar_gantulga_33074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_asmund_pudlat_33082():
    '''
    testing functionality of asmund_pudlat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_asmund_pudlat_33082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_info_bounty_33083():
    '''
    testing functionality of info_bounty
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_info_bounty_33083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_resource_dr_nuka_vrolyck_33092():
    '''
    testing functionality of dr_nuka_vrolyck
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("resource")

    test_card = resource_dr_nuka_vrolyck_33092()
    test_card.play(test_game_environment.runner,test_game_environment)
