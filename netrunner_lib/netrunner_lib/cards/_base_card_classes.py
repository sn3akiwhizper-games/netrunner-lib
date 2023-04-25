import json
import random
from enum import Enum

from netrunner_lib.game_events import *
from netrunner_lib import errors
from netrunner_lib.variables import debug_print

# class CardLocation(Enum):
#     '''
#     Enum listing all possible locations a card can be located in
#     '''
#     DECK=0
#     HAND=1
#     PROGRAMS=2
#     HARDWARE=3
#     RESOURCES=4
#     HQ_UPGRADES=5
#     HQ_ICE=6
#     RND_UPGRADES=7
#     RND_ICE=8
#     ARCHIVE_UPGRADES=9
#     ARCHIVES_ICE=10

# class CardState():
#     def __init__(self,location:CardLocation=CardLocation.DECK,rezzed:bool=False,installed:bool=False):
#         '''
#         Track the state of the card
#         INPUT:
#             - location:CardLocation
#             - rezzed:bool
#             - installed:bool
#         '''
#         self.location=location
#         self.rezzed=rezzed
#         self.installed=installed

class Card:
    """
    Base card class holding all the basic information needed
    """
    def __init__(self, card_json:str):
        """
        Create an instance of a card from it's json string representation
        """
        card_json:dict = json.loads(card_json)
        self.advancement_cost:int = int(card_json.get('advancement_cost',0))
        self.advancement_counters:int = int(card_json.get('advancement_counters',0))
        self.agenda_points:int = int(card_json.get('agenda_points',0))
        self.base_link = card_json.get('base_link',None)
        self.code:str = card_json.get('code')#required
        self.cost:int = int(card_json.get('cost',0))
        self.faction_code = card_json.get('faction_code')#required
        self.faction_cost = card_json.get('faction_cost',0)
        self.flavor = card_json.get('flavor',0)
        self.illustrator = card_json.get('illustrator',0)
        self.influence_limit = card_json.get('influence_limit',0)
        self.keywords = card_json.get('keywords',None)
        self.deck_limit = card_json.get('deck_limit')#required
        self.memory_cost = card_json.get('memory_cost',0)
        self.minimum_deck_size = card_json.get('minimum_deck_size',0)
        self.pack_code = card_json.get('pack_code')#required
        self.position = card_json.get('position')#required
        self.quantity = card_json.get('quantity')#required
        self.side_code = card_json.get('side_code')#required
        self.strength = card_json.get('strength',0)
        self.text = card_json.get('text',None)
        self.stripped_text = card_json.get('stripped_text',None)
        self.title = card_json.get('title')#required
        self.stripped_title = card_json.get('stripped_title',None)
        self.trash_cost = card_json.get('trash_cost',0)
        self.type_code = card_json.get('type_code')#required
        self.uniqueness = card_json.get('uniqueness')#required
        #custom fields
        self.image_path = card_json.get('image_path',None)
        self.state = {"location":None,"rezzed":False,"installed":False,"scored":False} #track state of card, rezzed, scored, etc.
        self.game_id = f"{self.code}_{random.randint(0,9999):04}" #custom id of this card for this game. (used to differentiate b/w multiple copies of the same card)

    def __str__(self) -> str:
        '''
        return a string representation of a card for printing
        '''
        return f"{self.title}({self.type_code})[{self.game_id}]"

    def print_details(self) -> None:
        '''
        quick print card details (title, type_code, code, cost, text, keywords, image path)
        '''
        print(f"""{self.title}({self.type_code})[{self.code}] -- cost: {self.cost}
text: {self.stripped_text}
keywords: {self.keywords}
image:{self.image_path}""")

    def play(self,player,kwargs) -> str:
        '''
        test if a player can afford this card
        input:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        debug_print(f'CARD]: testing card affordability {self.code}[cost={self.cost}] for player {player.name}[credits={player.credit_pool}]',1)
        #check if player can afford base cost
        if player.credit_pool < self.cost:
            debug_print(f'CARD]: player CAN NOT afford card',3)
            return "insufficient credits"
        else:
            debug_print('CARD]: player CAN afford card',3)
            return "nop"

    def get_card_index(self,location:list[any]) -> int:
        '''
        get the index of this card in the given location (should be an array)
        INPUT:
            - location:list array that holds cards to be searched for this card(self)
        RETURN:
            - int representing the index of the card in the provided location
        RAISES:
            - CARD_NOT_FOUND: if card doesn't exist in location
        '''
        for idx, location_card in enumerate(location):
            if location_card.game_id == self.game_id:
                return idx
        raise errors.CARD_NOT_FOUND

    def trash(self, player) -> str:
        '''
        trash this card from its current location, sending to discard pile
        returns str "trashed" on success
        INPUT:
            - player:netrunner_lib.players.Player player object who is holding the card
        RETURN:
            - str: "trashed" on success
        RAISES:
            - Exception(TRASH_ERROR) if the card location isn't handled
        '''
        if self.state['location'] == 'hand':
            hand_idx = self.get_card_index(player.hand)
            player.discard.append(player.hand.pop(hand_idx))
        elif self.state['location'] == 'programs':#runner
            program_idx = self.get_card_index(player.programs)
            player.discard.append(player.programs.pop(program_idx))
        elif self.state['location'] == 'hardware':#runner
            hardware_idx = self.get_card_index(player.hardware)
            player.discard.append(player.hardware.pop(hardware_idx))
        elif self.state['location'] == 'resources':#runner
            resource_idx = self.get_card_index(player.resources)
            player.discard.append(player.resources.pop(resource_idx))
        elif self.state['location'] == "hq_root":#corpo
            raise Exception('TODO')
        elif self.state['location'] == 'hq_upgrades':#corpo
            hq_upgrade_idx = self.get_card_index(player.hq_server.upgrades)
            player.discard.append(player.hq_server.upgrades.pop(hq_upgrade_idx))
        elif self.state['location'] == 'hq_ice':#corpo
            hq_ice_idx = self.get_card_index(player.hq_server.ice)
            player.discard.append(player.hq_server.ice.pop(hq_ice_idx))
        elif self.state['location'] == "rnd_root":#corpo
            raise Exception('TODO')
        elif self.state['location'] == 'rnd_upgrades':#corpo
            rnd_upgrade_idx = self.get_card_index(player.rnd_server.upgrades)
            player.discard.append(player.rnd_server.upgrades.pop(rnd_upgrade_idx))
        elif self.state['location'] == 'rnd_ice':#corpo
            rnd_ice_idx = self.get_card_index(player.rnd_server.upgrades)
            player.discard.append(player.rnd_server.upgrades.pop(rnd_ice_idx))
        elif self.state['location'] == "archive_root":#corpo
            raise Exception('TODO')
        elif self.state['location'] == 'archive_upgrades':#corpo
            archive_upgrade_idx = self.get_card_index(player.archive_server.upgrades)
            player.discard.append(player.archive_server.upgrades.pop(archive_upgrade_idx))
        elif self.state['location'] == 'archive_ice':#corpo
            archive_ice_idx = self.get_card_index(player.archive_server.upgrades)
            player.discard.append(player.archive_server.upgrades.pop(archive_ice_idx))
        elif self.state['location'] == "remote_root":#corpo
            #match on card game ID
            for idx, server in enumerate(player.remote_servers):
                if server.root.game_id == self.game_id:
                    _ = player.remote_servers.pop(idx)
                    return "trashed"
            raise Exception(f'TRASH_ERROR: remote_root: game_id={self.game_id}')
        elif self.state['location'] == "remote_upgrades":#corpo
            #look for card in HQ
            #look for card in RND
            #look for card in Archives
            #look for card in Remote Servers
            raise Exception('TODO')
        elif self.state['location'] == "remote_ice":#corpo
            #look for card in HQ
            #look for card in RND
            #look for card in Archives
            #look for card in Remote Servers
            raise Exception('TODO')
        else:
            raise Exception(f'TRASH_ERROR')
        return "trashed"

class Agenda(Card):
    '''
    Agendas are the main goal of the game. They count for points, and a player wins by getting 7 or more scored points. The Corporation attempts to score points by advancing agendas beyond their advancement requirement. The Runner attempts to score points by stealing those agendas through runs before the Corporation can score them. Agendas can only be installed in remote servers, and only one agenda or one asset can be installed in a single remote server at any given time. Agendas in the Corporation's score area are active. Agendas in any score area add to that player's number of scored points.[src](https://ancur.fandom.com/wiki/Agenda)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)
        self.is_scored = False
        
    def play(self, player, kwargs) -> str:
        '''
        play a card action
        input:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        # super_result = super().play(player,kwargs) #wont run super b/c we don't check cost for playing agendas
        # if super_result != "nop":
        #     return super_result
        # else:
        result = player.install_new_remote_server(self)
        if result == "installed":
            _ = player.hand.pop(kwargs['hand_index'])
        return result

    def score(self, player, game) -> bool:
        if player.credits >= self.advancement_cost:
            player.credits -= self.advancement_cost
            self.is_scored = True
            return True
        else:
            return False

class Asset(Card):
    '''
    Assets are cards the Corporation can install in remote servers. They can have a variety of uses, including tricking the Runner into thinking there's an Agenda installed in the server, providing sources of income, giving new abilities and effects, etc. Assets can only be installed in a remote server, and there can ever only be one asset or agenda in a remote server at any given time.[src](https://ancur.fandom.com/wiki/Asset)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)
        
    def play(self, player, kwargs) -> str:
        '''
        play a card action
        1. test super play action (can afford)
        2. install asset to new remote server
        3. remove card from hand if successfully installed
        4. set new state elements for card
        card is paid for when rezzed
        INPUT:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'installed': card successfully installed
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            result = player.install_new_remote_server(self)
            if result == "installed":
                player.remove_card_from_hand(kwargs['hand_index'])
                self.state['location']="remote_root"
                self.state['installed']=True
                debug_print(f'installed asset card in new remote, state={self.state}',3)
            return result

    def rez(self, player, game):
        if player.credits >= self.cost:
            player.credits -= self.cost
            self.is_rezzed = True
            return True
        else:
            return False

class Event(Card):
    '''
    Events are one-time use cards for the Runner. An event is immediately resolved and then trashed after being played. The Runner can play an event from Grip as an action during the Action Phase, spending Click.png and the play cost of the event in credits.[src](https://ancur.fandom.com/wiki/Event)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)

    def play(self, player, kwargs) -> str:
        '''
        play a card action
        input:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "nop"

    def use(self, player, game):
        raise Exception('TODELETE')
        pass

class Hardware(Card):
    '''
    Hardware is a type of card the Runner installs in his/her rig for special abilities and effects. A console is a special type of hardware that is limited to one per Runner.[src](https://ancur.fandom.com/wiki/Hardware)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)
    
    def play(self, player, kwargs) -> str:
        '''
        play a card action
        input:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        
        result = player.install_hardware(self)
        if result == "installed":
            player.credit_pool -= self.cost
            player.hand.pop(kwargs['hand_index'])
        return result

    def use_credit(self):
        if self.credit_pool > 0:
            self.credit_pool -= 1
            return True
        else:
            return False

class Ice(Card):
    '''
    The Corporation installs ice in front of his/her servers to protect them from the Runner. In order to access a server, the Runner must first deal with that ice during a run on that server. Ice is always installed in the outermost position in front of a server. Installing a piece of ice costs 1Credit.png for each other piece of ice already protecting that server. Ice has special required conditional abilities called subroutines. If the Runner does not break the subroutine(s) on a piece of ice that s/he encounters, then the effects of those subroutines resolve. There are four main subtypes of ice: Barrier, Code Gate, Sentry, and Trap.[src](https://ancur.fandom.com/wiki/Ice)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)

    def play(self, player, kwargs) -> str:
        '''
        play a card action
        input:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        
        #check if server id has been provided, otherwise prompt the player to select
        if 'server' in kwargs.keys():
            server_id = int(kwargs['server'])
        else:
            server_id = prompt_server_selection(kwargs['game_manager'])
        
        #check if server has other ice installed, if so check if player can afford increased cost
        num_installed_ice = len(player.get_server_by_id(server_id).ice)
        if num_installed_ice > 0:
            if player.credit_pool < (self.cost+num_installed_ice):
                return "insufficient credits"
        
        #if they can afford then install, otherwise reject
        result = player.install_ice(server_id,self)
        if result == "installed":
            player.credit_pool -= (self.cost+num_installed_ice)
            player.hand.pop(kwargs['hand_index'])
        return result

    def interact_with_runner(self, runner, game):
        raise Exception('TODELETE')
        pass

class Identity(Card):
    '''
    The identity card is one of the most important cards of a deck. It determines which cards you can use through the faction and influence systems, puts a minimum limit on how many cards you have to have in your deck, and provides you with a special ability that is always active throughout the game.[src](https://ancur.fandom.com/wiki/Identity)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)
        
    def set_deck(self, deck):
        raise Exception('TODELETE')
        self.deck = deck
        
    def get_deck(self):
        raise Exception('TODELETE')
        return self.deck

class Operation(Card):
    '''
    Operations are one-time cards that are played, resolved, and trashed as soon as they're played. The Corporation can play an operation from Headquarters as an action during the Action Phase, spending Click.png and the play cost of the operation in credits.[src](https://ancur.fandom.com/wiki/Operation)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)

    def play(self, player, kwargs) -> str:
        '''
        play a card action
        input:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "nop"
        
    def use(self, player, game):
        pass

class Program(Card):
    '''
    Programs are a type of card the Runner installs in his/her rig. They are often used in various ways during runs, but can have other utility as well. Unlike resources and hardware, the Runner can only have a certain number of programs installed at once. The Runner can never have programs with a combined memory cost greater than his/her total available memory units.[src](https://ancur.fandom.com/wiki/Program)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)
        
    def play(self, player, kwargs) -> str:
        '''
        play a card action
        input:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        
        if player.memory_units < self.memory_cost:
            return "insufficient memory"
        
        result = player.install_program(self)
        if result == "installed":
            player.credit_pool -= self.cost
            player.memory_units -= self.memory_cost
            player.hand.pop(kwargs['hand_index'])
        return result

    # def install(self, player):
    #     '''
    #     install the card from hand to programs array
    #     '''
    #     try:
    #         self.state['location'] = 'programs'
    #         hand_idx = self.get_card_index(player.hand)
    #         player.programs.append(player.hand.pop(hand_idx))
    #         return "installed"
    #     except Exception as e:
    #         raise Exception(f'Error installing program: {self.game_id}')

class Resource(Card):
    '''
    Resources are a type of card that the Runner can install in his/her rig. They are slightly more risky cards because they can be trashed by the Corporation when the Runner is tagged, but they tend to have powerful abilities and effects.[src](https://ancur.fandom.com/wiki/Resource)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)
        
    def play(self, player, kwargs) -> str:
        '''
        play a card action
        input:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            self.state['location'] = 'resources'
            self.state['installed'] = True
            hand_idx = self.get_card_index(player.hand)
            player.credit_pool -= self.cost
            player.resources.append(player.hand.pop(hand_idx))
            return "installed"

class Upgrade(Card):
    '''
    Upgrades are a type of Corporation card that can be installed in servers for abilities and effects. Unlike agendas and assets, there can be any number of upgrades installed in any server. Also unlike agendas and assets, upgrades can be installed in central servers as well as remote servers. Upgrades installed in a central server are installed in the root of that server.[src](https://ancur.fandom.com/wiki/Upgrade)
    '''
    def __init__(self, card_json):
        super().__init__(card_json)
        
    def play(self, player, kwargs) -> str:
        '''
        play a card action
        input:
            - player: player playing the card
            - kwargs: options provided, will usually include
                - 'game_manager': gameinstance
                - 'hand_index': index of the card being played in players hand
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        
        #check if server id has been provided, otherwise prompt the player to select
        if 'server' in kwargs.keys():
            server_id = int(kwargs['server'])
        else:
            # server_id = prompt_server_selection(kwargs['game_manager'])
            prompt_message = f"""1) HQ   2) R&D  3) Archives
{' '.join([f"{idx+3}) Remote {idx}" for x, idx in enumerate(player.remote_servers)])}
selection = input('Choose a server: (idx number)"""
            server_id = int(player.prompt(prompt_message))-1

        #if they can afford then install
        result = player.install_upgrade(server_id,self)
        if result == "installed":
            player.credit_pool -= self.cost
            player.hand.pop(kwargs['hand_index'])
        return result

    def rez(self, player, game):
        if player.credits >= self.cost:
            player.credits -= self.cost
            self.is_rezzed = True
            return True
        else:
            return False
        
    def use_credit(self): #IS THIS USED???
        if self.credit_pool > 0:
            self.credit_pool -= 1
            return True
        else:
            return False
