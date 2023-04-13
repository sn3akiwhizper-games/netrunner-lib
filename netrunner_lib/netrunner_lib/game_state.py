import random

from netrunner_lib.deck import Deck
from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.players import *

class NetrunnerGame:
    def __init__(self, corpo_player:Corpo, runner_player:Runner):
        self.runner = runner_player
        self.corpo = corpo_player
        self.turn = 1
        self.state = ""
        self.current_player = None
        self.win_condition = {
                "corpo":{
                    "agenda_points":7
                },
                "runner":{
                    "agenda_points":7
                }
            } #define the conditions needed for either side to win

    def setup(self, starting_credits:int=5):
        '''
        manage initial setup of the game
        '''
        self.runner.setup(starting_credits)
        self.corpo.setup(starting_credits)
        self.current_player = self.corpo

    def start_turn(self):
        '''
        tell the current player to start their turn
        '''
        print(f'Player {self.current_player.name} begin your turn')
        # self.current_player.do_turn_actions()

    def perform_turn(self,player:Player, state:str, **kwargs) -> str:
        '''
        does checking to ensure flow of game not violated
        if all is well, route turn actions to appropriate player
        returns current state after doing turn actions
        '''
        if self.current_player != player:
            return "illegal player"
        kwargs['game_manager'] = self
        result = player.do_turn_actions(state, **kwargs)
        return result

    def end_turn(self):
        #toggle who's turn it is and increment counter, maybe track the time it takes for each turn here
        self.current_player = self.runner if self.current_player == self.corpo else self.corpo
        self.turn += 1
        #check win condition here
        self.check_win_conditions()
    
    def check_win_conditions(self):
        '''
        check whether either player has won the game
            - either player reaches defined agenda points
            - corpo's R&D server is empty
            - runner takes more damage than # of cards in their hand
        return Tuple with [win,none] & [winning player|None]

        Example win definition:
            game.win_condition = {
                "corpo":{
                    "agenda_points":6
                },
                "runner":{
                    "agenda_points":6
                }
            }
        '''
        if self.corpo.scored_agendas == self.win_condition['corpo']['agenda_points']:
            return "win",self.corpo
        elif self.runner.scored_agendas == self.win_condition['runner']['agenda_points']:
            return "win",self.runner
        elif self.corpo.deck.length()==0:
            return "win",self.runner
        else:
            return "none",None

    def play_card(self, card:Card, player:Player):
        raise Exception('IS THIS IMPLEMENTED? MIGHT BE REDUNDANT?!?!')
        if player == self.runner:
            if card in self.runner_hand:
                self.runner_hand.remove(card)
                if isinstance(card, Hardware) or isinstance(card, Program) or isinstance(card, Resource):
                    self.runner_rig.append(card)
                else:
                    card.play(self.runner, self)
            else:
                raise ValueError("The card is not in the runner's hand.")
        elif player == self.corp:
            if card in self.corp_hand:
                self.corp_hand.remove(card)
                if isinstance(card, Asset) or isinstance(card, Upgrade):
                    self.corp_hq.append(card)
                elif isinstance(card, Agenda):
                    self.corp_rnd.append(card)
                else:
                    card.play(self.corp, self)
            else:
                raise ValueError("The card is not in the corp's hand.")
        else:
            raise ValueError("Invalid player.")

    def print_state(self):
        '''
        print out the current game state info
        '''
        print('###################################################')
        print(f"CURRENT GAME STATE:: Turn[{self.turn}] {self.current_player.name}'s turn")
        self.corpo.print_player_details()
        self.corpo.print_play_area_details()
        self.runner.print_player_details()
        self.runner.print_play_area_details()
        print('###################################################')

    def prompt_player(self,player,options):
        raise Exception('DEPRECATED')
        answer = input(f'{type(self.player)}: select an option (index)-> {options}')
        return answer

class RunManager:
    '''
    # This implementation defines a RunManager class that takes in the runner, corp, and attacked_server objects as input to the __init__ method. It then provides a initiate_run method that implements the turn sequence described in the rules for a run.

    1. Initiation Phase
    2. Approach Ice Phase
    3. Encounter Ice phase
    4. Movement Phase
    5. Success Phase
    6. Run Ends Phase

    # The initiate_run method checks whether there is ice protecting the attacked server, and if so, it proceeds to the Approach Ice Phase by calling the approach_next_ice method, which checks whether the ice the Runner is approaching is rezzed, and proceeds to the Encounter Ice Phase by calling the initiate_run method again if it is, or goes back to the Movement Phase by calling move_to_next_ice if it is not.

    # If there is no ice protecting the server, the initiate_run method proceeds directly to the Success Phase by calling the complete_run method.

    # The move_to_next_ice method checks whether there is more ice between the Runner and the server, and if so, proceeds to the Approach Ice Phase by calling approach_next_ice. Otherwise, it proceeds to the Movement Phase by calling complete_run.

    # The approach_next_ice method resolves any relevant abilities, rezzes any non-ice cards and/or the ice the Runner is approaching, and checks whether the ice is rezzed. If it is, it proceeds to the Encounter Ice Phase by calling initiate_run. If it is not, it goes back to the Movement Phase by calling move_to_next_ice.

    # The complete_run method declares the run successful, resolves any relevant abilities, and breaches the attacked server. It then returns True to indicate a successful run.
    '''
    def __init__(self, runner, corp, attacked_server):
        self.runner = runner
        self.corp = corp
        self.attacked_server = attacked_server
        raise Exception('NOT IMPLEMENT, VERY GROSS')
        
    def initiate_run(self):
        # 1.a. The Runner announces the attacked server.
        # 1.b. Any “When a run begins…” abilities resolve.
        # 1.c. Is there ice protecting the server?
        if self.corp.has_ice_on_server(self.attacked_server):
            # 2. Approach Ice Phase
            # 2.a. Any “When the Runner approaches ice…” abilities resolve.
            # 2.b. The Corp can rez non-ice cards and/or the ice the Runner is approaching.
            # 2.c. Is the ice the Runner is approaching rezzed?
            if self.corp.is_ice_rezzed_on_server(self.attacked_server):
                # 3. Encounter Ice Phase
                # 3.a. Any “When the Runner encounters ice…” abilities resolve.
                # 3.b. The Runner can use icebreakers to interact with the ice they are encountering, as well as other cards relevant to interacting with ice.
                # 3.c. The Corp resolves the unbroken subroutines.
                # 3.d. Did a subroutine end the run?
                if self.corp.is_run_ended(self.runner):
                    # 6. End Phase
                    # 6.a. The run ends unsuccessfully.
                    return False
                else:
                    # 4. Movement Phase
                    # 4.a. Any “When the Runner passes ice…” abilities resolve.
                    # 4.b. Would the Runner like to jack out?
                    # 4.c. The Corp can rez non-ice cards.
                    # 4.d. Is there more ice between the Runner and the server?
                    # 4.e. The Runner approaches the attacked server, and any “When the Runner approaches server…” abilities resolve.
                    # 4.f. Continue to (5).
                    return self.move_to_next_ice()
            else:
                # 4. Movement Phase
                # 4.a. Any “When the Runner passes ice…” abilities resolve.
                # 4.b. Would the Runner like to jack out?
                # 4.c. The Corp can rez non-ice cards.
                # 4.d. Is there more ice between the Runner and the server?
                # 4.e. The Runner approaches the attacked server, and any “When the Runner approaches server…” abilities resolve.
                # 4.f. Continue to (5).
                return self.move_to_next_ice()
        else:
            # 5. Success Phase
            # 5.a. The run is declared successful, and any “When the Runner makes a successful run…” abilities resolve.
            # 5.b. The Runner breaches the attacked server.
            # 6. End Phase
            # 6.a. The run ends successfully.
            return self.complete_run()
    
    def move_to_next_ice(self):
        # 4.d. Is there more ice between the Runner and the server?
        if self.corp.has_next_ice_on_server(self.attacked_server):
            # Return to (2), with the Runner approaching the next inward piece of ice.
            return self.approach_next_ice()
        else:
            # 4.e. The Runner approaches the attacked server, and any “When the Runner approaches server…” abilities resolve.
            # 4.f. Continue to (5).
            return self.complete_run()

    def approach_next_ice(self):
        # 2.a. Any “When the Runner approaches ice…” abilities resolve.
        # 2.b. The Corp can rez non-ice cards and/or the ice the Runner is approaching.
        self.corp.rez_cards_on_server(self.attacked_server)
        # 2.c. Is the ice the Runner is approaching rezzed?
        if self.corp.is_ice_rezzed_on_server(self.attacked_server):
            # Continue to (3).
            return self.initiate_run()
        else:
            # Jump to (4).
            return self.move_to_next_ice()

    def complete_run(self):
        # 5.a. The run is declared successful, and any “When the Runner makes a successful run…” abilities resolve.
        # 5.b. The Runner breaches the attacked server.
        self.runner.breach_server(self.corp, self.attacked_server)
        # 6. End Phase
        # 6.a. The run ends successfully.
        return True

# 1. Initiation Phase
    # 1.a. The Runner announces the attacked server.
    # 1.b. Any “When a run begins…” abilities resolve.
    # 1.c. Is there ice protecting the server?

# 2. Approach Ice Phase
    # 2.a. Any “When the Runner approaches ice…” abilities resolve.
    # 2.b. The Corp can rez non-ice cards and/or the ice the Runner is approaching.
    # 2.c. Is the ice the Runner is approaching rezzed?

# 3. Encounter Ice Phase
    # 3.a. Any “When the Runner encounters ice…” abilities resolve.
    # 3.b. The Runner can use icebreakers to interact with the ice they are encountering, as well as other cards relevant to interacting with ice.
    # 3.c. The Corp resolves the unbroken subroutines.
    # 3.d. Did a subroutine end the run?
# 6. End Phase
    # 6.a. The run ends unsuccessfully.

# 4. Movement Phase
    # 4.a. Any “When the Runner passes ice…” abilities resolve.
    # 4.b. Would the Runner like to jack out?
    # 4.c. The Corp can rez non-ice cards.
    # 4.d. Is there more ice between the Runner and the server?
    # 4.e. The Runner approaches the attacked server, and any “When the Runner approaches server…” abilities resolve.
    # 4.f. Continue to (5).

# 5. Success Phase
    # 5.a. The run is declared successful, and any “When the Runner makes a successful run…” abilities resolve.
    # 5.b. The Runner breaches the attacked server.
# 6. End Phase
    # 6.a. The run ends successfully.
