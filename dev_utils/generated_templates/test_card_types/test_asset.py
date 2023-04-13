
'''
test cases for card classes of type asset
'''
from netrunner_lib.cards._base_card_classes import Asset
from netrunner_lib.cards.asset import *
from netrunner_lib.game_state import NetrunnerGame
from netrunner_lib.players import *
from netrunner_lib.tests._test_utilities import *


######################
def test_asset_adonis_campaign_01056():
    '''
    testing functionality of adonis_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_adonis_campaign_01056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_aggressive_secretary_01057():
    '''
    testing functionality of aggressive_secretary
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_aggressive_secretary_01057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_project_junebug_01069():
    '''
    testing functionality of project_junebug
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_project_junebug_01069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_snare_01070():
    '''
    testing functionality of snare
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_snare_01070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_zaibatsu_loyalty_01071():
    '''
    testing functionality of zaibatsu_loyalty
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_zaibatsu_loyalty_01071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ghost_branch_01087():
    '''
    testing functionality of ghost_branch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ghost_branch_01087()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_security_subcontract_01096():
    '''
    testing functionality of security_subcontract
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_security_subcontract_01096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_melange_mining_corp_01108():
    '''
    testing functionality of melange_mining_corp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_melange_mining_corp_01108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_pad_campaign_01109():
    '''
    testing functionality of pad_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_pad_campaign_01109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_encryption_protocol_02029():
    '''
    testing functionality of encryption_protocol
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_encryption_protocol_02029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_edge_of_world_02053():
    '''
    testing functionality of edge_of_world
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_edge_of_world_02053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_marked_accounts_02055():
    '''
    testing functionality of marked_accounts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_marked_accounts_02055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_private_contracts_02059():
    '''
    testing functionality of private_contracts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_private_contracts_02059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_dedicated_server_02072():
    '''
    testing functionality of dedicated_server
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_dedicated_server_02072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_net_police_02075():
    '''
    testing functionality of net_police
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_net_police_02075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_eve_campaign_02092():
    '''
    testing functionality of eve_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_eve_campaign_02092()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ronin_02112():
    '''
    testing functionality of ronin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ronin_02112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_dedicated_response_team_02118():
    '''
    testing functionality of dedicated_response_team
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_dedicated_response_team_02118()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_alix_t4lb07_03008():
    '''
    testing functionality of alix_t4lb07
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_alix_t4lb07_03008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_cerebral_overwriter_03009():
    '''
    testing functionality of cerebral_overwriter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_cerebral_overwriter_03009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_director_haas_03010():
    '''
    testing functionality of director_haas
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_director_haas_03010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_haas_arcology_ai_03011():
    '''
    testing functionality of haas_arcology_ai
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_haas_arcology_ai_03011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_thomas_haas_03012():
    '''
    testing functionality of thomas_haas
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_thomas_haas_03012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_levy_university_03024():
    '''
    testing functionality of levy_university
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_levy_university_03024()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_server_diagnostics_03025():
    '''
    testing functionality of server_diagnostics
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_server_diagnostics_03025()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_jackson_howard_04015():
    '''
    testing functionality of jackson_howard
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_jackson_howard_04015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_elizabeth_mills_04037():
    '''
    testing functionality of elizabeth_mills
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_elizabeth_mills_04037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_isabel_mcguire_04050():
    '''
    testing functionality of isabel_mcguire
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_isabel_mcguire_04050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_sundew_04054():
    '''
    testing functionality of sundew
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_sundew_04054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_city_surveillance_04055():
    '''
    testing functionality of city_surveillance
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_city_surveillance_04055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_rex_campaign_04070():
    '''
    testing functionality of rex_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_rex_campaign_04070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_shock_04073():
    '''
    testing functionality of shock
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_shock_04073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_toshiyuki_sakai_04092():
    '''
    testing functionality of toshiyuki_sakai
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_toshiyuki_sakai_04092()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_grndl_refinery_04099():
    '''
    testing functionality of grndl_refinery
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_grndl_refinery_04099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_broadcast_square_04112():
    '''
    testing functionality of broadcast_square
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_broadcast_square_04112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_chairman_hiro_05008():
    '''
    testing functionality of chairman_hiro
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_chairman_hiro_05008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_mental_health_clinic_05009():
    '''
    testing functionality of mental_health_clinic
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_mental_health_clinic_05009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_psychic_field_05010():
    '''
    testing functionality of psychic_field
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_psychic_field_05010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_shikyu_05011():
    '''
    testing functionality of shikyu
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_shikyu_05011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_tenma_line_05012():
    '''
    testing functionality of tenma_line
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_tenma_line_05012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_plan_b_05023():
    '''
    testing functionality of plan_b
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_plan_b_05023()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_primary_transmission_dish_06006():
    '''
    testing functionality of primary_transmission_dish
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_primary_transmission_dish_06006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_the_root_06008():
    '''
    testing functionality of the_root
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_the_root_06008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_sealed_vault_06029():
    '''
    testing functionality of sealed_vault
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_sealed_vault_06029()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_elizas_toybox_06042():
    '''
    testing functionality of elizas_toybox
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_elizas_toybox_06042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_the_news_now_hour_06045():
    '''
    testing functionality of the_news_now_hour
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_the_news_now_hour_06045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_shattered_remains_06050():
    '''
    testing functionality of shattered_remains
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_shattered_remains_06050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_reversed_accounts_06066():
    '''
    testing functionality of reversed_accounts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_reversed_accounts_06066()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_docklands_crackdown_06072():
    '''
    testing functionality of docklands_crackdown
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_docklands_crackdown_06072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_hostile_infrastructure_06083():
    '''
    testing functionality of hostile_infrastructure
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_hostile_infrastructure_06083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_daily_business_show_06086():
    '''
    testing functionality of daily_business_show
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_daily_business_show_06086()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_executive_boot_camp_06088():
    '''
    testing functionality of executive_boot_camp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_executive_boot_camp_06088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_it_department_06103():
    '''
    testing functionality of it_department
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_it_department_06103()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_turtlebacks_06106():
    '''
    testing functionality of turtlebacks
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_turtlebacks_06106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_constellation_protocol_07008():
    '''
    testing functionality of constellation_protocol
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_constellation_protocol_07008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_mark_yale_07009():
    '''
    testing functionality of mark_yale
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_mark_yale_07009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_space_camp_07010():
    '''
    testing functionality of space_camp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_space_camp_07010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_the_board_07011():
    '''
    testing functionality of the_board
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_the_board_07011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_braintaping_warehouse_08010():
    '''
    testing functionality of braintaping_warehouse
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_braintaping_warehouse_08010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_capital_investors_08018():
    '''
    testing functionality of capital_investors
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_capital_investors_08018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_tech_startup_08020():
    '''
    testing functionality of tech_startup
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_tech_startup_08020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_blacklist_08036():
    '''
    testing functionality of blacklist
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_blacklist_08036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_student_loans_08038():
    '''
    testing functionality of student_loans
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_student_loans_08038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_corporate_town_08059():
    '''
    testing functionality of corporate_town
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_corporate_town_08059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_test_ground_08071():
    '''
    testing functionality of test_ground
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_test_ground_08071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_allele_repression_08073():
    '''
    testing functionality of allele_repression
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_allele_repression_08073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_expose_08075():
    '''
    testing functionality of expose
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_expose_08075()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_contract_killer_08078():
    '''
    testing functionality of contract_killer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_contract_killer_08078()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ronald_five_08088():
    '''
    testing functionality of ronald_five
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ronald_five_08088()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_early_premiere_08095():
    '''
    testing functionality of early_premiere
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_early_premiere_08095()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_cybernetics_court_08109():
    '''
    testing functionality of cybernetics_court
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_cybernetics_court_08109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_team_sponsorship_08110():
    '''
    testing functionality of team_sponsorship
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_team_sponsorship_08110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_genetics_pavilion_08113():
    '''
    testing functionality of genetics_pavilion
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_genetics_pavilion_08113()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_franchise_city_08114():
    '''
    testing functionality of franchise_city
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_franchise_city_08114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_worlds_plaza_08116():
    '''
    testing functionality of worlds_plaza
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_worlds_plaza_08116()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_public_support_08117():
    '''
    testing functionality of public_support
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_public_support_08117()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_lily_lockwell_09008():
    '''
    testing functionality of lily_lockwell
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_lily_lockwell_09008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_news_team_09009():
    '''
    testing functionality of news_team
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_news_team_09009()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_shannon_claire_09010():
    '''
    testing functionality of shannon_claire
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_shannon_claire_09010()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_victoria_jenkins_09011():
    '''
    testing functionality of victoria_jenkins
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_victoria_jenkins_09011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_reality_threedee_09012():
    '''
    testing functionality of reality_threedee
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_reality_threedee_09012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_launch_campaign_09027():
    '''
    testing functionality of launch_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_launch_campaign_09027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_kala_ghoda_real_tv_10015():
    '''
    testing functionality of kala_ghoda_real_tv
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_kala_ghoda_real_tv_10015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_mumba_temple_10018():
    '''
    testing functionality of mumba_temple
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_mumba_temple_10018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_museum_of_history_10019():
    '''
    testing functionality of museum_of_history
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_museum_of_history_10019()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_advanced_assembly_lines_10027():
    '''
    testing functionality of advanced_assembly_lines
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_advanced_assembly_lines_10027()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_lakshmi_smartfabrics_10028():
    '''
    testing functionality of lakshmi_smartfabrics
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_lakshmi_smartfabrics_10028()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_palana_agroplex_10031():
    '''
    testing functionality of palana_agroplex
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_palana_agroplex_10031()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_mumbad_construction_co_10036():
    '''
    testing functionality of mumbad_construction_co
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_mumbad_construction_co_10036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_pad_factory_10038():
    '''
    testing functionality of pad_factory
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_pad_factory_10038()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_clone_suffrage_movement_10049():
    '''
    testing functionality of clone_suffrage_movement
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_clone_suffrage_movement_10049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_bioethics_association_10050():
    '''
    testing functionality of bioethics_association
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_bioethics_association_10050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_political_dealings_10051():
    '''
    testing functionality of political_dealings
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_political_dealings_10051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_sensie_actors_union_10053():
    '''
    testing functionality of sensie_actors_union
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_sensie_actors_union_10053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_commercial_bankers_group_10054():
    '''
    testing functionality of commercial_bankers_group
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_commercial_bankers_group_10054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_mumbad_city_hall_10055():
    '''
    testing functionality of mumbad_city_hall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_mumbad_city_hall_10055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_jeeves_model_bioroids_10067():
    '''
    testing functionality of jeeves_model_bioroids
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_jeeves_model_bioroids_10067()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_raman_rai_10068():
    '''
    testing functionality of raman_rai
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_raman_rai_10068()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_aryabhata_tech_10070():
    '''
    testing functionality of aryabhata_tech
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_aryabhata_tech_10070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_executive_search_firm_10072():
    '''
    testing functionality of executive_search_firm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_executive_search_firm_10072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_indian_union_stock_exchange_10073():
    '''
    testing functionality of indian_union_stock_exchange
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_indian_union_stock_exchange_10073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_full_immersion_recstudio_10108():
    '''
    testing functionality of full_immersion_recstudio
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_full_immersion_recstudio_10108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ibrahim_salem_10109():
    '''
    testing functionality of ibrahim_salem
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ibrahim_salem_10109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_zealous_judge_10111():
    '''
    testing functionality of zealous_judge
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_zealous_judge_10111()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_hyoubu_research_facility_11012():
    '''
    testing functionality of hyoubu_research_facility
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_hyoubu_research_facility_11012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_watchdog_11015():
    '''
    testing functionality of watchdog
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_watchdog_11015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_sandburg_11020():
    '''
    testing functionality of sandburg
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_sandburg_11020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ci_fund_11036():
    '''
    testing functionality of ci_fund
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ci_fund_11036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_alexa_belsky_11055():
    '''
    testing functionality of alexa_belsky
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_alexa_belsky_11055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_fumiko_yamamori_11073():
    '''
    testing functionality of fumiko_yamamori
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_fumiko_yamamori_11073()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_chief_slee_11077():
    '''
    testing functionality of chief_slee
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_chief_slee_11077()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_anson_rose_11096():
    '''
    testing functionality of anson_rose
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_anson_rose_11096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_nasx_11118():
    '''
    testing functionality of nasx
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_nasx_11118()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_synth_dna_modification_12012():
    '''
    testing functionality of synth_dna_modification
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_synth_dna_modification_12012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_net_analytics_12014():
    '''
    testing functionality of net_analytics
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_net_analytics_12014()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_quarantine_system_12017():
    '''
    testing functionality of quarantine_system
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_quarantine_system_12017()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_cpc_generator_12034():
    '''
    testing functionality of cpc_generator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_cpc_generator_12034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_clyde_van_rite_12037():
    '''
    testing functionality of clyde_van_rite
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_clyde_van_rite_12037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_bioroid_work_crew_12051():
    '''
    testing functionality of bioroid_work_crew
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_bioroid_work_crew_12051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_whampoa_reclamation_12079():
    '''
    testing functionality of whampoa_reclamation
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_whampoa_reclamation_12079()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_open_forum_12097():
    '''
    testing functionality of open_forum
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_open_forum_12097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_mca_austerity_policy_12111():
    '''
    testing functionality of mca_austerity_policy
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_mca_austerity_policy_12111()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_breached_dome_12113():
    '''
    testing functionality of breached_dome
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_breached_dome_12113()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_estelle_moon_13032():
    '''
    testing functionality of estelle_moon
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_estelle_moon_13032()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_marilyn_campaign_13033():
    '''
    testing functionality of marilyn_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_marilyn_campaign_13033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_illegal_arms_factory_13045():
    '''
    testing functionality of illegal_arms_factory
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_illegal_arms_factory_13045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_mr_stone_13046():
    '''
    testing functionality of mr_stone
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_mr_stone_13046()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_honeyfarm_13054():
    '''
    testing functionality of honeyfarm
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_honeyfarm_13054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_longterm_investment_13055():
    '''
    testing functionality of longterm_investment
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_longterm_investment_13055()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_investigator_inez_delgado_a_14004():
    '''
    testing functionality of investigator_inez_delgado_a
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_investigator_inez_delgado_a_14004()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_investigator_inez_delgado_a_2_14005():
    '''
    testing functionality of investigator_inez_delgado_a_2
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_investigator_inez_delgado_a_2_14005()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_lt_todachine_14006():
    '''
    testing functionality of lt_todachine
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_lt_todachine_14006()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_lt_todachine_2_14007():
    '''
    testing functionality of lt_todachine_2
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_lt_todachine_2_14007()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_trojan_14008():
    '''
    testing functionality of trojan
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_trojan_14008()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_adonis_campaign_20064():
    '''
    testing functionality of adonis_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_adonis_campaign_20064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_aggressive_secretary_20065():
    '''
    testing functionality of aggressive_secretary
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_aggressive_secretary_20065()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_dedicated_response_team_20081():
    '''
    testing functionality of dedicated_response_team
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_dedicated_response_team_20081()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_elizabeth_mills_20082():
    '''
    testing functionality of elizabeth_mills
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_elizabeth_mills_20082()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_grndl_refinery_20083():
    '''
    testing functionality of grndl_refinery
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_grndl_refinery_20083()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_project_junebug_20096():
    '''
    testing functionality of project_junebug
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_project_junebug_20096()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ronin_20097():
    '''
    testing functionality of ronin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ronin_20097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_snare_20098():
    '''
    testing functionality of snare
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_snare_20098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ghost_branch_20112():
    '''
    testing functionality of ghost_branch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ghost_branch_20112()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_melange_mining_corp_20127():
    '''
    testing functionality of melange_mining_corp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_melange_mining_corp_20127()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_pad_campaign_20128():
    '''
    testing functionality of pad_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_pad_campaign_20128()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_gene_splicer_21012():
    '''
    testing functionality of gene_splicer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_gene_splicer_21012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_echo_chamber_21015():
    '''
    testing functionality of echo_chamber
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_echo_chamber_21015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_urban_renewal_21018():
    '''
    testing functionality of urban_renewal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_urban_renewal_21018()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_reconstruction_contract_21020():
    '''
    testing functionality of reconstruction_contract
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_reconstruction_contract_21020()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ngo_front_21039():
    '''
    testing functionality of ngo_front
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ngo_front_21039()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_kuwinda_k4h1u3_21049():
    '''
    testing functionality of kuwinda_k4h1u3
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_kuwinda_k4h1u3_21049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_personalized_portal_21056():
    '''
    testing functionality of personalized_portal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_personalized_portal_21056()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_technoco_21060():
    '''
    testing functionality of technoco
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_technoco_21060()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_malia_z0l0k4_21069():
    '''
    testing functionality of malia_z0l0k4
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_malia_z0l0k4_21069()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_amani_senai_21076():
    '''
    testing functionality of amani_senai
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_amani_senai_21076()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_rashida_jaheem_21080():
    '''
    testing functionality of rashida_jaheem
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_rashida_jaheem_21080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_warden_fatuma_21093():
    '''
    testing functionality of warden_fatuma
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_warden_fatuma_21093()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_false_flag_21120():
    '''
    testing functionality of false_flag
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_false_flag_21120()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_apis_keeper_isobel_22036():
    '''
    testing functionality of apis_keeper_isobel
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_apis_keeper_isobel_22036()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_neurostasis_22037():
    '''
    testing functionality of neurostasis
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_neurostasis_22037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_siu_22044():
    '''
    testing functionality of siu
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_siu_22044()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_drudge_work_22052():
    '''
    testing functionality of drudge_work
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_drudge_work_22052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_lady_liberty_22058():
    '''
    testing functionality of lady_liberty
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_lady_liberty_22058()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_adonis_campaign_25070():
    '''
    testing functionality of adonis_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_adonis_campaign_25070()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_aggressive_secretary_25071():
    '''
    testing functionality of aggressive_secretary
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_aggressive_secretary_25071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_marilyn_campaign_25072():
    '''
    testing functionality of marilyn_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_marilyn_campaign_25072()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_project_junebug_25089():
    '''
    testing functionality of project_junebug
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_project_junebug_25089()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ronin_25090():
    '''
    testing functionality of ronin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ronin_25090()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_snare_25091():
    '''
    testing functionality of snare
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_snare_25091()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_sundew_25092():
    '''
    testing functionality of sundew
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_sundew_25092()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_daily_business_show_25108():
    '''
    testing functionality of daily_business_show
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_daily_business_show_25108()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ghost_branch_25109():
    '''
    testing functionality of ghost_branch
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ghost_branch_25109()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_marked_accounts_25110():
    '''
    testing functionality of marked_accounts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_marked_accounts_25110()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_reversed_accounts_25111():
    '''
    testing functionality of reversed_accounts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_reversed_accounts_25111()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_contract_killer_25127():
    '''
    testing functionality of contract_killer
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_contract_killer_25127()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_elizabeth_mills_25128():
    '''
    testing functionality of elizabeth_mills
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_elizabeth_mills_25128()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_public_support_25129():
    '''
    testing functionality of public_support
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_public_support_25129()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_pad_campaign_25142():
    '''
    testing functionality of pad_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_pad_campaign_25142()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_calvin_b4l3y_26033():
    '''
    testing functionality of calvin_b4l3y
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_calvin_b4l3y_26033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_nanoetching_matrix_26034():
    '''
    testing functionality of nanoetching_matrix
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_nanoetching_matrix_26034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_public_health_portal_26042():
    '''
    testing functionality of public_health_portal
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_public_health_portal_26042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_storgotic_resonator_26043():
    '''
    testing functionality of storgotic_resonator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_storgotic_resonator_26043()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_daily_quest_26048():
    '''
    testing functionality of daily_quest
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_daily_quest_26048()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_tiered_subscription_26049():
    '''
    testing functionality of tiered_subscription
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_tiered_subscription_26049()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_roughneck_repair_squad_26057():
    '''
    testing functionality of roughneck_repair_squad
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_roughneck_repair_squad_26057()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_csr_campaign_26064():
    '''
    testing functionality of csr_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_csr_campaign_26064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_bass_ch1r180g4_26098():
    '''
    testing functionality of bass_ch1r180g4
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_bass_ch1r180g4_26098()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_cerebral_overwriter_26099():
    '''
    testing functionality of cerebral_overwriter
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_cerebral_overwriter_26099()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_vaporframe_fabricator_26100():
    '''
    testing functionality of vaporframe_fabricator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_vaporframe_fabricator_26100()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_prana_condenser_26107():
    '''
    testing functionality of prana_condenser
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_prana_condenser_26107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_wall_to_wall_26122():
    '''
    testing functionality of wall_to_wall
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_wall_to_wall_26122()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_hostile_infrastructure_29011():
    '''
    testing functionality of hostile_infrastructure
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_hostile_infrastructure_29011()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_turtlebacks_29012():
    '''
    testing functionality of turtlebacks
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_turtlebacks_29012()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_executive_boot_camp_29015():
    '''
    testing functionality of executive_boot_camp
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_executive_boot_camp_29015()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_nico_campaign_30037():
    '''
    testing functionality of nico_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_nico_campaign_30037()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_urtica_cipher_30045():
    '''
    testing functionality of urtica_cipher
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_urtica_cipher_30045()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_spin_doctor_30053():
    '''
    testing functionality of spin_doctor
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_spin_doctor_30053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_clearinghouse_30061():
    '''
    testing functionality of clearinghouse
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_clearinghouse_30061()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_regolith_mining_license_30071():
    '''
    testing functionality of regolith_mining_license
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_regolith_mining_license_30071()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_marilyn_campaign_31042():
    '''
    testing functionality of marilyn_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_marilyn_campaign_31042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ronin_31053():
    '''
    testing functionality of ronin
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ronin_31053()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_snare_31054():
    '''
    testing functionality of snare
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_snare_31054()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_daily_business_show_31063():
    '''
    testing functionality of daily_business_show
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_daily_business_show_31063()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_reversed_accounts_31064():
    '''
    testing functionality of reversed_accounts
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_reversed_accounts_31064()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_corporate_town_31074():
    '''
    testing functionality of corporate_town
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_corporate_town_31074()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_pad_campaign_31080():
    '''
    testing functionality of pad_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_pad_campaign_31080()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_refuge_campaign_33033():
    '''
    testing functionality of refuge_campaign
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_refuge_campaign_33033()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_trieste_model_bioroids_33034():
    '''
    testing functionality of trieste_model_bioroids
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_trieste_model_bioroids_33034()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_bladderwort_33041():
    '''
    testing functionality of bladderwort
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_bladderwort_33041()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_moon_pool_33042():
    '''
    testing functionality of moon_pool
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_moon_pool_33042()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_chekist_scion_33050():
    '''
    testing functionality of chekist_scion
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_chekist_scion_33050()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_drago_ivanov_33051():
    '''
    testing functionality of drago_ivanov
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_drago_ivanov_33051()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_ubiquitous_vig_33052():
    '''
    testing functionality of ubiquitous_vig
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_ubiquitous_vig_33052()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_svyatogor_excavator_33059():
    '''
    testing functionality of svyatogor_excavator
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_svyatogor_excavator_33059()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_nightmare_archive_33097():
    '''
    testing functionality of nightmare_archive
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_nightmare_archive_33097()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_dr_vientiane_keeling_33106():
    '''
    testing functionality of dr_vientiane_keeling
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_dr_vientiane_keeling_33106()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_reaper_function_33107():
    '''
    testing functionality of reaper_function
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_reaper_function_33107()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_gaslight_33114():
    '''
    testing functionality of gaslight
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_gaslight_33114()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_vera_ivanovna_shuyskaya_33115():
    '''
    testing functionality of vera_ivanovna_shuyskaya
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_vera_ivanovna_shuyskaya_33115()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_hostile_architecture_33122():
    '''
    testing functionality of hostile_architecture
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_hostile_architecture_33122()
    test_card.play(test_game_environment.runner,test_game_environment)

######################
def test_asset_superdeep_borehole_33123():
    '''
    testing functionality of superdeep_borehole
    '''
    #create test game state for the proper type
    test_game_environment = initialize_test_environment("asset")

    test_card = asset_superdeep_borehole_33123()
    test_card.play(test_game_environment.runner,test_game_environment)
