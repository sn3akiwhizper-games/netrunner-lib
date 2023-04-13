
'''
card classes of type program
'''
from netrunner_lib.cards._base_card_classes import Program
from netrunner_lib.game_events import *

class program_corroder_01007(Program):
    '''
    Cost: 2
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01007", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"If at first you don't succeed, boost its strength and try again.\" -g00ru", "illustrator": "Mike Nesbitt", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "core", "position": 7, "quantity": 2, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength.", "stripped_title": "Corroder", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Corroder", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_datasucker_01008(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run on a central server, place 1 virus counter on Datasucker. Hosted virus counter: Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01008", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Chelsea Conlin", "keywords": "Virus", "memory_cost": 1, "pack_code": "core", "position": 8, "quantity": 2, "side_code": "runner", "stripped_text": "Whenever you make a successful run on a central server, place 1 virus counter on Datasucker. Hosted virus counter: Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.", "stripped_title": "Datasucker", "text": "Whenever you make a successful run on a central server, place 1 virus counter on Datasucker.\n<strong>Hosted virus counter:</strong> Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.", "title": "Datasucker", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_djinn_01009(Program):
    '''
    Cost: 2
    Text: Djinn can host up to 3 mu of non-icebreaker programs. The memory costs of hosted programs do not count against your memory limit. click, 1 credit: Search your stack for a virus program, reveal it, and add it to your grip. Shuffle your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01009", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Mark Anthony Taduran", "keywords": "Daemon", "memory_cost": 1, "pack_code": "core", "position": 9, "quantity": 2, "side_code": "runner", "stripped_text": "Djinn can host up to 3 mu of non-icebreaker programs. The memory costs of hosted programs do not count against your memory limit. click, 1 credit: Search your stack for a virus program, reveal it, and add it to your grip. Shuffle your stack.", "stripped_title": "Djinn", "text": "Djinn can host up to 3[mu] of non-<strong>icebreaker</strong> programs.\nThe memory costs of hosted programs do not count against your memory limit.\n[click], 1[credit]: Search your stack for a <strong>virus</strong> program, reveal it, and add it to your grip. Shuffle your stack.", "title": "Djinn", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_medium_01010(Program):
    '''
    Cost: 3
    Text: Whenever you make a successful run on R&D, place 1 virus counter on this program. Whenever you breach R&D, choose a number less than the number of hosted virus counters. Access that many additional cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01010", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "It looked like random packet loss. It wasn't.", "illustrator": "Adam S. Doyle", "keywords": "Virus", "memory_cost": 1, "pack_code": "core", "position": 10, "quantity": 2, "side_code": "runner", "stripped_text": "Whenever you make a successful run on R&D, place 1 virus counter on this program. Whenever you breach R&D, choose a number less than the number of hosted virus counters. Access that many additional cards.", "stripped_title": "Medium", "text": "Whenever you make a successful run on R&D, place 1 virus counter on this program.\nWhenever you breach R&D, choose a number less than the number of hosted virus counters. Access that many additional cards.", "title": "Medium", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_mimic_01011(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01011", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "November 5th: the day when all would see the corrupt machinations of the corporate oligarchy.", "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "core", "position": 11, "quantity": 2, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine.", "stripped_title": "Mimic", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.", "title": "Mimic", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_parasite_01012(Program):
    '''
    Cost: 2
    Text: Install only on a rezzed piece of ice. When your turn begins, place 1 virus counter on this program. Host ice gets -1 strength for each hosted virus counter. When the strength of host ice is 0 or less, trash it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01012", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Bruno Balixa", "keywords": "Virus - Trojan", "memory_cost": 1, "pack_code": "core", "position": 12, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a rezzed piece of ice. When your turn begins, place 1 virus counter on this program. Host ice gets -1 strength for each hosted virus counter. When the strength of host ice is 0 or less, trash it.", "stripped_title": "Parasite", "text": "Install only on a rezzed piece of ice.\nWhen your turn begins, place 1 virus counter on this program.\nHost ice gets -1 strength for each hosted virus counter.\nWhen the strength of host ice is 0 or less, trash it.", "title": "Parasite", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_wyrm_01013(Program):
    '''
    Cost: 1
    Text: Interface -> 3 credits: Break 1 subroutine on a piece of ice with 0 or less strength. Interface -> 1 credit: The ice you are encountering gets -1 strength for the remainder of this encounter. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01013", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Fire and ichor\u2026", "illustrator": "Sandara Tang", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "core", "position": 13, "quantity": 2, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 3 credits: Break 1 subroutine on a piece of ice with 0 or less strength. Interface -> 1 credit: The ice you are encountering gets -1 strength for the remainder of this encounter. 1 credit: +1 strength.", "stripped_title": "Wyrm", "text": "Interface \u2192 <strong>3[credit]:</strong> Break 1 subroutine on a piece of ice with 0 or less strength.\nInterface \u2192 <strong>1[credit]:</strong> The ice you are encountering gets -1 strength for the remainder of this encounter.\n<strong>1[credit]:</strong> +1 strength.", "title": "Wyrm", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_yog0_01014(Program):
    '''
    Cost: 5
    Text: Interface -> 0 credits: Break 1 code gate subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01014", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "The Yog.0 database is a crowdsourced compilation of sniffed, spoofed, and logged passkeys. If the key to the gate is in the database, you're in. If it's not, change the gate!", "illustrator": "Kate Niemczyk", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "core", "position": 14, "quantity": 2, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 0 credits: Break 1 code gate subroutine.", "stripped_title": "Yog.0", "text": "Interface \u2192 <strong>0[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.", "title": "Yog.0", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_aurora_01025(Program):
    '''
    Cost: 3
    Text: Interface -> 2 credits: Break 1 barrier subroutine. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01025", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "core", "position": 25, "quantity": 2, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break 1 barrier subroutine. 2 credits: +3 strength.", "stripped_title": "Aurora", "text": "Interface \u2192 <strong>2[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>2[credit]:</strong> +3 strength.", "title": "Aurora", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_femme_fatale_01026(Program):
    '''
    Cost: 9
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01026", "cost": 9, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Kate Niemczyk", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "core", "position": 26, "quantity": 2, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.", "stripped_title": "Femme Fatale", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +1 strength.\nWhen you install this program, choose 1 installed piece of ice.\nWhenever you encounter the chosen ice, you may pay 1[credit] for each subroutine it has. If you do, bypass that ice.", "title": "Femme Fatale", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_ninja_01027(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +5 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01027", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "You feel Ninja before you see Ninja, if you see Ninja at all.", "illustrator": "Andrew Mar", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "core", "position": 27, "quantity": 2, "side_code": "runner", "strength": 0, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +5 strength.", "stripped_title": "Ninja", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>3[credit]:</strong> +5 strength.", "title": "Ninja", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sneakdoor_beta_01028(Program):
    '''
    Cost: 4
    Text: click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01028", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"The code isn't important. It's where the code takes you that is important.\" -g00ru", "illustrator": "Andrew Mar", "memory_cost": 2, "pack_code": "core", "position": 28, "quantity": 2, "side_code": "runner", "stripped_text": "click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.", "stripped_title": "Sneakdoor Beta", "text": "[click]<strong>:</strong> Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.", "title": "Sneakdoor Beta", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_battering_ram_01042(Program):
    '''
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 1 credit: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01042", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"It's called 'brute-forcing' and it's just as effective today as it was a hundred years ago.\" -Kate \"Mac\" McCaffrey", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Fracter", "memory_cost": 2, "pack_code": "core", "position": 42, "quantity": 2, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 2 credits: Break up to 2 barrier subroutines. 1 credit: +1 strength for the remainder of this run.", "stripped_title": "Battering Ram", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength for the remainder of this run.", "title": "Battering Ram", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gordian_blade_01043(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01043", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "It can slice through the thickest knots of data.", "illustrator": "Mike Nesbitt", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "core", "position": 43, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.", "stripped_title": "Gordian Blade", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength for the remainder of this run.", "title": "Gordian Blade", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_magnum_opus_01044(Program):
    '''
    Cost: 5
    Text: click: Gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01044", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "The Great Work was completed on a rainy Thursday afternoon. There were no seismic shifts, no solar flares, no sign from the earth or heavens that the world had changed. But upstalk in Heinlein, on a single Cybsoft manufactured datacore, the flickering data quantums of an account began to fill with creds. Real, honest-to-goodness UN certified creds.", "illustrator": "Outland Entertainment LLC", "memory_cost": 2, "pack_code": "core", "position": 44, "quantity": 2, "side_code": "runner", "stripped_text": "click: Gain 2 credits.", "stripped_title": "Magnum Opus", "text": "[click]: Gain 2[credit].", "title": "Magnum Opus", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_net_shield_01045(Program):
    '''
    Cost: 2
    Text: Interrupt -> The first time each turn you would suffer net damage, you may pay 1 credit to prevent 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01045", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Sucks energy like a martian terra-bot, but it keeps you focused", "illustrator": "Andrew Mar", "memory_cost": 1, "pack_code": "core", "position": 45, "quantity": 2, "side_code": "runner", "stripped_text": "Interrupt -> The first time each turn you would suffer net damage, you may pay 1 credit to prevent 1 net damage.", "stripped_title": "Net Shield", "text": "[interrupt] \u2192 The first time each turn you would suffer net damage, you may pay 1[credit] to prevent 1 net damage.", "title": "Net Shield", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_pipeline_01046(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01046", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "illustrator": "Matt Zeilinger", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "core", "position": 46, "quantity": 2, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength for the remainder of this run.", "stripped_title": "Pipeline", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +1 strength for the remainder of this run.", "title": "Pipeline", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_crypsis_01051(Program):
    '''
    Cost: 5
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. click: Place 1 virus counter on this program. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01051", "cost": 5, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Mauricio Herrera", "keywords": "Icebreaker - AI - Virus", "memory_cost": 1, "pack_code": "core", "position": 51, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. click: Place 1 virus counter on this program. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.", "stripped_title": "Crypsis", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine.\n<strong>1[credit]:</strong> +1 strength.\n<strong>[click]:</strong> Place 1 virus counter on this program.\nWhenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.", "title": "Crypsis", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_imp_02003(Program):
    '''
    Cost: 2
    Text: When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02003", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Something wicked this way comes.", "illustrator": "Wen Xiaodong", "keywords": "Virus", "memory_cost": 1, "pack_code": "wla", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.", "stripped_title": "Imp", "text": "When you install this program, place 2 virus counters on it.\nAccess \u2192 <strong>Hosted virus counter:</strong> Trash the card you are accessing. Use this ability only once per turn.", "title": "Imp", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_morning_star_02004(Program):
    '''
    Cost: 8
    Text: Interface -> 1 credit: Break any number of barrier subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02004", "cost": 8, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "Weaponizing the heavens, one star at a time.", "illustrator": "Robert Chew", "keywords": "Icebreaker - Fracter", "memory_cost": 2, "pack_code": "wla", "position": 4, "quantity": 3, "side_code": "runner", "strength": 5, "stripped_text": "Interface -> 1 credit: Break any number of barrier subroutines.", "stripped_title": "Morning Star", "text": "Interface \u2192 <strong>1[credit]:</strong> Break any number of <strong>barrier</strong> subroutines.", "title": "Morning Star", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_peacock_02006(Program):
    '''
    Cost: 3
    Text: Interface -> 2 credits: Break 1 code gate subroutine. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02006", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Show-off.", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "wla", "position": 6, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 2 credits: Break 1 code gate subroutine. 2 credits: +3 strength.", "stripped_title": "Peacock", "text": "Interface \u2192 <strong>2[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> +3 strength.", "title": "Peacock", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_zu13_key_master_02007(Program):
    '''
    Cost: 1
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02007", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "He always uses the same key.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Decoder - Cloud", "memory_cost": 1, "pack_code": "wla", "position": 7, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.", "stripped_title": "ZU.13 Key Master", "text": "If you have at least 2[link], the memory cost of this program is 0[mu], even if it is not installed.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "ZU.13 Key Master", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_snowball_02027(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength. Whenever you use this program to break a subroutine, this program gets +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02027", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"If your snowball gets big enough, you can make it into a snowman!\" -Chaos Theory", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "ta", "position": 27, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength. Whenever you use this program to break a subroutine, this program gets +1 strength for the remainder of this run.", "stripped_title": "Snowball", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.\nWhenever you use this program to break a subroutine, this program gets +1 strength for the remainder of this run.", "title": "Snowball", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_nerve_agent_02041(Program):
    '''
    Cost: 3
    Text: Whenever you make a successful run on HQ, place 1 virus counter on this program. Whenever you breach HQ, choose a number less than the number of hosted virus counters. Access that many additional cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02041", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Virus", "memory_cost": 1, "pack_code": "ce", "position": 41, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on HQ, place 1 virus counter on this program. Whenever you breach HQ, choose a number less than the number of hosted virus counters. Access that many additional cards.", "stripped_title": "Nerve Agent", "text": "Whenever you make a successful run on HQ, place 1 virus counter on this program.\nWhenever you breach HQ, choose a number less than the number of hosted virus counters. Access that many additional cards.", "title": "Nerve Agent", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_snitch_02045(Program):
    '''
    Cost: 3
    Text: Once per run, you may expose an unrezzed piece of ice when you approach it. You may then jack out.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02045", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"A snitch is a girl's best friend.\" -Andromeda", "illustrator": "Mashuri", "memory_cost": 1, "pack_code": "ce", "position": 45, "quantity": 3, "side_code": "runner", "stripped_text": "Once per run, you may expose an unrezzed piece of ice when you approach it. You may then jack out.", "stripped_title": "Snitch", "text": "Once per run, you may expose an unrezzed piece of ice when you approach it. You may then jack out.", "title": "Snitch", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_disrupter_02061(Program):
    '''
    Cost: 1
    Text: Interrupt -> trash: Reduce the base trace strength of a trace to 0.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02061", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"Saved my bacon more than once, but gives a wicked sense of d\u00e9j\u00e0 vu.\" -Whizzard", "illustrator": "Adam S. Doyle", "memory_cost": 1, "pack_code": "asis", "position": 61, "quantity": 3, "side_code": "runner", "stripped_text": "Interrupt -> trash: Reduce the base trace strength of a trace to 0.", "stripped_title": "Disrupter", "text": "[interrupt] \u2192 [trash]: Reduce the base trace strength of a trace to 0.", "title": "Disrupter", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_force_of_nature_02062(Program):
    '''
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02062", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "It always strikes twice.", "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "asis", "position": 62, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.", "stripped_title": "Force of Nature", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>code gate</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength.", "title": "Force of Nature", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_crescentus_02065(Program):
    '''
    Cost: 1
    Text: trash: Derez 1 piece of ice you fully broke during this encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02065", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "Cyberspace's strongest glue.", "illustrator": "Adam S. Doyle", "memory_cost": 1, "pack_code": "asis", "position": 65, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Derez 1 piece of ice you fully broke during this encounter.", "stripped_title": "Crescentus", "text": "<strong>[trash]:</strong> Derez 1 piece of ice you fully broke during this encounter.", "title": "Crescentus", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_deus_x_02066(Program):
    '''
    Cost: 3
    Text: Interface -> trash: Break any number of AP subroutines. Interrupt -> trash: Prevent any amount of net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02066", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Didn't see that coming.", "illustrator": "Andrew Mar", "keywords": "Icebreaker", "memory_cost": 1, "pack_code": "asis", "position": 66, "quantity": 3, "side_code": "runner", "strength": 10, "stripped_text": "Interface -> trash: Break any number of AP subroutines. Interrupt -> trash: Prevent any amount of net damage.", "stripped_title": "Deus X", "text": "Interface \u2192 <strong>[trash]:</strong> Break any number of <strong>AP</strong> subroutines.\n[interrupt] \u2192 <strong>[trash]:</strong> Prevent any amount of net damage.", "title": "Deus X", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_pheromones_02086(Program):
    '''
    Cost: 2
    Text: X recurring credits Use these credits during runs on HQ. X is the number of virus counters on Pheromones. Whenever you make a successful run on HQ, place 1 virus counter on Pheromones.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02086", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Virus", "memory_cost": 1, "pack_code": "hs", "position": 86, "quantity": 3, "side_code": "runner", "stripped_text": "X recurring credits Use these credits during runs on HQ. X is the number of virus counters on Pheromones. Whenever you make a successful run on HQ, place 1 virus counter on Pheromones.", "stripped_title": "Pheromones", "text": "X[recurring-credit]\nUse these credits during runs on HQ. X is the number of virus counters on Pheromones.\nWhenever you make a successful run on HQ, place 1 virus counter on Pheromones.", "title": "Pheromones", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_creeper_02089(Program):
    '''
    Cost: 5
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break 1 sentry subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02089", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"The itsy bitsy spider went up the data spout\u2026\"\n-Chaos Theory", "illustrator": "JuanManuel Tumburus", "keywords": "Icebreaker - Killer - Cloud", "memory_cost": 1, "pack_code": "hs", "position": 89, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break 1 sentry subroutine. 1 credit: +1 strength.", "stripped_title": "Creeper", "text": "If you have at least 2[link], the memory cost of this program is 0[mu], even if it is not installed.\nInterface \u2192 <strong>2[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Creeper", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_darwin_02102(Program):
    '''
    Cost: 3
    Text: Interface -> 2 credits: Break 1 subroutine. X is equal to the number of hosted virus counters. When your turn begins, you may pay 1 credit to place 1 virus counter on this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02102", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - AI - Virus", "memory_cost": 1, "pack_code": "fp", "position": 102, "quantity": 3, "side_code": "runner", "strength": null, "stripped_text": "Interface -> 2 credits: Break 1 subroutine. X is equal to the number of hosted virus counters. When your turn begins, you may pay 1 credit to place 1 virus counter on this program.", "stripped_title": "Darwin", "text": "Interface \u2192 2[credit]: Break 1 subroutine.\nX is equal to the number of hosted virus counters.\nWhen your turn begins, you may pay 1[credit] to place 1 virus counter on this program.", "title": "Darwin", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_faerie_02104(Program):
    '''
    Cost: 0
    Text: Interface -> 0 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02104", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Do you believe in faeries?", "illustrator": "Sara K. Diesel", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "fp", "position": 104, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 0 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.", "stripped_title": "Faerie", "text": "Interface \u2192 0[credit]: Break 1 <strong>sentry</strong> subroutine.\n1[credit]: +1 strength.\nWhenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.", "title": "Faerie", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_deep_thought_02108(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run on R&D, place 1 virus counter on Deep Thought. If there are at least 3 virus counters on Deep Thought, it gains "When your turn begins, you may look at the top card of R&D."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02108", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Anna Ignatieva", "keywords": "Virus", "memory_cost": 1, "pack_code": "fp", "position": 108, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on R&D, place 1 virus counter on Deep Thought. If there are at least 3 virus counters on Deep Thought, it gains \"When your turn begins, you may look at the top card of R&D.\"", "stripped_title": "Deep Thought", "text": "Whenever you make a successful run on R&D, place 1 virus counter on Deep Thought.\nIf there are at least 3 virus counters on Deep Thought, it gains \"When your turn begins, you may look at the top card of R&D.\"", "title": "Deep Thought", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_atman_03040(Program):
    '''
    Cost: 3
    Text: When you install this program, you may pay X credits to place X power counters on it. This program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength. Interface -> 1 credit: Break 1 subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03040", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "We are shaped by our thoughts; we become what we think.", "illustrator": "Diana Martinez", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "cac", "position": 40, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "When you install this program, you may pay X credits to place X power counters on it. This program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength. Interface -> 1 credit: Break 1 subroutine.", "stripped_title": "Atman", "text": "When you install this program, you may pay X[credit] to place X power counters on it.\nThis program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 subroutine.", "title": "Atman", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cloak_03041(Program):
    '''
    Cost: 1
    Text: 1 recurring credit Use this credit to pay for using icebreakers.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03041", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"No line that they lay could catch a shadow on the wall\u2026\"", "illustrator": "Adam S. Doyle", "keywords": "Stealth", "memory_cost": 1, "pack_code": "cac", "position": 41, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to pay for using icebreakers.", "stripped_title": "Cloak", "text": "1[recurring-credit]\nUse this credit to pay for using <strong>icebreakers</strong>.", "title": "Cloak", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_dagger_03042(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 1 credit: +5 strength. Use this ability only by spending a credit from a stealth card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03042", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"\u2026and once the shadow rises, the curtain shall fall.\" -revenant", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "cac", "position": 42, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 1 credit: +5 strength. Use this ability only by spending a credit from a stealth card.", "stripped_title": "Dagger", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>1[credit]:</strong> +5 strength. Use this ability only by spending a credit from a <strong>stealth</strong> card.", "title": "Dagger", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_chakana_03043(Program):
    '''
    Cost: 2
    Text: Whenever you make a successful run on R&D, place 1 virus counter on Chakana. If there are at least 3 virus counters on Chakana, the advancement requirement of all agendas is increased by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03043", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Virus", "memory_cost": 1, "pack_code": "cac", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on R&D, place 1 virus counter on Chakana. If there are at least 3 virus counters on Chakana, the advancement requirement of all agendas is increased by 1.", "stripped_title": "Chakana", "text": "Whenever you make a successful run on R&D, place 1 virus counter on Chakana.\nIf there are at least 3 virus counters on Chakana, the advancement requirement of all agendas is increased by 1.", "title": "Chakana", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cybercypher_03044(Program):
    '''
    Cost: 2
    Text: When you install this program, choose a server. Use this program only during runs on the chosen server. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03044", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "cac", "position": 44, "quantity": 3, "side_code": "runner", "strength": 4, "stripped_text": "When you install this program, choose a server. Use this program only during runs on the chosen server. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.", "stripped_title": "Cyber-Cypher", "text": "When you install this program, choose a server. Use this program only during runs on the chosen server.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Cyber-Cypher", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_paricia_03045(Program):
    '''
    Cost: 0
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs of assets.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03045", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Perfect for flooding servers.", "illustrator": "Ed Mattinian", "memory_cost": 1, "pack_code": "cac", "position": 45, "quantity": 3, "side_code": "runner", "stripped_text": "2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs of assets.", "stripped_title": "Paricia", "text": "2[recurring-credit] <em>(When you install this card and before your turn begins, refill to 2 hosted credits.)</em>\nYou can spend hosted credits to pay trash costs of assets.", "title": "Paricia", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_selfmodifying_code_03046(Program):
    '''
    Cost: 0
    Text: 2 credits, trash: Search your stack for a program. Install it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03046", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"Make sure you tell the source code which executable you want it to compile into. One time I left my rig for a couple of minutes, and when I came back all of my files had been replaced with cat vids.\" -The Professor", "illustrator": "Lili Ibrahim", "memory_cost": 2, "pack_code": "cac", "position": 46, "quantity": 3, "side_code": "runner", "stripped_text": "2 credits, trash: Search your stack for a program. Install it.", "stripped_title": "Self-modifying Code", "text": "<strong>2[credit]</strong>, [trash]<strong>:</strong> Search your stack for a program. Install it.", "title": "Self-modifying Code", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sahasrara_03047(Program):
    '''
    Cost: 2
    Text: 2 recurring credits Use these credits to install programs (you cannot use Sahasrara to install a program that trashes Sahasrara).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03047", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Out there, the thousand-petaled lotus symbolizes detachment from illusion. In here, it is the birthplace of a higher consciousness. Something infinitely pure.", "illustrator": "Lili Ibrahim", "memory_cost": 1, "pack_code": "cac", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "2 recurring credits Use these credits to install programs (you cannot use Sahasrara to install a program that trashes Sahasrara).", "stripped_title": "Sahasrara", "text": "2[recurring-credit]\nUse these credits to install programs (you cannot use Sahasrara to install a program that trashes Sahasrara).", "title": "Sahasrara", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_inti_03048(Program):
    '''
    Cost: 0
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 2 credits: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03048", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"The Incans believed that the sun god resided in the Haman Pacha, the upper realm of the cosmos. They just didn't know that the Haman Pacha hadn't been discovered yet.\" -The Professor", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "cac", "position": 48, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 barrier subroutine. 2 credits: +1 strength for the remainder of this run.", "stripped_title": "Inti", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>2[credit]:</strong> +1 strength for the remainder of this run.", "title": "Inti", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_pawn_04002(Program):
    '''
    Cost: 0
    Text: click: Host this program on the outermost piece of ice protecting a central server. Whenever you make a successful run while this program is hosted on a piece of ice, host it on the next inward piece of ice. If you cannot, trash this program and install 1 other Caissa program from your grip or heap, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04002", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Liiga Smilshkalne", "keywords": "Ca\u00efssa - Trojan", "memory_cost": 0, "pack_code": "om", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "click: Host this program on the outermost piece of ice protecting a central server. Whenever you make a successful run while this program is hosted on a piece of ice, host it on the next inward piece of ice. If you cannot, trash this program and install 1 other Caissa program from your grip or heap, ignoring all costs.", "stripped_title": "Pawn", "text": "[click]: Host this program on the outermost piece of ice protecting a central server.\nWhenever you make a successful run while this program is hosted on a piece of ice, host it on the next inward piece of ice. If you cannot, trash this program and install 1 other <strong>Ca\u00efssa</strong> program from your grip or heap, ignoring all costs.", "title": "Pawn", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_rook_04003(Program):
    '''
    Cost: 2
    Text: While this program is hosted on ice, the rez cost of each piece of ice protecting this server is increased by 2. click: Host this program on a piece of ice that is not hosting a Caissa program. If this program is hosted on ice, its click ability can only be used to host it on ice protecting the same server or in the same position as its current host ice. (Count positions from the innermost ice.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04003", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Gong Studios", "keywords": "Ca\u00efssa - Trojan", "memory_cost": 1, "pack_code": "om", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "While this program is hosted on ice, the rez cost of each piece of ice protecting this server is increased by 2. click: Host this program on a piece of ice that is not hosting a Caissa program. If this program is hosted on ice, its click ability can only be used to host it on ice protecting the same server or in the same position as its current host ice. (Count positions from the innermost ice.)", "stripped_title": "Rook", "text": "While this program is hosted on ice, the rez cost of each piece of ice protecting this server is increased by 2.\n[click]: Host this program on a piece of ice that is not hosting a <strong>Ca\u00efssa</strong> program.\nIf this program is hosted on ice, its [click] ability can only be used to host it on ice protecting the same server or in the same position as its current host ice. <em>(Count positions from the innermost ice.)</em>", "title": "Rook", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gorman_drip_v1_04005(Program):
    '''
    Cost: 1
    Text: Whenever the Corp spends a click to draw 1 card or gain 1 credit (not through a card ability), place 1 virus counter on Gorman Drip v1. click, trash: Gain 1 credit for each virus counter on Gorman Drip v1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04005", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "Simple in principle, a drip virus drains fractions of currency from their accounts into yours.", "illustrator": "Shawn Ye Zhongyi", "keywords": "Virus", "memory_cost": 1, "pack_code": "om", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp spends a click to draw 1 card or gain 1 credit (not through a card ability), place 1 virus counter on Gorman Drip v1. click, trash: Gain 1 credit for each virus counter on Gorman Drip v1.", "stripped_title": "Gorman Drip v1", "text": "Whenever the Corp spends a [click] to draw 1 card or gain 1[credit] (not through a card ability), place 1 virus counter on Gorman Drip v1.\n[click], [trash]: Gain 1[credit] for each virus counter on Gorman Drip v1.", "title": "Gorman Drip v1", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_false_echo_04007(Program):
    '''
    Cost: 1
    Text: Whenever you pass a piece of unrezzed ice, you may trash False Echo. If you do, the Corp must rez that ice or add it to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04007", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"What if this ice wants to be free?\" -Rielle \"Kit\" Peddler", "illustrator": "Anna Ignatieva", "memory_cost": 1, "pack_code": "om", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you pass a piece of unrezzed ice, you may trash False Echo. If you do, the Corp must rez that ice or add it to HQ.", "stripped_title": "False Echo", "text": "Whenever you pass a piece of unrezzed ice, you may trash False Echo. If you do, the Corp must rez that ice or add it to HQ.", "title": "False Echo", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_bishop_04021(Program):
    '''
    Cost: 0
    Text: Host ice gets -2 strength. click: Host this program on a piece of ice that is not hosting a Caissa program. If this program is hosted on ice protecting a central server, its click ability can only be used to host it on ice protecting a remote server. If this program is hosted on ice protecting a remote server, its click ability can only be used to host it on ice protecting a central server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04021", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Ca\u00efssa - Trojan", "memory_cost": 1, "pack_code": "st", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "Host ice gets -2 strength. click: Host this program on a piece of ice that is not hosting a Caissa program. If this program is hosted on ice protecting a central server, its click ability can only be used to host it on ice protecting a remote server. If this program is hosted on ice protecting a remote server, its click ability can only be used to host it on ice protecting a central server.", "stripped_title": "Bishop", "text": "Host ice gets -2 strength.\n[click]: Host this program on a piece of ice that is not hosting a <strong>Ca\u00efssa</strong> program.\nIf this program is hosted on ice protecting a central server, its [click] ability can only be used to host it on ice protecting a remote server. If this program is hosted on ice protecting a remote server, its [click] ability can only be used to host it on ice protecting a central server.", "title": "Bishop", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_scheherazade_04022(Program):
    '''
    Cost: 0
    Text: Scheherazade can host any number of programs. Whenever you install a program on Scheherazade, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04022", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "Installing 1001 programs puts you in the hacker hall of fame, or would if such an institution actually existed.", "illustrator": "Tim Durning", "keywords": "Daemon", "memory_cost": 0, "pack_code": "st", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "Scheherazade can host any number of programs. Whenever you install a program on Scheherazade, gain 1 credit.", "stripped_title": "Scheherazade", "text": "Scheherazade can host any number of programs.\nWhenever you install a program on Scheherazade, gain 1[credit].", "title": "Scheherazade", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_copycat_04025(Program):
    '''
    Cost: 1
    Text: Whenever you pass a piece of ice, you may trash Copycat. If you do, choose another rezzed copy of that piece of ice protecting any server. The run continues as if you had just passed the chosen piece of ice (you are now running from the new position).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04025", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "The copycat function should be used with extreme caution, or you might end up on the wrong side of cyberspace.", "illustrator": "Gong Studios", "memory_cost": 1, "pack_code": "st", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you pass a piece of ice, you may trash Copycat. If you do, choose another rezzed copy of that piece of ice protecting any server. The run continues as if you had just passed the chosen piece of ice (you are now running from the new position).", "stripped_title": "Copycat", "text": "Whenever you pass a piece of ice, you may trash Copycat. If you do, choose another rezzed copy of that piece of ice protecting any server. The run continues as if you had just passed the chosen piece of ice (you are now running from the new position).", "title": "Copycat", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_leviathan_04026(Program):
    '''
    Cost: 6
    Text: Interface -> 3 credits: Break up to 3 code gate subroutines. 3 credits: +5 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04026", "cost": 6, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "It's efficient as all hell, for certain very large values of \"efficient\". The whale avatar is either a nice touch or a tragic misapplication of programmer man-hour, depending on who you ask. -BT's Guide to Icebreaking", "illustrator": "Teuku Muharra", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "st", "position": 26, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 3 credits: Break up to 3 code gate subroutines. 3 credits: +5 strength.", "stripped_title": "Leviathan", "text": "Interface \u2192 <strong>3[credit]:</strong> Break up to 3 <strong>code gate</strong> subroutines.\n<strong>3[credit]:</strong> +5 strength.", "title": "Leviathan", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_knight_04043(Program):
    '''
    Cost: 2
    Text: Interface -> 2 credits: Break 1 subroutine on host ice. click: Host this program on a piece of ice that is not hosting a Caissa program. If this program is hosted on ice, its click ability cannot be used to host it on the next inward or outward piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04043", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "'Maneuver warfare' is a doctrine that advocates keeping an enemy off-balance. It works just as well in cyberspace as in reality.", "illustrator": "Christina Davis", "keywords": "Icebreaker - AI - Ca\u00efssa - Trojan", "memory_cost": 1, "pack_code": "mt", "position": 43, "quantity": 3, "side_code": "runner", "strength": 7, "stripped_text": "Interface -> 2 credits: Break 1 subroutine on host ice. click: Host this program on a piece of ice that is not hosting a Caissa program. If this program is hosted on ice, its click ability cannot be used to host it on the next inward or outward piece of ice.", "stripped_title": "Knight", "text": "Interface \u2192 <strong>2[credit]:</strong> Break 1 subroutine on host ice.\n<strong>[click]:</strong> Host this program on a piece of ice that is not hosting a <strong>Ca\u00efssa</strong> program.\nIf this program is hosted on ice, its [click] ability cannot be used to host it on the next inward or outward piece of ice.", "title": "Knight", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_expert_schedule_analyzer_04045(Program):
    '''
    Cost: 1
    Text: click: Run HQ. If successful, instead of breaching HQ, you may reveal all cards in HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04045", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Knowing is half the battle. The easy half, anyway.", "illustrator": "Anna Ignatieva", "memory_cost": 1, "pack_code": "mt", "position": 45, "quantity": 3, "side_code": "runner", "stripped_text": "click: Run HQ. If successful, instead of breaching HQ, you may reveal all cards in HQ.", "stripped_title": "Expert Schedule Analyzer", "text": "<strong>[click]:</strong> Run HQ. If successful, instead of breaching HQ, you may reveal all cards in HQ.", "title": "Expert Schedule Analyzer", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_torch_04047(Program):
    '''
    Cost: 9
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04047", "cost": 9, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "The core of the grid. A blinding sphere of light, teeming with energy, crackling with flame. Beyond were only twinkling bits of data in a field of darkness. No hacker dared approach the core, except one. He came back with a flare of code, a torch that burned with the fire of the core itself. The dark places of cyberspace were dark no more, and the legend of g00ru was born.", "illustrator": "Mike Nesbitt", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "mt", "position": 47, "quantity": 3, "side_code": "runner", "strength": 4, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.", "stripped_title": "Torch", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Torch", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_keyhole_04061(Program):
    '''
    Cost: 4
    Text: click: Run R&D. If successful, instead of breaching R&D, look at the top 3 cards of R&D. Trash 1 of those cards, then the Corp shuffles R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04061", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "The instructions claim that it sifts the most important data. 'Important', it has been found, is a highly relative term.", "illustrator": "Agri Karuniawan", "memory_cost": 2, "pack_code": "tc", "position": 61, "quantity": 3, "side_code": "runner", "stripped_text": "click: Run R&D. If successful, instead of breaching R&D, look at the top 3 cards of R&D. Trash 1 of those cards, then the Corp shuffles R&D.", "stripped_title": "Keyhole", "text": "<strong>[click]:</strong> Run R&D. If successful, instead of breaching R&D, look at the top 3 cards of R&D. Trash 1 of those cards, then the Corp shuffles R&D.\n", "title": "Keyhole", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_garrote_04065(Program):
    '''
    Cost: 7
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04065", "cost": 7, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "The first credited icebreaker was nothing more than a unique script to bypass the security calls on a Gibson 3 Data Sentry. Garrote has over 20,000 times the data as that first breaker, but the idea remains the same: cut off the power source from the network, and then smash on through.", "illustrator": "Zefanya Langkan Maega", "keywords": "Icebreaker - Killer", "memory_cost": 2, "pack_code": "tc", "position": 65, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 1 credit: +1 strength.", "stripped_title": "Garrote", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Garrote", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sharpshooter_04067(Program):
    '''
    Cost: 1
    Text: Interface -> trash: Break any number of destroyer subroutines. 1 credit: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04067", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"One-shot icebreakers are popular among many of my prot\u00e9g\u00e9s. They don't have the patience for the hunt.\" -The Professor", "illustrator": "Ed Mattinian", "keywords": "Icebreaker", "memory_cost": 1, "pack_code": "tc", "position": 67, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> trash: Break any number of destroyer subroutines. 1 credit: +2 strength.", "stripped_title": "Sharpshooter", "text": "Interface \u2192 <strong>[trash]:</strong> Break any number of <strong>destroyer</strong> subroutines.\n<strong>1[credit]:</strong> +2 strength.", "title": "Sharpshooter", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_hemorrhage_04082(Program):
    '''
    Cost: 3
    Text: Whenever you make a successful run, place 1 virus counter on Hemorrhage. click, 2 hosted virus counters: The Corp trashes 1 card from HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04082", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "Bleeding data is more of a science than an art. Too much and you can end up with a one-way ticket to flatline city. Not enough and you might as well be running an empty server.", "illustrator": "Ed Mattinian", "keywords": "Virus", "memory_cost": 1, "pack_code": "fal", "position": 82, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run, place 1 virus counter on Hemorrhage. click, 2 hosted virus counters: The Corp trashes 1 card from HQ.", "stripped_title": "Hemorrhage", "text": "Whenever you make a successful run, place 1 virus counter on Hemorrhage.\n[click], <strong>2 hosted virus counters:</strong> The Corp trashes 1 card from HQ.", "title": "Hemorrhage", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_alpha_04087(Program):
    '''
    Cost: 7
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. This program can only interface with the outermost piece of ice protecting a server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04087", "cost": 7, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "The beginning\u2026", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "fal", "position": 87, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. This program can only interface with the outermost piece of ice protecting a server.", "stripped_title": "Alpha", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine.\n<strong>1[credit]:</strong> +1 strength.\nThis program can only interface with the outermost piece of ice protecting a server.", "title": "Alpha", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_omega_04088(Program):
    '''
    Cost: 7
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. This program can only interface with the innermost piece of ice protecting a server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04088", "cost": 7, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\u2026and the end?", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "fal", "position": 88, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. This program can only interface with the innermost piece of ice protecting a server.", "stripped_title": "Omega", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine.\n<strong>1[credit]:</strong> +1 strength.\nThis program can only interface with the innermost piece of ice protecting a server.", "title": "Omega", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_savoirfaire_04105(Program):
    '''
    Cost: 0
    Text: You cannot use Savoir-faire more than once each turn. 2 credits: Install a program from your grip, paying the install cost.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04105", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Predictive algorithms that fetch you the program you need before you even know you need it. My second favorite lady.\" -Gabriel Santiago", "illustrator": "RC Torres", "memory_cost": 1, "pack_code": "dt", "position": 105, "quantity": 3, "side_code": "runner", "stripped_text": "You cannot use Savoir-faire more than once each turn. 2 credits: Install a program from your grip, paying the install cost.", "stripped_title": "Savoir-faire", "text": "You cannot use Savoir-faire more than once each turn.\n2[credit]: Install a program from your grip, paying the install cost.", "title": "Savoir-faire", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_paintbrush_04108(Program):
    '''
    Cost: 3
    Text: click: Choose a rezzed piece of ice. That ice gains sentry, code gate or barrier until the end of the next run this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04108", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "\"Hand-made code is like hand-made art. You can see the brush strokes, which lets you see the artist. And then you can see everything in a new way.\" -Kate \"Mac\" McCaffrey", "illustrator": "Viktoria Gavrilenko", "memory_cost": 2, "pack_code": "dt", "position": 108, "quantity": 3, "side_code": "runner", "stripped_text": "click: Choose a rezzed piece of ice. That ice gains sentry, code gate or barrier until the end of the next run this turn.", "stripped_title": "Paintbrush", "text": "[click]: Choose a rezzed piece of ice. That ice gains <strong>sentry</strong>, <strong>code gate</strong> or <strong>barrier</strong> until the end of the next run this turn.", "title": "Paintbrush", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_alias_05041(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +3 strength. This program cannot interface with ice protecting a remote server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05041", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Appearances are easy to change in cyberspace, but a high-quality render is not easy to mimic.", "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "hap", "position": 41, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +3 strength. This program cannot interface with ice protecting a remote server.", "stripped_title": "Alias", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +3 strength.\nThis program cannot interface with ice protecting a remote server.", "title": "Alias", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_breach_05042(Program):
    '''
    Cost: 2
    Text: Interface -> 2 credits: Break up to 3 barrier subroutines. 2 credits: +4 strength. This program cannot interface with ice protecting a remote server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05042", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "hap", "position": 42, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 2 credits: Break up to 3 barrier subroutines. 2 credits: +4 strength. This program cannot interface with ice protecting a remote server.", "stripped_title": "Breach", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 3 <strong>barrier</strong> subroutines.\n<strong>2[credit]:</strong> +4 strength.\nThis program cannot interface with ice protecting a remote server.", "title": "Breach", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_bug_05043(Program):
    '''
    Cost: 0
    Text: Install only if you made a successful run on HQ this turn. Whenever the Corp draws a card, you may pay 2 credits to reveal that card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05043", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "The digital equivalent of a fly on the wall.", "illustrator": "Liiga Smilshkalne", "memory_cost": 1, "pack_code": "hap", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "Install only if you made a successful run on HQ this turn. Whenever the Corp draws a card, you may pay 2 credits to reveal that card.", "stripped_title": "Bug", "text": "Install only if you made a successful run on HQ this turn.\nWhenever the Corp draws a card, you may pay 2[credit] to reveal that card.", "title": "Bug", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gingerbread_05044(Program):
    '''
    Cost: 2
    Text: Interface -> 1 credit: Break 1 tracer subroutine. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05044", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Catch me if you can!", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker", "memory_cost": 1, "pack_code": "hap", "position": 44, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 tracer subroutine. 2 credits: +3 strength.", "stripped_title": "Gingerbread", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>tracer</strong> subroutine.\n<strong>2[credit]:</strong> +3 strength.", "title": "Gingerbread", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_grappling_hook_05045(Program):
    '''
    Cost: 2
    Text: trash: Break all but 1 subroutine on a piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05045", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "If speed is of the essence, an indirect encounter with a piece of ice is usually best.", "illustrator": "Zefanya Langkan Maega", "memory_cost": 1, "pack_code": "hap", "position": 45, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Break all but 1 subroutine on a piece of ice.", "stripped_title": "Grappling Hook", "text": "[trash]: Break all but 1 subroutine on a piece of ice.", "title": "Grappling Hook", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_passport_05046(Program):
    '''
    Cost: 1
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. This program cannot interface with ice protecting a remote server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05046", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Nothing is secure when you have the right documentation.", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "hap", "position": 46, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. This program cannot interface with ice protecting a remote server.", "stripped_title": "Passport", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> +2 strength.\nThis program cannot interface with ice protecting a remote server.", "title": "Passport", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_overmind_05053(Program):
    '''
    Cost: 4
    Text: When you install this program, place 1 power counter on it for each unused MU. (Place counters after this program's MU cost applies.) Interface -> Hosted power counter: Break 1 subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05053", "cost": 4, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "hap", "position": 53, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "When you install this program, place 1 power counter on it for each unused MU. (Place counters after this program's MU cost applies.) Interface -> Hosted power counter: Break 1 subroutine. 1 credit: +1 strength.", "stripped_title": "Overmind", "text": "When you install this program, place 1 power counter on it for each unused MU. <em>(Place counters after this program's MU cost applies.)</em>\nInterface \u2192 <strong>Hosted power counter:</strong> Break 1 subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Overmind", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_lamprey_06014(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run on HQ, the Corp loses 1 credit. Trash Lamprey if the Corp purges virus counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06014", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Smirtouille", "keywords": "Virus", "memory_cost": 1, "pack_code": "up", "position": 14, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on HQ, the Corp loses 1 credit. Trash Lamprey if the Corp purges virus counters.", "stripped_title": "Lamprey", "text": "Whenever you make a successful run on HQ, the Corp loses 1[credit].\nTrash Lamprey if the Corp purges virus counters.", "title": "Lamprey", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_leprechaun_06019(Program):
    '''
    Cost: 2
    Text: Leprechaun can host up to 2 programs. The memory costs of hosted programs do not count against your memory limit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06019", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"I once saw someone running a seven-tier nested daemon tree. Not for any good reason, just to see if he could. Well, of course the root daemon crashed and he lost everything. I wonder what he's up to now?\" -Kate \"Mac\" McCaffrey", "illustrator": "Liiga Smilshkalne", "keywords": "Daemon", "memory_cost": 1, "pack_code": "up", "position": 19, "quantity": 3, "side_code": "runner", "stripped_text": "Leprechaun can host up to 2 programs. The memory costs of hosted programs do not count against your memory limit.", "stripped_title": "Leprechaun", "text": "Leprechaun can host up to 2 programs. The memory costs of hosted programs do not count against your memory limit.", "title": "Leprechaun", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_d4v1d_06033(Program):
    '''
    Cost: 3
    Text: Place 3 power counters on D4v1d when it is installed. Hosted power counter: Break ice subroutine on a piece of ice that has a strength of 5 or greater.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06033", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "Sometimes a single stone is enough.", "illustrator": "Andreas Zafiratos", "memory_cost": 1, "pack_code": "tsb", "position": 33, "quantity": 3, "side_code": "runner", "stripped_text": "Place 3 power counters on D4v1d when it is installed. Hosted power counter: Break ice subroutine on a piece of ice that has a strength of 5 or greater.", "stripped_title": "D4v1d", "text": "Place 3 power counters on D4v1d when it is installed.\n<strong>Hosted power counter:</strong> Break ice subroutine on a piece of ice that has a strength of 5 or greater.", "title": "D4v1d", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cache_06037(Program):
    '''
    Cost: 1
    Text: Place 3 virus counters on Cache when it is installed. Hosted virus counter: Gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06037", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"People keep saying that 'Cash is king' in the business, like it's untraceable in the days of DNA sniffers and microtracers. Digital credits can be just as anonymous, and they're just as easy to counterfeit.\" -Silhouette", "illustrator": "Ed Mattinian", "keywords": "Virus", "memory_cost": 1, "pack_code": "tsb", "position": 37, "quantity": 3, "side_code": "runner", "stripped_text": "Place 3 virus counters on Cache when it is installed. Hosted virus counter: Gain 1 credit.", "stripped_title": "Cache", "text": "Place 3 virus counters on Cache when it is installed.\n<strong>Hosted virus counter:</strong> Gain 1[credit].", "title": "Cache", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_llds_energy_regulator_06039(Program):
    '''
    Cost: 0
    Text: 3 credits or trash: Prevent an installed piece of hardware from being trashed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06039", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Originally not very popular, the regulator was overlooked by those who used energy sinks to protect their rig. But it quickly found an audience once Smoke casted a run on a Blue Sun server, using it to keep her rig online while repeatedly diverting energy spikes in excess of 50,000 volts.", "illustrator": "Ed Mattinian", "memory_cost": 1, "pack_code": "tsb", "position": 39, "quantity": 3, "side_code": "runner", "stripped_text": "3 credits or trash: Prevent an installed piece of hardware from being trashed.", "stripped_title": "LLDS Energy Regulator", "text": "3[credit] or [trash]: Prevent an installed piece of hardware from being trashed.", "title": "LLDS Energy Regulator", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_blackat_06053(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 barrier subroutine. If you spent a credit from a stealth card to use this ability, instead break up to 3 barrier subroutines. 2 credits: +1 strength. If you spent at least 1 credit from a stealth card to use this ability, instead +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06053", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Bad luck for any sysop blind enough to cross its path.", "illustrator": "Seage", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "fc", "position": 53, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 1 credit: Break 1 barrier subroutine. If you spent a credit from a stealth card to use this ability, instead break up to 3 barrier subroutines. 2 credits: +1 strength. If you spent at least 1 credit from a stealth card to use this ability, instead +2 strength.", "stripped_title": "BlacKat", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine. If you spent a credit from a <strong>stealth</strong> card to use this ability, instead break up to 3 <strong>barrier</strong> subroutines.\n<strong>2[credit]:</strong> +1 strength. If you spent at least 1 credit from a <strong>stealth</strong> card to use this ability, instead +2 strength.", "title": "BlacKat", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_refractor_06057(Program):
    '''
    Cost: 1
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +3 strength. Use this ability only by spending a credit from a stealth card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06057", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"If you look like you belong, people will ignore you for hours. Or years. It's only when you don't fit in that things start to go wrong.\" -Exile", "illustrator": "Hannah Christenson", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "fc", "position": 57, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +3 strength. Use this ability only by spending a credit from a stealth card.", "stripped_title": "Refractor", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +3 strength. Use this ability only by spending a credit from a <strong>stealth</strong> card.", "title": "Refractor", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_origami_06074(Program):
    '''
    Cost: 0
    Text: Your maximum hand size is increased by 1 for each copy of Origami installed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06074", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "The earliest instances of data folding were inspired by the traditional art of origami. Just as a crease pattern is the blueprint of a paper crane, there is a sequence to data that must be considered in order to achieve the greatest result.", "illustrator": "Adam S. Doyle", "memory_cost": 1, "pack_code": "uao", "position": 74, "quantity": 3, "side_code": "runner", "stripped_text": "Your maximum hand size is increased by 1 for each copy of Origami installed.", "stripped_title": "Origami", "text": "Your maximum hand size is increased by 1 for each copy of Origami installed.", "title": "Origami", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_switchblade_06077(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break any number of sentry subroutines. Use this ability only by spending a credit from a stealth card. 1 credit: +7 strength. Use this ability only by spending a credit from a stealth card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06077", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Small. Compact. Easy to slip by monitoring programs and it can do some damage.", "illustrator": "Chris Newman", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "uao", "position": 77, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "Interface -> 1 credit: Break any number of sentry subroutines. Use this ability only by spending a credit from a stealth card. 1 credit: +7 strength. Use this ability only by spending a credit from a stealth card.", "stripped_title": "Switchblade", "text": "Interface \u2192 <strong>1[credit]:</strong> Break any number of <strong>sentry</strong> subroutines. Use this ability only by spending a credit from a <strong>stealth</strong> card.\n<strong>1[credit]:</strong> +7 strength. Use this ability only by spending a credit from a <strong>stealth</strong> card.", "title": "Switchblade", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cerberus_cuj0_h3_06094(Program):
    '''
    Cost: 3
    Text: When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 sentry subroutines. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06094", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"He only likes to eat live meat.\" -MaxX", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "atr", "position": 94, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 sentry subroutines. 1 credit: +1 strength.", "stripped_title": "Cerberus \"Cuj.0\" H3", "text": "When you install this program, place 4 power counters on it.\nInterface \u2192 <strong>Hosted power counter:</strong> Break up to 2 <strong>sentry</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength.", "title": "Cerberus \"Cuj.0\" H3", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cerberus_rex_h2_06096(Program):
    '''
    Cost: 3
    Text: When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06096", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Useful for fetching all sorts of things\u2026but you better have a treat ready if he likes it.\" -Iain Stirling", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "atr", "position": 96, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 code gate subroutines. 1 credit: +1 strength.", "stripped_title": "Cerberus \"Rex\" H2", "text": "When you install this program, place 4 power counters on it.\nInterface \u2192 <strong>Hosted power counter:</strong> Break up to 2 <strong>code gate</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength.", "title": "Cerberus \"Rex\" H2", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cerberus_lady_h1_06099(Program):
    '''
    Cost: 4
    Text: When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 barrier subroutines. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06099", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"Its bytes are definitely worse than its bark.\" -Chaos Theory", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "atr", "position": 99, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 barrier subroutines. 1 credit: +1 strength.", "stripped_title": "Cerberus \"Lady\" H1", "text": "When you install this program, place 4 power counters on it.\nInterface \u2192 <strong>Hosted power counter:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength.", "title": "Cerberus \"Lady\" H1", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_incubator_06113(Program):
    '''
    Cost: 3
    Text: When your turn begins, place 1 virus counter on Incubator. click, trash: Move all virus counters from Incubator to another installed virus program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06113", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"What terrors hatch in her dispossessed mind, waiting for their moment to be born? My money's on a double-helix rainbow with the head of a panda.\" -fakespeare", "illustrator": "Smirtouille", "keywords": "Virus", "memory_cost": 1, "pack_code": "ts", "position": 113, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, place 1 virus counter on Incubator. click, trash: Move all virus counters from Incubator to another installed virus program.", "stripped_title": "Incubator", "text": "When your turn begins, place 1 virus counter on Incubator.\n[click], [trash]: Move all virus counters from Incubator to another installed <strong>virus</strong> program.", "title": "Incubator", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_ixodidae_06114(Program):
    '''
    Cost: 1
    Text: Whenever the Corp loses at least 1 credit, gain 1 credit. Trash Ixodidae if the Corp purges virus counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06114", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Digs in deeper than its Alabama counterpart.", "illustrator": "Bruno Balixa", "keywords": "Virus", "memory_cost": 1, "pack_code": "ts", "position": 114, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp loses at least 1 credit, gain 1 credit. Trash Ixodidae if the Corp purges virus counters.", "stripped_title": "Ixodidae", "text": "Whenever the Corp loses at least 1[credit], gain 1[credit].\nTrash Ixodidae if the Corp purges virus counters.", "title": "Ixodidae", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_collective_consciousness_06116(Program):
    '''
    Cost: 2
    Text: Draw 1 card whenever the Corp rezzes a piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06116", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"All programs are connected. The data that runs through one runs through all.\" -Rielle \"Kit\" Peddler", "illustrator": "Samuel R. Shimota", "memory_cost": 2, "pack_code": "ts", "position": 116, "quantity": 3, "side_code": "runner", "stripped_text": "Draw 1 card whenever the Corp rezzes a piece of ice.", "stripped_title": "Collective Consciousness", "text": "Draw 1 card whenever the Corp rezzes a piece of ice.", "title": "Collective Consciousness", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sage_06117(Program):
    '''
    Cost: 4
    Text: This program gets +1 strength for each unused MU. Interface -> 2 credits: Break 1 code gate or 1 barrier subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06117", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\u03b4\u1f76\u03c2 \u1f10\u03c2 \u03c4\u1f78\u03bd \u03b1\u1f50\u03c4\u1f78\u03bd \u03c0\u03bf\u03c4\u03b1\u03bc\u1f78\u03bd \u03bf\u1f50\u03ba \u1f02\u03bd \u1f10\u03bc\u03b2\u03b1\u03af\u03b7\u03c2", "illustrator": "Alexandra Douglass", "keywords": "Icebreaker - Decoder - Fracter", "memory_cost": 2, "pack_code": "ts", "position": 117, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "This program gets +1 strength for each unused MU. Interface -> 2 credits: Break 1 code gate or 1 barrier subroutine.", "stripped_title": "Sage", "text": "This program gets +1 strength for each unused MU.\nInterface \u2192 <strong>2[credit]:</strong> Break 1 <strong>code gate</strong> or 1 <strong>barrier</strong> subroutine.", "title": "Sage", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_au_revoir_06119(Program):
    '''
    Cost: 1
    Text: Gain 1 credit whenever you jack out.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06119", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "The datastream slipped away, and it felt like being born for a second time, if only you could remember the first. A rush of air fills the lungs to bursting, and you gasp it out, coughing and choking as the dim lights of the room shine with the brilliance of a thousand suns.", "illustrator": "Crystal Ben", "memory_cost": 1, "pack_code": "ts", "position": 119, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 1 credit whenever you jack out.", "stripped_title": "Au Revoir", "text": "Gain 1[credit] whenever you jack out.", "title": "Au Revoir", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_eater_07040(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 subroutine. You cannot access cards for the remainder of this run. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07040", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Nom nom nom.", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "oac", "position": 40, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 subroutine. You cannot access cards for the remainder of this run. 1 credit: +1 strength.", "stripped_title": "Eater", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine. You cannot access cards for the remainder of this run.\n<strong>1[credit]:</strong> +1 strength.", "title": "Eater", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gravedigger_07041(Program):
    '''
    Cost: 2
    Text: Whenever an installed Corp card is trashed, place 1 virus counter on Gravedigger. click, hosted virus counter: The Corp trashes the top card of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07041", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"Once your sniffer finds the protocols the server uses to trash its own data, you can spoof those same protocols. It's quite the show.\" -Ji \"Noise\" Reilly", "illustrator": "Hannah Christenson", "keywords": "Virus", "memory_cost": 1, "pack_code": "oac", "position": 41, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever an installed Corp card is trashed, place 1 virus counter on Gravedigger. click, hosted virus counter: The Corp trashes the top card of R&D.", "stripped_title": "Gravedigger", "text": "Whenever an installed Corp card is trashed, place 1 virus counter on Gravedigger.\n[click], <strong>hosted virus counter:</strong> The Corp trashes the top card of R&D.", "title": "Gravedigger", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_hivemind_07042(Program):
    '''
    Cost: 3
    Text: Place 1 virus counter on Hivemind when it is installed. Virus counters on Hivemind are considered to be hosted on all other virus programs for the purposes of card effects (and can be spent as if on them).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07042", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 5, "flavor": "\"We built the network. But then the network evolved. Can we be sure that it is not alive?\" -g00ru", "illustrator": "Donald Crank", "keywords": "Virus", "memory_cost": 2, "pack_code": "oac", "position": 42, "quantity": 3, "side_code": "runner", "stripped_text": "Place 1 virus counter on Hivemind when it is installed. Virus counters on Hivemind are considered to be hosted on all other virus programs for the purposes of card effects (and can be spent as if on them).", "stripped_title": "Hivemind", "text": "Place 1 virus counter on Hivemind when it is installed.\nVirus counters on Hivemind are considered to be hosted on all other <strong>virus</strong> programs for the purposes of card effects (and can be spent as if on them).", "title": "Hivemind", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_progenitor_07043(Program):
    '''
    Cost: 0
    Text: You can install virus programs onto this program. Limit 1 hosted program. The memory cost of the hosted program does not count against your memory limit. Interrupt -> Whenever virus counters would be purged, prevent 1 virus counter on the hosted program from being removed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07043", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Hannah Christenson", "keywords": "Daemon", "memory_cost": 0, "pack_code": "oac", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "You can install virus programs onto this program. Limit 1 hosted program. The memory cost of the hosted program does not count against your memory limit. Interrupt -> Whenever virus counters would be purged, prevent 1 virus counter on the hosted program from being removed.", "stripped_title": "Progenitor", "text": "You can install <strong>virus</strong> programs onto this program. Limit 1 hosted program.\nThe memory cost of the hosted program does not count against your memory limit.\n[interrupt] \u2192 Whenever virus counters would be purged, prevent 1 virus counter on the hosted program from being removed.", "title": "Progenitor", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_clot_08001(Program):
    '''
    Cost: 2
    Text: The Corp cannot score an agenda during the same turn they installed that agenda. When the Corp purges virus counters, trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08001", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Virus", "memory_cost": 1, "pack_code": "val", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "The Corp cannot score an agenda during the same turn they installed that agenda. When the Corp purges virus counters, trash this program.", "stripped_title": "Clot", "text": "The Corp cannot score an agenda during the same turn they installed that agenda.\nWhen the Corp purges virus counters, trash this program.", "title": "Clot", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_spike_08004(Program):
    '''
    Cost: 1
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. This program gets +1 strength for each installed icebreaker. Interface -> trash: Break up to 3 barrier subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08004", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Fracter - Cloud", "memory_cost": 1, "pack_code": "val", "position": 4, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. This program gets +1 strength for each installed icebreaker. Interface -> trash: Break up to 3 barrier subroutines.", "stripped_title": "Spike", "text": "If you have at least 2[link], the memory cost of this program is 0[mu], even if it is not installed.\nThis program gets +1 strength for each installed <strong>icebreaker</strong>.\nInterface \u2192 <strong>[trash]:</strong> Break up to 3 <strong>barrier</strong> subroutines.", "title": "Spike", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_study_guide_08028(Program):
    '''
    Cost: 3
    Text: This program gets +1 strength for each hosted power counter. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: Place 1 power counter on this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08028", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "\"Once you download the lecture source files, this program does a statistical analysis and distills the most important concepts.\" -Hayley Kaplan", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "bb", "position": 28, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "This program gets +1 strength for each hosted power counter. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: Place 1 power counter on this program.", "stripped_title": "Study Guide", "text": "This program gets +1 strength for each hosted power counter.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> Place 1 power counter on this program.", "title": "Study Guide", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_crowbar_08046(Program):
    '''
    Cost: 1
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. This program gets +1 strength for each installed icebreaker. Interface -> trash: Break up to 3 code gate subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08046", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Decoder - Cloud", "memory_cost": 1, "pack_code": "cc", "position": 46, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. This program gets +1 strength for each installed icebreaker. Interface -> trash: Break up to 3 code gate subroutines.", "stripped_title": "Crowbar", "text": "If you have at least 2[link], the memory cost of this program is 0[mu], even if it is not installed.\nThis program gets +1 strength for each installed <strong>icebreaker</strong>.\nInterface \u2192 <strong>[trash]:</strong> Break up to 3 <strong>code gate</strong> subroutines.", "title": "Crowbar", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_analog_dreamers_08048(Program):
    '''
    Cost: 2
    Text: click: Run R&D. If successful, instead of breaching R&D, you may choose 1 unrezzed non-ice card with no advancement counters on it. The Corp shuffles that card into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08048", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Sometimes progress means returning to the past.", "illustrator": "Laura Wilson", "memory_cost": 1, "pack_code": "cc", "position": 48, "quantity": 3, "side_code": "runner", "stripped_text": "click: Run R&D. If successful, instead of breaching R&D, you may choose 1 unrezzed non-ice card with no advancement counters on it. The Corp shuffles that card into R&D.", "stripped_title": "Analog Dreamers", "text": "<strong>[click]:</strong> Run R&D. If successful, instead of breaching R&D, you may choose 1 unrezzed non-ice card with no advancement counters on it. The Corp shuffles that card into R&D.", "title": "Analog Dreamers", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_faust_08061(Program):
    '''
    Cost: 3
    Text: Interface -> Trash a card from your grip: Break 1 subroutine. Trash a card from your grip: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08061", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "The server was quiet that night. I closed my eyes, the low-hum of the datastream lulling me into a trance. When I opened them, the construct stood before me in the shape of a man, clad in light of many colors. His stature was impressive, and his saccharine voice wormed its way into my very soul.", "illustrator": "Marko Fiedler", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "uw", "position": 61, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> Trash a card from your grip: Break 1 subroutine. Trash a card from your grip: +2 strength.", "stripped_title": "Faust", "text": "Interface \u2192 <strong>Trash a card from your grip:</strong> Break 1 subroutine.\n<strong>Trash a card from your grip:</strong> +2 strength.", "title": "Faust", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_shiv_08066(Program):
    '''
    Cost: 0
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. This program gets +1 strength for each installed icebreaker. Interface -> trash: Break up to 3 sentry subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08066", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Killer - Cloud", "memory_cost": 1, "pack_code": "uw", "position": 66, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. This program gets +1 strength for each installed icebreaker. Interface -> trash: Break up to 3 sentry subroutines.", "stripped_title": "Shiv", "text": "If you have at least 2[link], the memory cost of this program is 0[mu], even if it is not installed.\nThis program gets +1 strength for each installed <strong>icebreaker</strong>.\nInterface \u2192 <strong>[trash]:</strong> Break up to 3 <strong>sentry</strong> subroutines.", "title": "Shiv", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_chameleon_08069(Program):
    '''
    Cost: 2
    Text: When you install this program, choose barrier, code gate, or sentry. When your discard phase ends, add this program to your grip. Interface -> 1 credit: Break 1 subroutine on a piece of ice that has the chosen subtype.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08069", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker", "memory_cost": 1, "pack_code": "uw", "position": 69, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "When you install this program, choose barrier, code gate, or sentry. When your discard phase ends, add this program to your grip. Interface -> 1 credit: Break 1 subroutine on a piece of ice that has the chosen subtype.", "stripped_title": "Chameleon", "text": "When you install this program, choose <strong>barrier</strong>, <strong>code gate</strong>, or <strong>sentry</strong>.\nWhen your discard phase ends, add this program to your grip.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 subroutine on a piece of ice that has the chosen subtype.", "title": "Chameleon", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_hyperdriver_08070(Program):
    '''
    Cost: 1
    Text: When your turn begins, you may remove Hyperdriver from the game and gain click click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08070", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"It doesn't actually bend time. It just feels like it. That's relativity.\" -Hayley Kaplan", "illustrator": "Adam S. Doyle", "memory_cost": 3, "pack_code": "uw", "position": 70, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may remove Hyperdriver from the game and gain click click click.", "stripped_title": "Hyperdriver", "text": "When your turn begins, you may remove Hyperdriver from the game and gain [click][click][click].", "title": "Hyperdriver", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_trope_08081(Program):
    '''
    Cost: 1
    Text: When your turn begins, place 1 power counter on Trope. click, remove Trope from the game: Shuffle 1 card from your heap into your stack for each power counter on Trope.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08081", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"Did you ever notice how everything goes in cycles? The stuff that's cool now was cool before. That's why I keep copy of everything!\" -Princess Space Kitten", "illustrator": "Reiko Murakami", "memory_cost": 1, "pack_code": "oh", "position": 81, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, place 1 power counter on Trope. click, remove Trope from the game: Shuffle 1 card from your heap into your stack for each power counter on Trope.", "stripped_title": "Trope", "text": "When your turn begins, place 1 power counter on Trope.\n[click], <strong>remove Trope from the game:</strong> Shuffle 1 card from your heap into your stack for each power counter on Trope.", "title": "Trope", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_surfer_08102(Program):
    '''
    Cost: 2
    Text: 2 credits: Swap a piece of barrier ice currently being encountered with a piece of ice directly before or after it. The run continues from this new position. You are still encountering that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08102", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Cowabunga, dude!", "illustrator": "Victor Garcia", "memory_cost": 1, "pack_code": "uot", "position": 102, "quantity": 3, "side_code": "runner", "stripped_text": "2 credits: Swap a piece of barrier ice currently being encountered with a piece of ice directly before or after it. The run continues from this new position. You are still encountering that ice.", "stripped_title": "Surfer", "text": "2[credit]: Swap a piece of <strong>barrier</strong> ice currently being encountered with a piece of ice directly before or after it. The run continues from this new position. You are still encountering that ice.", "title": "Surfer", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_davinci_08107(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run, place 1 power counter on DaVinci. trash: Install a card from your grip with an install cost equal to or less than the number of power counters on DaVinci, ignoring the install cost.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08107", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Our life is made by the death of others.\" -Leonardo Da Vinci", "illustrator": "Alexandr Elichev", "memory_cost": 1, "pack_code": "uot", "position": 107, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run, place 1 power counter on DaVinci. trash: Install a card from your grip with an install cost equal to or less than the number of power counters on DaVinci, ignoring the install cost.", "stripped_title": "DaVinci", "text": "Whenever you make a successful run, place 1 power counter on DaVinci.\n[trash]: Install a card from your grip with an install cost equal to or less than the number of power counters on DaVinci, ignoring the install cost.", "title": "DaVinci", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_endless_hunger_09033(Program):
    '''
    Cost: 0
    Text: Interface -> Trash 1 installed card: Break 1 "Subroutine End the run." subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09033", "cost": 0, "deck_limit": 3, "faction_code": "apex", "faction_cost": 2, "flavor": "\"I've been monitoring the anomaly's activity across the New Angeles Pacifica and Andea trunk lines and associated nodes. I have yet to detect a predictable pattern or even to formulate a theory as to the anomaly's nature.\" -Jos\u00e9o Greene, SYNC Analyst", "illustrator": "Hannah Christenson", "keywords": "Icebreaker", "memory_cost": 4, "pack_code": "dad", "position": 33, "quantity": 3, "side_code": "runner", "strength": 11, "stripped_text": "Interface -> Trash 1 installed card: Break 1 \"Subroutine End the run.\" subroutine.", "stripped_title": "Endless Hunger", "text": "Interface \u2192 <strong>Trash 1 installed card:</strong> Break 1 \"[subroutine] End the run.\" subroutine.", "title": "Endless Hunger", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_harbinger_09034(Program):
    '''
    Cost: 0
    Text: Interrupt -> When this program would be trashed, turn it facedown instead of adding it to your heap. (It is still considered trashed.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09034", "cost": 0, "deck_limit": 3, "faction_code": "apex", "faction_cost": 1, "flavor": "I AM BECOME DEATH", "illustrator": "Adam S. Doyle", "memory_cost": 0, "pack_code": "dad", "position": 34, "quantity": 3, "side_code": "runner", "stripped_text": "Interrupt -> When this program would be trashed, turn it facedown instead of adding it to your heap. (It is still considered trashed.)", "stripped_title": "Harbinger", "text": "[interrupt] \u2192 When this program would be trashed, turn it facedown instead of adding it to your heap. <em>(It is still considered trashed.)</em>", "title": "Harbinger", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_multithreader_09040(Program):
    '''
    Cost: 3
    Text: 2 recurring credits Use these credits to pay for using programs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09040", "cost": 3, "deck_limit": 3, "faction_code": "adam", "faction_cost": 1, "flavor": "Bioroids have two brains running in parallel, each capable of running sophisticated programming. There are certain advantages to the setup.", "illustrator": "Lili Ibrahim", "memory_cost": 1, "pack_code": "dad", "position": 40, "quantity": 3, "side_code": "runner", "stripped_text": "2 recurring credits Use these credits to pay for using programs.", "stripped_title": "Multithreader", "text": "2[recurring-credit]\nUse these credits to pay for using programs.", "title": "Multithreader", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gs_striker_m1_09048(Program):
    '''
    Cost: 4
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break any number of code gate subroutines. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09048", "cost": 4, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 2, "flavor": "Bigger.", "illustrator": "Ethan Patrick Harris", "keywords": "Icebreaker - Decoder - Cloud", "memory_cost": 1, "pack_code": "dad", "position": 48, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break any number of code gate subroutines. 2 credits: +3 strength.", "stripped_title": "GS Striker M1", "text": "If you have at least 2[link], the memory cost of this program is 0[mu], even if it is not installed.\nInterface \u2192 <strong>2[credit]:</strong> Break any number of <strong>code gate</strong> subroutines.\n<strong>2[credit]:</strong> +3 strength.", "title": "GS Striker M1", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gs_shrike_m2_09049(Program):
    '''
    Cost: 5
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break any number of sentry subroutines. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09049", "cost": 5, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 2, "flavor": "Badder.", "illustrator": "Donald Crank", "keywords": "Icebreaker - Killer - Cloud", "memory_cost": 1, "pack_code": "dad", "position": 49, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break any number of sentry subroutines. 2 credits: +3 strength.", "stripped_title": "GS Shrike M2", "text": "If you have at least 2[link], the memory cost of this program is 0[mu], even if it is not installed.\nInterface \u2192 <strong>2[credit]:</strong> Break any number of <strong>sentry</strong> subroutines.\n<strong>2[credit]:</strong> +3 strength.", "title": "GS Shrike M2", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gs_sherman_m3_09050(Program):
    '''
    Cost: 3
    Text: If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break any number of barrier subroutines. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09050", "cost": 3, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 2, "flavor": "Boom.", "illustrator": "Ethan Patrick Harris", "keywords": "Icebreaker - Fracter - Cloud", "memory_cost": 1, "pack_code": "dad", "position": 50, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "If you have at least 2 link, the memory cost of this program is 0 mu, even if it is not installed. Interface -> 2 credits: Break any number of barrier subroutines. 2 credits: +3 strength.", "stripped_title": "GS Sherman M3", "text": "If you have at least 2[link], the memory cost of this program is 0[mu], even if it is not installed.\nInterface \u2192 <strong>2[credit]:</strong> Break any number of <strong>barrier</strong> subroutines.\n<strong>2[credit]:</strong> +3 strength.", "title": "GS Sherman M3", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_mongoose_10005(Program):
    '''
    Cost: 3
    Text: You cannot use this program to break subroutines on more than one ice per run. Interface -> 1 credit: Break up to 2 sentry subroutines. 2 credits: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10005", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "It is the hardest thing in the world to frighten a mongoose, because he is eaten up from nose to tail with curiosity. The motto of all the mongoose family is \"Run and find out\". -Rudyard Kipling, Rikki-Tikki-Tavi", "illustrator": "Hannah Christenson", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "kg", "position": 5, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "You cannot use this program to break subroutines on more than one ice per run. Interface -> 1 credit: Break up to 2 sentry subroutines. 2 credits: +2 strength.", "stripped_title": "Mongoose", "text": "You cannot use this program to break subroutines on more than one ice per run.\nInterface \u2192 <strong>1[credit]:</strong> Break up to 2 <strong>sentry</strong> subroutines.\n<strong>2[credit]:</strong> +2 strength.", "title": "Mongoose", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_panchatantra_10008(Program):
    '''
    Cost: 2
    Text: Once per turn, when you encounter a piece of ice, you may have it gain 1 subtype of your choice that is not sentry, code gate, or barrier for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10008", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"The basics should be like the stories you learned as a child\u2014unconscious, never forgotten, and suddenly relevant at the most random times.\" -g00ru", "illustrator": "Hannah Christenson", "memory_cost": 1, "pack_code": "kg", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "Once per turn, when you encounter a piece of ice, you may have it gain 1 subtype of your choice that is not sentry, code gate, or barrier for the remainder of this run.", "stripped_title": "Panchatantra", "text": "Once per turn, when you encounter a piece of ice, you may have it gain 1 subtype of your choice that is not <strong>sentry</strong>, <strong>code gate</strong>, or <strong>barrier</strong> for the remainder of this run.", "title": "Panchatantra", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_diwan_10021(Program):
    '''
    Cost: 1
    Text: When you install this program, choose a server. As an additional cost to install a card in the root of or protecting that server, the Corp must pay 1 credit. When the Corp purges virus counters, trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10021", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Lili Ibrahim", "keywords": "Virus", "memory_cost": 1, "pack_code": "bf", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this program, choose a server. As an additional cost to install a card in the root of or protecting that server, the Corp must pay 1 credit. When the Corp purges virus counters, trash this program.", "stripped_title": "Diwan", "text": "When you install this program, choose a server. As an additional cost to install a card in the root of or protecting that server, the Corp must pay 1[credit].\nWhen the Corp purges virus counters, trash this program.", "title": "Diwan", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sadyojata_10044(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 subroutine on a piece of ice with 3 or more subtypes. 1 credit: +1 strength. 2 credits: Swap this program with a deva program from your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10044", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "The Creator.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - AI - Deva", "memory_cost": 1, "pack_code": "dag", "position": 44, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 subroutine on a piece of ice with 3 or more subtypes. 1 credit: +1 strength. 2 credits: Swap this program with a deva program from your grip.", "stripped_title": "Sadyojata", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine on a piece of ice with 3 or more subtypes.\n<strong>1[credit]:</strong> +1 strength.\n<strong>2[credit]:</strong> Swap this program with a <strong>deva</strong> program from your grip.", "title": "Sadyojata", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_vamadeva_10061(Program):
    '''
    Cost: 6
    Text: Interface -> 1 credit: Break 1 subroutine on a piece of ice with exactly 1 subroutine. 1 credit: +1 strength. 2 credits: Swap this program with a deva program from your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10061", "cost": 6, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "The Preserver.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - AI - Deva", "memory_cost": 1, "pack_code": "si", "position": 61, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 subroutine on a piece of ice with exactly 1 subroutine. 1 credit: +1 strength. 2 credits: Swap this program with a deva program from your grip.", "stripped_title": "Vamadeva", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine on a piece of ice with exactly 1 subroutine.\n<strong>1[credit]:</strong> +1 strength.\n<strong>2[credit]:</strong> Swap this program with a <strong>deva</strong> program from your grip.", "title": "Vamadeva", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_brahman_10062(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break up to 2 subroutines. 2 credits: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, add 1 installed non-virus program to the top of your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10062", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - AI", "memory_cost": 2, "pack_code": "si", "position": 62, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 1 credit: Break up to 2 subroutines. 2 credits: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, add 1 installed non-virus program to the top of your stack.", "stripped_title": "Brahman", "text": "Interface \u2192 <strong>1[credit]:</strong> Break up to 2 subroutines.\n<strong>2[credit]:</strong> +1 strength.\nWhenever an encounter ends, if you used this program to break a subroutine during that encounter, add 1 installed non-<strong>virus</strong> program to the top of your stack.", "title": "Brahman", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_aghora_10097(Program):
    '''
    Cost: 5
    Text: Interface -> 1 credit: Break 1 subroutine on a piece of ice that has a rez cost of 5 or greater. 1 credit: +1 strength. 2 credits: Swap this program with a deva program from your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10097", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "The Destroyer.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - AI - Deva", "memory_cost": 1, "pack_code": "ftm", "position": 97, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 subroutine on a piece of ice that has a rez cost of 5 or greater. 1 credit: +1 strength. 2 credits: Swap this program with a deva program from your grip.", "stripped_title": "Aghora", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine on a piece of ice that has a rez cost of 5 or greater.\n<strong>1[credit]:</strong> +1 strength.\n<strong>2[credit]:</strong> Swap this program with a <strong>deva</strong> program from your grip.", "title": "Aghora", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_ankusa_10101(Program):
    '''
    Cost: 6
    Text: Whenever this program fully breaks a barrier, add that barrier to HQ. Interface -> 2 credits: Break 1 barrier subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10101", "cost": 6, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "ftm", "position": 101, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "Whenever this program fully breaks a barrier, add that barrier to HQ. Interface -> 2 credits: Break 1 barrier subroutine. 1 credit: +1 strength.", "stripped_title": "Ankusa", "text": "Whenever this program fully breaks a <strong>barrier</strong>, add that <strong>barrier</strong> to HQ.\nInterface \u2192 <strong>2[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Ankusa", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_dai_v_11006(Program):
    '''
    Cost: 6
    Text: Interface -> 2 credits: Break all subroutines. Use this ability only by spending credits from stealth cards. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11006", "cost": 6, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "In running, as in reality, all elements are connected.", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "23s", "position": 6, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break all subroutines. Use this ability only by spending credits from stealth cards. 1 credit: +1 strength.", "stripped_title": "Dai V", "text": "Interface \u2192 <strong>2[credit]:</strong> Break all subroutines. Use this ability only by spending credits from <strong>stealth</strong> cards.\n<strong>1[credit]:</strong> +1 strength.", "title": "Dai V", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_nfr_11023(Program):
    '''
    Cost: 3
    Text: Whenever this program fully breaks a piece of ice, place 1 power counter on this program. This program gets +1 strength for each power counter on it. Interface -> 1 credit: Break 1 barrier subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11023", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Balance out the equation.", "illustrator": "Mariusz Siergiejew", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "bm", "position": 23, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Whenever this program fully breaks a piece of ice, place 1 power counter on this program. This program gets +1 strength for each power counter on it. Interface -> 1 credit: Break 1 barrier subroutine.", "stripped_title": "Nfr", "text": "Whenever this program fully breaks a piece of ice, place 1 power counter on this program.\nThis program gets +1 strength for each power counter on it.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.", "title": "Nfr", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_paperclip_11024(Program):
    '''
    Cost: 4
    Text: Whenever you encounter a barrier, you may install this program from your heap. X credits: +X strength. Then, if this program can interface with the barrier you are encountering, break up to X subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11024", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"It is not wise to call someone crazy until you fully understand what they're trying to say.\" -Omar Keung", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "bm", "position": 24, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Whenever you encounter a barrier, you may install this program from your heap. X credits: +X strength. Then, if this program can interface with the barrier you are encountering, break up to X subroutines.", "stripped_title": "Paperclip", "text": "Whenever you encounter a <strong>barrier</strong>, you may install this program from your heap.\n<strong>X[credit]:</strong> +X strength. Then, if this program can interface with the <strong>barrier</strong> you are encountering, break up to X subroutines.", "title": "Paperclip", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_golden_11025(Program):
    '''
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 sentry subroutines. 2 credits: +4 strength. 2 credits, add this program to your grip: Derez 1 sentry this program fully broke during this encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11025", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "The program was as close to a hunting raptor as she could afford...for now.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "bm", "position": 25, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break up to 2 sentry subroutines. 2 credits: +4 strength. 2 credits, add this program to your grip: Derez 1 sentry this program fully broke during this encounter.", "stripped_title": "Golden", "text": "Interface \u2192 2[credit]: Break up to 2 <strong>sentry</strong> subroutines.\n<strong>2[credit]:</strong> +4 strength.\n<strong>2[credit]</strong>, <strong>add this program to your grip:</strong> Derez 1 <strong>sentry</strong> this program fully broke during this encounter.", "title": "Golden", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_black_orchestra_11042(Program):
    '''
    Cost: 3
    Text: Whenever you encounter a code gate, you may install this program from your heap. 3 credits: +2 strength. Then, if this program can interface with the code gate you are encountering, break up to 2 subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11042", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"In extremity, your conscience may make you terrible.\" -Omar Keung, the Flashpoint", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "es", "position": 42, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Whenever you encounter a code gate, you may install this program from your heap. 3 credits: +2 strength. Then, if this program can interface with the code gate you are encountering, break up to 2 subroutines.", "stripped_title": "Black Orchestra", "text": "Whenever you encounter a <strong>code gate</strong>, you may install this program from your heap.\n<strong>3[credit]:</strong> +2 strength. Then, if this program can interface with the <strong>code gate</strong> you are encountering, break up to 2 subroutines.", "title": "Black Orchestra", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_peregrine_11044(Program):
    '''
    Cost: 5
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 3 credits: +3 strength. 2 credits, add this program to your grip: Derez 1 code gate this program fully broke during this encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11044", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Khan's avatar lifted her arm and the bird launched itself into the air.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "es", "position": 44, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 3 credits: +3 strength. 2 credits, add this program to your grip: Derez 1 code gate this program fully broke during this encounter.", "stripped_title": "Peregrine", "text": "Interface \u2192 1[credit]: Break 1 <strong>code gate</strong> subroutine.\n<strong>3[credit]:</strong> +3 strength.\n<strong>2[credit]</strong>, </strong>add this program to your grip:</strong> Derez 1 <strong>code gate</strong> this program fully broke during this encounter.", "title": "Peregrine", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_houdini_11045(Program):
    '''
    Cost: 2
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +4 strength for the remainder of this run. Use this ability only by spending at least 1 credit from a stealth card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11045", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "My brain is the key that sets my mind free.", "illustrator": "Galen Dara", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "es", "position": 45, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +4 strength for the remainder of this run. Use this ability only by spending at least 1 credit from a stealth card.", "stripped_title": "Houdini", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> +4 strength for the remainder of this run. Use this ability only by spending at least 1 credit from a <strong>stealth</strong> card.", "title": "Houdini", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_saker_11064(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 2 credits: +2 strength. 2 credits, add this program to your grip: Derez 1 barrier this program fully broke during this encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11064", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Spiraling even higher, every feature of cyberspace sprawled before it.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "in", "position": 64, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 barrier subroutine. 2 credits: +2 strength. 2 credits, add this program to your grip: Derez 1 barrier this program fully broke during this encounter.", "stripped_title": "Saker", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>2[credit]:</strong> +2 strength.\n<strong>2[credit]</strong>, <strong>add this program to your grip:</strong> Derez 1 <strong>barrier</strong> this program fully broke during this encounter.", "title": "Saker", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_blackstone_11068(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 3 credits: +4 strength for the remainder of this run. Use this ability only by spending at least 1 credit from a stealth card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11068", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "The personality must be bigger than the prop.", "illustrator": "Seage", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "in", "position": 68, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 1 credit: Break 1 barrier subroutine. 3 credits: +4 strength for the remainder of this run. Use this ability only by spending at least 1 credit from a stealth card.", "stripped_title": "Blackstone", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>3[credit]:</strong> +4 strength for the remainder of this run. Use this ability only by spending at least 1[credit] from a <strong>stealth</strong> card.", "title": "Blackstone", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_mkultra_11081(Program):
    '''
    Cost: 2
    Text: Whenever you encounter a sentry, you may install this program from your heap. 3 credits: +2 strength. Then, if this program can interface with the sentry you are encountering, break up to 2 subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11081", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"These things are always there, under the surface, but no one wants to know the truth.\" -Omar Keung, the Flashpoint", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "ml", "position": 81, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Whenever you encounter a sentry, you may install this program from your heap. 3 credits: +2 strength. Then, if this program can interface with the sentry you are encountering, break up to 2 subroutines.", "stripped_title": "MKUltra", "text": "Whenever you encounter a <strong>sentry</strong>, you may install this program from your heap.\n<strong>3[credit]:</strong> +2 strength. Then, if this program can interface with the <strong>sentry</strong> you are encountering, break up to 2 subroutines.", "title": "MKUltra", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_equivocation_11084(Program):
    '''
    Cost: 2
    Text: Whenever you make a successful run on R&D, you may reveal the top card of R&D. If you do, you may force the Corp to draw that card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11084", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "It is only the illusion of choice.", "illustrator": "Michelle Lockamy", "memory_cost": 1, "pack_code": "ml", "position": 84, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on R&D, you may reveal the top card of R&D. If you do, you may force the Corp to draw that card.", "stripped_title": "Equivocation", "text": "Whenever you make a successful run on R&D, you may reveal the top card of R&D. If you do, you may force the Corp to draw that card.", "title": "Equivocation", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_misdirection_11085(Program):
    '''
    Cost: 0
    Text: click, click, X credits: Remove X tags.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11085", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"It's the most fundamental element of illusions and running both. In either case, it should be the first skill you master.\" -Ele \"Smoke\" Scovak", "illustrator": "Michelle Lockamy", "memory_cost": 1, "pack_code": "ml", "position": 85, "quantity": 3, "side_code": "runner", "stripped_text": "click, click, X credits: Remove X tags.", "stripped_title": "Misdirection", "text": "[click], [click], X[credit]: Remove X tags.", "title": "Misdirection", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_reaver_11086(Program):
    '''
    Cost: 2
    Text: The first time you trash an installed card each turn, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11086", "cost": 2, "deck_limit": 3, "faction_code": "apex", "faction_cost": 4, "flavor": "\"It had been hoped that the Network disruptions surrounding the conflict might also disrupt the phenomenon. Evidently, the reverse is true.\" -Jos\u00e9o Greene, SYNC Analyst", "illustrator": "Adam S. Doyle", "memory_cost": 1, "pack_code": "ml", "position": 86, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you trash an installed card each turn, draw 1 card.", "stripped_title": "Reaver", "text": "The first time you trash an installed card each turn, draw 1 card.", "title": "Reaver", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_baba_yaga_11088(Program):
    '''
    Cost: 5
    Text: You may host any number of non-AI icebreaker programs on this program. This program gains the paid abilities of all hosted icebreaker programs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11088", "cost": 5, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 2, "flavor": "\"She was riding in a great iron mortar and driving it with the pestle, and as she came she swept away her trail behind her with a kitchen broom.\" -Vasilissa the Beautiful", "illustrator": "Shawn Ye Zhongyi", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "ml", "position": 88, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "You may host any number of non-AI icebreaker programs on this program. This program gains the paid abilities of all hosted icebreaker programs.", "stripped_title": "Baba Yaga", "text": "You may host any number of non-<strong>AI</strong> <strong>icebreaker</strong> programs on this program.\nThis program gains the paid abilities of all hosted <strong>icebreaker</strong> programs.", "title": "Baba Yaga", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sunya_11102(Program):
    '''
    Cost: 3
    Text: Whenever this program fully breaks a piece of ice, place 1 power counter on this program. This program gets +1 strength for each power counter on it. Interface -> 2 credits: Break 1 sentry subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11102", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Open yourself to the universe.", "illustrator": "Lale Ann", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "qu", "position": 102, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Whenever this program fully breaks a piece of ice, place 1 power counter on this program. This program gets +1 strength for each power counter on it. Interface -> 2 credits: Break 1 sentry subroutine.", "stripped_title": "Sunya", "text": "Whenever this program fully breaks a piece of ice, place 1 power counter on this program.\nThis program gets +1 strength for each power counter on it.\nInterface \u2192 <strong>2[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.", "title": "S\u016bnya", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_tapwrm_11104(Program):
    '''
    Cost: 0
    Text: Install only if you made a successful run on a central server this turn. When your turn begins, gain 1 credit for every 5 credits in the Corp's credit pool. Trash Tapwrm if the Corp purges virus counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11104", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Donald Crank", "keywords": "Virus", "memory_cost": 1, "pack_code": "qu", "position": 104, "quantity": 3, "side_code": "runner", "stripped_text": "Install only if you made a successful run on a central server this turn. When your turn begins, gain 1 credit for every 5 credits in the Corp's credit pool. Trash Tapwrm if the Corp purges virus counters.", "stripped_title": "Tapwrm", "text": "Install only if you made a successful run on a central server this turn.\nWhen your turn begins, gain 1[credit] for every 5[credit] in the Corp's credit pool.\nTrash Tapwrm if the Corp purges virus counters.", "title": "Tapwrm", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_tracker_11105(Program):
    '''
    Cost: 0
    Text: When your turn begins, you may choose a server. click, 2 credits: Run the chosen server. The first time a subroutine would resolve during that run, prevent it from resolving.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11105", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Everything leaves a ripple in cyberspace. If you can find the ripples, nothing can hide.\" -Khan", "illustrator": "Alexandr Elichev", "memory_cost": 2, "pack_code": "qu", "position": 105, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may choose a server. click, 2 credits: Run the chosen server. The first time a subroutine would resolve during that run, prevent it from resolving.", "stripped_title": "Tracker", "text": "When your turn begins, you may choose a server.\n<strong>[click]</strong>, <strong>2[credit]:</strong> Run the chosen server. The first time a subroutine would resolve during that run, prevent it from resolving.", "title": "Tracker", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_fawkes_11108(Program):
    '''
    Cost: 5
    Text: Interface -> 1 credit: Break 1 sentry subroutine. X credits: +X strength for the remainder of this run. Use this ability only by spending at least 1 credit from a stealth card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11108", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Faster than the eye can follow.", "illustrator": "Shawn Ye Zhongyi", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "qu", "position": 108, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. X credits: +X strength for the remainder of this run. Use this ability only by spending at least 1 credit from a stealth card.", "stripped_title": "Fawkes", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>X[credit]:</strong> +X strength for the remainder of this run. Use this ability only by spending at least 1 credit from a <strong>stealth</strong> card.", "title": "Fawkes", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_customized_secretary_12027(Program):
    '''
    Cost: 2
    Text: When you install Customized Secretary reveal the top 5 cards of the stack. You may host any number of revealed programs from your stack on it. Shuffle your stack. click: Install a hosted program, paying all install costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12027", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Liiga Smilshkalne", "memory_cost": 1, "pack_code": "so", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "When you install Customized Secretary reveal the top 5 cards of the stack. You may host any number of revealed programs from your stack on it. Shuffle your stack. click: Install a hosted program, paying all install costs.", "stripped_title": "Customized Secretary", "text": "When you install Customized Secretary reveal the top 5 cards of the stack. You may host any number of revealed programs from your stack on it. Shuffle your stack.\n[click]: Install a hosted program, paying all install costs.", "title": "Customized Secretary", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_berserker_12041(Program):
    '''
    Cost: 4
    Text: Whenever you encounter a barrier, for the remainder of that encounter this program gets +1 strength for each subroutine on that barrier. Interface -> 2 credits: Break up to 2 barrier subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12041", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "eas", "position": 41, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Whenever you encounter a barrier, for the remainder of that encounter this program gets +1 strength for each subroutine on that barrier. Interface -> 2 credits: Break up to 2 barrier subroutines.", "stripped_title": "Berserker", "text": "Whenever you encounter a <strong>barrier</strong>, for the remainder of that encounter this program gets +1 strength for each subroutine on that <strong>barrier</strong>.\nInterface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines.", "title": "Berserker", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_persephone_12042(Program):
    '''
    Cost: 5
    Text: Interface -> 2 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever you pass a sentry after encountering it, you may trash the top card of your stack. If you do, trash 1 card from the top of R&D for each subroutine on that sentry that resolved during that encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12042", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - Killer", "memory_cost": 2, "pack_code": "eas", "position": 42, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever you pass a sentry after encountering it, you may trash the top card of your stack. If you do, trash 1 card from the top of R&D for each subroutine on that sentry that resolved during that encounter.", "stripped_title": "Persephone", "text": "Interface \u2192 <strong>2[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.\nWhenever you pass a <strong>sentry</strong> after encountering it, you may trash the top card of your stack. If you do, trash 1 card from the top of R&D for each subroutine on that <strong>sentry</strong> that resolved during that encounter.", "title": "Persephone", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_inversificator_12048(Program):
    '''
    Cost: 6
    Text: The first time each turn you pass a piece of ice after an encounter during which this program fully broke that ice, you may swap it with another installed piece of ice. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12048", "cost": 6, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Donald Crank", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "eas", "position": 48, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "The first time each turn you pass a piece of ice after an encounter during which this program fully broke that ice, you may swap it with another installed piece of ice. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.", "stripped_title": "Inversificator", "text": "The first time each turn you pass a piece of ice after an encounter during which this program fully broke that ice, you may swap it with another installed piece of ice.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Inversificator", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_massdriver_12067(Program):
    '''
    Cost: 8
    Text: Whenever this program fully breaks a piece of ice, the first 3 subroutines of the next encounter this run do not resolve. Interface -> 2 credits: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12067", "cost": 8, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Alexandr Elichev", "keywords": "Icebreaker - Decoder", "memory_cost": 2, "pack_code": "baw", "position": 67, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Whenever this program fully breaks a piece of ice, the first 3 subroutines of the next encounter this run do not resolve. Interface -> 2 credits: Break 1 code gate subroutine. 1 credit: +1 strength.", "stripped_title": "Mass-Driver", "text": "Whenever this program fully breaks a piece of ice, the first 3 subroutines of the next encounter this run do not resolve.\nInterface \u2192 <strong>2[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Mass-Driver", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_god_of_war_12082(Program):
    '''
    Cost: 4
    Text: When your turn begins, you may take 1 tag to place 2 virus counters on this program. Interface -> Hosted virus counter: Break 1 subroutine. 2 credits: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12082", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"Subtle? You don't really understand the point of all of this, do you?\" -Alice Merchant", "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - AI - Virus", "memory_cost": 1, "pack_code": "fm", "position": 82, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "When your turn begins, you may take 1 tag to place 2 virus counters on this program. Interface -> Hosted virus counter: Break 1 subroutine. 2 credits: +1 strength.", "stripped_title": "God of War", "text": "When your turn begins, you may take 1 tag to place 2 virus counters on this program.\nInterface \u2192 <strong>Hosted virus counter:</strong> Break 1 subroutine.\n<strong>2[credit]:</strong> +1 strength.", "title": "God of War", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_flashbang_12085(Program):
    '''
    Cost: 5
    Text: Interface -> 6 credits: Derez the sentry you are encountering. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12085", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"It's my sentry cheat sheet.\" -Revenant", "illustrator": "Tim Durning", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "fm", "position": 85, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "Interface -> 6 credits: Derez the sentry you are encountering. 1 credit: +1 strength.", "stripped_title": "Flashbang", "text": "Interface \u2192 <strong>6[credit]:</strong> Derez the <strong>sentry</strong> you are encountering.\n<strong>1[credit]:</strong> +1 strength.", "title": "Flashbang", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_maven_12087(Program):
    '''
    Cost: 5
    Text: This program gets +1 strength for each installed program. Interface -> 2 credits: Break 1 subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12087", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI", "memory_cost": 2, "pack_code": "fm", "position": 87, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "This program gets +1 strength for each installed program. Interface -> 2 credits: Break 1 subroutine.", "stripped_title": "Maven", "text": "This program gets +1 strength for each installed program.\nInterface \u2192 <strong>2[credit]:</strong> Break 1 subroutine.", "title": "Maven", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_nanotk_12088(Program):
    '''
    Cost: 4
    Text: During runs, this program gets +1 strength for each piece of ice protecting the attacked server. Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12088", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"Anyone can hit someone where they are weakest.\" -S'onge Galaxy", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "fm", "position": 88, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "During runs, this program gets +1 strength for each piece of ice protecting the attacked server. Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +2 strength.", "stripped_title": "Na'Not'K", "text": "During runs, this program gets +1 strength for each piece of ice protecting the attacked server.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>3[credit]:</strong> +2 strength.", "title": "Na'Not'K", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_aumakua_12104(Program):
    '''
    Cost: 3
    Text: This program gets +1 strength for each hosted virus counter. Whenever you expose a card, place 1 virus counter on this program. Whenever you finish breaching a server, if you did not steal or trash any accessed cards, place 1 virus counter on this program. Interface -> 1 credit: Break 1 subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12104", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI - Virus", "memory_cost": 1, "pack_code": "cd", "position": 104, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "This program gets +1 strength for each hosted virus counter. Whenever you expose a card, place 1 virus counter on this program. Whenever you finish breaching a server, if you did not steal or trash any accessed cards, place 1 virus counter on this program. Interface -> 1 credit: Break 1 subroutine.", "stripped_title": "Aumakua", "text": "This program gets +1 strength for each hosted virus counter.\nWhenever you expose a card, place 1 virus counter on this program.\nWhenever you finish breaching a server, if you did not steal or trash any accessed cards, place 1 virus counter on this program.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 subroutine.", "title": "Aumakua", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_abagnale_13006(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. trash: Bypass the code gate you are encountering.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13006", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Technology breeds crime.\"", "illustrator": "BalanceSheet", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "td", "position": 6, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. trash: Bypass the code gate you are encountering.", "stripped_title": "Abagnale", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> +2 strength.\n[trash]<strong>:</strong> Bypass the <strong>code gate</strong> you are encountering.", "title": "Abagnale", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_lustig_13007(Program):
    '''
    Cost: 5
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +5 strength. trash: Bypass the sentry you are encountering.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13007", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Never boast. Just let your importance be quietly obvious.\"", "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "td", "position": 7, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +5 strength. trash: Bypass the sentry you are encountering.", "stripped_title": "Lustig", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>3[credit]:</strong> +5 strength.\n<strong>[trash]:</strong> Bypass the <strong>sentry</strong> you are encountering.", "title": "Lustig", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_demara_13008(Program):
    '''
    Cost: 4
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 2 credits: +3 strength. trash: Bypass the barrier you are encountering.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13008", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"It's a matter of 'acquiring' the right credentials.\"", "illustrator": "Mariusz Siergiejew", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "td", "position": 8, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break up to 2 barrier subroutines. 2 credits: +3 strength. trash: Bypass the barrier you are encountering.", "stripped_title": "Demara", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>2[credit]:</strong> +3 strength.\n<strong>[trash]:</strong> Bypass the <strong>barrier</strong> you are encountering.", "title": "Demara", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_mammon_13009(Program):
    '''
    Cost: 3
    Text: Interface -> Hosted power counter: Break 1 subroutine. 2 credits: +2 strength. When your turn begins, you may pay X credits to place X power counters on this program. When your turn ends, remove all hosted power counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13009", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "td", "position": 9, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "Interface -> Hosted power counter: Break 1 subroutine. 2 credits: +2 strength. When your turn begins, you may pay X credits to place X power counters on this program. When your turn ends, remove all hosted power counters.", "stripped_title": "Mammon", "text": "Interface \u2192 <strong>Hosted power counter:</strong> Break 1 subroutine.\n<strong>2[credit]:</strong> +2 strength.\nWhen your turn begins, you may pay X[credit] to place X power counters on this program.\nWhen your turn ends, remove all hosted power counters.", "title": "Mammon", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_adept_13017(Program):
    '''
    Cost: 5
    Text: This program gets +1 strength for each unused MU. Interface -> 2 credits: Break 1 sentry or barrier subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13017", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\u039c\u03b5\u03b3\u03ac\u03bb\u03bf \u03bc\u03ad\u03c1\u03bf\u03c2 \u03c4\u03b7\u03c2 \u03bc\u03ac\u03b8\u03b7\u03c3\u03b7\u03c2 \u03b4\u03b5\u03bd \u03b4\u03b9\u03b4\u03ac\u03c3\u03ba\u03b5\u03b9 \u03c4\u03b7\u03bd \u03ba\u03b1\u03c4\u03b1\u03bd\u03cc\u03b7\u03c3\u03b7", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Fracter - Killer", "memory_cost": 2, "pack_code": "td", "position": 17, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "This program gets +1 strength for each unused MU. Interface -> 2 credits: Break 1 sentry or barrier subroutine.", "stripped_title": "Adept", "text": "This program gets +1 strength for each unused MU.\nInterface \u2192 <strong>2[credit]:</strong> Break 1 <strong>sentry</strong> or <strong>barrier</strong> subroutine.", "title": "Adept", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_savant_13018(Program):
    '''
    Cost: 4
    Text: This program gets +1 strength for each unused MU. Interface -> 2 credits: Break 1 sentry or 2 code gate subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13018", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\u0394\u03b5\u03bd \u03c5\u03c0\u1f01\u03c1\u03c7\u03b5\u03b9 \u03c4\u03af\u03c0\u03bf\u03c4\u03b1 \u03bc\u03cc\u03bd\u03b9\u03bc\u03bf, \u03b5\u03ba\u03c4\u03cc\u03c2 \u03b1\u03c0\u03cc \u03c4\u03b7\u03bd \u03b1\u03bb\u03bb\u03b1\u03b3\u03ae.", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Killer - Decoder", "memory_cost": 2, "pack_code": "td", "position": 18, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "This program gets +1 strength for each unused MU. Interface -> 2 credits: Break 1 sentry or 2 code gate subroutines.", "stripped_title": "Savant", "text": "This program gets +1 strength for each unused MU.\nInterface \u2192 <strong>2[credit]:</strong> Break 1 <strong>sentry</strong> or 2 <strong>code gate</strong> subroutines.", "title": "Savant", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_egret_13019(Program):
    '''
    Cost: 2
    Text: Install only on a rezzed piece of ice. Host ice gains barrier, code gate, and sentry.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13019", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Trojan", "memory_cost": 1, "pack_code": "td", "position": 19, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a rezzed piece of ice. Host ice gains barrier, code gate, and sentry.", "stripped_title": "Egret", "text": "Install only on a rezzed piece of ice.\nHost ice gains <strong>barrier</strong>, <strong>code gate</strong>, and <strong>sentry</strong>.", "title": "Egret", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_dhegdheer_13020(Program):
    '''
    Cost: 2
    Text: You can install other programs onto this program. Each program installed this way costs 1 credit less to install. Limit 1 hosted program. The memory cost of the hosted program does not count against your memory limit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13020", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Liiga Smilshkalne", "keywords": "Daemon", "memory_cost": 0, "pack_code": "td", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "You can install other programs onto this program. Each program installed this way costs 1 credit less to install. Limit 1 hosted program. The memory cost of the hosted program does not count against your memory limit.", "stripped_title": "Dhegdheer", "text": "You can install other programs onto this program. Each program installed this way costs 1[credit] less to install. Limit 1 hosted program.\nThe memory cost of the hosted program does not count against your memory limit.", "title": "Dhegdheer", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_surveillance_network_key_14018(Program):
    '''
    Cost: 2
    Text: Whenever the Corp spends click to draw 1 or more cards (including through a card ability), reveal the first card drawn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14018", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Micha\u0142 Mi\u0142kowski", "memory_cost": 1, "pack_code": "tdc", "position": 19, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp spends click to draw 1 or more cards (including through a card ability), reveal the first card drawn.", "stripped_title": "Surveillance Network Key", "text": "Whenever the Corp spends [click] to draw 1 or more cards (including through a card ability), reveal the first card drawn.", "title": "Surveillance Network Key", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_surveillance_network_key_2_14019(Program):
    '''
    Cost: 2
    Text: Whenever the Corp spends click to draw 1 or more cards (including through a card ability), reveal the first card drawn. 2 credits: For the remainder of this run, access 1 additional card whenever you access cards from HQ or R&D. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14019", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Micha\u0142 Mi\u0142kowski", "memory_cost": 1, "pack_code": "tdc", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp spends click to draw 1 or more cards (including through a card ability), reveal the first card drawn. 2 credits: For the remainder of this run, access 1 additional card whenever you access cards from HQ or R&D. Use this ability only once per turn.", "stripped_title": "Surveillance Network Key 2", "text": "Whenever the Corp spends [click] to draw 1 or more cards (including through a card ability), reveal the first card drawn.\n2[credit]: For the remainder of this run, access 1 additional card whenever you access cards from HQ or R&D. Use this ability only once per turn.", "title": "Surveillance Network Key 2", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sneakdoor_prime_a_14026(Program):
    '''
    Cost: 6
    Text: click,click: Make a run on a remote server. If successful, instead treat it as a successful run on a central server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14026", "cost": 6, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Dmitry Prosvirnin", "memory_cost": 2, "pack_code": "tdc", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "click,click: Make a run on a remote server. If successful, instead treat it as a successful run on a central server.", "stripped_title": "Sneakdoor Prime A", "text": "[click],[click]: Make a run on a remote server. If successful, instead treat it as a successful run on a central server.", "title": "Sneakdoor Prime A", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sneakdoor_prime_b_14027(Program):
    '''
    Cost: 6
    Text: click,click: Make a run on a central server. If successful, instead treat it as a successful run on a remote server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14027", "cost": 6, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Dmitry Prosvirnin", "memory_cost": 2, "pack_code": "tdc", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "click,click: Make a run on a central server. If successful, instead treat it as a successful run on a remote server.", "stripped_title": "Sneakdoor Prime B", "text": "[click],[click]: Make a run on a central server. If successful, instead treat it as a successful run on a remote server.", "title": "Sneakdoor Prime B", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_darwin_20008(Program):
    '''
    Cost: 3
    Text: Interface -> 2 credits: Break 1 subroutine. X is equal to the number of hosted virus counters. When your turn begins, you may pay 1 credit to place 1 virus counter on this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20008", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - AI - Virus", "memory_cost": 1, "pack_code": "core2", "position": 8, "quantity": 2, "side_code": "runner", "strength": null, "stripped_text": "Interface -> 2 credits: Break 1 subroutine. X is equal to the number of hosted virus counters. When your turn begins, you may pay 1 credit to place 1 virus counter on this program.", "stripped_title": "Darwin", "text": "Interface \u2192 2[credit]: Break 1 subroutine.\nX is equal to the number of hosted virus counters.\nWhen your turn begins, you may pay 1[credit] to place 1 virus counter on this program.", "title": "Darwin", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_datasucker_20009(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run on a central server, place 1 virus counter on Datasucker. Hosted virus counter: Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20009", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Liiga Smilshkalne", "keywords": "Virus", "memory_cost": 1, "pack_code": "core2", "position": 9, "quantity": 2, "side_code": "runner", "stripped_text": "Whenever you make a successful run on a central server, place 1 virus counter on Datasucker. Hosted virus counter: Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.", "stripped_title": "Datasucker", "text": "Whenever you make a successful run on a central server, place 1 virus counter on Datasucker.\n<strong>Hosted virus counter:</strong> Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.", "title": "Datasucker", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_force_of_nature_20010(Program):
    '''
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20010", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "It always strikes twice.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "core2", "position": 10, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.", "stripped_title": "Force of Nature", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>code gate</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength.", "title": "Force of Nature", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_imp_20011(Program):
    '''
    Cost: 2
    Text: When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20011", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Something wicked this way comes.", "illustrator": "Wen Xiaodong", "keywords": "Virus", "memory_cost": 1, "pack_code": "core2", "position": 11, "quantity": 1, "side_code": "runner", "stripped_text": "When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.", "stripped_title": "Imp", "text": "When you install this program, place 2 virus counters on it.\nAccess \u2192 <strong>Hosted virus counter:</strong> Trash the card you are accessing. Use this ability only once per turn.", "title": "Imp", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_hemorrhage_20012(Program):
    '''
    Cost: 3
    Text: Whenever you make a successful run, place 1 virus counter on Hemorrhage. click, 2 hosted virus counters: The Corp trashes 1 card from HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20012", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "Bleeding data is more of a science than an art. Too much and you can end up with a one-way ticket to flatline city. Not enough and you might as well be running an empty server.", "illustrator": "Ed Mattinian", "keywords": "Virus", "memory_cost": 1, "pack_code": "core2", "position": 12, "quantity": 1, "side_code": "runner", "stripped_text": "Whenever you make a successful run, place 1 virus counter on Hemorrhage. click, 2 hosted virus counters: The Corp trashes 1 card from HQ.", "stripped_title": "Hemorrhage", "text": "Whenever you make a successful run, place 1 virus counter on Hemorrhage.\n[click], <strong>2 hosted virus counters:</strong> The Corp trashes 1 card from HQ.", "title": "Hemorrhage", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_mimic_20013(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20013", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "November 5th: the day when all would see the corrupt machinations of the corporate oligarchy.", "illustrator": "Matt Zeilinger", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "core2", "position": 13, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine.", "stripped_title": "Mimic", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.", "title": "Mimic", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_morning_star_20014(Program):
    '''
    Cost: 8
    Text: Interface -> 1 credit: Break any number of barrier subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20014", "cost": 8, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "Weaponizing the heavens, one star at a time.", "illustrator": "Robert Chew", "keywords": "Icebreaker - Fracter", "memory_cost": 2, "pack_code": "core2", "position": 14, "quantity": 3, "side_code": "runner", "strength": 5, "stripped_text": "Interface -> 1 credit: Break any number of barrier subroutines.", "stripped_title": "Morning Star", "text": "Interface \u2192 <strong>1[credit]:</strong> Break any number of <strong>barrier</strong> subroutines.", "title": "Morning Star", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_aurora_20027(Program):
    '''
    Cost: 3
    Text: Interface -> 2 credits: Break 1 barrier subroutine. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20027", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "core2", "position": 27, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break 1 barrier subroutine. 2 credits: +3 strength.", "stripped_title": "Aurora", "text": "Interface \u2192 <strong>2[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>2[credit]:</strong> +3 strength.", "title": "Aurora", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_faerie_20028(Program):
    '''
    Cost: 0
    Text: Interface -> 0 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20028", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Do you believe in faeries?", "illustrator": "Sara K. Diesel", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "core2", "position": 28, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 0 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.", "stripped_title": "Faerie", "text": "Interface \u2192 0[credit]: Break 1 <strong>sentry</strong> subroutine.\n1[credit]: +1 strength.\nWhenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.", "title": "Faerie", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_femme_fatale_20029(Program):
    '''
    Cost: 9
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20029", "cost": 9, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Anna Christenson", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "core2", "position": 29, "quantity": 2, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.", "stripped_title": "Femme Fatale", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +1 strength.\nWhen you install this program, choose 1 installed piece of ice.\nWhenever you encounter the chosen ice, you may pay 1[credit] for each subroutine it has. If you do, bypass that ice.", "title": "Femme Fatale", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_peacock_20030(Program):
    '''
    Cost: 3
    Text: Interface -> 2 credits: Break 1 code gate subroutine. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20030", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Show-off.", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "core2", "position": 30, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 2 credits: Break 1 code gate subroutine. 2 credits: +3 strength.", "stripped_title": "Peacock", "text": "Interface \u2192 <strong>2[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> +3 strength.", "title": "Peacock", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_pheromones_20031(Program):
    '''
    Cost: 2
    Text: X recurring credits Use these credits during runs on HQ. X is the number of virus counters on Pheromones. Whenever you make a successful run on HQ, place 1 virus counter on Pheromones.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20031", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Virus", "memory_cost": 1, "pack_code": "core2", "position": 31, "quantity": 1, "side_code": "runner", "stripped_text": "X recurring credits Use these credits during runs on HQ. X is the number of virus counters on Pheromones. Whenever you make a successful run on HQ, place 1 virus counter on Pheromones.", "stripped_title": "Pheromones", "text": "X[recurring-credit]\nUse these credits during runs on HQ. X is the number of virus counters on Pheromones.\nWhenever you make a successful run on HQ, place 1 virus counter on Pheromones.", "title": "Pheromones", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sneakdoor_beta_20032(Program):
    '''
    Cost: 4
    Text: click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20032", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"The code isn't important. It's where the code takes you that is important.\" -g00ru", "illustrator": "Andrew Mar", "memory_cost": 2, "pack_code": "core2", "position": 32, "quantity": 1, "side_code": "runner", "stripped_text": "click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.", "stripped_title": "Sneakdoor Beta", "text": "[click]<strong>:</strong> Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.", "title": "Sneakdoor Beta", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_battering_ram_20048(Program):
    '''
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 1 credit: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20048", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"It's called 'brute-forcing' and it's just as effective today as it was a hundred years ago.\" -Kate \"Mac\" McCaffrey", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Fracter", "memory_cost": 2, "pack_code": "core2", "position": 48, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 2 credits: Break up to 2 barrier subroutines. 1 credit: +1 strength for the remainder of this run.", "stripped_title": "Battering Ram", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength for the remainder of this run.", "title": "Battering Ram", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gordian_blade_20049(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20049", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "It can slice through the thickest knots of data.", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "core2", "position": 49, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.", "stripped_title": "Gordian Blade", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength for the remainder of this run.", "title": "Gordian Blade", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_magnum_opus_20050(Program):
    '''
    Cost: 5
    Text: click: Gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20050", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "The Great Work was completed on a rainy Thursday afternoon. There were no seismic shifts, no solar flares, no sign from the earth or heavens that the world had changed. But upstalk in Heinlein, on a single Cybsoft manufactured datacore, the flickering data quantums of an account began to fill with creds. Real, honest-to-goodness UN certified creds.", "illustrator": "Outland Entertainment LLC", "memory_cost": 2, "pack_code": "core2", "position": 50, "quantity": 2, "side_code": "runner", "stripped_text": "click: Gain 2 credits.", "stripped_title": "Magnum Opus", "text": "[click]: Gain 2[credit].", "title": "Magnum Opus", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_pipeline_20051(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20051", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "core2", "position": 51, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength for the remainder of this run.", "stripped_title": "Pipeline", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +1 strength for the remainder of this run.", "title": "Pipeline", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_crypsis_20058(Program):
    '''
    Cost: 5
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. click: Place 1 virus counter on this program. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20058", "cost": 5, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI - Virus", "memory_cost": 1, "pack_code": "core2", "position": 58, "quantity": 2, "side_code": "runner", "strength": 0, "stripped_text": "Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. click: Place 1 virus counter on this program. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.", "stripped_title": "Crypsis", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine.\n<strong>1[credit]:</strong> +1 strength.\n<strong>[click]:</strong> Place 1 virus counter on this program.\nWhenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.", "title": "Crypsis", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_yusuf_21002(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run, you may place 1 virus counter on this program. Interface -> Any virus counter: Break 1 barrier subroutine. Any virus counter: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21002", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Alexandr Elichev", "keywords": "Icebreaker - Fracter - Virus", "memory_cost": 2, "pack_code": "ss", "position": 2, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Whenever you make a successful run, you may place 1 virus counter on this program. Interface -> Any virus counter: Break 1 barrier subroutine. Any virus counter: +1 strength.", "stripped_title": "Yusuf", "text": "Whenever you make a successful run, you may place 1 virus counter on this program.\nInterface \u2192 <strong>Any virus counter:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>Any virus counter:</strong> +1 strength.", "title": "Yusuf", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_puffer_21004(Program):
    '''
    Cost: 4
    Text: This program gets +1 strength and costs +1 mu for each hosted power counter. Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. click: Place 1 power counter on this program or remove 1 hosted power counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21004", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "ss", "position": 4, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "This program gets +1 strength and costs +1 mu for each hosted power counter. Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. click: Place 1 power counter on this program or remove 1 hosted power counter.", "stripped_title": "Puffer", "text": "This program gets +1 strength and costs +1[mu] for each hosted power counter.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +1 strength.\n<strong>[click]:</strong> Place 1 power counter on this program or remove 1 hosted power counter.", "title": "Puffer", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_upya_21007(Program):
    '''
    Cost: 0
    Text: Whenever you make a successful run on R&D, you may place 1 power counter on Upya. click, 3 hosted power counters: Gain click click. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21007", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "New life through new understanding.", "illustrator": "Galen Dara", "memory_cost": 1, "pack_code": "ss", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on R&D, you may place 1 power counter on Upya. click, 3 hosted power counters: Gain click click. Use this ability only once per turn.", "stripped_title": "Upya", "text": "Whenever you make a successful run on R&D, you may place 1 power counter on Upya.\n<strong>[click], 3 hosted power counters</strong>: Gain [click][click]. Use this ability only once per turn.", "title": "Upya", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_plague_21022(Program):
    '''
    Cost: 2
    Text: When you install Plague, choose a server. Whenever you make a successful run on the chosen server, you may place 2 virus counters on Plague.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21022", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Embedded in the mainframe, it proliferates and devours with each agitation.", "illustrator": "Ethan Patrick Harris", "keywords": "Virus", "memory_cost": 1, "pack_code": "dtwn", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "When you install Plague, choose a server. Whenever you make a successful run on the chosen server, you may place 2 virus counters on Plague.", "stripped_title": "Plague", "text": "When you install Plague, choose a server.\nWhenever you make a successful run on the chosen server, you may place 2 virus counters on Plague.", "title": "Plague", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_wari_21024(Program):
    '''
    Cost: 1
    Text: The first time you make a successful run on HQ each turn, you may trash Wari to name sentry, code gate or barrier. Expose a piece of ice, then add it to HQ if it has the named subtype.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21024", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "flavor": "\"He's probably the best pet I've ever had but I'd still trade him for something better.\" - 419", "illustrator": "Adam S. Doyle", "memory_cost": 1, "pack_code": "dtwn", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you make a successful run on HQ each turn, you may trash Wari to name sentry, code gate or barrier. Expose a piece of ice, then add it to HQ if it has the named subtype.", "stripped_title": "Wari", "text": "The first time you make a successful run on HQ each turn, you may trash Wari to name <strong>sentry</strong>, <strong>code gate</strong> or <strong>barrier</strong>. Expose a piece of ice, then add it to HQ if it has the named subtype.", "title": "Wari", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_takobi_21026(Program):
    '''
    Cost: 2
    Text: Whenever you fully break a piece of ice, you may place 1 power counter on this program. 2 hosted power counters: Choose 1 installed non-AI icebreaker. That icebreaker gets +3 strength for the remainder of the current encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21026", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "When standard breaking just doesn't cut it.", "illustrator": "Andreas Zafiratos", "memory_cost": 1, "pack_code": "dtwn", "position": 26, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you fully break a piece of ice, you may place 1 power counter on this program. 2 hosted power counters: Choose 1 installed non-AI icebreaker. That icebreaker gets +3 strength for the remainder of the current encounter.", "stripped_title": "Takobi", "text": "Whenever you fully break a piece of ice, you may place 1 power counter on this program.\n<strong>2 hosted power counters:</strong> Choose 1 installed non-<strong>AI</strong> <strong>icebreaker</strong>. That <strong>icebreaker</strong> gets +3 strength for the remainder of the current encounter.", "title": "Takobi", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_rng_key_21029(Program):
    '''
    Cost: 0
    Text: The first time you make a successful run on HQ or R&D each turn, you may name a number. If you do, reveal the next card that you access this run. If it has a rez cost, play cost, or advancement requirement equal to the named number, either gain 3 credits or draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21029", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Between nothing and infinity.", "illustrator": "Andreas Zafiratos", "memory_cost": 1, "pack_code": "dtwn", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you make a successful run on HQ or R&D each turn, you may name a number. If you do, reveal the next card that you access this run. If it has a rez cost, play cost, or advancement requirement equal to the named number, either gain 3 credits or draw 2 cards.", "stripped_title": "RNG Key", "text": "The first time you make a successful run on HQ or R&D each turn, you may name a number. If you do, reveal the next card that you access this run. If it has a rez cost, play cost, or advancement requirement equal to the named number, either gain 3[credit] or draw 2 cards.", "title": "RNG Key", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_exer_21041(Program):
    '''
    Cost: 2
    Text: Whenever you breach R&D, access 1 additional card. When the Corp purges virus counters, trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21041", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"Amateurs feign it as 'random packet loss'. They do this for safety. They do this out of fear. But why should we cower? <em>We</em> will collapse the Corporatocracy, piece by piece! They are not the ones to fear. <em>We</em> are.\"\n- Freedom Khumalo", "illustrator": "Ed Mattinian", "keywords": "Virus", "memory_cost": 1, "pack_code": "cotc", "position": 41, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you breach R&D, access 1 additional card. When the Corp purges virus counters, trash this program.", "stripped_title": "eXer", "text": "Whenever you breach R&D, access 1 additional card.\nWhen the Corp purges virus counters, trash this program.", "title": "eXer", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_nyashia_21067(Program):
    '''
    Cost: 2
    Text: When you install this program, place 3 power counters on it. Whenever you breach R&D, you may remove 1 hosted power counter to access 1 additional card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21067", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Speed gets you in, intuition gets you out.", "illustrator": "Liiga Smilshkalne", "memory_cost": 1, "pack_code": "tdatd", "position": 67, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this program, place 3 power counters on it. Whenever you breach R&D, you may remove 1 hosted power counter to access 1 additional card.", "stripped_title": "Nyashia", "text": "When you install this program, place 3 power counters on it.\nWhenever you breach R&D, you may remove 1 hosted power counter to access 1 additional card.", "title": "Nyashia", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_consume_21068(Program):
    '''
    Cost: 2
    Text: Whenever you trash a Corp card, you may place 1 virus counter on Consume. click: Gain 2 credits for each hosted virus counter, then remove all virus counters from Consume.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21068", "cost": 2, "deck_limit": 3, "faction_code": "apex", "faction_cost": 5, "flavor": "\"It 'ate' the vertex grid?! What does that even mean?\"\n- Nkiru Qi\u016b, Asa Group sysop", "illustrator": "Pavel Kolomeyets", "keywords": "Virus", "memory_cost": 0, "pack_code": "tdatd", "position": 68, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you trash a Corp card, you may place 1 virus counter on Consume. click: Gain 2 credits for each hosted virus counter, then remove all virus counters from Consume.", "stripped_title": "Consume", "text": "Whenever you trash a Corp card, you may place 1 virus counter on Consume.\n[click]: Gain 2[credit] for each hosted virus counter, then remove all virus counters from Consume.", "title": "Consume", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_trypano_21082(Program):
    '''
    Cost: 2
    Text: Install only on a piece of ice. When your turn begins, you may place 1 virus counter on this program. When there are 5 or more hosted virus counters, trash host ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21082", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Twisting, writhing, ripping into all that it touches.", "illustrator": "Ethan Patrick Harris", "keywords": "Virus - Trojan", "memory_cost": 1, "pack_code": "win", "position": 82, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a piece of ice. When your turn begins, you may place 1 virus counter on this program. When there are 5 or more hosted virus counters, trash host ice.", "stripped_title": "Trypano", "text": "Install only on a piece of ice.\nWhen your turn begins, you may place 1 virus counter on this program.\nWhen there are 5 or more hosted virus counters, trash host ice.", "title": "Trypano", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_laamb_21086(Program):
    '''
    Cost: 4
    Text: Whenever you encounter a piece of ice, you may pay 2 credits. If you do, it gains barrier for the remainder of that encounter. Use this ability only once per turn. Interface -> 2 credits: Break any number of barrier subroutines. 3 credits: +6 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21086", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - Fracter", "memory_cost": 2, "pack_code": "win", "position": 86, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Whenever you encounter a piece of ice, you may pay 2 credits. If you do, it gains barrier for the remainder of that encounter. Use this ability only once per turn. Interface -> 2 credits: Break any number of barrier subroutines. 3 credits: +6 strength.", "stripped_title": "Laamb", "text": "Whenever you encounter a piece of ice, you may pay 2[credit]. If you do, it gains <strong>barrier</strong> for the remainder of that encounter. Use this ability only once per turn.\nInterface \u2192 <strong>2[credit]:</strong> Break any number of <strong>barrier</strong> subroutines.\n<strong>3[credit]:</strong> +6 strength.", "title": "Laamb", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_musaazi_21102(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run, you may place 1 virus counter on this program. Interface -> Any virus counter: Break sentry subroutine. Any virus counter: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21102", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Killer - Virus", "memory_cost": 2, "pack_code": "ka", "position": 102, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Whenever you make a successful run, you may place 1 virus counter on this program. Interface -> Any virus counter: Break sentry subroutine. Any virus counter: +1 strength.", "stripped_title": "Musaazi", "text": "Whenever you make a successful run, you may place 1 virus counter on this program.\nInterface \u2192 <strong>Any virus counter:</strong> Break <strong>sentry</strong> subroutine.\n<strong>Any virus counter:</strong> +1 strength.", "title": "Musaazi", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_amina_21104(Program):
    '''
    Cost: 7
    Text: Interface -> 2 credits: Break up to 3 code gate subroutines. 2 credits: +3 strength. The first time each turn this program fully breaks a piece of ice, the Corp loses 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21104", "cost": 7, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "flavor": "Her gallop, thunder; her blade, lightning.", "illustrator": "Ethan Patrick Harris", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "ka", "position": 104, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 2 credits: Break up to 3 code gate subroutines. 2 credits: +3 strength. The first time each turn this program fully breaks a piece of ice, the Corp loses 1 credit.", "stripped_title": "Amina", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 3 <strong>code gate</strong> subroutines.\n<strong>2[credit]:</strong> +3 strength.\nThe first time each turn this program fully breaks a piece of ice, the Corp loses 1[credit].", "title": "Amina", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_engolo_21108(Program):
    '''
    Cost: 5
    Text: Whenever you encounter a piece of ice, you may pay 2 credits. If you do, it gains code gate for the remainder of that encounter. Use this ability only once per turn. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +4 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21108", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - Decoder", "memory_cost": 2, "pack_code": "ka", "position": 108, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Whenever you encounter a piece of ice, you may pay 2 credits. If you do, it gains code gate for the remainder of that encounter. Use this ability only once per turn. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +4 strength.", "stripped_title": "Engolo", "text": "Whenever you encounter a piece of ice, you may pay 2[credit]. If you do, it gains <strong>code gate</strong> for the remainder of that encounter. Use this ability only once per turn.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> +4 strength.", "title": "Engolo", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cradle_22006(Program):
    '''
    Cost: 4
    Text: This program gets -1 strength for each card in your grip. Interface -> 2 credits: Break any number of code gate subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22006", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "... clack... clack... clack...", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "rar", "position": 6, "quantity": 3, "side_code": "runner", "strength": 5, "stripped_text": "This program gets -1 strength for each card in your grip. Interface -> 2 credits: Break any number of code gate subroutines.", "stripped_title": "Cradle", "text": "This program gets -1 strength for each card in your grip.\nInterface \u2192 <strong>2[credit]:</strong> Break any number of <strong>code gate</strong> subroutines.", "title": "Cradle", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_bankroll_22011(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run, you may place 1 credit from the bank on Bankroll. trash: Take all credits from Bankroll.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22011", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"With the rise of crypto, banking has become much more complicated. Financial crime has not only kept pace, but exploded exponentially.\"\n-After the Flash: A History of the War-That-Wasn't", "illustrator": "Andreas Zafiratos", "memory_cost": 1, "pack_code": "rar", "position": 11, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run, you may place 1 credit from the bank on Bankroll. trash: Take all credits from Bankroll.", "stripped_title": "Bankroll", "text": "Whenever you make a successful run, you may place 1[credit] from the bank on Bankroll.\n[trash]: Take all credits from Bankroll.", "title": "Bankroll", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_tycoon_22012(Program):
    '''
    Cost: 1
    Text: Interface -> 1 credit: Break up to 2 barrier subroutines. 2 credits: +3 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, the Corp gains 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22012", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Any piece of ice is really just a paywall.\"\n-Liza Talking Thunder", "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "rar", "position": 12, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break up to 2 barrier subroutines. 2 credits: +3 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, the Corp gains 2 credits.", "stripped_title": "Tycoon", "text": "Interface \u2192 <strong>1[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>2[credit]:</strong> +3 strength.\nWhenever an encounter ends, if you used this program to break a subroutine during that encounter, the Corp gains 2[credit].", "title": "Tycoon", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_ika_22019(Program):
    '''
    Cost: 0
    Text: 2 credits: Host this program on a piece of ice. Interface -> 1 credit: Break up to 2 subroutines on host sentry. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22019", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Running is all metaphor, all symbols and plumbing into the depths of the psyche. Sometimes that means tentacles.\" -Akiko Nisei", "illustrator": "Andreas Zafiratos", "keywords": "Icebreaker - Killer - Trojan", "memory_cost": 1, "pack_code": "rar", "position": 19, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "2 credits: Host this program on a piece of ice. Interface -> 1 credit: Break up to 2 subroutines on host sentry. 2 credits: +3 strength.", "stripped_title": "Ika", "text": "<strong>2[credit]:</strong> Host this program on a piece of ice.\nInterface \u2192 <strong>1[credit]:</strong> Break up to 2 subroutines on host <strong>sentry</strong>.\n<strong>2[credit]:</strong> +3 strength.", "title": "Ika", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_kyuban_22020(Program):
    '''
    Cost: 0
    Text: Install only on a piece of ice. Whenever you pass host ice, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22020", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "The journey is its own reward.", "illustrator": "Marius Siergiejew", "keywords": "Trojan", "memory_cost": 1, "pack_code": "rar", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a piece of ice. Whenever you pass host ice, gain 2 credits.", "stripped_title": "Kyuban", "text": "Install only on a piece of ice.\nWhenever you pass host ice, gain 2[credit].", "title": "Kyuban", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_algernon_22022(Program):
    '''
    Cost: 0
    Text: When your turn begins, you may pay 2 credits to gain click. If you do, trash Algernon when your turn ends if you did not make a successful run this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22022", "cost": 0, "deck_limit": 3, "faction_code": "adam", "faction_cost": 5, "flavor": "\"When we're together, I feel like I can do anything!\"", "illustrator": "Lili Ibrahim", "memory_cost": 1, "pack_code": "rar", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may pay 2 credits to gain click. If you do, trash Algernon when your turn ends if you did not make a successful run this turn.", "stripped_title": "Algernon", "text": "When your turn begins, you may pay 2[credit] to gain [click]. If you do, trash Algernon when your turn ends if you did not make a successful run this turn.", "title": "Algernon", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_corroder_25010(Program):
    '''
    Cost: 2
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25010", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"If at first you don't succeed, boost its strength and try again.\" -g00ru", "illustrator": "Mike Nesbitt", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "sc19", "position": 10, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength.", "stripped_title": "Corroder", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Corroder", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_datasucker_25011(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run on a central server, place 1 virus counter on Datasucker. Hosted virus counter: Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25011", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Liiga Smilshkalne", "keywords": "Virus", "memory_cost": 1, "pack_code": "sc19", "position": 11, "quantity": 2, "side_code": "runner", "stripped_text": "Whenever you make a successful run on a central server, place 1 virus counter on Datasucker. Hosted virus counter: Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.", "stripped_title": "Datasucker", "text": "Whenever you make a successful run on a central server, place 1 virus counter on Datasucker.\n<strong>Hosted virus counter:</strong> Rezzed piece of ice currently being encountered has -1 strength until the end of the encounter.", "title": "Datasucker", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_force_of_nature_25012(Program):
    '''
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25012", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "It always strikes twice.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "sc19", "position": 12, "quantity": 2, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.", "stripped_title": "Force of Nature", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>code gate</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength.", "title": "Force of Nature", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_imp_25013(Program):
    '''
    Cost: 2
    Text: When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25013", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Something wicked this way comes.", "illustrator": "Wen Xiaodong", "keywords": "Virus", "memory_cost": 1, "pack_code": "sc19", "position": 13, "quantity": 2, "side_code": "runner", "stripped_text": "When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.", "stripped_title": "Imp", "text": "When you install this program, place 2 virus counters on it.\nAccess \u2192 <strong>Hosted virus counter:</strong> Trash the card you are accessing. Use this ability only once per turn.", "title": "Imp", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_lamprey_25014(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run on HQ, the Corp loses 1 credit. Trash Lamprey if the Corp purges virus counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25014", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Smirtouille", "keywords": "Virus", "memory_cost": 1, "pack_code": "sc19", "position": 14, "quantity": 2, "side_code": "runner", "stripped_text": "Whenever you make a successful run on HQ, the Corp loses 1 credit. Trash Lamprey if the Corp purges virus counters.", "stripped_title": "Lamprey", "text": "Whenever you make a successful run on HQ, the Corp loses 1[credit].\nTrash Lamprey if the Corp purges virus counters.", "title": "Lamprey", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_mimic_25015(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25015", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "November 5th: the day when all would see the corrupt machinations of the corporate oligarchy.", "illustrator": "Matt Zeilinger", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "sc19", "position": 15, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine.", "stripped_title": "Mimic", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.", "title": "Mimic", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_abagnale_25033(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. trash: Bypass the code gate you are encountering.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25033", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Technology breeds crime.\"", "illustrator": "BalanceSheet", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "sc19", "position": 33, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. trash: Bypass the code gate you are encountering.", "stripped_title": "Abagnale", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> +2 strength.\n[trash]<strong>:</strong> Bypass the <strong>code gate</strong> you are encountering.", "title": "Abagnale", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_demara_25034(Program):
    '''
    Cost: 4
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 2 credits: +3 strength. trash: Bypass the barrier you are encountering.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25034", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"It's a matter of 'acquiring' the right credentials.\"", "illustrator": "Mariusz Siergiejew", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "sc19", "position": 34, "quantity": 2, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break up to 2 barrier subroutines. 2 credits: +3 strength. trash: Bypass the barrier you are encountering.", "stripped_title": "Demara", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>2[credit]:</strong> +3 strength.\n<strong>[trash]:</strong> Bypass the <strong>barrier</strong> you are encountering.", "title": "Demara", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_faerie_25035(Program):
    '''
    Cost: 0
    Text: Interface -> 0 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25035", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Do you believe in faeries?", "illustrator": "Sara K. Diesel", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "sc19", "position": 35, "quantity": 2, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 0 credits: Break 1 sentry subroutine. 1 credit: +1 strength. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.", "stripped_title": "Faerie", "text": "Interface \u2192 0[credit]: Break 1 <strong>sentry</strong> subroutine.\n1[credit]: +1 strength.\nWhenever an encounter ends, if you used this program to break a subroutine during that encounter, trash this program.", "title": "Faerie", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_femme_fatale_25036(Program):
    '''
    Cost: 9
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25036", "cost": 9, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Anna Christenson", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "sc19", "position": 36, "quantity": 2, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.", "stripped_title": "Femme Fatale", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +1 strength.\nWhen you install this program, choose 1 installed piece of ice.\nWhenever you encounter the chosen ice, you may pay 1[credit] for each subroutine it has. If you do, bypass that ice.", "title": "Femme Fatale", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sneakdoor_beta_25037(Program):
    '''
    Cost: 4
    Text: click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25037", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"The code isn't important. It's where the code takes you that is important.\" -g00ru", "illustrator": "Andrew Mar", "memory_cost": 2, "pack_code": "sc19", "position": 37, "quantity": 2, "side_code": "runner", "stripped_text": "click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.", "stripped_title": "Sneakdoor Beta", "text": "[click]<strong>:</strong> Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.", "title": "Sneakdoor Beta", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_atman_25051(Program):
    '''
    Cost: 3
    Text: When you install this program, you may pay X credits to place X power counters on it. This program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength. Interface -> 1 credit: Break 1 subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25051", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "We are shaped by our thoughts; we become what we think.", "illustrator": "Diana Martinez", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "sc19", "position": 51, "quantity": 1, "side_code": "runner", "strength": 0, "stripped_text": "When you install this program, you may pay X credits to place X power counters on it. This program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength. Interface -> 1 credit: Break 1 subroutine.", "stripped_title": "Atman", "text": "When you install this program, you may pay X[credit] to place X power counters on it.\nThis program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 subroutine.", "title": "Atman", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_battering_ram_25052(Program):
    '''
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 1 credit: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25052", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"It's called 'brute-forcing' and it's just as effective today as it was a hundred years ago.\" -Kate \"Mac\" McCaffrey", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Fracter", "memory_cost": 2, "pack_code": "sc19", "position": 52, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 2 credits: Break up to 2 barrier subroutines. 1 credit: +1 strength for the remainder of this run.", "stripped_title": "Battering Ram", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength for the remainder of this run.", "title": "Battering Ram", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_deus_x_25053(Program):
    '''
    Cost: 3
    Text: Interface -> trash: Break any number of AP subroutines. Interrupt -> trash: Prevent any amount of net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25053", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Didn't see that coming.", "illustrator": "Andrew Mar", "keywords": "Icebreaker", "memory_cost": 1, "pack_code": "sc19", "position": 53, "quantity": 1, "side_code": "runner", "strength": 10, "stripped_text": "Interface -> trash: Break any number of AP subroutines. Interrupt -> trash: Prevent any amount of net damage.", "stripped_title": "Deus X", "text": "Interface \u2192 <strong>[trash]:</strong> Break any number of <strong>AP</strong> subroutines.\n[interrupt] \u2192 <strong>[trash]:</strong> Prevent any amount of net damage.", "title": "Deus X", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gordian_blade_25054(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25054", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "It can slice through the thickest knots of data.", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "sc19", "position": 54, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.", "stripped_title": "Gordian Blade", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength for the remainder of this run.", "title": "Gordian Blade", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_pipeline_25055(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25055", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "illustrator": "Ed Mattinian", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "sc19", "position": 55, "quantity": 2, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength for the remainder of this run.", "stripped_title": "Pipeline", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +1 strength for the remainder of this run.", "title": "Pipeline", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_crypsis_25061(Program):
    '''
    Cost: 5
    Text: Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. click: Place 1 virus counter on this program. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25061", "cost": 5, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI - Virus", "memory_cost": 1, "pack_code": "sc19", "position": 61, "quantity": 2, "side_code": "runner", "strength": 0, "stripped_text": "Interface -> 1 credit: Break 1 subroutine. 1 credit: +1 strength. click: Place 1 virus counter on this program. Whenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.", "stripped_title": "Crypsis", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine.\n<strong>1[credit]:</strong> +1 strength.\n<strong>[click]:</strong> Place 1 virus counter on this program.\nWhenever an encounter ends, if you used this program to break a subroutine during that encounter, remove 1 hosted virus counter or trash this program.", "title": "Crypsis", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_chisel_26003(Program):
    '''
    Cost: 2
    Text: Install only on a piece of ice. Host ice gets -1 strength for each hosted virus counter. When you encounter host ice, if its strength is 0 or less, trash it. Otherwise, place 1 virus counter on this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26003", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "*tap* *tap* *tap*", "illustrator": "Krembler", "keywords": "Virus - Trojan", "memory_cost": 1, "pack_code": "df", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a piece of ice. Host ice gets -1 strength for each hosted virus counter. When you encounter host ice, if its strength is 0 or less, trash it. Otherwise, place 1 virus counter on this program.", "stripped_title": "Chisel", "text": "Install only on a piece of ice.\nHost ice gets -1 strength for each hosted virus counter.\nWhen you encounter host ice, if its strength is 0 or less, trash it. Otherwise, place 1 virus counter on this program.", "title": "Chisel", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_stargate_26004(Program):
    '''
    Cost: 4
    Text: click: Run R&D. If successful, instead of breaching R&D, reveal the top 3 cards of R&D. Trash 1 of the revealed cards. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26004", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"Net <em>space</em> is an abstraction, a white lie protecting fragile comprehensions. Do not limit yourself.\" -z\\h/r", "illustrator": "Iain Fairclough", "memory_cost": 2, "pack_code": "df", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "click: Run R&D. If successful, instead of breaching R&D, reveal the top 3 cards of R&D. Trash 1 of the revealed cards. Use this ability only once per turn.", "stripped_title": "Stargate", "text": "<strong>[click]:</strong> Run R&D. If successful, instead of breaching R&D, reveal the top 3 cards of R&D. Trash 1 of the revealed cards. Use this ability only once per turn.", "title": "Stargate", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_utae_26005(Program):
    '''
    Cost: 2
    Text: Interface -> X credits: Break X code gate subroutines. Use this ability only once per run. Interface -> 1 credit: Break 1 code gate subroutine. Use this ability only if you have 3 or more installed virtual resources. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26005", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Sing, sing as your heart desires!", "illustrator": "McGregor T. Crowley", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "df", "position": 5, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> X credits: Break X code gate subroutines. Use this ability only once per run. Interface -> 1 credit: Break 1 code gate subroutine. Use this ability only if you have 3 or more installed virtual resources. 1 credit: +1 strength.", "stripped_title": "Utae", "text": "Interface \u2192 <strong>X[credit]:</strong> Break X <strong>code gate</strong> subroutines. Use this ability only once per run.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine. Use this ability only if you have 3 or more installed <strong>virtual</strong> resources.\n<strong>1[credit]:</strong> +1 strength.", "title": "Utae", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_bukhgalter_26016(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 1 credit: +1 strength. The first time each turn this program fully breaks a piece of ice, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26016", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "flavor": "\"Do the job. Get paid. Leave feelings at the door.\" -\"Baklan\" Bochkin", "illustrator": "Iain Fairclough", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "df", "position": 16, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 1 credit: +1 strength. The first time each turn this program fully breaks a piece of ice, gain 2 credits.", "stripped_title": "Bukhgalter", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.\nThe first time each turn this program fully breaks a piece of ice, gain 2[credit].", "title": "Bukhgalter", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gauss_26024(Program):
    '''
    Cost: 2
    Text: When you install this program, it gets +3 strength for the remainder of the turn. Interface -> 1 credit: Break 1 barrier subroutine. 2 credits: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26024", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "It is not knowledge, but the act of learning, not possession, but the act of getting there, which grants the greatest enjoyment.", "illustrator": "Iain Fairclough", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "df", "position": 24, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "When you install this program, it gets +3 strength for the remainder of the turn. Interface -> 1 credit: Break 1 barrier subroutine. 2 credits: +2 strength.", "stripped_title": "Gauss", "text": "When you install this program, it gets +3 strength for the remainder of the turn.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>2[credit]:</strong> +2 strength.", "title": "Gauss", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_pelangi_26025(Program):
    '''
    Cost: 1
    Text: When you install this program, place 2 virus counters on it. Hosted virus counter: Choose an ice subtype. The ice you are encountering gains that subtype for the remainder of the encounter. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26025", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "It makes sysops see red. And orange, yellow, green...", "illustrator": "Iain Fairclough", "keywords": "Virus", "memory_cost": 1, "pack_code": "df", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this program, place 2 virus counters on it. Hosted virus counter: Choose an ice subtype. The ice you are encountering gains that subtype for the remainder of the encounter. Use this ability only once per turn.", "stripped_title": "Pelangi", "text": "When you install this program, place 2 virus counters on it.\n<strong>Hosted virus counter:</strong> Choose an ice subtype. The ice you are encountering gains that subtype for the remainder of the encounter. Use this ability only once per turn.", "title": "Pelangi", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_rezeki_26026(Program):
    '''
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26026", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"It takes such simple things to sustain us, the most important of which is to be thankful.\" -Lat", "illustrator": "Jakuza", "memory_cost": 1, "pack_code": "df", "position": 26, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, gain 1 credit.", "stripped_title": "Rezeki", "text": "When your turn begins, gain 1[credit].", "title": "Rezeki", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_odore_26071(Program):
    '''
    Cost: 4
    Text: Interface -> 2 credits: Break any number of sentry subroutines. Interface -> 0 credits: Break 1 sentry subroutine. Use this ability only if you have 3 or more installed virtual resources. 3 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26071", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Dance, and forget about time!", "illustrator": "Krembler", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "ur", "position": 71, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "Interface -> 2 credits: Break any number of sentry subroutines. Interface -> 0 credits: Break 1 sentry subroutine. Use this ability only if you have 3 or more installed virtual resources. 3 credits: +3 strength.", "stripped_title": "Odore", "text": "Interface \u2192 <strong>2[credit]:</strong> Break any number of <strong>sentry</strong> subroutines.\nInterface \u2192 <strong>0[credit]:</strong> Break 1 <strong>sentry</strong> subroutine. Use this ability only if you have 3 or more installed <strong>virtual</strong> resources.\n<strong>3[credit]:</strong> +3 strength.", "title": "Odore", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_afterimage_26079(Program):
    '''
    Cost: 4
    Text: Whenever you encounter a sentry, you may pay 2 credits to bypass it. Use this ability only once per turn and only by spending credits from stealth cards. Interface -> 1 credit: Break up to 2 sentry subroutines. 1 credit: +2 strength. Use this ability only by spending a credit from a stealth card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26079", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "illustrator": "Kevin Tame", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "ur", "position": 79, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Whenever you encounter a sentry, you may pay 2 credits to bypass it. Use this ability only once per turn and only by spending credits from stealth cards. Interface -> 1 credit: Break up to 2 sentry subroutines. 1 credit: +2 strength. Use this ability only by spending a credit from a stealth card.", "stripped_title": "Afterimage", "text": "Whenever you encounter a <strong>sentry</strong>, you may pay 2[credit] to bypass it. Use this ability only once per turn and only by spending credits from <strong>stealth</strong> cards.\nInterface \u2192 <strong>1[credit]:</strong> Break up to 2 <strong>sentry</strong> subroutines.\n<strong>1[credit]:</strong> +2 strength. Use this ability only by spending a credit from a <strong>stealth</strong> card.", "title": "Afterimage", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_makler_26080(Program):
    '''
    Cost: 5
    Text: Interface -> 2 credits: Break up to 2 barrier subroutines. 2 credits: +2 strength. The first time each turn this program fully breaks a piece of ice, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26080", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Debt is beautiful... <em>after</em> it is repaid.\"\n-\"Baklan\" Bochkin", "illustrator": "Krembler", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "ur", "position": 80, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 2 credits: Break up to 2 barrier subroutines. 2 credits: +2 strength. The first time each turn this program fully breaks a piece of ice, gain 1 credit.", "stripped_title": "Makler", "text": "Interface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>2[credit]:</strong> +2 strength.\nThe first time each turn this program fully breaks a piece of ice, gain 1[credit].", "title": "Makler", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cordyceps_26086(Program):
    '''
    Cost: 3
    Text: When you install this program, place 2 virus counters on it. Whenever you make a successful run on a central server, you may remove 1 hosted virus counter to swap a piece of ice protecting that server with another installed piece of ice. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26086", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "illustrator": "Krembler, Zoe Cohen", "keywords": "Virus", "memory_cost": 1, "pack_code": "ur", "position": 86, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this program, place 2 virus counters on it. Whenever you make a successful run on a central server, you may remove 1 hosted virus counter to swap a piece of ice protecting that server with another installed piece of ice. Use this ability only once per turn.", "stripped_title": "Cordyceps", "text": "When you install this program, place 2 virus counters on it.\nWhenever you make a successful run on a central server, you may remove 1 hosted virus counter to swap a piece of ice protecting that server with another installed piece of ice. Use this ability only once per turn.", "title": "Cordyceps", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_euler_26087(Program):
    '''
    Cost: 2
    Text: When you install this program, for the remainder of the turn it gains "Interface -> 0 credits: Break 1 code gate subroutine." Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26087", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Find truth not in the observation, but in the demonstration.", "illustrator": "Patrick Burk", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "ur", "position": 87, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "When you install this program, for the remainder of the turn it gains \"Interface -> 0 credits: Break 1 code gate subroutine.\" Interface -> 2 credits: Break up to 2 code gate subroutines. 1 credit: +1 strength.", "stripped_title": "Euler", "text": "When you install this program, for the remainder of the turn it gains \"Interface \u2192 <strong>0[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\"\nInterface \u2192 <strong>2[credit]:</strong> Break up to 2 <strong>code gate</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength.", "title": "Euler", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_mantle_26088(Program):
    '''
    Cost: 1
    Text: 1 recurring credit Spend hosted credits to use hardware and programs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26088", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Invisibility made it possible to get them, but it made it impossible to enjoy them when they are got.\"\n-H.G. Wells, <em>The Invisible Man</em>", "illustrator": "Krembler", "keywords": "Stealth", "memory_cost": 1, "pack_code": "ur", "position": 88, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Spend hosted credits to use hardware and programs.", "stripped_title": "Mantle", "text": "1[recurring-credit]\nSpend hosted credits to use hardware and programs.", "title": "Mantle", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_penrose_26089(Program):
    '''
    Cost: 3
    Text: When you install this program, for the remainder of the turn it gains "Interface -> 1 credit: Break 1 barrier subroutine." Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +3 strength. Use this ability only by spending a credit from a stealth card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26089", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Look at the problem from a different angle.", "illustrator": "Kevin Tame", "keywords": "Icebreaker - Decoder - Fracter", "memory_cost": 1, "pack_code": "ur", "position": 89, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "When you install this program, for the remainder of the turn it gains \"Interface -> 1 credit: Break 1 barrier subroutine.\" Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +3 strength. Use this ability only by spending a credit from a stealth card.", "stripped_title": "Penrose", "text": "When you install this program, for the remainder of the turn it gains \"Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\"\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +3 strength. Use this ability only by spending a credit from a <strong>stealth</strong> card.", "title": "Penrose", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_selfmodifying_code_26090(Program):
    '''
    Cost: 0
    Text: 2 credits, trash: Search your stack for a program. Install it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26090", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Consider this: the most notorious tool in cyberterrorism is one that, in isolation, does <em>nothing.</em>", "illustrator": "Chiara Biancheri", "memory_cost": 2, "pack_code": "ur", "position": 90, "quantity": 3, "side_code": "runner", "stripped_text": "2 credits, trash: Search your stack for a program. Install it.", "stripped_title": "Self-modifying Code", "text": "<strong>2[credit]</strong>, [trash]<strong>:</strong> Search your stack for a program. Install it.", "title": "Self-modifying Code", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_medium_29001(Program):
    '''
    Cost: 3
    Text: Whenever you make a successful run on R&D, place 1 virus counter on this program. Whenever you breach R&D, choose a number less than the number of hosted virus counters. Access that many additional cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29001", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "It looked like random packet loss. It wasn't.", "illustrator": "Adam S. Doyle", "keywords": "Virus", "memory_cost": 1, "pack_code": "sm", "position": 1, "quantity": 2, "side_code": "runner", "stripped_text": "Whenever you make a successful run on R&D, place 1 virus counter on this program. Whenever you breach R&D, choose a number less than the number of hosted virus counters. Access that many additional cards.", "stripped_title": "Medium", "text": "Whenever you make a successful run on R&D, place 1 virus counter on this program.\nWhenever you breach R&D, choose a number less than the number of hosted virus counters. Access that many additional cards.", "title": "Medium", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_parasite_29002(Program):
    '''
    Cost: 2
    Text: Install only on a rezzed piece of ice. When your turn begins, place 1 virus counter on this program. Host ice gets -1 strength for each hosted virus counter. When the strength of host ice is 0 or less, trash it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29002", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Bruno Balixa", "keywords": "Virus - Trojan", "memory_cost": 1, "pack_code": "sm", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a rezzed piece of ice. When your turn begins, place 1 virus counter on this program. Host ice gets -1 strength for each hosted virus counter. When the strength of host ice is 0 or less, trash it.", "stripped_title": "Parasite", "text": "Install only on a rezzed piece of ice.\nWhen your turn begins, place 1 virus counter on this program.\nHost ice gets -1 strength for each hosted virus counter.\nWhen the strength of host ice is 0 or less, trash it.", "title": "Parasite", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cache_29004(Program):
    '''
    Cost: 1
    Text: Place 3 virus counters on Cache when it is installed. Hosted virus counter: Gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29004", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"People keep saying that 'Cash is king' in the business, like it's untraceable in the days of DNA sniffers and microtracers. Digital credits can be just as anonymous, and they're just as easy to counterfeit.\" -Silhouette", "illustrator": "Ed Mattinian", "keywords": "Virus", "memory_cost": 1, "pack_code": "sm", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "Place 3 virus counters on Cache when it is installed. Hosted virus counter: Gain 1 credit.", "stripped_title": "Cache", "text": "Place 3 virus counters on Cache when it is installed.\n<strong>Hosted virus counter:</strong> Gain 1[credit].", "title": "Cache", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cerberus_lady_h1_29006(Program):
    '''
    Cost: 4
    Text: When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 barrier subroutines. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29006", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"Its bytes are definitely worse than its bark.\" -Chaos Theory", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "sm", "position": 6, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "When you install this program, place 4 power counters on it. Interface -> Hosted power counter: Break up to 2 barrier subroutines. 1 credit: +1 strength.", "stripped_title": "Cerberus \"Lady\" H1", "text": "When you install this program, place 4 power counters on it.\nInterface \u2192 <strong>Hosted power counter:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>1[credit]:</strong> +1 strength.", "title": "Cerberus \"Lady\" H1", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_botulus_30004(Program):
    '''
    Cost: 2
    Text: Install only on a piece of ice. When you install this program and when your turn begins, place 1 virus counter on this program. Hosted virus counter: Break 1 subroutine on host ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30004", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Was it something you ate?", "illustrator": "Cat Shen", "keywords": "Virus - Trojan", "memory_cost": 1, "pack_code": "sg", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a piece of ice. When you install this program and when your turn begins, place 1 virus counter on this program. Hosted virus counter: Break 1 subroutine on host ice.", "stripped_title": "Botulus", "text": "Install only on a piece of ice.\nWhen you install this program and when your turn begins, place 1 virus counter on this program.\n<strong>Hosted virus counter:</strong> Break 1 subroutine on host ice.", "title": "Botulus", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_buzzsaw_30005(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break up to 2 code gate subroutines. 3 credits: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30005", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "Destruction is an art.", "illustrator": "Cat Shen", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "sg", "position": 5, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 1 credit: Break up to 2 code gate subroutines. 3 credits: +1 strength.", "stripped_title": "Buzzsaw", "text": "Interface \u2192 <strong>1[credit]:</strong> Break up to 2 <strong>code gate</strong> subroutines.\n<strong>3[credit]:</strong> +1 strength.", "title": "Buzzsaw", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cleaver_30006(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break up to 2 barrier subroutines. 2 credits: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30006", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Subtlety is a luxury.", "illustrator": "Cat Shen", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "sg", "position": 6, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 1 credit: Break up to 2 barrier subroutines. 2 credits: +1 strength.", "stripped_title": "Cleaver", "text": "Interface \u2192 <strong>1[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines.\n<strong>2[credit]:</strong> +1 strength.", "title": "Cleaver", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_fermenter_30007(Program):
    '''
    Cost: 1
    Text: When you install this program and when your turn begins, place 1 virus counter on this program. click, trash: Gain 2 credits for each hosted virus counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30007", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"There's a tension to a cook. Each processing cycle sweetens the pot and raises the heat. I stir all night, but few have my appetite for danger.\"\n\u2014Ren\u00e9 \"Loup\" Arcemont", "illustrator": "Cat Shen", "keywords": "Virus", "memory_cost": 1, "pack_code": "sg", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this program and when your turn begins, place 1 virus counter on this program. click, trash: Gain 2 credits for each hosted virus counter.", "stripped_title": "Fermenter", "text": "When you install this program and when your turn begins, place 1 virus counter on this program.\n[click], [trash]<strong>:</strong> Gain 2[credit] for each hosted virus counter.", "title": "Fermenter", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_leech_30008(Program):
    '''
    Cost: 1
    Text: Whenever you make a successful run on a central server, place 1 virus counter on this program. Hosted virus counter: The ice you are encountering gets -1 strength for the remainder of this encounter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30008", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "The greediest bloodsucker this side of a corporate boardroom.", "illustrator": "Cat Shen", "keywords": "Virus", "memory_cost": 1, "pack_code": "sg", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on a central server, place 1 virus counter on this program. Hosted virus counter: The ice you are encountering gets -1 strength for the remainder of this encounter.", "stripped_title": "Leech", "text": "Whenever you make a successful run on a central server, place 1 virus counter on this program.\n<strong>Hosted virus counter:</strong> The ice you are encountering gets -1 strength for the remainder of this encounter.", "title": "Leech", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_carmen_30015(Program):
    '''
    Cost: 5
    Text: If you made a successful run this turn, this program costs 2 credits less to install. Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30015", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "The whole wide world your domain\nFor law your own free will.", "illustrator": "Jack Reeves", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "sg", "position": 15, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "If you made a successful run this turn, this program costs 2 credits less to install. Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +3 strength.", "stripped_title": "Carmen", "text": "If you made a successful run this turn, this program costs 2[credit] less to install.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +3 strength.", "title": "Carmen", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_marjanah_30016(Program):
    '''
    Cost: 0
    Text: Interface -> 2 credits: Break 1 barrier subroutine. If you made a successful run this turn, this ability costs 1 credit less to use. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30016", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"You can't rule a kingdom by standing still.\"\n\u2014Zahya Sadeghi", "illustrator": "Jack Reeves", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "sg", "position": 16, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 2 credits: Break 1 barrier subroutine. If you made a successful run this turn, this ability costs 1 credit less to use. 1 credit: +1 strength.", "stripped_title": "Marjanah", "text": "Interface \u2192 <strong>2[credit]:</strong> Break 1 <strong>barrier</strong> subroutine. If you made a successful run this turn, this ability costs 1[credit] less to use.\n<strong>1[credit]:</strong> +1 strength.", "title": "Marjanah", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_tranquilizer_30017(Program):
    '''
    Cost: 2
    Text: Install only on a piece of ice. When you install this program and when your turn begins, place 1 virus counter on this program. Then, if there are 3 or more hosted virus counters, derez host ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30017", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Shhhh. It's naptime.", "illustrator": "Jack Reeves", "keywords": "Virus - Trojan", "memory_cost": 1, "pack_code": "sg", "position": 17, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a piece of ice. When you install this program and when your turn begins, place 1 virus counter on this program. Then, if there are 3 or more hosted virus counters, derez host ice.", "stripped_title": "Tranquilizer", "text": "Install only on a piece of ice.\nWhen you install this program and when your turn begins, place 1 virus counter on this program. Then, if there are 3 or more hosted virus counters, derez host ice.", "title": "Tranquilizer", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_conduit_30024(Program):
    '''
    Cost: 4
    Text: Whenever a successful run on R&D ends, you may place 1 virus counter on this program. click: Run R&D. If successful, access X additional cards when you breach R&D. X is equal to the number of hosted virus counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30024", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "A dabbling with truth is a pernicious dream\nDrink deep, or taste not the raw datastream.", "illustrator": "Liiga Smilshkalne", "keywords": "Virus", "memory_cost": 1, "pack_code": "sg", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever a successful run on R&D ends, you may place 1 virus counter on this program. click: Run R&D. If successful, access X additional cards when you breach R&D. X is equal to the number of hosted virus counters.", "stripped_title": "Conduit", "text": "Whenever a successful run on R&D ends, you may place 1 virus counter on this program.\n[click]<strong>:</strong> Run R&D. If successful, access X additional cards when you breach R&D. X is equal to the number of hosted virus counters.", "title": "Conduit", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_echelon_30025(Program):
    '''
    Cost: 3
    Text: This program gets +1 strength for each installed icebreaker (including this one). Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30025", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "The beauty of open projects\u2014each stands atop past success.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "sg", "position": 25, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "This program gets +1 strength for each installed icebreaker (including this one). Interface -> 1 credit: Break 1 sentry subroutine. 3 credits: +2 strength.", "stripped_title": "Echelon", "text": "This program gets +1 strength for each installed <strong>icebreaker</strong> <em>(including this one)</em>.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>3[credit]:</strong> +2 strength.", "title": "Echelon", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_unity_30026(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for each installed icebreaker (including this one).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30026", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "The joy of handcrafted code\u2014each fits perfectly within the whole.", "illustrator": "Liiga Smilshkalne", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "sg", "position": 26, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for each installed icebreaker (including this one).", "stripped_title": "Unity", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength for each installed <strong>icebreaker</strong> <em>(including this one)</em>.", "title": "Unity", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_mayfly_30032(Program):
    '''
    Cost: 1
    Text: Interface -> 1 credit: Break 1 subroutine. When this run ends, trash this program. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30032", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Compiling even the smallest AI takes weeks for only seconds of runtime, but that brief, shining moment allows... <strong>everything</strong>.", "illustrator": "Scott Uminga", "keywords": "Icebreaker - AI", "memory_cost": 2, "pack_code": "sg", "position": 32, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "Interface -> 1 credit: Break 1 subroutine. When this run ends, trash this program. 1 credit: +1 strength.", "stripped_title": "Mayfly", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 subroutine. When this run ends, trash this program.\n<strong>1[credit]:</strong> +1 strength.", "title": "Mayfly", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_clot_31005(Program):
    '''
    Cost: 2
    Text: The Corp cannot score an agenda during the same turn they installed that agenda. When the Corp purges virus counters, trash this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31005", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Surprising, how a single blocked datafeed brings the system to its knees.", "illustrator": "Zoe Cohen", "keywords": "Virus", "memory_cost": 1, "pack_code": "su21", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "The Corp cannot score an agenda during the same turn they installed that agenda. When the Corp purges virus counters, trash this program.", "stripped_title": "Clot", "text": "The Corp cannot score an agenda during the same turn they installed that agenda.\nWhen the Corp purges virus counters, trash this program.", "title": "Clot", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_corroder_31006(Program):
    '''
    Cost: 2
    Text: Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31006", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"Oh, holy Rust,\nTurn foundation into dust.\nOh, sacred Flood,\nWash away what we have become.\"\n\u2014Rent Strike", "illustrator": "Zoe Cohen", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "su21", "position": 6, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 barrier subroutine. 1 credit: +1 strength.", "stripped_title": "Corroder", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Corroder", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_imp_31007(Program):
    '''
    Cost: 2
    Text: When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31007", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Just don't let it bounce back up the feed to <strong>your</strong> rig.", "illustrator": "Krembler", "keywords": "Virus", "memory_cost": 1, "pack_code": "su21", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this program, place 2 virus counters on it. Access -> Hosted virus counter: Trash the card you are accessing. Use this ability only once per turn.", "stripped_title": "Imp", "text": "When you install this program, place 2 virus counters on it.\nAccess \u2192 <strong>Hosted virus counter:</strong> Trash the card you are accessing. Use this ability only once per turn.", "title": "Imp", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_mimic_31008(Program):
    '''
    Cost: 3
    Text: Interface -> 1 credit: Break 1 sentry subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31008", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "What is another mask to those we already wear?", "illustrator": "Patrick B.", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "su21", "position": 8, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine.", "stripped_title": "Mimic", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.", "title": "Mimic", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_abagnale_31021(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. trash: Bypass the code gate you are encountering.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31021", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Slippier than a buttered escargot.", "illustrator": "Zoe Cohen", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "su21", "position": 21, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength. trash: Bypass the code gate you are encountering.", "stripped_title": "Abagnale", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> +2 strength.\n[trash]<strong>:</strong> Bypass the <strong>code gate</strong> you are encountering.", "title": "Abagnale", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_femme_fatale_31022(Program):
    '''
    Cost: 9
    Text: Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31022", "cost": 9, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "Her touch is as cold as her heart.", "illustrator": "Krembler", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "su21", "position": 22, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 sentry subroutine. 2 credits: +1 strength. When you install this program, choose 1 installed piece of ice. Whenever you encounter the chosen ice, you may pay 1 credit for each subroutine it has. If you do, bypass that ice.", "stripped_title": "Femme Fatale", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +1 strength.\nWhen you install this program, choose 1 installed piece of ice.\nWhenever you encounter the chosen ice, you may pay 1[credit] for each subroutine it has. If you do, bypass that ice.", "title": "Femme Fatale", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_sneakdoor_beta_31023(Program):
    '''
    Cost: 4
    Text: click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31023", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "There is no such thing as truly disconnected from the Net.", "illustrator": "Atomikrin", "memory_cost": 2, "pack_code": "su21", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "click: Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.", "stripped_title": "Sneakdoor Beta", "text": "[click]<strong>:</strong> Run Archives. If that run would be declared successful, change the attacked server to HQ for the remainder of that run.", "title": "Sneakdoor Beta", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_atman_31030(Program):
    '''
    Cost: 3
    Text: When you install this program, you may pay X credits to place X power counters on it. This program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength. Interface -> 1 credit: Break 1 subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31030", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "I do not run with my tools. I run with my heart.", "illustrator": "Atomikrin", "keywords": "Icebreaker - AI", "memory_cost": 1, "pack_code": "su21", "position": 30, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "When you install this program, you may pay X credits to place X power counters on it. This program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength. Interface -> 1 credit: Break 1 subroutine.", "stripped_title": "Atman", "text": "When you install this program, you may pay X[credit] to place X power counters on it.\nThis program gets +1 strength for each hosted power counter, and it can only interface with ice of exactly equal strength.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 subroutine.", "title": "Atman", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_chameleon_31031(Program):
    '''
    Cost: 2
    Text: When you install this program, choose barrier, code gate, or sentry. When your discard phase ends, add this program to your grip. Interface -> 1 credit: Break 1 subroutine on a piece of ice that has the chosen subtype.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31031", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "I saved it to my desktop once; couldn't find the thing for a week!", "illustrator": "Krembler", "keywords": "Icebreaker", "memory_cost": 1, "pack_code": "su21", "position": 31, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "When you install this program, choose barrier, code gate, or sentry. When your discard phase ends, add this program to your grip. Interface -> 1 credit: Break 1 subroutine on a piece of ice that has the chosen subtype.", "stripped_title": "Chameleon", "text": "When you install this program, choose <strong>barrier</strong>, <strong>code gate</strong>, or <strong>sentry</strong>.\nWhen your discard phase ends, add this program to your grip.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 subroutine on a piece of ice that has the chosen subtype.", "title": "Chameleon", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_egret_31032(Program):
    '''
    Cost: 2
    Text: Install only on a rezzed piece of ice. Host ice gains barrier, code gate, and sentry.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31032", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Pallas Athena sent a heron gliding down the night. They could not see it passing, but they heard its cry.\"\n\u2014The Iliad", "illustrator": "N. Hopkins", "keywords": "Trojan", "memory_cost": 1, "pack_code": "su21", "position": 32, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a rezzed piece of ice. Host ice gains barrier, code gate, and sentry.", "stripped_title": "Egret", "text": "Install only on a rezzed piece of ice.\nHost ice gains <strong>barrier</strong>, <strong>code gate</strong>, and <strong>sentry</strong>.", "title": "Egret", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_gordian_blade_31033(Program):
    '''
    Cost: 4
    Text: Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31033", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "A thousand puzzles with a single solution.", "illustrator": "Zoe Cohen", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "su21", "position": 33, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength for the remainder of this run.", "stripped_title": "Gordian Blade", "text": "Interface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength for the remainder of this run.", "title": "Gordian Blade", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_paricia_31034(Program):
    '''
    Cost: 0
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs of assets.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31034", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "A rising tide drowns all servers.", "illustrator": "Zoe Cohen", "memory_cost": 1, "pack_code": "su21", "position": 34, "quantity": 3, "side_code": "runner", "stripped_text": "2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs of assets.", "stripped_title": "Paricia", "text": "2[recurring-credit] <em>(When you install this card and before your turn begins, refill to 2 hosted credits.)</em>\nYou can spend hosted credits to pay trash costs of assets.", "title": "Paricia", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_revolver_32002(Program):
    '''
    Cost: 2
    Text: When you install this program, place 6 power counters on it. Interface -> trash or hosted power counter: Break 1 sentry subroutine. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "32002", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "illustrator": "Bruno Balixa", "keywords": "Icebreaker - Killer - Weapon", "memory_cost": 1, "pack_code": "msbp", "position": 2, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "When you install this program, place 6 power counters on it. Interface -> trash or hosted power counter: Break 1 sentry subroutine. 2 credits: +3 strength.", "stripped_title": "Revolver", "text": "When you install this program, place 6 power counters on it.\nInterface \u2192 [trash] or <strong>hosted power counter:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +3 strength.", "title": "Revolver", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_begemot_33007(Program):
    '''
    Cost: 5
    Text: When you install this program, suffer 1 core damage. This program gets +1 strength for each core damage you have taken this game. Interface -> 1 credit: Break any number of barrier subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33007", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "He didn't speak, but I knew exactly what he wanted, and what I had to do.", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Icebreaker - Fracter", "memory_cost": 2, "pack_code": "ms", "position": 7, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "When you install this program, suffer 1 core damage. This program gets +1 strength for each core damage you have taken this game. Interface -> 1 credit: Break any number of barrier subroutines.", "stripped_title": "Begemot", "text": "When you install this program, suffer 1 core damage.\nThis program gets +1 strength for each core damage you have taken this game.\nInterface \u2192 <strong>1[credit]:</strong> Break any number of <strong>barrier</strong> subroutines.", "title": "Begemot", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cats_cradle_33016(Program):
    '''
    Cost: 2
    Text: The rez cost of each piece of code gate ice is increased by 1 credit. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33016", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "I can show you a carpet, a fish, a magical tale...", "illustrator": "Bruno Balixa", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "ms", "position": 16, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "The rez cost of each piece of code gate ice is increased by 1 credit. Interface -> 1 credit: Break 1 code gate subroutine. 1 credit: +1 strength.", "stripped_title": "Cat's Cradle", "text": "The rez cost of each piece of <strong>code gate</strong> ice is increased by 1[credit].\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>1[credit]:</strong> +1 strength.", "title": "Cat's Cradle", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_cezve_33017(Program):
    '''
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits during runs on central servers.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33017", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "The feel of flour-fine coffee, the scent of caramelizing sugar, the gentle heat of the flame. A ritual I never forget.", "illustrator": "Bruno Balixa", "memory_cost": 1, "pack_code": "ms", "position": 17, "quantity": 3, "side_code": "runner", "stripped_text": "2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits during runs on central servers.", "stripped_title": "Cezve", "text": "2[recurring-credit] <em>(When you install this card and before your turn begins, refill to 2 hosted credits.)</em>\nYou can spend hosted credits during runs on central servers.", "title": "Cezve", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_revolver_33018(Program):
    '''
    Cost: 2
    Text: When you install this program, place 6 power counters on it. Interface -> trash or hosted power counter: Break 1 sentry subroutine. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33018", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Aim with your eye. Shoot with your mind. Break with your soul.\"\n\u2013Sundog", "illustrator": "Bruno Balixa", "keywords": "Icebreaker - Killer - Weapon", "memory_cost": 1, "pack_code": "ms", "position": 18, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "When you install this program, place 6 power counters on it. Interface -> trash or hosted power counter: Break 1 sentry subroutine. 2 credits: +3 strength.", "stripped_title": "Revolver", "text": "When you install this program, place 6 power counters on it.\nInterface \u2192 [trash] or <strong>hosted power counter:</strong> Break 1 <strong>sentry</strong> subroutine.\n<strong>2[credit]:</strong> +3 strength.", "title": "Revolver", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_hyperbaric_33026(Program):
    '''
    Cost: 3
    Text: When you install this program, place 1 power counter on it. This program gets +1 strength for each hosted power counter. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: Place 1 power counter on this program.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33026", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Cat Shen", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "ms", "position": 26, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "When you install this program, place 1 power counter on it. This program gets +1 strength for each hosted power counter. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: Place 1 power counter on this program.", "stripped_title": "Hyperbaric", "text": "When you install this program, place 1 power counter on it.\nThis program gets +1 strength for each hosted power counter.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> Place 1 power counter on this program.", "title": "Hyperbaric", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_propeller_33027(Program):
    '''
    Cost: 1
    Text: When you install this program, place 4 power counters on it. Interface -> 1 credit: Break 1 barrier subroutine. Hosted power counter: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33027", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Within netspace, tangible space can be manipulated as desired, and fluid dynamics rarely factors into ice development.", "illustrator": "Cat Shen", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "ms", "position": 27, "quantity": 3, "side_code": "runner", "strength": 0, "stripped_text": "When you install this program, place 4 power counters on it. Interface -> 1 credit: Break 1 barrier subroutine. Hosted power counter: +2 strength.", "stripped_title": "Propeller", "text": "When you install this program, place 4 power counters on it.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>barrier</strong> subroutine.\n<strong>Hosted power counter:</strong> +2 strength.", "title": "Propeller", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_abaasy_33070(Program):
    '''
    Cost: 2
    Text: The first time each turn this program fully breaks a piece of ice, you may trash 1 card from your grip to draw 1 card. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33070", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Every piece of ice I see, I see Abaasy.", "illustrator": "Bruno Balixa", "keywords": "Icebreaker - Decoder", "memory_cost": 1, "pack_code": "ph", "position": 70, "quantity": 3, "side_code": "runner", "strength": 1, "stripped_text": "The first time each turn this program fully breaks a piece of ice, you may trash 1 card from your grip to draw 1 card. Interface -> 1 credit: Break 1 code gate subroutine. 2 credits: +2 strength.", "stripped_title": "Abaasy", "text": "The first time each turn this program fully breaks a piece of ice, you may trash 1 card from your grip to draw 1 card.\nInterface \u2192 <strong>1[credit]:</strong> Break 1 <strong>code gate</strong> subroutine.\n<strong>2[credit]:</strong> +2 strength.", "title": "Abaasy", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_hush_33071(Program):
    '''
    Cost: 1
    Text: Install only on a piece of ice. Host ice cannot gain abilities and loses all abilities except its printed subroutines. click: Host this program on another installed piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33071", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "Quiet. I need to focus.", "illustrator": "Scott Uminga", "keywords": "Trojan", "memory_cost": 1, "pack_code": "ph", "position": 71, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a piece of ice. Host ice cannot gain abilities and loses all abilities except its printed subroutines. click: Host this program on another installed piece of ice.", "stripped_title": "Hush", "text": "Install only on a piece of ice.\nHost ice cannot gain abilities and loses all abilities except its printed subroutines.\n<strong>[click]:</strong> Host this program on another installed piece of ice.", "title": "Hush", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_nga_33072(Program):
    '''
    Cost: 2
    Text: When you install this program, load 3 power counters onto it. When it is empty, trash it. The first time each turn you make a successful run, you may remove 1 hosted power counter to sabotage 1. (The Corp trashes 1 card of their choice from HQ or the top of R&D.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33072", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Relinquish your foolish notions of control.", "illustrator": "Bruno Balixa", "memory_cost": 1, "pack_code": "ph", "position": 72, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this program, load 3 power counters onto it. When it is empty, trash it. The first time each turn you make a successful run, you may remove 1 hosted power counter to sabotage 1. (The Corp trashes 1 card of their choice from HQ or the top of R&D.)", "stripped_title": "Nga", "text": "When you install this program, load 3 power counters onto it. When it is empty, trash it.\nThe first time each turn you make a successful run, you may remove 1 hosted power counter to sabotage 1. <em>(The Corp trashes 1 card of their choice from HQ or the top of R&D.)</em>", "title": "Nga", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_num_33073(Program):
    '''
    Cost: 4
    Text: Interface -> 2 credits: Break 1 sentry subroutine.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33073", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "I give you understanding, that you might control that which would threaten you.", "illustrator": "Bruno Balixa", "keywords": "Icebreaker - Killer", "memory_cost": 1, "pack_code": "ph", "position": 73, "quantity": 3, "side_code": "runner", "strength": 8, "stripped_text": "Interface -> 2 credits: Break 1 sentry subroutine.", "stripped_title": "Num", "text": "Interface \u2192 <strong>2[credit]:</strong> Break 1 <strong>sentry</strong> subroutine.", "title": "Num", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_tremolo_33080(Program):
    '''
    Cost: 3
    Text: Interface -> 3 credits: Break up to 2 barrier subroutines. This ability costs 1 credit less to use for each installed piece of cybernetic hardware. 2 credits: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33080", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "A repeated note, the alternation of fingers, the rhythm of stitches... the resulting intensity is always the same.", "illustrator": "Bruno Balixa", "keywords": "Icebreaker - Fracter", "memory_cost": 1, "pack_code": "ph", "position": 80, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "Interface -> 3 credits: Break up to 2 barrier subroutines. This ability costs 1 credit less to use for each installed piece of cybernetic hardware. 2 credits: +2 strength.", "stripped_title": "Tremolo", "text": "Interface \u2192 <strong>3[credit]:</strong> Break up to 2 <strong>barrier</strong> subroutines. This ability costs 1[credit] less to use for each installed piece of <strong>cybernetic</strong> hardware.\n<strong>2[credit]:</strong> +2 strength.", "title": "Tremolo", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_tunnel_vision_33081(Program):
    '''
    Cost: 2
    Text: When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) Interface -> 2 credits: Break up to 2 subroutines on a piece of ice protecting your mark. 2 credits: +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33081", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"How could I pick a favorite? They\u02bcre all good dogs.\"\n\u2014Nyusha \"Sable\" Sintashta", "illustrator": "Anthony Hutchings", "keywords": "Icebreaker - AI", "memory_cost": 2, "pack_code": "ph", "position": 81, "quantity": 3, "side_code": "runner", "strength": 2, "stripped_text": "When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) Interface -> 2 credits: Break up to 2 subroutines on a piece of ice protecting your mark. 2 credits: +2 strength.", "stripped_title": "Tunnel Vision", "text": "When your turn begins, identify your mark. <em>(If you don\u02bct have a mark, a random central server becomes your mark for this turn.)</em>\nInterface \u2192 <strong>2[credit]:</strong> Break up to 2 subroutines on a piece of ice protecting your mark.\n<strong>2[credit]:</strong> +2 strength.", "title": "Tunnel Vision", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_flux_capacitor_33087(Program):
    '''
    Cost: 0
    Text: Install only on a piece of ice. The first time you break a subroutine during each encounter with host ice, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33087", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Are you telling me it\u02bcs pronounced \u02bcgigawatts\u02bc?\"\n\u2014Captain Padma Isbister", "illustrator": "Ed Mattinian", "keywords": "Trojan", "memory_cost": 1, "pack_code": "ph", "position": 87, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on a piece of ice. The first time you break a subroutine during each encounter with host ice, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)", "stripped_title": "Flux Capacitor", "text": "Install only on a piece of ice.\nThe first time you break a subroutine during each encounter with host ice, you may charge 1 of your installed cards. <em>(Add 1 power counter to a card that already has one.)</em>", "title": "Flux Capacitor", "type_code": "program", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_nanuq_33088(Program):
    '''
    Cost: 4
    Text: When this program is uninstalled, remove it from the game. When an agenda is scored or stolen, remove this program from the game. Interface -> 2 credits: Break up to 2 subroutines. 1 credit: +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33088", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 5, "flavor": "Nanuq never leaves, but instead waits, invisible, for the next hunt.", "illustrator": "Adam S. Doyle", "keywords": "Icebreaker - AI", "memory_cost": 2, "pack_code": "ph", "position": 88, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "When this program is uninstalled, remove it from the game. When an agenda is scored or stolen, remove this program from the game. Interface -> 2 credits: Break up to 2 subroutines. 1 credit: +1 strength.", "stripped_title": "Nanuq", "text": "When this program is uninstalled, remove it from the game.\nWhen an agenda is scored or stolen, remove this program from the game.\nInterface \u2192 <strong>2[credit]:</strong> Break up to 2 subroutines.\n1[credit]: +1 strength.", "title": "Nanuq", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_orca_33089(Program):
    '''
    Cost: 10
    Text: The first time each turn this program fully breaks a piece of ice, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.) Interface -> 2 credits: Break any number of sentry subroutines. 2 credits: +3 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33089", "cost": 10, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Jakuza", "keywords": "Icebreaker - Killer", "memory_cost": 2, "pack_code": "ph", "position": 89, "quantity": 3, "side_code": "runner", "strength": 3, "stripped_text": "The first time each turn this program fully breaks a piece of ice, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.) Interface -> 2 credits: Break any number of sentry subroutines. 2 credits: +3 strength.", "stripped_title": "Orca", "text": "The first time each turn this program fully breaks a piece of ice, you may charge 1 of your installed cards. <em>(Add 1 power counter to a card that already has one.)</em>\nInterface \u2192 <strong>2[credit]:</strong> Break any number of <strong>sentry</strong> subroutines.\n<strong>2[credit]:</strong> +3 strength.", "title": "Orca", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_k2cp_turbine_33090(Program):
    '''
    Cost: 4
    Text: Each installed non-AI icebreaker gets +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33090", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "Every rig needs a power source. How about one with blades moving at Mach 2?", "illustrator": "Ed Mattinian", "memory_cost": 1, "pack_code": "ph", "position": 90, "quantity": 3, "side_code": "runner", "stripped_text": "Each installed non-AI icebreaker gets +2 strength.", "stripped_title": "K2CP Turbine", "text": "Each installed non-<strong>AI</strong> <strong>icebreaker</strong> gets +2 strength.", "title": "K2CP Turbine", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_world_tree_33091(Program):
    '''
    Cost: 6
    Text: The first time each turn you make a successful run, you may trash 1 of your other installed cards to search your stack for 1 card of the same type. (Shuffle your stack after searching it.) Install the card you found, paying 3 credits less.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33091", "cost": 6, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "Few constructs reach the Deep Net, but these old trees have stretched their roots further than once thought possible.", "illustrator": "Liiga Smilshkalne", "keywords": "Deep Net", "memory_cost": 2, "pack_code": "ph", "position": 91, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you make a successful run, you may trash 1 of your other installed cards to search your stack for 1 card of the same type. (Shuffle your stack after searching it.) Install the card you found, paying 3 credits less.", "stripped_title": "World Tree", "text": "The first time each turn you make a successful run, you may trash 1 of your other installed cards to search your stack for 1 card of the same type. <em>(Shuffle your stack after searching it.)</em> Install the card you found, paying 3[credit] less.", "title": "World Tree", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class program_matryoshka_33094(Program):
    '''
    Cost: 3
    Text: When your turn begins, turn each hosted card faceup. click: Host a copy of Matryoshka from your grip faceup on this program. (It is not installed.) Interface -> X{c}, turn 1 hosted copy of Matryoshka facedown: Break X subroutines. 1 credit: +1 strength. Limit 6 per deck.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33094", "cost": 3, "deck_limit": 6, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "{Card 6} Look at the little baby, even she helps!\n{Card 5} She\u02bcs little\u2014but fierce.\n{Card 4} Just as brave as his sisters.\n{Card 3} She\u02bcs a typical middle child, really.\n{Card 2} Always there to back up her big sister.\n{Card 1} She leads and they all follow.", "illustrator": "Ed Mattinian", "keywords": "Icebreaker - AI", "memory_cost": 2, "pack_code": "ph", "position": 94, "quantity": 6, "side_code": "runner", "strength": 2, "stripped_text": "When your turn begins, turn each hosted card faceup. click: Host a copy of Matryoshka from your grip faceup on this program. (It is not installed.) Interface -> X{c}, turn 1 hosted copy of Matryoshka facedown: Break X subroutines. 1 credit: +1 strength. Limit 6 per deck.", "stripped_title": "Matryoshka", "text": "When your turn begins, turn each hosted card faceup.\n[click]<strong>:</strong> Host a copy of Matryoshka from your grip faceup on this program. <em>(It is not installed.)</em>\nInterface \u2192 <strong>X[credit]</strong>, <strong>turn 1 hosted copy of Matryoshka facedown:</strong> Break X subroutines.\n<strong>1[credit]:</strong> +1 strength.\nLimit 6 per deck.", "title": "Matryoshka", "type_code": "program", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"
