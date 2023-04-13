
'''
test cases for card classes of type hardware
'''
from netrunner_lib.cards._base_card_classes import Hardware
from netrunner_lib.cards.hardware import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
def test_hardware_cyberfeeder_01005():
    '''
    testing functionality of cyberfeeder
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_cyberfeeder_01005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_grimoire_01006():
    '''
    testing functionality of grimoire
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_grimoire_01006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_lemuria_codecracker_01023():
    '''
    testing functionality of lemuria_codecracker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_lemuria_codecracker_01023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_desperado_01024():
    '''
    testing functionality of desperado
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_desperado_01024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_akamatsu_mem_chip_01038():
    '''
    testing functionality of akamatsu_mem_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_akamatsu_mem_chip_01038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_rabbit_hole_01039():
    '''
    testing functionality of rabbit_hole
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_rabbit_hole_01039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_the_personal_touch_01040():
    '''
    testing functionality of the_personal_touch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_the_personal_touch_01040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_the_toolbox_01041():
    '''
    testing functionality of the_toolbox
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_the_toolbox_01041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_spinal_modem_02002():
    '''
    testing functionality of spinal_modem
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_spinal_modem_02002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_cortez_chip_02005():
    '''
    testing functionality of cortez_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_cortez_chip_02005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_plascrete_carapace_02009():
    '''
    testing functionality of plascrete_carapace
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_plascrete_carapace_02009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_e3_feedback_implants_02024():
    '''
    testing functionality of e3_feedback_implants
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_e3_feedback_implants_02024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_dyson_mem_chip_02028():
    '''
    testing functionality of dyson_mem_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_dyson_mem_chip_02028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_muresh_bodysuit_02044():
    '''
    testing functionality of muresh_bodysuit
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_muresh_bodysuit_02044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_dinosaurus_02048():
    '''
    testing functionality of dinosaurus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_dinosaurus_02048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_doppelganger_02064():
    '''
    testing functionality of doppelganger
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_doppelganger_02064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_hq_interface_02085():
    '''
    testing functionality of hq_interface
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_hq_interface_02085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_replicator_02088():
    '''
    testing functionality of replicator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_replicator_02088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_rd_interface_02107():
    '''
    testing functionality of rd_interface
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_rd_interface_02107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_monolith_03036():
    '''
    testing functionality of monolith
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_monolith_03036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_feedback_filter_03037():
    '''
    testing functionality of feedback_filter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_feedback_filter_03037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_clone_chip_03038():
    '''
    testing functionality of clone_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_clone_chip_03038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_omnidrive_03039():
    '''
    testing functionality of omnidrive
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_omnidrive_03039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_lockpick_04006():
    '''
    testing functionality of lockpick
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_lockpick_04006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_record_reconstructor_04028():
    '''
    testing functionality of record_reconstructor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_record_reconstructor_04028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_prepaid_voicepad_04029():
    '''
    testing functionality of prepaid_voicepad
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_prepaid_voicepad_04029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_deep_red_04042():
    '''
    testing functionality of deep_red
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_deep_red_04042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_llds_processor_04066():
    '''
    testing functionality of llds_processor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_llds_processor_04066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_capstone_04068():
    '''
    testing functionality of capstone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_capstone_04068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_blackguard_04085():
    '''
    testing functionality of blackguard
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_blackguard_04085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_cybersolutions_mem_chip_04086():
    '''
    testing functionality of cybersolutions_mem_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_cybersolutions_mem_chip_04086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_dyson_fractal_generator_04103():
    '''
    testing functionality of dyson_fractal_generator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_dyson_fractal_generator_04103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_silencer_04104():
    '''
    testing functionality of silencer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_silencer_04104()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_logos_05037():
    '''
    testing functionality of logos
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_logos_05037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_public_terminal_05038():
    '''
    testing functionality of public_terminal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_public_terminal_05038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_unregistered_sw_35_05039():
    '''
    testing functionality of unregistered_sw_35
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_unregistered_sw_35_05039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_window_05040():
    '''
    testing functionality of window
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_window_05040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_qcoherence_chip_05052():
    '''
    testing functionality of qcoherence_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_qcoherence_chip_05052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_boxe_06055():
    '''
    testing functionality of boxe
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_boxe_06055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_autoscripter_06076():
    '''
    testing functionality of autoscripter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_autoscripter_06076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_astrolabe_06079():
    '''
    testing functionality of astrolabe
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_astrolabe_06079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_ekomind_06093():
    '''
    testing functionality of ekomind
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_ekomind_06093()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_cybsoft_macrodrive_06098():
    '''
    testing functionality of cybsoft_macrodrive
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_cybsoft_macrodrive_06098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_archives_interface_07044():
    '''
    testing functionality of archives_interface
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_archives_interface_07044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_chop_bot_3000_07045():
    '''
    testing functionality of chop_bot_3000
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_chop_bot_3000_07045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_memstrips_07046():
    '''
    testing functionality of memstrips
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_memstrips_07046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_vigil_07047():
    '''
    testing functionality of vigil
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_vigil_07047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_qianju_pt_07054():
    '''
    testing functionality of qianju_pt
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_qianju_pt_07054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_dorm_computer_08024():
    '''
    testing functionality of dorm_computer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_dorm_computer_08024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_comet_08027():
    '''
    testing functionality of comet
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_comet_08027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_skulljack_08042():
    '''
    testing functionality of skulljack
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_skulljack_08042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_turntable_08043():
    '''
    testing functionality of turntable
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_turntable_08043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_titanium_ribs_08045():
    '''
    testing functionality of titanium_ribs
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_titanium_ribs_08045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_netready_eyes_08047():
    '''
    testing functionality of netready_eyes
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_netready_eyes_08047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_brain_cage_08049():
    '''
    testing functionality of brain_cage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_brain_cage_08049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_forger_08065():
    '''
    testing functionality of forger
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_forger_08065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_bookmark_08106():
    '''
    testing functionality of bookmark
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_bookmark_08106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_heartbeat_09032():
    '''
    testing functionality of heartbeat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_heartbeat_09032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_brain_chip_09039():
    '''
    testing functionality of brain_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_brain_chip_09039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_security_chip_09046():
    '''
    testing functionality of security_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_security_chip_09046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_security_nexus_09047():
    '''
    testing functionality of security_nexus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_security_nexus_09047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_ramujanreliant_550_bmi_10002():
    '''
    testing functionality of ramujanreliant_550_bmi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_ramujanreliant_550_bmi_10002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_maya_10007():
    '''
    testing functionality of maya
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_maya_10007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_emp_device_10020():
    '''
    testing functionality of emp_device
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_emp_device_10020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_netchip_10024():
    '''
    testing functionality of netchip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_netchip_10024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_reflection_10041():
    '''
    testing functionality of reflection
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_reflection_10041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_spy_camera_10042():
    '''
    testing functionality of spy_camera
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_spy_camera_10042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_sports_hopper_10064():
    '''
    testing functionality of sports_hopper
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_sports_hopper_10064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_gpi_net_tap_11003():
    '''
    testing functionality of gpi_net_tap
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_gpi_net_tap_11003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_mirror_11005():
    '''
    testing functionality of mirror
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_mirror_11005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_obelus_11041():
    '''
    testing functionality of obelus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_obelus_11041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_the_gauntlet_11063():
    '''
    testing functionality of the_gauntlet
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_the_gauntlet_11063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_top_hat_11067():
    '''
    testing functionality of top_hat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_top_hat_11067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_sifr_11101():
    '''
    testing functionality of sifr
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_sifr_11101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_recon_drone_11103():
    '''
    testing functionality of recon_drone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_recon_drone_11103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_maw_12002():
    '''
    testing functionality of maw
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_maw_12002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_severnius_stim_implant_12021():
    '''
    testing functionality of severnius_stim_implant
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_severnius_stim_implant_12021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_rubicon_switch_12043():
    '''
    testing functionality of rubicon_switch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_rubicon_switch_12043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_adjusted_matrix_12046():
    '''
    testing functionality of adjusted_matrix
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_adjusted_matrix_12046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_dedicated_processor_12047():
    '''
    testing functionality of dedicated_processor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_dedicated_processor_12047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_maui_12063():
    '''
    testing functionality of maui
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_maui_12063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_daredevil_12066():
    '''
    testing functionality of daredevil
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_daredevil_12066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_respirocytes_12102():
    '''
    testing functionality of respirocytes
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_respirocytes_12102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_polyhistor_13005():
    '''
    testing functionality of polyhistor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_polyhistor_13005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_llds_memory_diamond_13015():
    '''
    testing functionality of llds_memory_diamond
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_llds_memory_diamond_13015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_ubax_13016():
    '''
    testing functionality of ubax
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_ubax_13016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_bmi_buffer_14020():
    '''
    testing functionality of bmi_buffer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_bmi_buffer_14020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_bmi_buffer_2_14021():
    '''
    testing functionality of bmi_buffer_2
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_bmi_buffer_2_14021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_cyberfeeder_20006():
    '''
    testing functionality of cyberfeeder
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_cyberfeeder_20006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_spinal_modem_20007():
    '''
    testing functionality of spinal_modem
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_spinal_modem_20007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_doppelganger_20025():
    '''
    testing functionality of doppelganger
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_doppelganger_20025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_hq_interface_20026():
    '''
    testing functionality of hq_interface
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_hq_interface_20026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_dinosaurus_20045():
    '''
    testing functionality of dinosaurus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_dinosaurus_20045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_rabbit_hole_20046():
    '''
    testing functionality of rabbit_hole
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_rabbit_hole_20046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_the_personal_touch_20047():
    '''
    testing functionality of the_personal_touch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_the_personal_touch_20047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_dyson_mem_chip_20057():
    '''
    testing functionality of dyson_mem_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_dyson_mem_chip_20057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_zamba_21003():
    '''
    testing functionality of zamba
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_zamba_21003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_cyberdelia_21006():
    '''
    testing functionality of cyberdelia
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_cyberdelia_21006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_acacia_21021():
    '''
    testing functionality of acacia
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_acacia_21021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_friday_chip_21042():
    '''
    testing functionality of friday_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_friday_chip_21042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_knobkierie_21062():
    '''
    testing functionality of knobkierie
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_knobkierie_21062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_gebrselassie_21087():
    '''
    testing functionality of gebrselassie
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_gebrselassie_21087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_zer0_21101():
    '''
    testing functionality of zer0
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_zer0_21101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_hippo_21103():
    '''
    testing functionality of hippo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_hippo_21103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_flameout_21109():
    '''
    testing functionality of flameout
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_flameout_21109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_patchwork_22004():
    '''
    testing functionality of patchwork
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_patchwork_22004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_hijacked_router_22005():
    '''
    testing functionality of hijacked_router
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_hijacked_router_22005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_paragon_22010():
    '''
    testing functionality of paragon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_paragon_22010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_minds_eye_22017():
    '''
    testing functionality of minds_eye
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_minds_eye_22017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_mache_22018():
    '''
    testing functionality of mache
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_mache_22018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_cyberfeeder_25008():
    '''
    testing functionality of cyberfeeder
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_cyberfeeder_25008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_patchwork_25009():
    '''
    testing functionality of patchwork
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_patchwork_25009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_hq_interface_25031():
    '''
    testing functionality of hq_interface
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_hq_interface_25031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_paragon_25032():
    '''
    testing functionality of paragon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_paragon_25032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_akamatsu_mem_chip_25048():
    '''
    testing functionality of akamatsu_mem_chip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_akamatsu_mem_chip_25048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_dinosaurus_25049():
    '''
    testing functionality of dinosaurus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_dinosaurus_25049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_rd_interface_25050():
    '''
    testing functionality of rd_interface
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_rd_interface_25050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_demolisher_26002():
    '''
    testing functionality of demolisher
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_demolisher_26002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_flip_switch_26013():
    '''
    testing functionality of flip_switch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_flip_switch_26013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_lucky_charm_26014():
    '''
    testing functionality of lucky_charm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_lucky_charm_26014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_masterwork_v37_26015():
    '''
    testing functionality of masterwork_v37
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_masterwork_v37_26015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_supercorridor_26023():
    '''
    testing functionality of supercorridor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_supercorridor_26023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_devil_charm_26068():
    '''
    testing functionality of devil_charm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_devil_charm_26068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_gachapon_26069():
    '''
    testing functionality of gachapon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_gachapon_26069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_keiko_26070():
    '''
    testing functionality of keiko
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_keiko_26070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_boomerang_26075():
    '''
    testing functionality of boomerang
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_boomerang_26075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_mu_safecracker_26076():
    '''
    testing functionality of mu_safecracker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_mu_safecracker_26076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_prognostic_qloop_26077():
    '''
    testing functionality of prognostic_qloop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_prognostic_qloop_26077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_swift_26078():
    '''
    testing functionality of swift
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_swift_26078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_aniccam_26084():
    '''
    testing functionality of aniccam
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_aniccam_26084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_simulchip_26085():
    '''
    testing functionality of simulchip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_simulchip_26085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_buffer_drive_26093():
    '''
    testing functionality of buffer_drive
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_buffer_drive_26093()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_swift_27002():
    '''
    testing functionality of swift
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_swift_27002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_e3_feedback_implants_29003():
    '''
    testing functionality of e3_feedback_implants
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_e3_feedback_implants_29003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_prepaid_voicepad_29008():
    '''
    testing functionality of prepaid_voicepad
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_prepaid_voicepad_29008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_carnivore_30003():
    '''
    testing functionality of carnivore
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_carnivore_30003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_docklands_pass_30013():
    '''
    testing functionality of docklands_pass
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_docklands_pass_30013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_pennyshaver_30014():
    '''
    testing functionality of pennyshaver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_pennyshaver_30014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_dzmz_optimizer_30022():
    '''
    testing functionality of dzmz_optimizer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_dzmz_optimizer_30022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_pantograph_30023():
    '''
    testing functionality of pantograph
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_pantograph_30023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_t400_memory_diamond_30031():
    '''
    testing functionality of t400_memory_diamond
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_t400_memory_diamond_30031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_prepaid_voicepad_31038():
    '''
    testing functionality of prepaid_voicepad
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_prepaid_voicepad_31038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_ghosttongue_33005():
    '''
    testing functionality of ghosttongue
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_ghosttongue_33005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_marrow_33006():
    '''
    testing functionality of marrow
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_marrow_33006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_panweave_33014():
    '''
    testing functionality of panweave
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_panweave_33014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_virtuoso_33015():
    '''
    testing functionality of virtuoso
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_virtuoso_33015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_endurance_33025():
    '''
    testing functionality of endurance
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_endurance_33025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_time_bomb_33069():
    '''
    testing functionality of time_bomb
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_time_bomb_33069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_poison_vial_33077():
    '''
    testing functionality of poison_vial
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_poison_vial_33077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_wake_implant_v2ajrj_33078():
    '''
    testing functionality of wake_implant_v2ajrj
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_wake_implant_v2ajrj_33078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_zenit_chip_jz2mj_33079():
    '''
    testing functionality of zenit_chip_jz2mj
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_zenit_chip_jz2mj_33079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_hippocampic_mechanocytes_33085():
    '''
    testing functionality of hippocampic_mechanocytes
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_hippocampic_mechanocytes_33085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_hardware_basilar_synthgland_2kvj_33086():
    '''
    testing functionality of basilar_synthgland_2kvj
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("hardware")

    test_card = hardware_basilar_synthgland_2kvj_33086()
    test_card.play(test_game_environment.runner,test_game_environment)
