'''
tests performed: (update with cat test_game_state1.py | grep ^\#-)
#- 

'''
from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.cards.hardware import *
from netrunner_lib.players import *
from netrunner_lib.game_state import *

random.seed(42)
TEST_NAME="TGame1"

def dprint(msg):
    print(f"[{TEST_NAME}]>> {msg}")

def print_details(corpo_player,runner_player):
    print(corpo_player.details())
    print(runner_player.details())

#- create runner and corpo players
print('-'*20)
print('-'*20)
print('-'*20, 'starting new game, test_game_play1')
print('-'*20)
print('-'*20)
dprint('> creating players')
runner_player = Runner('testrunner1','starter-deck-runner-beginner.o8d')
corpo_player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
players = [runner_player, corpo_player]#helper var for quicker tests

dprint(corpo_player.deck.identity_card)
dprint(f'corpo deck has {len(corpo_player.deck.cards)} cards')
dprint(runner_player.deck.identity_card)
dprint(f'runner deck has {len(runner_player.deck.cards)} cards')

#- create game manager instance with existing players
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

#- setup game with 5 starting credits
dprint('-'*20)
dprint('setting up the game')
game.setup(starting_credits=5)
game.print_state()

#- check initial turn #
#- check first player set as corpo
assert game.turn == 1
assert game.current_player == corpo_player

#- test starting credit pool from setup
assert corpo_player.credit_pool == 5
assert runner_player.credit_pool == 5

##############################################
##############################################
##############################################
##############################################
#first turn, corpo's turn
print('-'*20)
dprint('start corpo first turn')
#- test game manager start next turn, validate turn number and current player
game.start_turn()
assert game.turn == 1
assert game.current_player == corpo_player

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#- test corpo start turn action
dprint('>>corpo doing start turn action')
# state = corpo_player.do_turn_actions("start")
state = game.perform_turn(corpo_player,'start')
#- test returned state, corpo clicks, size corpo hand
assert state == "action"
assert corpo_player.clicks == 3
assert len(corpo_player.hand) == 6

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to gain a credit')
#- test corpo gain credit turn action
state = game.perform_turn(corpo_player,state,turn_action="gain_credit")
# state = corpo_player.do_turn_actions(state,turn_action="gain_credit")
game.print_state()
#- test returned state, corpo clicks, corpo credits
assert state == "action"
assert corpo_player.clicks == 2
assert corpo_player.credit_pool == 6

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to install Shadow ice on HQ')
#- test corpo play card action playing Enigma ice in front of HQ
state = game.perform_turn(corpo_player,state,turn_action="play_card",source='hand',hand_index=1,server=0)
# state = corpo_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=1, game_manager=game, server=0)
game.print_state()
#- test returned state, corpo clicks, size corpo hand, number ice for HQ server
assert state == "action"
assert corpo_player.clicks == 1
assert len(corpo_player.hand) == 5
assert len(corpo_player.hq_server.ice) == 1, f'number of corpo ice in hq incorrect, got {len(corpo_player.hq_server.ice)}'

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>corpo wants to play Anonymous Tip operation')
#- test corpo play card action playing Wall of Static ice in front of R&D
state = game.perform_turn(corpo_player,state,turn_action="play_card",source='hand',hand_index=1)
# state = corpo_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=1, game_manager=game)
game.print_state()
#- test returned state, corpo clicks, size corpo hand
assert state == "discard", f'invalid game state: {state}'
assert corpo_player.clicks == 0, 'corpo clicks not decremented'
assert len(corpo_player.hand) == 7, f'len corpo hand not accurate with draw 3 discard 1: {len(corpo_player.hand)}'
assert '01083_9459' not in [x.game_id for x in corpo_player.hand]
assert len(corpo_player.discard) == 1, f'corpo discard not correct after anon tip: {len(corpo_player.discard)}'

#end the second turn
#- test game end turn 1, turn advances and current player switch to runner
game.end_turn()
assert game.turn == 2
assert game.current_player == runner_player

##############################################
##############################################
##############################################
##############################################

#second turn, netrunners turn
print('-'*20)
dprint('>>starting first netrunner turn')
#- test game manager starting first turn
game.start_turn()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#- test runner does start turn action
dprint('>>runner doing start turn action')
state = game.perform_turn(runner_player,"start")
# state = runner_player.do_turn_actions("start")
#- test returned state and number runner clicks
assert state == "action"
assert runner_player.clicks == 4

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>runner wants to gain a credit')
#- test runner gain credit turn action
state = game.perform_turn(runner_player,state,turn_action="gain_credit")
# state = runner_player.do_turn_actions(state,turn_action="gain_credit")
#- test returned state, runner clicks, runner pool
game.print_state()
assert state == "action"
assert runner_player.clicks == 3
assert runner_player.credit_pool == 6

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>netrunner wants to draw a card')
#- test runner draw card turn action
state = game.perform_turn(runner_player,state,turn_action="draw_card")
# state = runner_player.do_turn_actions(state,turn_action="draw_card")
game.print_state()
#- test returned state, runner clicks, size of runner hand
assert state == "action"
assert runner_player.clicks == 2
assert len(runner_player.hand) == 6

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint(">>runner wants to play Easy Mark event")
runner_player.hand[0].print_details()
# Easy Mark(event)[01019]
# text: Gain 3 credits.
# keywords: Job
# image:\card_images\01019.jpg
#- test runner play card turn action playing Easy Mark event
state = game.perform_turn(runner_player,state,turn_action="play_card",source='hand',hand_index=0)
# state = runner_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=0,game_manager=game)
game.print_state()
#- test returned state, runner clicks, runner hand decreased after playing card
assert state == "action", f'incorrect game state: {state}'
assert runner_player.clicks == 1, f'runner clicks did not decrement after action: clicks={runner_player.clicks}'
assert len(runner_player.hand) == 5, f'runner hand did not decrease after playing card: len={len(runner_player.hand)}'

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dprint('>>netrunner wants to install Ninja Program')
runner_player.hand[4].print_details()
# Ninja(program)[01027] -- cost: 4
# text: Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +5 strength.
# keywords: Icebreaker - Killer
# image:\card_images\01027.jpg
#- test runner play card turn action playing Ninja program
state = game.perform_turn(runner_player,state,turn_action="play_card",source='hand',hand_index=4,credits_spent=3)
# state = runner_player.do_turn_actions(state,turn_action="play_card",source='hand',hand_index=4,game_manager=game, credits_spent=3)
game.print_state()
#- test returned state, runner clicks, length runner hand decreased
assert state == "discard"
assert runner_player.clicks == 0
assert len(runner_player.hand) == 4, f'runner hand did not decrease after playing card: len={len(runner_player.hand)}'

#end the first turn
#- test game manager end turn
game.end_turn()
#- test turn number, current player advanced to corpo
assert game.turn == 3
assert game.current_player == corpo_player

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
