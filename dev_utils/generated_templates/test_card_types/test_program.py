
'''
test cases for card classes of type program
'''
from netrunner_lib.cards._base_card_classes import Program
from netrunner_lib.cards.program import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
def test_program_corroder_01007():
    '''
    testing functionality of corroder
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_corroder_01007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_datasucker_01008():
    '''
    testing functionality of datasucker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_datasucker_01008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_djinn_01009():
    '''
    testing functionality of djinn
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_djinn_01009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_medium_01010():
    '''
    testing functionality of medium
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_medium_01010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_mimic_01011():
    '''
    testing functionality of mimic
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_mimic_01011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_parasite_01012():
    '''
    testing functionality of parasite
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_parasite_01012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_wyrm_01013():
    '''
    testing functionality of wyrm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_wyrm_01013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_yog0_01014():
    '''
    testing functionality of yog0
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_yog0_01014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_aurora_01025():
    '''
    testing functionality of aurora
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_aurora_01025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_femme_fatale_01026():
    '''
    testing functionality of femme_fatale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_femme_fatale_01026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_ninja_01027():
    '''
    testing functionality of ninja
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_ninja_01027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sneakdoor_beta_01028():
    '''
    testing functionality of sneakdoor_beta
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sneakdoor_beta_01028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_battering_ram_01042():
    '''
    testing functionality of battering_ram
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_battering_ram_01042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gordian_blade_01043():
    '''
    testing functionality of gordian_blade
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gordian_blade_01043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_magnum_opus_01044():
    '''
    testing functionality of magnum_opus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_magnum_opus_01044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_net_shield_01045():
    '''
    testing functionality of net_shield
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_net_shield_01045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_pipeline_01046():
    '''
    testing functionality of pipeline
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_pipeline_01046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_crypsis_01051():
    '''
    testing functionality of crypsis
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_crypsis_01051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_imp_02003():
    '''
    testing functionality of imp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_imp_02003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_morning_star_02004():
    '''
    testing functionality of morning_star
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_morning_star_02004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_peacock_02006():
    '''
    testing functionality of peacock
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_peacock_02006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_zu13_key_master_02007():
    '''
    testing functionality of zu13_key_master
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_zu13_key_master_02007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_snowball_02027():
    '''
    testing functionality of snowball
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_snowball_02027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_nerve_agent_02041():
    '''
    testing functionality of nerve_agent
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_nerve_agent_02041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_snitch_02045():
    '''
    testing functionality of snitch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_snitch_02045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_disrupter_02061():
    '''
    testing functionality of disrupter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_disrupter_02061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_force_of_nature_02062():
    '''
    testing functionality of force_of_nature
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_force_of_nature_02062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_crescentus_02065():
    '''
    testing functionality of crescentus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_crescentus_02065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_deus_x_02066():
    '''
    testing functionality of deus_x
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_deus_x_02066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_pheromones_02086():
    '''
    testing functionality of pheromones
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_pheromones_02086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_creeper_02089():
    '''
    testing functionality of creeper
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_creeper_02089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_darwin_02102():
    '''
    testing functionality of darwin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_darwin_02102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_faerie_02104():
    '''
    testing functionality of faerie
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_faerie_02104()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_deep_thought_02108():
    '''
    testing functionality of deep_thought
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_deep_thought_02108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_atman_03040():
    '''
    testing functionality of atman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_atman_03040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cloak_03041():
    '''
    testing functionality of cloak
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cloak_03041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_dagger_03042():
    '''
    testing functionality of dagger
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_dagger_03042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_chakana_03043():
    '''
    testing functionality of chakana
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_chakana_03043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cybercypher_03044():
    '''
    testing functionality of cybercypher
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cybercypher_03044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_paricia_03045():
    '''
    testing functionality of paricia
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_paricia_03045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_selfmodifying_code_03046():
    '''
    testing functionality of selfmodifying_code
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_selfmodifying_code_03046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sahasrara_03047():
    '''
    testing functionality of sahasrara
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sahasrara_03047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_inti_03048():
    '''
    testing functionality of inti
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_inti_03048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_pawn_04002():
    '''
    testing functionality of pawn
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_pawn_04002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_rook_04003():
    '''
    testing functionality of rook
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_rook_04003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gorman_drip_v1_04005():
    '''
    testing functionality of gorman_drip_v1
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gorman_drip_v1_04005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_false_echo_04007():
    '''
    testing functionality of false_echo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_false_echo_04007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_bishop_04021():
    '''
    testing functionality of bishop
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_bishop_04021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_scheherazade_04022():
    '''
    testing functionality of scheherazade
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_scheherazade_04022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_copycat_04025():
    '''
    testing functionality of copycat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_copycat_04025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_leviathan_04026():
    '''
    testing functionality of leviathan
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_leviathan_04026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_knight_04043():
    '''
    testing functionality of knight
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_knight_04043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_expert_schedule_analyzer_04045():
    '''
    testing functionality of expert_schedule_analyzer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_expert_schedule_analyzer_04045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_torch_04047():
    '''
    testing functionality of torch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_torch_04047()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_keyhole_04061():
    '''
    testing functionality of keyhole
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_keyhole_04061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_garrote_04065():
    '''
    testing functionality of garrote
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_garrote_04065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sharpshooter_04067():
    '''
    testing functionality of sharpshooter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sharpshooter_04067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_hemorrhage_04082():
    '''
    testing functionality of hemorrhage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_hemorrhage_04082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_alpha_04087():
    '''
    testing functionality of alpha
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_alpha_04087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_omega_04088():
    '''
    testing functionality of omega
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_omega_04088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_savoirfaire_04105():
    '''
    testing functionality of savoirfaire
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_savoirfaire_04105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_paintbrush_04108():
    '''
    testing functionality of paintbrush
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_paintbrush_04108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_alias_05041():
    '''
    testing functionality of alias
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_alias_05041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_breach_05042():
    '''
    testing functionality of breach
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_breach_05042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_bug_05043():
    '''
    testing functionality of bug
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_bug_05043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gingerbread_05044():
    '''
    testing functionality of gingerbread
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gingerbread_05044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_grappling_hook_05045():
    '''
    testing functionality of grappling_hook
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_grappling_hook_05045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_passport_05046():
    '''
    testing functionality of passport
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_passport_05046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_overmind_05053():
    '''
    testing functionality of overmind
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_overmind_05053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_lamprey_06014():
    '''
    testing functionality of lamprey
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_lamprey_06014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_leprechaun_06019():
    '''
    testing functionality of leprechaun
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_leprechaun_06019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_d4v1d_06033():
    '''
    testing functionality of d4v1d
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_d4v1d_06033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cache_06037():
    '''
    testing functionality of cache
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cache_06037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_llds_energy_regulator_06039():
    '''
    testing functionality of llds_energy_regulator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_llds_energy_regulator_06039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_blackat_06053():
    '''
    testing functionality of blackat
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_blackat_06053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_refractor_06057():
    '''
    testing functionality of refractor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_refractor_06057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_origami_06074():
    '''
    testing functionality of origami
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_origami_06074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_switchblade_06077():
    '''
    testing functionality of switchblade
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_switchblade_06077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cerberus_cuj0_h3_06094():
    '''
    testing functionality of cerberus_cuj0_h3
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cerberus_cuj0_h3_06094()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cerberus_rex_h2_06096():
    '''
    testing functionality of cerberus_rex_h2
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cerberus_rex_h2_06096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cerberus_lady_h1_06099():
    '''
    testing functionality of cerberus_lady_h1
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cerberus_lady_h1_06099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_incubator_06113():
    '''
    testing functionality of incubator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_incubator_06113()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_ixodidae_06114():
    '''
    testing functionality of ixodidae
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_ixodidae_06114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_collective_consciousness_06116():
    '''
    testing functionality of collective_consciousness
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_collective_consciousness_06116()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sage_06117():
    '''
    testing functionality of sage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sage_06117()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_au_revoir_06119():
    '''
    testing functionality of au_revoir
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_au_revoir_06119()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_eater_07040():
    '''
    testing functionality of eater
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_eater_07040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gravedigger_07041():
    '''
    testing functionality of gravedigger
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gravedigger_07041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_hivemind_07042():
    '''
    testing functionality of hivemind
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_hivemind_07042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_progenitor_07043():
    '''
    testing functionality of progenitor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_progenitor_07043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_clot_08001():
    '''
    testing functionality of clot
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_clot_08001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_spike_08004():
    '''
    testing functionality of spike
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_spike_08004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_study_guide_08028():
    '''
    testing functionality of study_guide
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_study_guide_08028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_crowbar_08046():
    '''
    testing functionality of crowbar
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_crowbar_08046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_analog_dreamers_08048():
    '''
    testing functionality of analog_dreamers
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_analog_dreamers_08048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_faust_08061():
    '''
    testing functionality of faust
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_faust_08061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_shiv_08066():
    '''
    testing functionality of shiv
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_shiv_08066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_chameleon_08069():
    '''
    testing functionality of chameleon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_chameleon_08069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_hyperdriver_08070():
    '''
    testing functionality of hyperdriver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_hyperdriver_08070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_trope_08081():
    '''
    testing functionality of trope
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_trope_08081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_surfer_08102():
    '''
    testing functionality of surfer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_surfer_08102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_davinci_08107():
    '''
    testing functionality of davinci
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_davinci_08107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_endless_hunger_09033():
    '''
    testing functionality of endless_hunger
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_endless_hunger_09033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_harbinger_09034():
    '''
    testing functionality of harbinger
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_harbinger_09034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_multithreader_09040():
    '''
    testing functionality of multithreader
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_multithreader_09040()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gs_striker_m1_09048():
    '''
    testing functionality of gs_striker_m1
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gs_striker_m1_09048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gs_shrike_m2_09049():
    '''
    testing functionality of gs_shrike_m2
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gs_shrike_m2_09049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gs_sherman_m3_09050():
    '''
    testing functionality of gs_sherman_m3
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gs_sherman_m3_09050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_mongoose_10005():
    '''
    testing functionality of mongoose
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_mongoose_10005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_panchatantra_10008():
    '''
    testing functionality of panchatantra
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_panchatantra_10008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_diwan_10021():
    '''
    testing functionality of diwan
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_diwan_10021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sadyojata_10044():
    '''
    testing functionality of sadyojata
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sadyojata_10044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_vamadeva_10061():
    '''
    testing functionality of vamadeva
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_vamadeva_10061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_brahman_10062():
    '''
    testing functionality of brahman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_brahman_10062()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_aghora_10097():
    '''
    testing functionality of aghora
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_aghora_10097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_ankusa_10101():
    '''
    testing functionality of ankusa
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_ankusa_10101()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_dai_v_11006():
    '''
    testing functionality of dai_v
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_dai_v_11006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_nfr_11023():
    '''
    testing functionality of nfr
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_nfr_11023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_paperclip_11024():
    '''
    testing functionality of paperclip
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_paperclip_11024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_golden_11025():
    '''
    testing functionality of golden
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_golden_11025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_black_orchestra_11042():
    '''
    testing functionality of black_orchestra
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_black_orchestra_11042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_peregrine_11044():
    '''
    testing functionality of peregrine
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_peregrine_11044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_houdini_11045():
    '''
    testing functionality of houdini
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_houdini_11045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_saker_11064():
    '''
    testing functionality of saker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_saker_11064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_blackstone_11068():
    '''
    testing functionality of blackstone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_blackstone_11068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_mkultra_11081():
    '''
    testing functionality of mkultra
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_mkultra_11081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_equivocation_11084():
    '''
    testing functionality of equivocation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_equivocation_11084()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_misdirection_11085():
    '''
    testing functionality of misdirection
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_misdirection_11085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_reaver_11086():
    '''
    testing functionality of reaver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_reaver_11086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_baba_yaga_11088():
    '''
    testing functionality of baba_yaga
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_baba_yaga_11088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sunya_11102():
    '''
    testing functionality of sunya
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sunya_11102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_tapwrm_11104():
    '''
    testing functionality of tapwrm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_tapwrm_11104()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_tracker_11105():
    '''
    testing functionality of tracker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_tracker_11105()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_fawkes_11108():
    '''
    testing functionality of fawkes
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_fawkes_11108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_customized_secretary_12027():
    '''
    testing functionality of customized_secretary
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_customized_secretary_12027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_berserker_12041():
    '''
    testing functionality of berserker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_berserker_12041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_persephone_12042():
    '''
    testing functionality of persephone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_persephone_12042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_inversificator_12048():
    '''
    testing functionality of inversificator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_inversificator_12048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_massdriver_12067():
    '''
    testing functionality of massdriver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_massdriver_12067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_god_of_war_12082():
    '''
    testing functionality of god_of_war
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_god_of_war_12082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_flashbang_12085():
    '''
    testing functionality of flashbang
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_flashbang_12085()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_maven_12087():
    '''
    testing functionality of maven
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_maven_12087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_nanotk_12088():
    '''
    testing functionality of nanotk
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_nanotk_12088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_aumakua_12104():
    '''
    testing functionality of aumakua
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_aumakua_12104()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_abagnale_13006():
    '''
    testing functionality of abagnale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_abagnale_13006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_lustig_13007():
    '''
    testing functionality of lustig
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_lustig_13007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_demara_13008():
    '''
    testing functionality of demara
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_demara_13008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_mammon_13009():
    '''
    testing functionality of mammon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_mammon_13009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_adept_13017():
    '''
    testing functionality of adept
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_adept_13017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_savant_13018():
    '''
    testing functionality of savant
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_savant_13018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_egret_13019():
    '''
    testing functionality of egret
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_egret_13019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_dhegdheer_13020():
    '''
    testing functionality of dhegdheer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_dhegdheer_13020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_surveillance_network_key_14018():
    '''
    testing functionality of surveillance_network_key
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_surveillance_network_key_14018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_surveillance_network_key_2_14019():
    '''
    testing functionality of surveillance_network_key_2
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_surveillance_network_key_2_14019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sneakdoor_prime_a_14026():
    '''
    testing functionality of sneakdoor_prime_a
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sneakdoor_prime_a_14026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sneakdoor_prime_b_14027():
    '''
    testing functionality of sneakdoor_prime_b
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sneakdoor_prime_b_14027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_darwin_20008():
    '''
    testing functionality of darwin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_darwin_20008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_datasucker_20009():
    '''
    testing functionality of datasucker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_datasucker_20009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_force_of_nature_20010():
    '''
    testing functionality of force_of_nature
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_force_of_nature_20010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_imp_20011():
    '''
    testing functionality of imp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_imp_20011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_hemorrhage_20012():
    '''
    testing functionality of hemorrhage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_hemorrhage_20012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_mimic_20013():
    '''
    testing functionality of mimic
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_mimic_20013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_morning_star_20014():
    '''
    testing functionality of morning_star
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_morning_star_20014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_aurora_20027():
    '''
    testing functionality of aurora
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_aurora_20027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_faerie_20028():
    '''
    testing functionality of faerie
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_faerie_20028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_femme_fatale_20029():
    '''
    testing functionality of femme_fatale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_femme_fatale_20029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_peacock_20030():
    '''
    testing functionality of peacock
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_peacock_20030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_pheromones_20031():
    '''
    testing functionality of pheromones
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_pheromones_20031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sneakdoor_beta_20032():
    '''
    testing functionality of sneakdoor_beta
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sneakdoor_beta_20032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_battering_ram_20048():
    '''
    testing functionality of battering_ram
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_battering_ram_20048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gordian_blade_20049():
    '''
    testing functionality of gordian_blade
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gordian_blade_20049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_magnum_opus_20050():
    '''
    testing functionality of magnum_opus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_magnum_opus_20050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_pipeline_20051():
    '''
    testing functionality of pipeline
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_pipeline_20051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_crypsis_20058():
    '''
    testing functionality of crypsis
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_crypsis_20058()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_yusuf_21002():
    '''
    testing functionality of yusuf
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_yusuf_21002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_puffer_21004():
    '''
    testing functionality of puffer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_puffer_21004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_upya_21007():
    '''
    testing functionality of upya
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_upya_21007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_plague_21022():
    '''
    testing functionality of plague
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_plague_21022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_wari_21024():
    '''
    testing functionality of wari
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_wari_21024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_takobi_21026():
    '''
    testing functionality of takobi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_takobi_21026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_rng_key_21029():
    '''
    testing functionality of rng_key
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_rng_key_21029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_exer_21041():
    '''
    testing functionality of exer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_exer_21041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_nyashia_21067():
    '''
    testing functionality of nyashia
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_nyashia_21067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_consume_21068():
    '''
    testing functionality of consume
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_consume_21068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_trypano_21082():
    '''
    testing functionality of trypano
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_trypano_21082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_laamb_21086():
    '''
    testing functionality of laamb
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_laamb_21086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_musaazi_21102():
    '''
    testing functionality of musaazi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_musaazi_21102()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_amina_21104():
    '''
    testing functionality of amina
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_amina_21104()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_engolo_21108():
    '''
    testing functionality of engolo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_engolo_21108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cradle_22006():
    '''
    testing functionality of cradle
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cradle_22006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_bankroll_22011():
    '''
    testing functionality of bankroll
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_bankroll_22011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_tycoon_22012():
    '''
    testing functionality of tycoon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_tycoon_22012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_ika_22019():
    '''
    testing functionality of ika
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_ika_22019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_kyuban_22020():
    '''
    testing functionality of kyuban
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_kyuban_22020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_algernon_22022():
    '''
    testing functionality of algernon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_algernon_22022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_corroder_25010():
    '''
    testing functionality of corroder
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_corroder_25010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_datasucker_25011():
    '''
    testing functionality of datasucker
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_datasucker_25011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_force_of_nature_25012():
    '''
    testing functionality of force_of_nature
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_force_of_nature_25012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_imp_25013():
    '''
    testing functionality of imp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_imp_25013()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_lamprey_25014():
    '''
    testing functionality of lamprey
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_lamprey_25014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_mimic_25015():
    '''
    testing functionality of mimic
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_mimic_25015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_abagnale_25033():
    '''
    testing functionality of abagnale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_abagnale_25033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_demara_25034():
    '''
    testing functionality of demara
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_demara_25034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_faerie_25035():
    '''
    testing functionality of faerie
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_faerie_25035()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_femme_fatale_25036():
    '''
    testing functionality of femme_fatale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_femme_fatale_25036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sneakdoor_beta_25037():
    '''
    testing functionality of sneakdoor_beta
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sneakdoor_beta_25037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_atman_25051():
    '''
    testing functionality of atman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_atman_25051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_battering_ram_25052():
    '''
    testing functionality of battering_ram
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_battering_ram_25052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_deus_x_25053():
    '''
    testing functionality of deus_x
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_deus_x_25053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gordian_blade_25054():
    '''
    testing functionality of gordian_blade
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gordian_blade_25054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_pipeline_25055():
    '''
    testing functionality of pipeline
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_pipeline_25055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_crypsis_25061():
    '''
    testing functionality of crypsis
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_crypsis_25061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_chisel_26003():
    '''
    testing functionality of chisel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_chisel_26003()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_stargate_26004():
    '''
    testing functionality of stargate
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_stargate_26004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_utae_26005():
    '''
    testing functionality of utae
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_utae_26005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_bukhgalter_26016():
    '''
    testing functionality of bukhgalter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_bukhgalter_26016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gauss_26024():
    '''
    testing functionality of gauss
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gauss_26024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_pelangi_26025():
    '''
    testing functionality of pelangi
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_pelangi_26025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_rezeki_26026():
    '''
    testing functionality of rezeki
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_rezeki_26026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_odore_26071():
    '''
    testing functionality of odore
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_odore_26071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_afterimage_26079():
    '''
    testing functionality of afterimage
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_afterimage_26079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_makler_26080():
    '''
    testing functionality of makler
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_makler_26080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cordyceps_26086():
    '''
    testing functionality of cordyceps
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cordyceps_26086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_euler_26087():
    '''
    testing functionality of euler
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_euler_26087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_mantle_26088():
    '''
    testing functionality of mantle
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_mantle_26088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_penrose_26089():
    '''
    testing functionality of penrose
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_penrose_26089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_selfmodifying_code_26090():
    '''
    testing functionality of selfmodifying_code
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_selfmodifying_code_26090()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_medium_29001():
    '''
    testing functionality of medium
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_medium_29001()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_parasite_29002():
    '''
    testing functionality of parasite
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_parasite_29002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cache_29004():
    '''
    testing functionality of cache
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cache_29004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cerberus_lady_h1_29006():
    '''
    testing functionality of cerberus_lady_h1
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cerberus_lady_h1_29006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_botulus_30004():
    '''
    testing functionality of botulus
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_botulus_30004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_buzzsaw_30005():
    '''
    testing functionality of buzzsaw
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_buzzsaw_30005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cleaver_30006():
    '''
    testing functionality of cleaver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cleaver_30006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_fermenter_30007():
    '''
    testing functionality of fermenter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_fermenter_30007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_leech_30008():
    '''
    testing functionality of leech
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_leech_30008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_carmen_30015():
    '''
    testing functionality of carmen
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_carmen_30015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_marjanah_30016():
    '''
    testing functionality of marjanah
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_marjanah_30016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_tranquilizer_30017():
    '''
    testing functionality of tranquilizer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_tranquilizer_30017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_conduit_30024():
    '''
    testing functionality of conduit
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_conduit_30024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_echelon_30025():
    '''
    testing functionality of echelon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_echelon_30025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_unity_30026():
    '''
    testing functionality of unity
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_unity_30026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_mayfly_30032():
    '''
    testing functionality of mayfly
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_mayfly_30032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_clot_31005():
    '''
    testing functionality of clot
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_clot_31005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_corroder_31006():
    '''
    testing functionality of corroder
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_corroder_31006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_imp_31007():
    '''
    testing functionality of imp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_imp_31007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_mimic_31008():
    '''
    testing functionality of mimic
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_mimic_31008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_abagnale_31021():
    '''
    testing functionality of abagnale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_abagnale_31021()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_femme_fatale_31022():
    '''
    testing functionality of femme_fatale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_femme_fatale_31022()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_sneakdoor_beta_31023():
    '''
    testing functionality of sneakdoor_beta
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_sneakdoor_beta_31023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_atman_31030():
    '''
    testing functionality of atman
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_atman_31030()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_chameleon_31031():
    '''
    testing functionality of chameleon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_chameleon_31031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_egret_31032():
    '''
    testing functionality of egret
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_egret_31032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_gordian_blade_31033():
    '''
    testing functionality of gordian_blade
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_gordian_blade_31033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_paricia_31034():
    '''
    testing functionality of paricia
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_paricia_31034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_revolver_32002():
    '''
    testing functionality of revolver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_revolver_32002()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_begemot_33007():
    '''
    testing functionality of begemot
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_begemot_33007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cats_cradle_33016():
    '''
    testing functionality of cats_cradle
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cats_cradle_33016()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_cezve_33017():
    '''
    testing functionality of cezve
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_cezve_33017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_revolver_33018():
    '''
    testing functionality of revolver
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_revolver_33018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_hyperbaric_33026():
    '''
    testing functionality of hyperbaric
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_hyperbaric_33026()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_propeller_33027():
    '''
    testing functionality of propeller
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_propeller_33027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_abaasy_33070():
    '''
    testing functionality of abaasy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_abaasy_33070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_hush_33071():
    '''
    testing functionality of hush
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_hush_33071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_nga_33072():
    '''
    testing functionality of nga
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_nga_33072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_num_33073():
    '''
    testing functionality of num
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_num_33073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_tremolo_33080():
    '''
    testing functionality of tremolo
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_tremolo_33080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_tunnel_vision_33081():
    '''
    testing functionality of tunnel_vision
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_tunnel_vision_33081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_flux_capacitor_33087():
    '''
    testing functionality of flux_capacitor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_flux_capacitor_33087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_nanuq_33088():
    '''
    testing functionality of nanuq
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_nanuq_33088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_orca_33089():
    '''
    testing functionality of orca
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_orca_33089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_k2cp_turbine_33090():
    '''
    testing functionality of k2cp_turbine
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_k2cp_turbine_33090()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_world_tree_33091():
    '''
    testing functionality of world_tree
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_world_tree_33091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_program_matryoshka_33094():
    '''
    testing functionality of matryoshka
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("program")

    test_card = program_matryoshka_33094()
    test_card.play(test_game_environment.runner,test_game_environment)
