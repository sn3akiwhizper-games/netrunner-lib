
'''
test cases for card classes of type upgrade
'''
from netrunner_lib.cards._base_card_classes import Upgrade
from netrunner_lib.cards.upgrade import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
def test_upgrade_corporate_troubleshooter_01065():
    '''
    testing functionality of corporate_troubleshooter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_corporate_troubleshooter_01065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_experiential_data_01066():
    '''
    testing functionality of experiential_data
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_experiential_data_01066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_akitaro_watanabe_01079():
    '''
    testing functionality of akitaro_watanabe
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_akitaro_watanabe_01079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_red_herrings_01091():
    '''
    testing functionality of red_herrings
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_red_herrings_01091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_sansan_city_grid_01092():
    '''
    testing functionality of sansan_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_sansan_city_grid_01092()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_research_station_01105():
    '''
    testing functionality of research_station
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_research_station_01105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_ash_2x3zb9cy_02013():
    '''
    testing functionality of ash_2x3zb9cy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_ash_2x3zb9cy_02013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_chilo_city_grid_02036():
    '''
    testing functionality of chilo_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_chilo_city_grid_02036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_amazon_industrial_zone_02038():
    '''
    testing functionality of amazon_industrial_zone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_amazon_industrial_zone_02038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_hokusai_grid_02095():
    '''
    testing functionality of hokusai_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_hokusai_grid_02095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_bernice_mai_02097():
    '''
    testing functionality of bernice_mai
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_bernice_mai_02097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_simone_diego_02099():
    '''
    testing functionality of simone_diego
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_simone_diego_02099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_ruhr_valley_02111():
    '''
    testing functionality of ruhr_valley
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_ruhr_valley_02111()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_midori_02113():
    '''
    testing functionality of midori
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_midori_02113()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_awakening_center_03021():
    '''
    testing functionality of awakening_center
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_awakening_center_03021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_tyrs_hand_03022():
    '''
    testing functionality of tyrs_hand
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_tyrs_hand_03022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_off_the_grid_04038():
    '''
    testing functionality of off_the_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_off_the_grid_04038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_panic_button_04072():
    '''
    testing functionality of panic_button
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_panic_button_04072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_strongbox_04091():
    '''
    testing functionality of strongbox
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_strongbox_04091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_caprice_nisei_04114():
    '''
    testing functionality of caprice_nisei
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_caprice_nisei_04114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_neotokyo_grid_05021():
    '''
    testing functionality of neotokyo_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_neotokyo_grid_05021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_tori_hanzo_05022():
    '''
    testing functionality of tori_hanzo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_tori_hanzo_05022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_midway_station_grid_06007():
    '''
    testing functionality of midway_station_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_midway_station_grid_06007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_heinlein_grid_06023():
    '''
    testing functionality of heinlein_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_heinlein_grid_06023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_willothewisp_06032():
    '''
    testing functionality of willothewisp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_willothewisp_06032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_port_anson_grid_06044():
    '''
    testing functionality of port_anson_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_port_anson_grid_06044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_crisium_grid_06048():
    '''
    testing functionality of crisium_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_crisium_grid_06048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_shell_corporation_06092():
    '''
    testing functionality of shell_corporation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_shell_corporation_06092()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_selfdestruct_06112():
    '''
    testing functionality of selfdestruct
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_selfdestruct_06112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_satellite_grid_07023():
    '''
    testing functionality of satellite_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_satellite_grid_07023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_the_twins_07024():
    '''
    testing functionality of the_twins
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_the_twins_07024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_dedicated_technician_team_07026():
    '''
    testing functionality of dedicated_technician_team
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_dedicated_technician_team_07026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_cyberdex_virus_suite_07027():
    '''
    testing functionality of cyberdex_virus_suite
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_cyberdex_virus_suite_07027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_valley_grid_08015():
    '''
    testing functionality of valley_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_valley_grid_08015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_breaker_bay_grid_08040():
    '''
    testing functionality of breaker_bay_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_breaker_bay_grid_08040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_oaktown_grid_08053():
    '''
    testing functionality of oaktown_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_oaktown_grid_08053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_ryon_knight_08054():
    '''
    testing functionality of ryon_knight
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_ryon_knight_08054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_marcus_batty_08074():
    '''
    testing functionality of marcus_batty
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_marcus_batty_08074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_underway_grid_08080():
    '''
    testing functionality of underway_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_underway_grid_08080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_old_hollywood_grid_08097():
    '''
    testing functionality of old_hollywood_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_old_hollywood_grid_08097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_product_placement_08115():
    '''
    testing functionality of product_placement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_product_placement_08115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_expo_grid_08119():
    '''
    testing functionality of expo_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_expo_grid_08119()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_keegan_lane_09024():
    '''
    testing functionality of keegan_lane
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_keegan_lane_09024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_rutherford_grid_09025():
    '''
    testing functionality of rutherford_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_rutherford_grid_09025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_mumbad_city_grid_10014():
    '''
    testing functionality of mumbad_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_mumbad_city_grid_10014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_disposable_hq_10034():
    '''
    testing functionality of disposable_hq
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_disposable_hq_10034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_surat_city_grid_10057():
    '''
    testing functionality of surat_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_surat_city_grid_10057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_mumbad_virtual_tour_10076():
    '''
    testing functionality of mumbad_virtual_tour
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_mumbad_virtual_tour_10076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_navi_mumbai_city_grid_10110():
    '''
    testing functionality of navi_mumbai_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_navi_mumbai_city_grid_10110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_georgia_emelyov_11014():
    '''
    testing functionality of georgia_emelyov
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_georgia_emelyov_11014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_prisec_11040():
    '''
    testing functionality of prisec
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_prisec_11040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_drone_screen_11076():
    '''
    testing functionality of drone_screen
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_drone_screen_11076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_manta_grid_11091():
    '''
    testing functionality of manta_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_manta_grid_11091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_nihongai_grid_11093():
    '''
    testing functionality of nihongai_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_nihongai_grid_11093()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_bryan_stinson_11117():
    '''
    testing functionality of bryan_stinson
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_bryan_stinson_11117()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_defense_construct_12011():
    '''
    testing functionality of defense_construct
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_defense_construct_12011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_oberth_protocol_12018():
    '''
    testing functionality of oberth_protocol
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_oberth_protocol_12018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_khondi_plaza_12019():
    '''
    testing functionality of khondi_plaza
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_khondi_plaza_12019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_signal_jamming_12020():
    '''
    testing functionality of signal_jamming
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_signal_jamming_12020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_bamboo_dome_12053():
    '''
    testing functionality of bamboo_dome
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_bamboo_dome_12053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_ben_musashi_12054():
    '''
    testing functionality of ben_musashi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_ben_musashi_12054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_henry_phillips_12056():
    '''
    testing functionality of henry_phillips
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_henry_phillips_12056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_warroid_tracker_12068():
    '''
    testing functionality of warroid_tracker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_warroid_tracker_12068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_traffic_analyzer_12075():
    '''
    testing functionality of traffic_analyzer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_traffic_analyzer_12075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_helheim_servers_12091():
    '''
    testing functionality of helheim_servers
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_helheim_servers_12091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_fractal_threat_matrix_12119():
    '''
    testing functionality of fractal_threat_matrix
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_fractal_threat_matrix_12119()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_black_level_clearance_13039():
    '''
    testing functionality of black_level_clearance
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_black_level_clearance_13039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_mason_bellamy_13040():
    '''
    testing functionality of mason_bellamy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_mason_bellamy_13040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_k_p_lynn_13052():
    '''
    testing functionality of k_p_lynn
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_k_p_lynn_13052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_ash_2x3zb9cy_20075():
    '''
    testing functionality of ash_2x3zb9cy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_ash_2x3zb9cy_20075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_strongbox_20076():
    '''
    testing functionality of strongbox
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_strongbox_20076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_hokusai_grid_20108():
    '''
    testing functionality of hokusai_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_hokusai_grid_20108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_red_herrings_20122():
    '''
    testing functionality of red_herrings
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_red_herrings_20122()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_bernice_mai_20123():
    '''
    testing functionality of bernice_mai
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_bernice_mai_20123()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_calibration_testing_21017():
    '''
    testing functionality of calibration_testing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_calibration_testing_21017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_jinja_city_grid_21031():
    '''
    testing functionality of jinja_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_jinja_city_grid_21031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_forced_connection_21037():
    '''
    testing functionality of forced_connection
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_forced_connection_21037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_code_replicator_21052():
    '''
    testing functionality of code_replicator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_code_replicator_21052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_tempus_21071():
    '''
    testing functionality of tempus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_tempus_21071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_bio_vault_21072():
    '''
    testing functionality of bio_vault
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_bio_vault_21072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_mwanza_city_grid_21096():
    '''
    testing functionality of mwanza_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_mwanza_city_grid_21096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_intake_21098():
    '''
    testing functionality of intake
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_intake_21098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_overseer_matrix_21100():
    '''
    testing functionality of overseer_matrix
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_overseer_matrix_21100()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_giordano_memorial_field_22033():
    '''
    testing functionality of giordano_memorial_field
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_giordano_memorial_field_22033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_daruma_22041():
    '''
    testing functionality of daruma
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_daruma_22041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_arella_salvatore_22049():
    '''
    testing functionality of arella_salvatore
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_arella_salvatore_22049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_embolus_23011():
    '''
    testing functionality of embolus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_embolus_23011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_hired_help_23101():
    '''
    testing functionality of hired_help
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_hired_help_23101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_ash_2x3zb9cy_25082():
    '''
    testing functionality of ash_2x3zb9cy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_ash_2x3zb9cy_25082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_mason_bellamy_25083():
    '''
    testing functionality of mason_bellamy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_mason_bellamy_25083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_hokusai_grid_25103():
    '''
    testing functionality of hokusai_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_hokusai_grid_25103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_product_placement_25120():
    '''
    testing functionality of product_placement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_product_placement_25120()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_red_herrings_25121():
    '''
    testing functionality of red_herrings
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_red_herrings_25121()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_crisium_grid_25139():
    '''
    testing functionality of crisium_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_crisium_grid_25139()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_cold_site_server_26038():
    '''
    testing functionality of cold_site_server
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_cold_site_server_26038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_letheia_nisei_26046():
    '''
    testing functionality of letheia_nisei
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_letheia_nisei_26046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_increased_drop_rates_26054():
    '''
    testing functionality of increased_drop_rates
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_increased_drop_rates_26054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_reduced_service_26062():
    '''
    testing functionality of reduced_service
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_reduced_service_26062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_tranquility_home_grid_26105():
    '''
    testing functionality of tranquility_home_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_tranquility_home_grid_26105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_la_costa_grid_26112():
    '''
    testing functionality of la_costa_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_la_costa_grid_26112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_ganked_26119():
    '''
    testing functionality of ganked
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_ganked_26119()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_cayambe_grid_26127():
    '''
    testing functionality of cayambe_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_cayambe_grid_26127()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_la_costa_grid_27005():
    '''
    testing functionality of la_costa_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_la_costa_grid_27005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_cayambe_grid_27007():
    '''
    testing functionality of cayambe_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_cayambe_grid_27007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_embolus_28003():
    '''
    testing functionality of embolus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_embolus_28003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_sansan_city_grid_29014():
    '''
    testing functionality of sansan_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_sansan_city_grid_29014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_manegarm_skunkworks_30042():
    '''
    testing functionality of manegarm_skunkworks
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_manegarm_skunkworks_30042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_anoetic_void_30050():
    '''
    testing functionality of anoetic_void
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_anoetic_void_30050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_amaze_amusements_30058():
    '''
    testing functionality of amaze_amusements
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_amaze_amusements_30058()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_malapert_data_vault_30066():
    '''
    testing functionality of malapert_data_vault
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_malapert_data_vault_30066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_corporate_troubleshooter_31049():
    '''
    testing functionality of corporate_troubleshooter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_corporate_troubleshooter_31049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_hokusai_grid_31059():
    '''
    testing functionality of hokusai_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_hokusai_grid_31059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_sansan_city_grid_31069():
    '''
    testing functionality of sansan_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_sansan_city_grid_31069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_crisium_grid_31079():
    '''
    testing functionality of crisium_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_crisium_grid_31079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_vladisibirsk_city_grid_32006():
    '''
    testing functionality of vladisibirsk_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_vladisibirsk_city_grid_32006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_mavirus_33047():
    '''
    testing functionality of mavirus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_mavirus_33047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_vladisibirsk_city_grid_33056():
    '''
    testing functionality of vladisibirsk_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_vladisibirsk_city_grid_33056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_djupstad_grid_33102():
    '''
    testing functionality of djupstad_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_djupstad_grid_33102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_mr_hendrik_33103():
    '''
    testing functionality of mr_hendrik
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_mr_hendrik_33103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_nanisivik_grid_33111():
    '''
    testing functionality of nanisivik_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_nanisivik_grid_33111()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_yakov_erikovich_avdakov_33126():
    '''
    testing functionality of yakov_erikovich_avdakov
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_yakov_erikovich_avdakov_33126()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_upgrade_zato_city_grid_33127():
    '''
    testing functionality of zato_city_grid
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("upgrade")

    test_card = upgrade_zato_city_grid_33127()
    test_card.play(test_game_environment.runner,test_game_environment)
