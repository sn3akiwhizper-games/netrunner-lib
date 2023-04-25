'''
tests performed: (update with cat test_game_play_all_types.py | grep ^\#-)
this file tests a full game using beginner decks
#- 

'''
import unittest

from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.cards.hardware import *
from netrunner_lib.players import *
from netrunner_lib.game_state import *
from netrunner_lib.tests._test_utilities import *

def dprint(msg):
    print(f"[{TEST_NAME}]>> {msg}")

def do_player_turns(player_obj,turn_dict):
    game.start_turn()
    state = "start"
    for turn in turn_dict:
        state = player_obj.do_turn_actions(turn_state=state,**turn)
    game.end_turn()

random.seed(42)
TEST_NAME="TGame2-all-types"

dprint('> creating players')
print('-'*20)
print('-'*20)
print('-'*20, 'starting new game, test_beginner_game1')
print('-'*20)
print('-'*20)
runner_player = Runner('testrunner1','starter-deck-runner-beginner.o8d')
corpo_player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
players = [runner_player, corpo_player]#helper var for quicker tests

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

corpo_turn1_acts = [
    {"turn_action":"start"},#corpo doing start turn action
    {"turn_action":"gain_credit"},#corpo doing start turn action
    {"turn_action":"play_card","source":"hand","hand_index":1,"game_manager":game,"server":0},#corpo wants to install Shadow ice on HQ
    {"turn_action":"play_card","source":"hand","hand_index":1,"game_manager":game},#corpo wants to play Anonymous Tip operation
]

do_player_turns(corpo_player,corpo_turn1_acts)

##############################################
##############################################
##############################################
##############################################

#second turn, netrunners turn
print('-'*20)
dprint('>>starting first netrunner turn')

runner_turn1_acts = [
    {"turn_action":"start"},#runner doing start turn action
    {"turn_action":"gain_credit"},#runner wants to gain a credit
    {"turn_action":"draw_card"},#netrunner wants to draw a card
    {"turn_action":"play_card","source":"hand","hand_index":0,"game_manager":game},#runner wants to play Easy Mark event
    {"turn_action":""},#netrunner wants to install Ninja Program
    {"turn_action":""},
]

do_player_turns(runner_player,runner_turn1_acts)

############################################################################################
############################################################################################
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
############################################################################################
############################################################################################

print('-'*20)
dprint('start corpo turn')

corpo_turn1_acts = [
    {"turn_action":"start"},#corpo doing start turn action
]

do_player_turns(corpo_player,corpo_turn1_acts)

##############################################
##############################################
##############################################
##############################################

#second turn, netrunners turn
print('-'*20)
dprint('>>starting netrunner turn')

runner_turn1_acts = [
    {"turn_action":"start"},#runner doing start turn action
    {"turn_action":""},
]

do_player_turns(runner_player,runner_turn1_acts)

##############################################
##############################################
##############################################
##############################################
##############################################
print('-#'*20)
print('-#'*20)
dprint('--end second round--')
game.print_state()
print('-#'*20)
print('-#'*20)
##############################################
##############################################
##############################################
##############################################

turn_acts = [
    {"turn_action":""},
]
