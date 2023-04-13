import json
import random

from netrunner_lib.game_events import *

class Card:
    def __init__(self, card_json:str):
        card_json:dict = json.loads(card_json)
        self.advancement_cost:int = int(card_json.get('advancement_cost'))
        self.advancement_counters:int = int(card_json.get('advancement_counters'))
        self.agenda_points:int = int(card_json.get('agenda_points'))
        self.base_link = card_json.get('base_link')
        self.code:str = card_json.get('code')#required
        self.cost:int = int(card_json.get('cost'))
        self.faction_code = card_json.get('faction_code')#required
        self.faction_cost = card_json.get('faction_cost')
        self.flavor = card_json.get('flavor')
        self.illustrator = card_json.get('illustrator')
        self.influence_limit = card_json.get('influence_limit')
        self.keywords = card_json.get('keywords')
        self.deck_limit = card_json.get('deck_limit')#required
        self.memory_cost = card_json.get('memory_cost')
        self.minimum_deck_size = card_json.get('minimum_deck_size')
        self.pack_code = card_json.get('pack_code')#required
        self.position = card_json.get('position')#required
        self.quantity = card_json.get('quantity')#required
        self.side_code = card_json.get('side_code')#required
        self.strength = card_json.get('strength')
        self.text = card_json.get('text')
        self.stripped_text = card_json.get('stripped_text')
        self.title = card_json.get('title')#required
        self.stripped_title = card_json.get('stripped_title')
        self.trash_cost = card_json.get('trash_cost')
        self.type_code = card_json.get('type_code')#required
        self.uniqueness = card_json.get('uniqueness')#required
        #custom fields
        self.image_path = card_json.get('image_path')
        self.state = {} #track state of card, rezzed, scored, etc.
        self.game_id = f"{self.code}_{random.randint(0,9999):04}" #custom id of this card for this game. (used to differentiate b/w multiple copies of the same card)

    def __str__(self) -> str:
        return f"{self.title}({self.type_code})[{self.game_id}]"

    def print_details(self):
        print(f"""{self.title}({self.type_code})[{self.code}] -- cost: {self.cost}
text: {self.stripped_text}
keywords: {self.keywords}
image:{self.image_path}""")

    def play(self,player,kwargs) -> str:
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
        print(f'CARD]: playing card {self.code} for player {player.name}')
        #check if player can afford base cost
        if not player.credit_pool >= self.cost:
            return "insufficient credits"
        else:
            return "nop"

    def get_card_index(self,location) -> int:
        '''
        get the index of this card in the given location (should be an array)
        '''
        for idx, location_card in enumerate(location):
            if location_card.game_id == self.game_id:
                return idx
        raise Exception('Card not found in location')

    def trash(self, player) -> str:
        '''
        trash this card from its current location, sending to discard pile
        returns str "trashed" on success
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
        elif self.state['location'] == 'hq_upgrades':#corpo
            hq_upgrade_idx = self.get_card_index(player.hq_server.upgrades)
            player.discard.append(player.hq_server.upgrades.pop(hq_upgrade_idx))
        elif self.state['location'] == 'hq_ice':#corpo
            hq_ice_idx = self.get_card_index(player.hq_server.ice)
            player.discard.append(player.hq_server.ice.pop(hq_ice_idx))
        elif self.state['location'] == 'rnd_upgrades':#corpo
            rnd_upgrade_idx = self.get_card_index(player.rnd_server.upgrades)
            player.discard.append(player.rnd_server.upgrades.pop(rnd_upgrade_idx))
        elif self.state['location'] == 'rnd_ice':#corpo
            rnd_ice_idx = self.get_card_index(player.rnd_server.upgrades)
            player.discard.append(player.rnd_server.upgrades.pop(rnd_ice_idx))
        elif self.state['location'] == 'archive_upgrades':#corpo
            archive_upgrade_idx = self.get_card_index(player.archive_server.upgrades)
            player.discard.append(player.archive_server.upgrades.pop(archive_upgrade_idx))
        elif self.state['location'] == 'archive_ice':#corpo
            archive_ice_idx = self.get_card_index(player.archive_server.upgrades)
            player.discard.append(player.archive_server.upgrades.pop(archive_ice_idx))
        else:
            raise Exception(f'Error trashing card: {self.game_id}')
        return "trashed"

class Agenda(Card):
    '''
    # This implementation includes attributes for the card's name, faction, advancement cost, agenda points, and text. The play method adds the agenda to the game's list of available agendas when it is played, and the trash method removes it from the game's list when it is trashed or discarded.

    # The score method allows the player to advance the agenda and score it, earning the number of agenda points indicated by the agenda_points attribute. If the player has enough credits to pay the advancement cost, the method sets the is_scored attribute to True and returns True, otherwise it returns False.

    # Additional methods and attributes could be added as needed to represent other aspects of the Agenda card type, such as the specific abilities or interactions that different agendas have with other cards in the game. For example, some agendas might have additional costs or conditions that must be met before they can be scored, or may provide additional benefits or penalties depending on the game state.
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
    This implementation includes attributes for the card's name, faction, cost, text, and trash cost. The play method adds the asset to the player's list of installed assets when it is played, and the trash method removes it from the player's list when it is trashed or discarded.

    The rez method allows the player to pay the cost to rez the asset, making it active and triggering any abilities it may have. If the player has enough credits to pay the cost, the method sets the is_rezzed attribute to True and returns True, otherwise it returns False.
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
        # super_result = super().play(player,kwargs)
        # if super_result != "nop":
        #     return super_result
        # else:
        result = player.install_new_remote_server(self)
        if result == "installed":
            _ = player.hand.pop(kwargs['hand_index'])
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
    # This implementation includes attributes for the card's name, faction, cost, and text. The play method adds the event to the player's list of installed events when it is played, and the trash method removes it from the player's list when it is trashed or discarded.

    # The use method allows the player to use the event, triggering any abilities it may have. This method could be overridden by subclasses to implement different types of events, such as gaining credits, drawing cards, or affecting the game state in some other way.
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
    # This implementation includes attributes for the card's name, faction, cost, text, and recurring credits. The play method adds the hardware to the player's list of installed hardware when it is played, and the trash method removes it from the player's list when it is trashed or discarded.

    # The use_credit method allows the player to use one of the recurring credits provided by the hardware, decrementing the credit pool if there are credits available. Additional methods and attributes could be added as needed to represent other aspects of the Hardware card type, such as specific abilities or interactions that different hardware have with other cards in the game.
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
    This implementation includes attributes for the card's name, faction, cost, text, strength, and subtype. The play method adds the ICE card to the game's list of installed ICE when it is played, and the trash method removes it from the game's list when it is trashed or discarded.

    The interact_with_runner method takes an instance of the Runner class as an input and interacts with the runner according to the specific abilities of the ICE card. This method could be overridden by subclasses to implement different types of interactions, such as dealing damage to the runner, ending their run, or forcing them to discard cards.
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
    # This implementation includes attributes for the card's name, faction, and text, as well as a deck attribute to store the player's deck associated with this identity.

    # The set_deck method sets the player's deck associated with this identity, while the get_deck method returns the deck associated with this identity.
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
    # This implementation includes attributes for the card's name, faction, cost, and text. The play method adds the operation to the player's list of installed operations when it is played, and the trash method removes it from the player's list when it is trashed or discarded.

    # The use method allows the player to use the operation, triggering any abilities it may have. This method could be overridden by subclasses to implement different types of operations, such as gaining credits, drawing cards, or affecting the game state in some other way.
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
    # This implementation includes attributes for the card's name, faction, cost, text, strength, and memory. The play method adds the program to the player's list of installed programs when it is played, and the trash method removes it from the player's list when it is trashed or discarded.
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
    # This implementation includes attributes for the card's name, faction, cost, and text. The play method adds the resource to the player's list of installed resources when it is played, and the trash method removes it from the player's list when it is trashed or discarded.

    # Additional methods and attributes could be added as needed to represent other aspects of the Resources card type, such as the specific abilities or interactions that different resources have with other cards in the game. For example, a resource card might provide the player with additional credits, allow the player to draw extra cards, or have a recurring ability that triggers on certain conditions.
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
    # This implementation includes attributes for the card's name, faction, cost, text, and recurring credits. The play method adds the upgrade to the player's list of installed upgrades when it is played, and the trash method removes it from the player's list when it is trashed or discarded.

    # The rez method allows the player to pay the cost to rez the upgrade, making it active and triggering any abilities it may have. If the player has enough credits to pay the cost, the method sets the is_rezzed attribute to True and returns True, otherwise it returns False.

    # The use_credit method allows the player to use one of the recurring credits provided by the upgrade, decrementing the credit pool if there are credits available.
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
