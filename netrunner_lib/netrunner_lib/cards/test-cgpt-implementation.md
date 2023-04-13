
# netrunner prompts

## netrunner game

Use information contained between context tags(<context></context>) as the relevant information necessary to answer the prompts that are contained between prompt tags(<prompt></prompt>). Information outside of those tags should be considered metadata about the use of context info or prompts.
This is my python class describing the state of a netrunner game:
<compact>
NetrunnerGame(corpo_player:Corpo, runner_player:Runner)
- setup(starting_credits:int=5)
- start_turn()
- perform_turn(player:Player, state:str, **kwargs) -> str
- end_turn()
- check_win_conditions() -> Tuple[[win,none], [winning player|None]]
- play_card(card, player)
- print_state()
- prompt_player(player, options)
</compact>
<context>
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

    def setup(self, starting_credits=5):
        '''
        manage initial setup of the game
        '''

    def start_turn(self):
        '''
        tell the current player to start their turn
        '''

    def perform_turn(self,player:Player, state:str, **kwargs) -> str:
        '''
        does checking to ensure flow of game not violated
        if all is well, route turn actions to appropriate player
        returns current state after doing turn actions
        '''

    def end_turn(self):
        '''
				toggle who's turn it is and increment counter, maybe track the time it takes for each turn here
				'''
	
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

    def play_card(self, card, player):

    def print_state(self):
        '''
        print out the current game state info
        '''

    def prompt_player(self,player,options):
</context>

## player classes

Use information contained between context tags(<context></context>) as the relevant information necessary to answer the prompts that are contained between prompt tags(<prompt></prompt>). Information outside of those tags should be considered metadata about the use of context info or prompts.
This is my python classes describing the types of players of a netrunner game:
<context>
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

    def setup_mulligan(self):
    
    def draw_card(self):

    def do_turn_actions(self, state:str):
    
    def get_deck(self):

    def get_hand(self):
    
    def get_discard(self):

    def print_player_details(self) -> None:
        '''
        print player details
        '''

    def print_hand(self) -> None:

    def prompt(self,msg:str) -> str:
        '''
        present prompt to this player, return input
        '''

class Server():
    def __init__(self, name:str, root_card:Card=None):
        self.name = name
        self.root = root_card
        self.upgrades = []
        self.ice = []
    
    def install_ice(self,ice_card:Card) -> str:
    
    def install_upgrade(self,upgrade_card:Card) -> str:

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

    def install_ice(self, server_id:int, card:Card) -> str:
        '''
        install an ice card to the appropriate server based on the provided index
        return status code
        '''
    
    def install_upgrade(self, server_id:int, card:Card) -> str:
        '''
        install an upgrade card to the appropriate server based on the provided index
        return status code
        '''

    def get_server_by_id(self, server_id:int) -> Server:
        '''
        return the server referenced by the provided ID
        NOT TO BE USED for setting info, just getting
        '''

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


    def print_play_area_details(self) -> None:
        '''
        print corpo play area details
        '''

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

    def install_program(self,program_card:Card) -> str:
        '''
        install a program to the runners program slots
        return status code
        '''
    
    def install_hardware(self,hardware_card:Card) -> str:
        '''
        install a hardware to the runners program slots
        return status code
        '''

    def print_play_area_details(self) -> None:
        '''
        print runner play area details
        '''
</context>

## card class

Use information contained between context tags(<context></context>) as the relevant information necessary to answer the prompts that are contained between prompt tags(<prompt></prompt>). Information outside of those tags should be considered metadata about the use of context info or prompts.
This is my python classes describing the types of cards in a netrunner game:
<context>
class Card:
    def __init__(self, card_json:str):
        card_json = json.loads(card_json)
        self.advancement_cost = card_json.get('advancement_cost')
        self.advancement_counters = card_json.get('advancement_counters')
        self.agenda_points = card_json.get('agenda_points')
        self.base_link = card_json.get('base_link')
        self.code = card_json.get('code')#required
        self.cost = card_json.get('cost')
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

    def print_details(self):

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

    def get_card_index(self,location) -> int:
        '''
        get the index of this card in the given location (should be an array)
        '''

    def trash(self, player) -> str:
        '''
        trash this card from its current location, sending to discard pile
        returns str "trashed" on success
        '''
</context>

## agenda prompt

Use information contained between context tags(<context></context>) as the relevant information necessary to answer the prompts that are contained between prompt tags(<prompt></prompt>). Information outside of those tags should be considered metadata about the use of context info or prompts.
This is my python classes describing the types of cards in a netrunner game:
<context>

</context>
<prompt>

</prompt>

## Compressed prompts

Use information contained between context tags(<context></context>) as the relevant information necessary to answer the prompts that are contained between prompt tags(<prompt></prompt>) that will be provided after consuming the context information. Information outside of those tags should be considered metadata about the use of context info or prompts.
This context block contains all JSON descriptions of the properties and methods of the classes used to implement the netrunner card game in python. The template of this representation is `{"class_name":"<name>","class_parent":"<type>","class_properties":[{"property_name":"<name>","type":"<type>"},...],"methods":[{"method_name":"<name>","parameters":[{"parameter_name":"<name>","type":"<type>"},...],"return_type":"<type>"},...]}`.
<context>
```json
{"class_name":"NetrunnerGame","parent_class":"None","class_properties":[{"property_name":"runner","type":"Runner"},{"property_name":"corpo","type":"Corpo"},{"property_name":"turn","type":"int"},{"property_name":"state","type":"str"},{"property_name":"current_player","type":"Player"},{"property_name":"win_condition","type":"dict"}],"methods":[{"method_name":"init","parameters":[{"parameter_name":"corpo_player","type":"Corpo"},{"parameter_name":"runner_player","type":"Runner"}],"return_type":"NoneType"},{"method_name":"setup","parameters":[{"parameter_name":"starting_credits","type":"int"}],"return_type":"NoneType"},{"method_name":"start_turn","parameters":[],"return_type":"NoneType"},{"method_name":"perform_turn","parameters":[{"parameter_name":"player","type":"Player"},{"parameter_name":"state","type":"str"}],"return_type":"str"},{"method_name":"end_turn","parameters":[],"return_type":"NoneType"},{"method_name":"check_win_conditions","parameters":[],"return_type":"Tuple[list, Union[None, str]]"},{"method_name":"play_card","parameters":[{"parameter_name":"card","type":"Card"},{"parameter_name":"player","type":"Player"}],"return_type":"NoneType"},{"method_name":"print_state","parameters":[],"return_type":"NoneType"},{"method_name":"prompt","parameters":[{"parameter_name":"player","type":"Player"},{"parameter_name":"message","type":"str"}],"return_type":"str"}]}

{"class_name":"Deck","class_properties":[{"property_name":"name","type":"str"},{"property_name":"deck_filepath","type":"str"},{"property_name":"date_created","type":"str"},{"property_name":"deck_type","type":"str"},{"property_name":"identity_card","type":"Card"},{"property_name":"cards","type":"list[Card]"},{"property_name":"card_image_preferences","type":"dict"}],"methods":[{"method_name":"_load_o8d_deckfile","parameters":[{"parameter_name":"deck_path","type":"str"}],"return_type":"NoneType"},{"method_name":"_load_json_deckfile","parameters":[{"parameter_name":"deck_path","type":"str"}],"return_type":"NoneType"},{"method_name":"_load_image_preferences","parameters":[],"return_type":"NoneType"},{"method_name":"shuffle","parameters":[],"return_type":"NoneType"},{"method_name":"remove_card","parameters":[{"parameter_name":"card_game_id","type":"str"}],"return_type":"NoneType"},{"method_name":"length","parameters":[],"return_type":"int"},{"method_name":"set_card_image_pref","parameters":[{"parameter_name":"card_code","type":"str"},{"parameter_name":"image_file","type":"str"}],"return_type":"NoneType"},{"method_name":"save","parameters":[],"return_type":"NoneType"}]}

{"class_name":"Player","parent_class":"None","class_properties":[{"property_name":"name","type":"str"},{"property_name":"deck","type":"Deck"},{"property_name":"faction","type":"str"},{"property_name":"hand","type":"list[Card]"},{"property_name":"discard","type":"list[Card]"},{"property_name":"credit_pool","type":"int"},{"property_name":"clicks","type":"int"},{"property_name":"scored_agendas","type":"list[Card]"}],"methods":[{"method_name":"setup","parameters":[{"parameter_name":"starting_credits","type":"int"}],"return_type":"None"},{"method_name":"setup_mulligan","parameters":[],"return_type":"None"},{"method_name":"draw_card","parameters":[],"return_type":"None"},{"method_name":"do_turn_actions","parameters":[{"parameter_name":"state","type":"str"}],"return_type":"str"},{"method_name":"get_deck","parameters":[],"return_type":"Deck"},{"method_name":"get_hand","parameters":[],"return_type":"list[Card]"},{"method_name":"get_discard","parameters":[],"return_type":"list[Card]"},{"method_name":"print_player_details","parameters":[],"return_type":"None"},{"method_name":"print_hand","parameters":[],"return_type":"None"},{"method_name":"prompt","parameters":[{"parameter_name":"msg","type":"str"}],"return_type":"str"}]}

{"class_name":"Server","parent_class":"None","class_properties": [{"property_name": "name","type":"str"},{"property_name":"root_card", "type":"Card"}],"methods":[{"method_name":"install_ice","parameters":[{"parameter_name":"ice_card","type":"Card"}],"return_type":"str"},{"method_name":"install_upgrade","parameters": [{"parameter_name":"upgrade_card","type":"Card"}],"return_type":"str"}]}

{"class_name":"Corpo","parent_class":"Player","class_properties":[{"property_name":"name","type":"str"},{"property_name":"deck_path","type":"str"},{"property_name":"faction","type":"str"},{"property_name":"hand","type":"list[Card]"},{"property_name":"discard","type":"list[Card]"},{"property_name":"credit_pool","type":"int"},{"property_name":"clicks","type":"int"},{"property_name":"scored_agendas","type":"list[Card]"},{"property_name":"hq_server","type":"Server"},{"property_name":"rnd_server","type":"Server"},{"property_name":"archive_server","type":"Server"},{"property_name":"remote_servers","type":"list[Server]"},{"property_name":"bad_publicity_score","type":"int"}],"methods":[{"method_name":"install_new_remote_server","parameters":[{"parameter_name":"card","type":"Card"}],"return_type":"str"},{"method_name":"install_ice","parameters":[{"parameter_name":"server_id","type":"int"},{"parameter_name":"card","type":"Card"}],"return_type":"str"},{"method_name":"install_upgrade","parameters":[{"parameter_name":"server_id","type":"int"},{"parameter_name":"card","type":"Card"}],"return_type":"str"},{"method_name":"get_server_by_id","parameters":[{"parameter_name":"server_id","type":"int"}],"return_type":"Server"},{"method_name":"do_turn_actions","parameters":[{"parameter_name":"turn_state","type":"str"},{"parameter_name":"**kwargs","type":"Any"}],"return_type":"str"},{"method_name":"print_play_area_details","parameters":[],"return_type":"None"}]}

{"class_name":"Runner","parent_class":"Player","class_properties":[{"property_name":"name","type":"str"},{"property_name":"deck_path","type":"str"},{"property_name":"programs","type":"list[Card]"},{"property_name":"hardware","type":"list[Card]"},{"property_name":"resources","type":"list[Card]"},{"property_name":"tags","type":"list[str]"},{"property_name":"memory_units","type":"int"},{"property_name":"brain_damage","type":"int"},{"property_name":"max_hand_size","type":"int"}],"methods":[{"method_name":"do_turn_actions","parameters":[{"parameter_name":"turn_state","type":"str"}],"return_type":"str"},{"method_name":"install_program","parameters":[{"parameter_name":"program_card","type":"Card"}],"return_type":"str"},{"method_name":"install_hardware","parameters":[{"parameter_name":"hardware_card","type":"Card"}],"return_type":"str"},{"method_name":"print_play_area_details","parameters":[],"return_type":"None"}]}

{"class_name":"Card","parent_class":"None","class_properties":[{"property_name":"advancement_cost","type":"int"},{"property_name":"advancement_counters","type":"int"},{"property_name":"agenda_points","type":"int"},{"property_name":"base_link","type":"TODO"},{"property_name":"code","type":"str"},{"property_name":"cost","type":"int"},{"property_name":"faction_code","type":"str"},{"property_name":"faction_cost","type":"int"},{"property_name":"flavor","type":"str"},{"property_name":"illustrator","type":"str"},{"property_name":"influence_limit","type":"int"},{"property_name":"keywords","type":"str"},{"property_name":"deck_limit","type":"str"},{"property_name":"memory_cost","type":"int"},{"property_name":"minimum_deck_size","type":"int"},{"property_name":"pack_code","type":"str"},{"property_name":"position","type":"str"},{"property_name":"quantity","type":"int"},{"property_name":"side_code","type":"str"},{"property_name":"strength","type":"int"},{"property_name":"text","type":"str"},{"property_name":"stripped_text","type":"str"},{"property_name":"title","type":"str"},{"property_name":"stripped_title","type":"str"},{"property_name":"trash_cost","type":"int"},{"property_name":"type_code","type":"str"},{"property_name":"uniqueness","type":"str"},{"property_name":"image_path","type":"str"},{"property_name":"state","type":"dict"},{"property_name":"game_id","type":"str"}],"methods":[{"method_name":"str","parameters":[],"return_type":"str"},{"method_name":"print_details","parameters":[],"return_type":"None"},{"method_name":"play","parameters":[{"parameter_name":"player","type":"Player"},{"parameter_name":"kwargs","type":"dict"}],"return_type":"str"},{"method_name":"get_card_index","parameters":[{"parameter_name":"location","type":"list"}],"return_type":"int"},{"method_name":"trash","parameters":[{"parameter_name":"player","type":"Player"}],"return_type":"str"}]}

{"class_name":"agenda","parent_class":"Card","class_properties":[{"property_name":"is_scored","type":"bool"},],"methods":[{"method_name":"__init__","parameters":[{"parameter_name":"card_json","type":"str"},],"return_type":"str"},{"method_name":"play","parameters":[{"parameter_name":"player","type":"Player"},{"parameter_name":"kwargs","type":"dict"},],"return_type":"str"},{"method_name":"score","parameters":[{"parameter_name":"player","type":"Player"},{"parameter_name":"game","type":"NetrunnerGame"},],"return_type":"bool"},]}
```
</context>
This next context block contains a JSON object that defines the properties for a specific card in the netrunner game.
<context>
```json
{"advancement_cost": 3, "agenda_points": 2, "code": "01081", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Initiative", "pack_code": "core", "position": 81, "quantity": 2, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: Place 1 advancement counter on an installed card you can advance. Limit 1 per deck.", "stripped_title": "AstroScript Pilot Program", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter:</strong> Place 1 advancement counter on an installed card you can advance.\nLimit 1 per deck.", "title": "AstroScript Pilot Program", "type_code": "agenda", "uniqueness": false}
```
</context>
<prompt>
Using the program definitions in the first context block and the json description of the card in the second context block, generate a python class that implements the properties and methods of the proposed card. The methods of the card will need to perform the actions described in the 'stripped_text' field of the card JSON. This card should be a subclass of the agenda card class and implement the __init__, play, and score methods at minimimum.
</prompt>
