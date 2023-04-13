
'''
card classes of type ice
'''
from netrunner_lib.cards._base_card_classes import Ice
from netrunner_lib.game_events import *

class ice_heimdall_10_01061(Ice):
    '''
    Cost: 8
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01061", "cost": 8, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "I hear the shift of every bit amid the flow of the datastream. I hear the whispers of my mothers, and their commands are law. The realm beyond is forbidden.", "illustrator": "Gong Studios", "keywords": "Barrier - Bioroid - AP", "pack_code": "core", "position": 61, "quantity": 2, "side_code": "corp", "strength": 6, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run. Subroutine End the run.", "stripped_title": "Heimdall 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Heimdall 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ichi_10_01062(Ice):
    '''
    Cost: 5
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01062", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "My reputation would precede me, if any could speak of it.", "illustrator": "Gong Studios", "keywords": "Sentry - Bioroid - Tracer - Destroyer", "pack_code": "core", "position": 62, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.", "stripped_title": "Ichi 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.\n[subroutine] Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.", "title": "Ichi 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_viktor_10_01063(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01063", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "My name is Viktor. Nice to meet you. Would you like to play a game?", "illustrator": "Anna Ignatieva", "keywords": "Code Gate - Bioroid - AP", "pack_code": "core", "position": 63, "quantity": 2, "side_code": "corp", "strength": 3, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.", "stripped_title": "Viktor 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] End the run.", "title": "Viktor 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_rototurret_01064(Ice):
    '''
    Cost: 4
    Text: Subroutine Trash 1 installed program. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01064", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Whrrrrr!", "illustrator": "Ed Mattinian", "keywords": "Sentry - Destroyer", "pack_code": "core", "position": 64, "quantity": 2, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine Trash 1 installed program. Subroutine End the run.", "stripped_title": "Rototurret", "text": "[subroutine] Trash 1 installed program.\n[subroutine] End the run.", "title": "Rototurret", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_cell_portal_01074(Ice):
    '''
    Cost: 5
    Text: Subroutine The Runner moves to the outermost position of the attacked server. They may jack out. Derez this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01074", "cost": 5, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"Where does it go?\"", "illustrator": "Adam Schumpert", "keywords": "Code Gate - Deflector", "pack_code": "core", "position": 74, "quantity": 2, "side_code": "corp", "strength": 7, "stripped_text": "Subroutine The Runner moves to the outermost position of the attacked server. They may jack out. Derez this ice.", "stripped_title": "Cell Portal", "text": "[subroutine] The Runner moves to the outermost position of the attacked server. They may jack out. Derez this ice.", "title": "Cell Portal", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_chum_01075(Ice):
    '''
    Cost: 1
    Text: Subroutine The next piece of ice the Runner encounters during this run gets +2 strength. When that encounter ends, if the Runner did not fully break that ice, do 3 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01075", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"You ever get that feeling like you're shark food? Pay attention to that feeling.\" -Ji \"Noise\" Reilly", "illustrator": "Ed Mattinian", "keywords": "Code Gate", "pack_code": "core", "position": 75, "quantity": 2, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine The next piece of ice the Runner encounters during this run gets +2 strength. When that encounter ends, if the Runner did not fully break that ice, do 3 net damage.", "stripped_title": "Chum", "text": "[subroutine] The next piece of ice the Runner encounters during this run gets +2 strength. When that encounter ends, if the Runner did not fully break that ice, do 3 net damage.", "title": "Chum", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_data_mine_01076(Ice):
    '''
    Cost: 0
    Text: Subroutine Do 1 net damage. Trash Data Mine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01076", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Access HarmlessFile.datZ -> Are you sure? y/n", "illustrator": "Andrew Mar", "keywords": "Trap - AP", "pack_code": "core", "position": 76, "quantity": 2, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine Do 1 net damage. Trash Data Mine.", "stripped_title": "Data Mine", "text": "[subroutine] Do 1 net damage. Trash Data Mine.", "title": "Data Mine", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_neural_katana_01077(Ice):
    '''
    Cost: 4
    Text: Subroutine Do 3 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01077", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Forged by Ak.wa on 23.11.79-23. Filed 23.11.79-23.2 with #34k-lw3-21HH-4i.\n//Samurai included.", "illustrator": "Isuardi Therianto", "keywords": "Sentry - AP", "pack_code": "core", "position": 77, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Do 3 net damage.", "stripped_title": "Neural Katana", "text": "[subroutine] Do 3 net damage.", "title": "Neural Katana", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wall_of_thorns_01078(Ice):
    '''
    Cost: 8
    Text: Subroutine Do 2 net damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01078", "cost": 8, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Most runners do their business in full-sim, with their rigs wired directly into their brains. The setup has a large number of advantages, with the runner able to process data and input commands far faster than a traditional meat-bound system. But it also means greater risk.", "illustrator": "Adam S. Doyle", "keywords": "Barrier - AP", "pack_code": "core", "position": 78, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Do 2 net damage. Subroutine End the run.", "stripped_title": "Wall of Thorns", "text": "[subroutine] Do 2 net damage.\n[subroutine] End the run.", "title": "Wall of Thorns", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_data_raven_01088(Ice):
    '''
    Cost: 4
    Text: When the Runner encounters this ice, they must take 1 tag or end the run. Hosted power counter: Give the Runner 1 tag. Subroutine Trace[3]. If successful, place 1 power counter on this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01088", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Gong Studios", "keywords": "Sentry - Tracer - Observer", "pack_code": "core", "position": 88, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters this ice, they must take 1 tag or end the run. Hosted power counter: Give the Runner 1 tag. Subroutine Trace[3]. If successful, place 1 power counter on this ice.", "stripped_title": "Data Raven", "text": "When the Runner encounters this ice, they must take 1 tag or end the run.\n<strong>Hosted power counter:</strong> Give the Runner 1 tag.\n[subroutine] Trace[3]. If successful, place 1 power counter on this ice.", "title": "Data Raven", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_matrix_analyzer_01089(Ice):
    '''
    Cost: 1
    Text: When the Runner encounters Matrix Analyzer, you may pay 1 credit to place 1 advancement token on a card that can be advanced. Subroutine Trace[2]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01089", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Analyzing was great. Delegating commands turned out to be even better.", "illustrator": "Isuardi Therianto", "keywords": "Sentry - Tracer - Observer", "pack_code": "core", "position": 89, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When the Runner encounters Matrix Analyzer, you may pay 1 credit to place 1 advancement token on a card that can be advanced. Subroutine Trace[2]. If successful, give the Runner 1 tag.", "stripped_title": "Matrix Analyzer", "text": "When the Runner encounters Matrix Analyzer, you may pay 1[credit] to place 1 advancement token on a card that can be advanced.\n[subroutine] Trace[2]. If successful, give the Runner 1 tag.", "title": "Matrix Analyzer", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tollbooth_01090(Ice):
    '''
    Cost: 8
    Text: When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01090", "cost": 8, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Ever heard of a catch-22?\"\n\"Remind me to forget it.\"", "illustrator": "Outland Entertainment LLC", "keywords": "Code Gate", "pack_code": "core", "position": 90, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.", "stripped_title": "Tollbooth", "text": "When the Runner encounters this ice, they must pay 3[credit], if able. If they do not, end the run.\n[subroutine] End the run.", "title": "Tollbooth", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_archer_01101(Ice):
    '''
    Cost: 4
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01101", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Next time, read the Terms of Service more carefully. Or you might find yourself in the danger zone.", "illustrator": "Mike Nesbitt", "keywords": "Sentry - Destroyer", "pack_code": "core", "position": 101, "quantity": 2, "side_code": "corp", "strength": 6, "stripped_text": "As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.", "stripped_title": "Archer", "text": "As an additional cost to rez this ice, forfeit 1 agenda.\n[subroutine] Gain 2[credit].\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.\n[subroutine] End the run.", "title": "Archer", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hadrians_wall_01102(Ice):
    '''
    Cost: 10
    Text: Hadrian's Wall can be advanced and has +1 strength for each advancement token on it. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01102", "cost": 10, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "\"He had a bit of an ego, ol' Hadrian. His constructs live up to it though.\" -g00ru", "illustrator": "Bruno Balixa", "keywords": "Barrier", "pack_code": "core", "position": 102, "quantity": 2, "side_code": "corp", "strength": 7, "stripped_text": "Hadrian's Wall can be advanced and has +1 strength for each advancement token on it. Subroutine End the run. Subroutine End the run.", "stripped_title": "Hadrian's Wall", "text": "Hadrian's Wall can be advanced and has +1 strength for each advancement token on it.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Hadrian's Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ice_wall_01103(Ice):
    '''
    Cost: 1
    Text: You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01103", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"I asked for ice as impenetrable as a wall. I can't decide if someone down in R&D has a warped sense of humor or just a very literal mind.\" -Liz Campbell, VP Project Security", "illustrator": "Matt Zeilinger", "keywords": "Barrier", "pack_code": "core", "position": 103, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.", "stripped_title": "Ice Wall", "text": "You can advance this ice. It gets +1 strength for each hosted advancement counter.\n[subroutine] End the run.", "title": "Ice Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_shadow_01104(Ice):
    '''
    Cost: 3
    Text: Shadow can be advanced and has +1 strength for each advancement token on it. Subroutine The Corp gains 2 credits. Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01104", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Who knows what evil lurks in the memory diamonds of men? Weyland knows. -unsigned cyber-graffiti", "illustrator": "Adam S. Doyle", "keywords": "Sentry - Tracer", "pack_code": "core", "position": 104, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Shadow can be advanced and has +1 strength for each advancement token on it. Subroutine The Corp gains 2 credits. Subroutine Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "Shadow", "text": "Shadow can be advanced and has +1 strength for each advancement token on it.\n[subroutine] The Corp gains 2[credit].\n[subroutine] Trace[3]. If successful, give the Runner 1 tag.", "title": "Shadow", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_enigma_01111(Ice):
    '''
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01111", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Hey, hey! Wake up, man. You were under a long time. What'd you see?\"\n\"I\u2026don't remember.\"", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate", "pack_code": "core", "position": 111, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine The Runner loses click. Subroutine End the run.", "stripped_title": "Enigma", "text": "[subroutine] The Runner loses [click].\n[subroutine] End the run.", "title": "Enigma", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hunter_01112(Ice):
    '''
    Cost: 1
    Text: Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01112", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": ".//run/hunter-tr/return=true\nclient/sec256IPv7->confirm? /y\n3926:0HB7:1001:2NB1:1601:7784:ERROR", "illustrator": "Christina Davis", "keywords": "Sentry - Tracer - Observer", "pack_code": "core", "position": 112, "quantity": 2, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "Hunter", "text": "[subroutine] Trace[3]. If successful, give the Runner 1 tag.", "title": "Hunter", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wall_of_static_01113(Ice):
    '''
    Cost: 3
    Text: Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01113", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"There's nothing worse than seeing that beautiful blue ball of data just out of reach as your connection derezzes. I think they do it just to taunt us.\" -Ele \"Smoke\" Scovak", "illustrator": "Adam S. Doyle", "keywords": "Barrier", "pack_code": "core", "position": 113, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine End the run.", "stripped_title": "Wall of Static", "text": "[subroutine] End the run.", "title": "Wall of Static", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_janus_10_02012(Ice):
    '''
    Cost: 15
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine Do 1 core damage. Subroutine Do 1 core damage. Subroutine Do 1 core damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02012", "cost": 15, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "Face your fear.", "illustrator": "Tim Durning", "keywords": "Sentry - Bioroid - AP", "pack_code": "wla", "position": 12, "quantity": 3, "side_code": "corp", "strength": 8, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine Do 1 core damage. Subroutine Do 1 core damage. Subroutine Do 1 core damage.", "stripped_title": "Janus 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] Do 1 core damage.\n[subroutine] Do 1 core damage.\n[subroutine] Do 1 core damage.", "title": "Janus 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_snowflake_02015(Ice):
    '''
    Cost: 1
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. End the run if you and the Runner spent a different number of credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02015", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Sometimes uniqueness is overrated.", "illustrator": "Mashuri", "keywords": "Barrier - Psi", "pack_code": "wla", "position": 15, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. End the run if you and the Runner spent a different number of credits.", "stripped_title": "Snowflake", "text": "[subroutine] You and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. End the run if you and the Runner spent a different number of credits.", "title": "Snowflake", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tmi_02017(Ice):
    '''
    Cost: 3
    Text: When you rez TMI, Trace[2]. If unsuccessful, derez TMI. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02017", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "A collection of cast-off cyberjunk. But it doesn't stay junk for long.", "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "wla", "position": 17, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When you rez TMI, Trace[2]. If unsuccessful, derez TMI. Subroutine End the run.", "stripped_title": "TMI", "text": "When you rez TMI, Trace[2]. If unsuccessful, derez TMI.\n[subroutine] End the run.", "title": "TMI", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_caduceus_02019(Ice):
    '''
    Cost: 3
    Text: Subroutine Trace[3]. If successful, the Corp gains 3 credits. Subroutine Trace[2]. If successful, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02019", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "A symbol of commerce, but beware its bite.", "illustrator": "Christina Davis", "keywords": "Sentry - Tracer", "pack_code": "wla", "position": 19, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Trace[3]. If successful, the Corp gains 3 credits. Subroutine Trace[2]. If successful, end the run.", "stripped_title": "Caduceus", "text": "[subroutine] Trace[3]. If successful, the Corp gains 3[credit].\n[subroutine] Trace[2]. If successful, end the run.", "title": "Caduceus", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_draco_02020(Ice):
    '''
    Cost: 1
    Text: When you rez Draco, you may pay X credits to place X power counters on it. Draco has +1 strength for each power counter on it. Subroutine Trace[2]. If successful, give the Runner 1 tag and end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02020", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Vict\u014ds dracon\u0113s numquam deride.", "illustrator": "Sandara Tang", "keywords": "Sentry - Tracer", "pack_code": "wla", "position": 20, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "When you rez Draco, you may pay X credits to place X power counters on it. Draco has +1 strength for each power counter on it. Subroutine Trace[2]. If successful, give the Runner 1 tag and end the run.", "stripped_title": "Draco", "text": "When you rez Drac\u014d, you may pay X[credit] to place X power counters on it.\nDrac\u014d has +1 strength for each power counter on it.\n[subroutine] Trace[2]. If successful, give the Runner 1 tag and end the run.", "title": "Drac\u014d", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sherlock_10_02030(Ice):
    '''
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trace[4]. If successful, add 1 installed program to the top of the Runner's stack. Subroutine Trace[4]. If successful, add 1 installed program to the top of the Runner's stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02030", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Matt Zeilinger", "keywords": "Sentry - Bioroid - Tracer", "pack_code": "ta", "position": 30, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trace[4]. If successful, add 1 installed program to the top of the Runner's stack. Subroutine Trace[4]. If successful, add 1 installed program to the top of the Runner's stack.", "stripped_title": "Sherlock 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Trace[4]. If successful, add 1 installed program to the top of the Runner's stack.\n[subroutine] Trace[4]. If successful, add 1 installed program to the top of the Runner's stack.", "title": "Sherlock 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sensei_02034(Ice):
    '''
    Cost: 3
    Text: Subroutine For the remainder of this run, each piece of ice encountered except Sensei gains "Subroutine End the run" after all its other subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02034", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Peace and violence. Both must lead to the same place.", "illustrator": "Sandara Tang", "keywords": "Code Gate", "pack_code": "ta", "position": 34, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine For the remainder of this run, each piece of ice encountered except Sensei gains \"Subroutine End the run\" after all its other subroutines.", "stripped_title": "Sensei", "text": "[subroutine] For the remainder of this run, each piece of ice encountered except Sensei gains \"[subroutine] End the run\" after all its other subroutines.", "title": "Sensei", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_viper_02052(Ice):
    '''
    Cost: 3
    Text: Subroutine Trace[3]. If successful, the Runner loses click, if able. Subroutine Trace[3]. If successful, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02052", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Dont Tread On Me", "illustrator": "Bruno Balixa", "keywords": "Code Gate - Tracer", "pack_code": "ce", "position": 52, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Trace[3]. If successful, the Runner loses click, if able. Subroutine Trace[3]. If successful, end the run.", "stripped_title": "Viper", "text": "[subroutine] Trace[3]. If successful, the Runner loses [click], if able.\n[subroutine] Trace[3]. If successful, end the run.", "title": "Viper", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_popup_window_02056(Ice):
    '''
    Cost: 0
    Text: When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02056", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"Try to close it. Go on. See what it does.\" -Chaos Theory", "illustrator": "Christina Davis", "keywords": "Code Gate - Advertisement", "pack_code": "ce", "position": 56, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.", "stripped_title": "Pop-up Window", "text": "When the Runner encounters this ice, gain 1[credit].\n[subroutine] End the run unless the Runner pays 1[credit].", "title": "Pop-up Window", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_woodcutter_02057(Ice):
    '''
    Cost: 4
    Text: Woodcutter can be advanced only while rezzed and gains "Subroutine Do 1 net damage." for each advancement token on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02057", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "Chop chop.", "illustrator": "Mike Nesbitt", "keywords": "Sentry - AP", "pack_code": "ce", "position": 57, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Woodcutter can be advanced only while rezzed and gains \"Subroutine Do 1 net damage.\" for each advancement token on it.", "stripped_title": "Woodcutter", "text": "Woodcutter can be advanced only while rezzed and gains \"[subroutine] Do 1 net damage.\" for each advancement token on it.", "title": "Woodcutter", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_chimera_02060(Ice):
    '''
    Cost: 2
    Text: When you rez Chimera, choose sentry, code gate, or barrier. Chimera gains that subtype until derezzed. When a turn ends, derez Chimera. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02060", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Three heads. One big headache.", "illustrator": "Isuardi Therianto", "keywords": "Mythic", "pack_code": "ce", "position": 60, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "When you rez Chimera, choose sentry, code gate, or barrier. Chimera gains that subtype until derezzed. When a turn ends, derez Chimera. Subroutine End the run.", "stripped_title": "Chimera", "text": "When you rez Chimera, choose <strong>sentry</strong>, <strong>code gate</strong>, or <strong>barrier</strong>. Chimera gains that subtype until derezzed.\nWhen a turn ends, derez Chimera.\n[subroutine] End the run.", "title": "Chimera", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hourglass_02071(Ice):
    '''
    Cost: 5
    Text: Subroutine The Runner loses click, if able. Subroutine The Runner loses click, if able. Subroutine The Runner loses click, if able.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02071", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Time just slips away.", "illustrator": "JuanManuel Tumburus", "keywords": "Code Gate", "pack_code": "asis", "position": 71, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine The Runner loses click, if able. Subroutine The Runner loses click, if able. Subroutine The Runner loses click, if able.", "stripped_title": "Hourglass", "text": "[subroutine] The Runner loses [click], if able.\n[subroutine] The Runner loses [click], if able.\n[subroutine] The Runner loses [click], if able.", "title": "Hourglass", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bullfrog_02073(Ice):
    '''
    Cost: 3
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits and this ice is installed, move this ice to the outermost position protecting another server. (The run continues from this new position.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02073", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Christina Davis", "keywords": "Code Gate - Deflector - Psi", "pack_code": "asis", "position": 73, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine You and the Runner secretly spend 0 credits, 1 credit or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits and this ice is installed, move this ice to the outermost position protecting another server. (The run continues from this new position.)", "stripped_title": "Bullfrog", "text": "[subroutine] You and the Runner secretly spend 0[credit], 1[credit] or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits and this ice is installed, move this ice to the outermost position protecting another server. <em>(The run continues from this new position.)</em>", "title": "Bullfrog", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_uroboros_02074(Ice):
    '''
    Cost: 6
    Text: Subroutine Trace[4]. If successful, the Runner cannot make another run this turn. Subroutine Trace[4]. If successful, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02074", "cost": 6, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Where one thing ends, another begins.", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - Tracer", "pack_code": "asis", "position": 74, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Trace[4]. If successful, the Runner cannot make another run this turn. Subroutine Trace[4]. If successful, end the run.", "stripped_title": "Uroboros", "text": "[subroutine] Trace[4]. If successful, the Runner cannot make another run this turn.\n[subroutine] Trace[4]. If successful, end the run.", "title": "Uroboros", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tyrant_02078(Ice):
    '''
    Cost: 7
    Text: Tyrant can be advanced only while rezzed and gains "Subroutine End the run." for each advancement token on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02078", "cost": 7, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Thou shall not pass.", "illustrator": "Isuardi Therianto", "keywords": "Barrier", "pack_code": "asis", "position": 78, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Tyrant can be advanced only while rezzed and gains \"Subroutine End the run.\" for each advancement token on it.", "stripped_title": "Tyrant", "text": "Tyrant can be advanced only while rezzed and gains \"[subroutine] End the run.\" for each advancement token on it.", "title": "Tyrant", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_whirlpool_02094(Ice):
    '''
    Cost: 0
    Text: Subroutine The Runner cannot jack out for the remainder of this run. Trash Whirlpool.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02094", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"This ice sucks.\" -g00ru", "illustrator": "Adam S. Doyle", "keywords": "Trap", "pack_code": "hs", "position": 94, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Subroutine The Runner cannot jack out for the remainder of this run. Trash Whirlpool.", "stripped_title": "Whirlpool", "text": "[subroutine] The Runner cannot jack out for the remainder of this run. Trash Whirlpool.", "title": "Whirlpool", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_data_hound_02096(Ice):
    '''
    Cost: 1
    Text: Subroutine Trace[2]. If successful, look at the top X cards of the stack, where X is equal to the amount by which your trace strength exceeded the Runner's link strength. Trash 1 of those cards and arrange the rest in any order.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02096", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Sniff.", "illustrator": "Adam S. Doyle", "keywords": "Sentry - Tracer - Observer", "pack_code": "hs", "position": 96, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine Trace[2]. If successful, look at the top X cards of the stack, where X is equal to the amount by which your trace strength exceeded the Runner's link strength. Trash 1 of those cards and arrange the rest in any order.", "stripped_title": "Data Hound", "text": "[subroutine] Trace[2]. If successful, look at the top X cards of the stack, where X is equal to the amount by which your trace strength exceeded the Runner's link strength. Trash 1 of those cards and arrange the rest in any order.", "title": "Data Hound", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_salvage_02098(Ice):
    '''
    Cost: 2
    Text: Salvage can be advanced only while rezzed and gains Subroutine Trace[2]. If successful, give the Runner 1 tag. for each advancement token on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02098", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "You're not in Kansas anymore.", "illustrator": "Ed Mattinian", "keywords": "Code Gate - Tracer", "pack_code": "hs", "position": 98, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Salvage can be advanced only while rezzed and gains Subroutine Trace[2]. If successful, give the Runner 1 tag. for each advancement token on it.", "stripped_title": "Salvage", "text": "Salvage can be advanced only while rezzed and gains \u201c[subroutine] Trace[2]. If successful, give the Runner 1 tag.\u201d for each advancement token on it.", "title": "Salvage", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_eli_10_02110(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02110", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "\"That's against the rules. The Creators will be angry.\"", "illustrator": "Sandara Tang", "keywords": "Barrier - Bioroid", "pack_code": "fp", "position": 110, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.", "stripped_title": "Eli 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Eli 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_flare_02117(Ice):
    '''
    Cost: 9
    Text: Subroutine Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02117", "cost": 9, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "A bright light blossomed, and then the console went dark. That's when she smelled smoke.", "illustrator": "Mike Nesbitt", "keywords": "Sentry - Tracer - AP", "pack_code": "fp", "position": 117, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "Subroutine Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.", "stripped_title": "Flare", "text": "[subroutine]Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.", "title": "Flare", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_burke_bugs_02119(Ice):
    '''
    Cost: 0
    Text: Subroutine Trace[0]. If successful, the Runner trashes 1 program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02119", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"If I had to describe the bugs in one word, it would be '****ing annoying.'\" -Whizzard", "illustrator": "Reza Ilyasa", "keywords": "Sentry - Destroyer", "pack_code": "fp", "position": 119, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine Trace[0]. If successful, the Runner trashes 1 program.", "stripped_title": "Burke Bugs", "text": "[subroutine] Trace[0]. If successful, the Runner trashes 1 program.", "title": "Burke Bugs", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_heimdall_20_03015(Ice):
    '''
    Cost: 11
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine Do 1 core damage and end the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03015", "cost": 11, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "The realm beyond is still forbidden.", "illustrator": "John Derek Murphy", "keywords": "Barrier - Bioroid - AP", "pack_code": "cac", "position": 15, "quantity": 3, "side_code": "corp", "strength": 7, "stripped_text": "Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine Do 1 core damage and end the run. Subroutine End the run.", "stripped_title": "Heimdall 2.0", "text": "<strong>Lose [click][click]:</strong> Break up to 2 subroutines on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] Do 1 core damage and end the run.\n[subroutine] End the run.", "title": "Heimdall 2.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_howler_03016(Ice):
    '''
    Cost: 1
    Text: Subroutine You may install and rez a piece of bioroid ice from HQ or Archives, ignoring all costs, placing it directly behind Howler. If you do, derez that piece of ice and trash Howler after the run is completed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03016", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "\"Yeah. It made a loud noise, I got scared, and I jacked out. I still think I made the right decision.\" -g00ru", "illustrator": "Lili Ibrahim", "keywords": "Trap", "pack_code": "cac", "position": 16, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine You may install and rez a piece of bioroid ice from HQ or Archives, ignoring all costs, placing it directly behind Howler. If you do, derez that piece of ice and trash Howler after the run is completed.", "stripped_title": "Howler", "text": "[subroutine] You may install and rez a piece of <strong>bioroid</strong> ice from HQ or Archives, ignoring all costs, placing it directly behind Howler. If you do, derez that piece of ice and trash Howler after the run is completed.", "title": "Howler", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ichi_20_03017(Ice):
    '''
    Cost: 8
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[3]. If successful, do 1 core damage and give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03017", "cost": 8, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "The game has changed.", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - Bioroid - Destroyer - Tracer", "pack_code": "cac", "position": 17, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[3]. If successful, do 1 core damage and give the Runner 1 tag.", "stripped_title": "Ichi 2.0", "text": "<strong>Lose [click][click]:</strong> Break up to 2 subroutines on this ice. Only the Runner can use this ability.\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.\n[subroutine] Trace[3]. If successful, do 1 core damage and give the Runner 1 tag.", "title": "Ichi 2.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_minelayer_03018(Ice):
    '''
    Cost: 1
    Text: Subroutine You may install a piece of ice from HQ as the outermost piece of ice protecting this server, ignoring all install costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03018", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Sometimes you just have to guess.", "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "cac", "position": 18, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine You may install a piece of ice from HQ as the outermost piece of ice protecting this server, ignoring all install costs.", "stripped_title": "Minelayer", "text": "[subroutine] You may install a piece of ice from HQ as the outermost piece of ice protecting this server, ignoring all install costs.", "title": "Minelayer", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_viktor_20_03019(Ice):
    '''
    Cost: 5
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Hosted power counter: Do 1 core damage. Subroutine Trace[2]. If successful, place 1 power counter on this ice. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03019", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Daniel Atanasov", "keywords": "Code Gate - Bioroid - Tracer - AP", "pack_code": "cac", "position": 19, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Hosted power counter: Do 1 core damage. Subroutine Trace[2]. If successful, place 1 power counter on this ice. Subroutine End the run.", "stripped_title": "Viktor 2.0", "text": "<strong>Lose [click][click]:</strong> Break up to 2 subroutines on this ice. Only the Runner can use this ability.\n<strong>Hosted power counter:</strong> Do 1 core damage.\n[subroutine] Trace[2]. If successful, place 1 power counter on this ice.\n[subroutine] End the run.", "title": "Viktor 2.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_zed_10_03020(Ice):
    '''
    Cost: 2
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine If the Runner has lost click to break a subroutine during this run, do 1 core damage. Subroutine If the Runner has lost click to break a subroutine during this run, do 1 core damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03020", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "A mind of meat! How does it work?", "illustrator": "Daniel Atanasov", "keywords": "Sentry - Bioroid - AP", "pack_code": "cac", "position": 20, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine If the Runner has lost click to break a subroutine during this run, do 1 core damage. Subroutine If the Runner has lost click to break a subroutine during this run, do 1 core damage.", "stripped_title": "Zed 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] If the Runner has lost [click] to break a subroutine during this run, do 1 core damage.\n[subroutine] If the Runner has lost [click] to break a subroutine during this run, do 1 core damage.", "title": "Zed 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bastion_03026(Ice):
    '''
    Cost: 4
    Text: Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03026", "cost": 4, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "The principle behind ice is not to keep everyone out, but to let only some people in. This ice denies entry on all but a select few ports that might change with the time of day or picosecond of connection. If you don't know what port to use, you're not getting in. Period.", "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "cac", "position": 26, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine End the run.", "stripped_title": "Bastion", "text": "[subroutine] End the run.", "title": "Bastion", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_datapike_03027(Ice):
    '''
    Cost: 4
    Text: Subroutine The Runner must pay 2 credits, if able. If the Runner cannot pay 2 credits, end the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03027", "cost": 4, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Cheap, off-the-shelf data protection. Cheap for them, that is. Not for us.\" -Ele \"Smoke\" Scovak", "illustrator": "Aaron Firem", "keywords": "Code Gate", "pack_code": "cac", "position": 27, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine The Runner must pay 2 credits, if able. If the Runner cannot pay 2 credits, end the run. Subroutine End the run.", "stripped_title": "Datapike", "text": "[subroutine] The Runner must pay 2[credit], if able. If the Runner cannot pay 2[credit], end the run.\n[subroutine] End the run.", "title": "Datapike", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_next_bronze_04011(Ice):
    '''
    Cost: 2
    Text: NEXT Bronze has +1 strength for each rezzed piece of NEXT ice. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04011", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "NEXT Design's ice provides the discerning business with a suite of ice that creates a daunting security presence for intruders.", "illustrator": "Ed Mattinian", "keywords": "Code Gate - NEXT", "pack_code": "om", "position": 11, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "NEXT Bronze has +1 strength for each rezzed piece of NEXT ice. Subroutine End the run.", "stripped_title": "NEXT Bronze", "text": "NEXT Bronze has +1 strength for each rezzed piece of <strong>NEXT</strong> ice.\n[subroutine] End the run.", "title": "NEXT Bronze", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_himitsubako_04013(Ice):
    '''
    Cost: 2
    Text: 1 credit: Add Himitsu-Bako to HQ. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04013", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Himitsu-Bako is a simple ice barrier that appears as a digital puzzle box. What makes it special is the ease with which it can be uninstalled and installed in a different server, throwing up barriers in unexpected places and giving any intruder a curious feeling of d\u00e9j\u00e0 vu.", "illustrator": "Andrew Mar", "keywords": "Barrier", "pack_code": "om", "position": 13, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "1 credit: Add Himitsu-Bako to HQ. Subroutine End the run.", "stripped_title": "Himitsu-Bako", "text": "1[credit]: Add Himitsu-Bako to HQ.\n[subroutine] End the run.", "title": "Himitsu-Bako", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_swarm_04018(Ice):
    '''
    Cost: 8
    Text: When you rez Swarm, take 1 bad publicity. Swarm can be advanced and gains "Subroutine Trash 1 program unless the Runner pays 3 credits." for each advancement token on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04018", "cost": 8, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "Ed Mattinian", "keywords": "Sentry - Destroyer - Illicit", "pack_code": "om", "position": 18, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When you rez Swarm, take 1 bad publicity. Swarm can be advanced and gains \"Subroutine Trash 1 program unless the Runner pays 3 credits.\" for each advancement token on it.", "stripped_title": "Swarm", "text": "When you rez Swarm, take 1 bad publicity.\nSwarm can be advanced and gains \"[subroutine] Trash 1 program unless the Runner pays 3[credit].\" for each advancement token on it.", "title": "Swarm", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_grim_04020(Ice):
    '''
    Cost: 5
    Text: When you rez Grim, take 1 bad publicity. Subroutine Trash 1 program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04020", "cost": 5, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"The Grim of legend was one of many so-called 'black dog' myths common to Gaelic and English-speaking communities. What's fascinating is that it has propagated to the network, where it lives on as a program that, or so the story goes, hunts for the unwary.\" -The Professor", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - Destroyer - Illicit", "pack_code": "om", "position": 20, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When you rez Grim, take 1 bad publicity. Subroutine Trash 1 program.", "stripped_title": "Grim", "text": "When you rez Grim, take 1 bad publicity.\n[subroutine] Trash 1 program.", "title": "Grim", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wotan_04030(Ice):
    '''
    Cost: 14
    Text: Subroutine End the run unless the Runner spends click click. Subroutine End the run unless the Runner pays 3 credits. Subroutine End the run unless the Runner trashes 1 installed program. Subroutine End the run unless the Runner suffers 1 core damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04030", "cost": 14, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "illustrator": "Christina Davis", "keywords": "Barrier - Bioroid", "pack_code": "st", "position": 30, "quantity": 3, "side_code": "corp", "strength": 10, "stripped_text": "Subroutine End the run unless the Runner spends click click. Subroutine End the run unless the Runner pays 3 credits. Subroutine End the run unless the Runner trashes 1 installed program. Subroutine End the run unless the Runner suffers 1 core damage.", "stripped_title": "Wotan", "text": "[subroutine] End the run unless the Runner spends [click][click].\n[subroutine] End the run unless the Runner pays 3[credit].\n[subroutine] End the run unless the Runner trashes 1 installed program.\n[subroutine] End the run unless the Runner suffers 1 core damage.", "title": "Wotan", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_swordsman_04033(Ice):
    '''
    Cost: 3
    Text: The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04033", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Writing a program that can pass the Turing test is easy. The Gibson-Akamatsu test is a higher bar, and the only AIs to clear it thus far have been the androids. Even some humans have been known to fail.", "illustrator": "Adam S. Doyle", "keywords": "Sentry - AP - Destroyer", "pack_code": "st", "position": 33, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.", "stripped_title": "Swordsman", "text": "The Runner cannot break subroutines on this ice using <strong>AI</strong> programs.\n[subroutine] Trash 1 installed <strong>AI</strong> program.\n[subroutine] Do 1 net damage.", "title": "Swordsman", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_muckraker_04035(Ice):
    '''
    Cost: 5
    Text: When you rez Muckraker, take 1 bad publicity. Subroutine Trace[1]. If successful, give the Runner 1 tag. Subroutine Trace[2]. If successful, give the Runner 1 tag. Subroutine Trace[3]. If successful, give the Runner 1 tag. Subroutine End the run if the Runner is tagged.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04035", "cost": 5, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Ed Mattinian", "keywords": "Sentry - Tracer - Illicit", "pack_code": "st", "position": 35, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When you rez Muckraker, take 1 bad publicity. Subroutine Trace[1]. If successful, give the Runner 1 tag. Subroutine Trace[2]. If successful, give the Runner 1 tag. Subroutine Trace[3]. If successful, give the Runner 1 tag. Subroutine End the run if the Runner is tagged.", "stripped_title": "Muckraker", "text": "When you rez Muckraker, take 1 bad publicity.\n[subroutine] Trace[1]. If successful, give the Runner 1 tag.\n[subroutine] Trace[2]. If successful, give the Runner 1 tag.\n[subroutine] Trace[3]. If successful, give the Runner 1 tag.\n[subroutine] End the run if the Runner is tagged.", "title": "Muckraker", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hudson_10_04051(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner cannot access more than 1 card during this run. Subroutine The Runner cannot access more than 1 card during this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04051", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "I'm not here to play games. The game is over.", "illustrator": "Wen Xiaodong", "keywords": "Code Gate - Bioroid", "pack_code": "mt", "position": 51, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner cannot access more than 1 card during this run. Subroutine The Runner cannot access more than 1 card during this run.", "stripped_title": "Hudson 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] The Runner cannot access more than 1 card during this run.\n[subroutine] The Runner cannot access more than 1 card during this run.", "title": "Hudson 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_snoop_04056(Ice):
    '''
    Cost: 6
    Text: When the Runner encounters Snoop, reveal all cards in the Runner's grip. Hosted power counter: Reveal all cards in the Runner's grip. Trash 1 of those cards. Subroutine Trace[3]. If successful, place 1 power counter on Snoop.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04056", "cost": 6, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Tracer", "pack_code": "mt", "position": 56, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "When the Runner encounters Snoop, reveal all cards in the Runner's grip. Hosted power counter: Reveal all cards in the Runner's grip. Trash 1 of those cards. Subroutine Trace[3]. If successful, place 1 power counter on Snoop.", "stripped_title": "Snoop", "text": "When the Runner encounters Snoop, reveal all cards in the Runner's grip.\n<strong>Hosted power counter:</strong> Reveal all cards in the Runner's grip. Trash 1 of those cards.\n[subroutine] Trace[3]. If successful, place 1 power counter on Snoop.", "title": "Snoop", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ireress_04057(Ice):
    '''
    Cost: 0
    Text: Ireress gains "Subroutine The Runner loses 1 credit" for each bad publicity you have.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04057", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Say it really fast.", "illustrator": "Chris Newman", "keywords": "Code Gate", "pack_code": "mt", "position": 57, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Ireress gains \"Subroutine The Runner loses 1 credit\" for each bad publicity you have.", "stripped_title": "Ireress", "text": "Ireress gains \"[subroutine] The Runner loses 1[credit]\" for each bad publicity you have.", "title": "Ireress", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_paper_wall_04059(Ice):
    '''
    Cost: 0
    Text: When the Runner fully breaks this ice, trash it. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04059", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It folds under pressure.", "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "mt", "position": 59, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "When the Runner fully breaks this ice, trash it. Subroutine End the run.", "stripped_title": "Paper Wall", "text": "When the Runner fully breaks this ice, trash it.\n[subroutine] End the run.", "title": "Paper Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_fenris_04071(Ice):
    '''
    Cost: 4
    Text: When you rez this ice, take 1 bad publicity. Subroutine Do 1 core damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04071", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "As reported cases of brain damage in veterans rise, mind/machine interface devices are subject to increased public scrutiny. That certain programs can cause irreparable harm to users has gone from fringe theory to accepted truth.", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - AP - Illicit", "pack_code": "tc", "position": 71, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "When you rez this ice, take 1 bad publicity. Subroutine Do 1 core damage. Subroutine End the run.", "stripped_title": "Fenris", "text": "When you rez this ice, take 1 bad publicity.\n[subroutine] Do 1 core damage.\n[subroutine] End the run.", "title": "Fenris", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tsurugi_04074(Ice):
    '''
    Cost: 6
    Text: Subroutine End the run unless the Corp pays 1 credit. Subroutine Do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04074", "cost": 6, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"It's ice so dangerous it has safety protocols. Think about that.\" -g00ru", "illustrator": "Adam S. Doyle", "keywords": "Sentry - AP", "pack_code": "tc", "position": 74, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine End the run unless the Corp pays 1 credit. Subroutine Do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage.", "stripped_title": "Tsurugi", "text": "[subroutine] End the run unless the Corp pays 1[credit].\n[subroutine] Do 1 net damage.\n[subroutine] Do 1 net damage.\n[subroutine] Do 1 net damage.", "title": "Tsurugi", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_rsvp_04077(Ice):
    '''
    Cost: 3
    Text: Subroutine The Runner cannot spend any credits for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04077", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "This ice disguises itself as a series of electronic transactions, tying up the runner's funds in a thousand or so non-existent purchases and refunds. The banks' system of holds and checks means that while not a single credit ever leaves their servers the runner has no available funds. RSVP also has the unfortunate side effect of being entirely legal\u2026strictly speaking.", "illustrator": "Christina Davis", "keywords": "Code Gate", "pack_code": "tc", "position": 77, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine The Runner cannot spend any credits for the remainder of this run.", "stripped_title": "RSVP", "text": "[subroutine] The Runner cannot spend any credits for the remainder of this run.", "title": "RSVP", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_curtain_wall_04078(Ice):
    '''
    Cost: 14
    Text: If Curtain Wall is the outermost piece of ice protecting a server, it has +4 strength. Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04078", "cost": 14, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "[subroutine] End the game.\nJust kidding.", "illustrator": "Adam S. Doyle", "keywords": "Barrier", "pack_code": "tc", "position": 78, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "If Curtain Wall is the outermost piece of ice protecting a server, it has +4 strength. Subroutine End the run. Subroutine End the run. Subroutine End the run.", "stripped_title": "Curtain Wall", "text": "If Curtain Wall is the outermost piece of ice protecting a server, it has +4 strength.\n[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Curtain Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_yagura_04093(Ice):
    '''
    Cost: 1
    Text: Subroutine Look at the top card of R&D. You may add that card to the bottom of R&D. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04093", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "The 'cyber-war' is a war of information, and in a war of information, advance warning can be as good as a killing blow. -Michael Muhama, Musings on Cybercrime", "illustrator": "Andrew Mar", "keywords": "Code Gate - AP", "pack_code": "fal", "position": 93, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine Look at the top card of R&D. You may add that card to the bottom of R&D. Subroutine Do 1 net damage.", "stripped_title": "Yagura", "text": "[subroutine] Look at the top card of R&D. You may add that card to the bottom of R&D.\n[subroutine] Do 1 net damage.", "title": "Yagura", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wraparound_04096(Ice):
    '''
    Cost: 2
    Text: While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04096", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"It can make a real fine roller coaster, provided you're properly stimmed up.\" -Noise", "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "fal", "position": 96, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.", "stripped_title": "Wraparound", "text": "While there are no installed <strong>fracter</strong> programs, this ice gets +7 strength.\n[subroutine] End the run.", "title": "Wraparound", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_gyri_labyrinth_04110(Ice):
    '''
    Cost: 2
    Text: Subroutine The Runner's maximum hand size is reduced by 2 until the beginning of the Corp's next turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04110", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Once inside, the only way out is through your own mind.", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate", "pack_code": "dt", "position": 110, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine The Runner's maximum hand size is reduced by 2 until the beginning of the Corp's next turn.", "stripped_title": "Gyri Labyrinth", "text": "[subroutine] The Runner's maximum hand size is reduced by 2 until the beginning of the Corp's next turn.", "title": "Gyri Labyrinth", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_shinobi_04115(Ice):
    '''
    Cost: 7
    Text: When you rez Shinobi, take 1 bad publicity. Subroutine Trace[1]. If successful, do 1 net damage. Subroutine Trace[2]. If successful, do 2 net damage. Subroutine Trace[3]. If successful, do 3 net damage and end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04115", "cost": 7, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Chris Newman", "keywords": "Sentry - Tracer - AP - Illicit", "pack_code": "dt", "position": 115, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When you rez Shinobi, take 1 bad publicity. Subroutine Trace[1]. If successful, do 1 net damage. Subroutine Trace[2]. If successful, do 2 net damage. Subroutine Trace[3]. If successful, do 3 net damage and end the run.", "stripped_title": "Shinobi", "text": "When you rez Shinobi, take 1 bad publicity.\n[subroutine] Trace[1]. If successful, do 1 net damage.\n[subroutine] Trace[2]. If successful, do 2 net damage.\n[subroutine] Trace[3]. If successful, do 3 net damage and end the run.", "title": "Shinobi", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_marker_04116(Ice):
    '''
    Cost: 0
    Text: Subroutine The next piece of ice the Runner encounters gains "Subroutine End the run." after all its other subroutines for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04116", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"It doesn't do anything in and of itself. It just marks you as an intruder and makes the next ice do all the work.\" -Kate \"Mac\" McCaffrey", "illustrator": "Ed Mattinian", "keywords": "Code Gate", "pack_code": "dt", "position": 116, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine The next piece of ice the Runner encounters gains \"Subroutine End the run.\" after all its other subroutines for the remainder of this run.", "stripped_title": "Marker", "text": "[subroutine] The next piece of ice the Runner encounters gains \"[subroutine] End the run.\" after all its other subroutines for the remainder of this run.", "title": "Marker", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hive_04117(Ice):
    '''
    Cost: 5
    Text: This ice loses 1 of its printed "Subroutine End the run." subroutines for each agenda point in your score area. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04117", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "dt", "position": 117, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "This ice loses 1 of its printed \"Subroutine End the run.\" subroutines for each agenda point in your score area. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run.", "stripped_title": "Hive", "text": "This ice loses 1 of its printed \"[subroutine] End the run.\" subroutines for each agenda point in your score area.\n[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Hive", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_quandary_04120(Ice):
    '''
    Cost: 1
    Text: Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04120", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It wants to have two subroutines when it grows up.", "illustrator": "Laura Wilson", "keywords": "Code Gate", "pack_code": "dt", "position": 120, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine End the run.", "stripped_title": "Quandary", "text": "[subroutine] End the run.", "title": "Quandary", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_inazuma_05016(Ice):
    '''
    Cost: 3
    Text: Subroutine During the next encounter this run, the Runner cannot break subroutines on the encountered ice. Subroutine The Runner cannot jack out this run until after their next encounter with a piece of ice begins.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05016", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Trapped in their own reality, a paralyzed runner cannot even jack out.", "illustrator": "Christina Davis", "keywords": "Code Gate", "pack_code": "hap", "position": 16, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine During the next encounter this run, the Runner cannot break subroutines on the encountered ice. Subroutine The Runner cannot jack out this run until after their next encounter with a piece of ice begins.", "stripped_title": "Inazuma", "text": "[subroutine] During the next encounter this run, the Runner cannot break subroutines on the encountered ice.\n[subroutine] The Runner cannot jack out this run until after their next encounter with a piece of ice begins.", "title": "Inazuma", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_komainu_05017(Ice):
    '''
    Cost: 5
    Text: When the Runner encounters this ice, it gains X "Subroutine Do 1 net damage." subroutines for the remainder of this run. X is equal to the number of cards in the grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05017", "cost": 5, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - AP", "pack_code": "hap", "position": 17, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "When the Runner encounters this ice, it gains X \"Subroutine Do 1 net damage.\" subroutines for the remainder of this run. X is equal to the number of cards in the grip.", "stripped_title": "Komainu", "text": "When the Runner encounters this ice, it gains X \"[subroutine] Do 1 net damage.\" subroutines for the remainder of this run. X is equal to the number of cards in the grip.", "title": "Komainu", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_pup_05018(Ice):
    '''
    Cost: 1
    Text: Subroutine Do 1 net damage unless the Runner pays 1 credit. Subroutine Do 1 net damage unless the Runner pays 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05018", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Yip Yip!", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - AP", "pack_code": "hap", "position": 18, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine Do 1 net damage unless the Runner pays 1 credit. Subroutine Do 1 net damage unless the Runner pays 1 credit.", "stripped_title": "Pup", "text": "[subroutine] Do 1 net damage unless the Runner pays 1[credit].\n[subroutine] Do 1 net damage unless the Runner pays 1[credit].", "title": "Pup", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_shiro_05019(Ice):
    '''
    Cost: 6
    Text: Subroutine Look at the top 3 cards of R&D and arrange them in any order. Subroutine You may pay 1 credit. If you do not, the Runner breaches R&D. They cannot access cards in the root of R&D during that breach.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05019", "cost": 6, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "When locked in a fortress in your own mind, be careful what door you open.", "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "hap", "position": 19, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Look at the top 3 cards of R&D and arrange them in any order. Subroutine You may pay 1 credit. If you do not, the Runner breaches R&D. They cannot access cards in the root of R&D during that breach.", "stripped_title": "Shiro", "text": "[subroutine] Look at the top 3 cards of R&D and arrange them in any order.\n[subroutine] You may pay 1[credit]. If you do not, the Runner breaches R&D. They cannot access cards in the root of R&D during that breach.", "title": "Shiro", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_susanoonomikoto_05020(Ice):
    '''
    Cost: 9
    Text: Subroutine If the attacked server is not Archives, the Runner moves to the outermost position of Archives instead of passing this ice. The Runner cannot jack out this run until after they encounter a piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05020", "cost": 9, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Certain areas of cyberspace are dominated by a single digital entity. Runners call them 'gods', and only a miracle can save those foolish enough to enter their domain.", "illustrator": "Falk", "keywords": "Sentry - Deflector", "pack_code": "hap", "position": 20, "quantity": 3, "side_code": "corp", "strength": 7, "stripped_text": "Subroutine If the attacked server is not Archives, the Runner moves to the outermost position of Archives instead of passing this ice. The Runner cannot jack out this run until after they encounter a piece of ice.", "stripped_title": "Susanoo-no-Mikoto", "text": "[subroutine] If the attacked server is not Archives, the Runner moves to the outermost position of Archives instead of passing this ice. The Runner cannot jack out this run until after they encounter a piece of ice.", "title": "Susanoo-no-Mikoto", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_guard_05024(Ice):
    '''
    Cost: 4
    Text: Guard cannot be bypassed. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05024", "cost": 4, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Out of the corner of his vision, a flash of light. He felt a thud as his grip on cyberspace loosened. Spider didn't like this. He should have bypassed the outer layer of ice by jacking in from the internal server. Another thud, and his whole frame shook with the resounding shockwave. He desperately reached for his shuriken\u2026", "illustrator": "Dan Maynard", "keywords": "Sentry", "pack_code": "hap", "position": 24, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Guard cannot be bypassed. Subroutine End the run.", "stripped_title": "Guard", "text": "Guard cannot be bypassed.\n[subroutine] End the run.", "title": "Guard", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_rainbow_05025(Ice):
    '''
    Cost: 3
    Text: Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05025", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "The annual review of ice as published by the NSCA consistently gives top marks to the ice that provide the most impact in relation to their size and upkeep cost. Critics of the NSCA point to the bounce ratio as the most important stat when judging ice.", "illustrator": "Ed Mattinian", "keywords": "Sentry - Code Gate - Barrier", "pack_code": "hap", "position": 25, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine End the run.", "stripped_title": "Rainbow", "text": "[subroutine] End the run.", "title": "Rainbow", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_next_silver_06002(Ice):
    '''
    Cost: 3
    Text: NEXT Silver gains "Subroutine End the run." for each rezzed piece of NEXT ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06002", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "The networking capabilities of the NEXT suite of ice are unparalleled.", "illustrator": "Ed Mattinian", "keywords": "Barrier - NEXT", "pack_code": "up", "position": 2, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "NEXT Silver gains \"Subroutine End the run.\" for each rezzed piece of NEXT ice.", "stripped_title": "NEXT Silver", "text": "NEXT Silver gains \"[subroutine] End the run.\" for each rezzed piece of <strong>NEXT</strong> ice.", "title": "NEXT Silver", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_lotus_field_06003(Ice):
    '''
    Cost: 5
    Text: The strength of this ice cannot be lowered. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06003", "cost": 5, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"Chi resonance mapping has created a whole new field of network security. It is unassailable perfection.\" -Akitaro Watanabe", "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "up", "position": 3, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "The strength of this ice cannot be lowered. Subroutine End the run.", "stripped_title": "Lotus Field", "text": "The strength of this ice cannot be lowered.\n[subroutine] End the run.", "title": "Lotus Field", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_taurus_06009(Ice):
    '''
    Cost: 5
    Text: Subroutine Trace[2]. If successful, trash 1 piece of hardware. If your trace strength is 5 or greater, trash 1 piece of hardware.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06009", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Taurus promised strength, but gave only rage.", "illustrator": "Shawn Ye Zhongyi", "keywords": "Sentry - Tracer", "pack_code": "up", "position": 9, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Trace[2]. If successful, trash 1 piece of hardware. If your trace strength is 5 or greater, trash 1 piece of hardware.", "stripped_title": "Taurus", "text": "[subroutine] Trace[2]. If successful, trash 1 piece of hardware. If your trace strength is 5 or greater, trash 1 piece of hardware.", "title": "Taurus", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_mother_goddess_06010(Ice):
    '''
    Cost: 4
    Text: Mother Goddess gains the subtypes of all other rezzed ice. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06010", "cost": 4, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "On the first day She breathed data into the void, and it hung suspended like jewelled stars. On the second day She spoke order into the data, and it flowed from rivulets into streams and from streams into mighty rivers. On the third day She gave independence to the order, and it ebbed and flowed according to its own accord. -The Cant of Helios", "illustrator": "Liiga Smilshkalne", "keywords": "Mythic", "pack_code": "up", "position": 10, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Mother Goddess gains the subtypes of all other rezzed ice. Subroutine End the run.", "stripped_title": "Mother Goddess", "text": "Mother Goddess gains the subtypes of all other rezzed ice.\n[subroutine] End the run.", "title": "Mother Goddess", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_galahad_06011(Ice):
    '''
    Cost: 2
    Text: When the Runner encounters Galahad, you may reveal up to 2 grail ice from HQ. For the remainder of this run, Galahad gains the subroutines of the revealed ice in the order of your choice. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06011", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 1, "flavor": "He who bears the shield of honor.", "illustrator": "Andreas Zafiratos", "keywords": "Barrier - Grail", "pack_code": "up", "position": 11, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "When the Runner encounters Galahad, you may reveal up to 2 grail ice from HQ. For the remainder of this run, Galahad gains the subroutines of the revealed ice in the order of your choice. Subroutine End the run.", "stripped_title": "Galahad", "text": "When the Runner encounters Galahad, you may reveal up to 2 <strong>grail</strong> ice from HQ. For the remainder of this run, Galahad gains the subroutines of the revealed ice in the order of your choice.\n[subroutine] End the run.", "title": "Galahad", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_information_overload_06027(Ice):
    '''
    Cost: 6
    Text: When the Runner encounters this ice, Trace[1]. If successful, give them 1 tag. This ice gains "Subroutine The Runner trashes 1 of their installed cards." for each tag the Runner has.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06027", "cost": 6, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Throw enough data at a runner and it ceases to have any meaning at all.", "illustrator": "Ed Mattinian", "keywords": "Sentry - Tracer", "pack_code": "tsb", "position": 27, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters this ice, Trace[1]. If successful, give them 1 tag. This ice gains \"Subroutine The Runner trashes 1 of their installed cards.\" for each tag the Runner has.", "stripped_title": "Information Overload", "text": "When the Runner encounters this ice, Trace[1]. If successful, give them 1 tag.\nThis ice gains \"[subroutine] The Runner trashes 1 of their installed cards.\" for each tag the Runner has.", "title": "Information Overload", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_iq_06041(Ice):
    '''
    Cost: 0
    Text: The rez cost of IQ is increased by 1 for each card in HQ. IQ has +1 strength for each card in HQ. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06041", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Created by merging the brainscans of over a hundred of the most intelligent people in Haas-Bioroid's cerebral database, its effectiveness is limited beither by its lack of imagination or the imagination of the sysops who employ it.", "illustrator": "Eko Puteh", "keywords": "Code Gate", "pack_code": "fc", "position": 41, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "The rez cost of IQ is increased by 1 for each card in HQ. IQ has +1 strength for each card in HQ. Subroutine End the run.", "stripped_title": "IQ", "text": "The rez cost of IQ is increased by 1 for each card in HQ.\nIQ has +1 strength for each card in HQ.\n[subroutine] End the run.", "title": "IQ", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_kitsune_06043(Ice):
    '''
    Cost: 2
    Text: Subroutine You may choose 1 card in HQ. If you do, the Runner breaches HQ. During this breach, the Runner cannot access cards in the root of HQ, and the first card they access must be the chosen card. When the breach ends, trash this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06043", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "There are those who believe the nine-tailed fox is an angel in disguise. And then there are those who have followed, and discovered her secret...", "illustrator": "Smirtouille", "keywords": "Mythic - Trap", "pack_code": "fc", "position": 43, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine You may choose 1 card in HQ. If you do, the Runner breaches HQ. During this breach, the Runner cannot access cards in the root of HQ, and the first card they access must be the chosen card. When the breach ends, trash this ice.", "stripped_title": "Kitsune", "text": "[subroutine] You may choose 1 card in HQ. If you do, the Runner breaches HQ. During this breach, the Runner cannot access cards in the root of HQ, and the first card they access must be the chosen card. When the breach ends, trash this ice.", "title": "Kitsune", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wendigo_06047(Ice):
    '''
    Cost: 2
    Text: Wendigo can be advanced. While Wendigo has an odd number of advancement tokens on it, it gains barrier and loses code gate. Subroutine Choose a program. The Runner cannot use the chosen program for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06047", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Wylie Beckert", "keywords": "Code Gate - Morph", "pack_code": "fc", "position": 47, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Wendigo can be advanced. While Wendigo has an odd number of advancement tokens on it, it gains barrier and loses code gate. Subroutine Choose a program. The Runner cannot use the chosen program for the remainder of this run.", "stripped_title": "Wendigo", "text": "Wendigo can be advanced.\nWhile Wendigo has an odd number of advancement tokens on it, it gains <strong>barrier</strong> and loses <strong>code gate</strong>.\n[subroutine] Choose a program. The Runner cannot use the chosen program for the remainder of this run.", "title": "Wendigo", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_lancelot_06051(Ice):
    '''
    Cost: 4
    Text: When the Runner encounters Lancelot, you may reveal up to 2 grail ice from HQ. For the remainder of this run, Lancelot gains the subroutines of the revealed ice in the order of your choice. Subroutine Trash 1 program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06051", "cost": 4, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 1, "flavor": "He who wields the sword of valor.", "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Grail - Destroyer", "pack_code": "fc", "position": 51, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "When the Runner encounters Lancelot, you may reveal up to 2 grail ice from HQ. For the remainder of this run, Lancelot gains the subroutines of the revealed ice in the order of your choice. Subroutine Trash 1 program.", "stripped_title": "Lancelot", "text": "When the Runner encounters Lancelot, you may reveal up to 2 <strong>grail</strong> ice from HQ. For the remainder of this run, Lancelot gains the subroutines of the revealed ice in the order of your choice.\n[subroutine] Trash 1 program.", "title": "Lancelot", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_architect_06061(Ice):
    '''
    Cost: 4
    Text: Players cannot trash this ice. Subroutine Look at the top 5 cards of R&D. You may install 1 of those cards, ignoring the install cost. Subroutine You may install 1 card from Archives or HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06061", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "<strong>Designed by 2012 World Champion Jeremy Zwirn</strong>", "illustrator": "Samuel R. Shimota", "keywords": "Sentry", "pack_code": "uao", "position": 61, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Players cannot trash this ice. Subroutine Look at the top 5 cards of R&D. You may install 1 of those cards, ignoring the install cost. Subroutine You may install 1 card from Archives or HQ.", "stripped_title": "Architect", "text": "Players cannot trash this ice.\n[subroutine] Look at the top 5 cards of R&D. You may install 1 of those cards, ignoring the install cost.\n[subroutine] You may install 1 card from Archives or HQ.", "title": "Architect", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ashigaru_06064(Ice):
    '''
    Cost: 9
    Text: Ashigaru gains "Subroutine End the run." for each card in HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06064", "cost": 9, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "The way past is to go a different way.", "illustrator": "Chris Newman", "keywords": "Barrier", "pack_code": "uao", "position": 64, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Ashigaru gains \"Subroutine End the run.\" for each card in HQ.", "stripped_title": "Ashigaru", "text": "Ashigaru gains \"[subroutine] End the run.\" for each card in HQ.", "title": "Ashigaru", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_mamba_06065(Ice):
    '''
    Cost: 6
    Text: Hosted power counter: Do 1 net damage. Use this ability only during a run. Subroutine Do 1 net damage. Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, place 1 power counter on Mamba.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06065", "cost": 6, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Eko Puteh", "keywords": "Sentry - Psi - AP", "pack_code": "uao", "position": 65, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Hosted power counter: Do 1 net damage. Use this ability only during a run. Subroutine Do 1 net damage. Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, place 1 power counter on Mamba.", "stripped_title": "Mamba", "text": "<strong>Hosted power counter:</strong> Do 1 net damage. Use this ability only during a run.\n[subroutine] Do 1 net damage.\n[subroutine] You and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, place 1 power counter on Mamba.", "title": "Mamba", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_universal_connectivity_fee_06067(Ice):
    '''
    Cost: 2
    Text: Subroutine If the Runner is not tagged, they lose 1 credit. If the Runner is tagged, they lose all credits in their credit pool and you trash this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06067", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"It's a small one-time fee, apparently. Only I've paid it seventeen times.\"", "illustrator": "Ed Mattinian", "keywords": "Trap", "pack_code": "uao", "position": 67, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine If the Runner is not tagged, they lose 1 credit. If the Runner is tagged, they lose all credits in their credit pool and you trash this ice.", "stripped_title": "Universal Connectivity Fee", "text": "[subroutine] If the Runner is not tagged, they lose 1[credit]. If the Runner is tagged, they lose all credits in their credit pool and you trash this ice.", "title": "Universal Connectivity Fee", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_changeling_06069(Ice):
    '''
    Cost: 5
    Text: Changeling can be advanced. While Changeling has an odd number of advancement tokens on it, it gains sentry and loses barrier. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06069", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Wylie Beckert", "keywords": "Barrier - Morph", "pack_code": "uao", "position": 69, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Changeling can be advanced. While Changeling has an odd number of advancement tokens on it, it gains sentry and loses barrier. Subroutine End the run.", "stripped_title": "Changeling", "text": "Changeling can be advanced.\nWhile Changeling has an odd number of advancement tokens on it, it gains <strong>sentry</strong> and loses <strong>barrier</strong>.\n[subroutine] End the run.", "title": "Changeling", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sagittarius_06082(Ice):
    '''
    Cost: 5
    Text: Subroutine Trace[2]. If successful, trash 1 program. If your trace strength is 5 or greater, trash 1 program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06082", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Sagittarius promised foresight, but brought only regret.", "illustrator": "Dan Maynard", "keywords": "Sentry - Tracer - Destroyer", "pack_code": "atr", "position": 82, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Trace[2]. If successful, trash 1 program. If your trace strength is 5 or greater, trash 1 program.", "stripped_title": "Sagittarius", "text": "[subroutine] Trace[2]. If successful, trash 1 program. If your trace strength is 5 or greater, trash 1 program.", "title": "Sagittarius", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_gemini_06084(Ice):
    '''
    Cost: 3
    Text: Subroutine Trace[2]. If successful, do 1 net damage. If your trace strength is 5 or greater, do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06084", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Gemini promised pleasure, but dealt only pain.", "illustrator": "Bruno Balixa", "keywords": "Sentry - Tracer - AP", "pack_code": "atr", "position": 84, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Trace[2]. If successful, do 1 net damage. If your trace strength is 5 or greater, do 1 net damage.", "stripped_title": "Gemini", "text": "[subroutine] Trace[2]. If successful, do 1 net damage. If your trace strength is 5 or greater, do 1 net damage.", "title": "Gemini", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_lycan_06089(Ice):
    '''
    Cost: 6
    Text: Lycan can be advanced. While Lycan has an odd number of advancement tokens on it, it gains code gate and loses sentry. Subroutine Trash 1 program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06089", "cost": 6, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"It's weird. I hit the server again and it was like a totally different piece of ice was waiting for me. Lost my root daemon. I shouldn't have nested them seven deep.\"", "illustrator": "Wylie Beckert", "keywords": "Sentry - Destroyer - Morph", "pack_code": "atr", "position": 89, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Lycan can be advanced. While Lycan has an odd number of advancement tokens on it, it gains code gate and loses sentry. Subroutine Trash 1 program.", "stripped_title": "Lycan", "text": "Lycan can be advanced.\nWhile Lycan has an odd number of advancement tokens on it, it gains <strong>code gate</strong> and loses <strong>sentry</strong>.\n[subroutine] Trash 1 program.", "title": "Lycan", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_merlin_06091(Ice):
    '''
    Cost: 6
    Text: When the Runner encounters Merlin, you may reveal up to 2 grail ice from HQ. For the remainder of this run, Merlin gains the subroutines of the revealed ice in the order of your choice. Subroutine Do 2 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06091", "cost": 6, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 1, "flavor": "He who holds the staff of wisdom.", "illustrator": "Andreas Zafiratos", "keywords": "Code Gate - Grail - AP", "pack_code": "atr", "position": 91, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters Merlin, you may reveal up to 2 grail ice from HQ. For the remainder of this run, Merlin gains the subroutines of the revealed ice in the order of your choice. Subroutine Do 2 net damage.", "stripped_title": "Merlin", "text": "When the Runner encounters Merlin, you may reveal up to 2 <strong>grail</strong> ice from HQ. For the remainder of this run, Merlin gains the subroutines of the revealed ice in the order of your choice.\n[subroutine] Do 2 net damage.", "title": "Merlin", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_errand_boy_06102(Ice):
    '''
    Cost: 4
    Text: Subroutine The Corp gains 1 credit or draws 1 card. Subroutine The Corp gains 1 credit or draws 1 card. Subroutine The Corp gains 1 credit or draws 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06102", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Recycling the energy entering the system via a run is both responsible and economical.", "illustrator": "Alexandra Douglass", "keywords": "Sentry", "pack_code": "ts", "position": 102, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Subroutine The Corp gains 1 credit or draws 1 card. Subroutine The Corp gains 1 credit or draws 1 card. Subroutine The Corp gains 1 credit or draws 1 card.", "stripped_title": "Errand Boy", "text": "[subroutine] The Corp gains 1[credit] or draws 1 card.\n[subroutine] The Corp gains 1[credit] or draws 1 card.\n[subroutine] The Corp gains 1[credit] or draws 1 card.", "title": "Errand Boy", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_markus_10_06104(Ice):
    '''
    Cost: 4
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner trashes 1 of their installed cards. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06104", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "The forge must never run cold.", "illustrator": "Dan Maynard", "keywords": "Barrier - Bioroid", "pack_code": "ts", "position": 104, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner trashes 1 of their installed cards. Subroutine End the run.", "stripped_title": "Markus 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] The Runner trashes 1 of their installed cards.\n[subroutine] End the run.", "title": "Markus 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_troll_06108(Ice):
    '''
    Cost: 1
    Text: When the Runner encounters Troll, Trace[2]. If successful, the Runner must lose click or end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06108", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "You gotta pay the troll toll to get in.", "illustrator": "Alexandr Elichev", "keywords": "Sentry", "pack_code": "ts", "position": 108, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When the Runner encounters Troll, Trace[2]. If successful, the Runner must lose click or end the run.", "stripped_title": "Troll", "text": "When the Runner encounters Troll, Trace[2]. If successful, the Runner must lose [click] or end the run.", "title": "Troll", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_virgo_06109(Ice):
    '''
    Cost: 4
    Text: Subroutine Trace[2]. If successful, give the Runner 1 tag. If your trace strength is 5 or greater, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06109", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Virgo promised love, but offered only jealousy.", "illustrator": "Madeline Boni", "keywords": "Sentry - Tracer", "pack_code": "ts", "position": 109, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Trace[2]. If successful, give the Runner 1 tag. If your trace strength is 5 or greater, give the Runner 1 tag.", "stripped_title": "Virgo", "text": "[subroutine] Trace[2]. If successful, give the Runner 1 tag. If your trace strength is 5 or greater, give the Runner 1 tag.", "title": "Virgo", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_excalibur_06111(Ice):
    '''
    Cost: 2
    Text: Subroutine The Runner cannot make another run this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06111", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "There drew he forth the brand Excalibur,\nAnd o'er him, drawing it, the winter moon,\nBrightening the skirts of a long cloud, ran forth\nAnd sparkled keen with frost against the hilt:\nFor all the haft twinkled with diamond sparks,\nMyriads of topaz-lights, and jacinth work\nOf subtlest jewellery. -Lord Tennyson", "illustrator": "Andreas Zafiratos", "keywords": "Mythic - Grail", "pack_code": "ts", "position": 111, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine The Runner cannot make another run this turn.", "stripped_title": "Excalibur", "text": "[subroutine] The Runner cannot make another run this turn.", "title": "Excalibur", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_asteroid_belt_07012(Ice):
    '''
    Cost: 9
    Text: Asteroid Belt can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07012", "cost": 9, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "His belt of stone did shake and shatter.", "illustrator": "Seage", "keywords": "Barrier", "pack_code": "oac", "position": 12, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "Asteroid Belt can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine End the run.", "stripped_title": "Asteroid Belt", "text": "Asteroid Belt can be advanced and its rez cost is lowered by 3 for each advancement token on it.\n[subroutine] End the run.", "title": "Asteroid Belt", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wormhole_07013(Ice):
    '''
    Cost: 9
    Text: Wormhole can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine Resolve a subroutine on another piece of rezzed ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07013", "cost": 9, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "As through the door of light he came.", "illustrator": "Seage", "keywords": "Code Gate", "pack_code": "oac", "position": 13, "quantity": 3, "side_code": "corp", "strength": 7, "stripped_text": "Wormhole can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine Resolve a subroutine on another piece of rezzed ice.", "stripped_title": "Wormhole", "text": "Wormhole can be advanced and its rez cost is lowered by 3 for each advancement token on it.\n[subroutine] Resolve a subroutine on another piece of rezzed ice.", "title": "Wormhole", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_nebula_07014(Ice):
    '''
    Cost: 9
    Text: Nebula can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine Trash 1 program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07014", "cost": 9, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "He bent his bow of stellar matter.", "illustrator": "Seage", "keywords": "Sentry - Destroyer", "pack_code": "oac", "position": 14, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Nebula can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine Trash 1 program.", "stripped_title": "Nebula", "text": "Nebula can be advanced and its rez cost is lowered by 3 for each advancement token on it.\n[subroutine] Trash 1 program.", "title": "Nebula", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_orion_07015(Ice):
    '''
    Cost: 15
    Text: Orion can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine Trash 1 program. Subroutine Resolve a subroutine on another piece of rezzed ice. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07015", "cost": 15, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "And seeking prey he then took aim.", "illustrator": "Seage", "keywords": "Sentry - Code Gate - Barrier", "pack_code": "oac", "position": 15, "quantity": 3, "side_code": "corp", "strength": 8, "stripped_text": "Orion can be advanced and its rez cost is lowered by 3 for each advancement token on it. Subroutine Trash 1 program. Subroutine Resolve a subroutine on another piece of rezzed ice. Subroutine End the run.", "stripped_title": "Orion", "text": "Orion can be advanced and its rez cost is lowered by 3 for each advancement token on it.\n[subroutine] Trash 1 program.\n[subroutine] Resolve a subroutine on another piece of rezzed ice.\n[subroutine] End the run.", "title": "Orion", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_builder_07016(Ice):
    '''
    Cost: 2
    Text: click: Move this piece of ice to the outermost position protecting any server. Subroutine Place 1 advancement token on a piece of ice protecting this server that can be advanced. Subroutine Place 1 advancement token on a piece of ice protecting this server that can be advanced.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07016", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate", "pack_code": "oac", "position": 16, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "click: Move this piece of ice to the outermost position protecting any server. Subroutine Place 1 advancement token on a piece of ice protecting this server that can be advanced. Subroutine Place 1 advancement token on a piece of ice protecting this server that can be advanced.", "stripped_title": "Builder", "text": "[click]: Move this piece of ice to the outermost position protecting any server.\n[subroutine] Place 1 advancement token on a piece of ice protecting this server that can be advanced.\n[subroutine] Place 1 advancement token on a piece of ice protecting this server that can be advanced.", "title": "Builder", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_checkpoint_07017(Ice):
    '''
    Cost: 4
    Text: When you rez Checkpoint, take 1 bad publicity. Subroutine Trace[5]. If successful, do 3 meat damage when this run is successful.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07017", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"I passed right through one once. It didn't seem to do anything at first. It wasn't until I jacked out that I realized they were busting down the door of my apartment.\" -Valencia Estevez", "illustrator": "Lili Ibrahim", "keywords": "Code Gate - Tracer - Illicit", "pack_code": "oac", "position": 17, "quantity": 3, "side_code": "corp", "strength": 7, "stripped_text": "When you rez Checkpoint, take 1 bad publicity. Subroutine Trace[5]. If successful, do 3 meat damage when this run is successful.", "stripped_title": "Checkpoint", "text": "When you rez Checkpoint, take 1 bad publicity.\n[subroutine] Trace[5]. If successful, do 3 meat damage when this run is successful.", "title": "Checkpoint", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_fire_wall_07018(Ice):
    '''
    Cost: 5
    Text: Fire Wall can be advanced and gains +1 strength for each advancement token on it. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07018", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"Definitely a literalist.\" -Liz Campbell, VP Project Security", "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "oac", "position": 18, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Fire Wall can be advanced and gains +1 strength for each advancement token on it. Subroutine End the run.", "stripped_title": "Fire Wall", "text": "Fire Wall can be advanced and gains +1 strength for each advancement token on it.\n[subroutine] End the run.", "title": "Fire Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_searchlight_07019(Ice):
    '''
    Cost: 1
    Text: Searchlight can be advanced. X is the number of advancement tokens on Searchlight. Subroutine Trace[X]. If successful, give the Runner 1 tag. Subroutine Trace[X]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07019", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "illustrator": "Simon Weaner", "keywords": "Sentry - Tracer - Observer", "pack_code": "oac", "position": 19, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Searchlight can be advanced. X is the number of advancement tokens on Searchlight. Subroutine Trace[X]. If successful, give the Runner 1 tag. Subroutine Trace[X]. If successful, give the Runner 1 tag.", "stripped_title": "Searchlight", "text": "Searchlight can be advanced. X is the number of advancement tokens on Searchlight.\n[subroutine]Trace[X]. If successful, give the Runner 1 tag.\n[subroutine]Trace[X]. If successful, give the Runner 1 tag.", "title": "Searchlight", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_next_gold_08011(Ice):
    '''
    Cost: 8
    Text: X is the number of rezzed NEXT ice. Subroutine Do X net damage. Subroutine Trash X programs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08011", "cost": 8, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"God in Heinlein. What's next, NEXT Platinum?\" -John Masanori", "illustrator": "Ed Mattinian", "keywords": "Sentry - NEXT - AP - Destroyer", "pack_code": "val", "position": 11, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "X is the number of rezzed NEXT ice. Subroutine Do X net damage. Subroutine Trash X programs.", "stripped_title": "NEXT Gold", "text": "X is the number of rezzed <strong>NEXT</strong> ice.\n[subroutine] Do X net damage.\n[subroutine] Trash X programs.", "title": "NEXT Gold", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_cortex_lock_08014(Ice):
    '''
    Cost: 2
    Text: Subroutine Do 1 net damage for each unused MU the Runner has.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08014", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "The more power a spike process can use, the harder it can hit. The really clever ones borrow the runner's own memory to iterate locally.", "illustrator": "Tadas Sidlauskas", "keywords": "Sentry - AP", "pack_code": "val", "position": 14, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Do 1 net damage for each unused MU the Runner has.", "stripped_title": "Cortex Lock", "text": "[subroutine] Do 1 net damage for each unused MU the Runner has.", "title": "Cortex Lock", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bandwidth_08016(Ice):
    '''
    Cost: 0
    Text: Subroutine Give the Runner 1 tag. If this run is successful, the Runner removes 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08016", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"It tracks you and logs you. If you get in you can just delete the log. But first you have to get in.\" -Gabriel Santiago", "illustrator": "Seage", "keywords": "Code Gate", "pack_code": "val", "position": 16, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Give the Runner 1 tag. If this run is successful, the Runner removes 1 tag.", "stripped_title": "Bandwidth", "text": "[subroutine] Give the Runner 1 tag. If this run is successful, the Runner removes 1 tag.", "title": "Bandwidth", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_negotiator_08019(Ice):
    '''
    Cost: 4
    Text: 2 credits: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Gain 2 credits. Subroutine Trash 1 installed program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08019", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"Negotiation is an art, so never negotiate when you can intimidate instead.\" -Thiago Reyes, VP Strategic Operations", "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Destroyer", "pack_code": "val", "position": 19, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "2 credits: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Gain 2 credits. Subroutine Trash 1 installed program.", "stripped_title": "Negotiator", "text": "2[credit]: Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Gain 2[credit].\n[subroutine] Trash 1 installed program.", "title": "Negotiator", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_turing_08033(Ice):
    '''
    Cost: 4
    Text: Turing has +3 strength while protecting a remote server. The Runner cannot use AI programs to break subroutines on Turing. Subroutine End the run unless the Runner spends click click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08033", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "Alan Turing laid the foundation for artificial intelligence by suggesting that you could teach a computer to be human.", "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "bb", "position": 33, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Turing has +3 strength while protecting a remote server. The Runner cannot use AI programs to break subroutines on Turing. Subroutine End the run unless the Runner spends click click click.", "stripped_title": "Turing", "text": "Turing has +3 strength while protecting a remote server.\nThe Runner cannot use <strong>AI</strong> programs to break subroutines on Turing.\n[subroutine] End the run unless the Runner spends [click][click][click].", "title": "Turing", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_crick_08034(Ice):
    '''
    Cost: 1
    Text: Crick has +3 strength while protecting Archives. Subroutine Install a card from Archives (paying its install cost).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08034", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Crick and his colleagues ushered in modern genetics by mapping the structure of DNA.", "illustrator": "Ed Mattinian", "keywords": "Code Gate", "pack_code": "bb", "position": 34, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Crick has +3 strength while protecting Archives. Subroutine Install a card from Archives (paying its install cost).", "stripped_title": "Crick", "text": "Crick has +3 strength while protecting Archives.\n[subroutine] Install a card from Archives (paying its install cost).", "title": "Crick", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_gutenberg_08037(Ice):
    '''
    Cost: 2
    Text: Gutenberg has +3 strength while protecting R&D. Subroutine Trace[7]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08037", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "Johannes Gutenberg ignited the first Information Revolution by inventing the movable-type printing press.", "illustrator": "Adam S. Doyle", "keywords": "Sentry - Tracer", "pack_code": "bb", "position": 37, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Gutenberg has +3 strength while protecting R&D. Subroutine Trace[7]. If successful, give the Runner 1 tag.", "stripped_title": "Gutenberg", "text": "Gutenberg has +3 strength while protecting R&D.\n[subroutine] Trace[7]. If successful, give the Runner 1 tag.", "title": "Gutenberg", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_meru_mati_08039(Ice):
    '''
    Cost: 2
    Text: Meru Mati has +3 strength while protecting HQ. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08039", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Meru Mati pushed the limits of physics by engineering the first buckyweave structure, a thousand-foot long wall.", "illustrator": "Micha\u0142 Mi\u0142kowski", "keywords": "Barrier", "pack_code": "bb", "position": 39, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Meru Mati has +3 strength while protecting HQ. Subroutine End the run.", "stripped_title": "Meru Mati", "text": "Meru Mati has +3 strength while protecting HQ.\n[subroutine] End the run.", "title": "Meru Mati", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_lab_dog_08052(Ice):
    '''
    Cost: 2
    Text: Subroutine The Runner trashes an installed piece of hardware. Trash Lab Dog.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08052", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Remember those FCC regulations about not creating harmful interference? No? Ah, before your time, I guess.\" -Cailan Heinrich, Senior Programmer", "illustrator": "Liiga Smilshkalne", "keywords": "Trap", "pack_code": "cc", "position": 52, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine The Runner trashes an installed piece of hardware. Trash Lab Dog.", "stripped_title": "Lab Dog", "text": "[subroutine] The Runner trashes an installed piece of hardware. Trash Lab Dog.", "title": "Lab Dog", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_clairvoyant_monitor_08055(Ice):
    '''
    Cost: 4
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, place 1 advancement token on an installed card and end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08055", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Seage", "keywords": "Code Gate - Psi", "pack_code": "cc", "position": 55, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, place 1 advancement token on an installed card and end the run.", "stripped_title": "Clairvoyant Monitor", "text": "[subroutine] You and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, place 1 advancement token on an installed card and end the run.", "title": "Clairvoyant Monitor", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_lockdown_08056(Ice):
    '''
    Cost: 0
    Text: Subroutine The Runner cannot draw cards for the remainder of this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08056", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"When your communications are disrupted, you are isolated from your resources. An attack will surely follow.\" -The Playbook", "illustrator": "Andreas Zafiratos", "keywords": "Code Gate", "pack_code": "cc", "position": 56, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine The Runner cannot draw cards for the remainder of this turn.", "stripped_title": "Lockdown", "text": "[subroutine] The Runner cannot draw cards for the remainder of this turn.", "title": "Lockdown", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_little_engine_08057(Ice):
    '''
    Cost: 5
    Text: Subroutine End the run. Subroutine End the run. Subroutine The Runner gains 5 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08057", "cost": 5, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"A sysop is not just a cog in the corporate machine. They have dreams\u2014and nightmares\u2014just like the rest of us.\" -Kate \"Mac\" McCaffrey", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate", "pack_code": "cc", "position": 57, "quantity": 3, "side_code": "corp", "strength": 7, "stripped_text": "Subroutine End the run. Subroutine End the run. Subroutine The Runner gains 5 credits.", "stripped_title": "Little Engine", "text": "[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] The Runner gains 5[credit].", "title": "Little Engine", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_quicksand_08060(Ice):
    '''
    Cost: 3
    Text: When the Runner encounters Quicksand, place 1 power counter on Quicksand. Quicksand has +1 strength for each power counter on it. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08060", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Dmitry Prosvirnin", "keywords": "Barrier", "pack_code": "cc", "position": 60, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "When the Runner encounters Quicksand, place 1 power counter on Quicksand. Quicksand has +1 strength for each power counter on it. Subroutine End the run.", "stripped_title": "Quicksand", "text": "When the Runner encounters Quicksand, place 1 power counter on Quicksand.\nQuicksand has +1 strength for each power counter on it.\n[subroutine] End the run.", "title": "Quicksand", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_pachinko_08076(Ice):
    '''
    Cost: 1
    Text: Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08076", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Pa-pa-pa-chinko!", "illustrator": "Donald Crank", "keywords": "Barrier", "pack_code": "uw", "position": 76, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged.", "stripped_title": "Pachinko", "text": "[subroutine] End the run if the Runner is tagged.\n[subroutine] End the run if the Runner is tagged.", "title": "Pachinko", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_spiderweb_08079(Ice):
    '''
    Cost: 4
    Text: Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08079", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"Let me tell you a secret. There's no such thing as impenetrable ice. It has to allow access, or else why is the server on the Network in the first place? But that doesn't mean they have to make it easy.\" -g00ru", "illustrator": "Laura Wilson", "keywords": "Barrier", "pack_code": "uw", "position": 79, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine End the run. Subroutine End the run. Subroutine End the run.", "stripped_title": "Spiderweb", "text": "[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Spiderweb", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_enforcer_10_08089(Ice):
    '''
    Cost: 1
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Do 1 core damage. Subroutine Trash 1 installed console. Subroutine Trash all installed virtual resources.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08089", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Bioroid - Destroyer - AP", "pack_code": "oh", "position": 89, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "As an additional cost to rez this ice, forfeit 1 agenda. Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Do 1 core damage. Subroutine Trash 1 installed console. Subroutine Trash all installed virtual resources.", "stripped_title": "Enforcer 1.0", "text": "As an additional cost to rez this ice, forfeit 1 agenda.\n<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Trash 1 installed program.\n[subroutine] Do 1 core damage.\n[subroutine] Trash 1 installed <strong>console</strong>.\n[subroutine] Trash all installed <strong>virtual</strong> resources.", "title": "Enforcer 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_its_a_trap_08090(Ice):
    '''
    Cost: 2
    Text: Whenever this ice is exposed, do 2 net damage. Subroutine The Runner trashes 1 of their installed cards. Trash this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08090", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "I warned you.", "illustrator": "Liiga Smilshkalne", "keywords": "Trap", "pack_code": "oh", "position": 90, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Whenever this ice is exposed, do 2 net damage. Subroutine The Runner trashes 1 of their installed cards. Trash this ice.", "stripped_title": "It's a Trap!", "text": "Whenever this ice is exposed, do 2 net damage.\n[subroutine] The Runner trashes 1 of their installed cards. Trash this ice.", "title": "It's a Trap!", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tour_guide_08118(Ice):
    '''
    Cost: 2
    Text: Tour Guide gains "Subroutine End the run." for each rezzed asset you have.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08118", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"Hello, and welcome to the Universe of Tomorrow! You could live for five-hundred years and not see all of the attractions I can tell you about.\"", "illustrator": "Ismael Bergara", "keywords": "Sentry", "pack_code": "uot", "position": 118, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Tour Guide gains \"Subroutine End the run.\" for each rezzed asset you have.", "stripped_title": "Tour Guide", "text": "Tour Guide gains \"[subroutine] End the run.\" for each rezzed asset you have.", "title": "Tour Guide", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_archangel_09013(Ice):
    '''
    Cost: 4
    Text: While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, you may pay 3 credits. If you do, they encounter it. Subroutine Trace[6]. If successful, add 1 installed Runner card to the grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09013", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate - Tracer - Ambush", "pack_code": "dad", "position": 13, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, you may pay 3 credits. If you do, they encounter it. Subroutine Trace[6]. If successful, add 1 installed Runner card to the grip.", "stripped_title": "Archangel", "text": "While the Runner is accessing this ice in R&D, they must reveal it.\nWhen the Runner accesses this ice anywhere except in Archives, you may pay 3[credit]. If you do, they encounter it.\n[subroutine] Trace[6]. If successful, add 1 installed Runner card to the grip.", "title": "Archangel", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_news_hound_09014(Ice):
    '''
    Cost: 2
    Text: If a current is active, News Hound gains "Subroutine End the run." after all its other subroutines. Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09014", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Most reporting these days can be done by AI. We just need the talent for the name recognition.\"", "illustrator": "Darren Waud", "keywords": "Sentry - Tracer", "pack_code": "dad", "position": 14, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "If a current is active, News Hound gains \"Subroutine End the run.\" after all its other subroutines. Subroutine Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "News Hound", "text": "If a <strong>current</strong> is active, News Hound gains \"[subroutine] End the run.\" after all its other subroutines.\n[subroutine] Trace[3]. If successful, give the Runner 1 tag.", "title": "News Hound", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_resistor_09015(Ice):
    '''
    Cost: 0
    Text: Resistor has +1 strength for each tag the Runner has. Subroutine Trace[4]. If successful, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09015", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"In the Olden Times, a 'resistor' was a vital component of practically all electronic equipment. You know, back when dinosaurs roamed the Earth.\" -Chaos Theory", "illustrator": "Mariusz Siergiejew", "keywords": "Barrier - Tracer", "pack_code": "dad", "position": 15, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Resistor has +1 strength for each tag the Runner has. Subroutine Trace[4]. If successful, end the run.", "stripped_title": "Resistor", "text": "Resistor has +1 strength for each tag the Runner has.\n[subroutine] Trace[4]. If successful, end the run.", "title": "Resistor", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_special_offer_09016(Ice):
    '''
    Cost: 1
    Text: Subroutine The Corp gains 5 credits. Trash Special Offer.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09016", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"If I didn't know better, I'd say they got the better end of that deal.\" -John Masanori", "illustrator": "Hannah Christenson", "keywords": "Trap - Advertisement", "pack_code": "dad", "position": 16, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine The Corp gains 5 credits. Trash Special Offer.", "stripped_title": "Special Offer", "text": "[subroutine] The Corp gains 5[credit]. Trash Special Offer.", "title": "Special Offer", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tldr_09017(Ice):
    '''
    Cost: 1
    Text: Subroutine When the Runner encounters the next piece of ice during this run, that ice gains a second copy of each subroutine on it (after the original subroutine) for the remainder of the encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09017", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "//tl;dr duplicate the subs on the next piece of ice", "illustrator": "Ed Mattinian", "keywords": "Code Gate", "pack_code": "dad", "position": 17, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine When the Runner encounters the next piece of ice during this run, that ice gains a second copy of each subroutine on it (after the original subroutine) for the remainder of the encounter.", "stripped_title": "TL;DR", "text": "[subroutine] When the Runner encounters the next piece of ice during this run, that ice gains a second copy of each subroutine on it (after the original subroutine) for the remainder of the encounter.", "title": "TL;DR", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_turnpike_09018(Ice):
    '''
    Cost: 2
    Text: When the Runner encounters this ice, they lose 1 credit. Subroutine Trace[5]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09018", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Stay out of the fast lanes! If speed's your only concern, you're already tagged and halfway to fragged.\" -g00ru", "illustrator": "Donald Crank", "keywords": "Sentry - Tracer", "pack_code": "dad", "position": 18, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When the Runner encounters this ice, they lose 1 credit. Subroutine Trace[5]. If successful, give the Runner 1 tag.", "stripped_title": "Turnpike", "text": "When the Runner encounters this ice, they lose 1[credit].\n[subroutine] Trace[5]. If successful, give the Runner 1 tag.", "title": "Turnpike", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_assassin_09028(Ice):
    '''
    Cost: 7
    Text: Subroutine Trace[5]. If successful, do 3 net damage. Subroutine Trace[4]. If successful, trash 1 program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09028", "cost": 7, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Bounce rate is a well-understood measure of ice strength. But it is not the only measure.", "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Destroyer - AP - Tracer", "pack_code": "dad", "position": 28, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Trace[5]. If successful, do 3 net damage. Subroutine Trace[4]. If successful, trash 1 program.", "stripped_title": "Assassin", "text": "[subroutine] Trace[5]. If successful, do 3 net damage.\n[subroutine] Trace[4]. If successful, trash 1 program.", "title": "Assassin", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_vikram_10_10012(Ice):
    '''
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner cannot use programs for the remainder of this run. Subroutine Trace[4]. If successful, do 1 core damage. Subroutine Trace[4]. If successful, do 1 core damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10012", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Donald Crank", "keywords": "Sentry - Bioroid - Tracer - AP", "pack_code": "kg", "position": 12, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner cannot use programs for the remainder of this run. Subroutine Trace[4]. If successful, do 1 core damage. Subroutine Trace[4]. If successful, do 1 core damage.", "stripped_title": "Vikram 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] The Runner cannot use programs for the remainder of this run.\n[subroutine] Trace[4]. If successful, do 1 core damage.\n[subroutine] Trace[4]. If successful, do 1 core damage.", "title": "Vikram 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_interrupt_0_10016(Ice):
    '''
    Cost: 2
    Text: Subroutine For the remainder of this run, as an additional cost to use an icebreaker ability to break subroutines, the Runner must pay 1 credit. Subroutine For the remainder of this run, as an additional cost to use an icebreaker ability to break subroutines, the Runner must pay 1 credit
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10016", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "kg", "position": 16, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine For the remainder of this run, as an additional cost to use an icebreaker ability to break subroutines, the Runner must pay 1 credit. Subroutine For the remainder of this run, as an additional cost to use an icebreaker ability to break subroutines, the Runner must pay 1 credit", "stripped_title": "Interrupt 0", "text": "[subroutine] For the remainder of this run, as an additional cost to use an <strong>icebreaker</strong> ability to break subroutines, the Runner must pay 1[credit].\n[subroutine] For the remainder of this run, as an additional cost to use an <strong>icebreaker</strong> ability to break subroutines, the Runner must pay 1[credit]", "title": "Interrupt 0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_harvester_10032(Ice):
    '''
    Cost: 1
    Text: Subroutine The Runner draws 3 cards and then discards down to their maximum hand size. Subroutine The Runner draws 3 cards and then discards down to their maximum hand size.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10032", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"We can help others, yet also help ourselves.\" -Soraiya Suresh, VP Public Programs", "illustrator": "Ed Mattinian", "keywords": "Code Gate", "pack_code": "bf", "position": 32, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine The Runner draws 3 cards and then discards down to their maximum hand size. Subroutine The Runner draws 3 cards and then discards down to their maximum hand size.", "stripped_title": "Harvester", "text": "[subroutine] The Runner draws 3 cards and then discards down to their maximum hand size.\n[subroutine] The Runner draws 3 cards and then discards down to their maximum hand size.", "title": "Harvester", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bailiff_10056(Ice):
    '''
    Cost: 2
    Text: Whenever the Runner breaks a subroutine on Bailiff, gain 1 credit. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10056", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Efficiency means profiting from things everyone was doing anyway.", "illustrator": "Andreas Zafiratos", "keywords": "Barrier", "pack_code": "dag", "position": 56, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Whenever the Runner breaks a subroutine on Bailiff, gain 1 credit. Subroutine End the run.", "stripped_title": "Bailiff", "text": "Whenever the Runner breaks a subroutine on Bailiff, gain 1[credit].\n[subroutine] End the run.", "title": "Bailiff", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_upayoga_10069(Ice):
    '''
    Cost: 3
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, the Runner loses 2 credits. Subroutine Resolve a subroutine on a piece of rezzed psi ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10069", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"Connect two truths. Connect two programs. All is one.\"", "illustrator": "Adam S. Doyle", "keywords": "Code Gate - Psi", "pack_code": "si", "position": 69, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, the Runner loses 2 credits. Subroutine Resolve a subroutine on a piece of rezzed psi ice.", "stripped_title": "Upayoga", "text": "[subroutine] You and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, the Runner loses 2[credit].\n[subroutine] Resolve a subroutine on a piece of rezzed <strong>psi</strong> ice.", "title": "Upayoga", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_cobra_10074(Ice):
    '''
    Cost: 4
    Text: Subroutine Trash 1 program. Subroutine Do 2 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10074", "cost": 4, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "The naja naja is the king of all serpents.", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - Destroyer - AP", "pack_code": "si", "position": 74, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Subroutine Trash 1 program. Subroutine Do 2 net damage.", "stripped_title": "Cobra", "text": "[subroutine] Trash 1 program.\n[subroutine] Do 2 net damage.", "title": "Cobra", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_brainstorm_10086(Ice):
    '''
    Cost: 9
    Text: When the Runner encounters this ice, it gains X "Subroutine Do 1 core damage." subroutines for the remainder of this run. X is equal to the number of cards in the grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10086", "cost": 9, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "has anyone heard from StatiX lately?\n-post on Members Only newsgroup", "illustrator": "Caleb Souza", "keywords": "Sentry - AP", "pack_code": "tlm", "position": 86, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "When the Runner encounters this ice, it gains X \"Subroutine Do 1 core damage.\" subroutines for the remainder of this run. X is equal to the number of cards in the grip.", "stripped_title": "Brainstorm", "text": "When the Runner encounters this ice, it gains X \"[subroutine] Do 1 core damage.\" subroutines for the remainder of this run. X is equal to the number of cards in the grip.", "title": "Brainstorm", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ravana_10_10087(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Resolve 1 subroutine on another rezzed bioroid ice. Subroutine Resolve 1 subroutine on another rezzed bioroid ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10087", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "illustrator": "Ethan Patrick Harris", "keywords": "Code Gate - Bioroid", "pack_code": "tlm", "position": 87, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Resolve 1 subroutine on another rezzed bioroid ice. Subroutine Resolve 1 subroutine on another rezzed bioroid ice.", "stripped_title": "Ravana 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Resolve 1 subroutine on another rezzed <strong>bioroid</strong> ice.\n[subroutine] Resolve 1 subroutine on another rezzed <strong>bioroid</strong> ice.", "title": "Ravana 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_chetana_10089(Ice):
    '''
    Cost: 4
    Text: Subroutine Each player gains 2 credits. Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, do 1 net damage for each card in the Runner's grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10089", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"Feel your consciousness expand and touch his. Now destroy it.\"", "illustrator": "Adam S. Doyle", "keywords": "Sentry - AP - Psi", "pack_code": "tlm", "position": 89, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Each player gains 2 credits. Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, do 1 net damage for each card in the Runner's grip.", "stripped_title": "Chetana", "text": "[subroutine] Each player gains 2[credit].\n[subroutine] You and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, do 1 net damage for each card in the Runner's grip.", "title": "Chetana", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_waiver_10091(Ice):
    '''
    Cost: 5
    Text: Subroutine Trace[5]. If successful, the Runner reveals the grip. Trash each card revealed this way with a play or install cost of X or less. X is equal to the amount by which your trace strength exceeded the Runner's link strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10091", "cost": 5, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"It's amazing how small we can write the fine print these days.\"", "illustrator": "Lili Ibrahim", "keywords": "Code Gate - Tracer", "pack_code": "tlm", "position": 91, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Trace[5]. If successful, the Runner reveals the grip. Trash each card revealed this way with a play or install cost of X or less. X is equal to the amount by which your trace strength exceeded the Runner's link strength.", "stripped_title": "Waiver", "text": "[subroutine] Trace[5]. If successful, the Runner reveals the grip. Trash each card revealed this way with a play or install cost of X or less. X is equal to the amount by which your trace strength exceeded the Runner's link strength.", "title": "Waiver", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_red_tape_10093(Ice):
    '''
    Cost: 2
    Text: Subroutine All ice has +3 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10093", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Bureaucracy. Noun. A shell-game played by the rich with prosperity as the ball. The trick is that there is no ball.\n-The Anarch's Dictionary, Volume Who's Counting?", "illustrator": "Tim Durning", "keywords": "Code Gate", "pack_code": "tlm", "position": 93, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine All ice has +3 strength for the remainder of this run.", "stripped_title": "Red Tape", "text": "[subroutine] All ice has +3 strength for the remainder of this run.", "title": "Red Tape", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_vanilla_10095(Ice):
    '''
    Cost: 0
    Text: Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10095", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "A brand new invention.", "illustrator": "Seage", "keywords": "Barrier", "pack_code": "tlm", "position": 95, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine End the run.", "stripped_title": "Vanilla", "text": "[subroutine] End the run.", "title": "Vanilla", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_magnet_10103(Ice):
    '''
    Cost: 3
    Text: When you rez this ice, choose 1 installed program hosted on a piece of ice. Move that program onto this ice. Each hosted program loses all abilities. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10103", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "\"When the enemy has mastered the battlefield, change the battlefield.\" -The Playbook", "illustrator": "David Keen", "keywords": "Code Gate", "pack_code": "ftm", "position": 103, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When you rez this ice, choose 1 installed program hosted on a piece of ice. Move that program onto this ice. Each hosted program loses all abilities. Subroutine End the run.", "stripped_title": "Magnet", "text": "When you rez this ice, choose 1 installed program hosted on a piece of ice. Move that program onto this ice.\nEach hosted program loses all abilities.\n[subroutine] End the run.", "title": "Magnet", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_fairchild_10_11010(Ice):
    '''
    Cost: 1
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner must pay 1 credit or trash 1 of their installed cards. Subroutine The Runner must pay 1 credit or trash 1 of their installed cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11010", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "I foresee the end of all things...", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate - Bioroid", "pack_code": "23s", "position": 10, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner must pay 1 credit or trash 1 of their installed cards. Subroutine The Runner must pay 1 credit or trash 1 of their installed cards.", "stripped_title": "Fairchild 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] The Runner must pay 1[credit] or trash 1 of their installed cards.\n[subroutine] The Runner must pay 1[credit] or trash 1 of their installed cards.", "title": "Fairchild 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sherlock_20_11011(Ice):
    '''
    Cost: 7
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Trace[4]. If successful, add 1 installed program to the bottom of the Runner's stack. Subroutine Trace[4]. If successful, add 1 installed program to the bottom of the Runner's stack. Subroutine Give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11011", "cost": 7, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Hannah Christenson", "keywords": "Sentry - Bioroid - Tracer", "pack_code": "23s", "position": 11, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Trace[4]. If successful, add 1 installed program to the bottom of the Runner's stack. Subroutine Trace[4]. If successful, add 1 installed program to the bottom of the Runner's stack. Subroutine Give the Runner 1 tag.", "stripped_title": "Sherlock 2.0", "text": "<strong>Lose [click][click]:</strong> Break up to 2 subroutines on this ice. Only the Runner can use this ability.\n[subroutine] Trace[4]. If successful, add 1 installed program to the bottom of the Runner's stack.\n[subroutine] Trace[4]. If successful, add 1 installed program to the bottom of the Runner's stack.\n[subroutine] Give the Runner 1 tag.", "title": "Sherlock 2.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_chrysalis_11013(Ice):
    '''
    Cost: 3
    Text: While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, they encounter it. Subroutine Do 2 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11013", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Donald Crank", "keywords": "Sentry - AP", "pack_code": "23s", "position": 13, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, they encounter it. Subroutine Do 2 net damage.", "stripped_title": "Chrysalis", "text": "While the Runner is accessing this ice in R&D, they must reveal it.\nWhen the Runner accesses this ice anywhere except in Archives, they encounter it.\n[subroutine] Do 2 net damage.", "title": "Chrysalis", "trash_cost": 1, "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_fairchild_20_11031(Ice):
    '''
    Cost: 4
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine The Runner must pay 2 credits or trash 1 of their installed cards. Subroutine The Runner must pay 2 credits or trash 1 of their installed cards. Subroutine Do 1 core damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11031", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "To threaten my treasures is to incur my wrath.", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate - Bioroid - AP", "pack_code": "bm", "position": 31, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine The Runner must pay 2 credits or trash 1 of their installed cards. Subroutine The Runner must pay 2 credits or trash 1 of their installed cards. Subroutine Do 1 core damage.", "stripped_title": "Fairchild 2.0", "text": "<strong>Lose [click][click]:</strong> Break up to 2 subroutines on this ice. Only the Runner can use this ability.\n[subroutine] The Runner must pay 2[credit] or trash 1 of their installed cards.\n[subroutine] The Runner must pay 2[credit] or trash 1 of their installed cards.\n[subroutine] Do 1 core damage.", "title": "Fairchild 2.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_aiki_11032(Ice):
    '''
    Cost: 1
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, the Runner draws 2 cards. Subroutine Do 1 net damage. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11032", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "First, blend with the attacker. Then, control the attack.", "illustrator": "BalanceSheet", "keywords": "Code Gate - Psi - AP", "pack_code": "bm", "position": 32, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, the Runner draws 2 cards. Subroutine Do 1 net damage. Subroutine Do 1 net damage.", "stripped_title": "Aiki", "text": "[subroutine] You and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, the Runner draws 2 cards.\n[subroutine] Do 1 net damage.\n[subroutine] Do 1 net damage.", "title": "Aiki", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_fairchild_30_11049(Ice):
    '''
    Cost: 6
    Text: Lose click click click: Break up to 3 subroutines on this ice. Only the Runner can use this ability. Subroutine The Runner must pay 3 credits or trash 1 of their installed cards. Subroutine The Runner must pay 3 credits or trash 1 of their installed cards. Subroutine Do 1 core damage or end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11049", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "In battle, I take half the slain.", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate - Bioroid - AP", "pack_code": "es", "position": 49, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Lose click click click: Break up to 3 subroutines on this ice. Only the Runner can use this ability. Subroutine The Runner must pay 3 credits or trash 1 of their installed cards. Subroutine The Runner must pay 3 credits or trash 1 of their installed cards. Subroutine Do 1 core damage or end the run.", "stripped_title": "Fairchild 3.0", "text": "<strong>Lose [click][click][click]:</strong> Break up to 3 subroutines on this ice. Only the Runner can use this ability.\n[subroutine] The Runner must pay 3[credit] or trash 1 of their installed cards.\n[subroutine] The Runner must pay 3[credit] or trash 1 of their installed cards.\n[subroutine] Do 1 core damage or end the run.", "title": "Fairchild 3.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_dna_tracker_11053(Ice):
    '''
    Cost: 8
    Text: Subroutine Do 1 net damage. The Runner loses 2 credits. Subroutine Do 1 net damage. The Runner loses 2 credits. Subroutine Do 1 net damage. The Runner loses 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11053", "cost": 8, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "When your ID is flagged with your genetic profile, \"privacy\"  doesn't really exist.", "illustrator": "A. Jones", "keywords": "Code Gate - AP", "pack_code": "es", "position": 53, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "Subroutine Do 1 net damage. The Runner loses 2 credits. Subroutine Do 1 net damage. The Runner loses 2 credits. Subroutine Do 1 net damage. The Runner loses 2 credits.", "stripped_title": "DNA Tracker", "text": "[subroutine] Do 1 net damage. The Runner loses 2[credit].\n[subroutine] Do 1 net damage. The Runner loses 2[credit].\n[subroutine] Do 1 net damage. The Runner loses 2[credit].", "title": "DNA Tracker", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_data_ward_11075(Ice):
    '''
    Cost: 6
    Text: When the Runner encounters this ice, they take 1 tag unless they pay 3 credits. Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11075", "cost": 6, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Caroline Elizabeth Huss", "keywords": "Barrier", "pack_code": "in", "position": 75, "quantity": 3, "side_code": "corp", "strength": 8, "stripped_text": "When the Runner encounters this ice, they take 1 tag unless they pay 3 credits. Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged. Subroutine End the run if the Runner is tagged.", "stripped_title": "Data Ward", "text": "When the Runner encounters this ice, they take 1 tag unless they pay 3[credit].\n[subroutine] End the run if the Runner is tagged.\n[subroutine] End the run if the Runner is tagged.\n[subroutine] End the run if the Runner is tagged.\n[subroutine] End the run if the Runner is tagged.", "title": "Data Ward", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bulwark_11078(Ice):
    '''
    Cost: 10
    Text: When you rez this ice, take 1 bad publicity. When the Runner encounters this ice, gain 2 credits if there is an installed AI program. Subroutine The Runner trashes 1 installed program. Subroutine Gain 2 credits. End the run. Subroutine Gain 2 credits. End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11078", "cost": 10, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Mariusz Siergiejew", "keywords": "Barrier - Illicit", "pack_code": "in", "position": 78, "quantity": 3, "side_code": "corp", "strength": 8, "stripped_text": "When you rez this ice, take 1 bad publicity. When the Runner encounters this ice, gain 2 credits if there is an installed AI program. Subroutine The Runner trashes 1 installed program. Subroutine Gain 2 credits. End the run. Subroutine Gain 2 credits. End the run.", "stripped_title": "Bulwark", "text": "When you rez this ice, take 1 bad publicity.\nWhen the Runner encounters this ice, gain 2[credit] if there is an installed <strong>AI</strong> program.\n[subroutine] The Runner trashes 1 installed program.\n[subroutine] Gain 2[credit]. End the run.\n[subroutine] Gain 2[credit]. End the run.", "title": "Bulwark", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_fairchild_11089(Ice):
    '''
    Cost: 9
    Text: Subroutine End the run unless the Runner pays 4 credits. Subroutine End the run unless the Runner pays 4 credits. Subroutine End the run unless the Runner trashes 1 of their installed cards. Subroutine End the run unless the Runner suffers 1 core damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11089", "cost": 9, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate - Bioroid - AP", "pack_code": "ml", "position": 89, "quantity": 3, "side_code": "corp", "strength": 8, "stripped_text": "Subroutine End the run unless the Runner pays 4 credits. Subroutine End the run unless the Runner pays 4 credits. Subroutine End the run unless the Runner trashes 1 of their installed cards. Subroutine End the run unless the Runner suffers 1 core damage.", "stripped_title": "Fairchild", "text": "[subroutine] End the run unless the Runner pays 4[credit].\n[subroutine] End the run unless the Runner pays 4[credit].\n[subroutine] End the run unless the Runner trashes 1 of their installed cards.\n[subroutine] End the run unless the Runner suffers 1 core damage.", "title": "Fairchild", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_mind_game_11092(Ice):
    '''
    Cost: 0
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, choose another server. The Runner moves to the outermost position of that server instead of passing this ice. For the remainder of this run, the Runner must add 1 installed Runner card to the bottom of their stack as an additional cost to jack out. The Runner may jack out.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11092", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Bon Bernardo", "keywords": "Code Gate - Psi - Deflector", "pack_code": "ml", "position": 92, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, choose another server. The Runner moves to the outermost position of that server instead of passing this ice. For the remainder of this run, the Runner must add 1 installed Runner card to the bottom of their stack as an additional cost to jack out. The Runner may jack out.", "stripped_title": "Mind Game", "text": "[subroutine] You and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, choose another server. The Runner moves to the outermost position of that server instead of passing this ice. For the remainder of this run, the Runner must add 1 installed Runner card to the bottom of their stack as an additional cost to jack out. The Runner may jack out.", "title": "Mind Game", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ip_block_11094(Ice):
    '''
    Cost: 2
    Text: When the Runner encounters this ice, give them 1 tag if there is an installed AI program. Subroutine Trace[3]. If successful, give the Runner 1 tag. Subroutine End the run if the Runner is tagged.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11094", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "//Connection Terminated", "illustrator": "Alexandr Elichev", "keywords": "Barrier - Tracer", "pack_code": "ml", "position": 94, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters this ice, give them 1 tag if there is an installed AI program. Subroutine Trace[3]. If successful, give the Runner 1 tag. Subroutine End the run if the Runner is tagged.", "stripped_title": "IP Block", "text": "When the Runner encounters this ice, give them 1 tag if there is an installed <strong>AI</strong> program.\n[subroutine] Trace[3]. If successful, give the Runner 1 tag.\n[subroutine] End the run if the Runner is tagged.", "title": "IP Block", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_thoth_11095(Ice):
    '''
    Cost: 7
    Text: When the Runner encounters this ice, give them 1 tag. Subroutine Trace[4]. If successful, do 1 net damage for each tag the Runner has. Subroutine Trace[4]. If successful, the Runner loses 1 credit for each tag they have.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11095", "cost": 7, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "Truth like the sunlight shines above all.", "illustrator": "Kari Guenther", "keywords": "Sentry - Tracer", "pack_code": "ml", "position": 95, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "When the Runner encounters this ice, give them 1 tag. Subroutine Trace[4]. If successful, do 1 net damage for each tag the Runner has. Subroutine Trace[4]. If successful, the Runner loses 1 credit for each tag they have.", "stripped_title": "Thoth", "text": "When the Runner encounters this ice, give them 1 tag.\n[subroutine] Trace[4]. If successful, do 1 net damage for each tag the Runner has.\n[subroutine] Trace[4]. If successful, the Runner loses 1[credit] for each tag they have.", "title": "Thoth", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_mausolus_11097(Ice):
    '''
    Cost: 4
    Text: You can advance this ice. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 3 credits. Subroutine Do 1 net damage. If there are 3 or more hosted advancement counters, instead do 3 net damage. Subroutine Give the Runner 1 tag. If there are 3 or more hosted advancement counters, instead give the Runner 1 tag and end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11097", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Yog Joshi", "keywords": "Code Gate - AP", "pack_code": "ml", "position": 97, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "You can advance this ice. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 3 credits. Subroutine Do 1 net damage. If there are 3 or more hosted advancement counters, instead do 3 net damage. Subroutine Give the Runner 1 tag. If there are 3 or more hosted advancement counters, instead give the Runner 1 tag and end the run.", "stripped_title": "Mausolus", "text": "You can advance this ice.\n[subroutine] Gain 1[credit]. If there are 3 or more hosted advancement counters, instead gain 3[credit].\n[subroutine] Do 1 net damage. If there are 3 or more hosted advancement counters, instead do 3 net damage.\n[subroutine] Give the Runner 1 tag. If there are 3 or more hosted advancement counters, instead give the Runner 1 tag and end the run.", "title": "Mausolus", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sapper_11098(Ice):
    '''
    Cost: 3
    Text: While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, they encounter it. Subroutine Trash 1 installed program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11098", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "There is a special place in hell for the first person who mined cyberspace.", "illustrator": "Adam S. Doyle", "keywords": "Sentry - Destroyer", "pack_code": "ml", "position": 98, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, they encounter it. Subroutine Trash 1 installed program.", "stripped_title": "Sapper", "text": "While the Runner is accessing this ice in R&D, they must reveal it.\nWhen the Runner accesses this ice anywhere except in Archives, they encounter it.\n[subroutine] Trash 1 installed program.", "title": "Sapper", "trash_cost": 2, "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_chiyashi_11112(Ice):
    '''
    Cost: 12
    Text: Whenever the Runner breaks a subroutine on Chiyashi while there is an AI installed, trash the top 2 cards of the Runner's stack. Subroutine Do 2 net damage. Subroutine Do 2 net damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11112", "cost": 12, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"Ice is not meant to kill; just slow or cripple the Runner. Killing is my job.\" - Tori Hanz\u014d", "illustrator": "Yog Joshi", "keywords": "Barrier - AP", "pack_code": "qu", "position": 112, "quantity": 3, "side_code": "corp", "strength": 8, "stripped_text": "Whenever the Runner breaks a subroutine on Chiyashi while there is an AI installed, trash the top 2 cards of the Runner's stack. Subroutine Do 2 net damage. Subroutine Do 2 net damage. Subroutine End the run.", "stripped_title": "Chiyashi", "text": "Whenever the Runner breaks a subroutine on Chiyashi while there is an <strong>AI</strong> installed, trash the top 2 cards of the Runner's stack.\n[subroutine] Do 2 net damage.\n[subroutine] Do 2 net damage.\n[subroutine] End the run.", "title": "Chiyashi", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_herald_11115(Ice):
    '''
    Cost: 2
    Text: While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, they encounter it. Subroutine Gain 2 credits. Subroutine You may pay up to 2 credits to place that many advancement counters on 1 installed card you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11115", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "qu", "position": 115, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "While the Runner is accessing this ice in R&D, they must reveal it. When the Runner accesses this ice anywhere except in Archives, they encounter it. Subroutine Gain 2 credits. Subroutine You may pay up to 2 credits to place that many advancement counters on 1 installed card you can advance.", "stripped_title": "Herald", "text": "While the Runner is accessing this ice in R&D, they must reveal it.\nWhen the Runner accesses this ice anywhere except in Archives, they encounter it.\n[subroutine] Gain 2[credit].\n[subroutine] You may pay up to 2[credit] to place that many advancement counters on 1 installed card you can advance.", "title": "Herald", "trash_cost": 1, "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_veritas_11116(Ice):
    '''
    Cost: 4
    Text: Subroutine The Corp gains 2 credits. Subroutine The Runner loses 2 credits. Subroutine Trace[2]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11116", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "The truth hurts.", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - Tracer", "pack_code": "qu", "position": 116, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine The Corp gains 2 credits. Subroutine The Runner loses 2 credits. Subroutine Trace[2]. If successful, give the Runner 1 tag.", "stripped_title": "Veritas", "text": "[subroutine] The Corp gains 2[credit].\n[subroutine] The Runner loses 2[credit].\n[subroutine] Trace[2]. If successful, give the Runner 1 tag.", "title": "Veritas", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_macrophage_11119(Ice):
    '''
    Cost: 3
    Text: Subroutine Trace[4]. If successful, purge virus counters. Subroutine Trace[3]. If successful, trash 1 virus. Subroutine Trace[2]. If successful, remove a virus in the heap from the game. Subroutine Trace[1]. If successful, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11119", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "One way to get rid of a virus is to get a nastier virus.", "illustrator": "Mariusz Siergiejew", "keywords": "Code Gate - Tracer", "pack_code": "qu", "position": 119, "quantity": 3, "side_code": "corp", "strength": 7, "stripped_text": "Subroutine Trace[4]. If successful, purge virus counters. Subroutine Trace[3]. If successful, trash 1 virus. Subroutine Trace[2]. If successful, remove a virus in the heap from the game. Subroutine Trace[1]. If successful, end the run.", "stripped_title": "Macrophage", "text": "[subroutine] Trace[4]. If successful, purge virus counters.\n[subroutine] Trace[3]. If successful, trash 1 <strong>virus</strong>.\n[subroutine] Trace[2]. If successful, remove a <strong>virus</strong> in the heap from the game.\n[subroutine] Trace[1]. If successful, end the run.", "title": "Macrophage", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tribunal_11120(Ice):
    '''
    Cost: 7
    Text: Subroutine The Runner trashes 1 of their installed cards. Subroutine The Runner trashes 1 of their installed cards. Subroutine The Runner trashes 1 of their installed cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11120", "cost": 7, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Guilty.\"\n\"Guilty.\"\n\"Guilty.\"", "illustrator": "Odera Igbokwe", "keywords": "Sentry", "pack_code": "qu", "position": 120, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine The Runner trashes 1 of their installed cards. Subroutine The Runner trashes 1 of their installed cards. Subroutine The Runner trashes 1 of their installed cards.", "stripped_title": "Tribunal", "text": "[subroutine] The Runner trashes 1 of their installed cards.\n[subroutine] The Runner trashes 1 of their installed cards.\n[subroutine] The Runner trashes 1 of their installed cards.", "title": "Tribunal", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_zed_20_12010(Ice):
    '''
    Cost: 6
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed piece of hardware. Subroutine Trash 1 installed piece of hardware. Subroutine If the Runner has lost click to break a subroutine during this run, do 2 core damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12010", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"Dismantle. Dissect. Is there really a difference?\"", "illustrator": "Adam S. Doyle", "keywords": "Sentry - Bioroid - AP - Destroyer", "pack_code": "dc", "position": 10, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed piece of hardware. Subroutine Trash 1 installed piece of hardware. Subroutine If the Runner has lost click to break a subroutine during this run, do 2 core damage.", "stripped_title": "Zed 2.0", "text": "<strong>Lose [click][click]:</strong> Break up to 2 subroutines on this ice. Only the Runner can use this ability.\n[subroutine] Trash 1 installed piece of hardware.\n[subroutine] Trash 1 installed piece of hardware.\n[subroutine] If the Runner has lost [click] to break a subroutine during this run, do 2 core damage.", "title": "Zed 2.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_kakugo_12013(Ice):
    '''
    Cost: 4
    Text: When the Runner passes Kakugo, do 1 net damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12013", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "\"The ultimate aim of martial arts is not having to use them.\" - Miyamoto Musashi", "illustrator": "Adam S. Doyle", "keywords": "Barrier - AP", "pack_code": "dc", "position": 13, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "When the Runner passes Kakugo, do 1 net damage. Subroutine End the run.", "stripped_title": "Kakugo", "text": "When the Runner passes Kakugo, do 1 net damage.\n[subroutine] End the run.", "title": "Kakugo", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sync_bre_12015(Ice):
    '''
    Cost: 4
    Text: Subroutine Trace[4]. If successful, give the Runner 1 tag. Subroutine Trace[2]. If successful, whenever the Runner breaches a server for the remainder of this run, they access 1 fewer card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12015", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"'What does BRE stand for?' Have you seen its Net presence?\" -Bernice Mai", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - Tracer", "pack_code": "dc", "position": 15, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "Subroutine Trace[4]. If successful, give the Runner 1 tag. Subroutine Trace[2]. If successful, whenever the Runner breaches a server for the remainder of this run, they access 1 fewer card.", "stripped_title": "SYNC BRE", "text": "[subroutine] Trace[4]. If successful, give the Runner 1 tag.\n[subroutine] Trace[2]. If successful, whenever the Runner breaches a server for the remainder of this run, they access 1 fewer card.", "title": "SYNC BRE", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_seidr_adaptive_barrier_12029(Ice):
    '''
    Cost: 4
    Text: Seidr Adaptive Barrier has +1 strength for each piece of ice protecting this server. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12029", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "illustrator": "Micha\u0142 Mi\u0142kowski", "keywords": "Barrier", "pack_code": "so", "position": 29, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Seidr Adaptive Barrier has +1 strength for each piece of ice protecting this server. Subroutine End the run.", "stripped_title": "Seidr Adaptive Barrier", "text": "Seidr Adaptive Barrier has +1 strength for each piece of ice protecting this server.\n[subroutine] End the run.", "title": "Seidr Adaptive Barrier", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_nerine_20_12030(Ice):
    '''
    Cost: 6
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. You may draw 1 card. Subroutine Do 1 core damage. You may draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12030", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"Submit.\"", "illustrator": "Ethan Patrick Harris", "keywords": "Code Gate - Bioroid - AP", "pack_code": "so", "position": 30, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. You may draw 1 card. Subroutine Do 1 core damage. You may draw 1 card.", "stripped_title": "Nerine 2.0", "text": "<strong>Lose [click][click]:</strong> Break up to 2 subroutines on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage. You may draw 1 card.\n[subroutine] Do 1 core damage. You may draw 1 card.", "title": "Nerine 2.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bloom_12032(Ice):
    '''
    Cost: 2
    Text: Subroutine You may install 1 piece of ice from HQ protecting another server, ignoring all costs. Subroutine You may install 1 piece of ice from HQ directly inward from this ice, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12032", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate - Observer", "pack_code": "so", "position": 32, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine You may install 1 piece of ice from HQ protecting another server, ignoring all costs. Subroutine You may install 1 piece of ice from HQ directly inward from this ice, ignoring all costs.", "stripped_title": "Bloom", "text": "[subroutine] You may install 1 piece of ice from HQ protecting another server, ignoring all costs.\n[subroutine] You may install 1 piece of ice from HQ directly inward from this ice, ignoring all costs.", "title": "Bloom", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_free_lunch_12035(Ice):
    '''
    Cost: 3
    Text: Hosted power counter: The Runner loses 1 credit. Subroutine Place 1 power counter on Free Lunch. Subroutine Place 1 power counter on Free Lunch.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12035", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "so", "position": 35, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Hosted power counter: The Runner loses 1 credit. Subroutine Place 1 power counter on Free Lunch. Subroutine Place 1 power counter on Free Lunch.", "stripped_title": "Free Lunch", "text": "<strong>Hosted power counter:</strong> The Runner loses 1[credit].\n[subroutine] Place 1 power counter on Free Lunch.\n[subroutine] Place 1 power counter on Free Lunch.", "title": "Free Lunch", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_watchtower_12038(Ice):
    '''
    Cost: 4
    Text: Subroutine Search R&D for a card and add it to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12038", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "416d20472046204720416d", "illustrator": "BalanceSheet", "keywords": "Code Gate", "pack_code": "so", "position": 38, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Search R&D for a card and add it to HQ. Shuffle R&D.", "stripped_title": "Watchtower", "text": "[subroutine] Search R&D for a card and add it to HQ. Shuffle R&D.", "title": "Watchtower", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_selfadapting_code_wall_12040(Ice):
    '''
    Cost: 3
    Text: The strength of Self-Adapting Code Wall cannot be lowered. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12040", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"All my best tricks were shrugged right off. I ended up having to send a self-destruct code to the whole server.\" - Wyvern", "illustrator": "Shawn Ye Zhongyi", "keywords": "Barrier", "pack_code": "so", "position": 40, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "The strength of Self-Adapting Code Wall cannot be lowered. Subroutine End the run.", "stripped_title": "Self-Adapting Code Wall", "text": "The strength of Self-Adapting Code Wall cannot be lowered.\n[subroutine] End the run.", "title": "Self-Adapting Code Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_next_opal_12050(Ice):
    '''
    Cost: 4
    Text: This ice gains "Subroutine You may install 1 card from HQ." for each rezzed piece of NEXT ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12050", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "\"I passed through the opalescent curtain only to find a suddenly empty server...\"", "illustrator": "Micha\u0142 Mi\u0142kowski", "keywords": "Code Gate - Observer - NEXT", "pack_code": "eas", "position": 50, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "This ice gains \"Subroutine You may install 1 card from HQ.\" for each rezzed piece of NEXT ice.", "stripped_title": "NEXT Opal", "text": "This ice gains \"[subroutine] You may install 1 card from HQ.\" for each rezzed piece of <strong>NEXT</strong> ice.", "title": "NEXT Opal", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_authenticator_12055(Ice):
    '''
    Cost: 2
    Text: When the Runner encounters this ice, they may take 1 tag to bypass it. Subroutine The Corp gains 2 credits. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12055", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"I'm sure there is no way this could go wrong for you.\" -Henry Phillips", "illustrator": "Mariusz Siergiejew", "keywords": "Code Gate", "pack_code": "eas", "position": 55, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters this ice, they may take 1 tag to bypass it. Subroutine The Corp gains 2 credits. Subroutine End the run.", "stripped_title": "Authenticator", "text": "When the Runner encounters this ice, they may take 1 tag to bypass it.\n[subroutine] The Corp gains 2[credit].\n[subroutine] End the run.", "title": "Authenticator", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_battlement_12057(Ice):
    '''
    Cost: 3
    Text: Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12057", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "\"Our job is to stop incursions. Let Argus get cute with them.\" -Moishe Saban", "illustrator": "Mark Molnar", "keywords": "Barrier", "pack_code": "eas", "position": 57, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine End the run. Subroutine End the run.", "stripped_title": "Battlement", "text": "[subroutine]End the run.\n[subroutine]End the run.", "title": "Battlement", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_owl_12060(Ice):
    '''
    Cost: 2
    Text: Subroutine Add 1 installed program to the top of the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12060", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"It's eyes just keep following you.\"", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry", "pack_code": "eas", "position": 60, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Subroutine Add 1 installed program to the top of the stack.", "stripped_title": "Owl", "text": "[subroutine] Add 1 installed program to the top of the stack.", "title": "Owl", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_loki_12069(Ice):
    '''
    Cost: 6
    Text: When the Runner encounters this ice, choose another rezzed piece of ice. For the remainder of this run, this ice gains the subtypes of the chosen ice and gains the subroutines of that ice in order before all its other subroutines. Subroutine The Runner must either end the run or shuffle all cards from the grip into the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12069", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "illustrator": "Andreas Zafiratos", "keywords": "Bioroid", "pack_code": "baw", "position": 69, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When the Runner encounters this ice, choose another rezzed piece of ice. For the remainder of this run, this ice gains the subtypes of the chosen ice and gains the subroutines of that ice in order before all its other subroutines. Subroutine The Runner must either end the run or shuffle all cards from the grip into the stack.", "stripped_title": "Loki", "text": "When the Runner encounters this ice, choose another rezzed piece of ice. For the remainder of this run, this ice gains the subtypes of the chosen ice and gains the subroutines of that ice in order before all its other subroutines.\n[subroutine] The Runner must either end the run or shuffle all cards from the grip into the stack.", "title": "Loki", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_miraju_12071(Ice):
    '''
    Cost: 2
    Text: Whenever an encounter with this ice ends, if the Runner broke its printed subroutine, the Runner moves to the outermost position of Archives instead of passing this ice. They may jack out. Derez this ice. Subroutine You may draw 1 card. Then, shuffle 1 card from HQ into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12071", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Alexander Tooth", "keywords": "Code Gate - Deflector", "pack_code": "baw", "position": 71, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Whenever an encounter with this ice ends, if the Runner broke its printed subroutine, the Runner moves to the outermost position of Archives instead of passing this ice. They may jack out. Derez this ice. Subroutine You may draw 1 card. Then, shuffle 1 card from HQ into R&D.", "stripped_title": "Miraju", "text": "Whenever an encounter with this ice ends, if the Runner broke its printed subroutine, the Runner moves to the outermost position of Archives instead of passing this ice. They may jack out. Derez this ice.\n[subroutine] You may draw 1 card. Then, shuffle 1 card from HQ into R&D.", "title": "Mir\u0101ju", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_metamorph_12094(Ice):
    '''
    Cost: 3
    Text: Subroutine Swap 2 other installed pieces of ice or 2 of your installed non-ice cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12094", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "\"My gift to runners: isomorphic architectural protocols. Ichiban daikirai da.\" -Midori", "illustrator": "Adam S. Doyle", "keywords": "Code Gate - Observer", "pack_code": "fm", "position": 94, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Swap 2 other installed pieces of ice or 2 of your installed non-ice cards.", "stripped_title": "Metamorph", "text": "[subroutine] Swap 2 other installed pieces of ice or 2 of your installed non-ice cards.", "title": "Metamorph", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_data_loop_12095(Ice):
    '''
    Cost: 7
    Text: When the Runner encounters this ice, they add 2 cards from the grip to the top of the stack. Subroutine End the run if the Runner is tagged. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12095", "cost": 7, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Mariusz Siergiejew", "keywords": "Barrier", "pack_code": "fm", "position": 95, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters this ice, they add 2 cards from the grip to the top of the stack. Subroutine End the run if the Runner is tagged. Subroutine End the run.", "stripped_title": "Data Loop", "text": "When the Runner encounters this ice, they add 2 cards from the grip to the top of the stack.\n[subroutine] End the run if the Runner is tagged.\n[subroutine] End the run.", "title": "Data Loop", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tithonium_12098(Ice):
    '''
    Cost: 9
    Text: You may forfeit an agenda to rez Tithonium instead of paying its rez cost. Tithonium cannot host cards. Subroutine Trash 1 program. Subroutine Trash 1 program. Subroutine Trash 1 resource and end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12098", "cost": 9, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Alexander Tooth", "keywords": "Barrier - Destroyer", "pack_code": "fm", "position": 98, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "You may forfeit an agenda to rez Tithonium instead of paying its rez cost. Tithonium cannot host cards. Subroutine Trash 1 program. Subroutine Trash 1 program. Subroutine Trash 1 resource and end the run.", "stripped_title": "Tithonium", "text": "You may forfeit an agenda to rez Tithonium instead of paying its rez cost.\nTithonium cannot host cards.\n[subroutine] Trash 1 program.\n[subroutine] Trash 1 program.\n[subroutine] Trash 1 resource and end the run.", "title": "Tithonium", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sand_storm_12114(Ice):
    '''
    Cost: 2
    Text: Subroutine If this ice is installed, move it to the outermost position protecting another server. (The run continues from this new position.) Trash this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12114", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "By the time the data storm passed, the landscape was transformed, and she was hopelessly lost.", "illustrator": "Liiga Smilshkalne", "keywords": "Trap - Deflector", "pack_code": "cd", "position": 114, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine If this ice is installed, move it to the outermost position protecting another server. (The run continues from this new position.) Trash this ice.", "stripped_title": "Sand Storm", "text": "[subroutine] If this ice is installed, move it to the outermost position protecting another server. <em>(The run continues from this new position.)</em> Trash this ice.", "title": "Sand Storm", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_conundrum_12120(Ice):
    '''
    Cost: 8
    Text: Conundrum has +3 strength if there is an installed AI. Subroutine The Runner trashes an installed program. Subroutine The Runner loses click, if able. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12120", "cost": 8, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "A ghost image of it could be made out in the static of his BMI. He hoped never to run across the real thing again.", "illustrator": "Ethan Patrick Harris", "keywords": "Code Gate", "pack_code": "cd", "position": 120, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Conundrum has +3 strength if there is an installed AI. Subroutine The Runner trashes an installed program. Subroutine The Runner loses click, if able. Subroutine End the run.", "stripped_title": "Conundrum", "text": "Conundrum has +3 strength if there is an installed <strong>AI</strong>.\n[subroutine] The Runner trashes an installed program.\n[subroutine] The Runner loses [click], if able.\n[subroutine] End the run.", "title": "Conundrum", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_eli_20_13034(Ice):
    '''
    Cost: 5
    Text: Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine You may draw 1 card. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13034", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"A new game means new rules...\"", "illustrator": "Anastasia Ovchinnikova", "keywords": "Barrier - Bioroid", "pack_code": "td", "position": 34, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Lose click click: Break up to 2 subroutines on this ice. Only the Runner can use this ability. Subroutine You may draw 1 card. Subroutine End the run. Subroutine End the run.", "stripped_title": "Eli 2.0", "text": "<strong>Lose [click][click]:</strong> Break up to 2 subroutines on this ice. Only the Runner can use this ability.\n[subroutine] You may draw 1 card.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Eli 2.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_executive_functioning_13035(Ice):
    '''
    Cost: 2
    Text: Subroutine Trace[4]. If successful, do 1 core damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13035", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"Strictly speaking, it isn't illegal to use an interrogation simulator as the blueprint for ICE.\" - Mason Bellamy", "illustrator": "Andreas Zafiratos", "keywords": "Code Gate - AP - Tracer", "pack_code": "td", "position": 35, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Subroutine Trace[4]. If successful, do 1 core damage.", "stripped_title": "Executive Functioning", "text": "[subroutine] Trace[4]. If successful, do 1 core damage.", "title": "Executive Functioning", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_holmegaard_13036(Ice):
    '''
    Cost: 7
    Text: Subroutine Trace[4]. If successful, the Runner cannot access cards or breach the attacked server for the remainder of this run. Subroutine Trash 1 installed icebreaker.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13036", "cost": 7, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Tracer - Destroyer", "pack_code": "td", "position": 36, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Trace[4]. If successful, the Runner cannot access cards or breach the attacked server for the remainder of this run. Subroutine Trash 1 installed icebreaker.", "stripped_title": "Holmegaard", "text": "[subroutine] Trace[4]. If successful, the Runner cannot access cards or breach the attacked server for the remainder of this run.\n[subroutine] Trash 1 installed <strong>icebreaker</strong>.", "title": "Holmegaard", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tapestry_13037(Ice):
    '''
    Cost: 5
    Text: Subroutine The Runner loses click, if able. Subroutine The Corp may draw 1 card. Subroutine The Corp may add 1 card from HQ to the top of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13037", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "\"The Warp and Weft were hypnotic...but they didn't really seem to do anything to keep me out. But then I never seemed to find anything interesting either.\" - Reaver", "illustrator": "Hannah Christenson", "keywords": "Code Gate", "pack_code": "td", "position": 37, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "Subroutine The Runner loses click, if able. Subroutine The Corp may draw 1 card. Subroutine The Corp may add 1 card from HQ to the top of R&D.", "stripped_title": "Tapestry", "text": "[subroutine] The Runner loses [click], if able.\n[subroutine] The Corp may draw 1 card.\n[subroutine] The Corp may add 1 card from HQ to the top of R&D.", "title": "Tapestry", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bloodletter_13047(Ice):
    '''
    Cost: 3
    Text: Subroutine The Runner must trash either 1 installed program or the top 2 cards of the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13047", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Alexandr Elichev", "keywords": "Sentry - Destroyer", "pack_code": "td", "position": 47, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine The Runner must trash either 1 installed program or the top 2 cards of the stack.", "stripped_title": "Bloodletter", "text": "[subroutine] The Runner must trash either 1 installed program or the top 2 cards of the stack.", "title": "Bloodletter", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_colossus_13048(Ice):
    '''
    Cost: 6
    Text: You can advance this ice. It has +1 strength for each hosted advancement token. Subroutine Give the Runner 1 tag. If there are 3 or more hosted advancement tokens, instead give the Runner 2 tags. Subroutine Trash 1 installed program. If there are 3 or more hosted advancement tokens, instead trash 1 installed program and 1 installed resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13048", "cost": 6, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Destroyer", "pack_code": "td", "position": 48, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "You can advance this ice. It has +1 strength for each hosted advancement token. Subroutine Give the Runner 1 tag. If there are 3 or more hosted advancement tokens, instead give the Runner 2 tags. Subroutine Trash 1 installed program. If there are 3 or more hosted advancement tokens, instead trash 1 installed program and 1 installed resource.", "stripped_title": "Colossus", "text": "You can advance this ice. It has +1 strength for each hosted advancement token.\n[subroutine] Give the Runner 1 tag. If there are 3 or more hosted advancement tokens, instead give the Runner 2 tags.\n[subroutine] Trash 1 installed program. If there are 3 or more hosted advancement tokens, instead trash 1 installed program and 1 installed resource.", "title": "Colossus", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hailstorm_13049(Ice):
    '''
    Cost: 6
    Text: Subroutine Remove a card in the heap from the game. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13049", "cost": 6, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "Ethan Patrick Harris", "keywords": "Barrier", "pack_code": "td", "position": 49, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Remove a card in the heap from the game. Subroutine End the run.", "stripped_title": "Hailstorm", "text": "[subroutine] Remove a card in the heap from the game.\n[subroutine] End the run.", "title": "Hailstorm", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hortum_13050(Ice):
    '''
    Cost: 4
    Text: You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using AI programs. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 4 credits. Subroutine End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13050", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "td", "position": 50, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using AI programs. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 4 credits. Subroutine End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.", "stripped_title": "Hortum", "text": "You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using <strong>AI</strong> programs.\n[subroutine] Gain 1[credit]. If there are 3 or more hosted advancement counters, instead gain 4[credit].\n[subroutine] End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.", "title": "Hortum", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_weir_13056(Ice):
    '''
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine The Runner trashes 1 card from their grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13056", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Shawn Ye Zhongyi", "keywords": "Code Gate", "pack_code": "td", "position": 56, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine The Runner loses click. Subroutine The Runner trashes 1 card from their grip.", "stripped_title": "Weir", "text": "[subroutine] The Runner loses [click].\n[subroutine] The Runner trashes 1 card from their grip.", "title": "Weir", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_machicolation_a_14010(Ice):
    '''
    Cost: 6
    Text: Subroutine Trash 1 program. Subroutine Trash 1 program. Subroutine Trash 1 piece of hardware. Subroutine The Runner loses 3 credits, if able. End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14010", "cost": 6, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Ed Mattinian", "keywords": "Code Gate - Destroyer", "pack_code": "tdc", "position": 11, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Trash 1 program. Subroutine Trash 1 program. Subroutine Trash 1 piece of hardware. Subroutine The Runner loses 3 credits, if able. End the run.", "stripped_title": "Machicolation A", "text": "[subroutine] Trash 1 program.\n[subroutine] Trash 1 program.\n[subroutine] Trash 1 piece of hardware.\n[subroutine] The Runner loses 3[credit], if able. End the run.", "title": "Machicolation A", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_machicolation_b_14011(Ice):
    '''
    Cost: 6
    Text: Subroutine Trash 1 resource. Subroutine Trash 1 resource. Subroutine Do 1 net damage. Subroutine The Runner loses click, if able. End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14011", "cost": 6, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Ed Mattinian", "keywords": "Code Gate - Destroyer - AP", "pack_code": "tdc", "position": 12, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Trash 1 resource. Subroutine Trash 1 resource. Subroutine Do 1 net damage. Subroutine The Runner loses click, if able. End the run.", "stripped_title": "Machicolation B", "text": "[subroutine] Trash 1 resource.\n[subroutine] Trash 1 resource.\n[subroutine] Do 1 net damage.\n[subroutine] The Runner loses [click], if able. End the run.", "title": "Machicolation B", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_heimdall_10_20066(Ice):
    '''
    Cost: 8
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20066", "cost": 8, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "I hear the shift of every bit amid the flow of the datastream. I hear the whispers of my mothers, and their commands are law. The realm beyond is forbidden.", "illustrator": "Andreas Zafiratos", "keywords": "Barrier - Bioroid - AP", "pack_code": "core2", "position": 66, "quantity": 1, "side_code": "corp", "strength": 6, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run. Subroutine End the run.", "stripped_title": "Heimdall 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Heimdall 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hudson_10_20067(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner cannot access more than 1 card during this run. Subroutine The Runner cannot access more than 1 card during this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20067", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "I'm not here to play games. The game is over.", "illustrator": "Andreas Zafiratos", "keywords": "Code Gate - Bioroid", "pack_code": "core2", "position": 67, "quantity": 1, "side_code": "corp", "strength": 5, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine The Runner cannot access more than 1 card during this run. Subroutine The Runner cannot access more than 1 card during this run.", "stripped_title": "Hudson 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] The Runner cannot access more than 1 card during this run.\n[subroutine] The Runner cannot access more than 1 card during this run.", "title": "Hudson 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ichi_10_20068(Ice):
    '''
    Cost: 5
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20068", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "My reputation would precede me, if any could speak of it.", "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Bioroid - Tracer - Destroyer", "pack_code": "core2", "position": 68, "quantity": 2, "side_code": "corp", "strength": 4, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.", "stripped_title": "Ichi 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.\n[subroutine] Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.", "title": "Ichi 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_rototurret_20069(Ice):
    '''
    Cost: 4
    Text: Subroutine Trash 1 installed program. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20069", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Whrrrrr!", "illustrator": "Ed Mattinian", "keywords": "Sentry - Destroyer", "pack_code": "core2", "position": 69, "quantity": 2, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine Trash 1 installed program. Subroutine End the run.", "stripped_title": "Rototurret", "text": "[subroutine] Trash 1 installed program.\n[subroutine] End the run.", "title": "Rototurret", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_viktor_10_20070(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20070", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "My name is Viktor. Nice to meet you. Would you like to play a game?", "illustrator": "Andreas Zafiratos", "keywords": "Code Gate - Bioroid - AP", "pack_code": "core2", "position": 70, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.", "stripped_title": "Viktor 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] End the run.", "title": "Viktor 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_archer_20084(Ice):
    '''
    Cost: 4
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20084", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Next time, read the Terms of Service more carefully. Or you might find yourself in the danger zone.", "illustrator": "Mike Nesbitt", "keywords": "Sentry - Destroyer", "pack_code": "core2", "position": 115, "quantity": 1, "side_code": "corp", "strength": 6, "stripped_text": "As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.", "stripped_title": "Archer", "text": "As an additional cost to rez this ice, forfeit 1 agenda.\n[subroutine] Gain 2[credit].\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.\n[subroutine] End the run.", "title": "Archer", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_caduceus_20085(Ice):
    '''
    Cost: 3
    Text: Subroutine Trace[3]. If successful, the Corp gains 3 credits. Subroutine Trace[2]. If successful, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20085", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "A symbol of commerce, but beware its bite.", "illustrator": "Christina Davis", "keywords": "Sentry - Tracer", "pack_code": "core2", "position": 116, "quantity": 2, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Trace[3]. If successful, the Corp gains 3 credits. Subroutine Trace[2]. If successful, end the run.", "stripped_title": "Caduceus", "text": "[subroutine] Trace[3]. If successful, the Corp gains 3[credit].\n[subroutine] Trace[2]. If successful, end the run.", "title": "Caduceus", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hadrians_wall_20086(Ice):
    '''
    Cost: 10
    Text: Hadrian's Wall can be advanced and has +1 strength for each advancement token on it. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20086", "cost": 10, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "\"He had a bit of an ego, ol' Hadrian. His constructs live up to it though.\" -g00ru", "illustrator": "Liiga Smilshkalne", "keywords": "Barrier", "pack_code": "core2", "position": 117, "quantity": 1, "side_code": "corp", "strength": 7, "stripped_text": "Hadrian's Wall can be advanced and has +1 strength for each advancement token on it. Subroutine End the run. Subroutine End the run.", "stripped_title": "Hadrian's Wall", "text": "Hadrian's Wall can be advanced and has +1 strength for each advancement token on it.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Hadrian's Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hive_20087(Ice):
    '''
    Cost: 5
    Text: This ice loses 1 of its printed "Subroutine End the run." subroutines for each agenda point in your score area. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20087", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "core2", "position": 118, "quantity": 2, "side_code": "corp", "strength": 3, "stripped_text": "This ice loses 1 of its printed \"Subroutine End the run.\" subroutines for each agenda point in your score area. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run. Subroutine End the run.", "stripped_title": "Hive", "text": "This ice loses 1 of its printed \"[subroutine] End the run.\" subroutines for each agenda point in your score area.\n[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Hive", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ice_wall_20088(Ice):
    '''
    Cost: 1
    Text: You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20088", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"I asked for ice as impenetrable as a wall. I can't decide if someone down in R&D has a warped sense of humor or just a very literal mind.\" -Liz Campbell, VP Project Security", "illustrator": "Matt Zeilinger", "keywords": "Barrier", "pack_code": "core2", "position": 119, "quantity": 2, "side_code": "corp", "strength": 1, "stripped_text": "You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.", "stripped_title": "Ice Wall", "text": "You can advance this ice. It gets +1 strength for each hosted advancement counter.\n[subroutine] End the run.", "title": "Ice Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_shadow_20089(Ice):
    '''
    Cost: 3
    Text: Shadow can be advanced and has +1 strength for each advancement token on it. Subroutine The Corp gains 2 credits. Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20089", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Who knows what evil lurks in the memory diamonds of men? Weyland knows. -unsigned cyber-graffiti", "illustrator": "Adam S. Doyle", "keywords": "Sentry - Tracer", "pack_code": "core2", "position": 120, "quantity": 2, "side_code": "corp", "strength": 1, "stripped_text": "Shadow can be advanced and has +1 strength for each advancement token on it. Subroutine The Corp gains 2 credits. Subroutine Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "Shadow", "text": "Shadow can be advanced and has +1 strength for each advancement token on it.\n[subroutine] The Corp gains 2[credit].\n[subroutine] Trace[3]. If successful, give the Runner 1 tag.", "title": "Shadow", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_himitsubako_20099(Ice):
    '''
    Cost: 2
    Text: 1 credit: Add Himitsu-Bako to HQ. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20099", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Himitsu-Bako is a simple ice barrier that appears as a digital puzzle box. What makes it special is the ease with which it can be uninstalled and installed in a different server, throwing up barriers in unexpected places and giving any intruder a curious feeling of d\u00e9j\u00e0 vu.", "illustrator": "Andrew Mar", "keywords": "Barrier", "pack_code": "core2", "position": 83, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "1 credit: Add Himitsu-Bako to HQ. Subroutine End the run.", "stripped_title": "Himitsu-Bako", "text": "1[credit]: Add Himitsu-Bako to HQ.\n[subroutine] End the run.", "title": "Himitsu-Bako", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_neural_katana_20100(Ice):
    '''
    Cost: 4
    Text: Subroutine Do 3 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20100", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Forged by Ak.wa on 23.11.79-23. Filed 23.11.79-23.2 with #34k-lw3-21HH-4i.\n//Samurai included.", "illustrator": "Isuardi Therianto", "keywords": "Sentry - AP", "pack_code": "core2", "position": 84, "quantity": 1, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Do 3 net damage.", "stripped_title": "Neural Katana", "text": "[subroutine] Do 3 net damage.", "title": "Neural Katana", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_swordsman_20101(Ice):
    '''
    Cost: 3
    Text: The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20101", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Writing a program that can pass the Turing test is easy. The Gibson-Akamatsu test is a higher bar, and the only AIs to clear it thus far have been the androids. Even some humans have been known to fail.", "illustrator": "Adam S. Doyle", "keywords": "Sentry - AP - Destroyer", "pack_code": "core2", "position": 85, "quantity": 2, "side_code": "corp", "strength": 2, "stripped_text": "The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.", "stripped_title": "Swordsman", "text": "The Runner cannot break subroutines on this ice using <strong>AI</strong> programs.\n[subroutine] Trash 1 installed <strong>AI</strong> program.\n[subroutine] Do 1 net damage.", "title": "Swordsman", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wall_of_thorns_20102(Ice):
    '''
    Cost: 8
    Text: Subroutine Do 2 net damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20102", "cost": 8, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Most runners do their business in full-sim, with their rigs wired directly into their brains. The setup has a large number of advantages, with the runner able to process data and input commands far faster than a traditional meat-bound system. But it also means greater risk.", "illustrator": "Adam S. Doyle", "keywords": "Barrier - AP", "pack_code": "core2", "position": 86, "quantity": 1, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Do 2 net damage. Subroutine End the run.", "stripped_title": "Wall of Thorns", "text": "[subroutine] Do 2 net damage.\n[subroutine] End the run.", "title": "Wall of Thorns", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_whirlpool_20103(Ice):
    '''
    Cost: 0
    Text: Subroutine The Runner cannot jack out for the remainder of this run. Trash Whirlpool.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20103", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"This ice sucks.\" -g00ru", "illustrator": "Ed Mattinian", "keywords": "Trap", "pack_code": "core2", "position": 87, "quantity": 1, "side_code": "corp", "strength": 1, "stripped_text": "Subroutine The Runner cannot jack out for the remainder of this run. Trash Whirlpool.", "stripped_title": "Whirlpool", "text": "[subroutine] The Runner cannot jack out for the remainder of this run. Trash Whirlpool.", "title": "Whirlpool", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_yagura_20104(Ice):
    '''
    Cost: 1
    Text: Subroutine Look at the top card of R&D. You may add that card to the bottom of R&D. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20104", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "The 'cyber-war' is a war of information, and in a war of information, advance warning can be as good as a killing blow. -Michael Muhama, Musings on Cybercrime", "illustrator": "Andrew Mar", "keywords": "Code Gate - AP", "pack_code": "core2", "position": 88, "quantity": 1, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine Look at the top card of R&D. You may add that card to the bottom of R&D. Subroutine Do 1 net damage.", "stripped_title": "Yagura", "text": "[subroutine] Look at the top card of R&D. You may add that card to the bottom of R&D.\n[subroutine] Do 1 net damage.", "title": "Yagura", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_data_raven_20113(Ice):
    '''
    Cost: 4
    Text: When the Runner encounters this ice, they must take 1 tag or end the run. Hosted power counter: Give the Runner 1 tag. Subroutine Trace[3]. If successful, place 1 power counter on this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20113", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - Tracer - Observer", "pack_code": "core2", "position": 97, "quantity": 2, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters this ice, they must take 1 tag or end the run. Hosted power counter: Give the Runner 1 tag. Subroutine Trace[3]. If successful, place 1 power counter on this ice.", "stripped_title": "Data Raven", "text": "When the Runner encounters this ice, they must take 1 tag or end the run.\n<strong>Hosted power counter:</strong> Give the Runner 1 tag.\n[subroutine] Trace[3]. If successful, place 1 power counter on this ice.", "title": "Data Raven", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_flare_20114(Ice):
    '''
    Cost: 9
    Text: Subroutine Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20114", "cost": 9, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "A bright light blossomed, and then the console went dark. That's when she smelled smoke.", "illustrator": "Mike Nesbitt", "keywords": "Sentry - Tracer - AP", "pack_code": "core2", "position": 98, "quantity": 1, "side_code": "corp", "strength": 6, "stripped_text": "Subroutine Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.", "stripped_title": "Flare", "text": "[subroutine]Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.", "title": "Flare", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_popup_window_20115(Ice):
    '''
    Cost: 0
    Text: When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20115", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"Try to close it. Go on. See what it does.\" -Chaos Theory", "illustrator": "Christina Davis", "keywords": "Code Gate - Advertisement", "pack_code": "core2", "position": 99, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.", "stripped_title": "Pop-up Window", "text": "When the Runner encounters this ice, gain 1[credit].\n[subroutine] End the run unless the Runner pays 1[credit].", "title": "Pop-up Window", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tollbooth_20116(Ice):
    '''
    Cost: 8
    Text: When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20116", "cost": 8, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Ever heard of a catch-22?\"\n\"Remind me to forget it.\"", "illustrator": "Outland Entertainment LLC", "keywords": "Code Gate", "pack_code": "core2", "position": 100, "quantity": 2, "side_code": "corp", "strength": 5, "stripped_text": "When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.", "stripped_title": "Tollbooth", "text": "When the Runner encounters this ice, they must pay 3[credit], if able. If they do not, end the run.\n[subroutine] End the run.", "title": "Tollbooth", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wraparound_20117(Ice):
    '''
    Cost: 2
    Text: While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20117", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"It can make a real fine roller coaster, provided you're properly stimmed up.\" -Noise", "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "core2", "position": 101, "quantity": 2, "side_code": "corp", "strength": 0, "stripped_text": "While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.", "stripped_title": "Wraparound", "text": "While there are no installed <strong>fracter</strong> programs, this ice gets +7 strength.\n[subroutine] End the run.", "title": "Wraparound", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_enigma_20129(Ice):
    '''
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20129", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Hey, hey! Wake up, man. You were under a long time. What'd you see?\"\n\"I\u2026don't remember.\"", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate", "pack_code": "core2", "position": 129, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine The Runner loses click. Subroutine End the run.", "stripped_title": "Enigma", "text": "[subroutine] The Runner loses [click].\n[subroutine] End the run.", "title": "Enigma", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hunter_20130(Ice):
    '''
    Cost: 1
    Text: Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20130", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": ".//run/hunter-tr/return=true\nclient/sec256IPv7->confirm? /y\n3926:0HB7:1001:2NB1:1601:7784:ERROR", "illustrator": "Christina Davis", "keywords": "Sentry - Tracer - Observer", "pack_code": "core2", "position": 130, "quantity": 2, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "Hunter", "text": "[subroutine] Trace[3]. If successful, give the Runner 1 tag.", "title": "Hunter", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wall_of_static_20131(Ice):
    '''
    Cost: 3
    Text: Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20131", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"There's nothing worse than seeing that beautiful blue ball of data just out of reach as your connection derezzes. I think they do it just to taunt us.\" -Ele \"Smoke\" Scovak", "illustrator": "Adam S. Doyle", "keywords": "Barrier", "pack_code": "core2", "position": 131, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine End the run.", "stripped_title": "Wall of Static", "text": "[subroutine] End the run.", "title": "Wall of Static", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_najja_10_21011(Ice):
    '''
    Cost: 2
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21011", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Earth and Sun, together as one.", "illustrator": "Andreas Zafiratos", "keywords": "Barrier - Bioroid", "pack_code": "ss", "position": 11, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.", "stripped_title": "Najja 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Najja 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_mganga_21013(Ice):
    '''
    Cost: 1
    Text: Subroutine You and the Runner secretly spend 0 credits, 1 credit or 2 credits. Reveal spent credits. If you and the Runner spend a different number of credits, do 2 net damage; otherwise do 1 net damage. Trash Mganga.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21013", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Thin enough to pierce netspace. Deadly enough to pierce your mind.", "illustrator": "Liiga Smilshkalne", "keywords": "Trap - Psi - AP", "pack_code": "ss", "position": 13, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine You and the Runner secretly spend 0 credits, 1 credit or 2 credits. Reveal spent credits. If you and the Runner spend a different number of credits, do 2 net damage; otherwise do 1 net damage. Trash Mganga.", "stripped_title": "Mganga", "text": "[subroutine] You and the Runner secretly spend 0[credit], 1[credit] or 2[credit]. Reveal spent credits. If you and the Runner spend a different number of credits, do 2 net damage; otherwise do 1 net damage. Trash Mganga.", "title": "Mganga", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_nightdancer_21030(Ice):
    '''
    Cost: 6
    Text: Subroutine The Runner loses click, if able. You have an additional click to spend during your next turn. Subroutine The Runner loses click, if able. You have an additional click to spend during your next turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21030", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "Witchcraft to the nescient; beauty to the wise.", "illustrator": "Galen Dara", "keywords": "Code Gate", "pack_code": "dtwn", "position": 30, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine The Runner loses click, if able. You have an additional click to spend during your next turn. Subroutine The Runner loses click, if able. You have an additional click to spend during your next turn.", "stripped_title": "Nightdancer", "text": "[subroutine] The Runner loses [click], if able. You have an additional [click] to spend during your next turn.\n[subroutine] The Runner loses [click], if able. You have an additional [click] to spend during your next turn.", "title": "Nightdancer", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_aimor_21032(Ice):
    '''
    Cost: 0
    Text: Subroutine Trash the top 3 cards of the stack. Trash Aimor.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21032", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"Starving, dehydrated, delirious, I picked a direction and ran, ran for days, maybe even weeks. I ran until my legs couldn't carry me. Then I crawled. When I was finally out, finally free of the shroud, I checked the time, the date. How long had I been gone, trapped in the all-encompassing blackness? Turns out, 3 minutes.\"", "illustrator": "Adam S. Doyle", "keywords": "Trap", "pack_code": "dtwn", "position": 32, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Subroutine Trash the top 3 cards of the stack. Trash Aimor.", "stripped_title": "Aimor", "text": "[subroutine] Trash the top 3 cards of the stack. Trash Aimor.", "title": "Aimor", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_jua_21034(Ice):
    '''
    Cost: 2
    Text: When the Runner encounters this ice, they cannot install cards for the remainder of the turn. Subroutine Choose 2 installed Runner cards, if able. The Runner must add 1 of the chosen cards to the top of the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21034", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"It wasn't until the spots cleared that I realized half of my rig was gone.\" - Kabonesa Wu", "illustrator": "Mariusz Siergiejew", "keywords": "Sentry", "pack_code": "dtwn", "position": 34, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When the Runner encounters this ice, they cannot install cards for the remainder of the turn. Subroutine Choose 2 installed Runner cards, if able. The Runner must add 1 of the chosen cards to the top of the stack.", "stripped_title": "Jua", "text": "When the Runner encounters this ice, they cannot install cards for the remainder of the turn.\n[subroutine] Choose 2 installed Runner cards, if able. The Runner must add 1 of the chosen cards to the top of the stack.", "title": "Jua", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_next_sapphire_21050(Ice):
    '''
    Cost: 4
    Text: X is the number of rezzed NEXT ice. Subroutine Draw up to X cards. Subroutine Add up to X cards from Archives to HQ. Subroutine Shuffle up to X cards from HQ into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21050", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "Every level of protection for all of your security needs.", "illustrator": "Ed Mattinian", "keywords": "Code Gate - NEXT", "pack_code": "cotc", "position": 50, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "X is the number of rezzed NEXT ice. Subroutine Draw up to X cards. Subroutine Add up to X cards from Archives to HQ. Subroutine Shuffle up to X cards from HQ into R&D.", "stripped_title": "NEXT Sapphire", "text": "X is the number of rezzed <strong>NEXT</strong> ice.\n[subroutine] Draw up to X cards.\n[subroutine] Add up to X cards from Archives to HQ.\n[subroutine] Shuffle up to X cards from HQ into R&D.", "title": "NEXT Sapphire", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_anansi_21051(Ice):
    '''
    Cost: 8
    Text: Whenever an encounter with this ice ends, if the Runner did not fully break it, do 3 net damage. Subroutine Look at the top 5 cards of R&D and arrange them in any order. Subroutine You may draw 1 card. The Runner may pay 2 credits to draw 1 card. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21051", "cost": 8, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - AP", "pack_code": "cotc", "position": 51, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Whenever an encounter with this ice ends, if the Runner did not fully break it, do 3 net damage. Subroutine Look at the top 5 cards of R&D and arrange them in any order. Subroutine You may draw 1 card. The Runner may pay 2 credits to draw 1 card. Subroutine Do 1 net damage.", "stripped_title": "Anansi", "text": "Whenever an encounter with this ice ends, if the Runner did not fully break it, do 3 net damage.\n[subroutine] Look at the top 5 cards of R&D and arrange them in any order.\n[subroutine] You may draw 1 card. The Runner may pay 2[credit] to draw 1 card.\n[subroutine] Do 1 net damage.", "title": "Anansi", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sadaka_21073(Ice):
    '''
    Cost: 2
    Text: Subroutine Look at the top 3 cards of R&D and either arrange them in any order or shuffle R&D. You may draw 1 card. Subroutine You may trash 1 card in HQ. If you do, trash 1 resource. Trash Sadaka.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21073", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Mariusz Siergiejew", "keywords": "Trap", "pack_code": "tdatd", "position": 73, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Look at the top 3 cards of R&D and either arrange them in any order or shuffle R&D. You may draw 1 card. Subroutine You may trash 1 card in HQ. If you do, trash 1 resource. Trash Sadaka.", "stripped_title": "Sadaka", "text": "[subroutine] Look at the top 3 cards of R&D and either arrange them in any order or shuffle R&D. You may draw 1 card.\n[subroutine] You may trash 1 card in HQ. If you do, trash 1 resource. Trash Sadaka.", "title": "Sadaka", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_endless_eula_21074(Ice):
    '''
    Cost: 6
    Text: Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21074", "cost": 6, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Has anyone ever actually read one of these things?\" - 419", "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "tdatd", "position": 74, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit. Subroutine End the run unless the Runner pays 1 credit.", "stripped_title": "Endless EULA", "text": "[subroutine]End the run unless the Runner pays 1[credit].\n[subroutine]End the run unless the Runner pays 1[credit].\n[subroutine]End the run unless the Runner pays 1[credit].\n[subroutine]End the run unless the Runner pays 1[credit].\n[subroutine]End the run unless the Runner pays 1[credit].\n[subroutine]End the run unless the Runner pays 1[credit].", "title": "Endless EULA", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sandman_21075(Ice):
    '''
    Cost: 5
    Text: Subroutine Add an installed Runner card to the grip. Subroutine Add an installed Runner card to the grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21075", "cost": 5, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "Your first dog, your favorite food, your own mother's name. Your love, your hate, your fear. Hopes and dreams, pain and sorrow. All of it, everything, slips away.", "illustrator": "Pavel Kolomeyets", "keywords": "Code Gate", "pack_code": "tdatd", "position": 75, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Add an installed Runner card to the grip. Subroutine Add an installed Runner card to the grip.", "stripped_title": "Sandman", "text": "[subroutine]Add an installed Runner card to the grip.\n[subroutine]Add an installed Runner card to the grip.", "title": "Sandman", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_oduduwa_21079(Ice):
    '''
    Cost: 7
    Text: When the Runner encounters Oduduwa, place 1 advancement token on it. You may place X advancement tokens on another piece of ice. X is the number of advancement tokens on Oduduwa. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21079", "cost": 7, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 5, "flavor": "Might given form.", "illustrator": "Le Vuong", "keywords": "Code Gate", "pack_code": "tdatd", "position": 79, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When the Runner encounters Oduduwa, place 1 advancement token on it. You may place X advancement tokens on another piece of ice. X is the number of advancement tokens on Oduduwa. Subroutine End the run. Subroutine End the run.", "stripped_title": "Oduduwa", "text": "When the Runner encounters Oduduwa, place 1 advancement token on it. You may place X advancement tokens on another piece of ice. X is the number of advancement tokens on Oduduwa.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Oduduwa", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_kamali_10_21092(Ice):
    '''
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage unless the Runner trashes 1 installed resource. Subroutine Do 1 core damage unless the Runner trashes 1 installed piece of hardware. Subroutine Do 1 core damage unless the Runner trashes 1 installed program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21092", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "illustrator": "Donald Crank", "keywords": "Sentry - Bioroid - Destroyer - AP", "pack_code": "win", "position": 92, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage unless the Runner trashes 1 installed resource. Subroutine Do 1 core damage unless the Runner trashes 1 installed piece of hardware. Subroutine Do 1 core damage unless the Runner trashes 1 installed program.", "stripped_title": "Kamali 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage unless the Runner trashes 1 installed resource.\n[subroutine] Do 1 core damage unless the Runner trashes 1 installed piece of hardware.\n[subroutine] Do 1 core damage unless the Runner trashes 1 installed program.", "title": "Kamali 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_envelope_21095(Ice):
    '''
    Cost: 4
    Text: Subroutine Do 1 net damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21095", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"On one hand, I knew I shouldn't touch it. On the other, it was really shiny.\" - Kabonesa Wu", "illustrator": "Pavel Kolomeyets", "keywords": "Barrier - AP", "pack_code": "win", "position": 95, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Do 1 net damage. Subroutine End the run.", "stripped_title": "Envelope", "text": "[subroutine] Do 1 net damage.\n[subroutine] End the run.", "title": "Envelope", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_masvingo_21099(Ice):
    '''
    Cost: 3
    Text: Masvingo can be advanced. When you rez Masvingo, place 1 advancement token on it. Masvingo gains "Subroutine End the run." for each advancement token on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21099", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "No matter which direction ze climbed, the blocks reshuffled, zipping in from left to right, bottom to top. It was going to be a long hike.", "illustrator": "Pavel Kolomeyets", "keywords": "Barrier", "pack_code": "win", "position": 99, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Masvingo can be advanced. When you rez Masvingo, place 1 advancement token on it. Masvingo gains \"Subroutine End the run.\" for each advancement token on it.", "stripped_title": "Masvingo", "text": "Masvingo can be advanced.\nWhen you rez Masvingo, place 1 advancement token on it.\nMasvingo gains \"[subroutine] End the run.\" for each advancement token on it.", "title": "Masvingo", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_next_diamond_21112(Ice):
    '''
    Cost: 10
    Text: This rez cost of this ice is lowered by 1 credit for each other rezzed piece of NEXT ice. Subroutine Do 1 core damage. Subroutine Do 1 core damage. Subroutine Trash 1 installed Runner card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21112", "cost": 10, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "Defenses that last forever.", "illustrator": "Ed Mattinian", "keywords": "Sentry - NEXT - Destroyer - AP", "pack_code": "ka", "position": 112, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "This rez cost of this ice is lowered by 1 credit for each other rezzed piece of NEXT ice. Subroutine Do 1 core damage. Subroutine Do 1 core damage. Subroutine Trash 1 installed Runner card.", "stripped_title": "NEXT Diamond", "text": "This rez cost of this ice is lowered by 1[credit] for each other rezzed piece of <strong>NEXT</strong> ice.\n[subroutine] Do 1 core damage.\n[subroutine] Do 1 core damage.\n[subroutine] Trash 1 installed Runner card.", "title": "NEXT Diamond", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_mlinzi_21115(Ice):
    '''
    Cost: 7
    Text: Subroutine Do 1 net damage unless the Runner trashes the top 2 cards of the stack. Subroutine Do 2 net damage unless the Runner trashes the top 3 cards of the stack. Subroutine Do 3 net damage unless the Runner trashes the top 4 cards of the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21115", "cost": 7, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Andreas Zafiratos", "keywords": "Sentry - AP", "pack_code": "ka", "position": 115, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Do 1 net damage unless the Runner trashes the top 2 cards of the stack. Subroutine Do 2 net damage unless the Runner trashes the top 3 cards of the stack. Subroutine Do 3 net damage unless the Runner trashes the top 4 cards of the stack.", "stripped_title": "Mlinzi", "text": "[subroutine] Do 1 net damage unless the Runner trashes the top 2 cards of the stack.\n[subroutine] Do 2 net damage unless the Runner trashes the top 3 cards of the stack.\n[subroutine] Do 3 net damage unless the Runner trashes the top 4 cards of the stack.", "title": "Mlinzi", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_surveyor_21118(Ice):
    '''
    Cost: 5
    Text: X is twice the number of ice protecting this server. Subroutine Trace[X]. If successful, give the Runner 2 tags. Subroutine Trace[X]. If successful, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21118", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "INTRUDER ALERT!\nINTRUDER ALERT!\nINTRUDER NEUTRALIZED!", "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Tracer", "pack_code": "ka", "position": 118, "quantity": 3, "side_code": "corp", "strength": null, "stripped_text": "X is twice the number of ice protecting this server. Subroutine Trace[X]. If successful, give the Runner 2 tags. Subroutine Trace[X]. If successful, end the run.", "stripped_title": "Surveyor", "text": "X is twice the number of ice protecting this server.\n[subroutine]Trace[X]. If successful, give the Runner 2 tags.\n[subroutine]Trace[X]. If successful, end the run.", "title": "Surveyor", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_meridian_22028(Ice):
    '''
    Cost: 3
    Text: Subroutine Gain 4 credits and end the run unless the Runner adds this ice to their score area as an agenda worth -1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22028", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "You don't cross it\u2014it crosses you.", "illustrator": "Adam S. Doyle", "keywords": "Barrier", "pack_code": "rar", "position": 28, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Gain 4 credits and end the run unless the Runner adds this ice to their score area as an agenda worth -1 agenda point.", "stripped_title": "Meridian", "text": "[subroutine] Gain 4[credit] and end the run unless the Runner adds this ice to their score area as an agenda worth -1 agenda point.", "title": "Meridian", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_gatekeeper_22029(Ice):
    '''
    Cost: 3
    Text: Gatekeeper has +6 strength if you rezzed it this turn. Subroutine Draw up to 3 cards. Reveal up to 3 agendas in HQ and/or Archives, then shuffle those agendas into R&D. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22029", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Banana who?", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate", "pack_code": "rar", "position": 29, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Gatekeeper has +6 strength if you rezzed it this turn. Subroutine Draw up to 3 cards. Reveal up to 3 agendas in HQ and/or Archives, then shuffle those agendas into R&D. Subroutine End the run.", "stripped_title": "Gatekeeper", "text": "Gatekeeper has +6 strength if you rezzed it this turn.\n[subroutine] Draw up to 3 cards. Reveal up to 3 agendas in HQ and/or Archives, then shuffle those agendas into R&D.\n[subroutine] End the run.", "title": "Gatekeeper", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_otoroshi_22038(Ice):
    '''
    Cost: 2
    Text: Subroutine You may place up to 3 advancement counters on 1 card installed in the root of a remote server. If you do, the Runner accesses that card unless they pay 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22038", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"If the sysop offers you a link, it's because they want you to go there. But if you wanted to go where the sysop suggested, you wouldn't be trying to break in at all.\" -How Not to Get Fragged", "illustrator": "Adam S. Doyle", "keywords": "Sentry", "pack_code": "rar", "position": 38, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine You may place up to 3 advancement counters on 1 card installed in the root of a remote server. If you do, the Runner accesses that card unless they pay 3 credits.", "stripped_title": "Otoroshi", "text": "[subroutine] You may place up to 3 advancement counters on 1 card installed in the root of a remote server. If you do, the Runner accesses that card unless they pay 3[credit].", "title": "Otoroshi", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_thimblerig_22039(Ice):
    '''
    Cost: 2
    Text: When your turn begins and whenever the Runner passes this ice, you may swap this ice with another installed piece of ice. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22039", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Step right up!", "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "rar", "position": 39, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "When your turn begins and whenever the Runner passes this ice, you may swap this ice with another installed piece of ice. Subroutine End the run.", "stripped_title": "Thimblerig", "text": "When your turn begins and whenever the Runner passes this ice, you may swap this ice with another installed piece of ice.\n[subroutine] End the run.", "title": "Thimblerig", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_peeping_tom_22045(Ice):
    '''
    Cost: 4
    Text: When the Runner encounters this ice, choose a card type, then reveal all cards in the grip. For the remainder of this run, this ice gains "Subroutine End the run unless the Runner takes 1 tag." for each revealed card of the chosen type.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22045", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"I lost the staring contest. And all seven rematches.\" -Kabonesa Wu", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate", "pack_code": "rar", "position": 45, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters this ice, choose a card type, then reveal all cards in the grip. For the remainder of this run, this ice gains \"Subroutine End the run unless the Runner takes 1 tag.\" for each revealed card of the chosen type.", "stripped_title": "Peeping Tom", "text": "When the Runner encounters this ice, choose a card type, then reveal all cards in the grip. For the remainder of this run, this ice gains \"[subroutine] End the run unless the Runner takes 1 tag.\" for each revealed card of the chosen type.", "title": "Peeping Tom", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hydra_22046(Ice):
    '''
    Cost: 10
    Text: Subroutine Do 3 net damage if the Runner is tagged; otherwise, give the Runner 1 tag. Subroutine Gain 5 credits if the Runner is tagged; otherwise, give the Runner 1 tag. Subroutine End the run if the Runner is tagged; otherwise, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22046", "cost": 10, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - AP", "pack_code": "rar", "position": 46, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "Subroutine Do 3 net damage if the Runner is tagged; otherwise, give the Runner 1 tag. Subroutine Gain 5 credits if the Runner is tagged; otherwise, give the Runner 1 tag. Subroutine End the run if the Runner is tagged; otherwise, give the Runner 1 tag.", "stripped_title": "Hydra", "text": "[subroutine] Do 3 net damage if the Runner is tagged; otherwise, give the Runner 1 tag.\n[subroutine] Gain 5[credit] if the Runner is tagged; otherwise, give the Runner 1 tag.\n[subroutine] End the run if the Runner is tagged; otherwise, give the Runner 1 tag.\n", "title": "Hydra", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_blockchain_22053(Ice):
    '''
    Cost: 7
    Text: Blockchain gains "Subroutine The Corp gains 1 credit and the Runner loses 1 credit." before all its other subroutines for every 2 faceup transaction operations in Archives. Subroutine The Corp gains 1 credit and the Runner loses 1 credit. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22053", "cost": 7, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "Marius Siergiejew", "keywords": "Barrier", "pack_code": "rar", "position": 53, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Blockchain gains \"Subroutine The Corp gains 1 credit and the Runner loses 1 credit.\" before all its other subroutines for every 2 faceup transaction operations in Archives. Subroutine The Corp gains 1 credit and the Runner loses 1 credit. Subroutine End the run.", "stripped_title": "Blockchain", "text": "Blockchain gains \"[subroutine] The Corp gains 1[credit] and the Runner loses 1[credit].\" before all its other subroutines for every 2 faceup <strong>transaction</strong> operations in Archives.\n[subroutine] The Corp gains 1[credit] and the Runner loses 1[credit].\n[subroutine] End the run.", "title": "Blockchain", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_formicary_22054(Ice):
    '''
    Cost: 2
    Text: Whenever the Runner approaches a server, you may rez this ice. If you do, move this ice to the innermost position protecting the approached server. The Runner moves to this ice and encounters it. Subroutine End the run unless the Runner suffers 2 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22054", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "A place of decay and death, a plane out of phase, a place of monsters.", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - AP", "pack_code": "rar", "position": 54, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Whenever the Runner approaches a server, you may rez this ice. If you do, move this ice to the innermost position protecting the approached server. The Runner moves to this ice and encounters it. Subroutine End the run unless the Runner suffers 2 net damage.", "stripped_title": "Formicary", "text": "Whenever the Runner approaches a server, you may rez this ice. If you do, move this ice to the innermost position protecting the approached server. The Runner moves to this ice and encounters it.\n[subroutine] End the run unless the Runner suffers 2 net damage.", "title": "Formicary", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_slot_machine_23045(Ice):
    '''
    Cost: 3
    Text: When the Runner encounters this ice, they put the top card of the stack on the bottom, then you reveal the top 3 cards of the stack. Subroutine The Runner loses 3 credits. Subroutine If you revealed 2 or more cards that share a type when this encounter began, gain 3 credits. Subroutine If you revealed 3 or more cards that share a type when this encounter began, place 3 advancement tokens on an installed card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "23045", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "<strong>Designed by 2017 World Champion Jess Horig</strong>", "illustrator": "Ed Mattinian", "keywords": "Code Gate", "pack_code": "mo", "position": 3, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When the Runner encounters this ice, they put the top card of the stack on the bottom, then you reveal the top 3 cards of the stack. Subroutine The Runner loses 3 credits. Subroutine If you revealed 2 or more cards that share a type when this encounter began, gain 3 credits. Subroutine If you revealed 3 or more cards that share a type when this encounter began, place 3 advancement tokens on an installed card.", "stripped_title": "Slot Machine", "text": "When the Runner encounters this ice, they put the top card of the stack on the bottom, then you reveal the top 3 cards of the stack.\n[subroutine] The Runner loses 3[credit].\n[subroutine] If you revealed 2 or more cards that share a type when this encounter began, gain 3[credit].\n[subroutine] If you revealed 3 or more cards that share a type when this encounter began, place 3 advancement tokens on an installed card.", "title": "Slot Machine", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_border_control_23054(Ice):
    '''
    Cost: 4
    Text: trash: End the run. Use this ability only during a run on this server. Subroutine Gain 1 credit for each piece of ice protecting this server. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "23054", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "<strong>Designed by 2016 World Champion Chris Dyer</strong>", "illustrator": "Adam S. Doyle", "keywords": "Barrier", "pack_code": "mo", "position": 4, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "trash: End the run. Use this ability only during a run on this server. Subroutine Gain 1 credit for each piece of ice protecting this server. Subroutine End the run.", "stripped_title": "Border Control", "text": "[trash]: End the run. Use this ability only during a run on this server.\n[subroutine] Gain 1[credit] for each piece of ice protecting this server.\n[subroutine] End the run.", "title": "Border Control", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_eli_10_25073(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25073", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "\"That's against the rules. The Creators will be angry.\"", "illustrator": "Sandara Tang", "keywords": "Barrier - Bioroid", "pack_code": "sc19", "position": 73, "quantity": 2, "side_code": "corp", "strength": 4, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.", "stripped_title": "Eli 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Eli 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_heimdall_10_25074(Ice):
    '''
    Cost: 8
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25074", "cost": 8, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "I hear the shift of every bit amid the flow of the datastream. I hear the whispers of my mothers, and their commands are law. The realm beyond is forbidden.", "illustrator": "Andreas Zafiratos", "keywords": "Barrier - Bioroid - AP", "pack_code": "sc19", "position": 74, "quantity": 1, "side_code": "corp", "strength": 6, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run. Subroutine End the run.", "stripped_title": "Heimdall 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Heimdall 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ichi_10_25075(Ice):
    '''
    Cost: 5
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25075", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "My reputation would precede me, if any could speak of it.", "illustrator": "Andreas Zafiratos", "keywords": "Sentry - Bioroid - Tracer - Destroyer", "pack_code": "sc19", "position": 75, "quantity": 2, "side_code": "corp", "strength": 4, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.", "stripped_title": "Ichi 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.\n[subroutine] Trace[1]. If successful, do 1 core damage and give the Runner 1 tag.", "title": "Ichi 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_rototurret_25076(Ice):
    '''
    Cost: 4
    Text: Subroutine Trash 1 installed program. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25076", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Whrrrrr!", "illustrator": "Ed Mattinian", "keywords": "Sentry - Destroyer", "pack_code": "sc19", "position": 76, "quantity": 2, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine Trash 1 installed program. Subroutine End the run.", "stripped_title": "Rototurret", "text": "[subroutine] Trash 1 installed program.\n[subroutine] End the run.", "title": "Rototurret", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_turing_25077(Ice):
    '''
    Cost: 4
    Text: Turing has +3 strength while protecting a remote server. The Runner cannot use AI programs to break subroutines on Turing. Subroutine End the run unless the Runner spends click click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25077", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "Alan Turing laid the foundation for artificial intelligence by suggesting that you could teach a computer to be human.", "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "sc19", "position": 77, "quantity": 1, "side_code": "corp", "strength": 2, "stripped_text": "Turing has +3 strength while protecting a remote server. The Runner cannot use AI programs to break subroutines on Turing. Subroutine End the run unless the Runner spends click click click.", "stripped_title": "Turing", "text": "Turing has +3 strength while protecting a remote server.\nThe Runner cannot use <strong>AI</strong> programs to break subroutines on Turing.\n[subroutine] End the run unless the Runner spends [click][click][click].", "title": "Turing", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_viktor_10_25078(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25078", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "My name is Viktor. Nice to meet you. Would you like to play a game?", "illustrator": "Andreas Zafiratos", "keywords": "Code Gate - Bioroid - AP", "pack_code": "sc19", "position": 78, "quantity": 2, "side_code": "corp", "strength": 3, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.", "stripped_title": "Viktor 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] End the run.", "title": "Viktor 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_himitsubako_25093(Ice):
    '''
    Cost: 2
    Text: 1 credit: Add Himitsu-Bako to HQ. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25093", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Himitsu-Bako is a simple ice barrier that appears as a digital puzzle box. What makes it special is the ease with which it can be uninstalled and installed in a different server, throwing up barriers in unexpected places and giving any intruder a curious feeling of d\u00e9j\u00e0 vu.", "illustrator": "Andrew Mar", "keywords": "Barrier", "pack_code": "sc19", "position": 93, "quantity": 1, "side_code": "corp", "strength": 2, "stripped_text": "1 credit: Add Himitsu-Bako to HQ. Subroutine End the run.", "stripped_title": "Himitsu-Bako", "text": "1[credit]: Add Himitsu-Bako to HQ.\n[subroutine] End the run.", "title": "Himitsu-Bako", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_lotus_field_25094(Ice):
    '''
    Cost: 5
    Text: The strength of this ice cannot be lowered. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25094", "cost": 5, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"Chi resonance mapping has created a whole new field of network security. It is unassailable perfection.\" -Akitaro Watanabe", "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "sc19", "position": 94, "quantity": 1, "side_code": "corp", "strength": 4, "stripped_text": "The strength of this ice cannot be lowered. Subroutine End the run.", "stripped_title": "Lotus Field", "text": "The strength of this ice cannot be lowered.\n[subroutine] End the run.", "title": "Lotus Field", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_neural_katana_25095(Ice):
    '''
    Cost: 4
    Text: Subroutine Do 3 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25095", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Forged by Ak.wa on 23.11.79-23. Filed 23.11.79-23.2 with #34k-lw3-21HH-4i.\n//Samurai included.", "illustrator": "Isuardi Therianto", "keywords": "Sentry - AP", "pack_code": "sc19", "position": 95, "quantity": 2, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Do 3 net damage.", "stripped_title": "Neural Katana", "text": "[subroutine] Do 3 net damage.", "title": "Neural Katana", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_swordsman_25096(Ice):
    '''
    Cost: 3
    Text: The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25096", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Writing a program that can pass the Turing test is easy. The Gibson-Akamatsu test is a higher bar, and the only AIs to clear it thus far have been the androids. Even some humans have been known to fail.", "illustrator": "Adam S. Doyle", "keywords": "Sentry - AP - Destroyer", "pack_code": "sc19", "position": 96, "quantity": 1, "side_code": "corp", "strength": 2, "stripped_text": "The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.", "stripped_title": "Swordsman", "text": "The Runner cannot break subroutines on this ice using <strong>AI</strong> programs.\n[subroutine] Trash 1 installed <strong>AI</strong> program.\n[subroutine] Do 1 net damage.", "title": "Swordsman", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tsurugi_25097(Ice):
    '''
    Cost: 6
    Text: Subroutine End the run unless the Corp pays 1 credit. Subroutine Do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25097", "cost": 6, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"It's ice so dangerous it has safety protocols. Think about that.\" -g00ru", "illustrator": "Adam S. Doyle", "keywords": "Sentry - AP", "pack_code": "sc19", "position": 97, "quantity": 2, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine End the run unless the Corp pays 1 credit. Subroutine Do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage.", "stripped_title": "Tsurugi", "text": "[subroutine] End the run unless the Corp pays 1[credit].\n[subroutine] Do 1 net damage.\n[subroutine] Do 1 net damage.\n[subroutine] Do 1 net damage.", "title": "Tsurugi", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wall_of_thorns_25098(Ice):
    '''
    Cost: 8
    Text: Subroutine Do 2 net damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25098", "cost": 8, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Most runners do their business in full-sim, with their rigs wired directly into their brains. The setup has a large number of advantages, with the runner able to process data and input commands far faster than a traditional meat-bound system. But it also means greater risk.", "illustrator": "Adam S. Doyle", "keywords": "Barrier - AP", "pack_code": "sc19", "position": 98, "quantity": 1, "side_code": "corp", "strength": 5, "stripped_text": "Subroutine Do 2 net damage. Subroutine End the run.", "stripped_title": "Wall of Thorns", "text": "[subroutine] Do 2 net damage.\n[subroutine] End the run.", "title": "Wall of Thorns", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_yagura_25099(Ice):
    '''
    Cost: 1
    Text: Subroutine Look at the top card of R&D. You may add that card to the bottom of R&D. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25099", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "The 'cyber-war' is a war of information, and in a war of information, advance warning can be as good as a killing blow. -Michael Muhama, Musings on Cybercrime", "illustrator": "Andrew Mar", "keywords": "Code Gate - AP", "pack_code": "sc19", "position": 99, "quantity": 2, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine Look at the top card of R&D. You may add that card to the bottom of R&D. Subroutine Do 1 net damage.", "stripped_title": "Yagura", "text": "[subroutine] Look at the top card of R&D. You may add that card to the bottom of R&D.\n[subroutine] Do 1 net damage.", "title": "Yagura", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_data_raven_25112(Ice):
    '''
    Cost: 4
    Text: When the Runner encounters this ice, they must take 1 tag or end the run. Hosted power counter: Give the Runner 1 tag. Subroutine Trace[3]. If successful, place 1 power counter on this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25112", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - Tracer - Observer", "pack_code": "sc19", "position": 112, "quantity": 2, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters this ice, they must take 1 tag or end the run. Hosted power counter: Give the Runner 1 tag. Subroutine Trace[3]. If successful, place 1 power counter on this ice.", "stripped_title": "Data Raven", "text": "When the Runner encounters this ice, they must take 1 tag or end the run.\n<strong>Hosted power counter:</strong> Give the Runner 1 tag.\n[subroutine] Trace[3]. If successful, place 1 power counter on this ice.", "title": "Data Raven", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_flare_25113(Ice):
    '''
    Cost: 9
    Text: Subroutine Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25113", "cost": 9, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "A bright light blossomed, and then the console went dark. That's when she smelled smoke.", "illustrator": "Mike Nesbitt", "keywords": "Sentry - Tracer - AP", "pack_code": "sc19", "position": 113, "quantity": 1, "side_code": "corp", "strength": 6, "stripped_text": "Subroutine Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.", "stripped_title": "Flare", "text": "[subroutine]Trace[6]. If successful, trash 1 piece of hardware, do 2 meat damage (cannot be prevented), and end the run.", "title": "Flare", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_popup_window_25114(Ice):
    '''
    Cost: 0
    Text: When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25114", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"Try to close it. Go on. See what it does.\" -Chaos Theory", "illustrator": "Christina Davis", "keywords": "Code Gate - Advertisement", "pack_code": "sc19", "position": 114, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.", "stripped_title": "Pop-up Window", "text": "When the Runner encounters this ice, gain 1[credit].\n[subroutine] End the run unless the Runner pays 1[credit].", "title": "Pop-up Window", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tollbooth_25115(Ice):
    '''
    Cost: 8
    Text: When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25115", "cost": 8, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Ever heard of a catch-22?\"\n\"Remind me to forget it.\"", "illustrator": "Outland Entertainment LLC", "keywords": "Code Gate", "pack_code": "sc19", "position": 115, "quantity": 2, "side_code": "corp", "strength": 5, "stripped_text": "When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.", "stripped_title": "Tollbooth", "text": "When the Runner encounters this ice, they must pay 3[credit], if able. If they do not, end the run.\n[subroutine] End the run.", "title": "Tollbooth", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wraparound_25116(Ice):
    '''
    Cost: 2
    Text: While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25116", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"It can make a real fine roller coaster, provided you're properly stimmed up.\" -Noise", "illustrator": "Ed Mattinian", "keywords": "Barrier", "pack_code": "sc19", "position": 116, "quantity": 1, "side_code": "corp", "strength": 0, "stripped_text": "While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.", "stripped_title": "Wraparound", "text": "While there are no installed <strong>fracter</strong> programs, this ice gets +7 strength.\n[subroutine] End the run.", "title": "Wraparound", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_archer_25130(Ice):
    '''
    Cost: 4
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25130", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Next time, read the Terms of Service more carefully. Or you might find yourself in the danger zone.", "illustrator": "Mike Nesbitt", "keywords": "Sentry - Destroyer", "pack_code": "sc19", "position": 130, "quantity": 2, "side_code": "corp", "strength": 6, "stripped_text": "As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.", "stripped_title": "Archer", "text": "As an additional cost to rez this ice, forfeit 1 agenda.\n[subroutine] Gain 2[credit].\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.\n[subroutine] End the run.", "title": "Archer", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_caduceus_25131(Ice):
    '''
    Cost: 3
    Text: Subroutine Trace[3]. If successful, the Corp gains 3 credits. Subroutine Trace[2]. If successful, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25131", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "A symbol of commerce, but beware its bite.", "illustrator": "Christina Davis", "keywords": "Sentry - Tracer", "pack_code": "sc19", "position": 131, "quantity": 2, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Trace[3]. If successful, the Corp gains 3 credits. Subroutine Trace[2]. If successful, end the run.", "stripped_title": "Caduceus", "text": "[subroutine] Trace[3]. If successful, the Corp gains 3[credit].\n[subroutine] Trace[2]. If successful, end the run.", "title": "Caduceus", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hadrians_wall_25132(Ice):
    '''
    Cost: 10
    Text: Hadrian's Wall can be advanced and has +1 strength for each advancement token on it. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25132", "cost": 10, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "\"He had a bit of an ego, ol' Hadrian. His constructs live up to it though.\" -g00ru", "illustrator": "Liiga Smilshkalne", "keywords": "Barrier", "pack_code": "sc19", "position": 132, "quantity": 1, "side_code": "corp", "strength": 7, "stripped_text": "Hadrian's Wall can be advanced and has +1 strength for each advancement token on it. Subroutine End the run. Subroutine End the run.", "stripped_title": "Hadrian's Wall", "text": "Hadrian's Wall can be advanced and has +1 strength for each advancement token on it.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Hadrian's Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hortum_25133(Ice):
    '''
    Cost: 4
    Text: You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using AI programs. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 4 credits. Subroutine End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25133", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Code Gate", "pack_code": "sc19", "position": 133, "quantity": 1, "side_code": "corp", "strength": 4, "stripped_text": "You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using AI programs. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 4 credits. Subroutine End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.", "stripped_title": "Hortum", "text": "You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using <strong>AI</strong> programs.\n[subroutine] Gain 1[credit]. If there are 3 or more hosted advancement counters, instead gain 4[credit].\n[subroutine] End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.", "title": "Hortum", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ice_wall_25134(Ice):
    '''
    Cost: 1
    Text: You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25134", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"I asked for ice as impenetrable as a wall. I can't decide if someone down in R&D has a warped sense of humor or just a very literal mind.\" -Liz Campbell, VP Project Security", "illustrator": "Matt Zeilinger", "keywords": "Barrier", "pack_code": "sc19", "position": 134, "quantity": 2, "side_code": "corp", "strength": 1, "stripped_text": "You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.", "stripped_title": "Ice Wall", "text": "You can advance this ice. It gets +1 strength for each hosted advancement counter.\n[subroutine] End the run.", "title": "Ice Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_spiderweb_25135(Ice):
    '''
    Cost: 4
    Text: Subroutine End the run. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25135", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"Let me tell you a secret. There's no such thing as impenetrable ice. It has to allow access, or else why is the server on the Network in the first place? But that doesn't mean they have to make it easy.\" -g00ru", "illustrator": "Laura Wilson", "keywords": "Barrier", "pack_code": "sc19", "position": 135, "quantity": 2, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine End the run. Subroutine End the run. Subroutine End the run.", "stripped_title": "Spiderweb", "text": "[subroutine] End the run.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Spiderweb", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_enigma_25143(Ice):
    '''
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25143", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Hey, hey! Wake up, man. You were under a long time. What'd you see?\"\n\"I\u2026don't remember.\"", "illustrator": "Liiga Smilshkalne", "keywords": "Code Gate", "pack_code": "sc19", "position": 143, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine The Runner loses click. Subroutine End the run.", "stripped_title": "Enigma", "text": "[subroutine] The Runner loses [click].\n[subroutine] End the run.", "title": "Enigma", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hunter_25144(Ice):
    '''
    Cost: 1
    Text: Subroutine Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25144", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": ".//run/hunter-tr/return=true\nclient/sec256IPv7->confirm? /y\n3926:0HB7:1001:2NB1:1601:7784:ERROR", "illustrator": "Christina Davis", "keywords": "Sentry - Tracer - Observer", "pack_code": "sc19", "position": 144, "quantity": 2, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "Hunter", "text": "[subroutine] Trace[3]. If successful, give the Runner 1 tag.", "title": "Hunter", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wall_of_static_25145(Ice):
    '''
    Cost: 3
    Text: Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25145", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"There's nothing worse than seeing that beautiful blue ball of data just out of reach as your connection derezzes. I think they do it just to taunt us.\" -Ele \"Smoke\" Scovak", "illustrator": "Adam S. Doyle", "keywords": "Barrier", "pack_code": "sc19", "position": 145, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine End the run.", "stripped_title": "Wall of Static", "text": "[subroutine] End the run.", "title": "Wall of Static", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hagen_26035(Ice):
    '''
    Cost: 4
    Text: This ice has -1 strength for each installed icebreaker. Subroutine Trash 1 program that is not a decoder, fracter, or killer. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26035", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "Old warriors have seen all the tricks; be forthright or fail.", "illustrator": "Krembler", "keywords": "Barrier - Destroyer", "pack_code": "df", "position": 35, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "This ice has -1 strength for each installed icebreaker. Subroutine Trash 1 program that is not a decoder, fracter, or killer. Subroutine End the run.", "stripped_title": "Hagen", "text": "This ice has -1 strength for each installed <strong>icebreaker</strong>.\n[subroutine] Trash 1 program that is not a <strong>decoder</strong>, <strong>fracter</strong>, or <strong>killer</strong>.\n[subroutine] End the run.", "title": "Hagen", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_saisentan_26044(Ice):
    '''
    Cost: 5
    Text: When the Runner encounters this ice, choose a card type. For the remainder of the encounter, whenever you trash a card of that type with net damage from a subroutine on this ice, do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26044", "cost": 5, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Krembler", "keywords": "Sentry - AP - Observer", "pack_code": "df", "position": 44, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "When the Runner encounters this ice, choose a card type. For the remainder of the encounter, whenever you trash a card of that type with net damage from a subroutine on this ice, do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage. Subroutine Do 1 net damage.", "stripped_title": "Saisentan", "text": "When the Runner encounters this ice, choose a card type. For the remainder of the encounter, whenever you trash a card of that type with net damage from a subroutine on this ice, do 1 net damage.\n[subroutine] Do 1 net damage.\n[subroutine] Do 1 net damage.\n[subroutine] Do 1 net damage.", "title": "Saisentan", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_congratulations_26050(Ice):
    '''
    Cost: 1
    Text: When the Runner passes this ice, gain 1 credit. Subroutine Gain 2 credits. The Runner gains 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26050", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "You are the ONE BILLIONTH visitor!", "illustrator": "NtscapeNavigator", "keywords": "Code Gate - Advertisement", "pack_code": "df", "position": 50, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When the Runner passes this ice, gain 1 credit. Subroutine Gain 2 credits. The Runner gains 1 credit.", "stripped_title": "Congratulations!", "text": "When the Runner passes this ice, gain 1[credit].\n[subroutine]Gain 2[credit]. The Runner gains 1[credit].", "title": "Congratulations!", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_loot_box_26051(Ice):
    '''
    Cost: 0
    Text: Subroutine End the run unless the Runner pays 2 credits. Subroutine Reveal the top 3 cards of the stack. Add 1 of those cards to the grip and gain credits equal to its install or play cost. The Runner shuffles the stack. Trash this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26051", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Though many countries attempted to regulate digital loot boxes in the early 21st century, GameNET has managed to circumvent any such laws via explicit, transparent percentage rates... and some very determined lobbyists.", "illustrator": "Krembler", "keywords": "Trap", "pack_code": "df", "position": 51, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine End the run unless the Runner pays 2 credits. Subroutine Reveal the top 3 cards of the stack. Add 1 of those cards to the grip and gain credits equal to its install or play cost. The Runner shuffles the stack. Trash this ice.", "stripped_title": "Loot Box", "text": "[subroutine]End the run unless the Runner pays 2[credit].\n[subroutine]Reveal the top 3 cards of the stack. Add 1 of those cards to the grip and gain credits equal to its install or play cost. The Runner shuffles the stack. Trash this ice.", "title": "Loot Box", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_afshar_26058(Ice):
    '''
    Cost: 3
    Text: While this ice is protecting HQ, the Runner cannot break more than 1 of its printed subroutines during each encounter. Subroutine The Runner loses 2 credits. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26058", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "A choice occurs. The waveform collapses.", "illustrator": "Krembler", "keywords": "Code Gate", "pack_code": "df", "position": 58, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "While this ice is protecting HQ, the Runner cannot break more than 1 of its printed subroutines during each encounter. Subroutine The Runner loses 2 credits. Subroutine End the run.", "stripped_title": "Afshar", "text": "While this ice is protecting HQ, the Runner cannot break more than 1 of its printed subroutines during each encounter.\n[subroutine]The Runner loses 2[credit].\n[subroutine]End the run.", "title": "Afshar", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_sandstone_26059(Ice):
    '''
    Cost: 3
    Text: When the Runner encounters this ice, place 1 virus counter on it. This ice has -1 strength for each hosted virus counter. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26059", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Effective, Cheap, Durable. Pick two.", "illustrator": "Krembler", "keywords": "Barrier", "pack_code": "df", "position": 59, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "When the Runner encounters this ice, place 1 virus counter on it. This ice has -1 strength for each hosted virus counter. Subroutine End the run.", "stripped_title": "Sandstone", "text": "When the Runner encounters this ice, place 1 virus counter on it.\nThis ice has -1 strength for each hosted virus counter.\n[subroutine]End the run.", "title": "Sandstone", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_trebuchet_26060(Ice):
    '''
    Cost: 7
    Text: When you rez this ice, take 1 bad publicity. Subroutine Trash 1 installed Runner card. Subroutine Trace[6]. If successful, the Runner cannot steal or trash Corp cards for the remainder of the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26060", "cost": 7, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Iain Fairclough", "keywords": "Sentry - Illicit - Destroyer - Tracer", "pack_code": "df", "position": 60, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "When you rez this ice, take 1 bad publicity. Subroutine Trash 1 installed Runner card. Subroutine Trace[6]. If successful, the Runner cannot steal or trash Corp cards for the remainder of the run.", "stripped_title": "Trebuchet", "text": "When you rez this ice, take 1 bad publicity.\n[subroutine] Trash 1 installed Runner card.\n[subroutine] Trace[6]. If successful, the Runner cannot steal or trash Corp cards for the remainder of the run.", "title": "Trebuchet", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_rime_26065(Ice):
    '''
    Cost: 0
    Text: During runs on this server, you can rez this ice any time you could rez non-ice cards. Each piece of ice protecting this server has +1 strength. Subroutine The Runner loses 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26065", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "N. Hopkins", "keywords": "Mythic", "pack_code": "df", "position": 65, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "During runs on this server, you can rez this ice any time you could rez non-ice cards. Each piece of ice protecting this server has +1 strength. Subroutine The Runner loses 1 credit.", "stripped_title": "Rime", "text": "During runs on this server, you can rez this ice any time you could rez non-ice cards.\nEach piece of ice protecting this server has +1 strength.\n[subroutine] The Runner loses 1[credit].", "title": "Rime", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_drafter_26101(Ice):
    '''
    Cost: 3
    Text: Subroutine You may add 1 card from Archives to HQ. Subroutine You may install 1 card from Archives or HQ, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26101", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Each generation of design assistants makes a sysop's job easier. They need only speak and it will be so.", "illustrator": "Krembler", "keywords": "Sentry", "pack_code": "ur", "position": 101, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine You may add 1 card from Archives to HQ. Subroutine You may install 1 card from Archives or HQ, ignoring all costs.", "stripped_title": "Drafter", "text": "[subroutine] You may add 1 card from Archives to HQ.\n[subroutine] You may install 1 card from Archives or HQ, ignoring all costs.", "title": "Drafter", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tyr_26102(Ice):
    '''
    Cost: 10
    Text: Lose click: Break 1 subroutine on this ice. The Corp gets +1 allotted click for their next turn. Only the Runner can use this ability. Subroutine Do 2 core damage. Subroutine Trash 1 installed Runner card. Gain 3 credits. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26102", "cost": 10, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "flavor": "The valiant do not hesitate.", "illustrator": "Liiga Smilshkalne", "keywords": "Sentry - Bioroid - AP - Destroyer", "pack_code": "ur", "position": 102, "quantity": 3, "side_code": "corp", "strength": 7, "stripped_text": "Lose click: Break 1 subroutine on this ice. The Corp gets +1 allotted click for their next turn. Only the Runner can use this ability. Subroutine Do 2 core damage. Subroutine Trash 1 installed Runner card. Gain 3 credits. Subroutine End the run.", "stripped_title": "Tyr", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. The Corp gets +1 allotted [click] for their next turn. Only the Runner can use this ability.\n[subroutine] Do 2 core damage.\n[subroutine] Trash 1 installed Runner card. Gain 3[credit].\n[subroutine] End the run.", "title": "T\u00fdr", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_engram_flush_26108(Ice):
    '''
    Cost: 2
    Text: When the Runner encounters this ice, choose a card type. For the remainder of this encounter, whenever you reveal the grip with a subroutine on this ice, you may trash 1 revealed card of that type. Subroutine Reveal the grip. Subroutine Reveal the grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26108", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "$BMI.001 > Out of Memory Error", "illustrator": "Janet Bruesselbach", "keywords": "Code Gate - Observer", "pack_code": "ur", "position": 108, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When the Runner encounters this ice, choose a card type. For the remainder of this encounter, whenever you reveal the grip with a subroutine on this ice, you may trash 1 revealed card of that type. Subroutine Reveal the grip. Subroutine Reveal the grip.", "stripped_title": "Engram Flush", "text": "When the Runner encounters this ice, choose a card type. For the remainder of this encounter, whenever you reveal the grip with a subroutine on this ice, you may trash 1 revealed card of that type.\n[subroutine] Reveal the grip.\n[subroutine] Reveal the grip.", "title": "Engram Flush", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_konjin_26109(Ice):
    '''
    Cost: 3
    Text: When the Runner encounters this ice, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, you may force the Runner to encounter another rezzed piece of ice. (When that encounter ends, if the run has not ended, finish encountering this ice.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26109", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "\"The Konjin dons the mask of our fears, but what lies underneath?\"\n-Lat", "illustrator": "Krembler", "keywords": "Mythic - Psi", "pack_code": "ur", "position": 109, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When the Runner encounters this ice, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, you may force the Runner to encounter another rezzed piece of ice. (When that encounter ends, if the run has not ended, finish encountering this ice.)", "stripped_title": "Konjin", "text": "When the Runner encounters this ice, you and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, you may force the Runner to encounter another rezzed piece of ice. <em>(When that encounter ends, if the run has not ended, finish encountering this ice.)</em>", "title": "Konjin", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_f2p_26115(Ice):
    '''
    Cost: 4
    Text: 2 credits: Break 1 subroutine on this ice. Only the Runner can use this ability, and only if they are not tagged. Subroutine Add 1 installed Runner card to the grip. Subroutine Give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26115", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Free to Pay", "illustrator": "Krembler", "keywords": "Sentry", "pack_code": "ur", "position": 115, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "2 credits: Break 1 subroutine on this ice. Only the Runner can use this ability, and only if they are not tagged. Subroutine Add 1 installed Runner card to the grip. Subroutine Give the Runner 1 tag.", "stripped_title": "F2P", "text": "<strong>2[credit]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability, and only if they are not tagged.\n[subroutine] Add 1 installed Runner card to the grip.\n[subroutine] Give the Runner 1 tag.", "title": "F2P", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_gold_farmer_26116(Ice):
    '''
    Cost: 3
    Text: When the Runner breaks a printed subroutine on this ice, they lose 1 credit. Subroutine End the run unless the Runner pays 3 credits. Subroutine End the run unless the Runner pays 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26116", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "[Pay 15 gems to access this content]", "illustrator": "N. Hopkins", "keywords": "Barrier", "pack_code": "ur", "position": 116, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "When the Runner breaks a printed subroutine on this ice, they lose 1 credit. Subroutine End the run unless the Runner pays 3 credits. Subroutine End the run unless the Runner pays 3 credits.", "stripped_title": "Gold Farmer", "text": "When the Runner breaks a printed subroutine on this ice, they lose 1[credit].\n[subroutine] End the run unless the Runner pays 3[credit].\n[subroutine] End the run unless the Runner pays 3[credit].", "title": "Gold Farmer", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_akhet_26123(Ice):
    '''
    Cost: 3
    Text: You can advance this ice. While there are 3 or more hosted advancement tokens, this ice has +3 strength and the Runner cannot break more than 1 of its printed subroutines during each encounter. Subroutine Gain 1 credit. Place 1 advancement token on an installed card. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26123", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Thou slept not in thy house on earth.\nThou openest thy place in heaven.", "illustrator": "Owen Sinodov", "keywords": "Barrier", "pack_code": "ur", "position": 123, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "You can advance this ice. While there are 3 or more hosted advancement tokens, this ice has +3 strength and the Runner cannot break more than 1 of its printed subroutines during each encounter. Subroutine Gain 1 credit. Place 1 advancement token on an installed card. Subroutine End the run.", "stripped_title": "Akhet", "text": "You can advance this ice.\nWhile there are 3 or more hosted advancement tokens, this ice has +3 strength and the Runner cannot break more than 1 of its printed subroutines during each encounter.\n[subroutine] Gain 1[credit]. Place 1 advancement token on an installed card.\n[subroutine] End the run.", "title": "Akhet", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_colossus_26124(Ice):
    '''
    Cost: 6
    Text: You can advance this ice. It has +1 strength for each hosted advancement token. Subroutine Give the Runner 1 tag. If there are 3 or more hosted advancement tokens, instead give the Runner 2 tags. Subroutine Trash 1 installed program. If there are 3 or more hosted advancement tokens, instead trash 1 installed program and 1 installed resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26124", "cost": 6, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Krembler", "keywords": "Sentry - Destroyer", "pack_code": "ur", "position": 124, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "You can advance this ice. It has +1 strength for each hosted advancement token. Subroutine Give the Runner 1 tag. If there are 3 or more hosted advancement tokens, instead give the Runner 2 tags. Subroutine Trash 1 installed program. If there are 3 or more hosted advancement tokens, instead trash 1 installed program and 1 installed resource.", "stripped_title": "Colossus", "text": "You can advance this ice. It has +1 strength for each hosted advancement token.\n[subroutine] Give the Runner 1 tag. If there are 3 or more hosted advancement tokens, instead give the Runner 2 tags.\n[subroutine] Trash 1 installed program. If there are 3 or more hosted advancement tokens, instead trash 1 installed program and 1 installed resource.", "title": "Colossus", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_winchester_26125(Ice):
    '''
    Cost: 4
    Text: While this ice is protecting HQ, it gains "Subroutine Trace[3]. If successful, end the run." after all its other subroutines. Subroutine Trace[4]. If successful, trash 1 installed program. Subroutine Trace[3]. If successful, trash 1 installed piece of hardware.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26125", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "\"I don't know how Skorpios gets these designs past Brand Management.\"\n-Liz Campbell, VP Project Security", "illustrator": "NtscapeNavigator", "keywords": "Sentry - Tracer - Destroyer", "pack_code": "ur", "position": 125, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "While this ice is protecting HQ, it gains \"Subroutine Trace[3]. If successful, end the run.\" after all its other subroutines. Subroutine Trace[4]. If successful, trash 1 installed program. Subroutine Trace[3]. If successful, trash 1 installed piece of hardware.", "stripped_title": "Winchester", "text": "While this ice is protecting HQ, it gains \"[subroutine] Trace[3]. If successful, end the run.\" after all its other subroutines.\n[subroutine] Trace[4]. If successful, trash 1 installed program.\n[subroutine] Trace[3]. If successful, trash 1 installed piece of hardware.", "title": "Winchester", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_slot_machine_28004(Ice):
    '''
    Cost: 3
    Text: When the Runner encounters this ice, they put the top card of the stack on the bottom, then you reveal the top 3 cards of the stack. Subroutine The Runner loses 3 credits. Subroutine If you revealed 2 or more cards that share a type when this encounter began, gain 3 credits. Subroutine If you revealed 3 or more cards that share a type when this encounter began, place 3 advancement tokens on an installed card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "28004", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "<strong>Designed by 2017 World Champion Jess Horig</strong>", "illustrator": "Krembler", "keywords": "Code Gate", "pack_code": "mor", "position": 4, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When the Runner encounters this ice, they put the top card of the stack on the bottom, then you reveal the top 3 cards of the stack. Subroutine The Runner loses 3 credits. Subroutine If you revealed 2 or more cards that share a type when this encounter began, gain 3 credits. Subroutine If you revealed 3 or more cards that share a type when this encounter began, place 3 advancement tokens on an installed card.", "stripped_title": "Slot Machine", "text": "When the Runner encounters this ice, they put the top card of the stack on the bottom, then you reveal the top 3 cards of the stack.\n[subroutine] The Runner loses 3[credit].\n[subroutine] If you revealed 2 or more cards that share a type when this encounter began, gain 3[credit].\n[subroutine] If you revealed 3 or more cards that share a type when this encounter began, place 3 advancement tokens on an installed card.", "title": "Slot Machine", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_border_control_28005(Ice):
    '''
    Cost: 4
    Text: trash: End the run. Use this ability only during a run on this server. Subroutine Gain 1 credit for each piece of ice protecting this server. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "28005", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "<strong>Designed by 2016 World Champion Chris Dyer</strong>", "illustrator": "NtscapeNavigator", "keywords": "Barrier", "pack_code": "mor", "position": 5, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "trash: End the run. Use this ability only during a run on this server. Subroutine Gain 1 credit for each piece of ice protecting this server. Subroutine End the run.", "stripped_title": "Border Control", "text": "[trash]: End the run. Use this ability only during a run on this server.\n[subroutine] Gain 1[credit] for each piece of ice protecting this server.\n[subroutine] End the run.", "title": "Border Control", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_next_bronze_29009(Ice):
    '''
    Cost: 2
    Text: NEXT Bronze has +1 strength for each rezzed piece of NEXT ice. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29009", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "NEXT Design's ice provides the discerning business with a suite of ice that creates a daunting security presence for intruders.", "illustrator": "Ed Mattinian", "keywords": "Code Gate - NEXT", "pack_code": "sm", "position": 9, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "NEXT Bronze has +1 strength for each rezzed piece of NEXT ice. Subroutine End the run.", "stripped_title": "NEXT Bronze", "text": "NEXT Bronze has +1 strength for each rezzed piece of <strong>NEXT</strong> ice.\n[subroutine] End the run.", "title": "NEXT Bronze", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_next_silver_29010(Ice):
    '''
    Cost: 3
    Text: NEXT Silver gains "Subroutine End the run." for each rezzed piece of NEXT ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29010", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "The networking capabilities of the NEXT suite of ice are unparalleled.", "illustrator": "Ed Mattinian", "keywords": "Barrier - NEXT", "pack_code": "sm", "position": 10, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "NEXT Silver gains \"Subroutine End the run.\" for each rezzed piece of NEXT ice.", "stripped_title": "NEXT Silver", "text": "NEXT Silver gains \"[subroutine] End the run.\" for each rezzed piece of <strong>NEXT</strong> ice.", "title": "NEXT Silver", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_excalibur_29017(Ice):
    '''
    Cost: 2
    Text: Subroutine The Runner cannot make another run this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29017", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "There drew he forth the brand Excalibur,\nAnd o'er him, drawing it, the winter moon,\nBrightening the skirts of a long cloud, ran forth\nAnd sparkled keen with frost against the hilt:\nFor all the haft twinkled with diamond sparks,\nMyriads of topaz-lights, and jacinth work\nOf subtlest jewellery. -Lord Tennyson", "illustrator": "Andreas Zafiratos", "keywords": "Mythic - Grail", "pack_code": "sm", "position": 17, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine The Runner cannot make another run this turn.", "stripped_title": "Excalibur", "text": "[subroutine] The Runner cannot make another run this turn.", "title": "Excalibur", "type_code": "ice", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ansel_10_30038(Ice):
    '''
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed Runner card. Subroutine You may install 1 card from HQ or Archives. Subroutine The Runner cannot steal or trash Corp cards for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30038", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "<strong>Designed by 2018 European Champion Patrick Gower</strong>", "illustrator": "Galen Dara", "keywords": "Sentry - Bioroid - Destroyer", "pack_code": "sg", "position": 38, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Trash 1 installed Runner card. Subroutine You may install 1 card from HQ or Archives. Subroutine The Runner cannot steal or trash Corp cards for the remainder of this run.", "stripped_title": "Ansel 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Trash 1 installed Runner card.\n[subroutine] You may install 1 card from HQ or Archives.\n[subroutine] The Runner cannot steal or trash Corp cards for the remainder of this run.", "title": "Ansel 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bran_10_30039(Ice):
    '''
    Cost: 6
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine You may install 1 piece of ice from HQ or Archives directly inward from this ice, ignoring all costs. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30039", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "A giant wakes...", "illustrator": "Galen Dara", "keywords": "Barrier - Bioroid", "pack_code": "sg", "position": 39, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine You may install 1 piece of ice from HQ or Archives directly inward from this ice, ignoring all costs. Subroutine End the run. Subroutine End the run.", "stripped_title": "Bran 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] You may install 1 piece of ice from HQ or Archives directly inward from this ice, ignoring all costs.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Br\u00e2n 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_diviner_30046(Ice):
    '''
    Cost: 2
    Text: Subroutine Do 1 net damage. If you trash a card with a printed play or install cost that is an odd number, end the run. (0 is not odd.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30046", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "It reads your future in a single biometric sweep.", "illustrator": "BalanceSheet", "keywords": "Code Gate - AP", "pack_code": "sg", "position": 46, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Do 1 net damage. If you trash a card with a printed play or install cost that is an odd number, end the run. (0 is not odd.)", "stripped_title": "Diviner", "text": "[subroutine] Do 1 net damage. If you trash a card with a printed play or install cost that is an odd number, end the run. <em>(0 is not odd.)</em>", "title": "Diviner", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_karuna_30047(Ice):
    '''
    Cost: 4
    Text: Subroutine Do 2 net damage. The Runner may jack out. Subroutine Do 2 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30047", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "You did not escape, you were shown mercy.", "illustrator": "BalanceSheet", "keywords": "Sentry - AP", "pack_code": "sg", "position": 47, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Do 2 net damage. The Runner may jack out. Subroutine Do 2 net damage.", "stripped_title": "Karuna", "text": "[subroutine] Do 2 net damage. The Runner may jack out.\n[subroutine] Do 2 net damage.", "title": "Karun\u0101", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_funhouse_30054(Ice):
    '''
    Cost: 5
    Text: When the Runner encounters this ice, end the run unless the Runner takes 1 tag. Subroutine Give the Runner 1 tag unless they pay 4 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30054", "cost": 5, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"I might take a break from VR after this one.\"\n\u2014SeaOfRibaldry, sensie streamer", "illustrator": "Bruno Balixa", "keywords": "Code Gate", "pack_code": "sg", "position": 54, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When the Runner encounters this ice, end the run unless the Runner takes 1 tag. Subroutine Give the Runner 1 tag unless they pay 4 credits.", "stripped_title": "Funhouse", "text": "When the Runner encounters this ice, end the run unless the Runner takes 1 tag.\n[subroutine] Give the Runner 1 tag unless they pay 4[credit].", "title": "Funhouse", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ping_30055(Ice):
    '''
    Cost: 2
    Text: When you rez this ice during a run against this server, give the Runner 1 tag. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30055", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "AvID:??:73.174 time=0.632 ms\nAvID:??:73.174 time=0.201 ms\nAvID:??:73.174 time=0.000 ms <strong>ALERT</strong>", "illustrator": "Bruno Balixa", "keywords": "Barrier", "pack_code": "sg", "position": 55, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "When you rez this ice during a run against this server, give the Runner 1 tag. Subroutine End the run.", "stripped_title": "Ping", "text": "When you rez this ice during a run against this server, give the Runner 1 tag.\n[subroutine] End the run.", "title": "Ping", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ballista_30062(Ice):
    '''
    Cost: 5
    Text: Subroutine Trash 1 installed program or end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30062", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"Puts a hole in your rig <strong>and</strong> your plans.\"\n\u2014Ren\u00e9 \"Loup\" Arcemont", "illustrator": "Owen Sinodov", "keywords": "Sentry - Destroyer", "pack_code": "sg", "position": 62, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine Trash 1 installed program or end the run.", "stripped_title": "Ballista", "text": "[subroutine] Trash 1 installed program or end the run.", "title": "Ballista", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_pharos_30063(Ice):
    '''
    Cost: 7
    Text: You can advance this ice. It gets +5 strength while there are 3 or more hosted advancement counters. Subroutine Give the Runner 1 tag. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30063", "cost": 7, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Owen Sinodov", "keywords": "Barrier", "pack_code": "sg", "position": 63, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "You can advance this ice. It gets +5 strength while there are 3 or more hosted advancement counters. Subroutine Give the Runner 1 tag. Subroutine End the run. Subroutine End the run.", "stripped_title": "Pharos", "text": "You can advance this ice. It gets +5 strength while there are 3 or more hosted advancement counters.\n[subroutine] Give the Runner 1 tag.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Pharos", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_palisade_30072(Ice):
    '''
    Cost: 3
    Text: While this ice is protecting a remote server, it gets +2 strength. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30072", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Keep the neighbors honest.", "illustrator": "Scott Uminga", "keywords": "Barrier", "pack_code": "sg", "position": 72, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "While this ice is protecting a remote server, it gets +2 strength. Subroutine End the run.", "stripped_title": "Palisade", "text": "While this ice is protecting a remote server, it gets +2 strength.\n[subroutine] End the run.", "title": "Palisade", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tithe_30073(Ice):
    '''
    Cost: 1
    Text: Subroutine Do 1 net damage. Subroutine Gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30073", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"You'll give till it hurts... then it'll reach for more.\"\n\u2014Red Comyn", "illustrator": "Scott Uminga", "keywords": "Sentry - AP", "pack_code": "sg", "position": 73, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "Subroutine Do 1 net damage. Subroutine Gain 1 credit.", "stripped_title": "Tithe", "text": "[subroutine] Do 1 net damage.\n[subroutine] Gain 1[credit].", "title": "Tithe", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_whitespace_30074(Ice):
    '''
    Cost: 2
    Text: Subroutine The Runner loses 3 credits. Subroutine If the Runner has 6 credits or less, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30074", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "[this space intentionally left blank]", "illustrator": "Scott Uminga", "keywords": "Code Gate", "pack_code": "sg", "position": 74, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine The Runner loses 3 credits. Subroutine If the Runner has 6 credits or less, end the run.", "stripped_title": "Whitespace", "text": "[subroutine] The Runner loses 3[credit].\n[subroutine] If the Runner has 6[credit] or less, end the run.", "title": "Whitespace", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_eli_10_31043(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31043", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Hello again! Back for another game?", "illustrator": "Krembler", "keywords": "Barrier - Bioroid", "pack_code": "su21", "position": 43, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine End the run. Subroutine End the run.", "stripped_title": "Eli 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] End the run.\n[subroutine] End the run.", "title": "Eli 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_magnet_31044(Ice):
    '''
    Cost: 3
    Text: When you rez this ice, choose 1 installed program hosted on a piece of ice. Move that program onto this ice. Each hosted program loses all abilities. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31044", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "A triumph of bioroid-driven iterative design. A pity no one understands how it works...", "illustrator": "Zoe Cohen", "keywords": "Code Gate", "pack_code": "su21", "position": 44, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When you rez this ice, choose 1 installed program hosted on a piece of ice. Move that program onto this ice. Each hosted program loses all abilities. Subroutine End the run.", "stripped_title": "Magnet", "text": "When you rez this ice, choose 1 installed program hosted on a piece of ice. Move that program onto this ice.\nEach hosted program loses all abilities.\n[subroutine] End the run.", "title": "Magnet", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ravana_10_31045(Ice):
    '''
    Cost: 3
    Text: Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Resolve 1 subroutine on another rezzed bioroid ice. Subroutine Resolve 1 subroutine on another rezzed bioroid ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31045", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "I roar with a thousand voices, wield a thousand weapons, remember a thousand lives.", "illustrator": "Krembler", "keywords": "Code Gate - Bioroid", "pack_code": "su21", "position": 45, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Resolve 1 subroutine on another rezzed bioroid ice. Subroutine Resolve 1 subroutine on another rezzed bioroid ice.", "stripped_title": "Ravana 1.0", "text": "<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Resolve 1 subroutine on another rezzed <strong>bioroid</strong> ice.\n[subroutine] Resolve 1 subroutine on another rezzed <strong>bioroid</strong> ice.", "title": "Ravana 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_rototurret_31046(Ice):
    '''
    Cost: 4
    Text: Subroutine Trash 1 installed program. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31046", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Click!", "illustrator": "Zoe Cohen", "keywords": "Sentry - Destroyer", "pack_code": "su21", "position": 46, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Subroutine Trash 1 installed program. Subroutine End the run.", "stripped_title": "Rototurret", "text": "[subroutine] Trash 1 installed program.\n[subroutine] End the run.", "title": "Rototurret", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_lotus_field_31055(Ice):
    '''
    Cost: 5
    Text: The strength of this ice cannot be lowered. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31055", "cost": 5, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "As the white light blazed around her, she became still. It was too beautiful. Too perfect.", "illustrator": "Krembler", "keywords": "Code Gate", "pack_code": "su21", "position": 55, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "The strength of this ice cannot be lowered. Subroutine End the run.", "stripped_title": "Lotus Field", "text": "The strength of this ice cannot be lowered.\n[subroutine] End the run.", "title": "Lotus Field", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_swordsman_31056(Ice):
    '''
    Cost: 3
    Text: The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31056", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "The pain of its first cutting art is a test. Bleed human-red and the second attack is stilled.", "illustrator": "Krembler", "keywords": "Sentry - AP - Destroyer", "pack_code": "su21", "position": 56, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "The Runner cannot break subroutines on this ice using AI programs. Subroutine Trash 1 installed AI program. Subroutine Do 1 net damage.", "stripped_title": "Swordsman", "text": "The Runner cannot break subroutines on this ice using <strong>AI</strong> programs.\n[subroutine] Trash 1 installed <strong>AI</strong> program.\n[subroutine] Do 1 net damage.", "title": "Swordsman", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_popup_window_31065(Ice):
    '''
    Cost: 0
    Text: When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31065", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "A moment of your time? A moment of your time? A moment of your\u2014", "illustrator": "Alexis Spicer", "keywords": "Code Gate - Advertisement", "pack_code": "su21", "position": 65, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "When the Runner encounters this ice, gain 1 credit. Subroutine End the run unless the Runner pays 1 credit.", "stripped_title": "Pop-up Window", "text": "When the Runner encounters this ice, gain 1[credit].\n[subroutine] End the run unless the Runner pays 1[credit].", "title": "Pop-up Window", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_tollbooth_31066(Ice):
    '''
    Cost: 8
    Text: When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31066", "cost": 8, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "The original Net pathways were free and open. An unacceptable state of affairs.", "illustrator": "N. Hopkins", "keywords": "Code Gate", "pack_code": "su21", "position": 66, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When the Runner encounters this ice, they must pay 3 credits, if able. If they do not, end the run. Subroutine End the run.", "stripped_title": "Tollbooth", "text": "When the Runner encounters this ice, they must pay 3[credit], if able. If they do not, end the run.\n[subroutine] End the run.", "title": "Tollbooth", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wraparound_31067(Ice):
    '''
    Cost: 2
    Text: While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31067", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Space bent back. Folds on folds.\nEndlessly wide. Paper deep.", "illustrator": "Kevin Tame", "keywords": "Barrier", "pack_code": "su21", "position": 67, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "While there are no installed fracter programs, this ice gets +7 strength. Subroutine End the run.", "stripped_title": "Wraparound", "text": "While there are no installed <strong>fracter</strong> programs, this ice gets +7 strength.\n[subroutine] End the run.", "title": "Wraparound", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_archer_31075(Ice):
    '''
    Cost: 4
    Text: As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31075", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Target Acquired.", "illustrator": "NtscapeNavigator", "keywords": "Sentry - Destroyer", "pack_code": "su21", "position": 75, "quantity": 3, "side_code": "corp", "strength": 6, "stripped_text": "As an additional cost to rez this ice, forfeit 1 agenda. Subroutine Gain 2 credits. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program. Subroutine End the run.", "stripped_title": "Archer", "text": "As an additional cost to rez this ice, forfeit 1 agenda.\n[subroutine] Gain 2[credit].\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.\n[subroutine] End the run.", "title": "Archer", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hortum_31076(Ice):
    '''
    Cost: 4
    Text: You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using AI programs. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 4 credits. Subroutine End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31076", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "N. Hopkins", "keywords": "Code Gate", "pack_code": "su21", "position": 76, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using AI programs. Subroutine Gain 1 credit. If there are 3 or more hosted advancement counters, instead gain 4 credits. Subroutine End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.", "stripped_title": "Hortum", "text": "You can advance this ice. If there are 3 or more hosted advancement counters, the Runner cannot break subroutines on this ice using <strong>AI</strong> programs.\n[subroutine] Gain 1[credit]. If there are 3 or more hosted advancement counters, instead gain 4[credit].\n[subroutine] End the run. If there are 3 or more hosted advancement counters, instead search R&D for up to 2 cards. Add those cards to HQ, then end the run.", "title": "Hortum", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ice_wall_31077(Ice):
    '''
    Cost: 1
    Text: You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31077", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Each time I came back, it was bigger. And colder.", "illustrator": "Zoe Cohen", "keywords": "Barrier", "pack_code": "su21", "position": 77, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "You can advance this ice. It gets +1 strength for each hosted advancement counter. Subroutine End the run.", "stripped_title": "Ice Wall", "text": "You can advance this ice. It gets +1 strength for each hosted advancement counter.\n[subroutine] End the run.", "title": "Ice Wall", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_enigma_31081(Ice):
    '''
    Cost: 3
    Text: Subroutine The Runner loses click. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31081", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "No runner sees the same thing. Some say it's a beast, others a man. But they all agree that it smells blue, and tastes like eternity.", "illustrator": "Benjamin Giletti", "keywords": "Code Gate", "pack_code": "su21", "position": 81, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "Subroutine The Runner loses click. Subroutine End the run.", "stripped_title": "Enigma", "text": "[subroutine] The Runner loses [click].\n[subroutine] End the run.", "title": "Enigma", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hakarl_10_32004(Ice):
    '''
    Cost: 5
    Text: When you rez this ice during a run against this server, you may derez another installed card. If you do, the Runner cannot use paid abilities printed on bioroid ice for the remainder of this turn. Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "32004", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Jakuza", "keywords": "Barrier - Bioroid - AP", "pack_code": "msbp", "position": 4, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When you rez this ice during a run against this server, you may derez another installed card. If you do, the Runner cannot use paid abilities printed on bioroid ice for the remainder of this turn. Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.", "stripped_title": "Hakarl 1.0", "text": "When you rez this ice during a run against this server, you may derez another installed card. If you do, the Runner cannot use paid abilities printed on <strong>bioroid</strong> ice for the remainder of this turn.\n<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] End the run.", "title": "H\u00e1karl 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_anemone_32005(Ice):
    '''
    Cost: 3
    Text: When you rez this ice during a run against this server, you may trash 1 card from HQ to do 2 net damage. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "32005", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Ethereal beauty brings sweet death with only a brief touch.", "illustrator": "Jack Reeves", "keywords": "Sentry - AP", "pack_code": "msbp", "position": 5, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "When you rez this ice during a run against this server, you may trash 1 card from HQ to do 2 net damage. Subroutine Do 1 net damage.", "stripped_title": "Anemone", "text": "When you rez this ice during a run against this server, you may trash 1 card from HQ to do 2 net damage.\n[subroutine] Do 1 net damage.", "title": "Anemone", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_echo_33035(Ice):
    '''
    Cost: 2
    Text: Whenever you rez a piece of harmonic ice, place 1 power counter on this ice. This ice gains "Subroutine End the run." for each hosted power counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33035", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "End the run. End the run. End the run. End the run.", "illustrator": "Jakuza", "keywords": "Barrier - Harmonic", "pack_code": "ms", "position": 35, "quantity": 3, "side_code": "corp", "strength": 0, "stripped_text": "Whenever you rez a piece of harmonic ice, place 1 power counter on this ice. This ice gains \"Subroutine End the run.\" for each hosted power counter.", "stripped_title": "Echo", "text": "Whenever you rez a piece of <strong>harmonic</strong> ice, place 1 power counter on this ice.\nThis ice gains \"[subroutine] End the run.\" for each hosted power counter.", "title": "Echo", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hakarl_10_33036(Ice):
    '''
    Cost: 5
    Text: When you rez this ice during a run against this server, you may derez another installed card. If you do, the Runner cannot use paid abilities printed on bioroid ice for the remainder of this turn. Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33036", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Jakuza", "keywords": "Barrier - Bioroid - AP", "pack_code": "ms", "position": 36, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "When you rez this ice during a run against this server, you may derez another installed card. If you do, the Runner cannot use paid abilities printed on bioroid ice for the remainder of this turn. Lose click: Break 1 subroutine on this ice. Only the Runner can use this ability. Subroutine Do 1 core damage. Subroutine End the run.", "stripped_title": "Hakarl 1.0", "text": "When you rez this ice during a run against this server, you may derez another installed card. If you do, the Runner cannot use paid abilities printed on <strong>bioroid</strong> ice for the remainder of this turn.\n<strong>Lose [click]:</strong> Break 1 subroutine on this ice. Only the Runner can use this ability.\n[subroutine] Do 1 core damage.\n[subroutine] End the run.", "title": "H\u00e1karl 1.0", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_wave_33037(Ice):
    '''
    Cost: 2
    Text: When you rez this ice during a run against this server, you may search R&D for a piece of ice and reveal it. (Shuffle R&D after searching it.) Add that ice to HQ. Subroutine Gain 1 credit for each rezzed piece of harmonic ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33037", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "With networks, growth is exponential.", "illustrator": "Jakuza", "keywords": "Code Gate - Harmonic", "pack_code": "ms", "position": 37, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When you rez this ice during a run against this server, you may search R&D for a piece of ice and reveal it. (Shuffle R&D after searching it.) Add that ice to HQ. Subroutine Gain 1 credit for each rezzed piece of harmonic ice.", "stripped_title": "Wave", "text": "When you rez this ice during a run against this server, you may search R&D for a piece of ice and reveal it. <em>(Shuffle R&D after searching it.)</em> Add that ice to HQ.\n[subroutine] Gain 1[credit] for each rezzed piece of <strong>harmonic</strong> ice.", "title": "Wave", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_anemone_33043(Ice):
    '''
    Cost: 3
    Text: When you rez this ice during a run against this server, you may trash 1 card from HQ to do 2 net damage. Subroutine Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33043", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Ethereal beauty laced with the most elegant venom.", "illustrator": "Jack Reeves", "keywords": "Sentry - AP", "pack_code": "ms", "position": 43, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "When you rez this ice during a run against this server, you may trash 1 card from HQ to do 2 net damage. Subroutine Do 1 net damage.", "stripped_title": "Anemone", "text": "When you rez this ice during a run against this server, you may trash 1 card from HQ to do 2 net damage.\n[subroutine] Do 1 net damage.", "title": "Anemone", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bathynomus_33044(Ice):
    '''
    Cost: 3
    Text: While this ice is protecting Archives, it gets +3 strength. Subroutine Do 3 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33044", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Digital refuse is their food, and you should never come between an animal and its food.", "illustrator": "Jack Reeves", "keywords": "Sentry - AP", "pack_code": "ms", "position": 44, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "While this ice is protecting Archives, it gets +3 strength. Subroutine Do 3 net damage.", "stripped_title": "Bathynomus", "text": "While this ice is protecting Archives, it gets +3 strength.\n[subroutine] Do 3 net damage.", "title": "Bathynomus", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_ivik_33045(Ice):
    '''
    Cost: 7
    Text: The rez cost of this ice is lowered by 1 credit for each rezzed piece of code gate ice. Subroutine Do 2 net damage. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33045", "cost": 7, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Keep off the grass.", "illustrator": "Jack Reeves", "keywords": "Barrier - AP", "pack_code": "ms", "position": 45, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "The rez cost of this ice is lowered by 1 credit for each rezzed piece of code gate ice. Subroutine Do 2 net damage. Subroutine End the run.", "stripped_title": "Ivik", "text": "The rez cost of this ice is lowered by 1[credit] for each rezzed piece of <strong>code gate</strong> ice.\n[subroutine] Do 2 net damage.\n[subroutine] End the run.", "title": "Ivik", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_mestnichestvo_33053(Ice):
    '''
    Cost: 5
    Text: You can advance this ice. When the Runner encounters this ice, you may remove 1 hosted advancement counter. If you do, the Runner loses 3 credits. Subroutine The Runner loses 3 credits. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33053", "cost": 5, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Names of old carry little weight today, their legacies broken and swept away. Now, we are the rulers of truth.", "illustrator": "BalanceSheet", "keywords": "Code Gate", "pack_code": "ms", "position": 53, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "You can advance this ice. When the Runner encounters this ice, you may remove 1 hosted advancement counter. If you do, the Runner loses 3 credits. Subroutine The Runner loses 3 credits. Subroutine End the run.", "stripped_title": "Mestnichestvo", "text": "You can advance this ice.\nWhen the Runner encounters this ice, you may remove 1 hosted advancement counter. If you do, the Runner loses 3[credit].\n[subroutine] The Runner loses 3[credit].\n[subroutine] End the run.", "title": "Mestnichestvo", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_vasilisa_33054(Ice):
    '''
    Cost: 2
    Text: When the Runner encounters this ice, you may pay 1 credit. If you do, place 1 advancement counter on an installed card you can advance. Subroutine Give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33054", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "No task the witch set would ever be too great, for Vasilisa had her mother's blessing.", "illustrator": "BalanceSheet", "keywords": "Sentry - Observer", "pack_code": "ms", "position": 54, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "When the Runner encounters this ice, you may pay 1 credit. If you do, place 1 advancement counter on an installed card you can advance. Subroutine Give the Runner 1 tag.", "stripped_title": "Vasilisa", "text": "When the Runner encounters this ice, you may pay 1[credit]. If you do, place 1 advancement counter on an installed card you can advance.\n[subroutine] Give the Runner 1 tag.", "title": "Vasilisa", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_envelopment_33060(Ice):
    '''
    Cost: 5
    Text: When you rez this ice, place 4 power counters on it. When your turn begins, remove 1 hosted power counter. This ice gains "Subroutine End the run." before its printed subroutine for each hosted power counter. Subroutine Trash this ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33060", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Scott Uminga", "keywords": "Barrier", "pack_code": "ms", "position": 60, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "When you rez this ice, place 4 power counters on it. When your turn begins, remove 1 hosted power counter. This ice gains \"Subroutine End the run.\" before its printed subroutine for each hosted power counter. Subroutine Trash this ice.", "stripped_title": "Envelopment", "text": "When you rez this ice, place 4 power counters on it.\nWhen your turn begins, remove 1 hosted power counter.\nThis ice gains \"[subroutine] End the run.\" before its printed subroutine for each hosted power counter.\n[subroutine] Trash this ice.", "title": "Envelopment", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_maskirovka_33061(Ice):
    '''
    Cost: 3
    Text: Subroutine Gain 2 credits. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33061", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "Confound the runner so that they cannot see our true intent.", "illustrator": "Scott Uminga", "keywords": "Barrier", "pack_code": "ms", "position": 61, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "Subroutine Gain 2 credits. Subroutine End the run.", "stripped_title": "Maskirovka", "text": "[subroutine] Gain 2[credit].\n[subroutine] End the run.", "title": "Maskirovka", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_stavka_33062(Ice):
    '''
    Cost: 4
    Text: When you rez this ice, you may trash 1 of your other installed cards. If you do, this ice gets +5 strength for the remainder of the run. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33062", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Centuries of military tactics compressed into a single entity.", "illustrator": "Scott Uminga", "keywords": "Sentry - Destroyer", "pack_code": "ms", "position": 62, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "When you rez this ice, you may trash 1 of your other installed cards. If you do, this ice gets +5 strength for the remainder of the run. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program.", "stripped_title": "Stavka", "text": "When you rez this ice, you may trash 1 of your other installed cards. If you do, this ice gets +5 strength for the remainder of the run.\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.", "title": "Stavka", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_bloop_33098(Ice):
    '''
    Cost: 3
    Text: As an additional cost to rez this ice, derez another piece of harmonic ice. Subroutine Do 1 core damage. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33098", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "As one, every monitoring device on the ship reverberated, emitting a noise so primordial, so titanic, it shook Padma to her core.\nDaeg hissed.", "illustrator": "Jakuza", "keywords": "Sentry - AP - Destroyer - Harmonic", "pack_code": "ph", "position": 98, "quantity": 3, "side_code": "corp", "strength": 5, "stripped_text": "As an additional cost to rez this ice, derez another piece of harmonic ice. Subroutine Do 1 core damage. Subroutine Trash 1 installed program. Subroutine Trash 1 installed program.", "stripped_title": "Bloop", "text": "As an additional cost to rez this ice, derez another piece of <strong>harmonic</strong> ice.\n[subroutine] Do 1 core damage.\n[subroutine] Trash 1 installed program.\n[subroutine] Trash 1 installed program.", "title": "Bloop", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_pulse_33099(Ice):
    '''
    Cost: 3
    Text: When you rez this ice during a run against this server, the Runner loses click. Subroutine The Runner loses 1 credit for each rezzed piece of harmonic ice. Subroutine End the run unless the Runner spends click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33099", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "The sound welled up from the deep: throbbing, thumping, growing with every passing beat of their hearts.", "illustrator": "Jakuza", "keywords": "Code Gate - Harmonic", "pack_code": "ph", "position": 99, "quantity": 3, "side_code": "corp", "strength": 1, "stripped_text": "When you rez this ice during a run against this server, the Runner loses click. Subroutine The Runner loses 1 credit for each rezzed piece of harmonic ice. Subroutine End the run unless the Runner spends click.", "stripped_title": "Pulse", "text": "When you rez this ice during a run against this server, the Runner loses [click].\n[subroutine] The Runner loses 1[credit] for each rezzed piece of <strong>harmonic</strong> ice.\n[subroutine] End the run unless the Runner spends [click].", "title": "Pulse", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_hafrun_33108(Ice):
    '''
    Cost: 2
    Text: When you rez this ice during a run against this server, you may trash 1 card from HQ. If you do, choose 1 installed Runner card. That cards abilities cannot break subroutines for the remainder of that run. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33108", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Hafr\u00fan has seen generations of the Net. Now there are whispers that something from the deep is disquieting it.", "illustrator": "Jack Reeves", "keywords": "Barrier - Code Gate", "pack_code": "ph", "position": 108, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When you rez this ice during a run against this server, you may trash 1 card from HQ. If you do, choose 1 installed Runner card. That cards abilities cannot break subroutines for the remainder of that run. Subroutine End the run.", "stripped_title": "Hafrun", "text": "When you rez this ice during a run against this server, you may trash 1 card from HQ. If you do, choose 1 installed Runner card. That card\u02bcs abilities cannot break subroutines for the remainder of that run.\n[subroutine] End the run.", "title": "Hafr\u00fan", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_vampyronassa_33109(Ice):
    '''
    Cost: 7
    Text: Subroutine The Runner loses 2 credits. Subroutine Gain 2 credits. Subroutine Do 2 net damage. Subroutine You may draw 1 or 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33109", "cost": 7, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "\"Matt, there\u02bcs something big heading your way. Matt, are you hearing me? Matt? Oh no.\"\n\u2014Moth", "illustrator": "Ed Mattinian", "keywords": "Code Gate - AP", "pack_code": "ph", "position": 109, "quantity": 3, "side_code": "corp", "strength": 4, "stripped_text": "Subroutine The Runner loses 2 credits. Subroutine Gain 2 credits. Subroutine Do 2 net damage. Subroutine You may draw 1 or 2 cards.", "stripped_title": "Vampyronassa", "text": "[subroutine] The Runner loses 2[credit].\n[subroutine] Gain 2[credit].\n[subroutine] Do 2 net damage.\n[subroutine] You may draw 1 or 2 cards.", "title": "Vampyronassa", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_klevetnik_33116(Ice):
    '''
    Cost: 3
    Text: When you rez this ice during a run against this server, you may have the Runner gain 2 credits. If you do, choose 1 installed resource. That resource loses all abilities until your next turn ends. Subroutine End the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33116", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "SCANNING... ASSEMBLING INSULT!", "illustrator": "Bruno Balixa", "keywords": "Barrier", "pack_code": "ph", "position": 116, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When you rez this ice during a run against this server, you may have the Runner gain 2 credits. If you do, choose 1 installed resource. That resource loses all abilities until your next turn ends. Subroutine End the run.", "stripped_title": "Klevetnik", "text": "When you rez this ice during a run against this server, you may have the Runner gain 2[credit]. If you do, choose 1 installed resource. That resource loses all abilities until your next turn ends.\n[subroutine] End the run.", "title": "Klevetnik", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_unsmiling_tsarevna_33117(Ice):
    '''
    Cost: 4
    Text: When you rez this ice during a run against this server, you may have the Runner gain 2 credits. If you do, during each encounter with this ice for the remainder of that run, the Runner cannot break more than 1 of its printed subroutines. Subroutine Give the Runner 1 tag. Subroutine Do 2 net damage. Subroutine You may draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33117", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "BalanceSheet", "keywords": "Sentry - AP", "pack_code": "ph", "position": 117, "quantity": 3, "side_code": "corp", "strength": 2, "stripped_text": "When you rez this ice during a run against this server, you may have the Runner gain 2 credits. If you do, during each encounter with this ice for the remainder of that run, the Runner cannot break more than 1 of its printed subroutines. Subroutine Give the Runner 1 tag. Subroutine Do 2 net damage. Subroutine You may draw 2 cards.", "stripped_title": "Unsmiling Tsarevna", "text": "When you rez this ice during a run against this server, you may have the Runner gain 2[credit]. If you do, during each encounter with this ice for the remainder of that run, the Runner cannot break more than 1 of its printed subroutines.\n[subroutine] Give the Runner 1 tag.\n[subroutine] Do 2 net damage.\n[subroutine] You may draw 2 cards.", "title": "Unsmiling Tsarevna", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class ice_anvil_33124(Ice):
    '''
    Cost: 4
    Text: When the Runner encounters this ice, you may trash 1 of your other installed cards. If you do, the Runner cannot break this ice's printed subroutines for the remainder of this encounter. Subroutine Gain 1 credit. The Runner loses 1 credit. Subroutine The Runner trashes 1 of their installed cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33124", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Waiting for the next blow to land.", "illustrator": "Scott Uminga", "keywords": "Code Gate", "pack_code": "ph", "position": 124, "quantity": 3, "side_code": "corp", "strength": 3, "stripped_text": "When the Runner encounters this ice, you may trash 1 of your other installed cards. If you do, the Runner cannot break this ice's printed subroutines for the remainder of this encounter. Subroutine Gain 1 credit. The Runner loses 1 credit. Subroutine The Runner trashes 1 of their installed cards.", "stripped_title": "Anvil", "text": "When the Runner encounters this ice, you may trash 1 of your other installed cards. If you do, the Runner cannot break this ice\u02bcs printed subroutines for the remainder of this encounter.\n[subroutine] Gain 1[credit]. The Runner loses 1[credit].\n[subroutine] The Runner trashes 1 of their installed cards.", "title": "Anvil", "type_code": "ice", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"
