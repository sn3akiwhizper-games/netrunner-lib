
'''
test cases for card classes of type event
'''
from netrunner_lib.cards._base_card_classes import Event
from netrunner_lib.cards.event import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
def test_event_deja_vu_01002():
    '''
    testing functionality of deja_vu
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_deja_vu_01002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_demolition_run_01003():
    '''
    testing functionality of demolition_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_demolition_run_01003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_stimhack_01004():
    '''
    testing functionality of stimhack
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_stimhack_01004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_account_siphon_01018():
    '''
    testing functionality of account_siphon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_account_siphon_01018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_easy_mark_01019():
    '''
    testing functionality of easy_mark
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_easy_mark_01019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_forged_activation_orders_01020():
    '''
    testing functionality of forged_activation_orders
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_forged_activation_orders_01020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_inside_job_01021():
    '''
    testing functionality of inside_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_inside_job_01021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_special_order_01022():
    '''
    testing functionality of special_order
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_special_order_01022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_diesel_01034():
    '''
    testing functionality of diesel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_diesel_01034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_modded_01035():
    '''
    testing functionality of modded
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_modded_01035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_the_makers_eye_01036():
    '''
    testing functionality of the_makers_eye
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_the_makers_eye_01036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_tinkering_01037():
    '''
    testing functionality of tinkering
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_tinkering_01037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_infiltration_01049():
    '''
    testing functionality of infiltration
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_infiltration_01049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_sure_gamble_01050():
    '''
    testing functionality of sure_gamble
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_sure_gamble_01050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_vamp_02021():
    '''
    testing functionality of vamp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_vamp_02021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_satellite_uplink_02023():
    '''
    testing functionality of satellite_uplink
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_satellite_uplink_02023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_notoriety_02026():
    '''
    testing functionality of notoriety
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_notoriety_02026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_emergency_shutdown_02043():
    '''
    testing functionality of emergency_shutdown
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_emergency_shutdown_02043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_test_run_02047():
    '''
    testing functionality of test_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_test_run_02047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_surge_02081():
    '''
    testing functionality of surge
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_surge_02081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_networking_02084():
    '''
    testing functionality of networking
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_networking_02084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_quality_time_02087():
    '''
    testing functionality of quality_time
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_quality_time_02087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_kraken_02090():
    '''
    testing functionality of kraken
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_kraken_02090()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_retrieval_run_02101():
    '''
    testing functionality of retrieval_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_retrieval_run_02101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_indexing_02106():
    '''
    testing functionality of indexing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_indexing_02106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_escher_03031():
    '''
    testing functionality of escher
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_escher_03031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_exploratory_romp_03032():
    '''
    testing functionality of exploratory_romp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_exploratory_romp_03032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_freelance_coding_contract_03033():
    '''
    testing functionality of freelance_coding_contract
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_freelance_coding_contract_03033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_scavenge_03034():
    '''
    testing functionality of scavenge
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_scavenge_03034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_levy_ar_lab_access_03035():
    '''
    testing functionality of levy_ar_lab_access
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_levy_ar_lab_access_03035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_dirty_laundry_03052():
    '''
    testing functionality of dirty_laundry
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_dirty_laundry_03052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_frame_job_04001():
    '''
    testing functionality of frame_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_frame_job_04001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_hostage_04004():
    '''
    testing functionality of hostage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_hostage_04004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_recon_04024():
    '''
    testing functionality of recon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_recon_04024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_eureka_04027():
    '''
    testing functionality of eureka
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_eureka_04027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_running_interference_04044():
    '''
    testing functionality of running_interference
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_running_interference_04044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_lawyer_up_04063():
    '''
    testing functionality of lawyer_up
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_lawyer_up_04063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_leverage_04064():
    '''
    testing functionality of leverage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_leverage_04064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_quest_completed_04081():
    '''
    testing functionality of quest_completed
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_quest_completed_04081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_executive_wiretaps_04084():
    '''
    testing functionality of executive_wiretaps
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_executive_wiretaps_04084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_blackmail_04089():
    '''
    testing functionality of blackmail
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_blackmail_04089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_singularity_04101():
    '''
    testing functionality of singularity
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_singularity_04101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_queens_gambit_04102():
    '''
    testing functionality of queens_gambit
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_queens_gambit_04102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_power_nap_04107():
    '''
    testing functionality of power_nap
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_power_nap_04107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_lucky_find_04109():
    '''
    testing functionality of lucky_find
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_lucky_find_04109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_calling_in_favors_05031():
    '''
    testing functionality of calling_in_favors
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_calling_in_favors_05031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_early_bird_05032():
    '''
    testing functionality of early_bird
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_early_bird_05032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_express_delivery_05033():
    '''
    testing functionality of express_delivery
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_express_delivery_05033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_feint_05034():
    '''
    testing functionality of feint
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_feint_05034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_legwork_05035():
    '''
    testing functionality of legwork
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_legwork_05035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_planned_assault_05036():
    '''
    testing functionality of planned_assault
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_planned_assault_05036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_push_your_luck_05047():
    '''
    testing functionality of push_your_luck
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_push_your_luck_05047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_mass_install_05051():
    '''
    testing functionality of mass_install
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_mass_install_05051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_cyber_threat_06013():
    '''
    testing functionality of cyber_threat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_cyber_threat_06013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_paper_tripping_06015():
    '''
    testing functionality of paper_tripping
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_paper_tripping_06015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_social_engineering_06018():
    '''
    testing functionality of social_engineering
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_social_engineering_06018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_scrubbed_06034():
    '''
    testing functionality of scrubbed
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_scrubbed_06034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_three_steps_ahead_06035():
    '''
    testing functionality of three_steps_ahead
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_three_steps_ahead_06035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_unscheduled_maintenance_06036():
    '''
    testing functionality of unscheduled_maintenance
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_unscheduled_maintenance_06036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_net_celebrity_06038():
    '''
    testing functionality of net_celebrity
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_net_celebrity_06038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_inject_06073():
    '''
    testing functionality of inject
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_inject_06073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_tradein_06078():
    '''
    testing functionality of tradein
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_tradein_06078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_code_siphon_06115():
    '''
    testing functionality of code_siphon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_code_siphon_06115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_bribery_06118():
    '''
    testing functionality of bribery
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_bribery_06118()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_amped_up_07031():
    '''
    testing functionality of amped_up
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_amped_up_07031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_ive_had_worse_07032():
    '''
    testing functionality of ive_had_worse
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_ive_had_worse_07032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_itinerant_protesters_07033():
    '''
    testing functionality of itinerant_protesters
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_itinerant_protesters_07033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_showing_off_07034():
    '''
    testing functionality of showing_off
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_showing_off_07034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_wanton_destruction_07035():
    '''
    testing functionality of wanton_destruction
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_wanton_destruction_07035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_day_job_07036():
    '''
    testing functionality of day_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_day_job_07036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_forked_07037():
    '''
    testing functionality of forked
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_forked_07037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_knifed_07038():
    '''
    testing functionality of knifed
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_knifed_07038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_spooned_07039():
    '''
    testing functionality of spooned
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_spooned_07039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_uninstall_07053():
    '''
    testing functionality of uninstall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_uninstall_07053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_traffic_jam_08008():
    '''
    testing functionality of traffic_jam
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_traffic_jam_08008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_hacktivist_meeting_08021():
    '''
    testing functionality of hacktivist_meeting
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_hacktivist_meeting_08021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_career_fair_08023():
    '''
    testing functionality of career_fair
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_career_fair_08023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_game_day_08026():
    '''
    testing functionality of game_day
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_game_day_08026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_immolation_script_08041():
    '''
    testing functionality of immolation_script
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_immolation_script_08041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_drive_by_08064():
    '''
    testing functionality of drive_by
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_drive_by_08064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_power_to_the_people_08101():
    '''
    testing functionality of power_to_the_people
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_power_to_the_people_08101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_fisk_investment_seminar_08105():
    '''
    testing functionality of fisk_investment_seminar
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_fisk_investment_seminar_08105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_apocalypse_09030():
    '''
    testing functionality of apocalypse
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_apocalypse_09030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_prey_09031():
    '''
    testing functionality of prey
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_prey_09031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_independent_thinking_09038():
    '''
    testing functionality of independent_thinking
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_independent_thinking_09038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_employee_strike_09053():
    '''
    testing functionality of employee_strike
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_employee_strike_09053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_windfall_09054():
    '''
    testing functionality of windfall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_windfall_09054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_run_amok_10001():
    '''
    testing functionality of run_amok
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_run_amok_10001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_highstakes_job_10004():
    '''
    testing functionality of highstakes_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_highstakes_job_10004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_cbi_raid_10022():
    '''
    testing functionality of cbi_raid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_cbi_raid_10022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_corporate_scandal_10025():
    '''
    testing functionality of corporate_scandal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_corporate_scandal_10025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_populist_rally_10026():
    '''
    testing functionality of populist_rally
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_populist_rally_10026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_political_graffiti_10039():
    '''
    testing functionality of political_graffiti
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_political_graffiti_10039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_freedom_through_equality_10045():
    '''
    testing functionality of freedom_through_equality
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_freedom_through_equality_10045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_making_an_entrance_10058():
    '''
    testing functionality of making_an_entrance
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_making_an_entrance_10058()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_exclusive_party_10060():
    '''
    testing functionality of exclusive_party
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_exclusive_party_10060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_the_noble_path_10077():
    '''
    testing functionality of the_noble_path
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_the_noble_path_10077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_information_sifting_10079():
    '''
    testing functionality of information_sifting
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_information_sifting_10079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_out_of_the_ashes_10080():
    '''
    testing functionality of out_of_the_ashes
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_out_of_the_ashes_10080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_rebirth_10083():
    '''
    testing functionality of rebirth
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_rebirth_10083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_fear_the_masses_10096():
    '''
    testing functionality of fear_the_masses
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_fear_the_masses_10096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_the_price_of_freedom_10100():
    '''
    testing functionality of the_price_of_freedom
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_the_price_of_freedom_10100()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_rigged_results_10102():
    '''
    testing functionality of rigged_results
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_rigged_results_10102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_system_outage_11001():
    '''
    testing functionality of system_outage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_system_outage_11001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_another_day_another_paycheck_11007():
    '''
    testing functionality of another_day_another_paycheck
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_another_day_another_paycheck_11007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_deuces_wild_11008():
    '''
    testing functionality of deuces_wild
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_deuces_wild_11008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_injection_attack_11009():
    '''
    testing functionality of injection_attack
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_injection_attack_11009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_credit_crash_11021():
    '''
    testing functionality of credit_crash
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_credit_crash_11021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_rumor_mill_11022():
    '''
    testing functionality of rumor_mill
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_rumor_mill_11022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_data_breach_11028():
    '''
    testing functionality of data_breach
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_data_breach_11028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_en_passant_11061():
    '''
    testing functionality of en_passant
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_en_passant_11061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_frantic_coding_11062():
    '''
    testing functionality of frantic_coding
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_frantic_coding_11062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_government_investigations_11069():
    '''
    testing functionality of government_investigations
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_government_investigations_11069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_on_the_lam_11082():
    '''
    testing functionality of on_the_lam
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_on_the_lam_11082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_cold_read_11083():
    '''
    testing functionality of cold_read
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_cold_read_11083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_interdiction_11087():
    '''
    testing functionality of interdiction
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_interdiction_11087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_encore_11107():
    '''
    testing functionality of encore
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_encore_11107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_peace_in_our_time_11109():
    '''
    testing functionality of peace_in_our_time
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_peace_in_our_time_11109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_pushing_the_envelope_12001():
    '''
    testing functionality of pushing_the_envelope
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_pushing_the_envelope_12001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_exploit_12004():
    '''
    testing functionality of exploit
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_exploit_12004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_spot_the_prey_12005():
    '''
    testing functionality of spot_the_prey
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_spot_the_prey_12005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_mad_dash_12008():
    '''
    testing functionality of mad_dash
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_mad_dash_12008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_mobius_12024():
    '''
    testing functionality of mobius
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_mobius_12024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_system_seizure_12026():
    '''
    testing functionality of system_seizure
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_system_seizure_12026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_build_script_12028():
    '''
    testing functionality of build_script
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_build_script_12028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_mars_for_martians_12081():
    '''
    testing functionality of mars_for_martians
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_mars_for_martians_12081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_leave_no_trace_12083():
    '''
    testing functionality of leave_no_trace
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_leave_no_trace_12083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_rip_deal_12084():
    '''
    testing functionality of rip_deal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_rip_deal_12084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_lean_and_mean_12086():
    '''
    testing functionality of lean_and_mean
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_lean_and_mean_12086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_mining_accident_12101():
    '''
    testing functionality of mining_accident
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_mining_accident_12101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_dianas_hunt_12106():
    '''
    testing functionality of dianas_hunt
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_dianas_hunt_12106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_reshape_12107():
    '''
    testing functionality of reshape
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_reshape_12107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_bruteforcehack_13002():
    '''
    testing functionality of bruteforcehack
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_bruteforcehack_13002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_spear_phishing_13003():
    '''
    testing functionality of spear_phishing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_spear_phishing_13003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_syn_attack_13004():
    '''
    testing functionality of syn_attack
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_syn_attack_13004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_careful_planning_13013():
    '''
    testing functionality of careful_planning
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_careful_planning_13013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_deep_data_mining_13014():
    '''
    testing functionality of deep_data_mining
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_deep_data_mining_13014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_process_automation_13023():
    '''
    testing functionality of process_automation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_process_automation_13023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_security_leak_14009():
    '''
    testing functionality of security_leak
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_security_leak_14009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_demolition_run_20002():
    '''
    testing functionality of demolition_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_demolition_run_20002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_retrieval_run_20003():
    '''
    testing functionality of retrieval_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_retrieval_run_20003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_singularity_20004():
    '''
    testing functionality of singularity
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_singularity_20004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_stimhack_20005():
    '''
    testing functionality of stimhack
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_stimhack_20005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_easy_mark_20020():
    '''
    testing functionality of easy_mark
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_easy_mark_20020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_emergency_shutdown_20021():
    '''
    testing functionality of emergency_shutdown
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_emergency_shutdown_20021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_forged_activation_orders_20022():
    '''
    testing functionality of forged_activation_orders
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_forged_activation_orders_20022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_inside_job_20023():
    '''
    testing functionality of inside_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_inside_job_20023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_special_order_20024():
    '''
    testing functionality of special_order
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_special_order_20024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_diesel_20038():
    '''
    testing functionality of diesel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_diesel_20038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_indexing_20039():
    '''
    testing functionality of indexing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_indexing_20039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_modded_20040():
    '''
    testing functionality of modded
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_modded_20040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_notoriety_20041():
    '''
    testing functionality of notoriety
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_notoriety_20041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_test_run_20042():
    '''
    testing functionality of test_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_test_run_20042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_the_makers_eye_20043():
    '''
    testing functionality of the_makers_eye
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_the_makers_eye_20043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_tinkering_20044():
    '''
    testing functionality of tinkering
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_tinkering_20044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_infiltration_20055():
    '''
    testing functionality of infiltration
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_infiltration_20055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_sure_gamble_20056():
    '''
    testing functionality of sure_gamble
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_sure_gamble_20056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_by_any_means_21001():
    '''
    testing functionality of by_any_means
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_by_any_means_21001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_credit_kiting_21023():
    '''
    testing functionality of credit_kiting
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_credit_kiting_21023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_emergent_creativity_21028():
    '''
    testing functionality of emergent_creativity
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_emergent_creativity_21028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_corporate_grant_21044():
    '''
    testing functionality of corporate_grant
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_corporate_grant_21044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_marathon_21046():
    '''
    testing functionality of marathon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_marathon_21046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_white_hat_21048():
    '''
    testing functionality of white_hat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_white_hat_21048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_glut_cipher_21061():
    '''
    testing functionality of glut_cipher
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_glut_cipher_21061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_falsified_credentials_21064():
    '''
    testing functionality of falsified_credentials
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_falsified_credentials_21064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_because_i_can_21066():
    '''
    testing functionality of because_i_can
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_because_i_can_21066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_contaminate_21083():
    '''
    testing functionality of contaminate
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_contaminate_21083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_embezzle_21084():
    '''
    testing functionality of embezzle
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_embezzle_21084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_compile_21088():
    '''
    testing functionality of compile
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_compile_21088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_diversion_of_funds_21105():
    '''
    testing functionality of diversion_of_funds
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_diversion_of_funds_21105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_black_hat_21110():
    '''
    testing functionality of black_hat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_black_hat_21110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_divide_and_conquer_22002():
    '''
    testing functionality of divide_and_conquer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_divide_and_conquer_22002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_guinea_pig_22003():
    '''
    testing functionality of guinea_pig
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_guinea_pig_22003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_hot_pursuit_22009():
    '''
    testing functionality of hot_pursuit
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_hot_pursuit_22009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_insight_22016():
    '''
    testing functionality of insight
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_insight_22016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_reboot_22023():
    '''
    testing functionality of reboot
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_reboot_22023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_office_supplies_22024():
    '''
    testing functionality of office_supplies
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_office_supplies_22024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_labor_rights_23001():
    '''
    testing functionality of labor_rights
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_labor_rights_23001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_watch_the_world_burn_23100():
    '''
    testing functionality of watch_the_world_burn
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_watch_the_world_burn_23100()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_queens_gambit_25003():
    '''
    testing functionality of queens_gambit
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_queens_gambit_25003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_quest_completed_25004():
    '''
    testing functionality of quest_completed
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_quest_completed_25004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_retrieval_run_25005():
    '''
    testing functionality of retrieval_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_retrieval_run_25005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_run_amok_25006():
    '''
    testing functionality of run_amok
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_run_amok_25006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_stimhack_25007():
    '''
    testing functionality of stimhack
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_stimhack_25007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_career_fair_25022():
    '''
    testing functionality of career_fair
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_career_fair_25022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_easy_mark_25023():
    '''
    testing functionality of easy_mark
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_easy_mark_25023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_emergency_shutdown_25024():
    '''
    testing functionality of emergency_shutdown
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_emergency_shutdown_25024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_hostage_25025():
    '''
    testing functionality of hostage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_hostage_25025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_inside_job_25026():
    '''
    testing functionality of inside_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_inside_job_25026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_legwork_25027():
    '''
    testing functionality of legwork
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_legwork_25027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_networking_25028():
    '''
    testing functionality of networking
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_networking_25028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_spear_phishing_25029():
    '''
    testing functionality of spear_phishing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_spear_phishing_25029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_special_order_25030():
    '''
    testing functionality of special_order
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_special_order_25030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_diesel_25042():
    '''
    testing functionality of diesel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_diesel_25042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_modded_25043():
    '''
    testing functionality of modded
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_modded_25043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_notoriety_25044():
    '''
    testing functionality of notoriety
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_notoriety_25044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_test_run_25045():
    '''
    testing functionality of test_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_test_run_25045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_the_makers_eye_25046():
    '''
    testing functionality of the_makers_eye
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_the_makers_eye_25046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_tinkering_25047():
    '''
    testing functionality of tinkering
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_tinkering_25047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_sure_gamble_25059():
    '''
    testing functionality of sure_gamble
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_sure_gamble_25059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_dirty_laundry_25060():
    '''
    testing functionality of dirty_laundry
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_dirty_laundry_25060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_isolation_26001():
    '''
    testing functionality of isolation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_isolation_26001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_always_have_a_backup_plan_26011():
    '''
    testing functionality of always_have_a_backup_plan
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_always_have_a_backup_plan_26011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_blueberry_diesel_26012():
    '''
    testing functionality of blueberry_diesel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_blueberry_diesel_26012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_in_the_groove_26020():
    '''
    testing functionality of in_the_groove
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_in_the_groove_26020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_khusyuk_26021():
    '''
    testing functionality of khusyuk
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_khusyuk_26021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_spec_work_26022():
    '''
    testing functionality of spec_work
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_spec_work_26022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_direct_access_26028():
    '''
    testing functionality of direct_access
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_direct_access_26028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_rejig_26029():
    '''
    testing functionality of rejig
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_rejig_26029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_moshing_26067():
    '''
    testing functionality of moshing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_moshing_26067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_bravado_26074():
    '''
    testing functionality of bravado
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_bravado_26074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_harmony_ar_therapy_26083():
    '''
    testing functionality of harmony_ar_therapy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_harmony_ar_therapy_26083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_labor_rights_28001():
    '''
    testing functionality of labor_rights
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_labor_rights_28001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_indexing_29005():
    '''
    testing functionality of indexing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_indexing_29005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_lucky_find_29007():
    '''
    testing functionality of lucky_find
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_lucky_find_29007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_wildcat_strike_30002():
    '''
    testing functionality of wildcat_strike
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_wildcat_strike_30002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_mutual_favor_30011():
    '''
    testing functionality of mutual_favor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_mutual_favor_30011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_tread_lightly_30012():
    '''
    testing functionality of tread_lightly
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_tread_lightly_30012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_creative_commission_30020():
    '''
    testing functionality of creative_commission
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_creative_commission_30020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_vrcation_30021():
    '''
    testing functionality of vrcation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_vrcation_30021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_jailbreak_30028():
    '''
    testing functionality of jailbreak
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_jailbreak_30028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_overclock_30029():
    '''
    testing functionality of overclock
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_overclock_30029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_sure_gamble_30030():
    '''
    testing functionality of sure_gamble
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_sure_gamble_30030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_en_passant_31003():
    '''
    testing functionality of en_passant
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_en_passant_31003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_retrieval_run_31004():
    '''
    testing functionality of retrieval_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_retrieval_run_31004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_career_fair_31015():
    '''
    testing functionality of career_fair
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_career_fair_31015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_emergency_shutdown_31016():
    '''
    testing functionality of emergency_shutdown
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_emergency_shutdown_31016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_forged_activation_orders_31017():
    '''
    testing functionality of forged_activation_orders
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_forged_activation_orders_31017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_inside_job_31018():
    '''
    testing functionality of inside_job
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_inside_job_31018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_legwork_31019():
    '''
    testing functionality of legwork
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_legwork_31019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_networking_31020():
    '''
    testing functionality of networking
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_networking_31020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_diesel_31027():
    '''
    testing functionality of diesel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_diesel_31027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_test_run_31028():
    '''
    testing functionality of test_run
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_test_run_31028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_the_makers_eye_31029():
    '''
    testing functionality of the_makers_eye
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_the_makers_eye_31029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_dirty_laundry_31037():
    '''
    testing functionality of dirty_laundry
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_dirty_laundry_31037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_deep_dive_32003():
    '''
    testing functionality of deep_dive
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_deep_dive_32003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_chastushka_33002():
    '''
    testing functionality of chastushka
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_chastushka_33002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_running_hot_33003():
    '''
    testing functionality of running_hot
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_running_hot_33003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_steelskin_scarring_33004():
    '''
    testing functionality of steelskin_scarring
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_steelskin_scarring_33004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_carpe_diem_33012():
    '''
    testing functionality of carpe_diem
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_carpe_diem_33012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_pinhole_threading_33013():
    '''
    testing functionality of pinhole_threading
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_pinhole_threading_33013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_deep_dive_33022():
    '''
    testing functionality of deep_dive
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_deep_dive_33022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_into_the_depths_33023():
    '''
    testing functionality of into_the_depths
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_into_the_depths_33023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_rigging_up_33024():
    '''
    testing functionality of rigging_up
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_rigging_up_33024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_finality_33066():
    '''
    testing functionality of finality
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_finality_33066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_katorga_breakout_33067():
    '''
    testing functionality of katorga_breakout
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_katorga_breakout_33067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_raindrops_cut_stone_33068():
    '''
    testing functionality of raindrops_cut_stone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_raindrops_cut_stone_33068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_concerto_33075():
    '''
    testing functionality of concerto
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_concerto_33075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_reprise_33076():
    '''
    testing functionality of reprise
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_reprise_33076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_event_spark_of_inspiration_33084():
    '''
    testing functionality of spark_of_inspiration
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("event")

    test_card = event_spark_of_inspiration_33084()
    test_card.play(test_game_environment.runner,test_game_environment)
