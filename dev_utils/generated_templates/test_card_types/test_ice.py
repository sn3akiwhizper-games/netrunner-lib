
'''
test cases for card classes of type ice
'''
from netrunner_lib.cards._base_card_classes import Ice
from netrunner_lib.cards.ice import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
def test_ice_heimdall_10_01061():
    '''
    testing functionality of heimdall_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_heimdall_10_01061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ichi_10_01062():
    '''
    testing functionality of ichi_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ichi_10_01062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_viktor_10_01063():
    '''
    testing functionality of viktor_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_viktor_10_01063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_rototurret_01064():
    '''
    testing functionality of rototurret
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_rototurret_01064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_cell_portal_01074():
    '''
    testing functionality of cell_portal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_cell_portal_01074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_chum_01075():
    '''
    testing functionality of chum
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_chum_01075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_data_mine_01076():
    '''
    testing functionality of data_mine
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_data_mine_01076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_neural_katana_01077():
    '''
    testing functionality of neural_katana
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_neural_katana_01077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wall_of_thorns_01078():
    '''
    testing functionality of wall_of_thorns
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wall_of_thorns_01078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_data_raven_01088():
    '''
    testing functionality of data_raven
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_data_raven_01088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_matrix_analyzer_01089():
    '''
    testing functionality of matrix_analyzer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_matrix_analyzer_01089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tollbooth_01090():
    '''
    testing functionality of tollbooth
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tollbooth_01090()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_archer_01101():
    '''
    testing functionality of archer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_archer_01101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hadrians_wall_01102():
    '''
    testing functionality of hadrians_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hadrians_wall_01102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ice_wall_01103():
    '''
    testing functionality of ice_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ice_wall_01103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_shadow_01104():
    '''
    testing functionality of shadow
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_shadow_01104()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_enigma_01111():
    '''
    testing functionality of enigma
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_enigma_01111()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hunter_01112():
    '''
    testing functionality of hunter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hunter_01112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wall_of_static_01113():
    '''
    testing functionality of wall_of_static
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wall_of_static_01113()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_janus_10_02012():
    '''
    testing functionality of janus_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_janus_10_02012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_snowflake_02015():
    '''
    testing functionality of snowflake
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_snowflake_02015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tmi_02017():
    '''
    testing functionality of tmi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tmi_02017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_caduceus_02019():
    '''
    testing functionality of caduceus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_caduceus_02019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_draco_02020():
    '''
    testing functionality of draco
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_draco_02020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sherlock_10_02030():
    '''
    testing functionality of sherlock_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sherlock_10_02030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sensei_02034():
    '''
    testing functionality of sensei
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sensei_02034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_viper_02052():
    '''
    testing functionality of viper
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_viper_02052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_popup_window_02056():
    '''
    testing functionality of popup_window
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_popup_window_02056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_woodcutter_02057():
    '''
    testing functionality of woodcutter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_woodcutter_02057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_chimera_02060():
    '''
    testing functionality of chimera
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_chimera_02060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hourglass_02071():
    '''
    testing functionality of hourglass
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hourglass_02071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bullfrog_02073():
    '''
    testing functionality of bullfrog
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bullfrog_02073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_uroboros_02074():
    '''
    testing functionality of uroboros
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_uroboros_02074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tyrant_02078():
    '''
    testing functionality of tyrant
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tyrant_02078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_whirlpool_02094():
    '''
    testing functionality of whirlpool
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_whirlpool_02094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_data_hound_02096():
    '''
    testing functionality of data_hound
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_data_hound_02096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_salvage_02098():
    '''
    testing functionality of salvage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_salvage_02098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_eli_10_02110():
    '''
    testing functionality of eli_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_eli_10_02110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_flare_02117():
    '''
    testing functionality of flare
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_flare_02117()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_burke_bugs_02119():
    '''
    testing functionality of burke_bugs
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_burke_bugs_02119()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_heimdall_20_03015():
    '''
    testing functionality of heimdall_20
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_heimdall_20_03015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_howler_03016():
    '''
    testing functionality of howler
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_howler_03016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ichi_20_03017():
    '''
    testing functionality of ichi_20
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ichi_20_03017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_minelayer_03018():
    '''
    testing functionality of minelayer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_minelayer_03018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_viktor_20_03019():
    '''
    testing functionality of viktor_20
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_viktor_20_03019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_zed_10_03020():
    '''
    testing functionality of zed_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_zed_10_03020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bastion_03026():
    '''
    testing functionality of bastion
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bastion_03026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_datapike_03027():
    '''
    testing functionality of datapike
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_datapike_03027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_next_bronze_04011():
    '''
    testing functionality of next_bronze
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_next_bronze_04011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_himitsubako_04013():
    '''
    testing functionality of himitsubako
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_himitsubako_04013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_swarm_04018():
    '''
    testing functionality of swarm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_swarm_04018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_grim_04020():
    '''
    testing functionality of grim
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_grim_04020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wotan_04030():
    '''
    testing functionality of wotan
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wotan_04030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_swordsman_04033():
    '''
    testing functionality of swordsman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_swordsman_04033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_muckraker_04035():
    '''
    testing functionality of muckraker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_muckraker_04035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hudson_10_04051():
    '''
    testing functionality of hudson_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hudson_10_04051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_snoop_04056():
    '''
    testing functionality of snoop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_snoop_04056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ireress_04057():
    '''
    testing functionality of ireress
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ireress_04057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_paper_wall_04059():
    '''
    testing functionality of paper_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_paper_wall_04059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_fenris_04071():
    '''
    testing functionality of fenris
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_fenris_04071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tsurugi_04074():
    '''
    testing functionality of tsurugi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tsurugi_04074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_rsvp_04077():
    '''
    testing functionality of rsvp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_rsvp_04077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_curtain_wall_04078():
    '''
    testing functionality of curtain_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_curtain_wall_04078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_yagura_04093():
    '''
    testing functionality of yagura
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_yagura_04093()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wraparound_04096():
    '''
    testing functionality of wraparound
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wraparound_04096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_gyri_labyrinth_04110():
    '''
    testing functionality of gyri_labyrinth
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_gyri_labyrinth_04110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_shinobi_04115():
    '''
    testing functionality of shinobi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_shinobi_04115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_marker_04116():
    '''
    testing functionality of marker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_marker_04116()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hive_04117():
    '''
    testing functionality of hive
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hive_04117()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_quandary_04120():
    '''
    testing functionality of quandary
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_quandary_04120()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_inazuma_05016():
    '''
    testing functionality of inazuma
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_inazuma_05016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_komainu_05017():
    '''
    testing functionality of komainu
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_komainu_05017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_pup_05018():
    '''
    testing functionality of pup
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_pup_05018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_shiro_05019():
    '''
    testing functionality of shiro
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_shiro_05019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_susanoonomikoto_05020():
    '''
    testing functionality of susanoonomikoto
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_susanoonomikoto_05020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_guard_05024():
    '''
    testing functionality of guard
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_guard_05024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_rainbow_05025():
    '''
    testing functionality of rainbow
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_rainbow_05025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_next_silver_06002():
    '''
    testing functionality of next_silver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_next_silver_06002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_lotus_field_06003():
    '''
    testing functionality of lotus_field
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_lotus_field_06003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_taurus_06009():
    '''
    testing functionality of taurus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_taurus_06009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_mother_goddess_06010():
    '''
    testing functionality of mother_goddess
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_mother_goddess_06010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_galahad_06011():
    '''
    testing functionality of galahad
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_galahad_06011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_information_overload_06027():
    '''
    testing functionality of information_overload
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_information_overload_06027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_iq_06041():
    '''
    testing functionality of iq
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_iq_06041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_kitsune_06043():
    '''
    testing functionality of kitsune
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_kitsune_06043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wendigo_06047():
    '''
    testing functionality of wendigo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wendigo_06047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_lancelot_06051():
    '''
    testing functionality of lancelot
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_lancelot_06051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_architect_06061():
    '''
    testing functionality of architect
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_architect_06061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ashigaru_06064():
    '''
    testing functionality of ashigaru
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ashigaru_06064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_mamba_06065():
    '''
    testing functionality of mamba
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_mamba_06065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_universal_connectivity_fee_06067():
    '''
    testing functionality of universal_connectivity_fee
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_universal_connectivity_fee_06067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_changeling_06069():
    '''
    testing functionality of changeling
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_changeling_06069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sagittarius_06082():
    '''
    testing functionality of sagittarius
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sagittarius_06082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_gemini_06084():
    '''
    testing functionality of gemini
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_gemini_06084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_lycan_06089():
    '''
    testing functionality of lycan
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_lycan_06089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_merlin_06091():
    '''
    testing functionality of merlin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_merlin_06091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_errand_boy_06102():
    '''
    testing functionality of errand_boy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_errand_boy_06102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_markus_10_06104():
    '''
    testing functionality of markus_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_markus_10_06104()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_troll_06108():
    '''
    testing functionality of troll
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_troll_06108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_virgo_06109():
    '''
    testing functionality of virgo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_virgo_06109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_excalibur_06111():
    '''
    testing functionality of excalibur
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_excalibur_06111()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_asteroid_belt_07012():
    '''
    testing functionality of asteroid_belt
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_asteroid_belt_07012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wormhole_07013():
    '''
    testing functionality of wormhole
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wormhole_07013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_nebula_07014():
    '''
    testing functionality of nebula
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_nebula_07014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_orion_07015():
    '''
    testing functionality of orion
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_orion_07015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_builder_07016():
    '''
    testing functionality of builder
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_builder_07016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_checkpoint_07017():
    '''
    testing functionality of checkpoint
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_checkpoint_07017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_fire_wall_07018():
    '''
    testing functionality of fire_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_fire_wall_07018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_searchlight_07019():
    '''
    testing functionality of searchlight
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_searchlight_07019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_next_gold_08011():
    '''
    testing functionality of next_gold
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_next_gold_08011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_cortex_lock_08014():
    '''
    testing functionality of cortex_lock
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_cortex_lock_08014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bandwidth_08016():
    '''
    testing functionality of bandwidth
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bandwidth_08016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_negotiator_08019():
    '''
    testing functionality of negotiator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_negotiator_08019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_turing_08033():
    '''
    testing functionality of turing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_turing_08033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_crick_08034():
    '''
    testing functionality of crick
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_crick_08034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_gutenberg_08037():
    '''
    testing functionality of gutenberg
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_gutenberg_08037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_meru_mati_08039():
    '''
    testing functionality of meru_mati
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_meru_mati_08039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_lab_dog_08052():
    '''
    testing functionality of lab_dog
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_lab_dog_08052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_clairvoyant_monitor_08055():
    '''
    testing functionality of clairvoyant_monitor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_clairvoyant_monitor_08055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_lockdown_08056():
    '''
    testing functionality of lockdown
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_lockdown_08056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_little_engine_08057():
    '''
    testing functionality of little_engine
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_little_engine_08057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_quicksand_08060():
    '''
    testing functionality of quicksand
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_quicksand_08060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_pachinko_08076():
    '''
    testing functionality of pachinko
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_pachinko_08076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_spiderweb_08079():
    '''
    testing functionality of spiderweb
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_spiderweb_08079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_enforcer_10_08089():
    '''
    testing functionality of enforcer_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_enforcer_10_08089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_its_a_trap_08090():
    '''
    testing functionality of its_a_trap
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_its_a_trap_08090()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tour_guide_08118():
    '''
    testing functionality of tour_guide
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tour_guide_08118()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_archangel_09013():
    '''
    testing functionality of archangel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_archangel_09013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_news_hound_09014():
    '''
    testing functionality of news_hound
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_news_hound_09014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_resistor_09015():
    '''
    testing functionality of resistor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_resistor_09015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_special_offer_09016():
    '''
    testing functionality of special_offer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_special_offer_09016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tldr_09017():
    '''
    testing functionality of tldr
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tldr_09017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_turnpike_09018():
    '''
    testing functionality of turnpike
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_turnpike_09018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_assassin_09028():
    '''
    testing functionality of assassin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_assassin_09028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_vikram_10_10012():
    '''
    testing functionality of vikram_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_vikram_10_10012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_interrupt_0_10016():
    '''
    testing functionality of interrupt_0
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_interrupt_0_10016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_harvester_10032():
    '''
    testing functionality of harvester
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_harvester_10032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bailiff_10056():
    '''
    testing functionality of bailiff
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bailiff_10056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_upayoga_10069():
    '''
    testing functionality of upayoga
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_upayoga_10069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_cobra_10074():
    '''
    testing functionality of cobra
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_cobra_10074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_brainstorm_10086():
    '''
    testing functionality of brainstorm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_brainstorm_10086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ravana_10_10087():
    '''
    testing functionality of ravana_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ravana_10_10087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_chetana_10089():
    '''
    testing functionality of chetana
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_chetana_10089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_waiver_10091():
    '''
    testing functionality of waiver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_waiver_10091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_red_tape_10093():
    '''
    testing functionality of red_tape
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_red_tape_10093()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_vanilla_10095():
    '''
    testing functionality of vanilla
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_vanilla_10095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_magnet_10103():
    '''
    testing functionality of magnet
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_magnet_10103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_fairchild_10_11010():
    '''
    testing functionality of fairchild_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_fairchild_10_11010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sherlock_20_11011():
    '''
    testing functionality of sherlock_20
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sherlock_20_11011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_chrysalis_11013():
    '''
    testing functionality of chrysalis
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_chrysalis_11013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_fairchild_20_11031():
    '''
    testing functionality of fairchild_20
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_fairchild_20_11031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_aiki_11032():
    '''
    testing functionality of aiki
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_aiki_11032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_fairchild_30_11049():
    '''
    testing functionality of fairchild_30
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_fairchild_30_11049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_dna_tracker_11053():
    '''
    testing functionality of dna_tracker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_dna_tracker_11053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_data_ward_11075():
    '''
    testing functionality of data_ward
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_data_ward_11075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bulwark_11078():
    '''
    testing functionality of bulwark
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bulwark_11078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_fairchild_11089():
    '''
    testing functionality of fairchild
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_fairchild_11089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_mind_game_11092():
    '''
    testing functionality of mind_game
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_mind_game_11092()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ip_block_11094():
    '''
    testing functionality of ip_block
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ip_block_11094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_thoth_11095():
    '''
    testing functionality of thoth
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_thoth_11095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_mausolus_11097():
    '''
    testing functionality of mausolus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_mausolus_11097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sapper_11098():
    '''
    testing functionality of sapper
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sapper_11098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_chiyashi_11112():
    '''
    testing functionality of chiyashi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_chiyashi_11112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_herald_11115():
    '''
    testing functionality of herald
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_herald_11115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_veritas_11116():
    '''
    testing functionality of veritas
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_veritas_11116()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_macrophage_11119():
    '''
    testing functionality of macrophage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_macrophage_11119()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tribunal_11120():
    '''
    testing functionality of tribunal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tribunal_11120()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_zed_20_12010():
    '''
    testing functionality of zed_20
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_zed_20_12010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_kakugo_12013():
    '''
    testing functionality of kakugo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_kakugo_12013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sync_bre_12015():
    '''
    testing functionality of sync_bre
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sync_bre_12015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_seidr_adaptive_barrier_12029():
    '''
    testing functionality of seidr_adaptive_barrier
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_seidr_adaptive_barrier_12029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_nerine_20_12030():
    '''
    testing functionality of nerine_20
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_nerine_20_12030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bloom_12032():
    '''
    testing functionality of bloom
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bloom_12032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_free_lunch_12035():
    '''
    testing functionality of free_lunch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_free_lunch_12035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_watchtower_12038():
    '''
    testing functionality of watchtower
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_watchtower_12038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_selfadapting_code_wall_12040():
    '''
    testing functionality of selfadapting_code_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_selfadapting_code_wall_12040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_next_opal_12050():
    '''
    testing functionality of next_opal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_next_opal_12050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_authenticator_12055():
    '''
    testing functionality of authenticator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_authenticator_12055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_battlement_12057():
    '''
    testing functionality of battlement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_battlement_12057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_owl_12060():
    '''
    testing functionality of owl
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_owl_12060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_loki_12069():
    '''
    testing functionality of loki
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_loki_12069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_miraju_12071():
    '''
    testing functionality of miraju
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_miraju_12071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_metamorph_12094():
    '''
    testing functionality of metamorph
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_metamorph_12094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_data_loop_12095():
    '''
    testing functionality of data_loop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_data_loop_12095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tithonium_12098():
    '''
    testing functionality of tithonium
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tithonium_12098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sand_storm_12114():
    '''
    testing functionality of sand_storm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sand_storm_12114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_conundrum_12120():
    '''
    testing functionality of conundrum
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_conundrum_12120()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_eli_20_13034():
    '''
    testing functionality of eli_20
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_eli_20_13034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_executive_functioning_13035():
    '''
    testing functionality of executive_functioning
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_executive_functioning_13035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_holmegaard_13036():
    '''
    testing functionality of holmegaard
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_holmegaard_13036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tapestry_13037():
    '''
    testing functionality of tapestry
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tapestry_13037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bloodletter_13047():
    '''
    testing functionality of bloodletter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bloodletter_13047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_colossus_13048():
    '''
    testing functionality of colossus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_colossus_13048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hailstorm_13049():
    '''
    testing functionality of hailstorm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hailstorm_13049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hortum_13050():
    '''
    testing functionality of hortum
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hortum_13050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_weir_13056():
    '''
    testing functionality of weir
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_weir_13056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_machicolation_a_14010():
    '''
    testing functionality of machicolation_a
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_machicolation_a_14010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_machicolation_b_14011():
    '''
    testing functionality of machicolation_b
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_machicolation_b_14011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_heimdall_10_20066():
    '''
    testing functionality of heimdall_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_heimdall_10_20066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hudson_10_20067():
    '''
    testing functionality of hudson_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hudson_10_20067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ichi_10_20068():
    '''
    testing functionality of ichi_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ichi_10_20068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_rototurret_20069():
    '''
    testing functionality of rototurret
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_rototurret_20069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_viktor_10_20070():
    '''
    testing functionality of viktor_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_viktor_10_20070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_archer_20084():
    '''
    testing functionality of archer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_archer_20084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_caduceus_20085():
    '''
    testing functionality of caduceus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_caduceus_20085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hadrians_wall_20086():
    '''
    testing functionality of hadrians_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hadrians_wall_20086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hive_20087():
    '''
    testing functionality of hive
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hive_20087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ice_wall_20088():
    '''
    testing functionality of ice_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ice_wall_20088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_shadow_20089():
    '''
    testing functionality of shadow
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_shadow_20089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_himitsubako_20099():
    '''
    testing functionality of himitsubako
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_himitsubako_20099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_neural_katana_20100():
    '''
    testing functionality of neural_katana
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_neural_katana_20100()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_swordsman_20101():
    '''
    testing functionality of swordsman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_swordsman_20101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wall_of_thorns_20102():
    '''
    testing functionality of wall_of_thorns
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wall_of_thorns_20102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_whirlpool_20103():
    '''
    testing functionality of whirlpool
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_whirlpool_20103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_yagura_20104():
    '''
    testing functionality of yagura
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_yagura_20104()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_data_raven_20113():
    '''
    testing functionality of data_raven
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_data_raven_20113()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_flare_20114():
    '''
    testing functionality of flare
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_flare_20114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_popup_window_20115():
    '''
    testing functionality of popup_window
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_popup_window_20115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tollbooth_20116():
    '''
    testing functionality of tollbooth
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tollbooth_20116()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wraparound_20117():
    '''
    testing functionality of wraparound
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wraparound_20117()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_enigma_20129():
    '''
    testing functionality of enigma
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_enigma_20129()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hunter_20130():
    '''
    testing functionality of hunter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hunter_20130()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wall_of_static_20131():
    '''
    testing functionality of wall_of_static
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wall_of_static_20131()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_najja_10_21011():
    '''
    testing functionality of najja_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_najja_10_21011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_mganga_21013():
    '''
    testing functionality of mganga
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_mganga_21013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_nightdancer_21030():
    '''
    testing functionality of nightdancer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_nightdancer_21030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_aimor_21032():
    '''
    testing functionality of aimor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_aimor_21032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_jua_21034():
    '''
    testing functionality of jua
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_jua_21034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_next_sapphire_21050():
    '''
    testing functionality of next_sapphire
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_next_sapphire_21050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_anansi_21051():
    '''
    testing functionality of anansi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_anansi_21051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sadaka_21073():
    '''
    testing functionality of sadaka
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sadaka_21073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_endless_eula_21074():
    '''
    testing functionality of endless_eula
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_endless_eula_21074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sandman_21075():
    '''
    testing functionality of sandman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sandman_21075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_oduduwa_21079():
    '''
    testing functionality of oduduwa
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_oduduwa_21079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_kamali_10_21092():
    '''
    testing functionality of kamali_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_kamali_10_21092()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_envelope_21095():
    '''
    testing functionality of envelope
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_envelope_21095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_masvingo_21099():
    '''
    testing functionality of masvingo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_masvingo_21099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_next_diamond_21112():
    '''
    testing functionality of next_diamond
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_next_diamond_21112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_mlinzi_21115():
    '''
    testing functionality of mlinzi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_mlinzi_21115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_surveyor_21118():
    '''
    testing functionality of surveyor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_surveyor_21118()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_meridian_22028():
    '''
    testing functionality of meridian
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_meridian_22028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_gatekeeper_22029():
    '''
    testing functionality of gatekeeper
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_gatekeeper_22029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_otoroshi_22038():
    '''
    testing functionality of otoroshi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_otoroshi_22038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_thimblerig_22039():
    '''
    testing functionality of thimblerig
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_thimblerig_22039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_peeping_tom_22045():
    '''
    testing functionality of peeping_tom
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_peeping_tom_22045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hydra_22046():
    '''
    testing functionality of hydra
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hydra_22046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_blockchain_22053():
    '''
    testing functionality of blockchain
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_blockchain_22053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_formicary_22054():
    '''
    testing functionality of formicary
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_formicary_22054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_slot_machine_23045():
    '''
    testing functionality of slot_machine
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_slot_machine_23045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_border_control_23054():
    '''
    testing functionality of border_control
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_border_control_23054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_eli_10_25073():
    '''
    testing functionality of eli_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_eli_10_25073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_heimdall_10_25074():
    '''
    testing functionality of heimdall_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_heimdall_10_25074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ichi_10_25075():
    '''
    testing functionality of ichi_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ichi_10_25075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_rototurret_25076():
    '''
    testing functionality of rototurret
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_rototurret_25076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_turing_25077():
    '''
    testing functionality of turing
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_turing_25077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_viktor_10_25078():
    '''
    testing functionality of viktor_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_viktor_10_25078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_himitsubako_25093():
    '''
    testing functionality of himitsubako
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_himitsubako_25093()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_lotus_field_25094():
    '''
    testing functionality of lotus_field
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_lotus_field_25094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_neural_katana_25095():
    '''
    testing functionality of neural_katana
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_neural_katana_25095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_swordsman_25096():
    '''
    testing functionality of swordsman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_swordsman_25096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tsurugi_25097():
    '''
    testing functionality of tsurugi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tsurugi_25097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wall_of_thorns_25098():
    '''
    testing functionality of wall_of_thorns
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wall_of_thorns_25098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_yagura_25099():
    '''
    testing functionality of yagura
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_yagura_25099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_data_raven_25112():
    '''
    testing functionality of data_raven
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_data_raven_25112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_flare_25113():
    '''
    testing functionality of flare
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_flare_25113()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_popup_window_25114():
    '''
    testing functionality of popup_window
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_popup_window_25114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tollbooth_25115():
    '''
    testing functionality of tollbooth
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tollbooth_25115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wraparound_25116():
    '''
    testing functionality of wraparound
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wraparound_25116()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_archer_25130():
    '''
    testing functionality of archer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_archer_25130()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_caduceus_25131():
    '''
    testing functionality of caduceus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_caduceus_25131()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hadrians_wall_25132():
    '''
    testing functionality of hadrians_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hadrians_wall_25132()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hortum_25133():
    '''
    testing functionality of hortum
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hortum_25133()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ice_wall_25134():
    '''
    testing functionality of ice_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ice_wall_25134()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_spiderweb_25135():
    '''
    testing functionality of spiderweb
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_spiderweb_25135()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_enigma_25143():
    '''
    testing functionality of enigma
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_enigma_25143()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hunter_25144():
    '''
    testing functionality of hunter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hunter_25144()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wall_of_static_25145():
    '''
    testing functionality of wall_of_static
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wall_of_static_25145()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hagen_26035():
    '''
    testing functionality of hagen
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hagen_26035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_saisentan_26044():
    '''
    testing functionality of saisentan
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_saisentan_26044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_congratulations_26050():
    '''
    testing functionality of congratulations
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_congratulations_26050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_loot_box_26051():
    '''
    testing functionality of loot_box
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_loot_box_26051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_afshar_26058():
    '''
    testing functionality of afshar
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_afshar_26058()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_sandstone_26059():
    '''
    testing functionality of sandstone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_sandstone_26059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_trebuchet_26060():
    '''
    testing functionality of trebuchet
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_trebuchet_26060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_rime_26065():
    '''
    testing functionality of rime
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_rime_26065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_drafter_26101():
    '''
    testing functionality of drafter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_drafter_26101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tyr_26102():
    '''
    testing functionality of tyr
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tyr_26102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_engram_flush_26108():
    '''
    testing functionality of engram_flush
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_engram_flush_26108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_konjin_26109():
    '''
    testing functionality of konjin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_konjin_26109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_f2p_26115():
    '''
    testing functionality of f2p
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_f2p_26115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_gold_farmer_26116():
    '''
    testing functionality of gold_farmer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_gold_farmer_26116()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_akhet_26123():
    '''
    testing functionality of akhet
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_akhet_26123()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_colossus_26124():
    '''
    testing functionality of colossus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_colossus_26124()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_winchester_26125():
    '''
    testing functionality of winchester
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_winchester_26125()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_slot_machine_28004():
    '''
    testing functionality of slot_machine
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_slot_machine_28004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_border_control_28005():
    '''
    testing functionality of border_control
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_border_control_28005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_next_bronze_29009():
    '''
    testing functionality of next_bronze
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_next_bronze_29009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_next_silver_29010():
    '''
    testing functionality of next_silver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_next_silver_29010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_excalibur_29017():
    '''
    testing functionality of excalibur
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_excalibur_29017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ansel_10_30038():
    '''
    testing functionality of ansel_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ansel_10_30038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bran_10_30039():
    '''
    testing functionality of bran_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bran_10_30039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_diviner_30046():
    '''
    testing functionality of diviner
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_diviner_30046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_karuna_30047():
    '''
    testing functionality of karuna
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_karuna_30047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_funhouse_30054():
    '''
    testing functionality of funhouse
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_funhouse_30054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ping_30055():
    '''
    testing functionality of ping
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ping_30055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ballista_30062():
    '''
    testing functionality of ballista
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ballista_30062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_pharos_30063():
    '''
    testing functionality of pharos
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_pharos_30063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_palisade_30072():
    '''
    testing functionality of palisade
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_palisade_30072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tithe_30073():
    '''
    testing functionality of tithe
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tithe_30073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_whitespace_30074():
    '''
    testing functionality of whitespace
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_whitespace_30074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_eli_10_31043():
    '''
    testing functionality of eli_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_eli_10_31043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_magnet_31044():
    '''
    testing functionality of magnet
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_magnet_31044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ravana_10_31045():
    '''
    testing functionality of ravana_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ravana_10_31045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_rototurret_31046():
    '''
    testing functionality of rototurret
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_rototurret_31046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_lotus_field_31055():
    '''
    testing functionality of lotus_field
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_lotus_field_31055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_swordsman_31056():
    '''
    testing functionality of swordsman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_swordsman_31056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_popup_window_31065():
    '''
    testing functionality of popup_window
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_popup_window_31065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_tollbooth_31066():
    '''
    testing functionality of tollbooth
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_tollbooth_31066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wraparound_31067():
    '''
    testing functionality of wraparound
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wraparound_31067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_archer_31075():
    '''
    testing functionality of archer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_archer_31075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hortum_31076():
    '''
    testing functionality of hortum
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hortum_31076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ice_wall_31077():
    '''
    testing functionality of ice_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ice_wall_31077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_enigma_31081():
    '''
    testing functionality of enigma
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_enigma_31081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hakarl_10_32004():
    '''
    testing functionality of hakarl_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hakarl_10_32004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_anemone_32005():
    '''
    testing functionality of anemone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_anemone_32005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_echo_33035():
    '''
    testing functionality of echo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_echo_33035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hakarl_10_33036():
    '''
    testing functionality of hakarl_10
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hakarl_10_33036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_wave_33037():
    '''
    testing functionality of wave
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_wave_33037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_anemone_33043():
    '''
    testing functionality of anemone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_anemone_33043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bathynomus_33044():
    '''
    testing functionality of bathynomus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bathynomus_33044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_ivik_33045():
    '''
    testing functionality of ivik
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_ivik_33045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_mestnichestvo_33053():
    '''
    testing functionality of mestnichestvo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_mestnichestvo_33053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_vasilisa_33054():
    '''
    testing functionality of vasilisa
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_vasilisa_33054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_envelopment_33060():
    '''
    testing functionality of envelopment
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_envelopment_33060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_maskirovka_33061():
    '''
    testing functionality of maskirovka
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_maskirovka_33061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_stavka_33062():
    '''
    testing functionality of stavka
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_stavka_33062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_bloop_33098():
    '''
    testing functionality of bloop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_bloop_33098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_pulse_33099():
    '''
    testing functionality of pulse
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_pulse_33099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_hafrun_33108():
    '''
    testing functionality of hafrun
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_hafrun_33108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_vampyronassa_33109():
    '''
    testing functionality of vampyronassa
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_vampyronassa_33109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_klevetnik_33116():
    '''
    testing functionality of klevetnik
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_klevetnik_33116()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_unsmiling_tsarevna_33117():
    '''
    testing functionality of unsmiling_tsarevna
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_unsmiling_tsarevna_33117()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_ice_anvil_33124():
    '''
    testing functionality of anvil
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("ice")

    test_card = ice_anvil_33124()
    test_card.play(test_game_environment.runner,test_game_environment)
