'''
tests performed: (update with cat test_game_play_all_types.py | grep ^\#-)
this testfile created to test using upgrades
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
corpo_player = Corpo('testcorpo1','starter-deck-corp-intermediate.o8d')
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
dprint('>>corpo cheating for test and picking upgrade from deck')
#- test corpo draw a card
for card in corpo_player.deck.cards:
    if card.type_code == "upgrade":
        print('found upgrade card ',card.title)
        corpo_player.hand.append(card)
        corpo_player.clicks -= 1
        corpo_player.hand[-1].state['location'] = 'hand'

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to install Akitaro Watanabe upgrade on HQ')
#- test corpo play card install Akitaro Watanabe upgrade on HQ
state = corpo_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=6, game_manager=game, server=0)

assert len(corpo_player.hq_server.upgrades) == 1, f'upgrade not installed in HQ: len hq upgrades={len(corpo_player.hq_server.upgrades)}'

game.print_state()

# #end the second turn
# game.end_turn()

##############################################
##############################################
##############################################
##############################################

# #second turn, netrunners turn
# print('-'*20)
# dprint('>>starting first netrunner turn')
# game.start_turn()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# #- test runner does start turn action
# dprint('>>runner doing start turn action')
# state = runner_player.do_turn_actions("start")

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# dprint('>>runner wants to gain a credit')
# #- test runner gain credit turn action
# state = runner_player.do_turn_actions(state,turn_action="gain_credit")

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# dprint('>>netrunner wants to draw a card')
# #- test runner draw card turn action
# state = runner_player.do_turn_actions(state,turn_action="draw_card")

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# dprint(">>runner wants to play Easy Mark event")
# #- test runner play card turn action playing Easy Mark event
# state = runner_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=0,game_manager=game)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# dprint('>>netrunner wants to install Ninja Program')
# #- test runner play card turn action playing Ninja program
# state = runner_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=4,game_manager=game, credits_spent=3)

# #end the first turn
# #- test game manager end turn
# game.end_turn()

##############################################
##############################################
##############################################
##############################################
##############################################
# print('-#'*20)
# print('-#'*20)
# dprint('--end first round--')
# game.print_state()
# print('-#'*20)
# print('-#'*20)

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
