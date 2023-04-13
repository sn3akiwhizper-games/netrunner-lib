
'''
card classes of type identity
'''
from netrunner_lib.cards._base_card_classes import Identity
from netrunner_lib.game_events import *

class identity_the_shadow_pulling_the_strings_00005(Identity):
    '''
    Cost: n/a
    Text: Draft format only. You can use agendas from all factions in this deck.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "00005", "deck_limit": 1, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "The Past is the Future.", "illustrator": "S\u0142awomir Maniak", "influence_limit": null, "keywords": "Megacorp", "minimum_deck_size": 30, "pack_code": "draft", "position": 5, "quantity": 1, "side_code": "corp", "stripped_text": "Draft format only. You can use agendas from all factions in this deck.", "stripped_title": "The Shadow: Pulling the Strings", "text": "Draft format only.\nYou can use agendas from all factions in this deck.", "title": "The Shadow: Pulling the Strings", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_the_masque_cyber_general_00006(Identity):
    '''
    Cost: n/a
    Text: Draft format only.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "00006", "deck_limit": 1, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"This war is far from over.\"", "illustrator": "Imaginary FS Pte Ltd", "influence_limit": null, "keywords": "Natural", "minimum_deck_size": 30, "pack_code": "draft", "position": 6, "quantity": 1, "side_code": "runner", "stripped_text": "Draft format only.", "stripped_title": "The Masque: Cyber General", "text": "Draft format only.", "title": "The Masque: Cyber General", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_wyvern_chemically_enhanced_00007(Identity):
    '''
    Cost: n/a
    Text: Draft format only. You must maintain the order of your heap. Whenever you trash a Corp card, if you have more anarch cards installed than any other faction, shuffle the top card of your heap into your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "00007", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "illustrator": "Rachel Borovic", "influence_limit": null, "keywords": "G-mod", "minimum_deck_size": 30, "pack_code": "draft", "position": 7, "quantity": 1, "side_code": "runner", "stripped_text": "Draft format only. You must maintain the order of your heap. Whenever you trash a Corp card, if you have more anarch cards installed than any other faction, shuffle the top card of your heap into your stack.", "stripped_title": "Wyvern: Chemically Enhanced", "text": "Draft format only.\nYou must maintain the order of your heap.\nWhenever you trash a Corp card, if you have more [anarch] cards installed than any other faction, shuffle the top card of your heap into your stack.", "title": "Wyvern: Chemically Enhanced", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_boris_syfr_kovac_crafty_veteran_00008(Identity):
    '''
    Cost: n/a
    Text: Draft format only. If you have more criminal cards installed than any other faction, when your turn begins, remove 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "00008", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "illustrator": "Clark Huggins", "influence_limit": null, "keywords": "Cyborg", "minimum_deck_size": 30, "pack_code": "draft", "position": 8, "quantity": 1, "side_code": "runner", "stripped_text": "Draft format only. If you have more criminal cards installed than any other faction, when your turn begins, remove 1 tag.", "stripped_title": "Boris \"Syfr\" Kovac: Crafty Veteran", "text": "Draft format only.\nIf you have more [criminal] cards installed than any other faction, when your turn begins, remove 1 tag.", "title": "Boris \"Syfr\" Kovac: Crafty Veteran", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jamie_bzzz_micken_techno_savant_00009(Identity):
    '''
    Cost: n/a
    Text: Draft format only. If you have more shaper cards installed than any other faction, when you install a card the first time each turn, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "00009", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "illustrator": "Ralph Beisner", "influence_limit": null, "keywords": "Natural", "minimum_deck_size": 30, "pack_code": "draft", "position": 9, "quantity": 1, "side_code": "runner", "stripped_text": "Draft format only. If you have more shaper cards installed than any other faction, when you install a card the first time each turn, draw 1 card.", "stripped_title": "Jamie \"Bzzz\" Micken: Techno Savant", "text": "Draft format only.\nIf you have more [shaper] cards installed than any other faction, when you install a card the first time each turn, draw 1 card.", "title": "Jamie \"Bzzz\" Micken: Techno Savant", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_strategic_innovations_future_forward_00010(Identity):
    '''
    Cost: n/a
    Text: Draft format only. If you have more haas-bioroid cards rezzed than any other faction, when the Runner's turn ends, shuffle 1 card in Archives into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "00010", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Timothy Ben Zweifel", "influence_limit": null, "keywords": "Division", "minimum_deck_size": 30, "pack_code": "draft", "position": 10, "quantity": 1, "side_code": "corp", "stripped_text": "Draft format only. If you have more haas-bioroid cards rezzed than any other faction, when the Runner's turn ends, shuffle 1 card in Archives into R&D.", "stripped_title": "Strategic Innovations: Future Forward", "text": "Draft format only.\nIf you have more [haas-bioroid] cards rezzed than any other faction, when the Runner's turn ends, shuffle 1 card in Archives into R&D.", "title": "Strategic Innovations: Future Forward", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_synthetic_systems_the_world_reimagined_00011(Identity):
    '''
    Cost: n/a
    Text: Draft format only. If you have more jinteki cards rezzed than any other faction, when your turn begins, you may swap 2 pieces of installed ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "00011", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": null, "keywords": "Division", "minimum_deck_size": 30, "pack_code": "draft", "position": 11, "quantity": 1, "side_code": "corp", "stripped_text": "Draft format only. If you have more jinteki cards rezzed than any other faction, when your turn begins, you may swap 2 pieces of installed ice.", "stripped_title": "Synthetic Systems: The World Re-imagined", "text": "Draft format only.\nIf you have more [jinteki] cards rezzed than any other faction, when your turn begins, you may swap 2 pieces of installed ice.", "title": "Synthetic Systems: The World Re-imagined", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_information_dynamics_all_you_need_to_know_00012(Identity):
    '''
    Cost: n/a
    Text: Draft format only. If you have more nbn cards rezzed than any other faction, whenever an agenda is scored or stolen, give the runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "00012", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Amelie Hutt", "influence_limit": null, "keywords": "Division", "minimum_deck_size": 30, "pack_code": "draft", "position": 12, "quantity": 1, "side_code": "corp", "stripped_text": "Draft format only. If you have more nbn cards rezzed than any other faction, whenever an agenda is scored or stolen, give the runner 1 tag.", "stripped_title": "Information Dynamics: All You Need To Know", "text": "Draft format only.\nIf you have more [nbn] cards rezzed than any other faction, whenever an agenda is scored or stolen, give the runner 1 tag.", "title": "Information Dynamics: All You Need To Know", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_fringe_applications_tomorrow_today_00013(Identity):
    '''
    Cost: n/a
    Text: Draft format only. If you have more weyland-consortium cards rezzed than any other faction, when the Runner's turn begins, place an advancement token on a piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "00013", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": null, "keywords": "Division", "minimum_deck_size": 30, "pack_code": "draft", "position": 13, "quantity": 1, "side_code": "corp", "stripped_text": "Draft format only. If you have more weyland-consortium cards rezzed than any other faction, when the Runner's turn begins, place an advancement token on a piece of ice.", "stripped_title": "Fringe Applications: Tomorrow, Today", "text": "Draft format only.\nIf you have more [weyland-consortium] cards rezzed than any other faction, when the Runner's turn begins, place an advancement token on a piece of ice.", "title": "Fringe Applications: Tomorrow, Today", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_noise_hacker_extraordinaire_01001(Identity):
    '''
    Cost: n/a
    Text: Whenever you install a virus program, the Corp trashes the top card of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "01001", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"Watch this. It'll be funny.\"", "illustrator": "Ralph Beisner", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "core", "position": 1, "quantity": 1, "side_code": "runner", "stripped_text": "Whenever you install a virus program, the Corp trashes the top card of R&D.", "stripped_title": "Noise: Hacker Extraordinaire", "text": "Whenever you install a <strong>virus</strong> program, the Corp trashes the top card of R&D.", "title": "Noise: Hacker Extraordinaire", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_gabriel_santiago_consummate_professional_01017(Identity):
    '''
    Cost: n/a
    Text: The first time you make a successful run on HQ each turn, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "01017", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"Of course I steal from the rich. They're the ones with all the money.\"", "illustrator": "Ralph Beisner", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "core", "position": 17, "quantity": 1, "side_code": "runner", "stripped_text": "The first time you make a successful run on HQ each turn, gain 2 credits.", "stripped_title": "Gabriel Santiago: Consummate Professional", "text": "The first time you make a successful run on HQ each turn, gain 2[credit].", "title": "Gabriel Santiago: Consummate Professional", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_kate_mac_mccaffrey_digital_tinker_01033(Identity):
    '''
    Cost: n/a
    Text: Lower the install cost of the first program or piece of hardware you install each turn by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "01033", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"Are you listening?\"", "illustrator": "Ralph Beisner", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "core", "position": 33, "quantity": 1, "side_code": "runner", "stripped_text": "Lower the install cost of the first program or piece of hardware you install each turn by 1.", "stripped_title": "Kate \"Mac\" McCaffrey: Digital Tinker", "text": "Lower the install cost of the first program or piece of hardware you install each turn by 1.", "title": "Kate \"Mac\" McCaffrey: Digital Tinker", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_haasbioroid_engineering_the_future_01054(Identity):
    '''
    Cost: n/a
    Text: The first time you install a card each turn, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01054", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Effective. Reliable. Humane.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "core", "position": 54, "quantity": 1, "side_code": "corp", "stripped_text": "The first time you install a card each turn, gain 1 credit.", "stripped_title": "Haas-Bioroid: Engineering the Future", "text": "The first time you install a card each turn, gain 1[credit].", "title": "Haas-Bioroid: Engineering the Future", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jinteki_personal_evolution_01067(Identity):
    '''
    Cost: n/a
    Text: Whenever an agenda is scored or stolen, do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01067", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "When You Need the Human Touch.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "core", "position": 67, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever an agenda is scored or stolen, do 1 net damage.", "stripped_title": "Jinteki: Personal Evolution", "text": "Whenever an agenda is scored or stolen, do 1 net damage.", "title": "Jinteki: Personal Evolution", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nbn_making_news_01080(Identity):
    '''
    Cost: n/a
    Text: 2 recurring credits Use these credits during trace attempts.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01080", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Someone is Always Watching.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "core", "position": 80, "quantity": 1, "side_code": "corp", "stripped_text": "2 recurring credits Use these credits during trace attempts.", "stripped_title": "NBN: Making News", "text": "2[recurring-credit]\nUse these credits during trace attempts.", "title": "NBN: Making News", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_weyland_consortium_building_a_better_world_01093(Identity):
    '''
    Cost: n/a
    Text: Whenever you play a transaction operation, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01093", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Moving Upwards.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "core", "position": 93, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever you play a transaction operation, gain 1 credit.", "stripped_title": "Weyland Consortium: Building a Better World", "text": "Whenever you play a <strong>transaction</strong> operation, gain 1[credit].", "title": "Weyland Consortium: Building a Better World", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_whizzard_master_gamer_02001(Identity):
    '''
    Cost: n/a
    Text: 3 recurring credits Use these credits to trash cards.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "02001", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"Running is the ultimate game, and I get to make all the rules.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "wla", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "3 recurring credits Use these credits to trash cards.", "stripped_title": "Whizzard: Master Gamer", "text": "3[recurring-credit]\nUse these credits to trash cards.", "title": "Whizzard: Master Gamer", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_haasbioroid_stronger_together_02010(Identity):
    '''
    Cost: n/a
    Text: All bioroid ice has +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02010", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "A Different Breed of Machine.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "wla", "position": 10, "quantity": 3, "side_code": "corp", "stripped_text": "All bioroid ice has +1 strength.", "stripped_title": "Haas-Bioroid: Stronger Together", "text": "All <strong>bioroid</strong> ice has +1 strength.", "title": "Haas-Bioroid: Stronger Together", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jinteki_replicating_perfection_02031(Identity):
    '''
    Cost: n/a
    Text: The Runner cannot run on remote servers. Ignore this ability until the end of the turn whenever the Runner runs on a central server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02031", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "ta", "position": 31, "quantity": 3, "side_code": "corp", "stripped_text": "The Runner cannot run on remote servers. Ignore this ability until the end of the turn whenever the Runner runs on a central server.", "stripped_title": "Jinteki: Replicating Perfection", "text": "The Runner cannot run on remote servers. Ignore this ability until the end of the turn whenever the Runner runs on a central server.", "title": "Jinteki: Replicating Perfection", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_chaos_theory_wunderkind_02046(Identity):
    '''
    Cost: n/a
    Text: +1 mu
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "02046", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"Have you met Dinosaurus?\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 40, "pack_code": "ce", "position": 46, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu", "stripped_title": "Chaos Theory: Wunderkind", "text": "+1[mu]", "title": "Chaos Theory: W\u00fcnderkind", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_weyland_consortium_because_we_built_it_02076(Identity):
    '''
    Cost: n/a
    Text: 1 recurring credit Use this credit to advance ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02076", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Constructing Cyberspace.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "asis", "position": 76, "quantity": 3, "side_code": "corp", "stripped_text": "1 recurring credit Use this credit to advance ice.", "stripped_title": "Weyland Consortium: Because We Built It", "text": "1[recurring-credit]\nUse this credit to advance ice.", "title": "Weyland Consortium: Because We Built It", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_andromeda_dispossessed_ristie_02083(Identity):
    '''
    Cost: n/a
    Text: You draw a starting hand of 9 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "02083", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"I run with the best.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "hs", "position": 83, "quantity": 3, "side_code": "runner", "stripped_text": "You draw a starting hand of 9 cards.", "stripped_title": "Andromeda: Dispossessed Ristie", "text": "You draw a starting hand of 9 cards.", "title": "Andromeda: Dispossessed Ristie", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nbn_the_world_is_yours_02114(Identity):
    '''
    Cost: n/a
    Text: Your maximum hand size is increased by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02114", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "*Some restrictions may apply. Scan this card to find out more.", "influence_limit": 12, "keywords": "Megacorp", "minimum_deck_size": 40, "pack_code": "fp", "position": 114, "quantity": 3, "side_code": "corp", "stripped_text": "Your maximum hand size is increased by 1.", "stripped_title": "NBN: The World is Yours*", "text": "Your maximum hand size is increased by 1.", "title": "NBN: The World is Yours*", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_cerebral_imaging_infinite_frontiers_03001(Identity):
    '''
    Cost: n/a
    Text: Your maximum hand size is equal to the number of credits in your credit pool.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03001", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "The densest information cluster in the galaxy.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "cac", "position": 1, "quantity": 3, "side_code": "corp", "stripped_text": "Your maximum hand size is equal to the number of credits in your credit pool.", "stripped_title": "Cerebral Imaging: Infinite Frontiers", "text": "Your maximum hand size is equal to the number of credits in your credit pool.", "title": "Cerebral Imaging: Infinite Frontiers", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_custom_biotics_engineered_for_success_03002(Identity):
    '''
    Cost: n/a
    Text: You cannot include Jinteki cards in this deck.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03002", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "The Once and Future Android.", "illustrator": "Emilio Rodriguez", "influence_limit": 22, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "cac", "position": 2, "quantity": 3, "side_code": "corp", "stripped_text": "You cannot include Jinteki cards in this deck.", "stripped_title": "Custom Biotics: Engineered for Success", "text": "You cannot include Jinteki cards in this deck.", "title": "Custom Biotics: Engineered for Success", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_next_design_guarding_the_net_03003(Identity):
    '''
    Cost: n/a
    Text: Before taking your first turn, you may install up to 3 pieces of ice, with no more than a single piece of ice per server. Draw until you have 5 cards in HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03003", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 12, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "cac", "position": 3, "quantity": 3, "side_code": "corp", "stripped_text": "Before taking your first turn, you may install up to 3 pieces of ice, with no more than a single piece of ice per server. Draw until you have 5 cards in HQ.", "stripped_title": "NEXT Design: Guarding the Net", "text": "Before taking your first turn, you may install up to 3 pieces of ice, with no more than a single piece of ice per server. Draw until you have 5 cards in HQ.", "title": "NEXT Design: Guarding the Net", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_rielle_kit_peddler_transhuman_03028(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you encounter a piece of ice, it gains code gate for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "03028", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"I was not; I was; I am not; I am all.\"", "illustrator": "Matt Zeilinger", "influence_limit": 10, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "cac", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you encounter a piece of ice, it gains code gate for the remainder of this run.", "stripped_title": "Rielle \"Kit\" Peddler: Transhuman", "text": "The first time each turn you encounter a piece of ice, it gains <strong>code gate</strong> for the remainder of this run.", "title": "Rielle \"Kit\" Peddler: Transhuman", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_the_professor_keeper_of_knowledge_03029(Identity):
    '''
    Cost: n/a
    Text: The first copy of each program in this deck does not count against your influence limit.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "03029", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"New technology destroys the old.\"", "illustrator": "Matt Zeilinger", "influence_limit": 1, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "cac", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "The first copy of each program in this deck does not count against your influence limit.", "stripped_title": "The Professor: Keeper of Knowledge", "text": "The first copy of each program in this deck does not count against your influence limit.", "title": "The Professor: Keeper of Knowledge", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_exile_streethawk_03030(Identity):
    '''
    Cost: n/a
    Text: Whenever you install a program from your heap, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "03030", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"I can make that work.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "cac", "position": 30, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you install a program from your heap, draw 1 card.", "stripped_title": "Exile: Streethawk", "text": "Whenever you install a program from your heap, draw 1 card.", "title": "Exile: Streethawk", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_reina_roja_freedom_fighter_04041(Identity):
    '''
    Cost: n/a
    Text: The first piece of ice the Corp rezzes each turn costs 1 credit more to rez.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "04041", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"Analyzing the board won't help. Your mistake was thinking we're playing the same game.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Cyborg - G-mod", "minimum_deck_size": 45, "pack_code": "mt", "position": 41, "quantity": 3, "side_code": "runner", "stripped_text": "The first piece of ice the Corp rezzes each turn costs 1 credit more to rez.", "stripped_title": "Reina Roja: Freedom Fighter", "text": "The first piece of ice the Corp rezzes each turn costs 1[credit] more to rez.", "title": "Reina Roja: Freedom Fighter", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_grndl_power_unleashed_04097(Identity):
    '''
    Cost: n/a
    Text: You start the game with 10 credits and 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04097", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "<strong>G</strong>eostrategic <strong>R</strong>esearch and <strong>N</strong>eothermal <strong>D</strong>evelopment <strong>L</strong>aboratories", "illustrator": "Emilio Rodriguez", "influence_limit": 10, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "fal", "position": 97, "quantity": 3, "side_code": "corp", "stripped_text": "You start the game with 10 credits and 1 bad publicity.", "stripped_title": "GRNDL: Power Unleashed", "text": "You start the game with 10[credit] and 1 bad publicity.", "title": "GRNDL: Power Unleashed", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_harmony_medtech_biomedical_pioneer_05001(Identity):
    '''
    Cost: n/a
    Text: Each player needs 1 fewer agenda point to win the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05001", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "Evolving a Better You.", "illustrator": "Emilio Rodriguez", "influence_limit": 12, "keywords": "Division", "minimum_deck_size": 40, "pack_code": "hap", "position": 1, "quantity": 3, "side_code": "corp", "stripped_text": "Each player needs 1 fewer agenda point to win the game.", "stripped_title": "Harmony Medtech: Biomedical Pioneer", "text": "Each player needs 1 fewer agenda point to win the game.", "title": "Harmony Medtech: Biomedical Pioneer", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nisei_division_the_next_generation_05002(Identity):
    '''
    Cost: n/a
    Text: Whenever you and the Runner reveal secretly spent credits, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05002", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "Perfecting the Imperfect.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "hap", "position": 2, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you and the Runner reveal secretly spent credits, gain 1 credit.", "stripped_title": "Nisei Division: The Next Generation", "text": "Whenever you and the Runner reveal secretly spent credits, gain 1[credit].", "title": "Nisei Division: The Next Generation", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_tennin_institute_the_secrets_within_05003(Identity):
    '''
    Cost: n/a
    Text: When your turn begins, if the Runner did not make a successful run during their last turn, you may place 1 advancement counter on an installed card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05003", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "hap", "position": 3, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, if the Runner did not make a successful run during their last turn, you may place 1 advancement counter on an installed card.", "stripped_title": "Tennin Institute: The Secrets Within", "text": "When your turn begins, if the Runner did not make a successful run during their last turn, you may place 1 advancement counter on an installed card.", "title": "Tennin Institute: The Secrets Within", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_iain_stirling_retired_spook_05028(Identity):
    '''
    Cost: n/a
    Text: When your turn begins, gain 2 credits if the Corp has more scored agenda points than you.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "05028", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"Truth is a fickle mistress.\"", "illustrator": "Simon Eckert", "influence_limit": 10, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "hap", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, gain 2 credits if the Corp has more scored agenda points than you.", "stripped_title": "Iain Stirling: Retired Spook", "text": "When your turn begins, gain 2[credit] if the Corp has more scored agenda points than you.", "title": "Iain Stirling: Retired Spook", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_ken_express_tenma_disappeared_clone_05029(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you play a run event, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "05029", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"Try to keep up.\"", "illustrator": "Simon Eckert", "influence_limit": 17, "keywords": "Clone", "minimum_deck_size": 45, "pack_code": "hap", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you play a run event, gain 1 credit.", "stripped_title": "Ken \"Express\" Tenma: Disappeared Clone", "text": "The first time each turn you play a <strong>run</strong> event, gain 1[credit].", "title": "Ken \"Express\" Tenma: Disappeared Clone", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_silhouette_stealth_operative_05030(Identity):
    '''
    Cost: n/a
    Text: The first time you make a successful run on HQ each turn, you may expose 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "05030", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"Don't waste my time.\"", "illustrator": "Simon Eckert", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 40, "pack_code": "hap", "position": 30, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you make a successful run on HQ each turn, you may expose 1 card.", "stripped_title": "Silhouette: Stealth Operative", "text": "The first time you make a successful run on HQ each turn, you may expose 1 card.", "title": "Silhouette: Stealth Operative", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nearearth_hub_broadcast_center_06005(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you create a remote server, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06005", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Only the News You Need.", "illustrator": "Emilio Rodriguez", "influence_limit": 17, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "up", "position": 5, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn you create a remote server, draw 1 card.", "stripped_title": "Near-Earth Hub: Broadcast Center", "text": "The first time each turn you create a remote server, draw 1 card.", "title": "Near-Earth Hub: Broadcast Center", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nasir_meidan_cyber_explorer_06017(Identity):
    '''
    Cost: n/a
    Text: Whenever you encounter a piece of ice after an approach during which that ice was rezzed, lose all credits in your credit pool. Gain credits equal to the rez cost of that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "06017", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "up", "position": 17, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you encounter a piece of ice after an approach during which that ice was rezzed, lose all credits in your credit pool. Gain credits equal to the rez cost of that ice.", "stripped_title": "Nasir Meidan: Cyber Explorer", "text": "Whenever you encounter a piece of ice after an approach during which that ice was rezzed, lose all credits in your credit pool. Gain credits equal to the rez cost of that ice.", "title": "Nasir Meidan: Cyber Explorer", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_the_foundry_refining_the_process_06021(Identity):
    '''
    Cost: n/a
    Text: The first time you rez a piece of ice each turn, you may search R&D for another copy of that ice, reveal it, and add it to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06021", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "tsb", "position": 21, "quantity": 3, "side_code": "corp", "stripped_text": "The first time you rez a piece of ice each turn, you may search R&D for another copy of that ice, reveal it, and add it to HQ. Shuffle R&D.", "stripped_title": "The Foundry: Refining the Process", "text": "The first time you rez a piece of ice each turn, you may search R&D for another copy of that ice, reveal it, and add it to HQ. Shuffle R&D.", "title": "The Foundry: Refining the Process", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_quetzal_free_spirit_06052(Identity):
    '''
    Cost: n/a
    Text: 0 credits: Break 1 barrier subroutine. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "06052", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"Why should we be slaves to our genetic heritage?\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "fc", "position": 52, "quantity": 3, "side_code": "runner", "stripped_text": "0 credits: Break 1 barrier subroutine. Use this ability only once per turn.", "stripped_title": "Quetzal: Free Spirit", "text": "<strong>0[credit]:</strong> Break 1 <strong>barrier</strong> subroutine. Use this ability only once per turn.", "title": "Quetzal: Free Spirit", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_blue_sun_powering_the_future_06068(Identity):
    '''
    Cost: n/a
    Text: When your turn begins, you may add 1 rezzed card to HQ and gain credits equal to its rez cost.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06068", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Unlimited Energy. Reasonable Prices.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Corp", "minimum_deck_size": 45, "pack_code": "uao", "position": 68, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may add 1 rezzed card to HQ and gain credits equal to its rez cost.", "stripped_title": "Blue Sun: Powering the Future", "text": "When your turn begins, you may add 1 rezzed card to HQ and gain credits equal to its rez cost.", "title": "Blue Sun: Powering the Future", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_leela_patel_trained_pragmatist_06095(Identity):
    '''
    Cost: n/a
    Text: Whenever an agenda is scored or stolen, add 1 unrezzed card to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "06095", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"I'd say I do it for the challenge, but the truth is it's not that hard.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "atr", "position": 95, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever an agenda is scored or stolen, add 1 unrezzed card to HQ.", "stripped_title": "Leela Patel: Trained Pragmatist", "text": "Whenever an agenda is scored or stolen, add 1 unrezzed card to HQ.", "title": "Leela Patel: Trained Pragmatist", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_industrial_genomics_growing_solutions_06105(Identity):
    '''
    Cost: n/a
    Text: The trash cost of each card is increased by 1 for each facedown card in Archives.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06105", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "Achieve the Impossible.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "ts", "position": 105, "quantity": 3, "side_code": "corp", "stripped_text": "The trash cost of each card is increased by 1 for each facedown card in Archives.", "stripped_title": "Industrial Genomics: Growing Solutions", "text": "The trash cost of each card is increased by 1 for each facedown card in Archives.", "title": "Industrial Genomics: Growing Solutions", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_argus_security_protection_guaranteed_07001(Identity):
    '''
    Cost: n/a
    Text: Whenever the Runner steals an agenda, they must take 1 tag or suffer 2 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07001", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "We Never Sleep.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Corp", "minimum_deck_size": 45, "pack_code": "oac", "position": 1, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner steals an agenda, they must take 1 tag or suffer 2 meat damage.", "stripped_title": "Argus Security: Protection Guaranteed", "text": "Whenever the Runner steals an agenda, they must take 1 tag or suffer 2 meat damage.", "title": "Argus Security: Protection Guaranteed", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_gagarin_deep_space_expanding_the_horizon_07002(Identity):
    '''
    Cost: n/a
    Text: As an additional cost to access a card in the root of a remote server, the Runner must pay 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07002", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Sic Itur Ad Astra.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Corp", "minimum_deck_size": 45, "pack_code": "oac", "position": 2, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to access a card in the root of a remote server, the Runner must pay 1 credit.", "stripped_title": "Gagarin Deep Space: Expanding the Horizon", "text": "As an additional cost to access a card in the root of a remote server, the Runner must pay 1[credit].", "title": "Gagarin Deep Space: Expanding the Horizon", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_titan_transnational_investing_in_your_future_07003(Identity):
    '''
    Cost: n/a
    Text: Whenever you score an agenda, you may place 1 agenda counter on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07003", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "The Way Forward.", "illustrator": "Emilio Rodriguez", "influence_limit": 17, "keywords": "Corp", "minimum_deck_size": 45, "pack_code": "oac", "position": 3, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you score an agenda, you may place 1 agenda counter on it.", "stripped_title": "Titan Transnational: Investing In Your Future", "text": "Whenever you score an agenda, you may place 1 agenda counter on it.", "title": "Titan Transnational: Investing In Your Future", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_edward_kim_humanitys_hammer_07028(Identity):
    '''
    Cost: n/a
    Text: Trash the first operation you access each turn at no cost.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "07028", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"My only regret is that androids cannot feel my hate.\"", "illustrator": "Adam Schumpert", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "oac", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "Trash the first operation you access each turn at no cost.", "stripped_title": "Edward Kim: Humanity's Hammer", "text": "Trash the first operation you access each turn at no cost.", "title": "Edward Kim: Humanity's Hammer", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_maxx_maximum_punk_rock_07029(Identity):
    '''
    Cost: n/a
    Text: When your turn begins, trash the top 2 cards of your stack. Draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "07029", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"**** you, mother******!\"", "illustrator": "Adam Schumpert", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "oac", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, trash the top 2 cards of your stack. Draw 1 card.", "stripped_title": "MaxX: Maximum Punk Rock", "text": "When your turn begins, trash the top 2 cards of your stack. Draw 1 card.", "title": "MaxX: Maximum Punk Rock", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_valencia_estevez_the_angel_of_cayambe_07030(Identity):
    '''
    Cost: n/a
    Text: The Corp starts the game with 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "07030", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"Everyone deserves a chance. Everyone.\"", "illustrator": "Adam Schumpert", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 50, "pack_code": "oac", "position": 30, "quantity": 3, "side_code": "runner", "stripped_text": "The Corp starts the game with 1 bad publicity.", "stripped_title": "Valencia Estevez: The Angel of Cayambe", "text": "The Corp starts the game with 1 bad publicity.", "title": "Valencia Estevez: The Angel of Cayambe", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jinteki_biotech_life_imagined_08012(Identity):
    '''
    Cost: n/a
    Text: Before taking your first turn, you may switch this identity with any copy of Jinteki Biotech. click click click: Flip this identity. The Brewery: When you flip this identity, do 2 net damage. The Tank: When you flip this identity, shuffle all cards in Archives into R&D. The Greenhouse: When you flip this identity, place 4 advancement counters on 1 installed card that you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08012", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "val", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "Before taking your first turn, you may switch this identity with any copy of Jinteki Biotech. click click click: Flip this identity. The Brewery: When you flip this identity, do 2 net damage. The Tank: When you flip this identity, shuffle all cards in Archives into R&D. The Greenhouse: When you flip this identity, place 4 advancement counters on 1 installed card that you can advance.", "stripped_title": "Jinteki Biotech: Life Imagined", "text": "Before taking your first turn, you may switch this identity with any copy of Jinteki Biotech.\n<strong>[click][click][click]:</strong> Flip this identity.\nThe Brewery: When you flip this identity, do 2 net damage.\nThe Tank: When you flip this identity, shuffle all cards in Archives into R&D.\nThe Greenhouse: When you flip this identity, place 4 advancement counters on 1 installed card that you can advance.", "title": "Jinteki Biotech: Life Imagined", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_hayley_kaplan_universal_scholar_08025(Identity):
    '''
    Cost: n/a
    Text: The first time you install a card each turn, you may install another card of the same type from your grip (paying its install cost).
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "08025", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "bb", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you install a card each turn, you may install another card of the same type from your grip (paying its install cost).", "stripped_title": "Hayley Kaplan: Universal Scholar", "text": "The first time you install a card each turn, you may install another card of the same type from your grip (paying its install cost).", "title": "Hayley Kaplan: Universal Scholar", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_cybernetics_division_humanity_upgraded_08050(Identity):
    '''
    Cost: n/a
    Text: Each player's maximum hand size is reduced by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08050", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Define Yourself.", "illustrator": "Greg Semkow", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 40, "pack_code": "cc", "position": 50, "quantity": 3, "side_code": "corp", "stripped_text": "Each player's maximum hand size is reduced by 1.", "stripped_title": "Cybernetics Division: Humanity Upgraded", "text": "Each player's maximum hand size is reduced by 1.", "title": "Cybernetics Division: Humanity Upgraded", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_armand_geist_walker_tech_lord_08063(Identity):
    '''
    Cost: n/a
    Text: Whenever you use a trash ability, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "08063", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"Everything has a price.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "uw", "position": 63, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you use a trash ability, draw 1 card.", "stripped_title": "Armand \"Geist\" Walker: Tech Lord", "text": "Whenever you use a [trash] ability, draw 1 card.", "title": "Armand \"Geist\" Walker: Tech Lord", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_haarpsichord_studios_entertainment_unleashed_08092(Identity):
    '''
    Cost: n/a
    Text: The Runner cannot steal more than one agenda each turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08092", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Home of Your Imagination.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "oh", "position": 92, "quantity": 3, "side_code": "corp", "stripped_text": "The Runner cannot steal more than one agenda each turn.", "stripped_title": "Haarpsichord Studios: Entertainment Unleashed", "text": "The Runner cannot steal more than one agenda each turn.", "title": "Haarpsichord Studios: Entertainment Unleashed", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_laramy_fisk_savvy_investor_08104(Identity):
    '''
    Cost: n/a
    Text: The first time you make a successful run on a central server each turn, you may force the Corp to draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "08104", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "uot", "position": 104, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you make a successful run on a central server each turn, you may force the Corp to draw 1 card.", "stripped_title": "Laramy Fisk: Savvy Investor", "text": "The first time you make a successful run on a central server each turn, you may force the Corp to draw 1 card.", "title": "Laramy Fisk: Savvy Investor", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_chronos_protocol_selective_mindmapping_08111(Identity):
    '''
    Cost: n/a
    Text: For the first net damage the Runner suffers each turn, you may look at the Runner's grip and select the card that is trashed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08111", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "uot", "position": 111, "quantity": 3, "side_code": "corp", "stripped_text": "For the first net damage the Runner suffers each turn, you may look at the Runner's grip and select the card that is trashed.", "stripped_title": "Chronos Protocol: Selective Mind-mapping", "text": "For the first net damage the Runner suffers each turn, you may look at the Runner's grip and select the card that is trashed.", "title": "Chronos Protocol: Selective Mind-mapping", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_sync_everything_everywhere_09001(Identity):
    '''
    Cost: n/a
    Text: click: Flip this identity. The Runner pays 1 credit more when spending a click to remove a tag (not through a card ability). Flip side: click: Flip this identity. You may pay 2 credits fewer when spending a click to trash a resource (not through a card ability).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09001", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Maciej Rebisz", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 40, "pack_code": "dad", "position": 1, "quantity": 3, "side_code": "corp", "stripped_text": "click: Flip this identity. The Runner pays 1 credit more when spending a click to remove a tag (not through a card ability). Flip side: click: Flip this identity. You may pay 2 credits fewer when spending a click to trash a resource (not through a card ability).", "stripped_title": "SYNC: Everything, Everywhere", "text": "[click]: Flip this identity.\nThe Runner pays 1[credit] more when spending a [click] to remove a tag (not through a card ability).\nFlip side:\n[click]: Flip this identity.\nYou may pay 2[credit] fewer when spending a [click] to trash a resource (not through a card ability).", "title": "SYNC: Everything, Everywhere", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_new_angeles_sol_your_news_09002(Identity):
    '''
    Cost: n/a
    Text: Whenever an agenda is scored or stolen, you may play 1 current from HQ or Archives (paying its play cost).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09002", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Nothing but the Truth.", "illustrator": "Maciej Rebisz", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "dad", "position": 2, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever an agenda is scored or stolen, you may play 1 current from HQ or Archives (paying its play cost).", "stripped_title": "New Angeles Sol: Your News", "text": "Whenever an agenda is scored or stolen, you may play 1 <strong>current</strong> from HQ or Archives (paying its play cost).", "title": "New Angeles Sol: Your News", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_spark_agency_worldswide_reach_09003(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you rez an advertisement, the Runner loses 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09003", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "We're ready to start the fire.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "dad", "position": 3, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn you rez an advertisement, the Runner loses 1 credit.", "stripped_title": "Spark Agency: Worldswide Reach", "text": "The first time each turn you rez an <strong>advertisement</strong>, the Runner loses 1[credit].", "title": "Spark Agency: Worldswide Reach", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_apex_invasive_predator_09029(Identity):
    '''
    Cost: n/a
    Text: You cannot install non-virtual resources. When your turn begins, you may install 1 card from your grip facedown.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "09029", "deck_limit": 1, "faction_code": "apex", "faction_cost": 0, "illustrator": "Liiga Smilshkalne", "influence_limit": 25, "keywords": "Digital", "minimum_deck_size": 45, "pack_code": "dad", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "You cannot install non-virtual resources. When your turn begins, you may install 1 card from your grip facedown.", "stripped_title": "Apex: Invasive Predator", "text": "You cannot install non-<strong>virtual</strong> resources.\nWhen your turn begins, you may install 1 card from your grip facedown.", "title": "Apex: Invasive Predator", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_adam_compulsive_hacker_09037(Identity):
    '''
    Cost: n/a
    Text: You start the game with 3 different directive cards installed (these cards are not considered part of your deck).
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "09037", "deck_limit": 1, "faction_code": "adam", "faction_cost": 0, "illustrator": "Matt Zeilinger", "influence_limit": 25, "keywords": "Bioroid", "minimum_deck_size": 45, "pack_code": "dad", "position": 37, "quantity": 3, "side_code": "runner", "stripped_text": "You start the game with 3 different directive cards installed (these cards are not considered part of your deck).", "stripped_title": "Adam: Compulsive Hacker", "text": "You start the game with 3 different <strong>directive</strong> cards installed (these cards are not considered part of your deck).", "title": "Adam: Compulsive Hacker", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_sunny_lebeau_security_specialist_09045(Identity):
    '''
    Cost: n/a
    Text: n/a
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 2, "code": "09045", "deck_limit": 1, "faction_code": "sunny-lebeau", "faction_cost": 0, "flavor": "\"Mommy will be home soon, sweetie. She has to kick some ass first.\"", "illustrator": "Matt Zeilinger", "influence_limit": 25, "keywords": "Natural", "minimum_deck_size": 50, "pack_code": "dad", "position": 45, "quantity": 3, "side_code": "runner", "stripped_title": "Sunny Lebeau: Security Specialist", "title": "Sunny Lebeau: Security Specialist", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jesminder_sareen_girl_behind_the_curtain_10006(Identity):
    '''
    Cost: n/a
    Text: Interrupt -> The first time each run you would take 1 or more tags, prevent 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "10006", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"Mirrormode on.\"", "illustrator": "Adam Schumpert", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "kg", "position": 6, "quantity": 3, "side_code": "runner", "stripped_text": "Interrupt -> The first time each run you would take 1 or more tags, prevent 1 tag.", "stripped_title": "Jesminder Sareen: Girl Behind the Curtain", "text": "[interrupt] \u2192 The first time each run you would take 1 or more tags, prevent 1 tag.", "title": "Jesminder Sareen: Girl Behind the Curtain", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_palana_foods_sustainable_growth_10030(Identity):
    '''
    Cost: n/a
    Text: The first time each turn the Runner draws a card, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10030", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "We Are What We Eat.\u00a0", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "bf", "position": 30, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn the Runner draws a card, gain 1 credit.", "stripped_title": "Palana Foods: Sustainable Growth", "text": "The first time each turn the Runner draws a card, gain 1[credit].", "title": "P\u0101lan\u0101 Foods: Sustainable Growth", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nero_severn_information_broker_10040(Identity):
    '''
    Cost: n/a
    Text: Once per turn, you may jack out when you encounter a sentry.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "10040", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"Credits spend anywhere in the worlds, but there are other forms of currency.\"", "illustrator": "Adam Schumpert", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "dag", "position": 40, "quantity": 3, "side_code": "runner", "stripped_text": "Once per turn, you may jack out when you encounter a sentry.", "stripped_title": "Nero Severn: Information Broker", "text": "Once per turn, you may jack out when you encounter a <strong>sentry</strong>.", "title": "Nero Severn: Information Broker", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_harishchandra_ent_where_youre_the_star_10107(Identity):
    '''
    Cost: n/a
    Text: While the Runner is tagged, they play with the grip revealed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10107", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "We Know What You Want.", "illustrator": "Emilio Rodriguez", "influence_limit": 17, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "ftm", "position": 107, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is tagged, they play with the grip revealed.", "stripped_title": "Harishchandra Ent.: Where You're the Star", "text": "While the Runner is tagged, they play with the grip revealed.", "title": "Harishchandra Ent.: Where You're the Star", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_null_whistleblower_11002(Identity):
    '''
    Cost: n/a
    Text: Once per turn, when you encounter a piece of ice, you may trash 1 card from your grip. If you do, that ice has -2 strength for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "11002", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "23s", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "Once per turn, when you encounter a piece of ice, you may trash 1 card from your grip. If you do, that ice has -2 strength for the remainder of this run.", "stripped_title": "Null: Whistleblower", "text": "Once per turn, when you encounter a piece of ice, you may trash 1 card from your grip. If you do, that ice has -2 strength for the remainder of this run.", "title": "Null: Whistleblower", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nbn_controlling_the_message_11017(Identity):
    '''
    Cost: n/a
    Text: The first time the Runner trashes an installed Corp card each turn, you may trace[4]. If successful, give the Runner 1 tag (cannot be avoided).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11017", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "influence_limit": 12, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "23s", "position": 17, "quantity": 3, "side_code": "corp", "stripped_text": "The first time the Runner trashes an installed Corp card each turn, you may trace[4]. If successful, give the Runner 1 tag (cannot be avoided).", "stripped_title": "NBN: Controlling the Message", "text": "The first time the Runner trashes an installed Corp card each turn, you may trace[4]. If successful, give the Runner 1 tag (cannot be avoided).", "title": "NBN: Controlling the Message", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_khan_savvy_skiptracer_11027(Identity):
    '''
    Cost: n/a
    Text: The first time you pass a piece of ice each turn, you may install an icebreaker from your hand, lowering the install cost by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "11027", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "illustrator": "Matt Zeilinger", "influence_limit": 12, "keywords": "Natural", "minimum_deck_size": 40, "pack_code": "bm", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you pass a piece of ice each turn, you may install an icebreaker from your hand, lowering the install cost by 1.", "stripped_title": "Khan: Savvy Skiptracer", "text": "The first time you pass a piece of ice each turn, you may install an <strong>icebreaker</strong> from your hand, lowering the install cost by 1.", "title": "Khan: Savvy Skiptracer", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_weyland_consortium_builder_of_nations_11038(Identity):
    '''
    Cost: n/a
    Text: The first time each turn an encounter with an advanced piece of ice ends, do 1 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11038", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Strength makes leaders.", "influence_limit": 12, "keywords": "Megacorp", "minimum_deck_size": 40, "pack_code": "bm", "position": 38, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn an encounter with an advanced piece of ice ends, do 1 meat damage.", "stripped_title": "Weyland Consortium: Builder of Nations", "text": "The first time each turn an encounter with an advanced piece of ice ends, do 1 meat damage.", "title": "Weyland Consortium: Builder of Nations", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_omar_keung_conspiracy_theorist_11043(Identity):
    '''
    Cost: n/a
    Text: click: Run Archives. If that run would be declared successful, change the attacked server to HQ or R&D for the remainder of that run. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "11043", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "illustrator": "Matt Zeilinger", "influence_limit": 12, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "es", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "click: Run Archives. If that run would be declared successful, change the attacked server to HQ or R&D for the remainder of that run. Use this ability only once per turn.", "stripped_title": "Omar Keung: Conspiracy Theorist", "text": "<strong>[click]:</strong> Run Archives. If that run would be declared successful, change the attacked server to HQ or R&D for the remainder of that run. Use this ability only once per turn.", "title": "Omar Keung: Conspiracy Theorist", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jinteki_potential_unleashed_11054(Identity):
    '''
    Cost: n/a
    Text: Whenever the Runner takes at least 1 net damage, trash the top card of the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11054", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "Your better nature.", "influence_limit": 12, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "es", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner takes at least 1 net damage, trash the top card of the stack.", "stripped_title": "Jinteki: Potential Unleashed", "text": "Whenever the Runner takes at least 1 net damage, trash the top card of the stack.", "title": "Jinteki: Potential Unleashed", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_ele_smoke_scovak_cynosure_of_the_net_11066(Identity):
    '''
    Cost: n/a
    Text: 1 recurring credit Use this credit to pay for using icebreakers.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "11066", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"Nothing up my sleeve...\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "G-mod - Stealth", "minimum_deck_size": 40, "pack_code": "in", "position": 66, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to pay for using icebreakers.", "stripped_title": "Ele \"Smoke\" Scovak: Cynosure of the Net", "text": "1[recurring-credit]\nUse this credit to pay for using <strong>icebreakers</strong>.", "title": "Ele \"Smoke\" Scovak: Cynosure of the Net", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_haasbioroid_architects_of_tomorrow_11072(Identity):
    '''
    Cost: n/a
    Text: The first time each turn the Runner passes a rezzed piece of bioroid ice, you may rez 1 bioroid card, paying 4 credits less.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11072", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "influence_limit": 12, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "in", "position": 72, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn the Runner passes a rezzed piece of bioroid ice, you may rez 1 bioroid card, paying 4 credits less.", "stripped_title": "Haas-Bioroid: Architects of Tomorrow", "text": "The first time each turn the Runner passes a rezzed piece of <strong>bioroid</strong> ice, you may rez 1 <strong>bioroid</strong> card, paying 4[credit] less.", "title": "Haas-Bioroid: Architects of Tomorrow", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jemison_astronautics_sacrifice_audacity_success_12016(Identity):
    '''
    Cost: n/a
    Text: Whenever you forfeit an agenda, place X advancement counters on 1 installed card. X is equal to the agenda point value of the forfeited agenda plus 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12016", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Corp", "minimum_deck_size": 45, "pack_code": "dc", "position": 16, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you forfeit an agenda, place X advancement counters on 1 installed card. X is equal to the agenda point value of the forfeited agenda plus 1.", "stripped_title": "Jemison Astronautics: Sacrifice. Audacity. Success.", "text": "Whenever you forfeit an agenda, place X advancement counters on 1 installed card. X is equal to the agenda point value of the forfeited agenda plus 1.", "title": "Jemison Astronautics: Sacrifice. Audacity. Success.", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_los_data_hijacker_12025(Identity):
    '''
    Cost: n/a
    Text: The first time the Corp rezzes a piece of ice each turn, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "12025", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"From code to profit in three easy steps.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "so", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "The first time the Corp rezzes a piece of ice each turn, gain 2 credits.", "stripped_title": "Los: Data Hijacker", "text": "The first time the Corp rezzes a piece of ice each turn, gain 2[credit].", "title": "Los: Data Hijacker", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_aginfusion_new_miracles_for_a_new_world_12052(Identity):
    '''
    Cost: n/a
    Text: Trash the unrezzed piece of ice the Runner is approaching: Choose a server other than the attacked server. The Runner moves to the outermost position of that server and encounters any ice there. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12052", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 17, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "eas", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "Trash the unrezzed piece of ice the Runner is approaching: Choose a server other than the attacked server. The Runner moves to the outermost position of that server and encounters any ice there. Use this ability only once per turn.", "stripped_title": "AgInfusion: New Miracles for a New World", "text": "<strong>Trash the unrezzed piece of ice the Runner is approaching:</strong> Choose a server other than the attacked server. The Runner moves to the outermost position of that server and encounters any ice there. Use this ability only once per turn.", "title": "AgInfusion: New Miracles for a New World", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_alice_merchant_clan_agitator_12061(Identity):
    '''
    Cost: n/a
    Text: The first time you make a successful run on Archives each turn, the Corp must trash 1 card from HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "12061", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "Jarogniew's agent provocateur.", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 50, "pack_code": "baw", "position": 61, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you make a successful run on Archives each turn, the Corp must trash 1 card from HQ.", "stripped_title": "Alice Merchant: Clan Agitator", "text": "The first time you make a successful run on Archives each turn, the Corp must trash 1 card from HQ.", "title": "Alice Merchant: Clan Agitator", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_steve_cambridge_master_grifter_13001(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you make a successful run on HQ, you may choose 2 cards in your heap. If you do, the Corp removes 1 of those cards from the game, then you add the other card to your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "13001", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "illustrator": "Adam Schumpert", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "td", "position": 1, "quantity": 1, "side_code": "runner", "stripped_text": "The first time each turn you make a successful run on HQ, you may choose 2 cards in your heap. If you do, the Corp removes 1 of those cards from the game, then you add the other card to your grip.", "stripped_title": "Steve Cambridge: Master Grifter", "text": "The first time each turn you make a successful run on HQ, you may choose 2 cards in your heap. If you do, the Corp removes 1 of those cards from the game, then you add the other card to your grip.", "title": "Steve Cambridge: Master Grifter", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_ayla_bios_rahim_simulant_specialist_13012(Identity):
    '''
    Cost: n/a
    Text: Before drawing your starting hand, set aside the top 6 cards of your stack facedown. (You may look at those cards at any time.) Shuffle 2 of those cards into your stack. click: Add 1 card set aside with this identity to your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "13012", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "illustrator": "Adam Schumpert", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "td", "position": 12, "quantity": 1, "side_code": "runner", "stripped_text": "Before drawing your starting hand, set aside the top 6 cards of your stack facedown. (You may look at those cards at any time.) Shuffle 2 of those cards into your stack. click: Add 1 card set aside with this identity to your grip.", "stripped_title": "Ayla \"Bios\" Rahim: Simulant Specialist", "text": "Before drawing your starting hand, set aside the top 6 cards of your stack facedown. <em>(You may look at those cards at any time.)</em> Shuffle 2 of those cards into your stack.\n[click]<strong>:</strong> Add 1 card set aside with this identity to your grip.", "title": "Ayla \"Bios\" Rahim: Simulant Specialist", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_seidr_laboratories_destiny_defined_13028(Identity):
    '''
    Cost: n/a
    Text: The first time each turn the Runner loses or spends click during a run, you may add 1 card from Archives to the top of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13028", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Interweaving the Past and the Future.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "td", "position": 28, "quantity": 1, "side_code": "corp", "stripped_text": "The first time each turn the Runner loses or spends click during a run, you may add 1 card from Archives to the top of R&D.", "stripped_title": "Seidr Laboratories: Destiny Defined", "text": "The first time each turn the Runner loses or spends [click] during a run, you may add 1 card from Archives to the top of R&D.", "title": "Seidr Laboratories: Destiny Defined", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_skorpios_defense_systems_persuasive_power_13041(Identity):
    '''
    Cost: n/a
    Text: Interrupt -> Whenever 1 or more Runner cards would be trashed (from any location), set those cards aside instead of adding them to the heap. You can look at those cards. You may remove 1 of them from the game. Then, add all of those cards that are still set aside to the heap. Ignore this ability if you have already removed a card from the game with it this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13041", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Might makes right.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Subsidiary", "minimum_deck_size": 40, "pack_code": "td", "position": 41, "quantity": 1, "side_code": "corp", "stripped_text": "Interrupt -> Whenever 1 or more Runner cards would be trashed (from any location), set those cards aside instead of adding them to the heap. You can look at those cards. You may remove 1 of them from the game. Then, add all of those cards that are still set aside to the heap. Ignore this ability if you have already removed a card from the game with it this turn.", "stripped_title": "Skorpios Defense Systems: Persuasive Power", "text": "[interrupt] \u2192 Whenever 1 or more Runner cards would be trashed <em>(from any location)</em>, set those cards aside instead of adding them to the heap. You can look at those cards. You may remove 1 of them from the game. Then, add all of those cards that are still set aside to the heap. Ignore this ability if you have already removed a card from the game with it this turn.", "title": "Skorpios Defense Systems: Persuasive Power", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_reina_roja_freedom_fighter_20001(Identity):
    '''
    Cost: n/a
    Text: The first piece of ice the Corp rezzes each turn costs 1 credit more to rez.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "20001", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"Analyzing the board won't help. Your mistake was thinking we're playing the same game.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Cyborg - G-mod", "minimum_deck_size": 45, "pack_code": "core2", "position": 1, "quantity": 1, "side_code": "runner", "stripped_text": "The first piece of ice the Corp rezzes each turn costs 1 credit more to rez.", "stripped_title": "Reina Roja: Freedom Fighter", "text": "The first piece of ice the Corp rezzes each turn costs 1[credit] more to rez.", "title": "Reina Roja: Freedom Fighter", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_gabriel_santiago_consummate_professional_20019(Identity):
    '''
    Cost: n/a
    Text: The first time you make a successful run on HQ each turn, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "20019", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"Of course I steal from the rich. They're the ones with all the money.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "core2", "position": 19, "quantity": 1, "side_code": "runner", "stripped_text": "The first time you make a successful run on HQ each turn, gain 2 credits.", "stripped_title": "Gabriel Santiago: Consummate Professional", "text": "The first time you make a successful run on HQ each turn, gain 2[credit].", "title": "Gabriel Santiago: Consummate Professional", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_chaos_theory_wunderkind_20037(Identity):
    '''
    Cost: n/a
    Text: +1 mu
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "20037", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"Have you met Dinosaurus?\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 40, "pack_code": "core2", "position": 37, "quantity": 1, "side_code": "runner", "stripped_text": "+1 mu", "stripped_title": "Chaos Theory: Wunderkind", "text": "+1[mu]", "title": "Chaos Theory: W\u00fcnderkind", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_haasbioroid_stronger_together_20061(Identity):
    '''
    Cost: n/a
    Text: All bioroid ice has +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20061", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "A Different Breed of Machine.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "core2", "position": 61, "quantity": 1, "side_code": "corp", "stripped_text": "All bioroid ice has +1 strength.", "stripped_title": "Haas-Bioroid: Stronger Together", "text": "All <strong>bioroid</strong> ice has +1 strength.", "title": "Haas-Bioroid: Stronger Together", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_weyland_consortium_building_a_better_world_20077(Identity):
    '''
    Cost: n/a
    Text: Whenever you play a transaction operation, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20077", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Moving Upwards.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "core2", "position": 108, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever you play a transaction operation, gain 1 credit.", "stripped_title": "Weyland Consortium: Building a Better World", "text": "Whenever you play a <strong>transaction</strong> operation, gain 1[credit].", "title": "Weyland Consortium: Building a Better World", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jinteki_personal_evolution_20093(Identity):
    '''
    Cost: n/a
    Text: Whenever an agenda is scored or stolen, do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20093", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "When You Need the Human Touch.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "core2", "position": 77, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever an agenda is scored or stolen, do 1 net damage.", "stripped_title": "Jinteki: Personal Evolution", "text": "Whenever an agenda is scored or stolen, do 1 net damage.", "title": "Jinteki: Personal Evolution", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nbn_making_news_20109(Identity):
    '''
    Cost: n/a
    Text: 2 recurring credits Use these credits during trace attempts.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20109", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Someone is Always Watching.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "core2", "position": 93, "quantity": 1, "side_code": "corp", "stripped_text": "2 recurring credits Use these credits during trace attempts.", "stripped_title": "NBN: Making News", "text": "2[recurring-credit]\nUse these credits during trace attempts.", "title": "NBN: Making News", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_asa_group_security_through_vigilance_21009(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you install a card, you may install 1 non-agenda card from HQ in the root of or protecting the same server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21009", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Johan T\u00f6rnlund", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "ss", "position": 9, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn you install a card, you may install 1 non-agenda card from HQ in the root of or protecting the same server.", "stripped_title": "Asa Group: Security Through Vigilance", "text": "The first time each turn you install a card, you may install 1 non-agenda card from HQ in the root of or protecting the same server.", "title": "Asa Group: Security Through Vigilance", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_kabonesa_wu_netspace_thrillseeker_21025(Identity):
    '''
    Cost: n/a
    Text: click: Search your stack for a non-virus program and install it, lowering its install cost by 1 credit, then shuffle your stack. If that program is still installed when your turn ends, remove it from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "21025", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "illustrator": "Antonio De Luca", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "dtwn", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "click: Search your stack for a non-virus program and install it, lowering its install cost by 1 credit, then shuffle your stack. If that program is still installed when your turn ends, remove it from the game.", "stripped_title": "Kabonesa Wu: Netspace Thrillseeker", "text": "[click]: Search your stack for a non-<strong>virus</strong> program and install it, lowering its install cost by 1[credit], then shuffle your stack. If that program is still installed when your turn ends, remove it from the game.", "title": "Kabonesa Wu: Netspace Thrillseeker", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_azmari_edtech_shaping_the_future_21054(Identity):
    '''
    Cost: n/a
    Text: When your turn ends, you may name a card type. Gain 2 credits the first time each turn the Runner plays or installs a card that has the type you last named this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21054", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 40, "pack_code": "cotc", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn ends, you may name a card type. Gain 2 credits the first time each turn the Runner plays or installs a card that has the type you last named this way.", "stripped_title": "Azmari EdTech: Shaping the Future", "text": "When your turn ends, you may name a card type. Gain 2[credit] the first time each turn the Runner plays or installs a card that has the type you last named this way.", "title": "Azmari EdTech: Shaping the Future", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_419_amoral_scammer_21063(Identity):
    '''
    Cost: n/a
    Text: The first time the Corp installs a card each turn, you may expose that card unless the Corp pays 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "21063", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"Is there anything better than free money?\"", "illustrator": "Antonio De Luca", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "tdatd", "position": 63, "quantity": 3, "side_code": "runner", "stripped_text": "The first time the Corp installs a card each turn, you may expose that card unless the Corp pays 1 credit.", "stripped_title": "419: Amoral Scammer", "text": "The first time the Corp installs a card each turn, you may expose that card unless the Corp pays 1[credit].", "title": "419: Amoral Scammer", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_sso_industries_fueling_innovation_21077(Identity):
    '''
    Cost: n/a
    Text: When your turn ends, you may choose a piece of ice with no advancement tokens on it. If you do, place 1 advancement token on that piece of ice for each agenda point on all installed faceup agendas.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21077", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Johan T\u00f6rnlund", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "tdatd", "position": 77, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn ends, you may choose a piece of ice with no advancement tokens on it. If you do, place 1 advancement token on that piece of ice for each agenda point on all installed faceup agendas.", "stripped_title": "SSO Industries: Fueling Innovation", "text": "When your turn ends, you may choose a piece of ice with no advancement tokens on it. If you do, place 1 advancement token on that piece of ice for each agenda point on all installed faceup agendas.", "title": "SSO Industries: Fueling Innovation", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_freedom_khumalo_cryptoanarchist_21081(Identity):
    '''
    Cost: n/a
    Text: Access -> Any X virus counters: Trash the non-agenda card you are accessing. X is equal to that card's rez or play cost. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "21081", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "illustrator": "Antonio De Luca", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "win", "position": 81, "quantity": 3, "side_code": "runner", "stripped_text": "Access -> Any X virus counters: Trash the non-agenda card you are accessing. X is equal to that card's rez or play cost. Use this ability only once per turn.", "stripped_title": "Freedom Khumalo: Crypto-Anarchist", "text": "Access \u2192 <strong>Any X virus counters:</strong> Trash the non-agenda card you are accessing. X is equal to that card's rez or play cost. Use this ability only once per turn.", "title": "Freedom Khumalo: Crypto-Anarchist", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_mti_mwekundu_life_improved_21114(Identity):
    '''
    Cost: n/a
    Text: Whenever the Runner approaches a server, you may install 1 piece of ice from HQ in the innermost position protecting that server, ignoring all costs. The Runner moves to that ice and approaches it. If this is not the first time they have approached a piece of ice this run, they may jack out. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21114", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "ka", "position": 114, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner approaches a server, you may install 1 piece of ice from HQ in the innermost position protecting that server, ignoring all costs. The Runner moves to that ice and approaches it. If this is not the first time they have approached a piece of ice this run, they may jack out. Use this ability only once per turn.", "stripped_title": "Mti Mwekundu: Life Improved", "text": "Whenever the Runner approaches a server, you may install 1 piece of ice from HQ in the innermost position protecting that server, ignoring all costs. The Runner moves to that ice and approaches it. If this is not the first time they have approached a piece of ice this run, they may jack out. Use this ability only once per turn.", "title": "Mti Mwekundu: Life Improved", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nathaniel_gnat_hall_oneofakind_22001(Identity):
    '''
    Cost: n/a
    Text: When your turn begins, gain 1 credit if you have 2 or fewer cards in your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "22001", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"Damn, I'm good.\"", "illustrator": "Matt Zeilinger, A. Christensen", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 40, "pack_code": "rar", "position": 1, "quantity": 1, "side_code": "runner", "stripped_text": "When your turn begins, gain 1 credit if you have 2 or fewer cards in your grip.", "stripped_title": "Nathaniel \"Gnat\" Hall: One-of-a-Kind", "text": "When your turn begins, gain 1[credit] if you have 2 or fewer cards in your grip.", "title": "Nathaniel \"Gnat\" Hall: One-of-a-Kind", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_liza_talking_thunder_prominent_legislator_22008(Identity):
    '''
    Cost: n/a
    Text: The first time you make a successful run on a central server each turn, draw 2 cards and take 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "22008", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"You think you're the first to come after me?\"", "illustrator": "Matt Zeilinger, A. Christensen", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 50, "pack_code": "rar", "position": 8, "quantity": 1, "side_code": "runner", "stripped_text": "The first time you make a successful run on a central server each turn, draw 2 cards and take 1 tag.", "stripped_title": "Liza Talking Thunder: Prominent Legislator", "text": "The first time you make a successful run on a central server each turn, draw 2 cards and take 1 tag.", "title": "Liza Talking Thunder: Prominent Legislator", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_akiko_nisei_head_case_22015(Identity):
    '''
    Cost: n/a
    Text: Whenever you breach R&D, you and the Corp secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Corp spent the same number of credits, access 1 additional card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "22015", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "illustrator": "Matt Zeilinger, A. Christensen", "influence_limit": 12, "keywords": "Clone", "minimum_deck_size": 45, "pack_code": "rar", "position": 15, "quantity": 1, "side_code": "runner", "stripped_text": "Whenever you breach R&D, you and the Corp secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Corp spent the same number of credits, access 1 additional card.", "stripped_title": "Akiko Nisei: Head Case", "text": "Whenever you breach R&D, you and the Corp secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Corp spent the same number of credits, access 1 additional card.", "title": "Akiko Nisei: Head Case", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_sportsmetal_go_big_or_go_home_22026(Identity):
    '''
    Cost: n/a
    Text: Whenever an agenda is scored or stolen, gain 2 credits or draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22026", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Want It More.", "illustrator": "Viniciusde S Menezes", "influence_limit": 15, "keywords": "Subsidiary", "minimum_deck_size": 45, "pack_code": "rar", "position": 26, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever an agenda is scored or stolen, gain 2 credits or draw 2 cards.", "stripped_title": "Sportsmetal: Go Big or Go Home", "text": "Whenever an agenda is scored or stolen, gain 2[credit] or draw 2 cards.", "title": "Sportsmetal: Go Big or Go Home", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_saraswati_mnemonics_endless_exploration_22034(Identity):
    '''
    Cost: n/a
    Text: click, 1 credit: Install 1 card from HQ in the root of a remote server, then place 1 advancement counter on it. You cannot score or rez that card until your next turn begins.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22034", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Ben Zweifel", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "rar", "position": 34, "quantity": 1, "side_code": "corp", "stripped_text": "click, 1 credit: Install 1 card from HQ in the root of a remote server, then place 1 advancement counter on it. You cannot score or rez that card until your next turn begins.", "stripped_title": "Saraswati Mnemonics: Endless Exploration", "text": "<strong>[click]</strong>, <strong>1[credit]:</strong> Install 1 card from HQ in the root of a remote server, then place 1 advancement counter on it. You cannot score or rez that card until your next turn begins.", "title": "Saraswati Mnemonics: Endless Exploration", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_acme_consulting_the_truth_you_need_22042(Identity):
    '''
    Cost: n/a
    Text: The Runner is considered to have 1 additional tag (even if they have 0) during encounters with the outermost piece of ice protecting any server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22042", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Subsidiary", "minimum_deck_size": 45, "pack_code": "rar", "position": 42, "quantity": 1, "side_code": "corp", "stripped_text": "The Runner is considered to have 1 additional tag (even if they have 0) during encounters with the outermost piece of ice protecting any server.", "stripped_title": "Acme Consulting: The Truth You Need", "text": "The Runner is considered to have 1 additional tag (even if they have 0) during encounters with the outermost piece of ice protecting any server.", "title": "Acme Consulting: The Truth You Need", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_the_outfit_family_owned_and_operated_22050(Identity):
    '''
    Cost: n/a
    Text: Gain 3 credits whenever you take at least 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22050", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "We do things our way.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Subsidiary", "minimum_deck_size": 45, "pack_code": "rar", "position": 50, "quantity": 1, "side_code": "corp", "stripped_text": "Gain 3 credits whenever you take at least 1 bad publicity.", "stripped_title": "The Outfit: Family Owned and Operated", "text": "Gain 3[credit] whenever you take at least 1 bad publicity.", "title": "The Outfit: Family Owned and Operated", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_cyber_bureau_keeping_the_peace_24001(Identity):
    '''
    Cost: n/a
    Text: You draw a starting hand of 10 cards. Before taking your first turn, install up to 5 cards, ignoring all install costs. Rez any number of them, lowering the total rez cost among all cards by 20. Flip this identity. Detective's Bureau: Upholding the Law The first time the Runner initiates a run each turn, force the Runner to lose 1 credit for each agenda point in his or her score area, then you gain 1 credit for each credit lost. click: Gain 3 credits or draw 3 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "24001", "deck_limit": 1, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Amelie Hutt, Dmitry Burmak", "influence_limit": null, "keywords": "Police Department", "minimum_deck_size": 40, "pack_code": "napd", "position": 1, "quantity": 1, "side_code": "corp", "stripped_text": "You draw a starting hand of 10 cards. Before taking your first turn, install up to 5 cards, ignoring all install costs. Rez any number of them, lowering the total rez cost among all cards by 20. Flip this identity. Detective's Bureau: Upholding the Law The first time the Runner initiates a run each turn, force the Runner to lose 1 credit for each agenda point in his or her score area, then you gain 1 credit for each credit lost. click: Gain 3 credits or draw 3 cards.", "stripped_title": "Cyber Bureau: Keeping the Peace", "text": "You draw a starting hand of 10 cards.\nBefore taking your first turn, install up to 5 cards, ignoring all install costs. Rez any number of them, lowering the total rez cost among all cards by 20. Flip this identity.\nDetective's Bureau: Upholding the Law\nThe first time the Runner initiates a run each turn, force the Runner to lose 1[credit] for each agenda point in his or her score area, then you gain 1[credit] for each credit lost.\n[click]: Gain 3[credit] or draw 3 cards.", "title": "Cyber Bureau: Keeping the Peace", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_reina_roja_freedom_fighter_25001(Identity):
    '''
    Cost: n/a
    Text: The first piece of ice the Corp rezzes each turn costs 1 credit more to rez.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "25001", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"Analyzing the board won't help. Your mistake was thinking we're playing the same game.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Cyborg - G-mod", "minimum_deck_size": 45, "pack_code": "sc19", "position": 1, "quantity": 1, "side_code": "runner", "stripped_text": "The first piece of ice the Corp rezzes each turn costs 1 credit more to rez.", "stripped_title": "Reina Roja: Freedom Fighter", "text": "The first piece of ice the Corp rezzes each turn costs 1[credit] more to rez.", "title": "Reina Roja: Freedom Fighter", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_quetzal_free_spirit_25002(Identity):
    '''
    Cost: n/a
    Text: 0 credits: Break 1 barrier subroutine. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "25002", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "\"Why should we be slaves to our genetic heritage?\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "sc19", "position": 2, "quantity": 1, "side_code": "runner", "stripped_text": "0 credits: Break 1 barrier subroutine. Use this ability only once per turn.", "stripped_title": "Quetzal: Free Spirit", "text": "<strong>0[credit]:</strong> Break 1 <strong>barrier</strong> subroutine. Use this ability only once per turn.", "title": "Quetzal: Free Spirit", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_gabriel_santiago_consummate_professional_25020(Identity):
    '''
    Cost: n/a
    Text: The first time you make a successful run on HQ each turn, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "25020", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"Of course I steal from the rich. They're the ones with all the money.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "sc19", "position": 20, "quantity": 1, "side_code": "runner", "stripped_text": "The first time you make a successful run on HQ each turn, gain 2 credits.", "stripped_title": "Gabriel Santiago: Consummate Professional", "text": "The first time you make a successful run on HQ each turn, gain 2[credit].", "title": "Gabriel Santiago: Consummate Professional", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_leela_patel_trained_pragmatist_25021(Identity):
    '''
    Cost: n/a
    Text: Whenever an agenda is scored or stolen, add 1 unrezzed card to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "25021", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"I'd say I do it for the challenge, but the truth is it's not that hard.\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "sc19", "position": 21, "quantity": 1, "side_code": "runner", "stripped_text": "Whenever an agenda is scored or stolen, add 1 unrezzed card to HQ.", "stripped_title": "Leela Patel: Trained Pragmatist", "text": "Whenever an agenda is scored or stolen, add 1 unrezzed card to HQ.", "title": "Leela Patel: Trained Pragmatist", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_chaos_theory_wunderkind_25040(Identity):
    '''
    Cost: n/a
    Text: +1 mu
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "25040", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"Have you met Dinosaurus?\"", "illustrator": "Matt Zeilinger", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 40, "pack_code": "sc19", "position": 40, "quantity": 1, "side_code": "runner", "stripped_text": "+1 mu", "stripped_title": "Chaos Theory: Wunderkind", "text": "+1[mu]", "title": "Chaos Theory: W\u00fcnderkind", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_rielle_kit_peddler_transhuman_25041(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you encounter a piece of ice, it gains code gate for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "25041", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "\"I was not; I was; I am not; I am all.\"", "illustrator": "Matt Zeilinger", "influence_limit": 10, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "sc19", "position": 41, "quantity": 1, "side_code": "runner", "stripped_text": "The first time each turn you encounter a piece of ice, it gains code gate for the remainder of this run.", "stripped_title": "Rielle \"Kit\" Peddler: Transhuman", "text": "The first time each turn you encounter a piece of ice, it gains <strong>code gate</strong> for the remainder of this run.", "title": "Rielle \"Kit\" Peddler: Transhuman", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_haasbioroid_stronger_together_25066(Identity):
    '''
    Cost: n/a
    Text: All bioroid ice has +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25066", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "A Different Breed of Machine.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "sc19", "position": 66, "quantity": 1, "side_code": "corp", "stripped_text": "All bioroid ice has +1 strength.", "stripped_title": "Haas-Bioroid: Stronger Together", "text": "All <strong>bioroid</strong> ice has +1 strength.", "title": "Haas-Bioroid: Stronger Together", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_seidr_laboratories_destiny_defined_25067(Identity):
    '''
    Cost: n/a
    Text: The first time each turn the Runner loses or spends click during a run, you may add 1 card from Archives to the top of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25067", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Interweaving the Past and the Future.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "sc19", "position": 67, "quantity": 1, "side_code": "corp", "stripped_text": "The first time each turn the Runner loses or spends click during a run, you may add 1 card from Archives to the top of R&D.", "stripped_title": "Seidr Laboratories: Destiny Defined", "text": "The first time each turn the Runner loses or spends [click] during a run, you may add 1 card from Archives to the top of R&D.", "title": "Seidr Laboratories: Destiny Defined", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jinteki_personal_evolution_25084(Identity):
    '''
    Cost: n/a
    Text: Whenever an agenda is scored or stolen, do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25084", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "When You Need the Human Touch.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "sc19", "position": 84, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever an agenda is scored or stolen, do 1 net damage.", "stripped_title": "Jinteki: Personal Evolution", "text": "Whenever an agenda is scored or stolen, do 1 net damage.", "title": "Jinteki: Personal Evolution", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jinteki_replicating_perfection_25085(Identity):
    '''
    Cost: n/a
    Text: The Runner cannot run on remote servers. Ignore this ability until the end of the turn whenever the Runner runs on a central server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25085", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "sc19", "position": 85, "quantity": 1, "side_code": "corp", "stripped_text": "The Runner cannot run on remote servers. Ignore this ability until the end of the turn whenever the Runner runs on a central server.", "stripped_title": "Jinteki: Replicating Perfection", "text": "The Runner cannot run on remote servers. Ignore this ability until the end of the turn whenever the Runner runs on a central server.", "title": "Jinteki: Replicating Perfection", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nbn_making_news_25104(Identity):
    '''
    Cost: n/a
    Text: 2 recurring credits Use these credits during trace attempts.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25104", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Someone is Always Watching.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "sc19", "position": 104, "quantity": 1, "side_code": "corp", "stripped_text": "2 recurring credits Use these credits during trace attempts.", "stripped_title": "NBN: Making News", "text": "2[recurring-credit]\nUse these credits during trace attempts.", "title": "NBN: Making News", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_spark_agency_worldswide_reach_25105(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you rez an advertisement, the Runner loses 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25105", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "We're ready to start the fire.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "sc19", "position": 105, "quantity": 1, "side_code": "corp", "stripped_text": "The first time each turn you rez an advertisement, the Runner loses 1 credit.", "stripped_title": "Spark Agency: Worldswide Reach", "text": "The first time each turn you rez an <strong>advertisement</strong>, the Runner loses 1[credit].", "title": "Spark Agency: Worldswide Reach", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_weyland_consortium_building_a_better_world_25122(Identity):
    '''
    Cost: n/a
    Text: Whenever you play a transaction operation, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25122", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Moving Upwards.", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "sc19", "position": 122, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever you play a transaction operation, gain 1 credit.", "stripped_title": "Weyland Consortium: Building a Better World", "text": "Whenever you play a <strong>transaction</strong> operation, gain 1[credit].", "title": "Weyland Consortium: Building a Better World", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_blue_sun_powering_the_future_25123(Identity):
    '''
    Cost: n/a
    Text: When your turn begins, you may add 1 rezzed card to HQ and gain credits equal to its rez cost.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25123", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Unlimited Energy. Reasonable Prices.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Corp", "minimum_deck_size": 45, "pack_code": "sc19", "position": 123, "quantity": 1, "side_code": "corp", "stripped_text": "When your turn begins, you may add 1 rezzed card to HQ and gain credits equal to its rez cost.", "stripped_title": "Blue Sun: Powering the Future", "text": "When your turn begins, you may add 1 rezzed card to HQ and gain credits equal to its rez cost.", "title": "Blue Sun: Powering the Future", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_az_mccaffrey_mechanical_prodigy_26010(Identity):
    '''
    Cost: n/a
    Text: The first job resource, connection resource, or piece of hardware you install each turn costs 1 credit less to install.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "26010", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "\"You're not listening.\"", "illustrator": "Luminita Pham", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "df", "position": 10, "quantity": 1, "side_code": "runner", "stripped_text": "The first job resource, connection resource, or piece of hardware you install each turn costs 1 credit less to install.", "stripped_title": "Az McCaffrey: Mechanical Prodigy", "text": "The first <strong>job</strong> resource, <strong>connection</strong> resource, or piece of hardware you install each turn costs 1[credit] less to install.", "title": "Az McCaffrey: Mechanical Prodigy", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_lat_ethical_freelancer_26019(Identity):
    '''
    Cost: n/a
    Text: When your turn ends, if you have the same number of cards in your grip as the Corp has in HQ, you may draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "26019", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "illustrator": "Luminita Pham", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "df", "position": 19, "quantity": 1, "side_code": "runner", "stripped_text": "When your turn ends, if you have the same number of cards in your grip as the Corp has in HQ, you may draw 1 card.", "stripped_title": "Lat: Ethical Freelancer", "text": "When your turn ends, if you have the same number of cards in your grip as the Corp has in HQ, you may draw 1 card.", "title": "Lat: Ethical Freelancer", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_mirrormorph_endless_iteration_26031(Identity):
    '''
    Cost: n/a
    Text: If the first, second, and third actions you take on your turn are different from each other, when the third completes, you may gain 1 credit or take another different action, paying 1click less.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26031", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Kira L. Nguyen", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "df", "position": 31, "quantity": 1, "side_code": "corp", "stripped_text": "If the first, second, and third actions you take on your turn are different from each other, when the third completes, you may gain 1 credit or take another different action, paying 1click less.", "stripped_title": "MirrorMorph: Endless Iteration", "text": "If the first, second, and third actions you take on your turn are different from each other, when the third completes, you may gain 1[credit] or take another different action, paying 1[click] less.", "title": "MirrorMorph: Endless Iteration", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_hyoubu_institute_absolute_clarity_26039(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you reveal a card, gain 1 credit. click: Reveal a card from the grip at random or the top card of the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26039", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "No Stone Unturned.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "df", "position": 39, "quantity": 1, "side_code": "corp", "stripped_text": "The first time each turn you reveal a card, gain 1 credit. click: Reveal a card from the grip at random or the top card of the stack.", "stripped_title": "Hyoubu Institute: Absolute Clarity", "text": "The first time each turn you reveal a card, gain 1[credit].\n[click]<strong>:</strong> Reveal a card from the grip at random or the top card of the stack.", "title": "Hyoubu Institute: Absolute Clarity", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_hoshiko_shiro_untold_protagonist_26066(Identity):
    '''
    Cost: n/a
    Text: When your turn ends, if you accessed at least 1 card this turn, gain 2 credits and flip this identity. Flip side: When your turn begins, draw 1 card and lose 1 credit. When your turn ends, if you did not access at least 1 card this turn, flip this identity.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "26066", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "Please, let me have this dream.\nFlip side:\nI'm going to be my own kind of hero.", "illustrator": "Luminita Pham", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "ur", "position": 66, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn ends, if you accessed at least 1 card this turn, gain 2 credits and flip this identity. Flip side: When your turn begins, draw 1 card and lose 1 credit. When your turn ends, if you did not access at least 1 card this turn, flip this identity.", "stripped_title": "Hoshiko Shiro: Untold Protagonist", "text": "When your turn ends, if you accessed at least 1 card this turn, gain 2[credit] and flip this identity.\nFlip side:\nWhen your turn begins, draw 1 card and lose 1[credit].\nWhen your turn ends, if you did not access at least 1 card this turn, flip this identity.", "title": "Hoshiko Shiro: Untold Protagonist", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_gamenet_where_dreams_are_real_26113(Identity):
    '''
    Cost: n/a
    Text: Whenever a Corp card ability causes the Runner to spend or lose at least 1 credit during a run, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26113", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Your Favorite Distraction.", "illustrator": "Alejandro T. Castellanos", "influence_limit": 17, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "ur", "position": 113, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever a Corp card ability causes the Runner to spend or lose at least 1 credit during a run, gain 1 credit.", "stripped_title": "GameNET: Where Dreams are Real", "text": "Whenever a Corp card ability causes the Runner to spend or lose at least 1[credit] during a run, gain 1[credit].", "title": "GameNET: Where Dreams are Real", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_earth_station_sea_headquarters_26120(Identity):
    '''
    Cost: n/a
    Text: Limit 1 remote server. As an additional cost to run HQ, the Runner must pay 1 credit. click: Flip this identity. Flip side: Limit 1 remote server. As an additional cost to run a remote server, the Runner must pay 6 credits. When the Runner makes a successful run on HQ, flip this identity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26120", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "The First Step...\nFlip side:\n...Further Beyond", "illustrator": "Kira L. Nguyen", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "ur", "position": 120, "quantity": 3, "side_code": "corp", "stripped_text": "Limit 1 remote server. As an additional cost to run HQ, the Runner must pay 1 credit. click: Flip this identity. Flip side: Limit 1 remote server. As an additional cost to run a remote server, the Runner must pay 6 credits. When the Runner makes a successful run on HQ, flip this identity.", "stripped_title": "Earth Station: SEA Headquarters", "text": "Limit 1 remote server.\nAs an additional cost to run HQ, the Runner must pay 1[credit].\n[click]<strong>:</strong> Flip this identity.\nFlip side:\nLimit 1 remote server.\nAs an additional cost to run a remote server, the Runner must pay 6[credit].\nWhen the Runner makes a successful run on HQ, flip this identity.", "title": "Earth Station: SEA Headquarters", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_rene_loup_arcemont_party_animal_30001(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you trash a card you are accessing, gain 1 credit and draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "30001", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "Run wyld.", "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 40, "pack_code": "sg", "position": 1, "quantity": 1, "side_code": "runner", "stripped_text": "The first time each turn you trash a card you are accessing, gain 1 credit and draw 1 card.", "stripped_title": "Rene \"Loup\" Arcemont: Party Animal", "text": "The first time each turn you trash a card you are accessing, gain 1[credit] and draw 1 card.", "title": "Ren\u00e9 \"Loup\" Arcemont: Party Animal", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_zahya_sadeghi_versatile_smuggler_30010(Identity):
    '''
    Cost: n/a
    Text: Whenever a run on HQ or R&D ends, you may gain 1 credit for each time you accessed a card during that run. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "30010", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "I obtain your desire.", "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 40, "pack_code": "sg", "position": 10, "quantity": 1, "side_code": "runner", "stripped_text": "Whenever a run on HQ or R&D ends, you may gain 1 credit for each time you accessed a card during that run. Use this ability only once per turn.", "stripped_title": "Zahya Sadeghi: Versatile Smuggler", "text": "Whenever a run on HQ or R&D ends, you may gain 1[credit] for each time you accessed a card during that run. Use this ability only once per turn.", "title": "Zahya Sadeghi: Versatile Smuggler", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_tao_salonga_telepresence_magician_30019(Identity):
    '''
    Cost: n/a
    Text: Whenever an agenda is scored or stolen, you may swap 2 installed pieces of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "30019", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "Sufficient skill is indistinguishable from magic.", "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 40, "pack_code": "sg", "position": 19, "quantity": 1, "side_code": "runner", "stripped_text": "Whenever an agenda is scored or stolen, you may swap 2 installed pieces of ice.", "stripped_title": "Tao Salonga: Telepresence Magician", "text": "Whenever an agenda is scored or stolen, you may swap 2 installed pieces of ice.", "title": "T\u0101o Salonga: Telepresence Magician", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_haasbioroid_precision_design_30035(Identity):
    '''
    Cost: n/a
    Text: You get +1 maximum hand size. Whenever you score an agenda, you may add 1 card from Archives to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30035", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Not an Atom Misplaced.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 40, "pack_code": "sg", "position": 35, "quantity": 1, "side_code": "corp", "stripped_text": "You get +1 maximum hand size. Whenever you score an agenda, you may add 1 card from Archives to HQ.", "stripped_title": "Haas-Bioroid: Precision Design", "text": "You get +1 maximum hand size.\nWhenever you score an agenda, you may add 1 card from Archives to HQ.", "title": "Haas-Bioroid: Precision Design", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jinteki_restoring_humanity_30043(Identity):
    '''
    Cost: n/a
    Text: When your discard phase ends, if there is a facedown card in Archives, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30043", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "An End to Suffering.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 40, "pack_code": "sg", "position": 43, "quantity": 1, "side_code": "corp", "stripped_text": "When your discard phase ends, if there is a facedown card in Archives, gain 1 credit.", "stripped_title": "Jinteki: Restoring Humanity", "text": "When your discard phase ends, if there is a facedown card in Archives, gain 1[credit].", "title": "Jinteki: Restoring Humanity", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nbn_reality_plus_30051(Identity):
    '''
    Cost: n/a
    Text: The first time each turn the Runner takes a tag, gain 2 credits or draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30051", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Why Settle for Real?", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 40, "pack_code": "sg", "position": 51, "quantity": 1, "side_code": "corp", "stripped_text": "The first time each turn the Runner takes a tag, gain 2 credits or draw 2 cards.", "stripped_title": "NBN: Reality Plus", "text": "The first time each turn the Runner takes a tag, gain 2[credit] or draw 2 cards.", "title": "NBN: Reality Plus", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_weyland_consortium_built_to_last_30059(Identity):
    '''
    Cost: n/a
    Text: Whenever you advance a card, gain 2 credits if it had no advancement counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30059", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Here to Stay.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 40, "pack_code": "sg", "position": 59, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever you advance a card, gain 2 credits if it had no advancement counters.", "stripped_title": "Weyland Consortium: Built to Last", "text": "Whenever you advance a card, gain 2[credit] if it had no advancement counters.", "title": "Weyland Consortium: Built to Last", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_the_catalyst_convention_breaker_30076(Identity):
    '''
    Cost: n/a
    Text: n/a
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "30076", "deck_limit": 1, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Are you ready to start something big?", "illustrator": "Benjamin Giletti", "influence_limit": null, "keywords": "Natural", "minimum_deck_size": 30, "pack_code": "sg", "position": 76, "quantity": 1, "side_code": "runner", "stripped_title": "The Catalyst: Convention Breaker", "title": "The Catalyst: Convention Breaker", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_the_syndicate_profit_over_principle_30077(Identity):
    '''
    Cost: n/a
    Text: n/a
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30077", "deck_limit": 1, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "You work for us. You just don't know it yet.", "illustrator": "Emilio Rodriguez", "influence_limit": null, "keywords": "Megacorp", "minimum_deck_size": 30, "pack_code": "sg", "position": 77, "quantity": 1, "side_code": "corp", "stripped_title": "The Syndicate: Profit over Principle", "title": "The Syndicate: Profit over Principle", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_quetzal_free_spirit_31001(Identity):
    '''
    Cost: n/a
    Text: 0 credits: Break 1 barrier subroutine. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "31001", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "The hue of your soul, the voice of your spirit, the shape of your flesh are yours to decide. Be free.", "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "su21", "position": 1, "quantity": 1, "side_code": "runner", "stripped_text": "0 credits: Break 1 barrier subroutine. Use this ability only once per turn.", "stripped_title": "Quetzal: Free Spirit", "text": "<strong>0[credit]:</strong> Break 1 <strong>barrier</strong> subroutine. Use this ability only once per turn.", "title": "Quetzal: Free Spirit", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_reina_roja_freedom_fighter_31002(Identity):
    '''
    Cost: n/a
    Text: The first piece of ice the Corp rezzes each turn costs 1 credit more to rez.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 1, "code": "31002", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "I'm through with games.", "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "Cyborg - G-mod", "minimum_deck_size": 45, "pack_code": "su21", "position": 2, "quantity": 1, "side_code": "runner", "stripped_text": "The first piece of ice the Corp rezzes each turn costs 1 credit more to rez.", "stripped_title": "Reina Roja: Freedom Fighter", "text": "The first piece of ice the Corp rezzes each turn costs 1[credit] more to rez.", "title": "Reina Roja: Freedom Fighter", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_ken_express_tenma_disappeared_clone_31013(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you play a run event, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "31013", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "Live in the fast lane.", "illustrator": "Benjamin Giletti", "influence_limit": 17, "keywords": "Clone", "minimum_deck_size": 45, "pack_code": "su21", "position": 13, "quantity": 1, "side_code": "runner", "stripped_text": "The first time each turn you play a run event, gain 1 credit.", "stripped_title": "Ken \"Express\" Tenma: Disappeared Clone", "text": "The first time each turn you play a <strong>run</strong> event, gain 1[credit].", "title": "Ken \"Express\" Tenma: Disappeared Clone", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_steve_cambridge_master_grifter_31014(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you make a successful run on HQ, you may choose 2 cards in your heap. If you do, the Corp removes 1 of those cards from the game, then you add the other card to your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "31014", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "Yeah. I'm thinking I'm back.", "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "su21", "position": 14, "quantity": 1, "side_code": "runner", "stripped_text": "The first time each turn you make a successful run on HQ, you may choose 2 cards in your heap. If you do, the Corp removes 1 of those cards from the game, then you add the other card to your grip.", "stripped_title": "Steve Cambridge: Master Grifter", "text": "The first time each turn you make a successful run on HQ, you may choose 2 cards in your heap. If you do, the Corp removes 1 of those cards from the game, then you add the other card to your grip.", "title": "Steve Cambridge: Master Grifter", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_ayla_bios_rahim_simulant_specialist_31025(Identity):
    '''
    Cost: n/a
    Text: Before drawing your starting hand, set aside the top 6 cards of your stack facedown. (You may look at those cards at any time.) Shuffle 2 of those cards into your stack. click: Add 1 card set aside with this identity to your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "31025", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "Natural", "minimum_deck_size": 45, "pack_code": "su21", "position": 25, "quantity": 1, "side_code": "runner", "stripped_text": "Before drawing your starting hand, set aside the top 6 cards of your stack facedown. (You may look at those cards at any time.) Shuffle 2 of those cards into your stack. click: Add 1 card set aside with this identity to your grip.", "stripped_title": "Ayla \"Bios\" Rahim: Simulant Specialist", "text": "Before drawing your starting hand, set aside the top 6 cards of your stack facedown. <em>(You may look at those cards at any time.)</em> Shuffle 2 of those cards into your stack.\n[click]<strong>:</strong> Add 1 card set aside with this identity to your grip.", "title": "Ayla \"Bios\" Rahim: Simulant Specialist", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_rielle_kit_peddler_transhuman_31026(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you encounter a piece of ice, it gains code gate for the remainder of this run.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "31026", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "My thoughts open; unbound within, unblocked without.", "illustrator": "Benjamin Giletti", "influence_limit": 10, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "su21", "position": 26, "quantity": 1, "side_code": "runner", "stripped_text": "The first time each turn you encounter a piece of ice, it gains code gate for the remainder of this run.", "stripped_title": "Rielle \"Kit\" Peddler: Transhuman", "text": "The first time each turn you encounter a piece of ice, it gains <strong>code gate</strong> for the remainder of this run.", "title": "Rielle \"Kit\" Peddler: Transhuman", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_haasbioroid_architects_of_tomorrow_31040(Identity):
    '''
    Cost: n/a
    Text: The first time each turn the Runner passes a rezzed piece of bioroid ice, you may rez 1 bioroid card, paying 4 credits less.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31040", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Service is Guaranteed.", "illustrator": "Kira L. Nguyen", "influence_limit": 12, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "su21", "position": 40, "quantity": 1, "side_code": "corp", "stripped_text": "The first time each turn the Runner passes a rezzed piece of bioroid ice, you may rez 1 bioroid card, paying 4 credits less.", "stripped_title": "Haas-Bioroid: Architects of Tomorrow", "text": "The first time each turn the Runner passes a rezzed piece of <strong>bioroid</strong> ice, you may rez 1 <strong>bioroid</strong> card, paying 4[credit] less.", "title": "Haas-Bioroid: Architects of Tomorrow", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_jinteki_personal_evolution_31050(Identity):
    '''
    Cost: n/a
    Text: Whenever an agenda is scored or stolen, do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31050", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "The Essence of You.", "illustrator": "Kira L. Nguyen", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "su21", "position": 50, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever an agenda is scored or stolen, do 1 net damage.", "stripped_title": "Jinteki: Personal Evolution", "text": "Whenever an agenda is scored or stolen, do 1 net damage.", "title": "Jinteki: Personal Evolution", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nearearth_hub_broadcast_center_31060(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you create a remote server, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31060", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Every Hour, Every Minute, Every Second.", "illustrator": "Kira L. Nguyen", "influence_limit": 17, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "su21", "position": 60, "quantity": 1, "side_code": "corp", "stripped_text": "The first time each turn you create a remote server, draw 1 card.", "stripped_title": "Near-Earth Hub: Broadcast Center", "text": "The first time each turn you create a remote server, draw 1 card.", "title": "Near-Earth Hub: Broadcast Center", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_weyland_consortium_building_a_better_world_31070(Identity):
    '''
    Cost: n/a
    Text: Whenever you play a transaction operation, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31070", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Above the Competition.", "illustrator": "Kira L. Nguyen", "influence_limit": 15, "keywords": "Megacorp", "minimum_deck_size": 45, "pack_code": "su21", "position": 70, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever you play a transaction operation, gain 1 credit.", "stripped_title": "Weyland Consortium: Building a Better World", "text": "Whenever you play a <strong>transaction</strong> operation, gain 1[credit].", "title": "Weyland Consortium: Building a Better World", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_esa_afontov_ecoinsurrectionist_33001(Identity):
    '''
    Cost: n/a
    Text: The first time each turn you suffer core damage, you may draw 1 card and sabotage 2. (The Corp trashes 2 cards of their choice from HQ and/or the top of R&D.)
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "33001", "deck_limit": 1, "faction_code": "anarch", "faction_cost": 0, "flavor": "Waiting is useless. The crisis is here; pick a side.", "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "ms", "position": 1, "quantity": 1, "side_code": "runner", "stripped_text": "The first time each turn you suffer core damage, you may draw 1 card and sabotage 2. (The Corp trashes 2 cards of their choice from HQ and/or the top of R&D.)", "stripped_title": "Esa Afontov: Eco-Insurrectionist", "text": "The first time each turn you suffer core damage, you may draw 1 card and sabotage 2. <em>(The Corp trashes 2 cards of their choice from HQ and/or the top of R&D.)</em>", "title": "Es\u00e2 Afontov: Eco-Insurrectionist", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nyusha_sable_sintashta_symphonic_prodigy_33011(Identity):
    '''
    Cost: n/a
    Text: When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) The first time each turn you make a successful run on your mark, gain click.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "33011", "deck_limit": 1, "faction_code": "criminal", "faction_cost": 0, "flavor": "Flaws hold both beauty and opportunity.", "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "G-mod", "minimum_deck_size": 45, "pack_code": "ms", "position": 11, "quantity": 1, "side_code": "runner", "stripped_text": "When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) The first time each turn you make a successful run on your mark, gain click.", "stripped_title": "Nyusha \"Sable\" Sintashta: Symphonic Prodigy", "text": "When your turn begins, identify your mark. <em>(If you don\u2019t have a mark, a random central server becomes your mark for this turn.)</em>\nThe first time each turn you make a successful run on your mark, gain [click].", "title": "Nyusha \"Sable\" Sintashta: Symphonic Prodigy", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_captain_padma_isbister_intrepid_explorer_33021(Identity):
    '''
    Cost: n/a
    Text: The first time each turn a run on R&D begins, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "33021", "deck_limit": 1, "faction_code": "shaper", "faction_cost": 0, "flavor": "The sea is everything; its breath must remain pure and healthy.", "illustrator": "Benjamin Giletti", "influence_limit": 15, "keywords": "Cyborg", "minimum_deck_size": 45, "pack_code": "ms", "position": 21, "quantity": 1, "side_code": "runner", "stripped_text": "The first time each turn a run on R&D begins, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)", "stripped_title": "Captain Padma Isbister: Intrepid Explorer", "text": "The first time each turn a run on R&D begins, you may charge 1 of your installed cards. <em>(Add 1 power counter to a card that already has one.)</em>", "title": "Captain Padma Isbister: Intrepid Explorer", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_pravdivost_consulting_political_solutions_33048(Identity):
    '''
    Cost: n/a
    Text: The first time each turn the Runner makes a successful run, you may place 1 advancement counter on an installed card you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33048", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "Political news, fit for public consumption.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "ms", "position": 48, "quantity": 1, "side_code": "corp", "stripped_text": "The first time each turn the Runner makes a successful run, you may place 1 advancement counter on an installed card you can advance.", "stripped_title": "Pravdivost Consulting: Political Solutions", "text": "The first time each turn the Runner makes a successful run, you may place 1 advancement counter on an installed card you can advance.", "title": "Pravdivost Consulting: Political Solutions", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_ob_superheavy_logistics_extract_export_excel_33057(Identity):
    '''
    Cost: n/a
    Text: Whenever you trash a rezzed card, except during installation, you may search R&D for 1 card with a printed rez cost exactly 1 credit less than the trashed card's printed rez cost. Install and rez the card you found, ignoring credit costs. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33057", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Take all that is offered, and more.", "illustrator": "Vitalii Ostaschenko", "influence_limit": 15, "keywords": "Corp", "minimum_deck_size": 45, "pack_code": "ms", "position": 57, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever you trash a rezzed card, except during installation, you may search R&D for 1 card with a printed rez cost exactly 1 credit less than the trashed card's printed rez cost. Install and rez the card you found, ignoring credit costs. Use this ability only once per turn.", "stripped_title": "Ob Superheavy Logistics: Extract. Export. Excel.", "text": "Whenever you trash a rezzed card, except during installation, you may search R&D for 1 card with a printed rez cost exactly 1[credit] less than the trashed card's printed rez cost. Install and rez the card you found, ignoring credit costs. Use this ability only once per turn.", "title": "Ob Superheavy Logistics: Extract. Export. Excel.", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_nova_initiumia_catalyst__impetus_33093(Identity):
    '''
    Cost: n/a
    Text: Your deck cannot include more than 1 copy of any card.
    '''
    def __init__(self):
        super().__init__(r'''{"base_link": 0, "code": "33093", "deck_limit": 1, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "I found my twin hidden away on Luna. Now we will never be apart.", "illustrator": "Ferenc Patk\u00f3s", "influence_limit": null, "keywords": "Digital - Natural", "minimum_deck_size": 40, "pack_code": "ph", "position": 93, "quantity": 1, "side_code": "runner", "stripped_text": "Your deck cannot include more than 1 copy of any card.", "stripped_title": "Nova Initiumia: Catalyst & Impetus", "text": "Your deck cannot include more than 1 copy of any card.", "title": "Nova Initiumia: Catalyst & Impetus", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_thule_subsea_safety_below_33095(Identity):
    '''
    Cost: n/a
    Text: Whenever the Runner steals an agenda, do 1 core damage unless they spend click and 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33095", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Join us. Safe, away from the crisis.", "illustrator": "Kira L. Nguyen", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "ph", "position": 95, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever the Runner steals an agenda, do 1 core damage unless they spend click and 2 credits.", "stripped_title": "Thule Subsea: Safety Below", "text": "Whenever the Runner steals an agenda, do 1 core damage unless they spend [click] and 2[credit].", "title": "Thule Subsea: Safety Below", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_issuaq_adaptics_sustaining_diversity_33104(Identity):
    '''
    Cost: n/a
    Text: Whenever you score an agenda that you did not install or advance this turn, place 1 power counter on this identity. For each hosted power counter, you need 1 less agenda point to win the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33104", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "Bringing Mother Nature up to speed.", "illustrator": "Emilio Rodriguez", "influence_limit": 15, "keywords": "Division", "minimum_deck_size": 45, "pack_code": "ph", "position": 104, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever you score an agenda that you did not install or advance this turn, place 1 power counter on this identity. For each hosted power counter, you need 1 less agenda point to win the game.", "stripped_title": "Issuaq Adaptics: Sustaining Diversity", "text": "Whenever you score an agenda that you did not install or advance this turn, place 1 power counter on this identity.\nFor each hosted power counter, you need 1 less agenda point to win the game.", "title": "Issuaq Adaptics: Sustaining Diversity", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class identity_ampere_cybernetics_for_anyone_33128(Identity):
    '''
    Cost: n/a
    Text: Your deck cannot include more than 1 copy of any card. Your deck may include up to 2 different agenda cards from each Corp faction.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33128", "deck_limit": 1, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Affordable, Effective, and Uncompromising.", "illustrator": "Emilio Rodriguez", "influence_limit": null, "keywords": "Corp", "minimum_deck_size": 45, "pack_code": "ph", "position": 128, "quantity": 1, "side_code": "corp", "stripped_text": "Your deck cannot include more than 1 copy of any card. Your deck may include up to 2 different agenda cards from each Corp faction.", "stripped_title": "Ampere: Cybernetics For Anyone", "text": "Your deck cannot include more than 1 copy of any card.\nYour deck may include up to 2 different agenda cards from each Corp faction.", "title": "Amp\u00e8re: Cybernetics For Anyone", "type_code": "identity", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"
