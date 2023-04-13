
from netrunner_lib.deck import Deck
from netrunner_lib.cards._base_card_classes import *
from netrunner_lib.game_events import generic_player_prompt

class Player:
    def __init__(self,name, deck_path, deck_type):
        self.name = name
        self.deck = Deck(deck_path, deck_type)
        self.faction = self.deck.identity_card.faction_code
        self.hand = []
        self.discard = []
        self.credit_pool = 0 #measures money
        self.clicks = 0 #measures time
        self.scored_agendas:list[Card] = []
        return

    def setup(self, starting_credits=0):
        self.deck.shuffle()
        self.credit_pool = starting_credits
        self.hand = self.deck.cards[:5]
        for card in self.hand:
            card.state['location'] = 'hand'
        self.deck.cards = self.deck.cards[5:]
        for card in self.deck.cards:
            card.state['location'] = 'deck'

    def setup_mulligan(self):
        self.deck.cards = self.deck.cards+self.hand
        self.setup(self.credit_pool)
    
    def draw_card(self):
        self.hand.append(self.deck.cards.pop())
        self.hand[-1].state['location'] = "hand"

    def do_turn_actions(self, state:str):
        print(f'[PLAYER]>{self.name} player doing a turn action[{state}]-Click @ start of turn={self.clicks}')
    
    def get_deck(self):
        return self.deck

    def get_hand(self):
        return self.hand
    
    def get_discard(self):
        return self.discard

    def print_player_details(self) -> None:
        '''
        print player details
        '''
        print(f"""--------------------------------------------
Player:: Name[{self.name}]-Faction[{self.faction}]
Identity:: {self.deck.identity_card}
Hand:: {[str(x) for x in self.hand]}
DeckSize[{self.deck.length()}]-HandSize[{len(self.hand)}]-DiscardSize[{len(self.discard)}]
Credits[{self.credit_pool}]-Clicks[{self.clicks}]
ScoredAgendas[{self.scored_agendas}]
--------------------------------------------""")

    def print_hand(self) -> None:
        print([str(x) for x in self.hand])

    def prompt(self,msg:str) -> str:
        '''
        present prompt to this player, return input
        '''
        return input(msg)

class Server():
    def __init__(self, name:str, root_card:Card=None):
        self.name = name
        self.root = root_card
        self.upgrades = []
        self.ice = []
    
    def install_ice(self,ice_card:Card) -> str:
        ice_card.state['installed'] = True
        ice_card.state['rezzed'] = False
        ice_card.state['location'] = self.name
        self.ice.append(ice_card)
        return "installed"
    
    def install_upgrade(self,upgrade_card:Card) -> str:
        upgrade_card.state['installed'] = True
        upgrade_card.state['rezzed'] = False
        upgrade_card.state['location'] = self.name
        self.upgrades.append(upgrade_card)
        return "installed"

class Corpo(Player):
    '''
    playing field consists of credit pool, ice array, central servers[archives, R&D, HQ], and remote servers
    HQ = hand (idx=0)
    R&D = deck (idx=1)
    archives = discard (idx=2)
    remote servers can be agendas or assets (idx=2+n)
    '''
    def __init__(self,name, deck_path):
        super().__init__(name, deck_path, "corpo")
        self.hq_server:Server = Server("HQ")
        self.rnd_server:Server = Server("R&D")
        self.archive_server:Server = Server("Archives")
        self.remote_servers:list[Server] = []
        self.bad_publicity_score:int = 0
    
    def install_new_remote_server(self,card:Card) -> str:
        '''
        create a new remote server with the provided card as its root
        card should be agenda or asset
        '''
        self.remote_servers.append(Server(card.game_id, card))
        self.remote_servers[-1].root.state['state'] = "installed"
        self.remote_servers[-1].root.state['location'] = card.game_id
        return "installed"

    def install_ice(self, server_id:int, card:Card) -> str:
        '''
        install an ice card to the appropriate server based on the provided index
        return status code
        '''
        if server_id==0:
            return self.hq_server.install_ice(card)
        elif server_id==1:
            return self.rnd_server.install_ice(card)
        elif server_id==2:
            return self.archive_server.install_ice(card)
        else:
            return self.remote_servers[server_id-3].install_ice(card)
    
    def install_upgrade(self, server_id:int, card:Card) -> str:
        '''
        install an upgrade card to the appropriate server based on the provided index
        return status code
        '''
        if server_id==0:
            return self.hq_server.install_upgrade(card)
        elif server_id==1:
            return self.rnd_server.install_upgrade(card)
        elif server_id==2:
            return self.archive_server.install_upgrade(card)
        else:
            return self.remote_servers[server_id-3].install_upgrade(card)

    def get_server_by_id(self, server_id:int) -> Server:
        '''
        return the server referenced by the provided ID
        NOT TO BE USED for setting info, just getting
        '''
        if server_id==0:
            return self.hq_server
        elif server_id==1:
            return self.rnd_server
        elif server_id==2:
            return self.archive_server
        else:
            return self.remote_servers[server_id-3]

    def do_turn_actions(self,turn_state:str="start", **kwargs):
        '''
        do a turn action, the default turn_state is the first state of the players turn
        return the next state of action to perform
        ordering:
            - "start"
            - "action"
            - "discard"
            - "end_turn"
        kwargs:
            - source:str the source of the action (i.e. 'hand', or 'HQ' or whatever)
            - turn_action:str what state is the turn in
            - hand_index:int index of the card in the hand to use
            - game_manager:NetrunnerGame reference to game manager object
            - server:str which server the turn is doing actions on
        '''
        super().do_turn_actions(turn_state)
        if turn_state == "start":
            self.clicks = 3
            self.draw_card()
            #resolve "when your turn begins abilities"
            return "action"
        elif turn_state == "action":
            if self.clicks != 0:
                #take some actions
                if kwargs['turn_action'] == "gain_credit":
                    self.credit_pool += 1
                    self.clicks -= 1
                elif kwargs['turn_action'] == "draw_card":
                    self.draw_card()
                    self.clicks -= 1
                elif kwargs['turn_action'] == "play_card":#playing a card
                    if kwargs['source'] == "hand":
                        result = self.hand[kwargs['hand_index']].play(self,kwargs)
                        print(f'corpo turn_action play_card]:: play result={result}')
                    else:
                        print('unhandled kwargs[location] option')
                    self.clicks -= 1
                if self.clicks == 0:#advance to next step
                    return "discard"
                else:
                    return "action" 
            else:
                return "discard"#extra check to move to discard step in case click tracking messed up
        elif turn_state == "discard":
            if len(self.hand)>5:
                if not 'hand_index' in kwargs.keys():
                    hand_string_query = [f"{idx}) {card}" for idx, card in enumerate(self.hand)]
                    discard_index = generic_player_prompt(self,f"Select card to discard: {' '.join(hand_string_query)}")
                else:
                    discard_index = kwargs['hand_index']
                result = self.hand[discard_index].trash(self)
                if len(self.hand)>5:
                    return "discard"
            else:
                print('hand at acceptable size')
                return "end_turn"

    def print_play_area_details(self) -> None:
        '''
        print corpo play area details
        '''
        print(f'''--------------------------------------------
{self.hq_server.name}({len(self.hand)}):: {self.hq_server.root}
- Upgrades({len(self.hq_server.upgrades)}):: {[str(x) for x in self.hq_server.upgrades]}
- Ice({len(self.hq_server.ice)}):: {[str(x) for x in self.hq_server.ice]}
{self.rnd_server.name}({self.deck.length()}):: {self.rnd_server.root}
- Upgrades({len(self.rnd_server.upgrades)}):: {[str(x) for x in self.rnd_server.upgrades]}
- Ice({len(self.rnd_server.ice)}):: {[str(x) for x in self.rnd_server.ice]}
{self.archive_server.name}({len(self.discard)}):: {self.archive_server.root}
- Upgrades({len(self.archive_server.upgrades)}):: {[str(x) for x in self.archive_server.upgrades]}
- Ice({len(self.archive_server.ice)}):: {[str(x) for x in self.archive_server.ice]}''')
        for idx, remote_server in enumerate(self.remote_servers):
            print(f"""Remote-{remote_server.name}[{idx}]:: {remote_server.root}
- Upgrades({len(remote_server.upgrades)}):: {[str(x) for x in remote_server.upgrades]}
- Ice({len(remote_server.ice)}):: {[str(x) for x in remote_server.ice]}
--------------------------------------------""")

class Runner(Player):
    '''
    playing field consists of credit pool, heap, stack, identity card, programs, hardware, resources
    Stack = deck
    Grip = hand
    Heap = discard
    Putting a card into the play area is referred to as INSTALLING it. Putting a card into your discard pile is typically referred to as TRASHING it.
    '''
    def __init__(self,name, deck_path):
        super().__init__(name, deck_path, "runner")
        self.programs = []
        self.hardware = []
        self.resources = []
        self.tags = []
        self.memory_units = 4
        self.brain_damage = 0
        self.max_hand_size = 5 #shouldn't be modified
    
    def do_turn_actions(self,turn_state="start", **kwargs):
        '''
        do a turn action, the default turn_state is the first state of the players turn
        return the next state of action to perform
        ordering:
            - "start"
            - "action"
            - "discard"
            - "end_turn"
        kwargs:
            - source:str the source of the action (i.e. 'hand', or 'HQ' or whatever)
            - turn_action: what state is the turn in
            - hand_index: index of the card in the hand to use
            - game_manager:NetrunnerGame reference to game manager object
        '''
        super().do_turn_actions(turn_state)
        if turn_state == "start":
            self.clicks = 4
            #resolve "when your turn begins abilities"
            return "action"
        elif turn_state == "action":
            if self.clicks != 0:
                #take some actions
                if kwargs['turn_action'] == "gain_credit":
                    self.credit_pool += 1
                    self.clicks -= 1
                elif kwargs['turn_action'] == "draw_card":
                    self.draw_card()
                    self.clicks -= 1
                elif kwargs['turn_action'] == "play_card":
                    if kwargs['source'] == "hand":
                        result = self.hand[kwargs['hand_index']].play(self,kwargs)
                        print(f'runner turn_action play_card]:: play result={result}')
                    else:
                        print('unhandled kwargs[location] option ')
                    self.clicks -= 1
                elif kwargs['turn_action'] == "run_server":
                    print('running server')
                    self.clicks -= 1
                if self.clicks == 0:#advance to next step
                    return "discard"
                else:
                    return "action"
            else:
                return "discard"#extra check to move to discard step in case click tracking messed up
        elif turn_state == "discard":
            if len(self.hand)>(self.max_hand_size-self.brain_damage):
                self.hand.remove(self.hand[kwargs['hand_index']])
                if len(self.hand)>5:
                    return "discard"
            else:
                print('hand at acceptable size')
                return "end_turn"

    def install_program(self,program_card:Card) -> str:
        '''
        install a program to the runners program slots
        return status code
        '''
        program_card.state['installed'] = True
        program_card.state['location'] = "programs"
        self.programs.append(program_card)
        return "installed"
    
    def install_hardware(self,hardware_card:Card) -> str:
        '''
        install a hardware to the runners program slots
        return status code
        '''
        hardware_card.state['installed'] = True
        hardware_card.state['location'] = "hardware"
        self.programs.append(hardware_card)
        return "installed"

    def print_play_area_details(self) -> None:
        '''
        print runner play area details
        '''
        print(f'''--------------------------------------------
Programs({len(self.programs)}):: {[str(card) for card in self.programs]}
Hardware({len(self.hardware)}):: {[str(card) for card in self.hardware]}
Resources({len(self.resources)}):: {[str(card) for card in self.resources]}
--------------------------------------------''')

class AI_Corpo(Corpo):
    '''
    generic AI class for corpos
    playing field consists of credit pool, ice array, central servers[archives, R&D, HQ], and remote servers
    R&D = deck
    HQ = hand
    archives = discard
    '''
    def __init__(self,name, deck_path):
        super().__init__(name, deck_path, "corpo")

class AI_Runner(Runner):
    '''
    generic AI class for runners
    playing field consists of credit pool, heap, stack, identity card, programs, hardware, resources
    '''
    def __init__(self,name, deck_path):
        super().__init__(name, deck_path, "runner")
