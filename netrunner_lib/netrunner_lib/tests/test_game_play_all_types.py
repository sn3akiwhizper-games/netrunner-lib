'''
tests performed: (update with cat test_game_play_all_types.py | grep ^\#-)
this file tests all types of cards except upgrades, b/c starter deck don't have them, check out test_game_play_all_types2.py for test of upgrade cards
#- 

'''
from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.cards.hardware import *
from netrunner_lib.players import *
from netrunner_lib.game_state import *

random.seed(42)
TEST_NAME="TGame2-all-types"

def dprint(msg):
    print(f"[{TEST_NAME}]>> {msg}")

#- create runner and corpo players
print('-'*20)
print('-'*20)
print('-'*20, 'starting new game, test_game_play_all_types')
print('-'*20)
print('-'*20)
dprint('> creating players')
runner_player = Runner('testrunner1','starter-deck-runner-beginner.o8d')
corpo_player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
players = [runner_player, corpo_player]#helper var for quicker tests

dprint('-'*20)
dprint('creating game')
game = NetrunnerGame(corpo_player, runner_player)
game.win_condition = {
    "corpo":{
        "agenda_points":6
    },
    "runner":{
        "agenda_points":6
    }
}

dprint('-'*20)
dprint('setting up the game')
game.setup(starting_credits=5)
game.print_state()

##############################################
##############################################
##############################################
##############################################
#first turn, corpo's turn
print('-'*20)
dprint('start corpo first turn')
#- test game manager start next turn, validate turn number and current player
game.start_turn()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#- test corpo start turn action
dprint('>>corpo doing start turn action')
state = corpo_player.do_turn_actions("start")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to gain a credit')
#- test corpo gain credit turn action
state = corpo_player.do_turn_actions(state,turn_action="gain_credit")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to install Shadow ice on HQ')
#- test corpo play card action playing Enigma ice in front of HQ
state = corpo_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=1, game_manager=game, server=0)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to play Anonymous Tip operation')
#- test corpo play card action playing Wall of Static ice in front of R&D
state = corpo_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=1, game_manager=game)

#end the second turn
game.end_turn()

##############################################
##############################################
##############################################
##############################################

#second turn, netrunners turn
print('-'*20)
dprint('>>starting first netrunner turn')
game.start_turn()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#- test runner does start turn action
dprint('>>runner doing start turn action')
state = runner_player.do_turn_actions("start")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>runner wants to gain a credit')
#- test runner gain credit turn action
state = runner_player.do_turn_actions(state,turn_action="gain_credit")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>netrunner wants to draw a card')
#- test runner draw card turn action
state = runner_player.do_turn_actions(state,turn_action="draw_card")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint(">>runner wants to play Easy Mark event")
#- test runner play card turn action playing Easy Mark event
state = runner_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=0,game_manager=game)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>netrunner wants to install Ninja Program')
#- test runner play card turn action playing Ninja program
state = runner_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=4,game_manager=game, credits_spent=3)

#end the first turn
#- test game manager end turn
game.end_turn()

##############################################
##############################################
##############################################
##############################################
##############################################
print('-#'*20)
print('-#'*20)
dprint('--end first round--')
game.print_state()
print('-#'*20)
print('-#'*20)
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# [TGame2-all-types]>> --end first round--
# ###################################################
# CURRENT GAME STATE:: Turn[3] testcorpo1's turn
# --------------------------------------------
# Player:: Name[testcorpo1]-Faction[weyland-consortium]
# Identity:: Weyland Consortium: Building a Better World(identity)[01093_2045]
# Hand:: ['Priority Requisition(agenda)[01106_7573]', 'Posted Bounty(agenda)[01095_1654]', 'PAD Campaign(asset)[01109_0525]', 'Wall of Static(ice)[01113_8179]', 'Wall of Static(ice)[01113_7517]', 'Beanstalk Royalties(operation)[01098_7428]', 'Private Security Force(agenda)[01107_9125]']
# DeckSize[40]-HandSize[7]-DiscardSize[1]
# Credits[6]-Clicks[0]
# ScoredAgendas[[]]
# --------------------------------------------
# --------------------------------------------
# HQ(40):: None
# Upgrades(0):: []
# Ice(1):: ['Shadow(ice)[01104_2677]']
# --------------------------------------------
# --------------------------------------------
# Player:: Name[testrunner1]-Faction[shaper]
# Identity:: Kate "Mac" McCaffrey: Digital Tinker(identity)[01033_1824]
# Hand:: ['Easy Mark(event)[01019_8935]', 'Armitage Codebusting(resource)[01053_8785]', 'Diesel(event)[01034_0488]', 'The Personal Touch(hardware)[01040_0106]']
# DeckSize[39]-HandSize[4]-DiscardSize[1]
# Credits[6]-Clicks[0]
# ScoredAgendas[[]]
# --------------------------------------------
# --------------------------------------------
# Programs(1):: ['Ninja(program)[01027_6912]']
# Hardware(0):: []
# Resources(0):: []
# --------------------------------------------
# ###################################################
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
##############################################
##############################################
##############################################
##############################################
##############################################

#third turn, corpo's turn
print('-'*20)
dprint('start corpo second turn')
game.start_turn()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#- test corpo start turn action
dprint('>>corpo doing start turn action')
state = corpo_player.do_turn_actions("start")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to play Posted Bounty(agenda)[01095]')
#- test corpo play agenda card
state = corpo_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=1, game_manager=game)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to play PAD Campaign(asset)[01109_0525]')
#- test corpo play asset card
state = corpo_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=1, game_manager=game)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to play Wall of Static(ice)[01113_8179]')
#- test corpo play ice card
state = corpo_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=1, game_manager=game, server=3)

#end the second turn
game.end_turn()

##############################################
##############################################
##############################################
##############################################

#fourth turn, netrunners turn
print('-'*20)
dprint('>>starting second netrunner turn')
game.start_turn()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#- test runner does start turn action
dprint('>>runner doing start turn action')
state = runner_player.do_turn_actions("start")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>netrunner wants to install Armitage Codebusting(resource)[01053_8785]')
#- test runner play card armitage codebusting resource
state = runner_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=1,game_manager=game)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>netrunner wants to install The Personal Touch(hardware)[01040_0106]')
#- test runner play card personal touch hardware
state = runner_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=2,game_manager=game)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>netrunner wants to draw a card')
#- test runner draw card turn action
state = runner_player.do_turn_actions(state,turn_action="draw_card")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>netrunner wants to draw a card')
#- test runner draw card turn action
state = runner_player.do_turn_actions(state,turn_action="draw_card")

#end the turn
game.end_turn()

##############################################
##############################################
##############################################
##############################################
##############################################

#first turn, corpo's turn
print('-'*20)
dprint('start corpo first turn')
#- test game manager start next turn, validate turn number and current player
game.start_turn()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#- test corpo start turn action
dprint('>>corpo doing start turn action')
state = corpo_player.do_turn_actions("start")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo cheating for test and picking upgrade from deck')
#- test corpo draw a card
for card in corpo_player.deck.cards:
    if card.type_code == "upgrade":
        print('found upgrade card ',card.title)
        corpo_player.hand.append(card)

# state = corpo_player.do_turn_actions(state,turn_action="draw_card")

#end the second turn
# game.end_turn()

game.print_state()

##############################################
##############################################
##############################################
##############################################
##############################################
# RUNNER DECK
#   <section name="Identity">
#     <card qty="1" id="bc0f047c-01b1-427f-a439-d451eda01033">Kate &quot;Mac&quot; McCaffrey: Digital Tinker</card>
#   </section>
#   <section name="R&amp;D / Stack">
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01005">Cyberfeeder</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01007">Corroder</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01019">Easy Mark</card>
#     <card qty="1" id="bc0f047c-01b1-427f-a439-d451eda01026">Femme Fatale</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01027">Ninja</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01034">Diesel</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01035">Modded</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01036">The Maker&#039;s Eye</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01037">Tinkering</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01038">Akamatsu Mem Chip</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01039">Rabbit Hole</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01040">The Personal Touch</card>
#     <card qty="1" id="bc0f047c-01b1-427f-a439-d451eda01041">The Toolbox</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01043">Gordian Blade</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01044">Magnum Opus</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01048">Sacrificial Construct</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01049">Infiltration</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01050">Sure Gamble</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01051">Crypsis</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01053">Armitage Codebusting</card>
#   </section>
# ##############################################
# CORPO DECK
#   <section name="Identity">
#     <card qty="1" id="bc0f047c-01b1-427f-a439-d451eda01093">Weyland Consortium: Building a Better World</card>
#   </section>
#   <section name="R&amp;D / Stack">
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01056">Adonis Campaign</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01064">Rototurret</card>
#     <card qty="1" id="bc0f047c-01b1-427f-a439-d451eda01083">Anonymous Tip</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01090">Tollbooth</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01094">Hostile Takeover</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01095">Posted Bounty</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01098">Beanstalk Royalties</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01100">Shipment from Kaguya</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01101">Archer</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01102">Hadrian&#039;s Wall</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01103">Ice Wall</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01104">Shadow</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01106">Priority Requisition</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01107">Private Security Force</card>
#     <card qty="2" id="bc0f047c-01b1-427f-a439-d451eda01108">Melange Mining Corp.</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01109">PAD Campaign</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01110">Hedge Fund</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01111">Enigma</card>
#     <card qty="3" id="bc0f047c-01b1-427f-a439-d451eda01113">Wall of Static</card>
#   </section>
