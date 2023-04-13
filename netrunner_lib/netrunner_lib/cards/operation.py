
'''
card classes of type operation
'''
from netrunner_lib.cards._base_card_classes import Operation
from netrunner_lib.game_events import *

class operation_archived_memories_01058(Operation):
    '''
    Cost: 0
    Text: Add 1 card from Archives to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01058", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Do you think they\u2026feel it?\"", "illustrator": "Gong Studios", "pack_code": "core", "position": 58, "quantity": 2, "side_code": "corp", "stripped_text": "Add 1 card from Archives to HQ.", "stripped_title": "Archived Memories", "text": "Add 1 card from Archives to HQ.", "title": "Archived Memories", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_biotic_labor_01059(Operation):
    '''
    Cost: 4
    Text: Gain click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01059", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "\"Why of course, we have six different Haas-Bioroid models serving in a variety of positions at this branch office alone. We here at Haas-Bioroid aren't going to shy away from practicing what we preach, and we pass the savings from increased efficiency on to our valued customers.\"", "illustrator": "Mark Anthony Taduran", "pack_code": "core", "position": 59, "quantity": 3, "side_code": "corp", "stripped_text": "Gain click click.", "stripped_title": "Biotic Labor", "text": "Gain [click][click].", "title": "Biotic Labor", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_shipment_from_mirrormorph_01060(Operation):
    '''
    Cost: 1
    Text: Install up to 3 cards from HQ (one at a time and paying all install costs).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01060", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "The new heads were in. Their eyes always followed your movements when you unlocked the pressurized container and lifted the lid.", "illustrator": "Matt Zeilinger", "pack_code": "core", "position": 60, "quantity": 2, "side_code": "corp", "stripped_text": "Install up to 3 cards from HQ (one at a time and paying all install costs).", "stripped_title": "Shipment from MirrorMorph", "text": "Install up to 3 cards from HQ (one at a time and paying all install costs).", "title": "Shipment from MirrorMorph", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_neural_emp_01072(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner made a run during their last turn. Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01072", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "The trick isn't hitting the person you were aiming at. It's hitting <strong>only</strong> the person you were aiming at.", "illustrator": "Christina Davis", "keywords": "Gray Ops", "pack_code": "core", "position": 72, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner made a run during their last turn. Do 1 net damage.", "stripped_title": "Neural EMP", "text": "Play only if the Runner made a run during their last turn.\nDo 1 net damage.", "title": "Neural EMP", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_precognition_01073(Operation):
    '''
    Cost: 0
    Text: Look at the top 5 cards of R&D and arrange them in any order.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01073", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "There was a new texture in her phantom cortex. It had always been there, she realized. It was everything and nothing.", "illustrator": "Alexandra Douglass", "pack_code": "core", "position": 73, "quantity": 2, "side_code": "corp", "stripped_text": "Look at the top 5 cards of R&D and arrange them in any order.", "stripped_title": "Precognition", "text": "Look at the top 5 cards of R&D and arrange them in any order.", "title": "Precognition", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_anonymous_tip_01083(Operation):
    '''
    Cost: 0
    Text: Draw 3 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01083", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"Please stay connected. Priority transfer in progress. An operator will shortly verif-\"", "illustrator": "Mike Nesbitt", "pack_code": "core", "position": 83, "quantity": 2, "side_code": "corp", "stripped_text": "Draw 3 cards.", "stripped_title": "Anonymous Tip", "text": "Draw 3 cards.", "title": "Anonymous Tip", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        player.draw_card()
        player.draw_card()
        player.draw_card()
        return self.trash(player)

class operation_closed_accounts_01084(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner is tagged. The Runner loses all credits in their credit pool.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01084", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Mauricio Herrera", "keywords": "Gray Ops", "pack_code": "core", "position": 84, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. The Runner loses all credits in their credit pool.", "stripped_title": "Closed Accounts", "text": "Play only if the Runner is tagged.\nThe Runner loses all credits in their credit pool.", "title": "Closed Accounts", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_psychographics_01085(Operation):
    '''
    Cost: None
    Text: X must be equal to or less than the number of tags the Runner has. Place X advancement counters on 1 installed card you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01085", "cost": null, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "Access to the largest consumer database in the galaxy has its advantages.", "illustrator": "Matt Zeilinger", "pack_code": "core", "position": 85, "quantity": 2, "side_code": "corp", "stripped_text": "X must be equal to or less than the number of tags the Runner has. Place X advancement counters on 1 installed card you can advance.", "stripped_title": "Psychographics", "text": "X must be equal to or less than the number of tags the Runner has.\nPlace X advancement counters on 1 installed card you can advance.", "title": "Psychographics", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sea_source_01086(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner made a successful run during their last turn. Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01086", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"The SEA tipped us off to some suspicious data spikes up by the Castle.\" -Jerome Lock, on-duty tech", "illustrator": "Mauricio Herrera", "pack_code": "core", "position": 86, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "SEA Source", "text": "Play only if the Runner made a successful run during their last turn.\nTrace[3]. If successful, give the Runner 1 tag.", "title": "SEA Source", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_aggressive_negotiation_01097(Operation):
    '''
    Cost: 1
    Text: Play only if you scored an agenda this turn. Search R&D for 1 card and add it to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01097", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"I believe you'll find the terms are quite favorable.\"", "illustrator": "Kate Niemczyk", "pack_code": "core", "position": 97, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if you scored an agenda this turn. Search R&D for 1 card and add it to HQ. Shuffle R&D.", "stripped_title": "Aggressive Negotiation", "text": "Play only if you scored an agenda this turn.\nSearch R&D for 1 card and add it to HQ. Shuffle R&D.", "title": "Aggressive Negotiation", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_beanstalk_royalties_01098(Operation):
    '''
    Cost: 0
    Text: Gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01098", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "The New Angeles Space Elevator, better known as the Beanstalk, is the single greatest triumph of human engineering and ingenuity in history. The Beanstalk makes Earth orbit accessible to everyone\u2026for a small fee.", "illustrator": "Jonathan Lee", "keywords": "Transaction", "pack_code": "core", "position": 98, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 3 credits.", "stripped_title": "Beanstalk Royalties", "text": "Gain 3[credit].", "title": "Beanstalk Royalties", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_scorched_earth_01099(Operation):
    '''
    Cost: 3
    Text: Play only if the Runner is tagged. Do 4 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01099", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "\"I'd like to remind the ladies and gentlemen of the press that several of the buildings damaged in the blast were owned by Weyland Consortium subsidiaries\u2026\"", "illustrator": "Mark Anthony Taduran", "keywords": "Black Ops", "pack_code": "core", "position": 99, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Do 4 meat damage.", "stripped_title": "Scorched Earth", "text": "Play only if the Runner is tagged.\nDo 4 meat damage.", "title": "Scorched Earth", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_shipment_from_kaguya_01100(Operation):
    '''
    Cost: 0
    Text: Place 1 advancement token on each of up to 2 different installed cards that can be advanced.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01100", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"And then there's these two crates. No eID.\"\n\"Just leave those with me and forget you ever saw them.\"", "illustrator": "Andrew Mar", "pack_code": "core", "position": 100, "quantity": 2, "side_code": "corp", "stripped_text": "Place 1 advancement token on each of up to 2 different installed cards that can be advanced.", "stripped_title": "Shipment from Kaguya", "text": "Place 1 advancement token on each of up to 2 different installed cards that can be advanced.", "title": "Shipment from Kaguya", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hedge_fund_01110(Operation):
    '''
    Cost: 5
    Text: Gain 9 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01110", "cost": 5, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Hedge Fund. Noun. An ingenious device by which the rich get richer even while every other poor SOB is losing his shirt. -The Anarch's Dictionary, Volume Who's Counting?", "illustrator": "Gong Studios", "keywords": "Transaction", "pack_code": "core", "position": 110, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 9 credits.", "stripped_title": "Hedge Fund", "text": "Gain 9[credit].", "title": "Hedge Fund", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_trick_of_light_02033(Operation):
    '''
    Cost: 1
    Text: Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02033", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Smoke and mirrors optional.", "illustrator": "Anna Ignatieva", "pack_code": "ta", "position": 33, "quantity": 3, "side_code": "corp", "stripped_text": "Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.", "stripped_title": "Trick of Light", "text": "Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.", "title": "Trick of Light", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_big_brother_02035(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner is tagged. Give the Runner 2 tags.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02035", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Looking out for your interests since 1984.", "illustrator": "Matt Zeilinger", "keywords": "Gray Ops", "pack_code": "ta", "position": 35, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Give the Runner 2 tags.", "stripped_title": "Big Brother", "text": "Play only if the Runner is tagged.\nGive the Runner 2 tags.", "title": "Big Brother", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_power_grid_overload_02037(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner made a successful run during their last turn. Trace[2]. If successful, trash 1 installed piece of hardware with an install cost of X or less, where X is equal to the amount by which your trace strength exceeded the Runner's link strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02037", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "illustrator": "Howard Schechlman", "pack_code": "ta", "position": 37, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. Trace[2]. If successful, trash 1 installed piece of hardware with an install cost of X or less, where X is equal to the amount by which your trace strength exceeded the Runner's link strength.", "stripped_title": "Power Grid Overload", "text": "Play only if the Runner made a successful run during their last turn.\nTrace[2]. If successful, trash 1 installed piece of hardware with an install cost of X or less, where X is equal to the amount by which your trace strength exceeded the Runner's link strength.", "title": "Power Grid Overload", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_freelancer_02040(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner is tagged. Trash up to 2 resources.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02040", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "No contract. Just a handshake and a fistful of C-6 high explosives.", "illustrator": "RJ Palmer", "keywords": "Gray Ops", "pack_code": "ta", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Trash up to 2 resources.", "stripped_title": "Freelancer", "text": "Play only if the Runner is tagged.\nTrash up to 2 resources.", "title": "Freelancer", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sunset_02054(Operation):
    '''
    Cost: 0
    Text: Choose a server. Arrange the ice protecting that server in any order.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02054", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"You haven't run until you've seen the cybersun drift down behind the Great City, the space around you rippling with colors you can't imagine.\" -Kate \"Mac\" McCaffrey", "illustrator": "Adam S. Doyle", "pack_code": "ce", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "Choose a server. Arrange the ice protecting that server in any order.", "stripped_title": "Sunset", "text": "Choose a server. Arrange the ice protecting that server in any order.", "title": "Sunset", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_commercialization_02058(Operation):
    '''
    Cost: 0
    Text: Choose a piece of ice. Gain 1 credit for each advancement token on that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02058", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "The Division of Fringe Applications' revenue increased 37% year-over-year after corporate discovered that most of their projects made really fun toys.", "illustrator": "Matt Zeilinger", "keywords": "Transaction", "pack_code": "ce", "position": 58, "quantity": 3, "side_code": "corp", "stripped_text": "Choose a piece of ice. Gain 1 credit for each advancement token on that ice.", "stripped_title": "Commercialization", "text": "Choose a piece of ice. Gain 1[credit] for each advancement token on that ice.", "title": "Commercialization", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_green_level_clearance_02070(Operation):
    '''
    Cost: 1
    Text: Gain 3 credits and draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02070", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Green-two clearance is the highest level of security a corp can gain access to. Legally, anyway.", "illustrator": "Mauricio Herrera", "keywords": "Transaction", "pack_code": "asis", "position": 70, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 3 credits and draw 1 card.", "stripped_title": "Green Level Clearance", "text": "Gain 3[credit] and draw 1 card.", "title": "Green Level Clearance", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_oversight_ai_02079(Operation):
    '''
    Cost: 1
    Text: Rez a piece of ice, ignoring all costs, and install Oversight AI on that ice as a hosted condition counter with the text "Trash host ice if all its subroutines are broken during a single encounter."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02079", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Mark Anthony Taduran", "keywords": "Condition", "pack_code": "asis", "position": 79, "quantity": 3, "side_code": "corp", "stripped_text": "Rez a piece of ice, ignoring all costs, and install Oversight AI on that ice as a hosted condition counter with the text \"Trash host ice if all its subroutines are broken during a single encounter.\"", "stripped_title": "Oversight AI", "text": "Rez a piece of ice, ignoring all costs, and install Oversight AI on that ice as a hosted condition counter with the text \"Trash host ice if all its subroutines are broken during a single encounter.\"", "title": "Oversight AI", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_rework_02093(Operation):
    '''
    Cost: 0
    Text: Shuffle 1 card from HQ into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02093", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Also known as \"development hell.\"", "illustrator": "Adam S. Doyle", "pack_code": "hs", "position": 93, "quantity": 3, "side_code": "corp", "stripped_text": "Shuffle 1 card from HQ into R&D.", "stripped_title": "Rework", "text": "Shuffle 1 card from HQ into R&D.", "title": "Rework", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_foxfire_02100(Operation):
    '''
    Cost: 0
    Text: Trace[7]. If successful, trash 1 virtual resource or 1 link.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02100", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"It's kind of like an anagram.\" -designer Phoenix", "illustrator": "Jen Zee", "pack_code": "hs", "position": 100, "quantity": 3, "side_code": "corp", "stripped_text": "Trace[7]. If successful, trash 1 virtual resource or 1 link.", "stripped_title": "Foxfire", "text": "Trace[7]. If successful, trash 1 <strong>virtual</strong> resource or 1 <strong>link</strong>.", "title": "Foxfire", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_midseason_replacements_02116(Operation):
    '''
    Cost: 5
    Text: Play only if the Runner stole an agenda during their last turn. Trace[6]. If successful, give the Runner X tags. X is equal to the amount by which your trace strength exceeded their link strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02116", "cost": 5, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "illustrator": "Christina Davis", "pack_code": "fp", "position": 116, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner stole an agenda during their last turn. Trace[6]. If successful, give the Runner X tags. X is equal to the amount by which your trace strength exceeded their link strength.", "stripped_title": "Midseason Replacements", "text": "Play only if the Runner stole an agenda during their last turn.\nTrace[6]. If successful, give the Runner X tags. X is equal to the amount by which your trace strength exceeded their link strength.", "title": "Midseason Replacements", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_bioroid_efficiency_research_03013(Operation):
    '''
    Cost: 3
    Text: Rez a piece of bioroid ice, ignoring all costs, and install Bioroid Efficiency Research on that ice as a hosted condition counter with the text "Trash Bioroid Efficiency Research and derez host ice if all of its subroutines are broken during a single encounter."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03013", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Emilio Rodriguez", "keywords": "Condition", "pack_code": "cac", "position": 13, "quantity": 3, "side_code": "corp", "stripped_text": "Rez a piece of bioroid ice, ignoring all costs, and install Bioroid Efficiency Research on that ice as a hosted condition counter with the text \"Trash Bioroid Efficiency Research and derez host ice if all of its subroutines are broken during a single encounter.\"", "stripped_title": "Bioroid Efficiency Research", "text": "Rez a piece of <strong>bioroid</strong> ice, ignoring all costs, and install Bioroid Efficiency Research on that ice as a hosted condition counter with the text \"Trash Bioroid Efficiency Research and derez host ice if all of its subroutines are broken during a single encounter.\"", "title": "Bioroid Efficiency Research", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_successful_demonstration_03014(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner made an unsuccessful run during their last turn. Gain 7 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03014", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Success is defined by the safety of data, not the safety of potential intruders.", "illustrator": "Irys Ching", "keywords": "Transaction", "pack_code": "cac", "position": 14, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner made an unsuccessful run during their last turn. Gain 7 credits.", "stripped_title": "Successful Demonstration", "text": "Play only if the Runner made an unsuccessful run during their last turn.\nGain 7[credit].", "title": "Successful Demonstration", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_celebrity_gift_04012(Operation):
    '''
    Cost: 3
    Text: As an additional cost to play this operation, spend click. Reveal up to 5 cards in HQ. Gain 2 credits for each card you revealed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04012", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "When Miranda Rhapsody showed up with a teacup giraffe, suddenly everybody wanted one.", "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "om", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Reveal up to 5 cards in HQ. Gain 2 credits for each card you revealed this way.", "stripped_title": "Celebrity Gift", "text": "As an additional cost to play this operation, spend [click].\nReveal up to 5 cards in HQ. Gain 2[credit] for each card you revealed this way.", "title": "Celebrity Gift", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_invasion_of_privacy_04016(Operation):
    '''
    Cost: 2
    Text: As additional cost to play this operation, spend click. Trace[2]. If successful, reveal the grip. Trash up to X resources and/or events revealed this way, where X is equal to the amount by which your trace strength exceeded the Runner's link strength. If unsuccessful, take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04016", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Del Borovic", "keywords": "Double - Gray Ops", "pack_code": "om", "position": 16, "quantity": 3, "side_code": "corp", "stripped_text": "As additional cost to play this operation, spend click. Trace[2]. If successful, reveal the grip. Trash up to X resources and/or events revealed this way, where X is equal to the amount by which your trace strength exceeded the Runner's link strength. If unsuccessful, take 1 bad publicity.", "stripped_title": "Invasion of Privacy", "text": "As additional cost to play this operation, spend [click].\nTrace[2]. If successful, reveal the grip. Trash up to X resources and/or events revealed this way, where X is equal to the amount by which your trace strength exceeded the Runner's link strength. If unsuccessful, take 1 bad publicity.", "title": "Invasion of Privacy", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_cyberdex_trial_04019(Operation):
    '''
    Cost: 0
    Text: Purge virus counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04019", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Your free trial expired. Upgrade to the full version?", "illustrator": "J. Zhang", "pack_code": "om", "position": 19, "quantity": 3, "side_code": "corp", "stripped_text": "Purge virus counters.", "stripped_title": "Cyberdex Trial", "text": "Purge virus counters.", "title": "Cyberdex Trial", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hellion_alpha_test_04031(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner installed a resource during their last turn. Trace[2]. If successful, add 1 installed resource to the top of the stack. If unsuccessful, take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04031", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Isuardi Therianto", "keywords": "Black Ops", "pack_code": "st", "position": 31, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner installed a resource during their last turn. Trace[2]. If successful, add 1 installed resource to the top of the stack. If unsuccessful, take 1 bad publicity.", "stripped_title": "Hellion Alpha Test", "text": "Play only if the Runner installed a resource during their last turn.\nTrace[2]. If successful, add 1 installed resource to the top of the stack. If unsuccessful, take 1 bad publicity.", "title": "Hellion Alpha Test", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_shipment_from_sansan_04034(Operation):
    '''
    Cost: 0
    Text: As an additional cost to play this operation, spend click. Place up to 2 advancement tokens on a card that can be advanced.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04034", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "He signed for it, hand shaking in anticipation.", "illustrator": "Agri Karuniawan", "keywords": "Double", "pack_code": "st", "position": 34, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Place up to 2 advancement tokens on a card that can be advanced.", "stripped_title": "Shipment from SanSan", "text": "As an additional cost to play this operation, spend [click].\nPlace up to 2 advancement tokens on a card that can be advanced.", "title": "Shipment from SanSan", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_restructure_04040(Operation):
    '''
    Cost: 10
    Text: Gain 15 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04040", "cost": 10, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "There are many names for those in the Administration Department. But if you like your job, you just refer to them as \"sir\" and \"ma'am\".", "illustrator": "Isuardi Therianto", "keywords": "Transaction", "pack_code": "st", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 15 credits.", "stripped_title": "Restructure", "text": "Gain 15[credit].", "title": "Restructure", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_accelerated_diagnostics_04052(Operation):
    '''
    Cost: 1
    Text: Look at the top 3 cards of R&D. If any of those cards are operations, you may play them (paying their play cost), ignoring any additional costs. Trash the rest of the unplayed cards you looked at.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04052", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "\"I'm getting a reading that is\u2026off the charts. No, it crashed the charts. That counts as off, right?\"", "illustrator": "Gong Studios", "pack_code": "mt", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "Look at the top 3 cards of R&D. If any of those cards are operations, you may play them (paying their play cost), ignoring any additional costs. Trash the rest of the unplayed cards you looked at.", "stripped_title": "Accelerated Diagnostics", "text": "Look at the top 3 cards of R&D. If any of those cards are operations, you may play them (paying their play cost), ignoring any additional costs. Trash the rest of the unplayed cards you looked at.", "title": "Accelerated Diagnostics", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_power_shutdown_04058(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner made a run during their last turn. Trash any number of cards from the top of R&D. The Runner trashes an installed program or piece of hardware with an install cost equal to or less than the number of cards you trashed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04058", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Gong Studios", "keywords": "Gray Ops", "pack_code": "mt", "position": 58, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner made a run during their last turn. Trash any number of cards from the top of R&D. The Runner trashes an installed program or piece of hardware with an install cost equal to or less than the number of cards you trashed this way.", "stripped_title": "Power Shutdown", "text": "Play only if the Runner made a run during their last turn.\nTrash any number of cards from the top of R&D. The Runner trashes an installed program or piece of hardware with an install cost equal to or less than the number of cards you trashed this way.", "title": "Power Shutdown", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_interns_04060(Operation):
    '''
    Cost: 0
    Text: As an additional cost to play this operation, spend click. Install a non-operation card from Archives or HQ, ignoring the install cost.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04060", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"They're the only labor cheaper than clones.\"", "illustrator": "Akiko F. Minowa", "keywords": "Double", "pack_code": "mt", "position": 60, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Install a non-operation card from Archives or HQ, ignoring the install cost.", "stripped_title": "Interns", "text": "As an additional cost to play this operation, spend [click].\nInstall a non-operation card from Archives or HQ, ignoring the install cost.", "title": "Interns", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sweeps_week_04076(Operation):
    '''
    Cost: 1
    Text: Gain 1 credit for each card in the Runner's grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04076", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Let me get this straight. Your target market is 15-19 year old g-modded immigrants with one parent, a discretionary income over 2k a month, B+ or higher grades, an outgoing personality, and have a friend who owns a g-monkey?\"\n\"Yes. Is that a problem?\"\n\"No, not at all. I just don't get why your list is so short.\"", "illustrator": "Mike Nesbitt", "pack_code": "tc", "position": 76, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit for each card in the Runner's grip.", "stripped_title": "Sweeps Week", "text": "Gain 1[credit] for each card in the Runner's grip.", "title": "Sweeps Week", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_punitive_counterstrike_04079(Operation):
    '''
    Cost: 3
    Text: Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04079", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"I'd say it's nothing personal, but corporations are people, too.\"", "illustrator": "Lorraine Schleter", "keywords": "Black Ops", "pack_code": "tc", "position": 79, "quantity": 3, "side_code": "corp", "stripped_text": "Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.", "stripped_title": "Punitive Counterstrike", "text": "Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.", "title": "Punitive Counterstrike", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_blue_level_clearance_04090(Operation):
    '''
    Cost: 2
    Text: As an additional cost to play this operation, spend click. Gain 5 credits and draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04090", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Blue-one level clearance doesn't exist. And if it did exist, you wouldn't be cleared to know about it.", "illustrator": "Tim Durning", "keywords": "Double - Transaction", "pack_code": "fal", "position": 90, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Gain 5 credits and draw 2 cards.", "stripped_title": "Blue Level Clearance", "text": "As an additional cost to play this operation, spend [click].\nGain 5[credit] and draw 2 cards.", "title": "Blue Level Clearance", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_restoring_face_04094(Operation):
    '''
    Cost: 0
    Text: Trash one of your installed sysops, executives, or clones. If you do, remove up to 2 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04094", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "He slowly pried open the lid, and the tant\u014d glinted madly in the half-light. The executive motioned to the blade. Looks like the meeting was being cut short.", "illustrator": "Gong Studios", "pack_code": "fal", "position": 94, "quantity": 3, "side_code": "corp", "stripped_text": "Trash one of your installed sysops, executives, or clones. If you do, remove up to 2 bad publicity.", "stripped_title": "Restoring Face", "text": "Trash one of your installed <strong>sysops</strong>, <strong>executives</strong>, or <strong>clones</strong>. If you do, remove up to 2 bad publicity.", "title": "Restoring Face", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_subliminal_messaging_04100(Operation):
    '''
    Cost: 0
    Text: Gain 1 credit. The first time each turn you play a copy of Subliminal Messaging, gain click. When your turn begins, if this card is in Archives and the Runner did not initiate any runs during their last turn, you may reveal this card and add it to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04100", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Mike Nesbitt", "keywords": "Gray Ops", "pack_code": "fal", "position": 100, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit. The first time each turn you play a copy of Subliminal Messaging, gain click. When your turn begins, if this card is in Archives and the Runner did not initiate any runs during their last turn, you may reveal this card and add it to HQ.", "stripped_title": "Subliminal Messaging", "text": "Gain 1[credit].\nThe first time each turn you play a copy of Subliminal Messaging, gain [click].\nWhen your turn begins, if this card is in Archives and the Runner did not initiate any runs during their last turn, you may reveal this card and add it to HQ.", "title": "Subliminal Messaging", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_reclamation_order_04111(Operation):
    '''
    Cost: 1
    Text: As an additional cost to play this operation, spend click. Name a card other than Reclamation Order. Reveal any number of copies of the named card from Archives and add them to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04111", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Emilio Rodriguez", "keywords": "Double", "pack_code": "dt", "position": 111, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Name a card other than Reclamation Order. Reveal any number of copies of the named card from Archives and add them to HQ.", "stripped_title": "Reclamation Order", "text": "As an additional cost to play this operation, spend [click].\nName a card other than Reclamation Order. Reveal any number of copies of the named card from Archives and add them to HQ.", "title": "Reclamation Order", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_corporate_shuffle_04113(Operation):
    '''
    Cost: 0
    Text: As an additional cost to play this operation, spend click. Shuffle all cards in HQ into R&D. Draw 5 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04113", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "The only thing worse than being fired and replaced by a younger, cheaper worker? Being replaced by an android.", "illustrator": "Agri Karuniawan", "keywords": "Double", "pack_code": "dt", "position": 113, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Shuffle all cards in HQ into R&D. Draw 5 cards.", "stripped_title": "Corporate Shuffle", "text": "As an additional cost to play this operation, spend [click].\nShuffle all cards in HQ into R&D. Draw 5 cards.", "title": "Corporate Shuffle", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_witness_tampering_04118(Operation):
    '''
    Cost: 4
    Text: As an additional cost to play this operation, spend click. Remove up to 2 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04118", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"Now, let's talk about how little you remember of the events of June sixth through sixteenth.\"", "illustrator": "Lorraine Schleter", "keywords": "Double - Gray Ops", "pack_code": "dt", "position": 118, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Remove up to 2 bad publicity.", "stripped_title": "Witness Tampering", "text": "As an additional cost to play this operation, spend [click].\nRemove up to 2 bad publicity.", "title": "Witness Tampering", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_cerebral_cast_05013(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner made a successful run during their last turn. You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, they must suffer 1 core damage or take 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05013", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Smirtouille", "keywords": "Gray Ops - Psi", "pack_code": "hap", "position": 13, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, they must suffer 1 core damage or take 1 tag.", "stripped_title": "Cerebral Cast", "text": "Play only if the Runner made a successful run during their last turn.\nYou and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, they must suffer 1 core damage or take 1 tag.", "title": "Cerebral Cast", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_medical_research_fundraiser_05014(Operation):
    '''
    Cost: 3
    Text: Gain 8 credits. The Runner gains 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05014", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"Together we have all but eradicated natural diseases from the face of this planet. The new spectre of synthetic disease-of bioterrorism-demands that we continue our efforts.\"", "illustrator": "Gong Studios", "keywords": "Transaction", "pack_code": "hap", "position": 14, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 8 credits. The Runner gains 3 credits.", "stripped_title": "Medical Research Fundraiser", "text": "Gain 8[credit]. The Runner gains 3[credit].", "title": "Medical Research Fundraiser", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_mushin_no_shin_05015(Operation):
    '''
    Cost: 0
    Text: As an additional cost to play this operation, spend click. Install 1 asset, agenda, or upgrade from HQ in the root of a new server. Place 3 advancement counters on that card. You cannot score or rez that card until your next turn begins.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05015", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "hap", "position": 15, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Install 1 asset, agenda, or upgrade from HQ in the root of a new server. Place 3 advancement counters on that card. You cannot score or rez that card until your next turn begins.", "stripped_title": "Mushin No Shin", "text": "As an additional cost to play this operation, spend [click].\nInstall 1 asset, agenda, or upgrade from HQ in the root of a new server. Place 3 advancement counters on that card. You cannot score or rez that card until your next turn begins.", "title": "Mushin No Shin", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_diversified_portfolio_05026(Operation):
    '''
    Cost: 1
    Text: Gain 1 credit for each remote server with a card in its root.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05026", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "YucaBean has seen astounding growth in even the most remote markets.", "illustrator": "Emilio Rodriguez", "keywords": "Transaction", "pack_code": "hap", "position": 26, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit for each remote server with a card in its root.", "stripped_title": "Diversified Portfolio", "text": "Gain 1[credit] for each remote server with a card in its root.", "title": "Diversified Portfolio", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_fast_track_05027(Operation):
    '''
    Cost: 0
    Text: Search R&D for an agenda, reveal it, and add it to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05027", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "The longer the employees didn't look at the Doomsday Clock, the more it gnawed at the back of their minds. A quick look only reinforced what they already knew: there wasn't enough time.", "illustrator": "Zefanya Langkan Maega", "pack_code": "hap", "position": 27, "quantity": 3, "side_code": "corp", "stripped_text": "Search R&D for an agenda, reveal it, and add it to HQ. Shuffle R&D.", "stripped_title": "Fast Track", "text": "Search R&D for an agenda, reveal it, and add it to HQ. Shuffle R&D.", "title": "Fast Track", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_mutate_06004(Operation):
    '''
    Cost: 2
    Text: As an additional cost to play this operation, trash a rezzed piece of ice. Reveal cards from the top of R&D until you reveal a piece of ice. Install and rez that ice in the same position as the ice that was trashed, ignoring all costs. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06004", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Hannah Christenson", "pack_code": "up", "position": 4, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, trash a rezzed piece of ice. Reveal cards from the top of R&D until you reveal a piece of ice. Install and rez that ice in the same position as the ice that was trashed, ignoring all costs. Shuffle R&D.", "stripped_title": "Mutate", "text": "As an additional cost to play this operation, trash a rezzed piece of ice.\nReveal cards from the top of R&D until you reveal a piece of ice. Install and rez that ice in the same position as the ice that was trashed, ignoring all costs. Shuffle R&D.", "title": "Mutate", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_bad_times_06012(Operation):
    '''
    Cost: 4
    Text: Play only if the Runner is tagged. The Runner's memory limit is reduced by 2 until the end of the turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06012", "cost": 4, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Known as malware 0-394-41525-6 to sysops, runners just refer to it as \"bad times.\"", "illustrator": "Adam S. Doyle", "keywords": "Gray Ops", "pack_code": "up", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. The Runner's memory limit is reduced by 2 until the end of the turn.", "stripped_title": "Bad Times", "text": "Play only if the Runner is tagged.\nThe Runner's memory limit is reduced by 2 until the end of the turn.", "title": "Bad Times", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_enhanced_login_protocol_06022(Operation):
    '''
    Cost: 2
    Text: This operation is not trashed until another current is played or an agenda is stolen. As an additional cost to take the basic action to run a server for the first time each turn, the Runner must spend click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06022", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Lili Ibrahim", "keywords": "Current", "pack_code": "tsb", "position": 22, "quantity": 3, "side_code": "corp", "stripped_text": "This operation is not trashed until another current is played or an agenda is stolen. As an additional cost to take the basic action to run a server for the first time each turn, the Runner must spend click.", "stripped_title": "Enhanced Login Protocol", "text": "This operation is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nAs an additional cost to take the basic action to run a server for the first time each turn, the Runner must spend [click].", "title": "Enhanced Login Protocol", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_cerebral_static_06025(Operation):
    '''
    Cost: 2
    Text: This operation is not trashed until another current is played or an agenda is stolen. The Runner's identity loses its printed abilities.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06025", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Her eyes were the color of a vidscreen, tuned to a dead channel.", "illustrator": "Lili Ibrahim", "keywords": "Current", "pack_code": "tsb", "position": 25, "quantity": 3, "side_code": "corp", "stripped_text": "This operation is not trashed until another current is played or an agenda is stolen. The Runner's identity loses its printed abilities.", "stripped_title": "Cerebral Static", "text": "This operation is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nThe Runner's identity loses its printed abilities.", "title": "Cerebral Static", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_targeted_marketing_06026(Operation):
    '''
    Cost: 0
    Text: This card is not trashed until another current is played or an agenda is stolen. Name a card. Gain 10 credits whenever the Runner plays or installs a copy of that card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06026", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Gong Studios", "keywords": "Current", "pack_code": "tsb", "position": 26, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. Name a card. Gain 10 credits whenever the Runner plays or installs a copy of that card.", "stripped_title": "Targeted Marketing", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nName a card. Gain 10[credit] whenever the Runner plays or installs a copy of that card.", "title": "Targeted Marketing", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_paywall_implementation_06028(Operation):
    '''
    Cost: 0
    Text: This card is not trashed until another current is played or an agenda is stolen. Gain 1 credit whenever the Runner makes a successful run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06028", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Gong Studios", "keywords": "Current - Transaction", "pack_code": "tsb", "position": 28, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. Gain 1 credit whenever the Runner makes a successful run.", "stripped_title": "Paywall Implementation", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nGain 1[credit] whenever the Runner makes a successful run.", "title": "Paywall Implementation", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_lag_time_06031(Operation):
    '''
    Cost: 2
    Text: This operation is not trashed until another current is played or an agenda is stolen. All ice have +1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06031", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"I don't care how good your console is, or how tricked out your rig is. The lag time on a run on the moon from earthside can be a killer.\" -Leela Patel", "illustrator": "Ed Mattinian", "keywords": "Current", "pack_code": "tsb", "position": 31, "quantity": 3, "side_code": "corp", "stripped_text": "This operation is not trashed until another current is played or an agenda is stolen. All ice have +1 strength.", "stripped_title": "Lag Time", "text": "This operation is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nAll <strong>ice</strong> have +1 strength.", "title": "Lag Time", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_manhunt_06046(Operation):
    '''
    Cost: 3
    Text: This card is not trashed until another current is played or an agenda is stolen. The first time the Runner makes a successful run each turn, Trace[2]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06046", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Mauricio Herrera", "keywords": "Current", "pack_code": "fc", "position": 46, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. The first time the Runner makes a successful run each turn, Trace[2]. If successful, give the Runner 1 tag.", "stripped_title": "Manhunt", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nThe first time the Runner makes a successful run each turn, Trace[2]. If successful, give the Runner 1 tag.", "title": "Manhunt", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_peak_efficiency_06062(Operation):
    '''
    Cost: 1
    Text: Gain 1 credit for each rezzed piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06062", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "\"Servers fully-armed and operational.\"", "illustrator": "Adam S. Doyle", "pack_code": "uao", "position": 62, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit for each rezzed piece of ice.", "stripped_title": "Peak Efficiency", "text": "Gain 1[credit] for each rezzed piece of ice.", "title": "Peak Efficiency", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_reuse_06070(Operation):
    '''
    Cost: 0
    Text: As an additional cost to play this operation, spend click. Trash any number of cards from HQ. Gain 2 credits for each card trashed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06070", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "If the clones were nervous about living in a repurposed fuel tank, they never mentioned it.", "illustrator": "Yip Lee", "keywords": "Double", "pack_code": "uao", "position": 70, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Trash any number of cards from HQ. Gain 2 credits for each card trashed.", "stripped_title": "Reuse", "text": "As an additional cost to play this operation, spend [click].\nTrash any number of cards from HQ. Gain 2[credit] for each card trashed.", "title": "Reuse", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_snatch_and_grab_06090(Operation):
    '''
    Cost: 0
    Text: Trace[3]. If successful, trash 1 connection. The Runner can take 1 tag to prevent this.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06090", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "The last thing he saw was the tattoo of a strange beast on his captor's neck. It had a goat's head, the body of a lion, and the tail of a serpent. Then the bag was yanked over his head, and there was only darkness.", "illustrator": "Adam Schumpert", "keywords": "Gray Ops", "pack_code": "atr", "position": 90, "quantity": 3, "side_code": "corp", "stripped_text": "Trace[3]. If successful, trash 1 connection. The Runner can take 1 tag to prevent this.", "stripped_title": "Snatch and Grab", "text": "Trace[3]. If successful, trash 1 <strong>connection</strong>. The Runner can take 1 tag to prevent this.", "title": "Snatch and Grab", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_shoot_the_moon_06107(Operation):
    '''
    Cost: 3
    Text: As an additional cost to play this operation, spend click. Rez 1 piece of ice for each tag the Runner has, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06107", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Beny Maulana", "keywords": "Double", "pack_code": "ts", "position": 107, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Rez 1 piece of ice for each tag the Runner has, ignoring all costs.", "stripped_title": "Shoot the Moon", "text": "As an additional cost to play this operation, spend [click].\nRez 1 piece of ice for each tag the Runner has, ignoring all costs.", "title": "Shoot the Moon", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_housekeeping_07020(Operation):
    '''
    Cost: 2
    Text: This operation is not trashed until another current is played or an agenda is stolen. The first time each turn the Runner installs a card, they trash 1 card from the grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07020", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Tey Bartolome", "keywords": "Current - Gray Ops", "pack_code": "oac", "position": 20, "quantity": 3, "side_code": "corp", "stripped_text": "This operation is not trashed until another current is played or an agenda is stolen. The first time each turn the Runner installs a card, they trash 1 card from the grip.", "stripped_title": "Housekeeping", "text": "This operation is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nThe first time each turn the Runner installs a card, they trash 1 card from the grip.", "title": "Housekeeping", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_patch_07021(Operation):
    '''
    Cost: 0
    Text: Install Patch on a rezzed piece of ice as a hosted condition counter with the text "Host ice has +2 strength."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07021", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Update 1.1:\n-Fixes some stability issues. //maybe", "illustrator": "Andreas Zafiratos", "keywords": "Condition", "pack_code": "oac", "position": 21, "quantity": 3, "side_code": "corp", "stripped_text": "Install Patch on a rezzed piece of ice as a hosted condition counter with the text \"Host ice has +2 strength.\"", "stripped_title": "Patch", "text": "Install Patch on a rezzed piece of ice as a hosted condition counter with the text \"Host ice has +2 strength.\"", "title": "Patch", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_traffic_accident_07022(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner has at least 2 tags. Do 2 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07022", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"Traffic was murder.\"", "illustrator": "Alex Kim", "keywords": "Black Ops", "pack_code": "oac", "position": 22, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner has at least 2 tags. Do 2 meat damage.", "stripped_title": "Traffic Accident", "text": "Play only if the Runner has at least 2 tags.\nDo 2 meat damage.", "title": "Traffic Accident", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sub_boost_07025(Operation):
    '''
    Cost: 0
    Text: Install Sub Boost on a rezzed piece of ice as a hosted condition counter with the text "Host ice gains barrier and 'Subroutine End the run.' after all its other subroutines."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07025", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"It's fun watching them derez after hitting Enigma.\" -Grace Lamarr, Freelance Security Expert", "illustrator": "Smirtouille", "keywords": "Condition", "pack_code": "oac", "position": 25, "quantity": 3, "side_code": "corp", "stripped_text": "Install Sub Boost on a rezzed piece of ice as a hosted condition counter with the text \"Host ice gains barrier and 'Subroutine End the run.' after all its other subroutines.\"", "stripped_title": "Sub Boost", "text": "Install Sub Boost on a rezzed piece of ice as a hosted condition counter with the text \"Host ice gains <strong>barrier</strong> and '[subroutine] End the run.' after all its other subroutines.\"", "title": "Sub Boost", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_predictive_algorithm_08017(Operation):
    '''
    Cost: 0
    Text: This card is not trashed until another current is played or an agenda is stolen. As an additional cost to steal an agenda, the Runner must pay 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08017", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Ethan Patrick Harris", "keywords": "Current", "pack_code": "val", "position": 17, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. As an additional cost to steal an agenda, the Runner must pay 2 credits.", "stripped_title": "Predictive Algorithm", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nAs an additional cost to steal an agenda, the Runner must pay 2[credit].", "title": "Predictive Algorithm", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_recruiting_trip_08035(Operation):
    '''
    Cost: None
    Text: Search R&D for up to X different sysops (by title), reveal them, and add them to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08035", "cost": null, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"My script can perform the Kobayashi algorithm in .12 seconds.\"", "illustrator": "Dmitry Prosvirnin", "pack_code": "bb", "position": 35, "quantity": 3, "side_code": "corp", "stripped_text": "Search R&D for up to X different sysops (by title), reveal them, and add them to HQ. Shuffle R&D.", "stripped_title": "Recruiting Trip", "text": "Search R&D for up to X different <strong>sysops</strong> (by title), reveal them, and add them to HQ. Shuffle R&D.", "title": "Recruiting Trip", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_defective_brainchips_08072(Operation):
    '''
    Cost: 2
    Text: This operation is not trashed until another current is played or an agenda is stolen. Interrupt -> The first time each turn the Runner would suffer core damage, increase that damage by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08072", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "illustrator": "Sara K. Diesel", "keywords": "Current", "pack_code": "uw", "position": 72, "quantity": 3, "side_code": "corp", "stripped_text": "This operation is not trashed until another current is played or an agenda is stolen. Interrupt -> The first time each turn the Runner would suffer core damage, increase that damage by 1.", "stripped_title": "Defective Brainchips", "text": "This operation is not trashed until another <strong>current</strong> is played or an agenda is stolen.\n[interrupt] \u2192 The first time each turn the Runner would suffer core damage, increase that damage by 1.", "title": "Defective Brainchips", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_an_offer_you_cant_refuse_08091(Operation):
    '''
    Cost: 4
    Text: Choose a central server. The Runner may run that server. They cannot jack out during that run. If no run is made this way, add this operation to your score area as an agenda worth 1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08091", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "A. Jones", "pack_code": "oh", "position": 91, "quantity": 3, "side_code": "corp", "stripped_text": "Choose a central server. The Runner may run that server. They cannot jack out during that run. If no run is made this way, add this operation to your score area as an agenda worth 1 agenda point.", "stripped_title": "An Offer You Can't Refuse", "text": "Choose a central server. The Runner may run that server. They cannot jack out during that run. If no run is made this way, add this operation to your score area as an agenda worth 1 agenda point.", "title": "An Offer You Can't Refuse", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_casting_call_08096(Operation):
    '''
    Cost: 0
    Text: Install 1 agenda from HQ faceup and host this operation on that agenda as a condition counter with "Whenever the Runner accesses host agenda, they take 2 tags."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08096", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Smirtouille", "keywords": "Condition", "pack_code": "oh", "position": 96, "quantity": 3, "side_code": "corp", "stripped_text": "Install 1 agenda from HQ faceup and host this operation on that agenda as a condition counter with \"Whenever the Runner accesses host agenda, they take 2 tags.\"", "stripped_title": "Casting Call", "text": "Install 1 agenda from HQ faceup and host this operation on that agenda as a condition counter with \"Whenever the Runner accesses host agenda, they take 2 tags.\"", "title": "Casting Call", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_back_channels_08099(Operation):
    '''
    Cost: 0
    Text: Choose 1 card in the root of a remote server. Gain 3 credits for each advancement counter on that card, then trash it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08099", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Sometimes corps have to bury projects, but that doesn't mean they can't make a profit on them.", "illustrator": "Smirtouille", "keywords": "Transaction", "pack_code": "oh", "position": 99, "quantity": 3, "side_code": "corp", "stripped_text": "Choose 1 card in the root of a remote server. Gain 3 credits for each advancement counter on that card, then trash it.", "stripped_title": "Back Channels", "text": "Choose 1 card in the root of a remote server. Gain 3[credit] for each advancement counter on that card, then trash it.", "title": "Back Channels", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_247_news_cycle_09019(Operation):
    '''
    Cost: 0
    Text: As an additional cost to play 24/7 News Cycle, forfeit an agenda. Resolve the "when scored" ability on an agenda in your score area.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09019", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "The only thing worse than bad news...", "illustrator": "Thomas Williams", "pack_code": "dad", "position": 19, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play 24/7 News Cycle, forfeit an agenda. Resolve the \"when scored\" ability on an agenda in your score area.", "stripped_title": "24/7 News Cycle", "text": "As an additional cost to play 24/7 News Cycle, forfeit an agenda.\nResolve the \"when scored\" ability on an agenda in your score area.", "title": "24/7 News Cycle", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_ad_blitz_09020(Operation):
    '''
    Cost: None
    Text: As an additional cost to play this operation, spend click. Install and rez (paying all costs) X advertisements from Archives and/or HQ, if able.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09020", "cost": null, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Johan T\u00f6rnlund", "keywords": "Double", "pack_code": "dad", "position": 20, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Install and rez (paying all costs) X advertisements from Archives and/or HQ, if able.", "stripped_title": "Ad Blitz", "text": "As an additional cost to play this operation, spend [click].\nInstall and rez (paying all costs) X <strong>advertisements</strong> from Archives and/or HQ, if able.", "title": "Ad Blitz", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_media_blitz_09021(Operation):
    '''
    Cost: 2
    Text: This card is not trashed until another current is played or an agenda is stolen. Choose an agenda in the Runner's score area. Media Blitz gains the text of that agenda.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09021", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Dmitry Prosvirnin", "keywords": "Current", "pack_code": "dad", "position": 21, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. Choose an agenda in the Runner's score area. Media Blitz gains the text of that agenda.", "stripped_title": "Media Blitz", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nChoose an agenda in the Runner's score area. Media Blitz gains the text of that agenda.", "title": "Media Blitz", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_the_allseeing_i_09022(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner is tagged. Trash all resources. The Runner can remove 1 bad publicity to prevent this.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09022", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"Only with perfect information can we develop the perfect strategy.\" -The Playbook", "illustrator": "Matt Zeilinger", "pack_code": "dad", "position": 22, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Trash all resources. The Runner can remove 1 bad publicity to prevent this.", "stripped_title": "The All-Seeing I", "text": "Play only if the Runner is tagged.\nTrash all resources. The Runner can remove 1 bad publicity to prevent this.", "title": "The All-Seeing I", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_surveillance_sweep_09023(Operation):
    '''
    Cost: 2
    Text: This card is not trashed until another current is played or an agenda is stolen. The Runner must spend credits first for each trace attempt during a run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09023", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Simon Weaner", "keywords": "Current", "pack_code": "dad", "position": 23, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. The Runner must spend credits first for each trace attempt during a run.", "stripped_title": "Surveillance Sweep", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nThe Runner must spend credits first for each trace attempt during a run.", "title": "Surveillance Sweep", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_heritage_committee_10013(Operation):
    '''
    Cost: 1
    Text: This card costs 0 influence if you have 6 or more non-alliance jinteki cards in your deck. Draw 3 cards. Add 1 card from HQ to the top of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10013", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "It is only by respecting the past that we can build a better future.", "illustrator": "Anastasia Ovchinnikova", "keywords": "Alliance", "pack_code": "kg", "position": 13, "quantity": 3, "side_code": "corp", "stripped_text": "This card costs 0 influence if you have 6 or more non-alliance jinteki cards in your deck. Draw 3 cards. Add 1 card from HQ to the top of R&D.", "stripped_title": "Heritage Committee", "text": "This card costs 0 influence if you have 6 or more non-<strong>alliance</strong> [jinteki] cards in your deck.\nDraw 3 cards. Add 1 card from HQ to the top of R&D.", "title": "Heritage Committee", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_dedication_ceremony_10017(Operation):
    '''
    Cost: 1
    Text: Place 3 advancement tokens on a faceup card. You cannot score that card until your next turn begins.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10017", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "\"Never cut the ribbon until you have something to show off.\" -Eta Shah, VP Global Expansion", "illustrator": "Odera Igbokwe", "pack_code": "kg", "position": 17, "quantity": 3, "side_code": "corp", "stripped_text": "Place 3 advancement tokens on a faceup card. You cannot score that card until your next turn begins.", "stripped_title": "Dedication Ceremony", "text": "Place 3 advancement tokens on a faceup card. You cannot score that card until your next turn begins.", "title": "Dedication Ceremony", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_product_recall_10029(Operation):
    '''
    Cost: 0
    Text: This card costs 0 influence if you have 6 or more non-alliancehaas-bioroid cards in your deck. Trash a rezzed asset or upgrade. If you do, gain credits equal to its trash cost.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10029", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Antonio De Luca", "keywords": "Alliance", "pack_code": "bf", "position": 29, "quantity": 3, "side_code": "corp", "stripped_text": "This card costs 0 influence if you have 6 or more non-alliancehaas-bioroid cards in your deck. Trash a rezzed asset or upgrade. If you do, gain credits equal to its trash cost.", "stripped_title": "Product Recall", "text": "This card costs 0 influence if you have 6 or more non-<strong>alliance</strong>\u00a0[haas-bioroid] cards in your deck.\nTrash a rezzed asset or upgrade. If you do, gain credits equal to its trash cost.", "title": "Product Recall", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_clones_are_not_people_10052(Operation):
    '''
    Cost: 3
    Text: This card is not trashed until another current is played or an agenda is stolen. When you score an agenda, add "Clones are not People" to your score area as an agenda worth 1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10052", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Lars Bundvad", "keywords": "Current", "pack_code": "dag", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. When you score an agenda, add \"Clones are not People\" to your score area as an agenda worth 1 agenda point.", "stripped_title": "\"Clones are not People\"", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nWhen you score an agenda, add \"Clones are not People\" to your score area as an agenda worth 1 agenda point.", "title": "\"Clones are not People\"", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_salems_hospitality_10071(Operation):
    '''
    Cost: 2
    Text: This operation costs 0 influence if you have 6 or more non-alliance nbn cards in your deck. Choose a card name. The Runner reveals the grip and trashes all cards with the chosen name revealed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10071", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "illustrator": "Samuel Leung", "keywords": "Alliance - Gray Ops", "pack_code": "si", "position": 71, "quantity": 3, "side_code": "corp", "stripped_text": "This operation costs 0 influence if you have 6 or more non-alliance nbn cards in your deck. Choose a card name. The Runner reveals the grip and trashes all cards with the chosen name revealed this way.", "stripped_title": "Salem's Hospitality", "text": "This operation costs 0 influence if you have 6 or more non-<strong>alliance</strong> [nbn] cards in your deck.\nChoose a card name. The Runner reveals the grip and trashes all cards with the chosen name revealed this way.", "title": "Salem's Hospitality", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_localized_product_line_10075(Operation):
    '''
    Cost: 4
    Text: Search R&D for any number of copies of a card, reveal them, and add them to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10075", "cost": 4, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 3, "flavor": "It's the exact same coffee, but the price sure is different.", "illustrator": "Tim Durning", "pack_code": "si", "position": 75, "quantity": 3, "side_code": "corp", "stripped_text": "Search R&D for any number of copies of a card, reveal them, and add them to HQ. Shuffle R&D.", "stripped_title": "Localized Product Line", "text": "Search R&D for any number of copies of a card, reveal them, and add them to HQ. Shuffle R&D.", "title": "Localized Product Line", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_exchange_of_information_10092(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner is tagged. Swap an agenda in your score area with an agenda in the Runner's score area.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10092", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Del Borovic", "keywords": "Gray Ops", "pack_code": "tlm", "position": 92, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Swap an agenda in your score area with an agenda in the Runner's score area.", "stripped_title": "Exchange of Information", "text": "Play only if the Runner is tagged.\nSwap an agenda in your score area with an agenda in the Runner's score area.", "title": "Exchange of Information", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_consulting_visit_10094(Operation):
    '''
    Cost: 2
    Text: This card costs 0 influence if you have 6 or more non-alliance weyland-consortium cards in your deck. As an additional cost to play this operation, spend click. Search R&D for an operation and play it (paying all costs). Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10094", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Marya Yartseva", "keywords": "Alliance - Double", "pack_code": "tlm", "position": 94, "quantity": 3, "side_code": "corp", "stripped_text": "This card costs 0 influence if you have 6 or more non-alliance weyland-consortium cards in your deck. As an additional cost to play this operation, spend click. Search R&D for an operation and play it (paying all costs). Shuffle R&D.", "stripped_title": "Consulting Visit", "text": "This card costs 0 influence if you have 6 or more non-<strong>alliance</strong> [weyland-consortium] cards in your deck.\nAs an additional cost to play this operation, spend [click].\nSearch R&D for an operation and play it (paying all costs). Shuffle R&D.", "title": "Consulting Visit", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_lateral_growth_10104(Operation):
    '''
    Cost: 2
    Text: Gain 4 credits. You may install 1 card (paying the install cost).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10104", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Practical effects are expensive, but worth it. I had to smash seventeen stunt bioroids to get this shot.\" -Parvati Kapoor, director", "illustrator": "Antonio De Luca", "keywords": "Transaction", "pack_code": "ftm", "position": 104, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 4 credits. You may install 1 card (paying the install cost).", "stripped_title": "Lateral Growth", "text": "Gain 4[credit]. You may install 1 card (paying the install cost).", "title": "Lateral Growth", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_voter_intimidation_10106(Operation):
    '''
    Cost: 1
    Text: Play only if there is an agenda in the Runner's score area. You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, trash 1 resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10106", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "JuanManuel Tumburus", "keywords": "Gray Ops - Psi", "pack_code": "ftm", "position": 106, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if there is an agenda in the Runner's score area. You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, trash 1 resource.", "stripped_title": "Voter Intimidation", "text": "Play only if there is an agenda in the Runner's score area.\nYou and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, trash 1 resource.", "title": "Voter Intimidation", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_election_day_10112(Operation):
    '''
    Cost: 0
    Text: Trash all cards in HQ (minimum of 1). Draw 5 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10112", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"A new administration means we have to start greasing the wheels all over again. Let's get to work.\"", "illustrator": "Del Borovic", "pack_code": "ftm", "position": 112, "quantity": 3, "side_code": "corp", "stripped_text": "Trash all cards in HQ (minimum of 1). Draw 5 cards.", "stripped_title": "Election Day", "text": "Trash all cards in HQ (minimum of 1). Draw 5 cards.", "title": "Election Day", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_subcontract_10113(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner is tagged. Play up to 2 operations from HQ (paying all costs), resolving them one at a time.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10113", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "Judicious use of freelancers can increase efficiency and protect the company from legal repercussions. It's what they call a \"win-win\".", "illustrator": "Matt Zeilinger", "keywords": "Gray Ops", "pack_code": "ftm", "position": 113, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Play up to 2 operations from HQ (paying all costs), resolving them one at a time.", "stripped_title": "Subcontract", "text": "Play only if the Runner is tagged.\nPlay up to 2 operations from HQ (paying all costs), resolving them one at a time.", "title": "Subcontract", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hardhitting_news_11016(Operation):
    '''
    Cost: 3
    Text: After you resolve this operation, your action phase ends. Play only if the Runner made a run during their last turn. Trace[4]. If successful, give the Runner 4 tags.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11016", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Sander Mosk", "keywords": "Terminal", "pack_code": "23s", "position": 16, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, your action phase ends. Play only if the Runner made a run during their last turn. Trace[4]. If successful, give the Runner 4 tags.", "stripped_title": "Hard-Hitting News", "text": "After you resolve this operation, your action phase ends.\nPlay only if the Runner made a run during their last turn.\nTrace[4]. If successful, give the Runner 4 tags.", "title": "Hard-Hitting News", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_stock_buyback_11019(Operation):
    '''
    Cost: 1
    Text: After you resolve this operation, end your action phase. Gain 3 credits for each agenda in the Runner's score area.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11019", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "A stock dropping sharply is bad for shareholders, but not neccessarily bad for the company.", "illustrator": "RC Torres", "keywords": "Terminal - Transaction", "pack_code": "23s", "position": 19, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, end your action phase. Gain 3 credits for each agenda in the Runner's score area.", "stripped_title": "Stock Buy-Back", "text": "After you resolve this operation, end your action phase.\nGain 3[credit] for each agenda in the Runner's score area.", "title": "Stock Buy-Back", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_enforcing_loyalty_11033(Operation):
    '''
    Cost: 2
    Text: As an additional cost to play this operation, spend click. Trace[3]. If successful, trash an installed card that does not match the faction of the Runner's identity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11033", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"Eiko here. It's done.\"", "illustrator": "Adam Schumpert", "keywords": "Double - Gray Ops", "pack_code": "bm", "position": 33, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Trace[3]. If successful, trash an installed card that does not match the faction of the Runner's identity.", "stripped_title": "Enforcing Loyalty", "text": "As an additional cost to play this operation, spend [click].\nTrace[3]. If successful, trash an installed card that does not match the faction of the Runner's identity.", "title": "Enforcing Loyalty", "trash_cost": 1, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hatchet_job_11034(Operation):
    '''
    Cost: 2
    Text: As an additional cost to play this operation, spend click. Trace[5]. If successful, add an installed non-virtual card to the Runner's grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11034", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"SELL!! Buy platinum, but GET OUT OF THE TT CREDIT! It is TOXIC!\"", "illustrator": "Gary Bedell", "keywords": "Double - Gray Ops", "pack_code": "bm", "position": 34, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Trace[5]. If successful, add an installed non-virtual card to the Runner's grip.", "stripped_title": "Hatchet Job", "text": "As an additional cost to play this operation, spend [click].\nTrace[5]. If successful, add an installed non-<strong>virtual</strong> card to the Runner's grip.", "title": "Hatchet Job", "trash_cost": 0, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_special_report_11035(Operation):
    '''
    Cost: 1
    Text: Shuffle any number of cards from HQ into R&D. Draw that number of cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11035", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "By the time the report of Emelyov's murder was produced, there had already been a dozen more, hitting all the corps.", "illustrator": "Aurore Folny", "pack_code": "bm", "position": 35, "quantity": 3, "side_code": "corp", "stripped_text": "Shuffle any number of cards from HQ into R&D. Draw that number of cards.", "stripped_title": "Special Report", "text": "Shuffle any number of cards from HQ into R&D. Draw that number of cards.", "title": "Special Report", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_liquidation_11037(Operation):
    '''
    Cost: 1
    Text: As an additional cost to play this operation, spend click. Trash any number of your rezzed cards and gain 3 credits for each card trashed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11037", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "What's a little insurance fraud between friends?", "illustrator": "Pavel Kolomeyets", "keywords": "Double - Gray Ops - Transaction", "pack_code": "bm", "position": 37, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Trash any number of your rezzed cards and gain 3 credits for each card trashed.", "stripped_title": "Liquidation", "text": "As an additional cost to play this operation, spend [click].\nTrash any number of your rezzed cards and gain 3[credit] for each card trashed.", "title": "Liquidation", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_financial_collapse_11039(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner has at least 6 credits. The Runner loses 2 credits for each installed resource. The Runner can trash a resource to prevent this.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11039", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "She'd never heard her dads argue like this. Not ever. She'd give anything to make it stop.", "illustrator": "Matt Zeilinger", "pack_code": "bm", "position": 39, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner has at least 6 credits. The Runner loses 2 credits for each installed resource. The Runner can trash a resource to prevent this.", "stripped_title": "Financial Collapse", "text": "Play only if the Runner has at least 6[credit].\nThe Runner loses 2[credit] for each installed resource. The Runner can trash a resource to prevent this.", "title": "Financial Collapse", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_ark_lockdown_11050(Operation):
    '''
    Cost: 1
    Text: Name a card. Remove all copies of that card in the heap from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11050", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"If you live off-site, please consult the building AI for temporary housing. We regret that your off-site family cannot join you here while we are in lockdown...\"", "illustrator": "Johan T\u00f6rnlund", "pack_code": "es", "position": 50, "quantity": 3, "side_code": "corp", "stripped_text": "Name a card. Remove all copies of that card in the heap from the game.", "stripped_title": "Ark Lockdown", "text": "Name a card. Remove all copies of that card in the heap from the game.", "title": "Ark Lockdown", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hellion_beta_test_11051(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner trashed a card while accessing it during their last turn. Trace[2]. If successful, trash 2 installed non-program cards. If unsuccessful, take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11051", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"Wait a minute, I don't even have a cat.\"", "illustrator": "VIKO", "keywords": "Black Ops", "pack_code": "es", "position": 51, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner trashed a card while accessing it during their last turn. Trace[2]. If successful, trash 2 installed non-program cards. If unsuccessful, take 1 bad publicity.", "stripped_title": "Hellion Beta Test", "text": "Play only if the Runner trashed a card while accessing it during their last turn.\nTrace[2]. If successful, trash 2 installed non-program cards. If unsuccessful, take 1 bad publicity.", "title": "Hellion Beta Test", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_observe_and_destroy_11056(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner has fewer than 6 credits. As an additional cost to play this operation, remove 1 tag. Trash 1 installed card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11056", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Observing is fun, but it's just the appetizer.", "illustrator": "Antonio De Luca", "keywords": "Gray Ops", "pack_code": "es", "position": 56, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner has fewer than 6 credits. As an additional cost to play this operation, remove 1 tag. Trash 1 installed card.", "stripped_title": "Observe and Destroy", "text": "Play only if the Runner has fewer than 6[credit].\nAs an additional cost to play this operation, remove 1 tag.\nTrash 1 installed card.", "title": "Observe and Destroy", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_service_outage_11057(Operation):
    '''
    Cost: 1
    Text: This operation is not trashed until another current is played or an agenda is stolen. As an additional cost to run for the first time during their turn, the Runner must spend 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11057", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Samuel Leung", "keywords": "Current", "pack_code": "es", "position": 57, "quantity": 3, "side_code": "corp", "stripped_text": "This operation is not trashed until another current is played or an agenda is stolen. As an additional cost to run for the first time during their turn, the Runner must spend 1 credit.", "stripped_title": "Service Outage", "text": "This operation is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nAs an additional cost to run for the first time during their turn, the Runner must spend 1[credit].", "title": "Service Outage", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_boom_11058(Operation):
    '''
    Cost: 4
    Text: Play only if the Runner has at least 2 tags. As an additional cost to play this operation, spend click. Do 7 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11058", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "Game over.", "illustrator": "JuanManuel Tumburus", "keywords": "Double - Black Ops", "pack_code": "es", "position": 58, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner has at least 2 tags. As an additional cost to play this operation, spend click. Do 7 meat damage.", "stripped_title": "BOOM!", "text": "Play only if the Runner has at least 2 tags.\nAs an additional cost to play this operation, spend [click].\nDo 7 meat damage.", "title": "BOOM!", "trash_cost": 1, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_door_to_door_11059(Operation):
    '''
    Cost: 3
    Text: This card is not trashed until another current is played or an agenda is stolen. When the Runner's turn begins, Trace[1]. If successful, do 1 meat damage if the Runner is tagged; otherwise, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11059", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Maciej Rebisz", "keywords": "Current - Black Ops", "pack_code": "es", "position": 59, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. When the Runner's turn begins, Trace[1]. If successful, do 1 meat damage if the Runner is tagged; otherwise, give the Runner 1 tag.", "stripped_title": "Door to Door", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nWhen the Runner's turn begins, Trace[1]. If successful, do 1 meat damage if the Runner is tagged; otherwise, give the Runner 1 tag.", "title": "Door to Door", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_scarcity_of_resources_11060(Operation):
    '''
    Cost: 1
    Text: This card is not trashed until another current is played or an agenda is stolen. The install cost of each resource is increased by 2.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11060", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "The event is now referred to as the Water Tower Massacre. No one was ever indicted, and no one knows who paid the prisec team responsible.", "illustrator": "Maciej Rebisz", "keywords": "Current", "pack_code": "es", "position": 60, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. The install cost of each resource is increased by 2.", "stripped_title": "Scarcity of Resources", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nThe install cost of each resource is increased by 2.", "title": "Scarcity of Resources", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_wetwork_refit_11071(Operation):
    '''
    Cost: 1
    Text: Host this operation on a rezzed piece of bioroid ice as a condition counter with "Host ice gains 'Subroutine Do 1 core damage.' before all its other subroutines."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11071", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"I let the bioroids do a ride-along via remote, so they can see what pain really looks like.\" -Agent Valkyrie", "illustrator": "Antonio De Luca", "keywords": "Condition", "pack_code": "in", "position": 71, "quantity": 3, "side_code": "corp", "stripped_text": "Host this operation on a rezzed piece of bioroid ice as a condition counter with \"Host ice gains 'Subroutine Do 1 core damage.' before all its other subroutines.\"", "stripped_title": "Wetwork Refit", "text": "Host this operation on a rezzed piece of <strong>bioroid</strong> ice as a condition counter with \"Host ice gains '[subroutine] Do 1 core damage.' before all its other subroutines.\"", "title": "Wetwork Refit", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hasty_relocation_11074(Operation):
    '''
    Cost: 0
    Text: As an additional cost to play this operation, trash the top card of R&D. Draw 3 cards. Add 3 cards from HQ to the top of R&D in any order.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11074", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"Keep your head down, keep moving, try not to attract attention.\"", "illustrator": "Juan Novelletto", "pack_code": "in", "position": 74, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, trash the top card of R&D. Draw 3 cards. Add 3 cards from HQ to the top of R&D in any order.", "stripped_title": "Hasty Relocation", "text": "As an additional cost to play this operation, trash the top card of R&D.\nDraw 3 cards. Add 3 cards from HQ to the top of R&D in any order.", "title": "Hasty Relocation", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_best_defense_11079(Operation):
    '''
    Cost: 2
    Text: Trash 1 installed card with an install cost equal to or less than the number of tags the Runner has.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11079", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "When a shooting war threatens, the prudent course is to shoot first.", "illustrator": "Kate Laird", "keywords": "Gray Ops", "pack_code": "in", "position": 79, "quantity": 3, "side_code": "corp", "stripped_text": "Trash 1 installed card with an install cost equal to or less than the number of tags the Runner has.", "stripped_title": "Best Defense", "text": "Trash 1 installed card with an install cost equal to or less than the number of tags the Runner has.", "title": "Best Defense", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_preemptive_action_11080(Operation):
    '''
    Cost: 0
    Text: After you resolve this operation, end your action phase. Shuffle 3 cards from Archives into R&D. Remove Preemptive Action from the game instead of trashing it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11080", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "VIKO", "keywords": "Terminal", "pack_code": "in", "position": 80, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, end your action phase. Shuffle 3 cards from Archives into R&D. Remove Preemptive Action from the game instead of trashing it.", "stripped_title": "Preemptive Action", "text": "After you resolve this operation, end your action phase.\nShuffle 3 cards from Archives into R&D. Remove Preemptive Action from the game instead of trashing it.", "title": "Preemptive Action", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_friends_in_high_places_11090(Operation):
    '''
    Cost: 2
    Text: After you resolve this operation, end your action phase. Install up to 2 cards from Archives (paying all install costs).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11090", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Friends give friends advance warning before moving a carrier group down to enforce a no-fly zone.", "illustrator": "Simon Weaner", "keywords": "Terminal", "pack_code": "ml", "position": 90, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, end your action phase. Install up to 2 cards from Archives (paying all install costs).", "stripped_title": "Friends in High Places", "text": "After you resolve this operation, end your action phase.\nInstall up to 2 cards from Archives (paying all install costs).", "title": "Friends in High Places", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_enforced_curfew_11100(Operation):
    '''
    Cost: 0
    Text: This card is not trashed until another current is played or an agenda is stolen. The Runner's maximum hand size is reduced by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11100", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Get those civilians off the street. No more collateral damage.\" -Commissioner Dawn", "illustrator": "Sander Mosk", "keywords": "Current", "pack_code": "ml", "position": 100, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. The Runner's maximum hand size is reduced by 1.", "stripped_title": "Enforced Curfew", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nThe Runner's maximum hand size is reduced by 1.", "title": "Enforced Curfew", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_violet_level_clearance_11111(Operation):
    '''
    Cost: 5
    Text: After you resolve this operation, end your action phase. Gain 8 credits and draw 4 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11111", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "It required a hexadecimal code along with biometrics, delivered by way of BMI.", "illustrator": "Andreas Zafiratos", "keywords": "Terminal - Transaction", "pack_code": "qu", "position": 111, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, end your action phase. Gain 8 credits and draw 4 cards.", "stripped_title": "Violet Level Clearance", "text": "After you resolve this operation, end your action phase.\nGain 8[credit] and draw 4 cards.", "title": "Violet Level Clearance", "trash_cost": 1, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_psychokinesis_11113(Operation):
    '''
    Cost: 1
    Text: After you resolve this operation, end your action phase. Look at the top 5 cards of R&D. If any of those cards are agendas, assets, or upgrades, you may install 1 of those cards in a remote server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11113", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Dmitry Burmak", "keywords": "Terminal", "pack_code": "qu", "position": 113, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, end your action phase. Look at the top 5 cards of R&D. If any of those cards are agendas, assets, or upgrades, you may install 1 of those cards in a remote server.", "stripped_title": "Psychokinesis", "text": "After you resolve this operation, end your action phase.\nLook at the top 5 cards of R&D. If any of those cards are agendas, assets, or upgrades, you may install 1 of those cards in a remote server.", "title": "Psychokinesis", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_load_testing_12031(Operation):
    '''
    Cost: 0
    Text: When the Runner's next turn begins, they lose click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12031", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "flavor": "\"Trust me, most corps cannot match the performance of our brainmap enhanced system; a home-brewed rig doesn't stand a chance.\" - Rachel Giacomin", "illustrator": "Ed Mattinian", "pack_code": "so", "position": 31, "quantity": 3, "side_code": "corp", "stripped_text": "When the Runner's next turn begins, they lose click.", "stripped_title": "Load Testing", "text": "When the Runner's next turn begins, they lose [click].", "title": "Load Testing", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_replanting_12033(Operation):
    '''
    Cost: 1
    Text: As an additional cost to play this operation, spend click. Add one of your installed cards to HQ. Install 2 cards from HQ, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12033", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Mark Molnar", "keywords": "Double", "pack_code": "so", "position": 33, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Add one of your installed cards to HQ. Install 2 cards from HQ, ignoring all costs.", "stripped_title": "Replanting", "text": "As an additional cost to play this operation, spend [click].\nAdd one of your installed cards to HQ. Install 2 cards from HQ, ignoring all costs.", "title": "Replanting", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_mca_informant_12036(Operation):
    '''
    Cost: 4
    Text: After you resolve this operation, your action phase ends. Host this operation on an installed connection resource as a condition counter with "The Runner is considered to have 1 additional tag. Host resource gains 'click, 2 credits: Trash this resource.'"
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12036", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Limetown Studios", "keywords": "Terminal", "pack_code": "so", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, your action phase ends. Host this operation on an installed connection resource as a condition counter with \"The Runner is considered to have 1 additional tag. Host resource gains 'click, 2 credits: Trash this resource.'\"", "stripped_title": "MCA Informant", "text": "After you resolve this operation, your action phase ends.\nHost this operation on an installed <strong>connection</strong> resource as a condition counter with \"The Runner is considered to have 1 additional tag. Host resource gains '<strong>[click]</strong>, <strong>2[credit]:</strong> Trash this resource.'\"", "title": "MCA Informant", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sacrifice_12039(Operation):
    '''
    Cost: 0
    Text: As an additional cost to play this operation, forfeit an agenda. Remove 1 bad publicity per agenda point that the forfeited agenda was worth. Gain 1 credit for each bad publicity removed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12039", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "illustrator": "Martin de Diego S\u00e1daba", "pack_code": "so", "position": 39, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, forfeit an agenda. Remove 1 bad publicity per agenda point that the forfeited agenda was worth. Gain 1 credit for each bad publicity removed.", "stripped_title": "Sacrifice", "text": "As an additional cost to play this operation, forfeit an agenda.\nRemove 1 bad publicity per agenda point that the forfeited agenda was worth. Gain 1[credit] for each bad publicity removed.", "title": "Sacrifice", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_audacity_12058(Operation):
    '''
    Cost: 0
    Text: Play only if there are at least 2 other cards in HQ. Trash all cards from HQ. Place a total of 2 advancement counters on installed cards you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12058", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "Ed Mattinian", "pack_code": "eas", "position": 58, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if there are at least 2 other cards in HQ. Trash all cards from HQ. Place a total of 2 advancement counters on installed cards you can advance.", "stripped_title": "Audacity", "text": "Play only if there are at least 2 other cards in HQ.\nTrash all cards from HQ. Place a total of 2 advancement counters on installed cards you can advance.", "title": "Audacity", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_red_planet_couriers_12059(Operation):
    '''
    Cost: 5
    Text: As an additional cost to play this operation, spend click, click. Move all advancement tokens from all installed cards to 1 card that can be advanced.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12059", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "Matt Zeilinger", "keywords": "Triple", "pack_code": "eas", "position": 59, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click, click. Move all advancement tokens from all installed cards to 1 card that can be advanced.", "stripped_title": "Red Planet Couriers", "text": "As an additional cost to play this operation, spend [click], [click].\nMove all advancement tokens from all installed cards to 1 card that can be advanced.", "title": "Red Planet Couriers", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_shipment_from_tennin_12072(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner did not make a successful run during their last turn. Place 2 advancement counters on 1 installed card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12072", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Jan-Wah Li", "pack_code": "baw", "position": 72, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner did not make a successful run during their last turn. Place 2 advancement counters on 1 installed card.", "stripped_title": "Shipment from Tennin", "text": "Play only if the Runner did not make a successful run during their last turn.\nPlace 2 advancement counters on 1 installed card.", "title": "Shipment from Tennin", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_success_12078(Operation):
    '''
    Cost: 0
    Text: As an additional cost to play this operation, forfeit an agenda and spend click click. Advance a card X times. X equals the advancement requirement of the agenda just forfeited.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12078", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "The difference between surviving and thriving is successful terraforming.", "illustrator": "Mark Molnar", "keywords": "Triple", "pack_code": "baw", "position": 78, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, forfeit an agenda and spend click click. Advance a card X times. X equals the advancement requirement of the agenda just forfeited.", "stripped_title": "Success", "text": "As an additional cost to play this operation, forfeit an agenda and spend [click][click].\nAdvance a card X times. X equals the advancement requirement of the agenda just forfeited.", "title": "Success", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_mass_commercialization_12080(Operation):
    '''
    Cost: 0
    Text: Gain 2 credits for each card with at least 1 advancement token on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12080", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Mark Molnar", "keywords": "Transaction", "pack_code": "baw", "position": 80, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 2 credits for each card with at least 1 advancement token on it.", "stripped_title": "Mass Commercialization", "text": "Gain 2[credit] for each card with at least 1 advancement token on it.", "title": "Mass Commercialization", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_o_shortage_12090(Operation):
    '''
    Cost: 3
    Text: The Runner may trash 1 card from the grip at random. If they do not, gain click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12090", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Is the lack of oxygen causing distress, friend?\"\n-Gregory 3D3R6Z", "illustrator": "Wenjuinn Png", "pack_code": "fm", "position": 90, "quantity": 3, "side_code": "corp", "stripped_text": "The Runner may trash 1 card from the grip at random. If they do not, gain click click.", "stripped_title": "O Shortage", "text": "The Runner may trash 1 card from the grip at random. If they do not, gain [click][click].", "title": "O\u2082 Shortage", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_biased_reporting_12096(Operation):
    '''
    Cost: 2
    Text: Choose resource, hardware, or program. The Runner may trash any of their installed cards of the chosen type and gain 1 credit for each card trashed this way. Gain 2 credits for each card of the chosen type that is still installed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12096", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Ed Mattinian", "pack_code": "fm", "position": 96, "quantity": 3, "side_code": "corp", "stripped_text": "Choose resource, hardware, or program. The Runner may trash any of their installed cards of the chosen type and gain 1 credit for each card trashed this way. Gain 2 credits for each card of the chosen type that is still installed.", "stripped_title": "Biased Reporting", "text": "Choose resource, hardware, or program. The Runner may trash any of their installed cards of the chosen type and gain 1[credit] for each card trashed this way. Gain 2[credit] for each card of the chosen type that is still installed.", "title": "Biased Reporting", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_transparency_initiative_12099(Operation):
    '''
    Cost: 0
    Text: Turn an agenda faceup and install Transparency Initiative on that agenda as a hosted condition counter with the text "Host agenda gains public. Whenever you advance host agenda, gain 1 credit."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12099", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "Ed Mattinian", "pack_code": "fm", "position": 99, "quantity": 3, "side_code": "corp", "stripped_text": "Turn an agenda faceup and install Transparency Initiative on that agenda as a hosted condition counter with the text \"Host agenda gains public. Whenever you advance host agenda, gain 1 credit.\"", "stripped_title": "Transparency Initiative", "text": "Turn an agenda faceup and install Transparency Initiative on that agenda as a hosted condition counter with the text \"Host agenda gains <strong>public</strong>. Whenever you advance host agenda, gain 1[credit].\"", "title": "Transparency Initiative", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_rover_algorithm_12100(Operation):
    '''
    Cost: 2
    Text: Install Rover Algorithm on a rezzed piece of ice as a hosted condition counter with the text "Host ice has +1 strength for each power counter on Rover Algorithm. Whenever the Runner passes host ice, place 1 power counter on Rover Algorithm."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12100", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Andreas Zafiratos", "pack_code": "fm", "position": 100, "quantity": 3, "side_code": "corp", "stripped_text": "Install Rover Algorithm on a rezzed piece of ice as a hosted condition counter with the text \"Host ice has +1 strength for each power counter on Rover Algorithm. Whenever the Runner passes host ice, place 1 power counter on Rover Algorithm.\"", "stripped_title": "Rover Algorithm", "text": "Install Rover Algorithm on a rezzed piece of ice as a hosted condition counter with the text \"Host ice has +1 strength for each power counter on Rover Algorithm. Whenever the Runner passes host ice, place 1 power counter on Rover Algorithm.\"", "title": "Rover Algorithm", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_restore_12112(Operation):
    '''
    Cost: 1
    Text: Install and rez 1 card from Archives (paying all costs). Remove all other copies of that card in Archives from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12112", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Dmitry Prosvirnin", "pack_code": "cd", "position": 112, "quantity": 3, "side_code": "corp", "stripped_text": "Install and rez 1 card from Archives (paying all costs). Remove all other copies of that card in Archives from the game.", "stripped_title": "Restore", "text": "Install and rez 1 card from Archives (paying all costs). Remove all other copies of that card in Archives from the game.", "title": "Restore", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_rolling_brownout_12116(Operation):
    '''
    Cost: 2
    Text: This card is not trashed until another current is played or an agenda is stolen. The play cost of each operation and event is increased by 1. The first time the Runner plays an event each turn, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12116", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Ed Mattinian", "keywords": "Current", "pack_code": "cd", "position": 116, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. The play cost of each operation and event is increased by 1. The first time the Runner plays an event each turn, gain 1 credit.", "stripped_title": "Rolling Brownout", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nThe play cost of each operation and event is increased by 1.\nThe first time the Runner plays an event each turn, gain 1[credit].", "title": "Rolling Brownout", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_threat_level_alpha_12117(Operation):
    '''
    Cost: 3
    Text: As an additional cost to play this operation, spend click. Trace[1]. If successful, give the Runner 1 tag for each tag they have or, if the Runner has no tags, give them 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12117", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Kate Laird", "keywords": "Double", "pack_code": "cd", "position": 117, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Trace[1]. If successful, give the Runner 1 tag for each tag they have or, if the Runner has no tags, give them 1 tag.", "stripped_title": "Threat Level Alpha", "text": "As an additional cost to play this operation, spend [click].\nTrace[1]. If successful, give the Runner 1 tag for each tag they have or, if the Runner has no tags, give them 1 tag.", "title": "Threat Level Alpha", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_priority_construction_12118(Operation):
    '''
    Cost: 1
    Text: As an additional cost to play this operation, spend click. Install a piece of ice from HQ protecting a remote server (ignoring all costs). Place 3 advancement tokens on that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12118", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "illustrator": "Pavel Kolomeyets", "keywords": "Double", "pack_code": "cd", "position": 118, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Install a piece of ice from HQ protecting a remote server (ignoring all costs). Place 3 advancement tokens on that ice.", "stripped_title": "Priority Construction", "text": "As an additional cost to play this operation, spend [click].\nInstall a piece of ice from HQ protecting a remote server (ignoring all costs). Place 3 advancement tokens on that ice.", "title": "Priority Construction", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_ultraviolet_clearance_13038(Operation):
    '''
    Cost: 6
    Text: As an additional cost to play this operation, spend click click. Gain 10 credits and draw 4 cards. You may install 1 card from HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13038", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "\"If there were hidden partitions on the server, I'd know; I'm the head of this department!\"", "illustrator": "Andreas Zafiratos", "keywords": "Transaction - Triple", "pack_code": "td", "position": 38, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click click. Gain 10 credits and draw 4 cards. You may install 1 card from HQ.", "stripped_title": "Ultraviolet Clearance", "text": "As an additional cost to play this operation, spend [click][click].\nGain 10[credit] and draw 4 cards. You may install 1 card from HQ.", "title": "Ultraviolet Clearance", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hunter_seeker_13051(Operation):
    '''
    Cost: 2
    Text: As an additional cost to play this operation, spend click. Play only if the Runner stole an agenda during their last turn. Trash 1 installed card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13051", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Micha\u0142 Mi\u0142kowski", "keywords": "Double - Gray Ops", "pack_code": "td", "position": 51, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Play only if the Runner stole an agenda during their last turn. Trash 1 installed card.", "stripped_title": "Hunter Seeker", "text": "As an additional cost to play this operation, spend [click].\nPlay only if the Runner stole an agenda during their last turn.\nTrash 1 installed card.", "title": "Hunter Seeker", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_ipo_13057(Operation):
    '''
    Cost: 8
    Text: After you resolve this operation, end your action phase. Gain 13 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13057", "cost": 8, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Mark Molnar", "keywords": "Terminal - Transaction", "pack_code": "td", "position": 57, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, end your action phase. Gain 13 credits.", "stripped_title": "IPO", "text": "After you resolve this operation, end your action phase.\nGain 13[credit].", "title": "IPO", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_net_watchlist_14023(Operation):
    '''
    Cost: 0
    Text: This card is not trashed until another current is played or an agenda is stolen. The Runner must pay 2 credits as an additional cost to use an icebreaker.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14023", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Adam S. Doyle", "keywords": "Current", "pack_code": "tdc", "position": 10, "quantity": 1, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. The Runner must pay 2 credits as an additional cost to use an icebreaker.", "stripped_title": "Net Watchlist", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nThe Runner must pay 2[credit] as an additional cost to use an icebreaker.", "title": "Net Watchlist", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_archived_memories_20071(Operation):
    '''
    Cost: 0
    Text: Add 1 card from Archives to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20071", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Do you think they\u2026feel it?\"", "illustrator": "Gong Studios", "pack_code": "core2", "position": 71, "quantity": 1, "side_code": "corp", "stripped_text": "Add 1 card from Archives to HQ.", "stripped_title": "Archived Memories", "text": "Add 1 card from Archives to HQ.", "title": "Archived Memories", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_biotic_labor_20072(Operation):
    '''
    Cost: 4
    Text: Gain click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20072", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "\"Why of course, we have six different Haas-Bioroid models serving in a variety of positions at this branch office alone. We here at Haas-Bioroid aren't going to shy away from practicing what we preach, and we pass the savings from increased efficiency on to our valued customers.\"", "illustrator": "Mark Anthony Taduran", "pack_code": "core2", "position": 72, "quantity": 2, "side_code": "corp", "stripped_text": "Gain click click.", "stripped_title": "Biotic Labor", "text": "Gain [click][click].", "title": "Biotic Labor", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_green_level_clearance_20073(Operation):
    '''
    Cost: 1
    Text: Gain 3 credits and draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20073", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Green-two clearance is the highest level of security a corp can gain access to. Legally, anyway.", "illustrator": "Adam S. Doyle", "keywords": "Transaction", "pack_code": "core2", "position": 73, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 3 credits and draw 1 card.", "stripped_title": "Green Level Clearance", "text": "Gain 3[credit] and draw 1 card.", "title": "Green Level Clearance", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_shipment_from_mirrormorph_20074(Operation):
    '''
    Cost: 1
    Text: Install up to 3 cards from HQ (one at a time and paying all install costs).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20074", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "The new heads were in. Their eyes always followed your movements when you unlocked the pressurized container and lifted the lid.", "illustrator": "Matt Zeilinger", "pack_code": "core2", "position": 74, "quantity": 1, "side_code": "corp", "stripped_text": "Install up to 3 cards from HQ (one at a time and paying all install costs).", "stripped_title": "Shipment from MirrorMorph", "text": "Install up to 3 cards from HQ (one at a time and paying all install costs).", "title": "Shipment from MirrorMorph", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_beanstalk_royalties_20090(Operation):
    '''
    Cost: 0
    Text: Gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20090", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "The New Angeles Space Elevator, better known as the Beanstalk, is the single greatest triumph of human engineering and ingenuity in history. The Beanstalk makes Earth orbit accessible to everyone\u2026for a small fee.", "illustrator": "Jonathan Lee", "keywords": "Transaction", "pack_code": "core2", "position": 121, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 3 credits.", "stripped_title": "Beanstalk Royalties", "text": "Gain 3[credit].", "title": "Beanstalk Royalties", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_punitive_counterstrike_20091(Operation):
    '''
    Cost: 3
    Text: Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20091", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"I'd say it's nothing personal, but corporations are people, too.\"", "illustrator": "Lorraine Schleter", "keywords": "Black Ops", "pack_code": "core2", "position": 122, "quantity": 2, "side_code": "corp", "stripped_text": "Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.", "stripped_title": "Punitive Counterstrike", "text": "Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.", "title": "Punitive Counterstrike", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_shipment_from_kaguya_20092(Operation):
    '''
    Cost: 0
    Text: Place 1 advancement token on each of up to 2 different installed cards that can be advanced.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20092", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"And then there's these two crates. No eID.\"\n\"Just leave those with me and forget you ever saw them.\"", "illustrator": "Andrew Mar", "pack_code": "core2", "position": 123, "quantity": 2, "side_code": "corp", "stripped_text": "Place 1 advancement token on each of up to 2 different installed cards that can be advanced.", "stripped_title": "Shipment from Kaguya", "text": "Place 1 advancement token on each of up to 2 different installed cards that can be advanced.", "title": "Shipment from Kaguya", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_celebrity_gift_20105(Operation):
    '''
    Cost: 3
    Text: As an additional cost to play this operation, spend click. Reveal up to 5 cards in HQ. Gain 2 credits for each card you revealed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20105", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "When Miranda Rhapsody showed up with a teacup giraffe, suddenly everybody wanted one.", "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "core2", "position": 89, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Reveal up to 5 cards in HQ. Gain 2 credits for each card you revealed this way.", "stripped_title": "Celebrity Gift", "text": "As an additional cost to play this operation, spend [click].\nReveal up to 5 cards in HQ. Gain 2[credit] for each card you revealed this way.", "title": "Celebrity Gift", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_neural_emp_20106(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner made a run during their last turn. Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20106", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "The trick isn't hitting the person you were aiming at. It's hitting <strong>only</strong> the person you were aiming at.", "illustrator": "Matt Zeilinger", "keywords": "Gray Ops", "pack_code": "core2", "position": 90, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner made a run during their last turn. Do 1 net damage.", "stripped_title": "Neural EMP", "text": "Play only if the Runner made a run during their last turn.\nDo 1 net damage.", "title": "Neural EMP", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_trick_of_light_20107(Operation):
    '''
    Cost: 1
    Text: Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20107", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Smoke and mirrors optional.", "illustrator": "Anna Ignatieva", "pack_code": "core2", "position": 91, "quantity": 2, "side_code": "corp", "stripped_text": "Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.", "stripped_title": "Trick of Light", "text": "Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.", "title": "Trick of Light", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_anonymous_tip_20118(Operation):
    '''
    Cost: 0
    Text: Draw 3 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20118", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"Please stay connected. Priority transfer in progress. An operator will shortly verif-\"", "illustrator": "Dmitry Prosvirnin, Atha Kanaani", "pack_code": "core2", "position": 102, "quantity": 1, "side_code": "corp", "stripped_text": "Draw 3 cards.", "stripped_title": "Anonymous Tip", "text": "Draw 3 cards.", "title": "Anonymous Tip", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_closed_accounts_20119(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner is tagged. The Runner loses all credits in their credit pool.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20119", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Mauricio Herrera", "keywords": "Gray Ops", "pack_code": "core2", "position": 103, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. The Runner loses all credits in their credit pool.", "stripped_title": "Closed Accounts", "text": "Play only if the Runner is tagged.\nThe Runner loses all credits in their credit pool.", "title": "Closed Accounts", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_psychographics_20120(Operation):
    '''
    Cost: None
    Text: X must be equal to or less than the number of tags the Runner has. Place X advancement counters on 1 installed card you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20120", "cost": null, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "Access to the largest consumer database in the galaxy has its advantages.", "illustrator": "Kate Laird", "pack_code": "core2", "position": 104, "quantity": 3, "side_code": "corp", "stripped_text": "X must be equal to or less than the number of tags the Runner has. Place X advancement counters on 1 installed card you can advance.", "stripped_title": "Psychographics", "text": "X must be equal to or less than the number of tags the Runner has.\nPlace X advancement counters on 1 installed card you can advance.", "title": "Psychographics", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sea_source_20121(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner made a successful run during their last turn. Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20121", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"The SEA tipped us off to some suspicious data spikes up by the Castle.\" -Jerome Lock, on-duty tech", "illustrator": "Dmitry Prosvirnin, Atha Kanaani", "pack_code": "core2", "position": 105, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "SEA Source", "text": "Play only if the Runner made a successful run during their last turn.\nTrace[3]. If successful, give the Runner 1 tag.", "title": "SEA Source", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hedge_fund_20132(Operation):
    '''
    Cost: 5
    Text: Gain 9 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20132", "cost": 5, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Hedge Fund. Noun. An ingenious device by which the rich get richer even while every other poor SOB is losing his shirt. -The Anarch's Dictionary, Volume Who's Counting?", "illustrator": "Mark Molnar", "keywords": "Transaction", "pack_code": "core2", "position": 132, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 9 credits.", "stripped_title": "Hedge Fund", "text": "Gain 9[credit].", "title": "Hedge Fund", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_genotyping_21014(Operation):
    '''
    Cost: 1
    Text: Trash the top 2 cards of R&D, then shuffle up to 4 cards from Archives into R&D. Remove Genotyping from the game instead of trashing it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21014", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Sometimes you have to break a few eggs to sequence a genome.", "illustrator": "Pavel Kolomeyets", "pack_code": "ss", "position": 14, "quantity": 3, "side_code": "corp", "stripped_text": "Trash the top 2 cards of R&D, then shuffle up to 4 cards from Archives into R&D. Remove Genotyping from the game instead of trashing it.", "stripped_title": "Genotyping", "text": "Trash the top 2 cards of R&D, then shuffle up to 4 cards from Archives into R&D. Remove Genotyping from the game instead of trashing it.", "title": "Genotyping", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_selfgrowth_program_21016(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner is tagged. Add 2 installed Runner cards to the grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21016", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "Our patented ClearMind\u2122 technology pacifies the trials and tribulations of everyday life.", "illustrator": "Limetown Studios", "keywords": "Gray Ops", "pack_code": "ss", "position": 16, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Add 2 installed Runner cards to the grip.", "stripped_title": "Self-Growth Program", "text": "Play only if the Runner is tagged.\nAdd 2 installed Runner cards to the grip.", "title": "Self-Growth Program", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_wake_up_call_21019(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner trashed a Corp card during their last turn. Choose 1 installed piece of hardware or non-virtual resource. The Runner must either trash that card or suffer 4 meat damage. Remove this operation from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21019", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "James Cory Webster", "keywords": "Reprisal - Gray Ops", "pack_code": "ss", "position": 19, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner trashed a Corp card during their last turn. Choose 1 installed piece of hardware or non-virtual resource. The Runner must either trash that card or suffer 4 meat damage. Remove this operation from the game.", "stripped_title": "Wake Up Call", "text": "Play only if the Runner trashed a Corp card during their last turn.\nChoose 1 installed piece of hardware or non-<strong>virtual</strong> resource. The Runner must either trash that card or suffer 4 meat damage.\nRemove this operation from the game.", "title": "Wake Up Call", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_threat_assessment_21035(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner trashed a Corp card during their last turn. Choose 1 installed Runner card. The Runner must take 2 tags or add that card to the top of the stack. Remove this operation from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21035", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Reprisal - Gray Ops", "pack_code": "dtwn", "position": 35, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner trashed a Corp card during their last turn. Choose 1 installed Runner card. The Runner must take 2 tags or add that card to the top of the stack. Remove this operation from the game.", "stripped_title": "Threat Assessment", "text": "Play only if the Runner trashed a Corp card during their last turn.\nChoose 1 installed Runner card. The Runner must take 2 tags or add that card to the top of the stack.\nRemove this operation from the game.", "title": "Threat Assessment", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_economic_warfare_21036(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner made a successful run during their last turn. If the Runner has at least 4 credits, they lose 4 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21036", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "He found it odd that three frozen yogurt shops, all less than a block from his, opened within the same week.", "illustrator": "Micha\u0142 Mi\u0142kowski", "keywords": "Gray Ops", "pack_code": "dtwn", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. If the Runner has at least 4 credits, they lose 4 credits.", "stripped_title": "Economic Warfare", "text": "Play only if the Runner made a successful run during their last turn.\nIf the Runner has at least 4[credit], they lose 4[credit].", "title": "Economic Warfare", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_distract_the_masses_21040(Operation):
    '''
    Cost: 0
    Text: The Runner gains 2 credits. Trash up to 2 cards from HQ, then shuffle up to 2 cards from Archives into R&D. Remove Distract the Masses from the game instead of trashing it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21040", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Food. Drinks. Entertainment. It doesn't take much to gratify the bourgeoisie.\"", "illustrator": "Emilio Rodriguez", "pack_code": "dtwn", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "The Runner gains 2 credits. Trash up to 2 cards from HQ, then shuffle up to 2 cards from Archives into R&D. Remove Distract the Masses from the game instead of trashing it.", "stripped_title": "Distract the Masses", "text": "The Runner gains 2[credit]. Trash up to 2 cards from HQ, then shuffle up to 2 cards from Archives into R&D. Remove Distract the Masses from the game instead of trashing it.", "title": "Distract the Masses", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_reverse_infection_21053(Operation):
    '''
    Cost: 0
    Text: Choose one: * Purge virus counters. Trash 1 card from the top of the stack for every 3 virus counters removed. * Gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21053", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "illustrator": "Adam S. Doyle", "pack_code": "cotc", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "Choose one: * Purge virus counters. Trash 1 card from the top of the stack for every 3 virus counters removed. * Gain 2 credits.", "stripped_title": "Reverse Infection", "text": "Choose one:<ul><li>Purge virus counters. Trash 1 card from the top of the stack for every 3 virus counters removed.</li><li>Gain 2[credit].</li></ul>", "title": "Reverse Infection", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_death_and_taxes_21058(Operation):
    '''
    Cost: 2
    Text: This card is not trashed until another current is played or an agenda is stolen. Whenever the Runner installs a card or trashes an installed card, you may gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21058", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "The only certainties.", "illustrator": "Kathryn Steele", "keywords": "Current - Transaction", "pack_code": "cotc", "position": 58, "quantity": 3, "side_code": "corp", "stripped_text": "This card is not trashed until another current is played or an agenda is stolen. Whenever the Runner installs a card or trashes an installed card, you may gain 1 credit.", "stripped_title": "Death and Taxes", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nWhenever the Runner installs a card or trashes an installed card, you may gain 1[credit].", "title": "Death and Taxes", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_trojan_horse_21059(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner accessed a card during their last turn. Trace[4]. If successful, trash 1 installed program with an install cost of X or less, where X is equal to the amount by which your trace strength exceeded the Runner's link strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21059", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Fei F. Ou", "keywords": "Gray Ops", "pack_code": "cotc", "position": 59, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner accessed a card during their last turn. Trace[4]. If successful, trash 1 installed program with an install cost of X or less, where X is equal to the amount by which your trace strength exceeded the Runner's link strength.", "stripped_title": "Trojan Horse", "text": "Play only if the Runner accessed a card during their last turn.\nTrace[4]. If successful, trash 1 installed program with an install cost of X or less, where X is equal to the amount by which your trace strength exceeded the Runner's link strength.", "title": "Trojan Horse", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_kill_switch_21070(Operation):
    '''
    Cost: 1
    Text: This operation is not trashed until another current is played or an agenda is stolen. While the Runner is accessing an agenda in R&D, they must reveal it. Whenever an agenda is accessed or scored, Trace[3]. If successful, do 1 core damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21070", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "flavor": "\"Don't worry, he won't feel a thing! Probably.\"", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Current", "pack_code": "tdatd", "position": 70, "quantity": 3, "side_code": "corp", "stripped_text": "This operation is not trashed until another current is played or an agenda is stolen. While the Runner is accessing an agenda in R&D, they must reveal it. Whenever an agenda is accessed or scored, Trace[3]. If successful, do 1 core damage.", "stripped_title": "Kill Switch", "text": "This operation is not trashed until another <strong>current</strong> is played or an agenda is stolen.\nWhile the Runner is accessing an agenda in R&D, they must reveal it.\nWhenever an agenda is accessed or scored, Trace[3]. If successful, do 1 core damage.", "title": "Kill Switch", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_standard_procedure_21097(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner made a successful run during their last turn. Choose a card type, then reveal the grip. Gain 2 credits for each card of the chosen type revealed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21097", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Nasrul Hakim", "pack_code": "win", "position": 97, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. Choose a card type, then reveal the grip. Gain 2 credits for each card of the chosen type revealed this way.", "stripped_title": "Standard Procedure", "text": "Play only if the Runner made a successful run during their last turn.\nChoose a card type, then reveal the grip. Gain 2[credit] for each card of the chosen type revealed this way.", "title": "Standard Procedure", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_riot_suppression_21113(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner trashed a Corp card during their last turn. The Runner may suffer 1 core damage. If they do not, they get -3 allotted click for their next turn. Remove this operation from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21113", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "illustrator": "Adam Schumpert", "keywords": "Reprisal - Gray Ops", "pack_code": "ka", "position": 113, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner trashed a Corp card during their last turn. The Runner may suffer 1 core damage. If they do not, they get -3 allotted click for their next turn. Remove this operation from the game.", "stripped_title": "Riot Suppression", "text": "Play only if the Runner trashed a Corp card during their last turn.\nThe Runner may suffer 1 core damage. If they do not, they get -3 allotted [click] for their next turn.\nRemove this operation from the game.", "title": "Riot Suppression", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_market_forces_21117(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner is tagged. The Runner loses 3 credits for each tag they have, then you gain 1 credit for each credit lost this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21117", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"Once we have enough data, we can make the Invisible Hand more like an Invisible Fist.\"", "illustrator": "Caravan Studio", "keywords": "Gray Ops", "pack_code": "ka", "position": 117, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. The Runner loses 3 credits for each tag they have, then you gain 1 credit for each credit lost this way.", "stripped_title": "Market Forces", "text": "Play only if the Runner is tagged.\nThe Runner loses 3[credit] for each tag they have, then you gain 1[credit] for each credit lost this way.", "title": "Market Forces", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_highprofile_target_21119(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner is tagged. Do 2 meat damage for each tag the Runner has.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21119", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 5, "flavor": "\"You can't do thi...\"", "illustrator": "Fei F. Ou", "keywords": "Black Ops", "pack_code": "ka", "position": 119, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Do 2 meat damage for each tag the Runner has.", "stripped_title": "High-Profile Target", "text": "Play only if the Runner is tagged.\nDo 2 meat damage for each tag the Runner has.", "title": "High-Profile Target", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_divert_power_22030(Operation):
    '''
    Cost: 2
    Text: Derez any number of cards. You may rez a card, lowering its rez cost by 3 for each card that you derezzed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22030", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "If that doesn't work, try reversing the polarity.", "illustrator": "Marius Siergiejew", "pack_code": "rar", "position": 30, "quantity": 3, "side_code": "corp", "stripped_text": "Derez any number of cards. You may rez a card, lowering its rez cost by 3 for each card that you derezzed this way.", "stripped_title": "Divert Power", "text": "Derez any number of cards. You may rez a card, lowering its rez cost by 3 for each card that you derezzed this way.", "title": "Divert Power", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_fast_break_22031(Operation):
    '''
    Cost: 4
    Text: Gain X credits. Draw up to X cards. Install up to X cards in the root of and/or protecting a single remote server. X is equal to the number of agendas in the Runner's score area.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22031", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"Oh, my! He's on fire!\"", "illustrator": "James Cory Webster", "pack_code": "rar", "position": 31, "quantity": 3, "side_code": "corp", "stripped_text": "Gain X credits. Draw up to X cards. Install up to X cards in the root of and/or protecting a single remote server. X is equal to the number of agendas in the Runner's score area.", "stripped_title": "Fast Break", "text": "Gain X[credit]. Draw up to X cards. Install up to X cards in the root of and/or protecting a single remote server. X is equal to the number of agendas in the Runner's score area.", "title": "Fast Break", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_game_changer_22032(Operation):
    '''
    Cost: 6
    Text: Gain click for each agenda in the Runner's score area. Remove Game Changer from the game instead of trashing it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22032", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "flavor": "Coach Walden's pep talks were renowned for improving in direct proportion to the amount by which his team was losing.", "illustrator": "Matt Zeilinger", "pack_code": "rar", "position": 32, "quantity": 3, "side_code": "corp", "stripped_text": "Gain click for each agenda in the Runner's score area. Remove Game Changer from the game instead of trashing it.", "stripped_title": "Game Changer", "text": "Gain [click] for each agenda in the Runner's score area. Remove Game Changer from the game instead of trashing it.", "title": "Game Changer", "trash_cost": 2, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hangeki_22040(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner trashed a Corp card during their last turn. Choose 1 of your installed cards. The Runner may access that card. If they do, remove this operation from the game; otherwise, add this operation to the Runner's score area as an agenda worth -1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22040", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Reprisal - Gray Ops", "pack_code": "rar", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner trashed a Corp card during their last turn. Choose 1 of your installed cards. The Runner may access that card. If they do, remove this operation from the game; otherwise, add this operation to the Runner's score area as an agenda worth -1 agenda point.", "stripped_title": "Hangeki", "text": "Play only if the Runner trashed a Corp card during their last turn.\nChoose 1 of your installed cards. The Runner may access that card. If they do, remove this operation from the game; otherwise, add this operation to the Runner's score area as an agenda worth -1 agenda point.", "title": "Hangeki", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_eavesdrop_22047(Operation):
    '''
    Cost: 1
    Text: Install Eavesdrop on a piece of ice as a hosted condition counter with the text "Whenever the Runner encounters host ice, Trace[3]. If successful, give the Runner 1 tag."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22047", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"No, the audio is fine. It just never seems to turn off.\"", "illustrator": "Steve Hamilton", "keywords": "Gray Ops - Condition", "pack_code": "rar", "position": 47, "quantity": 3, "side_code": "corp", "stripped_text": "Install Eavesdrop on a piece of ice as a hosted condition counter with the text \"Whenever the Runner encounters host ice, Trace[3]. If successful, give the Runner 1 tag.\"", "stripped_title": "Eavesdrop", "text": "Install Eavesdrop on a piece of ice as a hosted condition counter with the text \"Whenever the Runner encounters host ice, Trace[3]. If successful, give the Runner 1 tag.\"", "title": "Eavesdrop", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_attitude_adjustment_22048(Operation):
    '''
    Cost: 2
    Text: Draw 2 cards. Reveal up to 2 agendas in HQ and/or Archives. Gain 2 credits for each agenda revealed, then shuffle those agendas into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22048", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Good news, ma'am. The compliance training was completed with little resistance.\"", "illustrator": "Priscilla Kim", "pack_code": "rar", "position": 48, "quantity": 3, "side_code": "corp", "stripped_text": "Draw 2 cards. Reveal up to 2 agendas in HQ and/or Archives. Gain 2 credits for each agenda revealed, then shuffle those agendas into R&D.", "stripped_title": "Attitude Adjustment", "text": "Draw 2 cards. Reveal up to 2 agendas in HQ and/or Archives. Gain 2[credit] for each agenda revealed, then shuffle those agendas into R&D.", "title": "Attitude Adjustment", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_building_blocks_22055(Operation):
    '''
    Cost: 5
    Text: Reveal a barrier from HQ. Install and rez it, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22055", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "\"It looks like a mistake but I'm pretty sure they leave the gaps on purpose.\" -Gnat", "illustrator": "Ed Mattinian", "pack_code": "rar", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "Reveal a barrier from HQ. Install and rez it, ignoring all costs.", "stripped_title": "Building Blocks", "text": "Reveal a <strong>barrier</strong> from HQ. Install and rez it, ignoring all costs.", "title": "Building Blocks", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_too_big_to_fail_22056(Operation):
    '''
    Cost: 0
    Text: Play only if you have fewer than 10 credits. Gain 7 credits and take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22056", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "\"This is blackmail!\"\n\"No, this is <em>extortion.</em>\"", "illustrator": "Timur Shevtsov", "keywords": "Transaction - Illicit", "pack_code": "rar", "position": 56, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if you have fewer than 10 credits. Gain 7 credits and take 1 bad publicity.", "stripped_title": "Too Big to Fail", "text": "Play only if you have fewer than 10[credit].\nGain 7[credit] and take 1 bad publicity.", "title": "Too Big to Fail", "trash_cost": 5, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_under_the_bus_22057(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner accessed a card during their last turn. Trash 1 installed connection resource and take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22057", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Timur Shevtsov", "keywords": "Gray Ops - Illicit", "pack_code": "rar", "position": 57, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner accessed a card during their last turn. Trash 1 installed connection resource and take 1 bad publicity.", "stripped_title": "Under the Bus", "text": "Play only if the Runner accessed a card during their last turn.\nTrash 1 installed <strong>connection</strong> resource and take 1 bad publicity.", "title": "Under the Bus", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_archived_memories_25079(Operation):
    '''
    Cost: 0
    Text: Add 1 card from Archives to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25079", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Do you think they\u2026feel it?\"", "illustrator": "Gong Studios", "pack_code": "sc19", "position": 79, "quantity": 1, "side_code": "corp", "stripped_text": "Add 1 card from Archives to HQ.", "stripped_title": "Archived Memories", "text": "Add 1 card from Archives to HQ.", "title": "Archived Memories", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_biotic_labor_25080(Operation):
    '''
    Cost: 4
    Text: Gain click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25080", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "\"Why of course, we have six different Haas-Bioroid models serving in a variety of positions at this branch office alone. We here at Haas-Bioroid aren't going to shy away from practicing what we preach, and we pass the savings from increased efficiency on to our valued customers.\"", "illustrator": "Mark Anthony Taduran", "pack_code": "sc19", "position": 80, "quantity": 2, "side_code": "corp", "stripped_text": "Gain click click.", "stripped_title": "Biotic Labor", "text": "Gain [click][click].", "title": "Biotic Labor", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_blue_level_clearance_25081(Operation):
    '''
    Cost: 2
    Text: As an additional cost to play this operation, spend click. Gain 5 credits and draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25081", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Blue-one level clearance doesn't exist. And if it did exist, you wouldn't be cleared to know about it.", "illustrator": "Tim Durning", "keywords": "Double - Transaction", "pack_code": "sc19", "position": 81, "quantity": 2, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Gain 5 credits and draw 2 cards.", "stripped_title": "Blue Level Clearance", "text": "As an additional cost to play this operation, spend [click].\nGain 5[credit] and draw 2 cards.", "title": "Blue Level Clearance", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_celebrity_gift_25100(Operation):
    '''
    Cost: 3
    Text: As an additional cost to play this operation, spend click. Reveal up to 5 cards in HQ. Gain 2 credits for each card you revealed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25100", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "When Miranda Rhapsody showed up with a teacup giraffe, suddenly everybody wanted one.", "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "sc19", "position": 100, "quantity": 2, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Reveal up to 5 cards in HQ. Gain 2 credits for each card you revealed this way.", "stripped_title": "Celebrity Gift", "text": "As an additional cost to play this operation, spend [click].\nReveal up to 5 cards in HQ. Gain 2[credit] for each card you revealed this way.", "title": "Celebrity Gift", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_neural_emp_25101(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner made a run during their last turn. Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25101", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "The trick isn't hitting the person you were aiming at. It's hitting <strong>only</strong> the person you were aiming at.", "illustrator": "Matt Zeilinger", "keywords": "Gray Ops", "pack_code": "sc19", "position": 101, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner made a run during their last turn. Do 1 net damage.", "stripped_title": "Neural EMP", "text": "Play only if the Runner made a run during their last turn.\nDo 1 net damage.", "title": "Neural EMP", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_trick_of_light_25102(Operation):
    '''
    Cost: 1
    Text: Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25102", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Smoke and mirrors optional.", "illustrator": "Anna Ignatieva", "pack_code": "sc19", "position": 102, "quantity": 1, "side_code": "corp", "stripped_text": "Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.", "stripped_title": "Trick of Light", "text": "Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.", "title": "Trick of Light", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_closed_accounts_25117(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner is tagged. The Runner loses all credits in their credit pool.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25117", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Mauricio Herrera", "keywords": "Gray Ops", "pack_code": "sc19", "position": 117, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. The Runner loses all credits in their credit pool.", "stripped_title": "Closed Accounts", "text": "Play only if the Runner is tagged.\nThe Runner loses all credits in their credit pool.", "title": "Closed Accounts", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_psychographics_25118(Operation):
    '''
    Cost: None
    Text: X must be equal to or less than the number of tags the Runner has. Place X advancement counters on 1 installed card you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25118", "cost": null, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "Access to the largest consumer database in the galaxy has its advantages.", "illustrator": "Kate Laird", "pack_code": "sc19", "position": 118, "quantity": 1, "side_code": "corp", "stripped_text": "X must be equal to or less than the number of tags the Runner has. Place X advancement counters on 1 installed card you can advance.", "stripped_title": "Psychographics", "text": "X must be equal to or less than the number of tags the Runner has.\nPlace X advancement counters on 1 installed card you can advance.", "title": "Psychographics", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sea_source_25119(Operation):
    '''
    Cost: 2
    Text: Play only if the Runner made a successful run during their last turn. Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25119", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"The SEA tipped us off to some suspicious data spikes up by the Castle.\" -Jerome Lock, on-duty tech", "illustrator": "Dmitry Prosvirnin, Atha Kanaani", "pack_code": "sc19", "position": 119, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "SEA Source", "text": "Play only if the Runner made a successful run during their last turn.\nTrace[3]. If successful, give the Runner 1 tag.", "title": "SEA Source", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_beanstalk_royalties_25136(Operation):
    '''
    Cost: 0
    Text: Gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25136", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "The New Angeles Space Elevator, better known as the Beanstalk, is the single greatest triumph of human engineering and ingenuity in history. The Beanstalk makes Earth orbit accessible to everyone\u2026for a small fee.", "illustrator": "Jonathan Lee", "keywords": "Transaction", "pack_code": "sc19", "position": 136, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 3 credits.", "stripped_title": "Beanstalk Royalties", "text": "Gain 3[credit].", "title": "Beanstalk Royalties", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_oversight_ai_25137(Operation):
    '''
    Cost: 1
    Text: Rez a piece of ice, ignoring all costs, and install Oversight AI on that ice as a hosted condition counter with the text "Trash host ice if all its subroutines are broken during a single encounter."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25137", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Mark Anthony Taduran", "keywords": "Condition", "pack_code": "sc19", "position": 137, "quantity": 2, "side_code": "corp", "stripped_text": "Rez a piece of ice, ignoring all costs, and install Oversight AI on that ice as a hosted condition counter with the text \"Trash host ice if all its subroutines are broken during a single encounter.\"", "stripped_title": "Oversight AI", "text": "Rez a piece of ice, ignoring all costs, and install Oversight AI on that ice as a hosted condition counter with the text \"Trash host ice if all its subroutines are broken during a single encounter.\"", "title": "Oversight AI", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_punitive_counterstrike_25138(Operation):
    '''
    Cost: 3
    Text: Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25138", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"I'd say it's nothing personal, but corporations are people, too.\"", "illustrator": "Lorraine Schleter", "keywords": "Black Ops", "pack_code": "sc19", "position": 138, "quantity": 2, "side_code": "corp", "stripped_text": "Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.", "stripped_title": "Punitive Counterstrike", "text": "Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.", "title": "Punitive Counterstrike", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hedge_fund_25146(Operation):
    '''
    Cost: 5
    Text: Gain 9 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25146", "cost": 5, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Hedge Fund. Noun. An ingenious device by which the rich get richer even while every other poor SOB is losing his shirt. -The Anarch's Dictionary, Volume Who's Counting?", "illustrator": "Mark Molnar", "keywords": "Transaction", "pack_code": "sc19", "position": 146, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 9 credits.", "stripped_title": "Hedge Fund", "text": "Gain 9[credit].", "title": "Hedge Fund", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_ipo_25147(Operation):
    '''
    Cost: 8
    Text: After you resolve this operation, end your action phase. Gain 13 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25147", "cost": 8, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Mark Molnar", "keywords": "Terminal - Transaction", "pack_code": "sc19", "position": 147, "quantity": 2, "side_code": "corp", "stripped_text": "After you resolve this operation, end your action phase. Gain 13 credits.", "stripped_title": "IPO", "text": "After you resolve this operation, end your action phase.\nGain 13[credit].", "title": "IPO", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_fully_operational_26036(Operation):
    '''
    Cost: 1
    Text: Gain 2 credits or draw 2 cards. Repeat this process for each remote server that has a card in its root and is protected by ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26036", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "Haas' unsecured servers were fortified just before the storm. Are their bioroid oracles that good, or were they tipped off?", "illustrator": "Krembler", "pack_code": "df", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 2 credits or draw 2 cards. Repeat this process for each remote server that has a card in its root and is protected by ice.", "stripped_title": "Fully Operational", "text": "Gain 2[credit] or draw 2 cards. Repeat this process for each remote server that has a card in its root and is protected by ice.", "title": "Fully Operational", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_red_level_clearance_26037(Operation):
    '''
    Cost: 1
    Text: Resolve two of the following in any order: * Draw 2 cards. * Gain 2 credits. * Install up to 1 non-agenda card. * Gain click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26037", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Not all secrets lie in vaults.", "illustrator": "Krembler", "keywords": "Transaction", "pack_code": "df", "position": 37, "quantity": 3, "side_code": "corp", "stripped_text": "Resolve two of the following in any order: * Draw 2 cards. * Gain 2 credits. * Install up to 1 non-agenda card. * Gain click.", "stripped_title": "Red Level Clearance", "text": "Resolve two of the following in any order:<ul><li>Draw 2 cards.</li><li>Gain 2[credit].</li><li>Install up to 1 non-agenda card.</li><li>Gain [click].</li></ul>", "title": "Red Level Clearance", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_complete_image_26045(Operation):
    '''
    Cost: 4
    Text: After you resolve this operation, your action phase ends. Play only if the Runner has 3 or more agenda points and they made a successful run during their last turn. Name a card, then do 1 net damage. If you trash a copy of the named card, repeat this process.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26045", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "illustrator": "Krembler", "keywords": "Terminal - Gray Ops", "pack_code": "df", "position": 45, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, your action phase ends. Play only if the Runner has 3 or more agenda points and they made a successful run during their last turn. Name a card, then do 1 net damage. If you trash a copy of the named card, repeat this process.", "stripped_title": "Complete Image", "text": "After you resolve this operation, your action phase ends.\nPlay only if the Runner has 3 or more agenda points and they made a successful run during their last turn.\nName a card, then do 1 net damage. If you trash a copy of the named card, repeat this process.", "title": "Complete Image", "trash_cost": 2, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_focus_group_26052(Operation):
    '''
    Cost: 3
    Text: Play only if the Runner made a successful run during their last turn. Choose a card type, then reveal the grip. You may pay X credits to place X advancement tokens on an installed card. X is equal to or less than the number of revealed cards of the chosen type.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26052", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"There's gonna be catering, right?\"", "illustrator": "Dimik", "pack_code": "df", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. Choose a card type, then reveal the grip. You may pay X credits to place X advancement tokens on an installed card. X is equal to or less than the number of revealed cards of the chosen type.", "stripped_title": "Focus Group", "text": "Play only if the Runner made a successful run during their last turn.\nChoose a card type, then reveal the grip. You may pay X[credit] to place X advancement tokens on an installed card. X is equal to or less than the number of revealed cards of the chosen type.", "title": "Focus Group", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_game_over_26053(Operation):
    '''
    Cost: 4
    Text: Play only if the Runner stole an agenda during their last turn. Choose a Runner card type. Trash all installed non-icebreaker cards of that type. The Runner may prevent any of those cards from being trashed by paying 3 credits each. Take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26053", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "It is pitch black. You are likely to be eaten by a Troll.", "illustrator": "Krembler", "keywords": "Illicit - Gray Ops", "pack_code": "df", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner stole an agenda during their last turn. Choose a Runner card type. Trash all installed non-icebreaker cards of that type. The Runner may prevent any of those cards from being trashed by paying 3 credits each. Take 1 bad publicity.", "stripped_title": "Game Over", "text": "Play only if the Runner stole an agenda during their last turn.\nChoose a Runner card type. Trash all installed non-<strong>icebreaker</strong> cards of that type. The Runner may prevent any of those cards from being trashed by paying 3[credit] each. Take 1 bad publicity.", "title": "Game Over", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_secure_and_protect_26061(Operation):
    '''
    Cost: 1
    Text: As an additional cost to play this operation, spend click. Search R&D for a piece of ice and reveal it. (Shuffle R&D after searching it.) Install that ice protecting a central server, paying 3 credits less.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26061", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "Secure Servers. Contain Infections. Protect Data.\n-The SecTech Mantra", "illustrator": "Krembler", "keywords": "Double", "pack_code": "df", "position": 61, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Search R&D for a piece of ice and reveal it. (Shuffle R&D after searching it.) Install that ice protecting a central server, paying 3 credits less.", "stripped_title": "Secure and Protect", "text": "As an additional cost to play this operation, spend [click].\nSearch R&D for a piece of ice and reveal it. <em>(Shuffle R&D after searching it.)</em> Install that ice protecting a central server, paying 3[credit] less.", "title": "Secure and Protect", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_next_activation_command_26103(Operation):
    '''
    Cost: 0
    Text: Play only if there is no active lockdown. This operation is not trashed until your next turn begins. The Runner cannot use non-icebreaker cards to break subroutines. Each piece of ice has +2 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26103", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"Uh oh, Keiko! Looks like we've pulled aggro!\"", "illustrator": "NtscapeNavigator", "keywords": "Lockdown", "pack_code": "ur", "position": 103, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if there is no active lockdown. This operation is not trashed until your next turn begins. The Runner cannot use non-icebreaker cards to break subroutines. Each piece of ice has +2 strength.", "stripped_title": "NEXT Activation Command", "text": "Play only if there is no active <strong>lockdown</strong>. This operation is not trashed until your next turn begins.\nThe Runner cannot use non-<strong>icebreaker</strong> cards to break subroutines. Each piece of ice has +2 strength.", "title": "NEXT Activation Command", "trash_cost": 4, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_scapenet_26104(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner made a successful run during their last turn. Trace[7]. If successful, remove 1 installed chip or virtual card from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26104", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "The Net is the consensual hallucination of the world's electronic architecture. <em>Our</em> electronic architecture. Don't get mad when the Runners succeed\u2014change the rules.", "illustrator": "Zoe Cohen", "keywords": "Gray Ops", "pack_code": "ur", "position": 104, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. Trace[7]. If successful, remove 1 installed chip or virtual card from the game.", "stripped_title": "Scapenet", "text": "Play only if the Runner made a successful run during their last turn.\nTrace[7]. If successful, remove 1 installed <strong>chip</strong> or <strong>virtual</strong> card from the game.", "title": "Scapenet", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hyoubu_precog_manifold_26110(Operation):
    '''
    Cost: 0
    Text: Play only if there is no active lockdown. This operation is not trashed until your next turn begins. Choose a server. Whenever the Runner makes a successful run on the chosen server, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, end the run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26110", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Iain Fairclough", "keywords": "Lockdown - Psi", "pack_code": "ur", "position": 110, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if there is no active lockdown. This operation is not trashed until your next turn begins. Choose a server. Whenever the Runner makes a successful run on the chosen server, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, end the run.", "stripped_title": "Hyoubu Precog Manifold", "text": "Play only if there is no active <strong>lockdown</strong>. This operation is not trashed until your next turn begins.\nChoose a server.\nWhenever the Runner makes a successful run on the chosen server, you and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, end the run.", "title": "Hyoubu Precog Manifold", "trash_cost": 4, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_kakurenbo_26111(Operation):
    '''
    Cost: 2
    Text: As an additional cost to play this operation, spend click click. Trash any number of cards from HQ. Turn all cards in Archives facedown. You may install 1 agenda, asset, or upgrade from Archives in the root of a remote server and place 2 advancement counters on it. Remove this operation from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26111", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Patrick Burk", "keywords": "Triple", "pack_code": "ur", "position": 111, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click click. Trash any number of cards from HQ. Turn all cards in Archives facedown. You may install 1 agenda, asset, or upgrade from Archives in the root of a remote server and place 2 advancement counters on it. Remove this operation from the game.", "stripped_title": "Kakurenbo", "text": "As an additional cost to play this operation, spend [click][click].\nTrash any number of cards from HQ. Turn all cards in Archives facedown. You may install 1 agenda, asset, or upgrade from Archives in the root of a remote server and place 2 advancement counters on it.\nRemove this operation from the game.", "title": "Kakurenbo", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_digital_rights_management_26117(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner did not make a successful run on HQ during their last turn. Search R&D for an agenda and reveal it. (Shuffle R&D after searching it.) Add that agenda to HQ. You may install 1 card from HQ in the root of a remote server. You cannot score agendas for the remainder of the turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26117", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Krembler", "pack_code": "ur", "position": 117, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner did not make a successful run on HQ during their last turn. Search R&D for an agenda and reveal it. (Shuffle R&D after searching it.) Add that agenda to HQ. You may install 1 card from HQ in the root of a remote server. You cannot score agendas for the remainder of the turn.", "stripped_title": "Digital Rights Management", "text": "Play only if the Runner did not make a successful run on HQ during their last turn.\nSearch R&D for an agenda and reveal it. <em>(Shuffle R&D after searching it.)</em> Add that agenda to HQ. You may install 1 card from HQ in the root of a remote server.\nYou cannot score agendas for the remainder of the turn.", "title": "Digital Rights Management", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sync_rerouting_26118(Operation):
    '''
    Cost: 0
    Text: Play only if there is no active lockdown. This operation is not trashed until your next turn begins. Whenever a run begins, the Runner must pay 4 credits or take 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26118", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"Deep inspect every packet on the continent. Burn out all our stacks if you have to. We cannot let these terrorists cover their tracks.\" -CEO Jenkins", "illustrator": "N. Hopkins", "keywords": "Lockdown", "pack_code": "ur", "position": 118, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if there is no active lockdown. This operation is not trashed until your next turn begins. Whenever a run begins, the Runner must pay 4 credits or take 1 tag.", "stripped_title": "SYNC Rerouting", "text": "Play only if there is no active <strong>lockdown</strong>. This operation is not trashed until your next turn begins.\nWhenever a run begins, the Runner must pay 4[credit] or take 1 tag.", "title": "SYNC Rerouting", "trash_cost": 3, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_argus_crackdown_26126(Operation):
    '''
    Cost: 0
    Text: Play only if there is no active lockdown. This operation is not trashed until your next turn begins. Whenever the Runner makes a successful run on a server protected by ice, do 2 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26126", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "\"If it moves, shoot it. Then shoot it again.\"\n-Chief Slee", "illustrator": "Krembler", "keywords": "Lockdown - Gray Ops", "pack_code": "ur", "position": 126, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if there is no active lockdown. This operation is not trashed until your next turn begins. Whenever the Runner makes a successful run on a server protected by ice, do 2 meat damage.", "stripped_title": "Argus Crackdown", "text": "Play only if there is no active <strong>lockdown</strong>. This operation is not trashed until your next turn begins.\nWhenever the Runner makes a successful run on a server protected by ice, do 2 meat damage.", "title": "Argus Crackdown", "trash_cost": 4, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_napd_cordon_26130(Operation):
    '''
    Cost: 0
    Text: Play only if there is no active lockdown. This operation is not trashed until your next turn begins. As an additional cost to steal an agenda, the Runner must pay 4 credits, plus 2 credits for each advancement token on that agenda.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26130", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Crisis is the true test of loyalty. Kick the anthill and see where the ants swarm.", "illustrator": "Olie Boldador", "keywords": "Lockdown", "pack_code": "ur", "position": 130, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if there is no active lockdown. This operation is not trashed until your next turn begins. As an additional cost to steal an agenda, the Runner must pay 4 credits, plus 2 credits for each advancement token on that agenda.", "stripped_title": "NAPD Cordon", "text": "Play only if there is no active <strong>lockdown</strong>. This operation is not trashed until your next turn begins.\nAs an additional cost to steal an agenda, the Runner must pay 4[credit], plus 2[credit] for each advancement token on that agenda.", "title": "NAPD Cordon", "trash_cost": 2, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_digital_rights_management_27006(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner did not make a successful run on HQ during their last turn. Search R&D for an agenda and reveal it. (Shuffle R&D after searching it.) Add that agenda to HQ. You may install 1 card from HQ in the root of a remote server. You cannot score agendas for the remainder of the turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "27006", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Krembler", "pack_code": "urbp", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner did not make a successful run on HQ during their last turn. Search R&D for an agenda and reveal it. (Shuffle R&D after searching it.) Add that agenda to HQ. You may install 1 card from HQ in the root of a remote server. You cannot score agendas for the remainder of the turn.", "stripped_title": "Digital Rights Management", "text": "Play only if the Runner did not make a successful run on HQ during their last turn.\nSearch R&D for an agenda and reveal it. <em>(Shuffle R&D after searching it.)</em> Add that agenda to HQ. You may install 1 card from HQ in the root of a remote server.\nYou cannot score agendas for the remainder of the turn.", "title": "Digital Rights Management", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sweeps_week_29013(Operation):
    '''
    Cost: 1
    Text: Gain 1 credit for each card in the Runner's grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29013", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Let me get this straight. Your target market is 15-19 year old g-modded immigrants with one parent, a discretionary income over 2k a month, B+ or higher grades, an outgoing personality, and have a friend who owns a g-monkey?\"\n\"Yes. Is that a problem?\"\n\"No, not at all. I just don't get why your list is so short.\"", "illustrator": "Mike Nesbitt", "pack_code": "sm", "position": 13, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit for each card in the Runner's grip.", "stripped_title": "Sweeps Week", "text": "Gain 1[credit] for each card in the Runner's grip.", "title": "Sweeps Week", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_scorched_earth_29016(Operation):
    '''
    Cost: 3
    Text: Play only if the Runner is tagged. Do 4 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29016", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "\"I'd like to remind the ladies and gentlemen of the press that several of the buildings damaged in the blast were owned by Weyland Consortium subsidiaries\u2026\"", "illustrator": "Mark Anthony Taduran", "keywords": "Black Ops", "pack_code": "sm", "position": 16, "quantity": 2, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Do 4 meat damage.", "stripped_title": "Scorched Earth", "text": "Play only if the Runner is tagged.\nDo 4 meat damage.", "title": "Scorched Earth", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_subliminal_messaging_29018(Operation):
    '''
    Cost: 0
    Text: Gain 1 credit. The first time each turn you play a copy of Subliminal Messaging, gain click. When your turn begins, if this card is in Archives and the Runner did not initiate any runs during their last turn, you may reveal this card and add it to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29018", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Mike Nesbitt", "keywords": "Gray Ops", "pack_code": "sm", "position": 18, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit. The first time each turn you play a copy of Subliminal Messaging, gain click. When your turn begins, if this card is in Archives and the Runner did not initiate any runs during their last turn, you may reveal this card and add it to HQ.", "stripped_title": "Subliminal Messaging", "text": "Gain 1[credit].\nThe first time each turn you play a copy of Subliminal Messaging, gain [click].\nWhen your turn begins, if this card is in Archives and the Runner did not initiate any runs during their last turn, you may reveal this card and add it to HQ.", "title": "Subliminal Messaging", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_seamless_launch_30040(Operation):
    '''
    Cost: 1
    Text: Place 2 advancement counters on 1 installed card that you did not install this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30040", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "The first lesson for handling bioroids is simple: they must not be allowed to feel.", "illustrator": "David Lei", "pack_code": "sg", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "Place 2 advancement counters on 1 installed card that you did not install this turn.", "stripped_title": "Seamless Launch", "text": "Place 2 advancement counters on 1 installed card that you did not install this turn.", "title": "Seamless Launch", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_sprint_30041(Operation):
    '''
    Cost: 0
    Text: Draw 3 cards. Shuffle 2 cards from HQ into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30041", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "All time is crunch time.", "illustrator": "Galen Dara", "pack_code": "sg", "position": 41, "quantity": 3, "side_code": "corp", "stripped_text": "Draw 3 cards. Shuffle 2 cards from HQ into R&D.", "stripped_title": "Sprint", "text": "Draw 3 cards. Shuffle 2 cards from HQ into R&D.", "title": "Sprint", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hansei_review_30048(Operation):
    '''
    Cost: 5
    Text: Gain 10 credits. If there are any cards in HQ, trash 1 of them.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30048", "cost": 5, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "\"Constant self-reflection is the key to excellence. We remember failed ideas, but do not carry them forward.\"\n\u2014Director Kase, unknown leadership seminar", "illustrator": "David Lei", "keywords": "Transaction", "pack_code": "sg", "position": 48, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 10 credits. If there are any cards in HQ, trash 1 of them.", "stripped_title": "Hansei Review", "text": "Gain 10[credit]. If there are any cards in HQ, trash 1 of them.", "title": "Hansei Review", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_neurospike_30049(Operation):
    '''
    Cost: 3
    Text: Do X net damage, where X is equal to the sum of the printed agenda points on agendas you scored this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30049", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Macroscale developments within the Net decouple the prior informational states\u2014surplus entropy is then gifted where it will do the most good.", "illustrator": "BalanceSheet", "keywords": "Gray Ops", "pack_code": "sg", "position": 49, "quantity": 3, "side_code": "corp", "stripped_text": "Do X net damage, where X is equal to the sum of the printed agenda points on agendas you scored this turn.", "stripped_title": "Neurospike", "text": "Do X net damage, where X is equal to the sum of the printed agenda points on agendas you scored this turn.", "title": "Neurospike", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_predictive_planogram_30056(Operation):
    '''
    Cost: 0
    Text: Resolve 1 of the following. If the Runner is tagged, you may resolve both instead. * Gain 3 credits. * Draw 3 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30056", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "For the best augmented reality shopping experience, please disable tracking protection.", "illustrator": "Bruno Balixa", "keywords": "Transaction", "pack_code": "sg", "position": 56, "quantity": 3, "side_code": "corp", "stripped_text": "Resolve 1 of the following. If the Runner is tagged, you may resolve both instead. * Gain 3 credits. * Draw 3 cards.", "stripped_title": "Predictive Planogram", "text": "Resolve 1 of the following. If the Runner is tagged, you may resolve both instead.<ul><li>Gain 3[credit].</li><li>Draw 3 cards.</li></ul>", "title": "Predictive Planogram", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_public_trail_30057(Operation):
    '''
    Cost: 4
    Text: Play only if the Runner made a successful run during their last turn. Give the Runner 1 tag unless they pay 8 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30057", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"A runner uses significant resources scrubbing their traces. Every cycle, it's harder to pin them down. But the game changes. In Heinlein, no one can last a day without brushing <strong>our</strong> AR-network.\"\n\u2014Cassie LaRosa, Lunar NetDefense Sysop", "illustrator": "Bruno Balixa", "keywords": "Gray Ops", "pack_code": "sg", "position": 57, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner made a successful run during their last turn. Give the Runner 1 tag unless they pay 8 credits.", "stripped_title": "Public Trail", "text": "Play only if the Runner made a successful run during their last turn.\nGive the Runner 1 tag unless they pay 8[credit].", "title": "Public Trail", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_government_subsidy_30064(Operation):
    '''
    Cost: 10
    Text: Gain 15 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30064", "cost": 10, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"If the government spent 1% of the funding they provide us tracking where the other 99% went, my colleagues and I would be in prison\u2026\n\u2026but that is a very big <strong>if</strong>.\"\n\u2014Huey DeMora, W-Con public-private facilitation seminar", "illustrator": "David Lei", "keywords": "Transaction", "pack_code": "sg", "position": 64, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 15 credits.", "stripped_title": "Government Subsidy", "text": "Gain 15[credit].", "title": "Government Subsidy", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_retribution_30065(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner is tagged. Trash 1 installed program or piece of hardware.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30065", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Did you really think you'd get away with it?", "illustrator": "David Lei", "keywords": "Gray Ops", "pack_code": "sg", "position": 65, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Trash 1 installed program or piece of hardware.", "stripped_title": "Retribution", "text": "Play only if the Runner is tagged.\nTrash 1 installed program or piece of hardware.", "title": "Retribution", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hedge_fund_30075(Operation):
    '''
    Cost: 5
    Text: Gain 9 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30075", "cost": 5, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "A financial instrument for diverting money from those outside to those inside.", "illustrator": "Kira L. Nguyen", "keywords": "Transaction", "pack_code": "sg", "position": 75, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 9 credits.", "stripped_title": "Hedge Fund", "text": "Gain 9[credit].", "title": "Hedge Fund", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_archived_memories_31047(Operation):
    '''
    Cost: 0
    Text: Add 1 card from Archives to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31047", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "It's not sleep. Sleep is dreams, activity, change. These are still, cold, dead.", "illustrator": "N. Hopkins", "pack_code": "su21", "position": 47, "quantity": 3, "side_code": "corp", "stripped_text": "Add 1 card from Archives to HQ.", "stripped_title": "Archived Memories", "text": "Add 1 card from Archives to HQ.", "title": "Archived Memories", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_biotic_labor_31048(Operation):
    '''
    Cost: 4
    Text: Gain click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31048", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "Sometimes we at Haas-Bioroid are asked how well bioroids interface socially with human workforces. Thanks to our tireless efforts, we believe this will not be a problem in the long term.", "illustrator": "Olie Boldador", "pack_code": "su21", "position": 48, "quantity": 3, "side_code": "corp", "stripped_text": "Gain click click.", "stripped_title": "Biotic Labor", "text": "Gain [click][click].", "title": "Biotic Labor", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_celebrity_gift_31057(Operation):
    '''
    Cost: 3
    Text: As an additional cost to play this operation, spend click. Reveal up to 5 cards in HQ. Gain 2 credits for each card you revealed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31057", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "We knew we'd found this season's must-have when all twenty of the A-tier influencers refused to return the teacup alpacas.", "illustrator": "N. Hopkins", "keywords": "Double", "pack_code": "su21", "position": 57, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Reveal up to 5 cards in HQ. Gain 2 credits for each card you revealed this way.", "stripped_title": "Celebrity Gift", "text": "As an additional cost to play this operation, spend [click].\nReveal up to 5 cards in HQ. Gain 2[credit] for each card you revealed this way.", "title": "Celebrity Gift", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_trick_of_light_31058(Operation):
    '''
    Cost: 1
    Text: Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31058", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Are you watching closely?", "illustrator": "N. Hopkins", "pack_code": "su21", "position": 58, "quantity": 3, "side_code": "corp", "stripped_text": "Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.", "stripped_title": "Trick of Light", "text": "Choose 1 installed card you can advance. Move up to 2 advancement counters from 1 other card to the chosen card.", "title": "Trick of Light", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_psychographics_31068(Operation):
    '''
    Cost: None
    Text: X must be equal to or less than the number of tags the Runner has. Place X advancement counters on 1 installed card you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31068", "cost": null, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "They know more about you than you do.", "illustrator": "Nedliv Audiovisuell", "pack_code": "su21", "position": 68, "quantity": 3, "side_code": "corp", "stripped_text": "X must be equal to or less than the number of tags the Runner has. Place X advancement counters on 1 installed card you can advance.", "stripped_title": "Psychographics", "text": "X must be equal to or less than the number of tags the Runner has.\nPlace X advancement counters on 1 installed card you can advance.", "title": "Psychographics", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_punitive_counterstrike_31078(Operation):
    '''
    Cost: 3
    Text: Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31078", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"Don't think we don't care. We are <strong>very</strong> upset.\"", "illustrator": "Zoe Cohen", "keywords": "Black Ops", "pack_code": "su21", "position": 78, "quantity": 3, "side_code": "corp", "stripped_text": "Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.", "stripped_title": "Punitive Counterstrike", "text": "Trace[5]. If successful, do X meat damage. X is equal to the sum of the printed agenda points on all agendas the Runner stole during their last turn.", "title": "Punitive Counterstrike", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_subliminal_messaging_31082(Operation):
    '''
    Cost: 0
    Text: Gain 1 credit. The first time each turn you play a copy of Subliminal Messaging, gain click. When your turn begins, if this card is in Archives and the Runner did not initiate any runs during their last turn, you may reveal this card and add it to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31082", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "You don't notice, but their profits do.", "illustrator": "Seojun Park", "keywords": "Gray Ops", "pack_code": "su21", "position": 82, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit. The first time each turn you play a copy of Subliminal Messaging, gain click. When your turn begins, if this card is in Archives and the Runner did not initiate any runs during their last turn, you may reveal this card and add it to HQ.", "stripped_title": "Subliminal Messaging", "text": "Gain 1[credit].\nThe first time each turn you play a copy of Subliminal Messaging, gain [click].\nWhen your turn begins, if this card is in Archives and the Runner did not initiate any runs during their last turn, you may reveal this card and add it to HQ.", "title": "Subliminal Messaging", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_big_deal_33038(Operation):
    '''
    Cost: 17
    Text: After you resolve this operation, your action phase ends. Place 4 advancement counters on 1 installed card. You may score that card, if able. Remove this operation from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33038", "cost": 17, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "flavor": "<strong>Designed by 2018 North American Champion Sam Suied</strong>", "illustrator": "Dimik", "keywords": "Terminal", "pack_code": "ms", "position": 38, "quantity": 3, "side_code": "corp", "stripped_text": "After you resolve this operation, your action phase ends. Place 4 advancement counters on 1 installed card. You may score that card, if able. Remove this operation from the game.", "stripped_title": "Big Deal", "text": "After you resolve this operation, your action phase ends.\nPlace 4 advancement counters on 1 installed card. You may score that card, if able.\nRemove this operation from the game.", "title": "Big Deal", "trash_cost": 3, "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_mitosis_33046(Operation):
    '''
    Cost: 3
    Text: As an additional cost to play this operation, spend click. Install up to 2 cards from HQ, creating a new remote server each time. Place 2 advancement counters on each of those cards. You cannot score or rez either of those cards this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33046", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "One becomes many.", "illustrator": "Emilio Rodriguez", "keywords": "Double", "pack_code": "ms", "position": 46, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Install up to 2 cards from HQ, creating a new remote server each time. Place 2 advancement counters on each of those cards. You cannot score or rez either of those cards this turn.", "stripped_title": "Mitosis", "text": "As an additional cost to play this operation, spend [click].\nInstall up to 2 cards from HQ, creating a new remote server each time. Place 2 advancement counters on each of those cards. You cannot score or rez either of those cards this turn.", "title": "Mitosis", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_backroom_machinations_33055(Operation):
    '''
    Cost: 2
    Text: As an additional cost to play this operation, remove 1 tag. Add this operation to your score area as an agenda worth 1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33055", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Recording devices at the door, please!\"", "illustrator": "Olie Boldador", "keywords": "Gray Ops", "pack_code": "ms", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, remove 1 tag. Add this operation to your score area as an agenda worth 1 agenda point.", "stripped_title": "Backroom Machinations", "text": "As an additional cost to play this operation, remove 1 tag.\nAdd this operation to your score area as an agenda worth 1 agenda point.", "title": "Backroom Machinations", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_extract_33063(Operation):
    '''
    Cost: 3
    Text: Gain 6 credits. You may trash 1 of your installed cards to gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33063", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Leave nothing of value behind.", "illustrator": "Vitalii Ostaschenko", "keywords": "Transaction", "pack_code": "ms", "position": 63, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 6 credits. You may trash 1 of your installed cards to gain 3 credits.", "stripped_title": "Extract", "text": "Gain 6[credit]. You may trash 1 of your installed cards to gain 3[credit].", "title": "Extract", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_mutually_assured_destruction_33064(Operation):
    '''
    Cost: 4
    Text: As an additional cost to play this operation, spend clickclick. Trash any number of your rezzed cards. Give the Runner 1 tag for each card trashed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33064", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "<strong>Designed by 2020 Asia-Pacific Champion Eric Keilback</strong>", "illustrator": "Dimik", "keywords": "Triple", "pack_code": "ms", "position": 64, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend clickclick. Trash any number of your rezzed cards. Give the Runner 1 tag for each card trashed this way.", "stripped_title": "Mutually Assured Destruction", "text": "As an additional cost to play this operation, spend [click][click].\nTrash any number of your rezzed cards. Give the Runner 1 tag for each card trashed this way.", "title": "Mutually Assured Destruction", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_trust_operation_33065(Operation):
    '''
    Cost: 0
    Text: Play only if the Runner is tagged. Trash 1 installed resource. Install and rez 1 card from Archives, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33065", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "Identify. Contact. Entrap. Counterintelligence never changes.", "illustrator": "Olie Boldador", "keywords": "Gray Ops", "pack_code": "ms", "position": 65, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Trash 1 installed resource. Install and rez 1 card from Archives, ignoring all costs.", "stripped_title": "Trust Operation", "text": "Play only if the Runner is tagged.\nTrash 1 installed resource. Install and rez 1 card from Archives, ignoring all costs.", "title": "Trust Operation", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_distributed_tracing_33100(Operation):
    '''
    Cost: 3
    Text: As an additional cost to play this operation, spend click. Play only if the Runner stole an agenda during their last turn. Give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33100", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "Sometimes, they want you to know that they know.", "illustrator": "Kira L. Nguyen", "keywords": "Double - Gray Ops", "pack_code": "ph", "position": 100, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, spend click. Play only if the Runner stole an agenda during their last turn. Give the Runner 1 tag.", "stripped_title": "Distributed Tracing", "text": "As an additional cost to play this operation, spend [click].\nPlay only if the Runner stole an agenda during their last turn.\nGive the Runner 1 tag.", "title": "Distributed Tracing", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_hypoxia_33101(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner is tagged. Do 1 core damage. The Runner gets -1 allotted click for their next turn. Remove this operation from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33101", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "You think that\u02bcs air you\u02bcre breathing now?", "illustrator": "Ed Mattinian", "keywords": "Black Ops", "pack_code": "ph", "position": 101, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner is tagged. Do 1 core damage. The Runner gets -1 allotted click for their next turn. Remove this operation from the game.", "stripped_title": "Hypoxia", "text": "Play only if the Runner is tagged.\nDo 1 core damage. The Runner gets -1 allotted [click] for their next turn.\nRemove this operation from the game.", "title": "Hypoxia", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_simulation_reset_33110(Operation):
    '''
    Cost: 1
    Text: Trash up to 5 cards from HQ. Shuffle that many cards from Archives into R&D. Draw that many cards. Remove this operation from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33110", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "\"The worst part about failed experiments? The queue for the incinerator.\"\n\u2014Overheard in the Issuaq Adaptics cafeteria.", "illustrator": "Anthony Hutchings", "pack_code": "ph", "position": 110, "quantity": 3, "side_code": "corp", "stripped_text": "Trash up to 5 cards from HQ. Shuffle that many cards from Archives into R&D. Draw that many cards. Remove this operation from the game.", "stripped_title": "Simulation Reset", "text": "Trash up to 5 cards from HQ. Shuffle that many cards from Archives into R&D. Draw that many cards.\nRemove this operation from the game.", "title": "Simulation Reset", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_nonequivalent_exchange_33118(Operation):
    '''
    Cost: 2
    Text: Gain 5 credits. You may have each player gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33118", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Oh, the text on these is endless. Just tap accept and you can read it later if you want.\"", "illustrator": "Dimik", "keywords": "Transaction", "pack_code": "ph", "position": 118, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 5 credits. You may have each player gain 2 credits.", "stripped_title": "Nonequivalent Exchange", "text": "Gain 5[credit]. You may have each player gain 2[credit].", "title": "Nonequivalent Exchange", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_shipment_from_vladisibirsk_33119(Operation):
    '''
    Cost: 1
    Text: Play only if the Runner has at least 2 tags. Place a total of 4 advancement counters on installed cards you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33119", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"Don\u02bct look at the crates.\"", "illustrator": "Ferenc Patk\u00f3s", "keywords": "Gray Ops", "pack_code": "ph", "position": 119, "quantity": 3, "side_code": "corp", "stripped_text": "Play only if the Runner has at least 2 tags. Place a total of 4 advancement counters on installed cards you can advance.", "stripped_title": "Shipment from Vladisibirsk", "text": "Play only if the Runner has at least 2 tags.\nPlace a total of 4 advancement counters on installed cards you can advance.", "title": "Shipment from Vladisibirsk", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class operation_end_of_the_line_33125(Operation):
    '''
    Cost: 3
    Text: As an additional cost to play this operation, remove 1 tag. Do 4 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33125", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "Under northern skies Sundog had lived all his life, and under them he would die.", "illustrator": "Olie Boldador", "keywords": "Black Ops", "pack_code": "ph", "position": 125, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play this operation, remove 1 tag. Do 4 meat damage.", "stripped_title": "End of the Line", "text": "As an additional cost to play this operation, remove 1 tag.\nDo 4 meat damage.", "title": "End of the Line", "type_code": "operation", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"
