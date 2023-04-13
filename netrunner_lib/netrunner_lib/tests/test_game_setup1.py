'''
tests performed: (update with cat test_game_setup1.py | grep ^#-)
#- create runner and corpo players
#- check players are of proper class
#- check initial credit pools
#- create game manager instance with existing players
#- check initial turn #
#- check players set properly in game manager
#- test initial game manager setup
#- test starting credit pool from setup
#- test size of starting hand
#- test runner taks a mulligan and redraws hand
#- test old hand is not the same as the new hand
#- test drawing cards
#- create runner and corpo players
#- check players are of proper class
#- check initial credit pools
#- create game manager instance with existing players
#- check initial turn #
#- check players set properly in game manager
#- test initial game manager setup
#- test starting credit pool from setup
#- test size of starting hand
#- test runner taks a mulligan and redraws hand
#- test old hand is not the same as the new hand
#- test drawing cards
#- create runner and corpo players
#- check players are of proper class
#- check initial credit pools
#- create game manager instance with existing players
#- check initial turn #
#- check players set properly in game manager
#- test initial game manager setup
#- test starting credit pool from setup
#- test size of starting hand
#- test runner taks a mulligan and redraws hand
#- test old hand is not the same as the new hand
#- test drawing cards
'''
from netrunner_lib.cards import *
from netrunner_lib.players import *
from netrunner_lib.game_state import *
import random

random.seed(42)

#- create runner and corpo players
print('-'*20)
print('creating players')
runner_player = Runner('testrunner1','starter-deck-runner-beginner.o8d')
corpo_player = Corpo('testcorpo1','starter-deck-corp-beginner-weyland-.o8d')
players = [runner_player, corpo_player]#helper var for quicker tests

#- check players are of proper class
assert isinstance(runner_player,Runner)
assert isinstance(corpo_player,Corpo)

print(corpo_player.deck.identity_card)
print(f'corpo deck has {len(corpo_player.deck.cards)} cards')
print(runner_player.deck.identity_card)
print(f'runner deck has {len(runner_player.deck.cards)} cards')

#- check initial credit pools
for player in players:
    assert player.credit_pool == 0

#- create game manager instance with existing players
print('-'*20)
print('creating game')
game = NetrunnerGame(corpo_player, runner_player)
#- check initial turn #
#- check players set properly in game manager
assert game.turn == 1
assert game.corpo == corpo_player
assert game.runner == runner_player

#- test initial game manager setup
print('-'*20)
print('setting up the game')
game.setup(starting_credits=5)

#- test starting credit pool from setup
for player in players:
    assert player.credit_pool == 5

#- test size of starting hand
for player in players:
    assert len(player.hand) == 5
    print([str(x) for x in player.hand])

#- test runner taks a mulligan and redraws hand
print('runner wants a mulligan')
old_hand = runner_player.hand
runner_player.setup_mulligan()
print(f'old hand: {[str(x) for x in old_hand]}')
print(f'new hand: {[str(x) for x in runner_player.hand]}')

#- test old hand is not the same as the new hand
assert old_hand != runner_player.hand

#- test drawing cards
for player in players:
    deck_length = len(player.deck.cards)
    player.draw_card()
    assert len(player.hand) == 6
    assert len(player.deck.cards) == deck_length-1
    print([str(x) for x in player.hand])
