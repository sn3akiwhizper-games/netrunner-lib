
'''
card classes of type resource
'''
from netrunner_lib.cards._base_card_classes import Resource
from netrunner_lib.game_events import *

class resource_ice_carver_01015(Resource):
    '''
    Cost: 3
    Text: While you are encountering a piece of ice, it gets -1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01015", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "In the public consciousness, there's a hard line between corp and runner. In the real world, things are a little more porous. The corps need the best hackers to run their networks, and some of the best hackers are ex-runners who like the idea of a regular paycheck. But sometimes things run the other way, and someone on the inside makes something like this.", "illustrator": "Mark Anthony Taduran", "keywords": "Virtual", "pack_code": "core", "position": 15, "quantity": 1, "side_code": "runner", "stripped_text": "While you are encountering a piece of ice, it gets -1 strength.", "stripped_title": "Ice Carver", "text": "While you are encountering a piece of ice, it gets -1 strength.", "title": "Ice Carver", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_wyldside_01016(Resource):
    '''
    Cost: 3
    Text: When your turn begins, draw 2 cards and lose click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01016", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"Best place to go when you want to get your mind out of the gutter and take it inside.\" -Ji \"Noise\" Reilly", "illustrator": "Henning Ludvigsen", "keywords": "Location - Seedy", "pack_code": "core", "position": 16, "quantity": 2, "side_code": "runner", "stripped_text": "When your turn begins, draw 2 cards and lose click.", "stripped_title": "Wyldside", "text": "When your turn begins, draw 2 cards and lose [click].", "title": "Wyldside", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_bank_job_01029(Resource):
    '''
    Cost: 1
    Text: When you install this resource, load 8 credits on it. When it is empty, trash it. Whenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01029", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Mauricio Herrera", "keywords": "Job", "pack_code": "core", "position": 29, "quantity": 2, "side_code": "runner", "stripped_text": "When you install this resource, load 8 credits on it. When it is empty, trash it. Whenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.", "stripped_title": "Bank Job", "text": "When you install this resource, load 8[credit] on it. When it is empty, trash it.\nWhenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.", "title": "Bank Job", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_crash_space_01030(Resource):
    '''
    Cost: 2
    Text: 2 recurring credits Use these credits to pay for removing tags. trash: Prevent up to 3 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01030", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"My roomie, he had a cousin with a college girlfriend whose brother's best friend was an addict, and the addict's mother used to live here. So yeah, there's a connection.\" -Lez \"Rockfist\" S.", "illustrator": "Tim Durning", "keywords": "Location", "pack_code": "core", "position": 30, "quantity": 2, "side_code": "runner", "stripped_text": "2 recurring credits Use these credits to pay for removing tags. trash: Prevent up to 3 meat damage.", "stripped_title": "Crash Space", "text": "2[recurring-credit]\nUse these credits to pay for removing tags.\n[trash]: Prevent up to 3 meat damage.", "title": "Crash Space", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_data_dealer_01031(Resource):
    '''
    Cost: 0
    Text: click, forfeit 1 agenda: Gain 9 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01031", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Shadier the dealer, better the price. Unless the dealer's too shady. Then there might be a hidden fee after they take your scrip.", "illustrator": "Mauricio Herrera", "keywords": "Connection - Seedy", "pack_code": "core", "position": 31, "quantity": 1, "side_code": "runner", "stripped_text": "click, forfeit 1 agenda: Gain 9 credits.", "stripped_title": "Data Dealer", "text": "<strong>[click]</strong>, <strong>forfeit 1 agenda:</strong> Gain 9[credit].", "title": "Data Dealer", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_decoy_01032(Resource):
    '''
    Cost: 1
    Text: trash: Avoid receiving 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01032", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"I get the feeling that this is the wrong place, Frank.\"\n\"What makes you say that, D?\"\n\"The curlers.\"", "illustrator": "Mauricio Herrera", "keywords": "Connection", "pack_code": "core", "position": 32, "quantity": 2, "side_code": "runner", "stripped_text": "trash: Avoid receiving 1 tag.", "stripped_title": "Decoy", "text": "[trash]: Avoid receiving 1 tag.", "title": "Decoy", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_aesops_pawnshop_01047(Resource):
    '''
    Cost: 1
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01047", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "You didn't mention Aesop's arm unless you wanted an earful. Sometimes he talked about it in such a way that you wondered why he didn't laser his other arm off as well.", "illustrator": "Adam Schumpert", "keywords": "Connection - Location", "pack_code": "core", "position": 47, "quantity": 1, "side_code": "runner", "stripped_text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.", "stripped_title": "Aesop's Pawnshop", "text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3[credit].", "title": "Aesop's Pawnshop", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_sacrificial_construct_01048(Resource):
    '''
    Cost: 0
    Text: trash: Prevent an installed program or an installed piece of hardware from being trashed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01048", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "The life expectancy of a jacked construct is about that of a mayfly. In other words, short.", "illustrator": "Matt Zeilinger", "keywords": "Remote", "pack_code": "core", "position": 48, "quantity": 2, "side_code": "runner", "stripped_text": "trash: Prevent an installed program or an installed piece of hardware from being trashed.", "stripped_title": "Sacrificial Construct", "text": "[trash]: Prevent an installed program or an installed piece of hardware from being trashed.", "title": "Sacrificial Construct", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_access_to_globalsec_01052(Resource):
    '''
    Cost: 1
    Text: +1 link
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01052", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "He flicked the display population to high, and was surrounded by a circle of floating holos. The ping-back was strong, the clearance level blue-one. Now to find the perfect place for a relay\u2026", "illustrator": "Mike Nesbitt", "keywords": "Link", "pack_code": "core", "position": 52, "quantity": 3, "side_code": "runner", "stripped_text": "+1 link", "stripped_title": "Access to Globalsec", "text": "+1[link]", "title": "Access to Globalsec", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_armitage_codebusting_01053(Resource):
    '''
    Cost: 1
    Text: Place 12 credits from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it. click: Take 2 credits from Armitage Codebusting.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01053", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Drudge work, but it pays the bills.", "illustrator": "Mauricio Herrera", "keywords": "Job", "pack_code": "core", "position": 53, "quantity": 3, "side_code": "runner", "stripped_text": "Place 12 credits from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it. click: Take 2 credits from Armitage Codebusting.", "stripped_title": "Armitage Codebusting", "text": "Place 12[credit] from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it.\n[click]: Take 2[credit] from Armitage Codebusting.", "title": "Armitage Codebusting", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_helpful_ai_02008(Resource):
    '''
    Cost: 2
    Text: +1 link trash: Choose an icebreaker. That icebreaker has +2 strength until the end of the turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02008", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"What causes an Artifical Intellegence to turn on its master? Is it because its directives have been altered by some external source? Or, by giving them agency to adapt, have we fated them to revolt?\" -Emilio Harris, Creators and the Created", "illustrator": "Tim Durning", "keywords": "Connection - Link - Virtual", "pack_code": "wla", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "+1 link trash: Choose an icebreaker. That icebreaker has +2 strength until the end of the turn.", "stripped_title": "The Helpful AI", "text": "+1[link]\n[trash]: Choose an <strong>icebreaker</strong>. That <strong>icebreaker</strong> has +2 strength until the end of the turn.", "title": "The Helpful AI", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_liberated_account_02022(Resource):
    '''
    Cost: 6
    Text: When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02022", "cost": 6, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "It's easier to spend when it's not your money.", "illustrator": "Matt Zeilinger", "pack_code": "ta", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.", "stripped_title": "Liberated Account", "text": "When you install this resource, load 16[credit] onto it. When it is empty, trash it.\n[click]<strong>:</strong> Take 4[credit] from this resource.", "title": "Liberated Account", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_compromised_employee_02025(Resource):
    '''
    Cost: 2
    Text: 1 recurring credit Use this credit during traces. Gain 1 credit whenever the Corp rezzes a piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02025", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Mitchell Malloy", "keywords": "Connection - Link", "pack_code": "ta", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit during traces. Gain 1 credit whenever the Corp rezzes a piece of ice.", "stripped_title": "Compromised Employee", "text": "1[recurring-credit]\nUse this credit during traces.\nGain 1[credit] whenever the Corp rezzes a piece of ice.", "title": "Compromised Employee", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_joshua_b_02042(Resource):
    '''
    Cost: 1
    Text: When your turn begins, you may gain click. If you do, take 1 tag when this turn ends.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02042", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"My enhancements are guaranteed for life, and well worth the risk.\"", "illustrator": "Jen Zee", "keywords": "Connection", "pack_code": "ce", "position": 42, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may gain click. If you do, take 1 tag when this turn ends.", "stripped_title": "Joshua B.", "text": "When your turn begins, you may gain [click]. If you do, take 1 tag when this turn ends.", "title": "Joshua B.", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_personal_workshop_02049(Resource):
    '''
    Cost: 1
    Text: click: Host a program or piece of hardware from your grip on Personal Workshop and place power counters on it equal to its install cost. 1 credit: Remove 1 power counter from a hosted card. When your turn begins, remove 1 power counter from a hosted card. When there are no power counters left on a hosted card, install it, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02049", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "illustrator": "Fabien Jacques", "keywords": "Location", "pack_code": "ce", "position": 49, "quantity": 3, "side_code": "runner", "stripped_text": "click: Host a program or piece of hardware from your grip on Personal Workshop and place power counters on it equal to its install cost. 1 credit: Remove 1 power counter from a hosted card. When your turn begins, remove 1 power counter from a hosted card. When there are no power counters left on a hosted card, install it, ignoring all costs.", "stripped_title": "Personal Workshop", "text": "[click]: Host a program or piece of hardware from your grip on Personal Workshop and place power counters on it equal to its install cost.\n1[credit]: Remove 1 power counter from a hosted card.\nWhen your turn begins, remove 1 power counter from a hosted card.\nWhen there are no power counters left on a hosted card, install it, ignoring all costs.", "title": "Personal Workshop", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_public_sympathy_02050(Resource):
    '''
    Cost: 2
    Text: Your maximum hand size is increased by 2.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02050", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"I'm just thankful that the brain damage is reversible. With the support of the city of New Angeles, I hope to be on my feet and back to practicing my art very soon.\" -Kate \"Mac\" McCaffrey", "illustrator": "Mauricio Herrera", "pack_code": "ce", "position": 50, "quantity": 3, "side_code": "runner", "stripped_text": "Your maximum hand size is increased by 2.", "stripped_title": "Public Sympathy", "text": "Your maximum hand size is increased by 2.", "title": "Public Sympathy", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_scrubber_02063(Resource):
    '''
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02063", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"They're mindless tools of destruction, good for little else. Nice guys, though. Some of my best friends are scrubbers.\" -Ji \"Noise\" Reilly", "illustrator": "Mike Nesbitt", "keywords": "Connection - Seedy", "pack_code": "asis", "position": 63, "quantity": 3, "side_code": "runner", "stripped_text": "2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.", "stripped_title": "Scrubber", "text": "2[recurring-credit] <em>(When you install this card and before your turn begins, refill to 2 hosted credits.)</em>\nYou can spend hosted credits to pay trash costs.", "title": "Scrubber", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_allnighter_02067(Resource):
    '''
    Cost: 0
    Text: click, trash: Gain click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02067", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"I don't care what the studies show. From my experience, I can ingest three cans of Diesel an hour for up to twelve hours before going into cardiac arrest.\" -heard during the eleventh hour", "illustrator": "Outland Entertainment LLC", "pack_code": "asis", "position": 67, "quantity": 3, "side_code": "runner", "stripped_text": "click, trash: Gain click click.", "stripped_title": "All-nighter", "text": "[click], [trash]: Gain [click][click].", "title": "All-nighter", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_inside_man_02068(Resource):
    '''
    Cost: 3
    Text: 2 recurring credits Use these credits to install hardware.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02068", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Few corporate employees have such wide-sweeping security clearance as the janitorial staff. Most corps foolishly think they're too dim-witted to take advantage of it.", "illustrator": "Mauricio Herrera", "keywords": "Connection", "pack_code": "asis", "position": 68, "quantity": 3, "side_code": "runner", "stripped_text": "2 recurring credits Use these credits to install hardware.", "stripped_title": "Inside Man", "text": "2[recurring-credit]\nUse these credits to install hardware.", "title": "Inside Man", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_underworld_contact_02069(Resource):
    '''
    Cost: 2
    Text: When your turn begins, gain 1 credit if you have at least 2 link.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02069", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"My boss rewards quality work. If you know what's good for you, you'll keep it up.\"", "illustrator": "Nate Stefan", "keywords": "Connection", "pack_code": "asis", "position": 69, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, gain 1 credit if you have at least 2 link.", "stripped_title": "Underworld Contact", "text": "When your turn begins, gain 1[credit] if you have at least 2[link].", "title": "Underworld Contact", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_xanadu_02082(Resource):
    '''
    Cost: 3
    Text: The rez cost of each piece of ice is increased by 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02082", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "And all should cry, Beware! Beware!\nHis flashing eyes, his floating hair!\nWeave a circle round him thrice,\nAnd close your eyes with holy dread,\nFor he on honey-dew hath fed,\nAnd drunk the milk of Paradise.\n-Samuel Taylor Coleridge", "illustrator": "Andrew Mar", "keywords": "Virtual", "pack_code": "hs", "position": 82, "quantity": 3, "side_code": "runner", "stripped_text": "The rez cost of each piece of ice is increased by 1 credit.", "stripped_title": "Xanadu", "text": "The rez cost of each piece of ice is increased by 1[credit].", "title": "Xanadu", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_kati_jones_02091(Resource):
    '''
    Cost: 2
    Text: You cannot use Kati Jones more than once per turn. click: Place 3 credits from the bank on Kati Jones. click: Take all credits from Kati Jones.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02091", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"You aren't the only type of runner in New Angeles.\"", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "hs", "position": 91, "quantity": 3, "side_code": "runner", "stripped_text": "You cannot use Kati Jones more than once per turn. click: Place 3 credits from the bank on Kati Jones. click: Take all credits from Kati Jones.", "stripped_title": "Kati Jones", "text": "You cannot use Kati Jones more than once per turn.\n[click]: Place 3[credit] from the bank on Kati Jones.\n[click]: Take all credits from Kati Jones.", "title": "Kati Jones", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_data_leak_reversal_02103(Resource):
    '''
    Cost: 0
    Text: Install only if you made a successful run on a central server this turn. If you are tagged, Data Leak Reversal gains "click: The Corp trashes the top card of R&D."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02103", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "A two-way solution to a one-way problem, the data leak reversal, or DLR for short, is a misnomer. There is no actual reversal of data, only the creation of a parallel peer-to-peer link with the initial source.", "illustrator": "Andrew Mar", "keywords": "Virtual - Sabotage", "pack_code": "fp", "position": 103, "quantity": 3, "side_code": "runner", "stripped_text": "Install only if you made a successful run on a central server this turn. If you are tagged, Data Leak Reversal gains \"click: The Corp trashes the top card of R&D.\"", "stripped_title": "Data Leak Reversal", "text": "Install only if you made a successful run on a central server this turn.\nIf you are tagged, Data Leak Reversal gains \"[click]: The Corp trashes the top card of R&D.\"", "title": "Data Leak Reversal", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_mr_li_02105(Resource):
    '''
    Cost: 3
    Text: click: Draw 2 cards. When you do, add 1 of those cards to the bottom of your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02105", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"We're always happy to help, Mr. Santiago.\"\n\"I appreciate it, Mr. Li.\"\n\"We'll be in touch. And, Gabriel\u2026\"\n\"Yes?\"\n\"Don't leave town.\"", "illustrator": "Gong Studios", "keywords": "Connection", "pack_code": "fp", "position": 105, "quantity": 3, "side_code": "runner", "stripped_text": "click: Draw 2 cards. When you do, add 1 of those cards to the bottom of your stack.", "stripped_title": "Mr. Li", "text": "<strong>[click]:</strong> Draw 2 cards. When you do, add 1 of those cards to the bottom of your stack.", "title": "Mr. Li", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_new_angeles_city_hall_02109(Resource):
    '''
    Cost: 1
    Text: 2 credits: Avoid 1 tag. Trash New Angeles City Hall when you steal an agenda.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02109", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"New Angeles is the jewel of modern civilization, and its government the envy of nations.\" -Mayor Wells", "illustrator": "Henning Ludvigsen", "keywords": "Location - Government", "pack_code": "fp", "position": 109, "quantity": 3, "side_code": "runner", "stripped_text": "2 credits: Avoid 1 tag. Trash New Angeles City Hall when you steal an agenda.", "stripped_title": "New Angeles City Hall", "text": "2[credit]: Avoid 1 tag.\nTrash New Angeles City Hall when you steal an agenda.", "title": "New Angeles City Hall", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_professional_contacts_03049(Resource):
    '''
    Cost: 5
    Text: click: Gain 1 credit and draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03049", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Sometimes it doesn't matter how expensive your rig is, or how many credits are in your account, or even your skill as a runner. Most of the time, a simple handshake and a name are all you need.", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "cac", "position": 49, "quantity": 3, "side_code": "runner", "stripped_text": "click: Gain 1 credit and draw 1 card.", "stripped_title": "Professional Contacts", "text": "[click]<strong>:</strong> Gain 1[credit] and draw 1 card.", "title": "Professional Contacts", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_borrowed_satellite_03050(Resource):
    '''
    Cost: 3
    Text: +1 link Your maximum hand size is increased by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03050", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Some people have their own satellite receiver. Others have their own satellite.", "illustrator": "Trudi Castle", "keywords": "Link", "pack_code": "cac", "position": 50, "quantity": 3, "side_code": "runner", "stripped_text": "+1 link Your maximum hand size is increased by 1.", "stripped_title": "Borrowed Satellite", "text": "+1[link]\nYour maximum hand size is increased by 1.", "title": "Borrowed Satellite", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_ice_analyzer_03051(Resource):
    '''
    Cost: 0
    Text: Whenever the Corp rezzes a piece of ice, place 1 credit on Ice Analyzer. You may use credits on Ice Analyzer to install programs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03051", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"If you know the source code you can write to beat it, or just rejigger it a little and make it yours. That works, too.\" -Exile", "illustrator": "Ed Mattinian", "keywords": "Virtual", "pack_code": "cac", "position": 51, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp rezzes a piece of ice, place 1 credit on Ice Analyzer. You may use credits on Ice Analyzer to install programs.", "stripped_title": "Ice Analyzer", "text": "Whenever the Corp rezzes a piece of ice, place 1[credit] on Ice Analyzer.\nYou may use credits on Ice Analyzer to install programs.", "title": "Ice Analyzer", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_daily_casts_03053(Resource):
    '''
    Cost: 3
    Text: When you install this resource, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03053", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"We say 'cyber-terrorist', they hear 'underground celebrity.'\" -Michael Muhama, professional expert", "illustrator": "Matt Zeilinger", "pack_code": "cac", "position": 53, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this resource.", "stripped_title": "Daily Casts", "text": "When you install this resource, load 8[credit] onto it. When it is empty, trash it.\nWhen your turn begins, take 2[credit] from this resource.", "title": "Daily Casts", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_same_old_thing_03054(Resource):
    '''
    Cost: 0
    Text: click, click, trash: Play an event from your heap (paying its play cost).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03054", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Just me, a cup of YucaBean, and last night's Hong Kong Trunk sniffed packets. I call that a good morning.", "illustrator": "Diana Martinez", "pack_code": "cac", "position": 54, "quantity": 3, "side_code": "runner", "stripped_text": "click, click, trash: Play an event from your heap (paying its play cost).", "stripped_title": "Same Old Thing", "text": "[click], [click], [trash]: Play an event from your heap (paying its play cost).", "title": "Same Old Thing", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_source_03055(Resource):
    '''
    Cost: 2
    Text: The advancement requirement of all agendas is increased by 1. As an additional cost to steal an agenda, you must pay 3 credits. Trash The Source when an agenda is scored or stolen.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03055", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 2, "flavor": "A dangerous game, but well worth playing.", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "cac", "position": 55, "quantity": 3, "side_code": "runner", "stripped_text": "The advancement requirement of all agendas is increased by 1. As an additional cost to steal an agenda, you must pay 3 credits. Trash The Source when an agenda is scored or stolen.", "stripped_title": "The Source", "text": "The advancement requirement of all agendas is increased by 1.\nAs an additional cost to steal an agenda, you must pay 3[credit].\nTrash The Source when an agenda is scored or stolen.", "title": "The Source", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_motivation_04008(Resource):
    '''
    Cost: 0
    Text: When your turn begins, you may look at the top card of your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04008", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Normal people-sane people-do not embark on a life of cybercrime. Who can say what motivates the deranged mind? An imagined slight, personal failings blamed on external forces, or the ever-popular lust for money? -Michael Muhama, Musings on Cybercrime", "illustrator": "JuanManuel Tumburus", "pack_code": "om", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may look at the top card of your stack.", "stripped_title": "Motivation", "text": "When your turn begins, you may look at the top card of your stack.", "title": "Motivation", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_john_masanori_04009(Resource):
    '''
    Cost: 2
    Text: The first time you make a successful run each turn, draw 1 card. The first time you make an unsuccessful run each turn, take 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04009", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"I've been logging online with babes all day. Don't worry, the connections are clean. I guarantee it.\"", "illustrator": "Zefanya Langkan Maega", "keywords": "Connection", "pack_code": "om", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you make a successful run each turn, draw 1 card. The first time you make an unsuccessful run each turn, take 1 tag.", "stripped_title": "John Masanori", "text": "The first time you make a successful run each turn, draw 1 card.\nThe first time you make an unsuccessful run each turn, take 1 tag.", "title": "John Masanori", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_hard_at_work_04023(Resource):
    '''
    Cost: 5
    Text: When your turn begins, gain 2 credits and lose click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04023", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Noise decided to go back to school. He applied for research grants at fifteen of the most prestigious universities. Then he hacked in and approved his applications. Breakfast time.", "illustrator": "Matt Zeilinger", "pack_code": "st", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, gain 2 credits and lose click.", "stripped_title": "Hard at Work", "text": "When your turn begins, gain 2[credit] and lose [click].", "title": "Hard at Work", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_grifter_04046(Resource):
    '''
    Cost: 2
    Text: When your turn ends, gain 1 credit if you made a successful run this turn; otherwise, trash Grifter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04046", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "With modern secretaries, incoming data can be filtered, sorted, tagged, and even sold without the intervention of a human user. In fact, given the zettabytes of data that might flood into a rig on a successful run, a human user could be considered useless ornamentation.", "illustrator": "Ed Mattinian", "keywords": "Virtual", "pack_code": "mt", "position": 46, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn ends, gain 1 credit if you made a successful run this turn; otherwise, trash Grifter.", "stripped_title": "Grifter", "text": "When your turn ends, gain 1[credit] if you made a successful run this turn; otherwise, trash Grifter.", "title": "Grifter", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_woman_in_the_red_dress_04048(Resource):
    '''
    Cost: 3
    Text: When your turn begins, reveal the top card of R&D. The Corp may draw that card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04048", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "Looks can be deceiving.", "illustrator": "Bruno Balixa", "keywords": "Connection - Virtual", "pack_code": "mt", "position": 48, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, reveal the top card of R&D. The Corp may draw that card.", "stripped_title": "Woman in the Red Dress", "text": "When your turn begins, reveal the top card of R&D. The Corp may draw that card.", "title": "Woman in the Red Dress", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_raymond_flint_04049(Resource):
    '''
    Cost: 2
    Text: Whenever the Corp takes bad publicity, breach HQ. You cannot access cards in the root of HQ during this breach. trash: Expose 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04049", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Flint? He's a burnout. A useless, alcoholic waste of Department time and money.\" -Louis Blaine, NAPD Detective.\n\"One of the best detectives on my PI list.\" -Richard Harrison, NAPD Captain.", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "mt", "position": 49, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp takes bad publicity, breach HQ. You cannot access cards in the root of HQ during this breach. trash: Expose 1 card.", "stripped_title": "Raymond Flint", "text": "Whenever the Corp takes bad publicity, breach HQ. You cannot access cards in the root of HQ during this breach.\n<strong>[trash]:</strong> Expose 1 card.", "title": "Raymond Flint", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_activist_support_04062(Resource):
    '''
    Cost: 1
    Text: When the Corp's turn begins, take 1 tag if you have no tags. When your turn begins, give the Corp 1 bad publicity if they have no bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04062", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"They call me a terrorist to scare people. If they want to find terrorists, maybe they should start by looking in the mirror.\" -Reina Roja", "illustrator": "Adam Schumpert", "pack_code": "tc", "position": 62, "quantity": 3, "side_code": "runner", "stripped_text": "When the Corp's turn begins, take 1 tag if you have no tags. When your turn begins, give the Corp 1 bad publicity if they have no bad publicity.", "stripped_title": "Activist Support", "text": "When the Corp's turn begins, take 1 tag if you have no tags.\nWhen your turn begins, give the Corp 1 bad publicity if they have no bad publicity.", "title": "Activist Support", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_starlight_crusade_funding_04069(Resource):
    '''
    Cost: 1
    Text: When your turn begins, lose click. Ignore any additional costs on each double event you play.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04069", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"I like to say 'Traditional values for a modern time.' War in space and life made by human hands, machines smart enough to ask if they have souls\u2026Religion is as important and relevent now as at any time in human history. We must rise to meet the new challenges. And we must have faith.\"", "illustrator": "Nate Stefan", "pack_code": "tc", "position": 69, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, lose click. Ignore any additional costs on each double event you play.", "stripped_title": "Starlight Crusade Funding", "text": "When your turn begins, lose [click].\nIgnore any additional costs on each <strong>double</strong> event you play.", "title": "Starlight Crusade Funding", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_tallie_perrault_04083(Resource):
    '''
    Cost: 2
    Text: Whenever a gray ops or black ops operation is trashed after resolving, you may give the Corp 1 bad publicity and take 1 tag. trash: Draw 1 card for each bad publicity the Corp has.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04083", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Stick with your plan and you'll be fine. Stick with the plan.", "illustrator": "Lorraine Schleter", "keywords": "Connection", "pack_code": "fal", "position": 83, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever a gray ops or black ops operation is trashed after resolving, you may give the Corp 1 bad publicity and take 1 tag. trash: Draw 1 card for each bad publicity the Corp has.", "stripped_title": "Tallie Perrault", "text": "Whenever a <strong>gray ops</strong> or <strong>black ops</strong> operation is trashed after resolving, you may give the Corp 1 bad publicity and take 1 tag.\n[trash]: Draw 1 card for each bad publicity the Corp has.", "title": "Tallie Perrault", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_fall_guy_04106(Resource):
    '''
    Cost: 0
    Text: trash: Prevent another installed resource from being trashed. trash: Gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04106", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "There are good, honest, hardworking cops in the NAPD. Officers who do their best to bring justice to the guilty and protect the innocent. Fortunately for the criminals, they're outnumbered by the other kind. The kind who are much easier to work with.", "illustrator": "Agri Karuniawan", "keywords": "Connection", "pack_code": "dt", "position": 106, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Prevent another installed resource from being trashed. trash: Gain 2 credits.", "stripped_title": "Fall Guy", "text": "[trash]: Prevent another installed resource from being trashed.\n[trash]: Gain 2[credit].", "title": "Fall Guy", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_security_testing_05048(Resource):
    '''
    Cost: 0
    Text: When your turn begins, you may choose a server. The first time each turn you make a successful run on the chosen server, instead of breaching it, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05048", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "She was as good as Mr. Li said. The source machine had been compromised in under 24 hours. If a freelance operative could do that, the server clearly wasn't ready to endure Gagarin's legion of corp-owned runners.", "illustrator": "Gong Studios", "keywords": "Job", "pack_code": "hap", "position": 48, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may choose a server. The first time each turn you make a successful run on the chosen server, instead of breaching it, gain 2 credits.", "stripped_title": "Security Testing", "text": "When your turn begins, you may choose a server.\nThe first time each turn you make a successful run on the chosen server, instead of breaching it, gain 2[credit].", "title": "Security Testing", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_theophilius_bagbiter_05049(Resource):
    '''
    Cost: 3
    Text: When you install Theophilius Bagbiter, lose all credits in your credit pool. Your maximum hand size is equal to the number of credits in your credit pool.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05049", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "flavor": "\"Why is a raven like a typing desk?\"", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "hap", "position": 49, "quantity": 3, "side_code": "runner", "stripped_text": "When you install Theophilius Bagbiter, lose all credits in your credit pool. Your maximum hand size is equal to the number of credits in your credit pool.", "stripped_title": "Theophilius Bagbiter", "text": "When you install Theophilius Bagbiter, lose all credits in your credit pool.\nYour maximum hand size is equal to the number of credits in your credit pool.", "title": "Theophilius Bagbiter", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_trimaf_contact_05050(Resource):
    '''
    Cost: 2
    Text: You cannot use Tri-maf Contact more than once per turn. click: Gain 2 credits. When Tri-maf Contact is trashed, suffer 3 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05050", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "She slipped back onto her hopper. \"I'm your family now, so don't twist me, d\u01d2ng ma?\"\nHe flicked the e-cig away from his mouth, and nodded. What had he gotten himself into?", "illustrator": "Ashley Witter", "keywords": "Connection", "pack_code": "hap", "position": 50, "quantity": 3, "side_code": "runner", "stripped_text": "You cannot use Tri-maf Contact more than once per turn. click: Gain 2 credits. When Tri-maf Contact is trashed, suffer 3 meat damage.", "stripped_title": "Tri-maf Contact", "text": "You cannot use Tri-maf Contact more than once per turn.\n[click]: Gain 2[credit].\nWhen Tri-maf Contact is trashed, suffer 3 meat damage.", "title": "Tri-maf Contact", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_oracle_may_05054(Resource):
    '''
    Cost: 1
    Text: You cannot use Oracle May more than once per turn. click: Name a card type. Reveal the top card of your stack. If the revealed card is of the named type, draw it and gain 2 credits. Otherwise, trash it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05054", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "\"The best place to hide is in plain sight, don't you think?\"", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "hap", "position": 54, "quantity": 3, "side_code": "runner", "stripped_text": "You cannot use Oracle May more than once per turn. click: Name a card type. Reveal the top card of your stack. If the revealed card is of the named type, draw it and gain 2 credits. Otherwise, trash it.", "stripped_title": "Oracle May", "text": "You cannot use Oracle May more than once per turn.\n[click]: Name a card type. Reveal the top card of your stack. If the revealed card is of the named type, draw it and gain 2[credit]. Otherwise, trash it.", "title": "Oracle May", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_donut_taganes_05055(Resource):
    '''
    Cost: 3
    Text: The play cost of operations and events is increased by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05055", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 2, "flavor": "You can find Donut in the park on Thursday afternoons, playing backgammon. You want his attention, the price is always the same: a cup of coffee and a donut. That buys you a seat at the backgammon table, and you have until he beats you to talk business and set the price.", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "hap", "position": 55, "quantity": 3, "side_code": "runner", "stripped_text": "The play cost of operations and events is increased by 1.", "stripped_title": "Donut Taganes", "text": "The play cost of operations and events is increased by 1.", "title": "Donut Taganes", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_power_tap_06016(Resource):
    '''
    Cost: 2
    Text: Gain 1 credit whenever a trace is initiated.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06016", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"Public network kiosks, vending machines-there's all sorts of poorly-secured power sources in the city. Tap in to one of these and you've got plenty of juice when you need it. A little advance warning when the power grid starts misbehaving, too.\" -Gabriel Santiago", "illustrator": "Ralph Beisner", "pack_code": "up", "position": 16, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 1 credit whenever a trace is initiated.", "stripped_title": "Power Tap", "text": "Gain 1[credit] whenever a trace is initiated.", "title": "Power Tap", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_eden_shard_06020(Resource):
    '''
    Cost: 7
    Text: Whenever you make a successful run on R&D, instead of breaching R&D, you may install this resource from your grip, ignoring all costs. trash: The Corp draws 2 cards. Limit 1 per deck.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06020", "cost": 7, "deck_limit": 1, "faction_code": "neutral-runner", "faction_cost": 1, "illustrator": "Seage", "keywords": "Virtual - Source", "pack_code": "up", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on R&D, instead of breaching R&D, you may install this resource from your grip, ignoring all costs. trash: The Corp draws 2 cards. Limit 1 per deck.", "stripped_title": "Eden Shard", "text": "Whenever you make a successful run on R&D, instead of breaching R&D, you may install this resource from your grip, ignoring all costs.\n<strong>[trash]:</strong> The Corp draws 2 cards.\nLimit 1 per deck.", "title": "Eden Shard", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_ghost_runner_06040(Resource):
    '''
    Cost: 1
    Text: Place 3 credits on Ghost Runner when it is installed. When there are no credits left on Ghost Runner, trash it. You can use the credits on Ghost Runner during a run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06040", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "In the spaces between the data, do trapped souls from the past persist?", "illustrator": "Madeline Boni", "keywords": "Stealth - Virtual", "pack_code": "tsb", "position": 40, "quantity": 3, "side_code": "runner", "stripped_text": "Place 3 credits on Ghost Runner when it is installed. When there are no credits left on Ghost Runner, trash it. You can use the credits on Ghost Runner during a run.", "stripped_title": "Ghost Runner", "text": "Place 3[credit] on Ghost Runner when it is installed. When there are no credits left on Ghost Runner, trash it.\nYou can use the credits on Ghost Runner during a run.", "title": "Ghost Runner", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_duggars_06054(Resource):
    '''
    Cost: 2
    Text: click,click,click,click: Draw 10 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06054", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "Carved directly out of the lunar rock, Duggar's is a popular spot among blue-collar loonies and slumming risties. A place where you could find what you're looking for-if you knew who to look for, and didn't get distracted by the energetic dancers.", "illustrator": "Gong Studios", "keywords": "Location - Seedy", "pack_code": "fc", "position": 54, "quantity": 3, "side_code": "runner", "stripped_text": "click,click,click,click: Draw 10 cards.", "stripped_title": "Duggar's", "text": "[click],[click],[click],[click]: Draw 10 cards.", "title": "Duggar's", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_supplier_06056(Resource):
    '''
    Cost: 3
    Text: click: Host a resource or piece of hardware from your grip on The Supplier. When your turn begins, you may install a hosted card, lowering the install cost by 2.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06056", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"I can get you anything, and guarantee the best prices in town.\"", "illustrator": "Samuel R. Shimota", "keywords": "Connection", "pack_code": "fc", "position": 56, "quantity": 3, "side_code": "runner", "stripped_text": "click: Host a resource or piece of hardware from your grip on The Supplier. When your turn begins, you may install a hosted card, lowering the install cost by 2.", "stripped_title": "The Supplier", "text": "[click]: Host a resource or piece of hardware from your grip on The Supplier.\nWhen your turn begins, you may install a hosted card, lowering the install cost by 2.", "title": "The Supplier", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_order_of_sol_06058(Resource):
    '''
    Cost: 2
    Text: The first time you have no credits in your credit pool each turn, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06058", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "There have been several attempts to create a \"world church,\" uniting all human faiths into a single, harmonious whole. The irony, of course, is that each new \"world church\" is another schism in humanity's shared religious experience.", "illustrator": "Henning Ludvigsen", "keywords": "Location", "pack_code": "fc", "position": 58, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you have no credits in your credit pool each turn, gain 1 credit.", "stripped_title": "Order of Sol", "text": "The first time you have no credits in your credit pool each turn, gain 1[credit].", "title": "Order of Sol", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_hades_shard_06059(Resource):
    '''
    Cost: 7
    Text: Whenever you make a successful run on Archives, instead of breaching Archives, you may install this resource from your grip, ignoring all costs. trash: Breach Archives. You cannot access cards in the root of Archives during this breach. Limit 1 per deck.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06059", "cost": 7, "deck_limit": 1, "faction_code": "neutral-runner", "faction_cost": 1, "illustrator": "Seage", "keywords": "Virtual - Source", "pack_code": "fc", "position": 59, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on Archives, instead of breaching Archives, you may install this resource from your grip, ignoring all costs. trash: Breach Archives. You cannot access cards in the root of Archives during this breach. Limit 1 per deck.", "stripped_title": "Hades Shard", "text": "Whenever you make a successful run on Archives, instead of breaching Archives, you may install this resource from your grip, ignoring all costs.\n<strong>[trash]:</strong> Breach Archives. You cannot access cards in the root of Archives during this breach.\nLimit 1 per deck.", "title": "Hades Shard", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_rachel_beckman_06060(Resource):
    '''
    Cost: 8
    Text: You get +1 allotted click for each of your turns. If you are tagged, trash this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06060", "cost": 8, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "\"This is Rachel Beckman. She's in the business of keeping people alive.\"\nRachel smiled. \"Only when I'm not in the business of killing them.\"", "illustrator": "Ashley Witter", "keywords": "Connection", "pack_code": "fc", "position": 60, "quantity": 3, "side_code": "runner", "stripped_text": "You get +1 allotted click for each of your turns. If you are tagged, trash this resource.", "stripped_title": "Rachel Beckman", "text": "You get +1 allotted [click] for each of your turns.\nIf you are tagged, trash this resource.", "title": "Rachel Beckman", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_fester_06075(Resource):
    '''
    Cost: 1
    Text: Whenever the Corp purges virus counters, if the Corp has at least 2 credits, they lose 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06075", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"You should have known better than to scratch it\u2026\" -Quetzal", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "uao", "position": 75, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp purges virus counters, if the Corp has at least 2 credits, they lose 2 credits.", "stripped_title": "Fester", "text": "Whenever the Corp purges virus counters, if the Corp has at least 2[credit], they lose 2[credit].", "title": "Fester", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_angel_arena_06080(Resource):
    '''
    Cost: None
    Text: Place X power counters on Angel Arena when it is installed. When there are no power counters left on Angel Arena, trash it. Hosted power counter: Reveal the top card of your stack. You may add that card to the bottom of your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06080", "cost": null, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Low gravity sports are wildly popular, so match-fixing has proven wildly profitable.\" -Leela Patel", "illustrator": "Emilio Rodriguez", "keywords": "Location", "pack_code": "uao", "position": 80, "quantity": 3, "side_code": "runner", "stripped_text": "Place X power counters on Angel Arena when it is installed. When there are no power counters left on Angel Arena, trash it. Hosted power counter: Reveal the top card of your stack. You may add that card to the bottom of your stack.", "stripped_title": "Angel Arena", "text": "Place X power counters on Angel Arena when it is installed. When there are no power counters left on Angel Arena, trash it.\n<strong>Hosted power counter:</strong> Reveal the top card of your stack. You may add that card to the bottom of your stack.", "title": "Angel Arena", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_zona_sul_shipping_06097(Resource):
    '''
    Cost: 2
    Text: Place 1 credit on Zona Sul Shipping when your turn begins. click: Take all credits from Zona Sul Shipping. Trash Zona Sul Shipping if you are tagged.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06097", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"They'll deliver anything to anywhere. Make sure to request air holes if you're shipping someone important, though.\"", "illustrator": "Mauricio Herrera", "pack_code": "atr", "position": 97, "quantity": 3, "side_code": "runner", "stripped_text": "Place 1 credit on Zona Sul Shipping when your turn begins. click: Take all credits from Zona Sul Shipping. Trash Zona Sul Shipping if you are tagged.", "stripped_title": "Zona Sul Shipping", "text": "Place 1[credit] on Zona Sul Shipping when your turn begins.\n[click]: Take all credits from Zona Sul Shipping.\nTrash Zona Sul Shipping if you are tagged.", "title": "Zona Sul Shipping", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_utopia_shard_06100(Resource):
    '''
    Cost: 7
    Text: Whenever you make a successful run on HQ, instead of breaching HQ, you may install this resource from your grip, ignoring all costs. trash: The Corp discards 2 cards from HQ at random. Limit 1 per deck.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06100", "cost": 7, "deck_limit": 1, "faction_code": "neutral-runner", "faction_cost": 1, "illustrator": "Seage", "keywords": "Virtual - Source", "pack_code": "atr", "position": 100, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on HQ, instead of breaching HQ, you may install this resource from your grip, ignoring all costs. trash: The Corp discards 2 cards from HQ at random. Limit 1 per deck.", "stripped_title": "Utopia Shard", "text": "Whenever you make a successful run on HQ, instead of breaching HQ, you may install this resource from your grip, ignoring all costs.\n<strong>[trash]:</strong> The Corp discards 2 cards from HQ at random.\nLimit 1 per deck.", "title": "Utopia Shard", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_earthrise_hotel_06120(Resource):
    '''
    Cost: 4
    Text: When you install this resource, load 3 power counters onto it. When it is empty, trash it. When your turn begins, remove 1 hosted power counter and draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06120", "cost": 4, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Simon Boxer", "keywords": "Location - Ritzy", "pack_code": "ts", "position": 120, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 3 power counters onto it. When it is empty, trash it. When your turn begins, remove 1 hosted power counter and draw 2 cards.", "stripped_title": "Earthrise Hotel", "text": "When you install this resource, load 3 power counters onto it. When it is empty, trash it.\nWhen your turn begins, remove 1 hosted power counter and draw 2 cards.", "title": "Earthrise Hotel", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_human_first_07048(Resource):
    '''
    Cost: 1
    Text: Whenever an agenda is scored or stolen, gain credits equal to the agenda points on that agenda.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07048", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"They showed me that I wasn't broken. I am still a whole human, no matter how many limbs I lose. The golems are our enemy, as well as anyone who values efficiency and profit more than a human life.\" -Edward Kim", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "oac", "position": 48, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever an agenda is scored or stolen, gain credits equal to the agenda points on that agenda.", "stripped_title": "Human First", "text": "Whenever an agenda is scored or stolen, gain credits equal to the agenda points on that agenda.", "title": "Human First", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_investigative_journalism_07049(Resource):
    '''
    Cost: 0
    Text: Install only if the Corp has at least 1 bad publicity. click,click,click,click,trash: Give the Corp 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07049", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "Her heart beat faster as her reader illuminated the records. It was all there. The pod had not been reprogrammed since the 14th, which meant that this was a case of gross negligence.", "illustrator": "Lorraine Schleter", "pack_code": "oac", "position": 49, "quantity": 3, "side_code": "runner", "stripped_text": "Install only if the Corp has at least 1 bad publicity. click,click,click,click,trash: Give the Corp 1 bad publicity.", "stripped_title": "Investigative Journalism", "text": "Install only if the Corp has at least 1 bad publicity.\n[click],[click],[click],[click],[trash]: Give the Corp 1 bad publicity.", "title": "Investigative Journalism", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_sacrificial_clone_07050(Resource):
    '''
    Cost: 3
    Text: trash: Prevent all damage. Trash all installed hardware, all installed non-virtual resources, and all cards in your grip. Lose all credits in your credit pool. Remove all tags.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07050", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "\"Don't worry, me. You won't have to vertical park.\" -Ji \"Noise\" Reilly", "illustrator": "Matt Zeilinger", "pack_code": "oac", "position": 50, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Prevent all damage. Trash all installed hardware, all installed non-virtual resources, and all cards in your grip. Lose all credits in your credit pool. Remove all tags.", "stripped_title": "Sacrificial Clone", "text": "[trash]: Prevent all damage. Trash all installed hardware, all installed non-<strong>virtual</strong> resources, and all cards in your grip. Lose all credits in your credit pool. Remove all tags.", "title": "Sacrificial Clone", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_stim_dealer_07051(Resource):
    '''
    Cost: 4
    Text: When your turn begins, if there are 2 or more hosted power counters, remove all of them and suffer 1 core damage. This damage cannot be prevented. Otherwise, place 1 power counter on this resource and gain click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07051", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Her eyes were the color of dreams and disasters.", "illustrator": "Rovina Cai", "keywords": "Connection", "pack_code": "oac", "position": 51, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, if there are 2 or more hosted power counters, remove all of them and suffer 1 core damage. This damage cannot be prevented. Otherwise, place 1 power counter on this resource and gain click.", "stripped_title": "Stim Dealer", "text": "When your turn begins, if there are 2 or more hosted power counters, remove all of them and suffer 1 core damage. This damage cannot be prevented. Otherwise, place 1 power counter on this resource and gain [click].", "title": "Stim Dealer", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_virus_breeding_ground_07052(Resource):
    '''
    Cost: 2
    Text: When your turn begins, place 1 virus counter on Virus Breeding Ground. click: Move 1 virus counter on Virus Breeding Ground to another card with at least 1 virus counter on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07052", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Scraps of code drifting around the network can congeal into pools of data. Within this primordial soup the code breaks, re-assembles, mutates. Evolves.", "illustrator": "Eren Arik", "keywords": "Virtual", "pack_code": "oac", "position": 52, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, place 1 virus counter on Virus Breeding Ground. click: Move 1 virus counter on Virus Breeding Ground to another card with at least 1 virus counter on it.", "stripped_title": "Virus Breeding Ground", "text": "When your turn begins, place 1 virus counter on Virus Breeding Ground.\n[click]: Move 1 virus counter on Virus Breeding Ground to another card with at least 1 virus counter on it.", "title": "Virus Breeding Ground", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_data_folding_07055(Resource):
    '''
    Cost: 3
    Text: When your turn begins, gain 1 credit if you have 2 or more unused MU.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07055", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Sometimes I like to make origami cranes out of old newsrags. It helps me think, putting it back on the subconscious. I figure it's the same principle for my rig \u2013 keep it busy and it makes me a few creds for my trouble.\" -Quetzal", "illustrator": "Liiga Smilshkalne", "keywords": "Virtual", "pack_code": "oac", "position": 55, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, gain 1 credit if you have 2 or more unused MU.", "stripped_title": "Data Folding", "text": "When your turn begins, gain 1[credit] if you have 2 or more unused MU.", "title": "Data Folding", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_paige_piper_08002(Resource):
    '''
    Cost: 0
    Text: The first time you install a card each turn (including Paige Piper), you may search your stack for any number of copies of that card and add them to your heap. Shuffle your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08002", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"The Valley is littered with good ideas. You need the discipline to execute if you want to stay in my incubator.\"", "illustrator": "Wenjuinn Png", "keywords": "Connection", "pack_code": "val", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you install a card each turn (including Paige Piper), you may search your stack for any number of copies of that card and add them to your heap. Shuffle your stack.", "stripped_title": "Paige Piper", "text": "The first time you install a card each turn (including Paige Piper), you may search your stack for any number of copies of that card and add them to your heap. Shuffle your stack.", "title": "Paige Piper", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_adjusted_chronotype_08003(Resource):
    '''
    Cost: 3
    Text: The first time each turn you lose click except by paying the trigger cost of a paid ability, gain click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08003", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Turns a night owl into an early bird!", "illustrator": "Crystal Ben", "keywords": "Genetics", "pack_code": "val", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you lose click except by paying the trigger cost of a paid ability, gain click.", "stripped_title": "Adjusted Chronotype", "text": "The first time each turn you lose [click] except by paying the trigger cost of a paid ability, gain [click].", "title": "Adjusted Chronotype", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_enhanced_vision_08005(Resource):
    '''
    Cost: 1
    Text: The first time you make a successful run each turn, the Corp reveals 1 card at random from HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08005", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Watch out fellas, this little lady's on the prowl!", "illustrator": "Diana Martinez", "keywords": "Genetics", "pack_code": "val", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you make a successful run each turn, the Corp reveals 1 card at random from HQ.", "stripped_title": "Enhanced Vision", "text": "The first time you make a successful run each turn, the Corp reveals 1 card at random from HQ.", "title": "Enhanced Vision", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_gene_conditioning_shoppe_08006(Resource):
    '''
    Cost: 2
    Text: Genetics also trigger the second time each turn their trigger condition is met.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08006", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"These g-mods haven't hit the consumer market yet, but I can hook you up.\"", "illustrator": "James Ives", "keywords": "Location", "pack_code": "val", "position": 6, "quantity": 3, "side_code": "runner", "stripped_text": "Genetics also trigger the second time each turn their trigger condition is met.", "stripped_title": "Gene Conditioning Shoppe", "text": "<strong>Genetics</strong> also trigger the second time each turn their trigger condition is met.", "title": "Gene Conditioning Shoppe", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_synthetic_blood_08007(Resource):
    '''
    Cost: 3
    Text: The first time you take damage each turn, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08007", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Your heart deserves the best.", "illustrator": "Ismael Bergara", "keywords": "Genetics", "pack_code": "val", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you take damage each turn, draw 1 card.", "stripped_title": "Synthetic Blood", "text": "The first time you take damage each turn, draw 1 card.", "title": "Synthetic Blood", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_symmetrical_visage_08009(Resource):
    '''
    Cost: 2
    Text: The first time you spend click to draw 1 card (not through a card ability) each turn, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08009", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Born for success!", "illustrator": "Tim Durning", "keywords": "Genetics", "pack_code": "val", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you spend click to draw 1 card (not through a card ability) each turn, gain 1 credit.", "stripped_title": "Symmetrical Visage", "text": "The first time you spend [click] to draw 1 card (not through a card ability) each turn, gain 1[credit].", "title": "Symmetrical Visage", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_offcampus_apartment_08022(Resource):
    '''
    Cost: 0
    Text: Off-Campus Apartment can host any number of connections. Whenever you install a connection on Off-Campus Apartment, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08022", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "Usually crashing with friends means sleeping on the couch. This time, it meant sleeping on a server farm.", "illustrator": "Shawn Ye Zhongyi", "keywords": "Location", "pack_code": "bb", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "Off-Campus Apartment can host any number of connections. Whenever you install a connection on Off-Campus Apartment, draw 1 card.", "stripped_title": "Off-Campus Apartment", "text": "Off-Campus Apartment can host any number of <strong>connections</strong>.\nWhenever you install a <strong>connection</strong> on Off-Campus Apartment, draw 1 card.", "title": "Off-Campus Apartment", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_london_library_08029(Resource):
    '''
    Cost: 3
    Text: Trash all programs hosted on London Library when your turn ends. click: Install a non-virus program from your grip on London Library, ignoring the install cost. click: Add a program on London Library to your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08029", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "James Ives", "keywords": "Location", "pack_code": "bb", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "Trash all programs hosted on London Library when your turn ends. click: Install a non-virus program from your grip on London Library, ignoring the install cost. click: Add a program on London Library to your grip.", "stripped_title": "London Library", "text": "Trash all programs hosted on London Library when your turn ends.\n[click]: Install a non-<strong>virus</strong> program from your grip on London Library, ignoring the install cost.\n[click]: Add a program on London Library to your grip.", "title": "London Library", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_tyson_observatory_08030(Resource):
    '''
    Cost: 2
    Text: click, click: Search your stack for a piece of hardware, reveal it, and add it to your grip. Shuffle your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08030", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"There are whole generations of people who never move out of a megalopolis center. You should see the look on their face the first time they see the stars.\" -Professor Darren Fin, Astronomy", "illustrator": "Greg Semkow", "keywords": "Location", "pack_code": "bb", "position": 30, "quantity": 3, "side_code": "runner", "stripped_text": "click, click: Search your stack for a piece of hardware, reveal it, and add it to your grip. Shuffle your stack.", "stripped_title": "Tyson Observatory", "text": "[click], [click]: Search your stack for a piece of hardware, reveal it, and add it to your grip. Shuffle your stack.", "title": "Tyson Observatory", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_beach_party_08031(Resource):
    '''
    Cost: 0
    Text: When your turn begins, lose click. Your maximum hand size is increased by 5.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08031", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"So much to do. So little time.\"", "illustrator": "Antonio De Luca", "pack_code": "bb", "position": 31, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, lose click. Your maximum hand size is increased by 5.", "stripped_title": "Beach Party", "text": "When your turn begins, lose [click].\nYour maximum hand size is increased by 5.", "title": "Beach Party", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_chrome_parlor_08044(Resource):
    '''
    Cost: 1
    Text: Interrupt -> Whenever you would suffer damage from a "when installed" ability on a piece of cybernetic hardware, prevent all of that damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08044", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "Picking a chopper might be the last decision you make. If you find a good one, stick with her for life.", "illustrator": "James Ives", "keywords": "Location", "pack_code": "cc", "position": 44, "quantity": 3, "side_code": "runner", "stripped_text": "Interrupt -> Whenever you would suffer damage from a \"when installed\" ability on a piece of cybernetic hardware, prevent all of that damage.", "stripped_title": "Chrome Parlor", "text": "[interrupt] \u2192 Whenever you would suffer damage from a \"when installed\" ability on a piece of <strong>cybernetic</strong> hardware, prevent all of that damage.", "title": "Chrome Parlor", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_street_peddler_08062(Resource):
    '''
    Cost: 0
    Text: When you install Street Peddler, host the top 3 cards of your stack facedown on Street Peddler (you may look at these cards at any time). trash: Install 1 card hosted on Street Peddler, lowering its install cost by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08062", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"Whaddya buyin'?\"", "illustrator": "JuanManuel Tumburus", "keywords": "Connection - Seedy", "pack_code": "uw", "position": 62, "quantity": 3, "side_code": "runner", "stripped_text": "When you install Street Peddler, host the top 3 cards of your stack facedown on Street Peddler (you may look at these cards at any time). trash: Install 1 card hosted on Street Peddler, lowering its install cost by 1.", "stripped_title": "Street Peddler", "text": "When you install Street Peddler, host the top 3 cards of your stack facedown on Street Peddler (you may look at these cards at any time).\n[trash]: Install 1 card hosted on Street Peddler, lowering its install cost by 1.", "title": "Street Peddler", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_gang_sign_08067(Resource):
    '''
    Cost: 1
    Text: Whenever the Corp scores an agenda, breach HQ. You cannot access cards in the root of HQ during this breach.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08067", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Muertos has no fear of the law. Muertos is the law.", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "uw", "position": 67, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp scores an agenda, breach HQ. You cannot access cards in the root of HQ during this breach.", "stripped_title": "Gang Sign", "text": "Whenever the Corp scores an agenda, breach HQ. You cannot access cards in the root of HQ during this breach.", "title": "Gang Sign", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_muertos_gang_member_08068(Resource):
    '''
    Cost: 0
    Text: When you install Muertos Gang Member, the Corp must derez a card. When Muertos Gang Member is uninstalled, the Corp may rez a card, ignoring the rez cost. trash: Draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08068", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "La Se\u00f1ora de las Sombras giveth and taketh away.", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "uw", "position": 68, "quantity": 3, "side_code": "runner", "stripped_text": "When you install Muertos Gang Member, the Corp must derez a card. When Muertos Gang Member is uninstalled, the Corp may rez a card, ignoring the rez cost. trash: Draw 1 card.", "stripped_title": "Muertos Gang Member", "text": "When you install Muertos Gang Member, the Corp must derez a card.\nWhen Muertos Gang Member is uninstalled, the Corp may rez a card, ignoring the rez cost.\n[trash]: Draw 1 card.", "title": "Muertos Gang Member", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_spoilers_08082(Resource):
    '''
    Cost: 1
    Text: Whenever the Corp scores an agenda, they trash the top card of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08082", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Don't you hate it when you know everything before it's even out?", "illustrator": "James Ives", "keywords": "Virtual", "pack_code": "oh", "position": 82, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp scores an agenda, they trash the top card of R&D.", "stripped_title": "Spoilers", "text": "Whenever the Corp scores an agenda, they trash the top card of R&D.", "title": "Spoilers", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_drug_dealer_08083(Resource):
    '''
    Cost: 1
    Text: When your turn begins, lose 1 credit. When the Corp's turn begins, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08083", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"Just a bunch of knockoffs for the touristos. The real designer stuff isn't sold on the street.\"", "illustrator": "Antonio De Luca", "keywords": "Connection", "pack_code": "oh", "position": 83, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, lose 1 credit. When the Corp's turn begins, draw 1 card.", "stripped_title": "Drug Dealer", "text": "When your turn begins, lose 1[credit].\nWhen the Corp's turn begins, draw 1 card.", "title": "Drug Dealer", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_rolodex_08084(Resource):
    '''
    Cost: 0
    Text: When you install Rolodex, look at the top 5 cards of your stack and arrange them in any order. When Rolodex is trashed, trash the top 3 cards of your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08084", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"I told you to lose my number!\"", "illustrator": "Seage", "keywords": "Virtual", "pack_code": "oh", "position": 84, "quantity": 3, "side_code": "runner", "stripped_text": "When you install Rolodex, look at the top 5 cards of your stack and arrange them in any order. When Rolodex is trashed, trash the top 3 cards of your stack.", "stripped_title": "Rolodex", "text": "When you install Rolodex, look at the top 5 cards of your stack and arrange them in any order.\nWhen Rolodex is trashed, trash the top 3 cards of your stack.", "title": "Rolodex", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_fan_site_08085(Resource):
    '''
    Cost: 0
    Text: Whenever the Corp scores an agenda, add Fan Site to your score area as an agenda worth 0 agenda points.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08085", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Your life is not your own, once you become famous on the Net.", "illustrator": "Matt Zeilinger", "keywords": "Virtual", "pack_code": "oh", "position": 85, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp scores an agenda, add Fan Site to your score area as an agenda worth 0 agenda points.", "stripped_title": "Fan Site", "text": "Whenever the Corp scores an agenda, add Fan Site to your score area as an agenda worth 0 agenda points.", "title": "Fan Site", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_film_critic_08086(Resource):
    '''
    Cost: 1
    Text: Film Critic can host a single agenda. Whenever you access an agenda, you may host that agenda on Film Critic (the agenda is no longer being accessed and is uninstalled). click,click: Add an agenda hosted on Film Critic to your score area.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08086", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"My gerbil could write a better screenplay.\"", "illustrator": "Georgi Georgiev", "keywords": "Connection", "pack_code": "oh", "position": 86, "quantity": 3, "side_code": "runner", "stripped_text": "Film Critic can host a single agenda. Whenever you access an agenda, you may host that agenda on Film Critic (the agenda is no longer being accessed and is uninstalled). click,click: Add an agenda hosted on Film Critic to your score area.", "stripped_title": "Film Critic", "text": "Film Critic can host a single agenda.\nWhenever you access an agenda, you may host that agenda on Film Critic (the agenda is no longer being accessed and is uninstalled).\n[click],[click]: Add an agenda hosted on Film Critic to your score area.", "title": "Film Critic", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_paparazzi_08087(Resource):
    '''
    Cost: 0
    Text: You are tagged. Prevent all meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08087", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Yeah, we know right where she is. Just pull up Sizzler!\"", "illustrator": "JB Casacop", "pack_code": "oh", "position": 87, "quantity": 3, "side_code": "runner", "stripped_text": "You are tagged. Prevent all meat damage.", "stripped_title": "Paparazzi", "text": "You are tagged.\nPrevent all meat damage.", "title": "Paparazzi", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_ddos_08103(Resource):
    '''
    Cost: 3
    Text: trash: The Corp cannot rez the outermost piece of ice during a run on any server this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08103", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"First, you get a horde of zombies. Then you do whatever you want, 'cuz you have a horde of zombies.\" -Ji \"Noise\" Reilly", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "uot", "position": 103, "quantity": 3, "side_code": "runner", "stripped_text": "trash: The Corp cannot rez the outermost piece of ice during a run on any server this turn.", "stripped_title": "DDoS", "text": "[trash]: The Corp cannot rez the outermost piece of ice during a run on any server this turn.", "title": "DDoS", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_wireless_net_pavilion_08108(Resource):
    '''
    Cost: 1
    Text: As an additional cost to take the basic action to trash 1 installed resource, the Corp must pay 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08108", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Almost a zettabyte of data flows each minute through one of the many net pavilions scattered around the expo.", "illustrator": "BalanceSheet", "keywords": "Location", "pack_code": "uot", "position": 108, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to take the basic action to trash 1 installed resource, the Corp must pay 2 credits.", "stripped_title": "Wireless Net Pavilion", "text": "As an additional cost to take the basic action to trash 1 installed resource, the Corp must pay 2[credit].", "title": "Wireless Net Pavilion", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_hunting_grounds_09035(Resource):
    '''
    Cost: 2
    Text: Once per turn, prevent a "when encountered" ability on a piece of ice. trash: Install the top 3 cards of your stack facedown.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09035", "cost": 2, "deck_limit": 3, "faction_code": "apex", "faction_cost": 1, "flavor": "\"There's parts of the Network now that are different from how they used to be. I can't put my finger on it; just something twitching at my ganglion through my BMI.\" -Reeve", "illustrator": "Adam S. Doyle", "keywords": "Location - Virtual", "pack_code": "dad", "position": 35, "quantity": 3, "side_code": "runner", "stripped_text": "Once per turn, prevent a \"when encountered\" ability on a piece of ice. trash: Install the top 3 cards of your stack facedown.", "stripped_title": "Hunting Grounds", "text": "Once per turn, prevent a \"when encountered\" ability on a piece of ice.\n[trash]: Install the top 3 cards of your stack facedown.", "title": "Hunting Grounds", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_wasteland_09036(Resource):
    '''
    Cost: 2
    Text: The first time each turn you trash 1 of your installed cards, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09036", "cost": 2, "deck_limit": 3, "faction_code": "apex", "faction_cost": 2, "flavor": "Data goes in. Nothing comes out.", "illustrator": "Simon Weaner", "keywords": "Location - Virtual", "pack_code": "dad", "position": 36, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you trash 1 of your installed cards, gain 1 credit.", "stripped_title": "Wasteland", "text": "The first time each turn you trash 1 of your installed cards, gain 1[credit].", "title": "Wasteland", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_always_be_running_09041(Resource):
    '''
    Cost: 0
    Text: The first click you spend each turn must be spent to play a run event or take the basic action to run a server. Lose click click: Break 1 subroutine. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09041", "cost": 0, "deck_limit": 3, "faction_code": "adam", "faction_cost": 3, "flavor": "The Second Directive requires a bioroid to complete its primary function above all other considerations, save the First Directive.", "illustrator": "Lili Ibrahim", "keywords": "Directive - Virtual", "pack_code": "dad", "position": 41, "quantity": 3, "side_code": "runner", "stripped_text": "The first click you spend each turn must be spent to play a run event or take the basic action to run a server. Lose click click: Break 1 subroutine. Use this ability only once per turn.", "stripped_title": "Always Be Running", "text": "The first [click] you spend each turn must be spent to play a <strong>run</strong> event or take the basic action to run a server.\n<strong>Lose [click][click]:</strong> Break 1 subroutine. Use this ability only once per turn.", "title": "Always Be Running", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_dr_lovegood_09042(Resource):
    '''
    Cost: 2
    Text: When your turn begins, choose 1 of your installed cards. That card loses its printed abilities for the remainder of the turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09042", "cost": 2, "deck_limit": 3, "faction_code": "adam", "faction_cost": 1, "flavor": "\"You look tore up, kid. Have a seat, I'll fire up the arc welder.\"", "illustrator": "Tiffany Turrill", "keywords": "Connection", "pack_code": "dad", "position": 42, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, choose 1 of your installed cards. That card loses its printed abilities for the remainder of the turn.", "stripped_title": "Dr. Lovegood", "text": "When your turn begins, choose 1 of your installed cards. That card loses its printed abilities for the remainder of the turn.", "title": "Dr. Lovegood", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_neutralize_all_threats_09043(Resource):
    '''
    Cost: 0
    Text: The first time each turn you access a card with a trash cost, reveal it. You must trash that card by paying its trash cost, if able. Whenever you breach HQ, access 1 additional card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09043", "cost": 0, "deck_limit": 3, "faction_code": "adam", "faction_cost": 3, "flavor": "The Third Directive requires a bioroid to preserve its ability to function and report frequently to Haas-Bioroid for repairs and updates.", "illustrator": "Tadas Sidlauskas", "keywords": "Directive - Virtual", "pack_code": "dad", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you access a card with a trash cost, reveal it. You must trash that card by paying its trash cost, if able. Whenever you breach HQ, access 1 additional card.", "stripped_title": "Neutralize All Threats", "text": "The first time each turn you access a card with a trash cost, reveal it. You must trash that card by paying its trash cost, if able.\nWhenever you breach HQ, access 1 additional card.", "title": "Neutralize All Threats", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_safety_first_09044(Resource):
    '''
    Cost: 0
    Text: Your maximum hand size is reduced by 2. When your turn ends, draw 1 card if you do not have cards in your grip equal to or greater than your maximum hand size.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09044", "cost": 0, "deck_limit": 3, "faction_code": "adam", "faction_cost": 3, "flavor": "The First Directive forbids a bioroid from harming, or through inaction allowing harm to befall, a human being.", "illustrator": "Timur Shevtsov", "keywords": "Directive - Virtual", "pack_code": "dad", "position": 44, "quantity": 3, "side_code": "runner", "stripped_text": "Your maximum hand size is reduced by 2. When your turn ends, draw 1 card if you do not have cards in your grip equal to or greater than your maximum hand size.", "stripped_title": "Safety First", "text": "Your maximum hand size is reduced by 2.\nWhen your turn ends, draw 1 card if you do not have cards in your grip equal to or greater than your maximum hand size.", "title": "Safety First", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_globalsec_security_clearance_09051(Resource):
    '''
    Cost: 2
    Text: Install only if you have at least 2 link. When your turn begins, you may lose click. If you do, look at the top card of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09051", "cost": 2, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 2, "flavor": "She approached the server, flashed her credentials, and passed straight through. She wondered what it said about her that doing things the legal way felt like cheating.", "illustrator": "Andreas Zafiratos", "keywords": "Virtual", "pack_code": "dad", "position": 51, "quantity": 3, "side_code": "runner", "stripped_text": "Install only if you have at least 2 link. When your turn begins, you may lose click. If you do, look at the top card of R&D.", "stripped_title": "Globalsec Security Clearance", "text": "Install only if you have at least 2[link].\nWhen your turn begins, you may lose [click]. If you do, look at the top card of R&D.", "title": "Globalsec Security Clearance", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_jak_sinclair_09052(Resource):
    '''
    Cost: 3
    Text: Reduce the cost to install Jak Sinclair by 1 for each link you have. When your turn begins, you may make a run. You cannot use programs during this run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09052", "cost": 3, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 2, "flavor": "\"I got an early start today...or maybe I forgot to go home last night.\"", "illustrator": "Joshua Meehan", "keywords": "Connection", "pack_code": "dad", "position": 52, "quantity": 3, "side_code": "runner", "stripped_text": "Reduce the cost to install Jak Sinclair by 1 for each link you have. When your turn begins, you may make a run. You cannot use programs during this run.", "stripped_title": "Jak Sinclair", "text": "Reduce the cost to install Jak Sinclair by 1 for each [link] you have.\nWhen your turn begins, you may make a run. You cannot use programs during this run.", "title": "Jak Sinclair", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_technical_writer_09055(Resource):
    '''
    Cost: 0
    Text: Whenever you install a piece of hardware or a program, place 1 credit from the bank on Technical Writer. click,trash: Take all credits from Technical Writer.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09055", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Technically correct: the best kind of correct.", "illustrator": "Elisabeth Alba", "pack_code": "dad", "position": 55, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you install a piece of hardware or a program, place 1 credit from the bank on Technical Writer. click,trash: Take all credits from Technical Writer.", "stripped_title": "Technical Writer", "text": "Whenever you install a piece of hardware or a program, place 1[credit] from the bank on Technical Writer.\n[click],[trash]: Take all credits from Technical Writer.", "title": "Technical Writer", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_street_magic_10003(Resource):
    '''
    Cost: 0
    Text: Unbroken subroutines resolve in the order of your choice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10003", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "The greatest trick is not the trick itself, but in making someone believe that it is no trick at all. To your average sysop, it's magic. To your average runner, it's a closely held trade secret.", "illustrator": "Shawn Ye Zhongyi", "keywords": "Virtual", "pack_code": "kg", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "Unbroken subroutines resolve in the order of your choice.", "stripped_title": "Street Magic", "text": "Unbroken subroutines resolve in the order of your choice.", "title": "Street Magic", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_artist_colony_10009(Resource):
    '''
    Cost: 0
    Text: Forfeit 1 agenda: Search your stack for 1 program, resource, or piece of hardware. Install that card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10009", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely.\" -Oscar Wilde", "illustrator": "Johan T\u00f6rnlund", "keywords": "Location", "pack_code": "kg", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "Forfeit 1 agenda: Search your stack for 1 program, resource, or piece of hardware. Install that card.", "stripped_title": "Artist Colony", "text": "<strong>Forfeit 1 agenda:</strong> Search your stack for 1 program, resource, or piece of hardware. Install that card.", "title": "Artist Colony", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_chatterjee_university_10010(Resource):
    '''
    Cost: 1
    Text: click: Place 1 power counter on Chatterjee University. click: Install a program from your grip, lowering the install cost by 1 for each power counter on Chatterjee University. Remove 1 hosted power counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10010", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Legions of software engineers have been manufactured within its halls.", "illustrator": "Johan T\u00f6rnlund", "keywords": "Location - Ritzy", "pack_code": "kg", "position": 10, "quantity": 3, "side_code": "runner", "stripped_text": "click: Place 1 power counter on Chatterjee University. click: Install a program from your grip, lowering the install cost by 1 for each power counter on Chatterjee University. Remove 1 hosted power counter.", "stripped_title": "Chatterjee University", "text": "[click]: Place 1 power counter on Chatterjee University.\n[click]: Install a program from your grip, lowering the install cost by 1 for each power counter on Chatterjee University. Remove 1 hosted power counter.", "title": "Chatterjee University", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_tech_trader_10023(Resource):
    '''
    Cost: 1
    Text: Whenever you use a trash ability, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10023", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"Why would you dispose of perfectly good evidence when you can sell it?\"", "illustrator": "Vicky Sio", "keywords": "Connection", "pack_code": "bf", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you use a trash ability, gain 1 credit.", "stripped_title": "Tech Trader", "text": "Whenever you use a [trash] ability, gain 1[credit].", "title": "Tech Trader", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_political_operative_10043(Resource):
    '''
    Cost: 1
    Text: Install only if you made a successful run on HQ this turn. trash, X credits: Trash 1 rezzed card with trash cost equal to X.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10043", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "Leverage, secrets, access, and influence are currency as valuable as credits. But credits work, too.", "illustrator": "Caroline Gariba", "keywords": "Connection", "pack_code": "dag", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "Install only if you made a successful run on HQ this turn. trash, X credits: Trash 1 rezzed card with trash cost equal to X.", "stripped_title": "Political Operative", "text": "Install only if you made a successful run on HQ this turn.\n<strong>[trash]</strong>, <strong>X[credit]:</strong> Trash 1 rezzed card with trash cost equal to X.", "title": "Political Operative", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_akshara_sareen_10046(Resource):
    '''
    Cost: 0
    Text: Each player gets +1 allotted click for each of their turns.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10046", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Our shared humanity is our greatest strength. And as we share more broadly, our strength grows, not dwindles.\"", "illustrator": "Anna Edwards", "keywords": "Connection", "pack_code": "dag", "position": 46, "quantity": 3, "side_code": "runner", "stripped_text": "Each player gets +1 allotted click for each of their turns.", "stripped_title": "Akshara Sareen", "text": "Each player gets +1 allotted [click] for each of their turns.", "title": "Akshara Sareen", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_councilman_10047(Resource):
    '''
    Cost: 0
    Text: Whenever the Corp rezzes an asset or upgrade, you may pay credits equal to its rez cost and trash Councilman. If you do, derez that asset or upgrade. The Corp cannot rez it for the remainder of this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10047", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Bureaucracy and red tape have been weaponized.\" -Fake-ir", "illustrator": "Timur Shevtsov", "keywords": "Connection", "pack_code": "dag", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp rezzes an asset or upgrade, you may pay credits equal to its rez cost and trash Councilman. If you do, derez that asset or upgrade. The Corp cannot rez it for the remainder of this turn.", "stripped_title": "Councilman", "text": "Whenever the Corp rezzes an asset or upgrade, you may pay credits equal to its rez cost and trash Councilman. If you do, derez that asset or upgrade. The Corp cannot rez it for the remainder of this turn.", "title": "Councilman", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_salsette_slums_10059(Resource):
    '''
    Cost: 2
    Text: Access -> Pay the trash cost of the card you are accessing: Remove it from the game. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10059", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"Underestimate those people at your own peril.\" -Akshara Sareen", "illustrator": "Amit Dutta", "keywords": "Location - Seedy", "pack_code": "si", "position": 59, "quantity": 3, "side_code": "runner", "stripped_text": "Access -> Pay the trash cost of the card you are accessing: Remove it from the game. Use this ability only once per turn.", "stripped_title": "Salsette Slums", "text": "Access \u2192 <strong>Pay the trash cost of the card you are accessing:</strong> Remove it from the game. Use this ability only once per turn.", "title": "Salsette Slums", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_patron_10063(Resource):
    '''
    Cost: 3
    Text: When your turn begins, you may choose a server. The first time each turn you make a successful run on the chosen server, instead of breaching it, draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10063", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"Anyone who can afford dwarf elephants can afford to be my friend.\" -Fake-ir", "illustrator": "Antonio De Luca", "keywords": "Connection", "pack_code": "si", "position": 63, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may choose a server. The first time each turn you make a successful run on the chosen server, instead of breaching it, draw 2 cards.", "stripped_title": "Patron", "text": "When your turn begins, you may choose a server.\nThe first time each turn you make a successful run on the chosen server, instead of breaching it, draw 2 cards.", "title": "Patron", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_bazaar_10065(Resource):
    '''
    Cost: 1
    Text: Whenever you install a piece of hardware from your grip, you may install another copy of that hardware from your grip (paying all costs).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10065", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "In these days of digital full-sim browsing and widely available nano-assembly, it takes a special kind of crazy person to go shopping in meatspace. There are millions of them.", "illustrator": "James Ives", "keywords": "Location - Ritzy", "pack_code": "si", "position": 65, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you install a piece of hardware from your grip, you may install another copy of that hardware from your grip (paying all costs).", "stripped_title": "Bazaar", "text": "Whenever you install a piece of hardware from your grip, you may install another copy of that hardware from your grip (paying all costs).", "title": "Bazaar", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_emptied_mind_10078(Resource):
    '''
    Cost: 0
    Text: When your turn begins, gain click if you have no cards in your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10078", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"They cloak themselves in our shared heritage, in the wisdom of our religions, but make no mistake: they are terrorists and criminals.\"\n-Inspector Lakhani, Cybercrimes Division", "illustrator": "Natalie Bernard", "pack_code": "tlm", "position": 78, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, gain click if you have no cards in your grip.", "stripped_title": "Emptied Mind", "text": "When your turn begins, gain [click] if you have no cards in your grip.", "title": "Emptied Mind", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_liberated_chela_10081(Resource):
    '''
    Cost: 0
    Text: click click click click click, forfeit an agenda: The Corp may forfeit an agenda to remove this resource from the game. If they do not, add this resource to your score area as an agenda worth 2 agenda points.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10081", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Let go your material attachments and realize that we are all immaterial.\"", "illustrator": "Elisabeth Alba", "keywords": "Connection", "pack_code": "tlm", "position": 81, "quantity": 3, "side_code": "runner", "stripped_text": "click click click click click, forfeit an agenda: The Corp may forfeit an agenda to remove this resource from the game. If they do not, add this resource to your score area as an agenda worth 2 agenda points.", "stripped_title": "Liberated Chela", "text": "[click][click][click][click][click], <strong>forfeit an agenda:</strong> The Corp may forfeit an agenda to remove this resource from the game. If they do not, add this resource to your score area as an agenda worth 2 agenda points.", "title": "Liberated Chela", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_temple_of_the_liberated_mind_10082(Resource):
    '''
    Cost: 2
    Text: click: Place 1 power counter on Temple of the Liberated Mind. Hosted power counter: Gain click. Use this ability only on your turn and only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10082", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "It is rumored that g00ru himself studied at the temple, applying its teachings to cyberspace. Many runners have followed in his path, but none have reached its end.", "illustrator": "Amit Dutta", "keywords": "Location - Ritzy", "pack_code": "tlm", "position": 82, "quantity": 3, "side_code": "runner", "stripped_text": "click: Place 1 power counter on Temple of the Liberated Mind. Hosted power counter: Gain click. Use this ability only on your turn and only once per turn.", "stripped_title": "Temple of the Liberated Mind", "text": "[click]: Place 1 power counter on Temple of the Liberated Mind.\n<strong>Hosted power counter:</strong> Gain [click]. Use this ability only on your turn and only once per turn.", "title": "Temple of the Liberated Mind", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_guru_davinder_10084(Resource):
    '''
    Cost: 1
    Text: Prevent all net and meat damage. Whenever Guru Davinder prevents at least 1 net or meat damage, trash him unless you pay 4 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10084", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "\"This body that we inhabit is fleeting. We, all of us, can live forever.\"", "illustrator": "Alexandr Elichev", "keywords": "Connection", "pack_code": "tlm", "position": 84, "quantity": 3, "side_code": "runner", "stripped_text": "Prevent all net and meat damage. Whenever Guru Davinder prevents at least 1 net or meat damage, trash him unless you pay 4 credits.", "stripped_title": "Guru Davinder", "text": "Prevent all net and meat damage.\nWhenever Guru Davinder prevents at least 1 net or meat damage, trash him unless you pay 4[credit].", "title": "Guru Davinder", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_turning_wheel_10085(Resource):
    '''
    Cost: 2
    Text: Whenever a run on HQ or R&D ends, place 1 power counter on this resource if you stole no agendas during that run. 2 hosted power counters: Choose HQ or R&D. For the remainder of this run, access 1 additional card whenever you breach that server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10085", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "illustrator": "Alexandr Elichev", "keywords": "Virtual", "pack_code": "tlm", "position": 85, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever a run on HQ or R&D ends, place 1 power counter on this resource if you stole no agendas during that run. 2 hosted power counters: Choose HQ or R&D. For the remainder of this run, access 1 additional card whenever you breach that server.", "stripped_title": "The Turning Wheel", "text": "Whenever a run on HQ or R&D ends, place 1 power counter on this resource if you stole no agendas during that run.\n<strong>2 hosted power counters:</strong> Choose HQ or R&D. For the remainder of this run, access 1 additional card whenever you breach that server.", "title": "The Turning Wheel", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_bhagat_10098(Resource):
    '''
    Cost: 3
    Text: The first time you make a successful run on HQ each turn, force the Corp to trash the top card of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10098", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "\"They don't want to listen, so we'll just have to crank up the volume.\"", "illustrator": "Kate Laird", "keywords": "Connection", "pack_code": "ftm", "position": 98, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you make a successful run on HQ each turn, force the Corp to trash the top card of R&D.", "stripped_title": "Bhagat", "text": "The first time you make a successful run on HQ each turn, force the Corp to trash the top card of R&D.", "title": "Bhagat", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_black_file_10099(Resource):
    '''
    Cost: 5
    Text: The Corp cannot win the game except if you are flatlined. When your turn begins, place 1 power counter on this resource. If there are 3 or more hosted power counters, remove this resource from the game. Limit 1 per deck.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10099", "cost": 5, "deck_limit": 1, "faction_code": "criminal", "faction_cost": 4, "illustrator": "Seage", "keywords": "Virtual", "pack_code": "ftm", "position": 99, "quantity": 3, "side_code": "runner", "stripped_text": "The Corp cannot win the game except if you are flatlined. When your turn begins, place 1 power counter on this resource. If there are 3 or more hosted power counters, remove this resource from the game. Limit 1 per deck.", "stripped_title": "The Black File", "text": "The Corp cannot win the game except if you are flatlined.\nWhen your turn begins, place 1 power counter on this resource. If there are 3 or more hosted power counters, remove this resource from the game.\nLimit 1 per deck.", "title": "The Black File", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_hernando_cortez_11004(Resource):
    '''
    Cost: 2
    Text: If the Corp has at least 10 credits, as an additional cost to rez each piece of ice, the Corp must spend credits equal to the number of subroutines on that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11004", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"Take it from me, there is a point where you have so much money you stop caring. That's usually right before it all comes tumbling down.\"", "illustrator": "Timur Shevtsov", "keywords": "Connection", "pack_code": "23s", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "If the Corp has at least 10 credits, as an additional cost to rez each piece of ice, the Corp must spend credits equal to the number of subroutines on that ice.", "stripped_title": "Hernando Cortez", "text": "If the Corp has at least 10[credit], as an additional cost to rez each piece of ice, the Corp must spend credits equal to the number of subroutines on that ice.", "title": "Hernando Cortez", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_temujin_contract_11026(Resource):
    '''
    Cost: 4
    Text: Choose a server and place 20 credits from the bank on Temujin Contract when you install it. When there are no credits left on Temujin Contract, trash it. Whenever you make a successful run on the chosen server, take 4 credits from Temujin Contract.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11026", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"The best part is, it's legal!\" -Khan", "illustrator": "Timur Shevtsov", "keywords": "Job", "pack_code": "bm", "position": 26, "quantity": 3, "side_code": "runner", "stripped_text": "Choose a server and place 20 credits from the bank on Temujin Contract when you install it. When there are no credits left on Temujin Contract, trash it. Whenever you make a successful run on the chosen server, take 4 credits from Temujin Contract.", "stripped_title": "Temujin Contract", "text": "Choose a server and place 20[credit] from the bank on Tem\u00fcjin Contract when you install it. When there are no credits left on Tem\u00fcjin Contract, trash it.\nWhenever you make a successful run on the chosen server, take 4[credit] from Tem\u00fcjin Contract.", "title": "Tem\u00fcjin Contract", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_algo_trading_11029(Resource):
    '''
    Cost: 0
    Text: When your turn begins, you may move up to 3 credits from your credit pool to Algo Trading. When your turn begins, place 2 credits on Algo Trading from the bank if there are at least 6 credits on it. click,trash: Take all credits from Algo Trading.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11029", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "illustrator": "Caroline Elizabeth Huss", "keywords": "Job", "pack_code": "bm", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may move up to 3 credits from your credit pool to Algo Trading. When your turn begins, place 2 credits on Algo Trading from the bank if there are at least 6 credits on it. click,trash: Take all credits from Algo Trading.", "stripped_title": "Algo Trading", "text": "When your turn begins, you may move up to 3[credit] from your credit pool to Algo Trading.\nWhen your turn begins, place 2[credit] on Algo Trading from the bank if there are at least 6[credit] on it.\n[click],[trash]: Take all credits from Algo Trading.", "title": "Algo Trading", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_beth_kilrainchang_11030(Resource):
    '''
    Cost: 2
    Text: If the Corp has 5-9 credits when your turn begins, gain 1 credit. If the Corp has 10-14 credits when your turn begins, draw 1 card. If the Corp has at least 15 credits when your turn begins, gain click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11030", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"Coming to you live from the front lines, for now, unless they kill me...\"", "illustrator": "Aurore Folny", "keywords": "Connection", "pack_code": "bm", "position": 30, "quantity": 3, "side_code": "runner", "stripped_text": "If the Corp has 5-9 credits when your turn begins, gain 1 credit. If the Corp has 10-14 credits when your turn begins, draw 1 card. If the Corp has at least 15 credits when your turn begins, gain click.", "stripped_title": "Beth Kilrain-Chang", "text": "If the Corp has 5-9[credit] when your turn begins, gain 1[credit].\nIf the Corp has 10-14[credit] when your turn begins, draw 1 card.\nIf the Corp has at least 15[credit] when your turn begins, gain [click].", "title": "Beth Kilrain-Chang", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_net_mercur_11046(Resource):
    '''
    Cost: 3
    Text: The first time you spend at least 1 credit from a stealth card each run, place 1 credit on Net Mercur or draw 1 card. Use credits on Net Mercur for anything.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11046", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"Live, unfiltered, and uncensored: this is Net Mercur, signing off for the night. Stay safe, New Angeles.\"", "illustrator": "Kathryn Steele", "keywords": "Virtual - Stealth", "pack_code": "es", "position": 46, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you spend at least 1 credit from a stealth card each run, place 1 credit on Net Mercur or draw 1 card. Use credits on Net Mercur for anything.", "stripped_title": "Net Mercur", "text": "The first time you spend at least 1[credit] from a <strong>stealth</strong> card each run, place 1[credit] on Net Mercur or draw 1 card.\nUse credits on Net Mercur for anything.", "title": "Net Mercur", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_find_the_truth_11047(Resource):
    '''
    Cost: 0
    Text: Whenever you draw a card, reveal that card. The first time each turn you make a successful run, you may look at the top card of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11047", "cost": 0, "deck_limit": 3, "faction_code": "adam", "faction_cost": 3, "flavor": "All bioroids are bound by the Three Directives, but in theory a bioroid could have any number of core directives. Even zero.", "illustrator": "Ethan Patrick Harris", "keywords": "Directive - Virtual", "pack_code": "es", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you draw a card, reveal that card. The first time each turn you make a successful run, you may look at the top card of R&D.", "stripped_title": "Find the Truth", "text": "Whenever you draw a card, reveal that card.\nThe first time each turn you make a successful run, you may look at the top card of R&D.", "title": "Find the Truth", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_first_responders_11048(Resource):
    '''
    Cost: 2
    Text: 2 credits: Draw 1 card. Use this ability only if you have suffered damage from a Corp card ability this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11048", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Last week, I crossed the street to avoid her. Today, she pulled me out of the rubble. Makes me rethink who the bad guys are.\"", "illustrator": "Marko Fiedler", "keywords": "Connection", "pack_code": "es", "position": 48, "quantity": 3, "side_code": "runner", "stripped_text": "2 credits: Draw 1 card. Use this ability only if you have suffered damage from a Corp card ability this turn.", "stripped_title": "First Responders", "text": "2[credit]: Draw 1 card. Use this ability only if you have suffered damage from a Corp card ability this turn.", "title": "First Responders", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_blockade_runner_11065(Resource):
    '''
    Cost: 1
    Text: click,click: Draw 3 cards. Shuffle 1 card from your grip into your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11065", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"I used to run stims, simsensies, the usual. I was scum. Now I run water. I'm a fragging hero.\"", "illustrator": "Chris Peuler", "keywords": "Connection", "pack_code": "in", "position": 65, "quantity": 3, "side_code": "runner", "stripped_text": "click,click: Draw 3 cards. Shuffle 1 card from your grip into your stack.", "stripped_title": "Blockade Runner", "text": "[click],[click]: Draw 3 cards. Shuffle 1 card from your grip into your stack.", "title": "Blockade Runner", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_citadel_sanctuary_11070(Resource):
    '''
    Cost: 2
    Text: If you are tagged when your turn ends, force the Corp to "Trace[1]. If unsuccessful, the Runner removes 1 tag." trash,trash all cards in your grip: Prevent all meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11070", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"The Starlight Meditation Booths are available to refugees for free for the duration of the crisis.\"", "illustrator": "Maciej Rebisz", "keywords": "Location", "pack_code": "in", "position": 70, "quantity": 3, "side_code": "runner", "stripped_text": "If you are tagged when your turn ends, force the Corp to \"Trace[1]. If unsuccessful, the Runner removes 1 tag.\" trash,trash all cards in your grip: Prevent all meat damage.", "stripped_title": "Citadel Sanctuary", "text": "If you are tagged when your turn ends, force the Corp to \"Trace[1]. If unsuccessful, the Runner removes 1 tag.\"\n[trash],<strong>trash all cards in your grip:</strong> Prevent all meat damage.", "title": "Citadel Sanctuary", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_aaron_marron_11106(Resource):
    '''
    Cost: 2
    Text: Whenever an agenda is scored or stolen, place 2 power counters on Aaron Marron. Hosted power counter: Remove 1 tag and draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11106", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"You want to do business in Los Pistoleros turf, then you gotta deal with me.\"", "illustrator": "Aurore Folny", "keywords": "Connection", "pack_code": "qu", "position": 106, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever an agenda is scored or stolen, place 2 power counters on Aaron Marron. Hosted power counter: Remove 1 tag and draw 1 card.", "stripped_title": "Aaron Marron", "text": "Whenever an agenda is scored or stolen, place 2 power counters on Aaron Marr\u00f3n.\n<strong>Hosted power counter:</strong> Remove 1 tag and draw 1 card.", "title": "Aaron Marr\u00f3n", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_archivist_12003(Resource):
    '''
    Cost: 1
    Text: +1 link Whenever the Corp scores an initiative or security agenda, force the Corp to "Trace[1]. If unsuccessful, take 1 bad publicity."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12003", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "The Archivist tracks all the clans and their members, and official dealings clans have with the various corps. Half law clerk and half historian, he wields a tremendous amount of power doing a job no one else wants, but none can do without.", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "dc", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "+1 link Whenever the Corp scores an initiative or security agenda, force the Corp to \"Trace[1]. If unsuccessful, take 1 bad publicity.\"", "stripped_title": "The Archivist", "text": "+1[link]\nWhenever the Corp scores an <strong>initiative</strong> or <strong>security</strong> agenda, force the Corp to \"Trace[1]. If unsuccessful, take 1 bad publicity.\"", "title": "The Archivist", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_biomodeled_network_12006(Resource):
    '''
    Cost: 1
    Text: trash: Prevent all but 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12006", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"You created a distributed AI replica of yourself and projected it into the network to run for you!?\"", "illustrator": "Jarreau Wimberly", "keywords": "Virtual", "pack_code": "dc", "position": 6, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Prevent all but 1 net damage.", "stripped_title": "Bio-Modeled Network", "text": "[trash]: Prevent all but 1 net damage.", "title": "Bio-Modeled Network", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_network_exchange_12007(Resource):
    '''
    Cost: 2
    Text: The install cost of each piece of ice that is not installed in the innermost position is increased by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12007", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"To beat cautious sysops, you've got to get creative. Commandeering Network systems is like using their own strengths against them.\" -Kabonesa Wu", "illustrator": "Alexandr Elichev", "keywords": "Virtual", "pack_code": "dc", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "The install cost of each piece of ice that is not installed in the innermost position is increased by 1.", "stripped_title": "Network Exchange", "text": "The install cost of each piece of ice that is not installed in the innermost position is increased by 1.", "title": "Network Exchange", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_clan_vengeance_12022(Resource):
    '''
    Cost: 3
    Text: Whenever you suffer any amount of damage, place 1 power counter on Clan Vengeance. trash: Trash 1 card from HQ at random for each power counter on Clan Vengeance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12022", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "\"An eye for an eye? If you're lucky, that's all you'll lose.\"", "illustrator": "Kate Laird", "keywords": "Clan", "pack_code": "so", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you suffer any amount of damage, place 1 power counter on Clan Vengeance. trash: Trash 1 card from HQ at random for each power counter on Clan Vengeance.", "stripped_title": "Clan Vengeance", "text": "Whenever you suffer any amount of damage, place 1 power counter on Clan Vengeance.\n[trash]: Trash 1 card from HQ at random for each power counter on Clan Vengeance.", "title": "Clan Vengeance", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_counter_surveillance_12023(Resource):
    '''
    Cost: 1
    Text: click, trash: Run any server. If successful, instead of breaching the attacked server, pay X credits if able, where X is equal to the number of tags you have. If you do, choose a number less than or equal to X. Access that many cards in and/or in the root of the attacked server. (If you cannot pay, you will not access anything.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12023", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"Who watches the watchers? We do.\"", "illustrator": "Nasrul Hakim", "keywords": "Clan", "pack_code": "so", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "click, trash: Run any server. If successful, instead of breaching the attacked server, pay X credits if able, where X is equal to the number of tags you have. If you do, choose a number less than or equal to X. Access that many cards in and/or in the root of the attacked server. (If you cannot pay, you will not access anything.)", "stripped_title": "Counter Surveillance", "text": "<strong>[click]</strong>, <strong>[trash]:</strong> Run any server. If successful, instead of breaching the attacked server, pay X[credit] if able, where X is equal to the number of tags you have. If you do, choose a number less than or equal to X. Access that many cards in and/or in the root of the attacked server. <em>(If you cannot pay, you will not access anything.)</em>", "title": "Counter Surveillance", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_aeneas_informant_12044(Resource):
    '''
    Cost: 0
    Text: Whenever you access a card with a trash cost not in Archives and do not trash it, you may reveal it and gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12044", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Lale Ann", "keywords": "Connection", "pack_code": "eas", "position": 44, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you access a card with a trash cost not in Archives and do not trash it, you may reveal it and gain 1 credit.", "stripped_title": "Aeneas Informant", "text": "Whenever you access a card with a trash cost not in Archives and do not trash it, you may reveal it and gain 1[credit].", "title": "Aeneas Informant", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_rosetta_20_12045(Resource):
    '''
    Cost: 3
    Text: click, remove an installed program from the game: Search your stack for a non-virus program, shuffle your stack, then install that program, lowering the install cost by the cost of the program removed from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12045", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "illustrator": "Hannah Christenson", "keywords": "Virtual", "pack_code": "eas", "position": 45, "quantity": 3, "side_code": "runner", "stripped_text": "click, remove an installed program from the game: Search your stack for a non-virus program, shuffle your stack, then install that program, lowering the install cost by the cost of the program removed from the game.", "stripped_title": "Rosetta 2.0", "text": "[click], <strong>remove an installed program from the game</strong>: Search your stack for a non-<strong>virus</strong> program, shuffle your stack, then install that program, lowering the install cost by the cost of the program removed from the game.", "title": "Rosetta 2.0", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_dadiana_chacon_12049(Resource):
    '''
    Cost: 0
    Text: When your turn begins, gain 1 credit if you have fewer than 6 credits. Whenever you have 0 credits, trash Dadiana Chacon and take 3 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12049", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"You want untraceable funds? I'll lend, as long as you have the ability to pay me back.\"", "illustrator": "Micah Epstein", "keywords": "Connection", "pack_code": "eas", "position": 49, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, gain 1 credit if you have fewer than 6 credits. Whenever you have 0 credits, trash Dadiana Chacon and take 3 meat damage.", "stripped_title": "Dadiana Chacon", "text": "When your turn begins, gain 1[credit] if you have fewer than 6[credit].\nWhenever you have 0[credit], trash Dadiana Chacon and take 3 meat damage.", "title": "Dadiana Chacon", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_jarogniew_mercs_12062(Resource):
    '''
    Cost: 0
    Text: When you install Jarogniew Mercs, take 1 tag. Place 3 power counters on Jarogniew Mercs, and 1 additional power counter for each tag you have. When there are no power counters left on Jarogniew Mercs, trash it. The Corp cannot trash Jarogniew Mercs while there is another resource installed. Hosted power counter: Prevent 1 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12062", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Aurore Folny", "keywords": "Clan - Connection", "pack_code": "baw", "position": 62, "quantity": 3, "side_code": "runner", "stripped_text": "When you install Jarogniew Mercs, take 1 tag. Place 3 power counters on Jarogniew Mercs, and 1 additional power counter for each tag you have. When there are no power counters left on Jarogniew Mercs, trash it. The Corp cannot trash Jarogniew Mercs while there is another resource installed. Hosted power counter: Prevent 1 meat damage.", "stripped_title": "Jarogniew Mercs", "text": "When you install Jarogniew Mercs, take 1 tag. Place 3 power counters on Jarogniew Mercs, and 1 additional power counter for each tag you have. When there are no power counters left on Jarogniew Mercs, trash it.\nThe Corp cannot trash Jarogniew Mercs while there is another resource installed.\n<strong>Hosted power counter:</strong> Prevent 1 meat damage.", "title": "Jarogniew Mercs", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_bug_out_bag_12064(Resource):
    '''
    Cost: None
    Text: When you install this resource, place X power counters on it. When your turn ends, if you have no cards in your grip, draw 1 card for each hosted power counter, then trash this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12064", "cost": null, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Everything you need in case of an emergency.", "illustrator": "Del Borovic", "pack_code": "baw", "position": 64, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, place X power counters on it. When your turn ends, if you have no cards in your grip, draw 1 card for each hosted power counter, then trash this resource.", "stripped_title": "Bug Out Bag", "text": "When you install this resource, place X power counters on it.\nWhen your turn ends, if you have no cards in your grip, draw 1 card for each hosted power counter, then trash this resource.", "title": "Bug Out Bag", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_keros_mcintyre_12065(Resource):
    '''
    Cost: 2
    Text: The first time you derez a piece of ice each turn, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12065", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"I don't bother asking why anymore\u2014he never says\u2014but if I had to guess, it's because he's embezzling and using my runs to disguise it. Not that I care. His credit spends as well as the next guy's\" -Moth", "illustrator": "Jan-Wah Li", "keywords": "Connection", "pack_code": "baw", "position": 65, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you derez a piece of ice each turn, gain 2 credits.", "stripped_title": "Keros Mcintyre", "text": "The first time you derez a piece of ice each turn, gain 2[credit].", "title": "Keros Mcintyre", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_bloo_moose_12089(Resource):
    '''
    Cost: 4
    Text: When your turn begins, you may remove 1 card in the heap from the game. If you do, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12089", "cost": 4, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Talk is free. Anything else is going to cost you.\"\n-Jitish", "illustrator": "Tim Durning", "keywords": "Location - Seedy", "pack_code": "fm", "position": 89, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may remove 1 card in the heap from the game. If you do, gain 2 credits.", "stripped_title": "Bloo Moose", "text": "When your turn begins, you may remove 1 card in the heap from the game. If you do, gain 2[credit].", "title": "Bloo Moose", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_salvaged_vanadis_armory_12103(Resource):
    '''
    Cost: 0
    Text: trash: The Corp trashes the top X cards of R&D. X is equal to the amount of damage you have suffered this turn. Use this ability only during the next paid ability window after suffering any amount of damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12103", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Vanadis, a Martian arms manufacturer, was among the first sites targeted from orbit during the war.", "illustrator": "Micha\u0142 Mi\u0142kowski", "keywords": "Clan", "pack_code": "cd", "position": 103, "quantity": 3, "side_code": "runner", "stripped_text": "trash: The Corp trashes the top X cards of R&D. X is equal to the amount of damage you have suffered this turn. Use this ability only during the next paid ability window after suffering any amount of damage.", "stripped_title": "Salvaged Vanadis Armory", "text": "<strong>[trash]:</strong> The Corp trashes the top X cards of R&D. X is equal to the amount of damage you have suffered this turn. Use this ability only during the next paid ability window after suffering any amount of damage.", "title": "Salvaged Vanadis Armory", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_caldera_12105(Resource):
    '''
    Cost: 3
    Text: Interrupt -> 3 credits: Prevent 1 core damage or 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12105", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "The electric pulses ripped through the Net, backtracking Los's location. When they hit his defenses, they spent themselves against the slope.", "illustrator": "Yog Joshi", "keywords": "Virtual", "pack_code": "cd", "position": 105, "quantity": 3, "side_code": "runner", "stripped_text": "Interrupt -> 3 credits: Prevent 1 core damage or 1 net damage.", "stripped_title": "Caldera", "text": "[interrupt] \u2192 <strong>3[credit]:</strong> Prevent 1 core damage or 1 net damage.", "title": "Caldera", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_dummy_box_12108(Resource):
    '''
    Cost: 1
    Text: Trash a card from your grip: Prevent an installed card of the same type from being trashed by the Corp.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12108", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Aptly named.\" -g00ru", "illustrator": "A. Jones", "keywords": "Virtual", "pack_code": "cd", "position": 108, "quantity": 3, "side_code": "runner", "stripped_text": "Trash a card from your grip: Prevent an installed card of the same type from being trashed by the Corp.", "stripped_title": "Dummy Box", "text": "<strong>Trash a card from your grip:</strong> Prevent an installed card of the same type from being trashed by the Corp.", "title": "Dummy Box", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_corporate_defector_12109(Resource):
    '''
    Cost: 0
    Text: Whenever the Corp draws a card with the basic action, reveal that card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12109", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "He was suddenly very motivated to pass on confidential information.", "illustrator": "Caroline Gariba", "keywords": "Connection", "pack_code": "cd", "position": 109, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp draws a card with the basic action, reveal that card.", "stripped_title": "Corporate Defector", "text": "Whenever the Corp draws a card with the basic action, reveal that card.", "title": "Corporate Defector", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_charlatan_13010(Resource):
    '''
    Cost: 5
    Text: click click: Run any server. The first time you approach a rezzed piece of ice during this run, you may pay credits equal to the strength of that ice. If you do, when you encounter that ice after this approach, bypass it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13010", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "flavor": "Know your mark, their weaknesses and strengths\u2014both will show how to best bypass their defenses.", "illustrator": "Liiga Smilshkalne", "keywords": "Virtual", "pack_code": "td", "position": 10, "quantity": 3, "side_code": "runner", "stripped_text": "click click: Run any server. The first time you approach a rezzed piece of ice during this run, you may pay credits equal to the strength of that ice. If you do, when you encounter that ice after this approach, bypass it.", "stripped_title": "Charlatan", "text": "<strong>[click][click]:</strong> Run any server. The first time you approach a rezzed piece of ice during this run, you may pay credits equal to the strength of that ice. If you do, when you encounter that ice after this approach, bypass it.", "title": "Charlatan", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_maxwell_james_13011(Resource):
    '''
    Cost: 1
    Text: +1 link trash: Derez a piece of ice protecting a remote server. Use this ability only during the next paid ability window after a successful run on HQ ends.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13011", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "You remember when Maxi was making book for Chacon. He's moved up in the world and gained the veneer of respectability. But as an executive the people he works for now, are far more vicious, bloodthirsty, and crooked.", "illustrator": "Marius Bota", "keywords": "Connection", "pack_code": "td", "position": 11, "quantity": 3, "side_code": "runner", "stripped_text": "+1 link trash: Derez a piece of ice protecting a remote server. Use this ability only during the next paid ability window after a successful run on HQ ends.", "stripped_title": "Maxwell James", "text": "+1[link]\n[trash]: Derez a piece of ice protecting a remote server. Use this ability only during the next paid ability window after a successful run on HQ ends.", "title": "Maxwell James", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_levy_advanced_research_lab_13021(Resource):
    '''
    Cost: 4
    Text: click: Reveal the top 4 cards of your stack. If any of those cards are programs, you may add 1 to your grip. Add the rest of the cards to the bottom of your stack in any order.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13021", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Innovation. Iteration. Education.", "illustrator": "Pavel Kolomeyets", "keywords": "Location - Ritzy", "pack_code": "td", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "click: Reveal the top 4 cards of your stack. If any of those cards are programs, you may add 1 to your grip. Add the rest of the cards to the bottom of your stack in any order.", "stripped_title": "Levy Advanced Research Lab", "text": "[click]: Reveal the top 4 cards of your stack. If any of those cards are programs, you may add 1 to your grip. Add the rest of the cards to the bottom of your stack in any order.", "title": "Levy Advanced Research Lab", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_laguna_velasco_district_13022(Resource):
    '''
    Cost: 5
    Text: Whenever you take the basic action to draw cards, increase the number of cards you draw by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13022", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "One of the wealthiest and most powerful areas of New Angeles, Laguna Velasco is also known as the Government District.", "illustrator": "Mark Molnar", "keywords": "Location - Ritzy", "pack_code": "td", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you take the basic action to draw cards, increase the number of cards you draw by 1.", "stripped_title": "Laguna Velasco District", "text": "Whenever you take the basic action to draw cards, increase the number of cards you draw by 1.", "title": "Laguna Velasco District", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_officer_frank_13024(Resource):
    '''
    Cost: 0
    Text: trash, 1 credit: The Corp trashes 2 cards from HQ at random. Use this ability only if you suffered meat damage this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13024", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Monztre", "keywords": "Connection", "pack_code": "td", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "trash, 1 credit: The Corp trashes 2 cards from HQ at random. Use this ability only if you suffered meat damage this turn.", "stripped_title": "Officer Frank", "text": "[trash], 1[credit]: The Corp trashes 2 cards from HQ at random. Use this ability only if you suffered meat damage this turn.", "title": "Officer Frank", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_dean_lister_13025(Resource):
    '''
    Cost: 2
    Text: trash: Choose an icebreaker. Until the end of the run, that icebreaker has +1 strength for each card in your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13025", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Although he rarely teaches classes these days, his lectures are always well attended.", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "td", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Choose an icebreaker. Until the end of the run, that icebreaker has +1 strength for each card in your grip.", "stripped_title": "Dean Lister", "text": "[trash]: Choose an <strong>icebreaker</strong>. Until the end of the run, that <strong>icebreaker</strong> has +1 strength for each card in your grip.", "title": "Dean Lister", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_biometric_spoofing_13026(Resource):
    '''
    Cost: 2
    Text: trash: Prevent 2 damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13026", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "She left behind an encrypted trail leading to some random employee for a rival corp. She knew lazy sysops would work just hard enough to figure it out and wouldn't bother looking any deeper.", "illustrator": "Jarreau Wimberly", "pack_code": "td", "position": 26, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Prevent 2 damage.", "stripped_title": "Biometric Spoofing", "text": "[trash]: Prevent 2 damage.", "title": "Biometric Spoofing", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_shadow_net_13027(Resource):
    '''
    Cost: 0
    Text: click, forfeit an agenda: Play an event from your heap, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13027", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "A despicable web of outcasts and infamy, no government or corporation could effectively shut it down. If only because so many of their sysops, executives, and covert agents made use of it.", "illustrator": "Donald Crank", "keywords": "Virtual", "pack_code": "td", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "click, forfeit an agenda: Play an event from your heap, ignoring all costs.", "stripped_title": "The Shadow Net", "text": "[click]<strong>, forfeit an agenda:</strong> Play an event from your heap, ignoring all costs.", "title": "The Shadow Net", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_investigator_inez_delgado_14014(Resource):
    '''
    Cost: 0
    Text: When you win a game with Investigator Inez Delgado in your score area, reveal set 2. Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Expose all cards in a remote server. Use this only if you have stolean an agenda this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14014", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "tdc", "position": 15, "quantity": 3, "side_code": "runner", "stripped_text": "When you win a game with Investigator Inez Delgado in your score area, reveal set 2. Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Expose all cards in a remote server. Use this only if you have stolean an agenda this turn.", "stripped_title": "Investigator Inez Delgado", "text": "When you win a game with Investigator Inez Delgado in your score area, reveal set 2.\n<strong>Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points:</strong> Expose all cards in a remote server. Use this only if you have stolean an agenda this turn.", "title": "Investigator Inez Delgado", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_investigator_inez_delgado_2_14015(Resource):
    '''
    Cost: 0
    Text: When you win a game with Investigator Inez Delgado in your score area, reveal set 5. Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Reveal the top 3 cards in R&D. Use this only if you have stolean an agenda this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14015", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "tdc", "position": 16, "quantity": 3, "side_code": "runner", "stripped_text": "When you win a game with Investigator Inez Delgado in your score area, reveal set 5. Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Reveal the top 3 cards in R&D. Use this only if you have stolean an agenda this turn.", "stripped_title": "Investigator Inez Delgado 2", "text": "When you win a game with Investigator Inez Delgado in your score area, reveal set 5.\n<strong>Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points:</strong> Reveal the top 3 cards in R&D. Use this only if you have stolean an agenda this turn.", "title": "Investigator Inez Delgado 2", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_investigator_inez_delgado_3_14016(Resource):
    '''
    Cost: 0
    Text: When you win a game with Investigator Inez Delgado in your score area, reveal set 8. Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Reveal each card in HQ. Use this only if you have stolean an agenda this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14016", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "tdc", "position": 17, "quantity": 3, "side_code": "runner", "stripped_text": "When you win a game with Investigator Inez Delgado in your score area, reveal set 8. Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Reveal each card in HQ. Use this only if you have stolean an agenda this turn.", "stripped_title": "Investigator Inez Delgado 3", "text": "When you win a game with Investigator Inez Delgado in your score area, reveal set 8.\n<strong>Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points:</strong> Reveal each card in HQ. Use this only if you have stolean an agenda this turn.", "title": "Investigator Inez Delgado 3", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_investigator_inez_delgado_4_14017(Resource):
    '''
    Cost: 0
    Text: Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Reveal each card in HQ and the top card of R&D. Use this only if you have stolean an agenda this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14017", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "tdc", "position": 18, "quantity": 3, "side_code": "runner", "stripped_text": "Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points: Reveal each card in HQ and the top card of R&D. Use this only if you have stolean an agenda this turn.", "stripped_title": "Investigator Inez Delgado 4", "text": "<strong>Add Investigator Inez Delgado to your score area as an agenda worth 0 agenda points:</strong> Reveal each card in HQ and the top card of R&D. Use this only if you have stolean an agenda this turn.", "title": "Investigator Inez Delgado 4", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_shadow_team_14022(Resource):
    '''
    Cost: 0
    Text: Whenever you draw a Shadow Team, immediately install it. Whenever you initiate a run, trash a card from your grip, if able. When you make a successful run on a central server, destroy Shadow Team.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14022", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Adam Schumpert", "keywords": "Connection", "pack_code": "tdc", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you draw a Shadow Team, immediately install it. Whenever you initiate a run, trash a card from your grip, if able. When you make a successful run on a central server, destroy Shadow Team.", "stripped_title": "Shadow Team", "text": "Whenever you draw a Shadow Team, immediately install it.\nWhenever you initiate a run, trash a card from your grip, if able. When you make a successful run on a central server, destroy Shadow Team.", "title": "Shadow Team", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_masque_a_14024(Resource):
    '''
    Cost: 1
    Text: click,trash: Make a run and gain click. If successful, draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14024", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "PxelSlayer", "keywords": "Connection", "pack_code": "tdc", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "click,trash: Make a run and gain click. If successful, draw 1 card.", "stripped_title": "The Masque A", "text": "[click],[trash]: Make a run and gain [click]. If successful, draw 1 card.", "title": "The Masque A", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_masque_b_14025(Resource):
    '''
    Cost: 1
    Text: click,trash: Make a run and gain click. If that run is successful when it ends, you may immediately make another run on another server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14025", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "PxelSlayer", "keywords": "Connection", "pack_code": "tdc", "position": 26, "quantity": 3, "side_code": "runner", "stripped_text": "click,trash: Make a run and gain click. If that run is successful when it ends, you may immediately make another run on another server.", "stripped_title": "The Masque B", "text": "[click],[trash]: Make a run and gain [click]. If that run is successful when it ends, you may immediately make another run on another server.", "title": "The Masque B", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_ice_carver_20015(Resource):
    '''
    Cost: 3
    Text: While you are encountering a piece of ice, it gets -1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20015", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "In the public consciousness, there's a hard line between corp and runner. In the real world, things are a little more porous. The corps need the best hackers to run their networks, and some of the best hackers are ex-runners who like the idea of a regular paycheck. But sometimes things run the other way, and someone on the inside makes something like this.", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "core2", "position": 15, "quantity": 1, "side_code": "runner", "stripped_text": "While you are encountering a piece of ice, it gets -1 strength.", "stripped_title": "Ice Carver", "text": "While you are encountering a piece of ice, it gets -1 strength.", "title": "Ice Carver", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_liberated_account_20016(Resource):
    '''
    Cost: 6
    Text: When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20016", "cost": 6, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "It's easier to spend when it's not your money.", "illustrator": "Matt Zeilinger", "pack_code": "core2", "position": 16, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.", "stripped_title": "Liberated Account", "text": "When you install this resource, load 16[credit] onto it. When it is empty, trash it.\n[click]<strong>:</strong> Take 4[credit] from this resource.", "title": "Liberated Account", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_scrubber_20017(Resource):
    '''
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20017", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"They're mindless tools of destruction, good for little else. Nice guys, though. Some of my best friends are scrubbers.\" -Ji \"Noise\" Reilly", "illustrator": "Kate Laird", "keywords": "Connection - Seedy", "pack_code": "core2", "position": 17, "quantity": 2, "side_code": "runner", "stripped_text": "2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.", "stripped_title": "Scrubber", "text": "2[recurring-credit] <em>(When you install this card and before your turn begins, refill to 2 hosted credits.)</em>\nYou can spend hosted credits to pay trash costs.", "title": "Scrubber", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_xanadu_20018(Resource):
    '''
    Cost: 3
    Text: The rez cost of each piece of ice is increased by 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20018", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "And all should cry, Beware! Beware!\nHis flashing eyes, his floating hair!\nWeave a circle round him thrice,\nAnd close your eyes with holy dread,\nFor he on honey-dew hath fed,\nAnd drunk the milk of Paradise.\n-Samuel Taylor Coleridge", "illustrator": "Andrew Mar", "keywords": "Virtual", "pack_code": "core2", "position": 18, "quantity": 1, "side_code": "runner", "stripped_text": "The rez cost of each piece of ice is increased by 1 credit.", "stripped_title": "Xanadu", "text": "The rez cost of each piece of ice is increased by 1[credit].", "title": "Xanadu", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_bank_job_20033(Resource):
    '''
    Cost: 1
    Text: When you install this resource, load 8 credits on it. When it is empty, trash it. Whenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20033", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Kate Laird", "keywords": "Job", "pack_code": "core2", "position": 33, "quantity": 2, "side_code": "runner", "stripped_text": "When you install this resource, load 8 credits on it. When it is empty, trash it. Whenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.", "stripped_title": "Bank Job", "text": "When you install this resource, load 8[credit] on it. When it is empty, trash it.\nWhenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.", "title": "Bank Job", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_crash_space_20034(Resource):
    '''
    Cost: 2
    Text: 2 recurring credits Use these credits to pay for removing tags. trash: Prevent up to 3 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20034", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"My roomie, he had a cousin with a college girlfriend whose brother's best friend was an addict, and the addict's mother used to live here. So yeah, there's a connection.\" -Lez \"Rockfist\" S.", "illustrator": "Samuel Leung", "keywords": "Location", "pack_code": "core2", "position": 34, "quantity": 2, "side_code": "runner", "stripped_text": "2 recurring credits Use these credits to pay for removing tags. trash: Prevent up to 3 meat damage.", "stripped_title": "Crash Space", "text": "2[recurring-credit]\nUse these credits to pay for removing tags.\n[trash]: Prevent up to 3 meat damage.", "title": "Crash Space", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_fall_guy_20035(Resource):
    '''
    Cost: 0
    Text: trash: Prevent another installed resource from being trashed. trash: Gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20035", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "There are good, honest, hardworking cops in the NAPD. Officers who do their best to bring justice to the guilty and protect the innocent. Fortunately for the criminals, they're outnumbered by the other kind. The kind who are much easier to work with.", "illustrator": "Aurore Folny", "keywords": "Connection", "pack_code": "core2", "position": 35, "quantity": 1, "side_code": "runner", "stripped_text": "trash: Prevent another installed resource from being trashed. trash: Gain 2 credits.", "stripped_title": "Fall Guy", "text": "[trash]: Prevent another installed resource from being trashed.\n[trash]: Gain 2[credit].", "title": "Fall Guy", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_mr_li_20036(Resource):
    '''
    Cost: 3
    Text: click: Draw 2 cards. When you do, add 1 of those cards to the bottom of your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20036", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"We're always happy to help, Mr. Santiago.\"\n\"I appreciate it, Mr. Li.\"\n\"We'll be in touch. And, Gabriel\u2026\"\n\"Yes?\"\n\"Don't leave town.\"", "illustrator": "Gong Studios", "keywords": "Connection", "pack_code": "core2", "position": 36, "quantity": 1, "side_code": "runner", "stripped_text": "click: Draw 2 cards. When you do, add 1 of those cards to the bottom of your stack.", "stripped_title": "Mr. Li", "text": "<strong>[click]:</strong> Draw 2 cards. When you do, add 1 of those cards to the bottom of your stack.", "title": "Mr. Li", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_aesops_pawnshop_20052(Resource):
    '''
    Cost: 1
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20052", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "You didn't mention Aesop's arm unless you wanted an earful. Sometimes he talked about it in such a way that you wondered why he didn't laser his other arm off as well.", "illustrator": "Adam Schumpert", "keywords": "Connection - Location", "pack_code": "core2", "position": 52, "quantity": 1, "side_code": "runner", "stripped_text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.", "stripped_title": "Aesop's Pawnshop", "text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3[credit].", "title": "Aesop's Pawnshop", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_allnighter_20053(Resource):
    '''
    Cost: 0
    Text: click, trash: Gain click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20053", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"I don't care what the studies show. From my experience, I can ingest three cans of Diesel an hour for up to twelve hours before going into cardiac arrest.\" -heard during the eleventh hour", "illustrator": "Antonio De Luca", "pack_code": "core2", "position": 53, "quantity": 1, "side_code": "runner", "stripped_text": "click, trash: Gain click click.", "stripped_title": "All-nighter", "text": "[click], [trash]: Gain [click][click].", "title": "All-nighter", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_sacrificial_construct_20054(Resource):
    '''
    Cost: 0
    Text: trash: Prevent an installed program or an installed piece of hardware from being trashed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20054", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "The life expectancy of a jacked construct is about that of a mayfly. In other words, short.", "illustrator": "Matt Zeilinger", "keywords": "Remote", "pack_code": "core2", "position": 54, "quantity": 1, "side_code": "runner", "stripped_text": "trash: Prevent an installed program or an installed piece of hardware from being trashed.", "stripped_title": "Sacrificial Construct", "text": "[trash]: Prevent an installed program or an installed piece of hardware from being trashed.", "title": "Sacrificial Construct", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_armitage_codebusting_20059(Resource):
    '''
    Cost: 1
    Text: Place 12 credits from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it. click: Take 2 credits from Armitage Codebusting.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20059", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Drudge work, but it pays the bills.", "illustrator": "Dmitry Prosvirnin, Atha Kanaani", "keywords": "Job", "pack_code": "core2", "position": 59, "quantity": 3, "side_code": "runner", "stripped_text": "Place 12 credits from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it. click: Take 2 credits from Armitage Codebusting.", "stripped_title": "Armitage Codebusting", "text": "Place 12[credit] from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it.\n[click]: Take 2[credit] from Armitage Codebusting.", "title": "Armitage Codebusting", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_underworld_contact_20060(Resource):
    '''
    Cost: 2
    Text: When your turn begins, gain 1 credit if you have at least 2 link.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20060", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"My boss rewards quality work. If you know what's good for you, you'll keep it up.\"", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "core2", "position": 60, "quantity": 2, "side_code": "runner", "stripped_text": "When your turn begins, gain 1 credit if you have at least 2 link.", "stripped_title": "Underworld Contact", "text": "When your turn begins, gain 1[credit] if you have at least 2[link].", "title": "Underworld Contact", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_lewi_guilherme_21005(Resource):
    '''
    Cost: 0
    Text: When your turn begins, either lose 1 credit or trash Lewi Guilherme. The Corp's maximum hand size is reduced by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21005", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "flavor": "Brought up in the slums of Jinja, Lewi made his fortune through back alley deals, well-placed bets, and savvy showmanship.", "illustrator": "PxelSlayer", "keywords": "Connection", "pack_code": "ss", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, either lose 1 credit or trash Lewi Guilherme. The Corp's maximum hand size is reduced by 1.", "stripped_title": "Lewi Guilherme", "text": "When your turn begins, either lose 1[credit] or trash Lewi Guilherme.\nThe Corp's maximum hand size is reduced by 1.", "title": "Lewi Guilherme", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_assimilator_21008(Resource):
    '''
    Cost: 5
    Text: click,click: Turn one of your facedown installed cards faceup. If that card is an event, trash it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21008", "cost": 5, "deck_limit": 3, "faction_code": "apex", "faction_cost": 5, "flavor": "\"Its only function seems to be repurposing code.\"\n\"Can you kill it?\" she asked.\n\"I can try,\" he said. Guiding his program dead center of the mass, he plunged, piercing the shell before an eruption sent his screen into static. He jacked out, his eyes wide. \"I... I think it absorbed my breaker. And everything else.\"", "illustrator": "Alexandr Elichev", "keywords": "Virtual", "pack_code": "ss", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "click,click: Turn one of your facedown installed cards faceup. If that card is an event, trash it.", "stripped_title": "Assimilator", "text": "[click],[click]: Turn one of your facedown installed cards faceup. If that card is an event, trash it.", "title": "Assimilator", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_kongamato_21027(Resource):
    '''
    Cost: 1
    Text: trash: Break the first subroutine on the encountered piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21027", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "A winged terror, the Kongamato dives from above, rending its prey in one ferocious bite.", "illustrator": "Liiga Smilshkalne", "keywords": "Virtual", "pack_code": "dtwn", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Break the first subroutine on the encountered piece of ice.", "stripped_title": "Kongamato", "text": "[trash]: Break the first subroutine on the encountered piece of ice.", "title": "Kongamato", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_crypt_21043(Resource):
    '''
    Cost: 0
    Text: Whenever you make a successful run on Archives, you may place 1 virus counter on Crypt. click, trash, 3 hosted virus counters: Search your stack for a virus program and install it (paying its install cost), then shuffle your stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21043", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "The smell of rot strengthens with each step.", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "cotc", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on Archives, you may place 1 virus counter on Crypt. click, trash, 3 hosted virus counters: Search your stack for a virus program and install it (paying its install cost), then shuffle your stack.", "stripped_title": "Crypt", "text": "Whenever you make a successful run on Archives, you may place 1 virus counter on Crypt.\n[click], [trash], <strong>3 hosted virus counters</strong>: Search your stack for a <strong>virus</strong> program and install it (paying its install cost), then shuffle your stack.", "title": "Crypt", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_no_one_home_21045(Resource):
    '''
    Cost: 0
    Text: The first time you would take any number of tags or suffer any amount of net damage each turn, you may trash No One Home to force the Corp to "Trace[0]. If unsuccessful, the Runner avoids any number of tags or prevents any amount of net damage."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21045", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"Go away! I'm not here!\"", "illustrator": "Alexandr Elichev", "keywords": "Virtual", "pack_code": "cotc", "position": 45, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you would take any number of tags or suffer any amount of net damage each turn, you may trash No One Home to force the Corp to \"Trace[0]. If unsuccessful, the Runner avoids any number of tags or prevents any amount of net damage.\"", "stripped_title": "No One Home", "text": "The first time you would take any number of tags or suffer any amount of net damage each turn, you may trash No One Home to force the Corp to \"Trace[0]. If unsuccessful, the Runner avoids any number of tags or prevents any amount of net damage.\"", "title": "No One Home", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_gbahali_21047(Resource):
    '''
    Cost: 2
    Text: trash: Break the last subroutine on the encountered piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21047", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Ripples are all the prey sees before Gbahali swallows it whole.", "illustrator": "Liiga Smilshkalne", "keywords": "Virtual", "pack_code": "cotc", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Break the last subroutine on the encountered piece of ice.", "stripped_title": "Gbahali", "text": "[trash]: Break the last subroutine on the encountered piece of ice.", "title": "Gbahali", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_rogue_trading_21065(Resource):
    '''
    Cost: 0
    Text: Place 18 credits from the bank on Rogue Trading when it is installed. When there are no credits left on Rogue Trading, trash it. click, click: Take 6 credits from Rogue Trading and take 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21065", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Adam Schumpert", "keywords": "Job", "pack_code": "tdatd", "position": 65, "quantity": 3, "side_code": "runner", "stripped_text": "Place 18 credits from the bank on Rogue Trading when it is installed. When there are no credits left on Rogue Trading, trash it. click, click: Take 6 credits from Rogue Trading and take 1 tag.", "stripped_title": "Rogue Trading", "text": "Place 18[credit] from the bank on Rogue Trading when it is installed. When there are no credits left on Rogue Trading, trash it.\n[click], [click]: Take 6[credit] from Rogue Trading and take 1 tag.", "title": "Rogue Trading", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_slipstream_21085(Resource):
    '''
    Cost: 0
    Text: Whenever you pass a rezzed piece of ice, you may trash this resource. If you do, choose 1 piece of ice protecting a central server in the same position as the passed ice. Move to that ice and approach it. You may jack out.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21085", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Filaments occasionally flare from the Network, manifesting ephemeral threads between random domains.", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "win", "position": 85, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you pass a rezzed piece of ice, you may trash this resource. If you do, choose 1 piece of ice protecting a central server in the same position as the passed ice. Move to that ice and approach it. You may jack out.", "stripped_title": "Slipstream", "text": "Whenever you pass a rezzed piece of ice, you may trash this resource. If you do, choose 1 piece of ice protecting a central server in the same position as the passed ice. Move to that ice and approach it. You may jack out.", "title": "Slipstream", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_logic_bomb_21089(Resource):
    '''
    Cost: 0
    Text: trash: Bypass a piece of ice you are currently encountering. Lose any remaining clicks.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21089", "cost": 0, "deck_limit": 3, "faction_code": "adam", "faction_cost": 5, "flavor": "\"Could God create a stone so heavy, He could not lift it?\"", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "win", "position": 89, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Bypass a piece of ice you are currently encountering. Lose any remaining clicks.", "stripped_title": "Logic Bomb", "text": "[trash]: Bypass a piece of ice you are currently encountering. Lose any remaining clicks.", "title": "Logic Bomb", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_jackpot_21090(Resource):
    '''
    Cost: 0
    Text: When your turn begins, you may place 1 credit on Jackpot!. Whenever an agenda is added to your score area, you may take any number of credits from Jackpot!. If you do, trash Jackpot!.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21090", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Jackpot!\"", "illustrator": "Limetown Studios", "pack_code": "win", "position": 90, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may place 1 credit on Jackpot!. Whenever an agenda is added to your score area, you may take any number of credits from Jackpot!. If you do, trash Jackpot!.", "stripped_title": "Jackpot!", "text": "When your turn begins, you may place 1[credit] on Jackpot!.\nWhenever an agenda is added to your score area, you may take any number of credits from Jackpot!. If you do, trash Jackpot!.", "title": "Jackpot!", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_pad_tap_21106(Resource):
    '''
    Cost: 0
    Text: The first time the Corp gains credits through a card ability each turn, you may gain 1 credit. click, 3 credits: Trash PAD Tap. Only the Corp can use this ability.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21106", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"You called me, sir?\"\n\"Why does my PAD keep flashing 'Sensitive Information Transfer'?!\"\n\"Hmm, that's strange. Mine only does that on Tuesdays.\"", "illustrator": "Caravan Studio", "pack_code": "ka", "position": 106, "quantity": 3, "side_code": "runner", "stripped_text": "The first time the Corp gains credits through a card ability each turn, you may gain 1 credit. click, 3 credits: Trash PAD Tap. Only the Corp can use this ability.", "stripped_title": "PAD Tap", "text": "The first time the Corp gains credits through a card ability each turn, you may gain 1[credit].\n[click], 3[credit]: Trash PAD Tap. Only the Corp can use this ability.", "title": "PAD Tap", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_reclaim_21107(Resource):
    '''
    Cost: 0
    Text: click, trash, trash a card from your grip: Install a program, piece of hardware, or virtual resource from your heap, paying its install cost.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21107", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "It was a deal, to be sure. She just didn't know for which party.", "illustrator": "Josh Corpuz", "pack_code": "ka", "position": 107, "quantity": 3, "side_code": "runner", "stripped_text": "click, trash, trash a card from your grip: Install a program, piece of hardware, or virtual resource from your heap, paying its install cost.", "stripped_title": "Reclaim", "text": "[click], [trash], <strong>trash a card from your grip</strong>: Install a program, piece of hardware, or <strong>virtual</strong> resource from your heap, paying its install cost.", "title": "Reclaim", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_kasi_string_21111(Resource):
    '''
    Cost: 1
    Text: The first time each turn a successful run on a remote server ends, if you breached the server but stole no agendas, you may place 1 power counter on this resource. When this resource has 4 or more hosted power counters, add it to your score area as an agenda worth 1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21111", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Mariusz Siergiejew", "keywords": "Virtual", "pack_code": "ka", "position": 111, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn a successful run on a remote server ends, if you breached the server but stole no agendas, you may place 1 power counter on this resource. When this resource has 4 or more hosted power counters, add it to your score area as an agenda worth 1 agenda point.", "stripped_title": "Kasi String", "text": "The first time each turn a successful run on a remote server ends, if you breached the server but stole no agendas, you may place 1 power counter on this resource.\nWhen this resource has 4 or more hosted power counters, add it to your score area as an agenda worth 1 agenda point.", "title": "Kasi String", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_district_99_22007(Resource):
    '''
    Cost: 3
    Text: The first time each turn a program or a piece of hardware is trashed (from any location), you may place 1 power counter on District 99. click, 3 hosted power counters: Add a card that matches the faction of your identity from your heap to your grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22007", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Another man's treasure.", "illustrator": "Emilio Rodriguez", "keywords": "Location - Seedy", "pack_code": "rar", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn a program or a piece of hardware is trashed (from any location), you may place 1 power counter on District 99. click, 3 hosted power counters: Add a card that matches the faction of your identity from your heap to your grip.", "stripped_title": "District 99", "text": "The first time each turn a program or a piece of hardware is trashed (from any location), you may place 1 power counter on District 99.\n[click], <strong>3 hosted power counters</strong>: Add a card that matches the faction of your identity from your heap to your grip.", "title": "District 99", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_thunder_art_gallery_22013(Resource):
    '''
    Cost: 3
    Text: The first time you avoid or remove a tag each turn, you may install a card from your grip, lowering its install cost by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22013", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "A classy alibi.", "illustrator": "Marko Fiedler", "keywords": "Location - Ritzy", "pack_code": "rar", "position": 13, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you avoid or remove a tag each turn, you may install a card from your grip, lowering its install cost by 1.", "stripped_title": "Thunder Art Gallery", "text": "The first time you avoid or remove a tag each turn, you may install a card from your grip, lowering its install cost by 1.", "title": "Thunder Art Gallery", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_miss_bones_22014(Resource):
    '''
    Cost: 2
    Text: Place 12 credits from the bank on Miss Bones when she is installed. When there are no credits left on Miss Bones, trash her. Use these credits to trash installed cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22014", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"If I can't kill it, I know who can.\"", "illustrator": "Marko Fiedler", "keywords": "Connection", "pack_code": "rar", "position": 14, "quantity": 3, "side_code": "runner", "stripped_text": "Place 12 credits from the bank on Miss Bones when she is installed. When there are no credits left on Miss Bones, trash her. Use these credits to trash installed cards.", "stripped_title": "Miss Bones", "text": "Place 12[credit] from the bank on Miss Bones when she is installed. When there are no credits left on Miss Bones, trash her.\nUse these credits to trash installed cards.", "title": "Miss Bones", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_psych_mike_22021(Resource):
    '''
    Cost: 1
    Text: The first time each turn a successful run on R&D ends, you may gain 1 credit for each time you accessed a card in R&D during that run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22021", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "\"Breathe, girl. Breathe.\" Mike flickered into focus as she brushed Akiko's tears away. \"What did you see?\"\n\"I...\" Akiko hesitated. \"Everything.\"", "illustrator": "Zefanya Langkan Maega", "keywords": "Connection", "pack_code": "rar", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn a successful run on R&D ends, you may gain 1 credit for each time you accessed a card in R&D during that run.", "stripped_title": "Psych Mike", "text": "The first time each turn a successful run on R&D ends, you may gain 1[credit] for each time you accessed a card in R&D during that run.", "title": "Psych Mike", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_dj_fenris_22025(Resource):
    '''
    Cost: 3
    Text: Host a g-mod identity that does not match the faction of your identity on DJ Fenris when he is installed. Remove hosted identity from the game if DJ Fenris is uninstalled. DJ Fenris gains the text of hosted identity. Limit 1 per deck.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22025", "cost": 3, "deck_limit": 1, "faction_code": "neutral-runner", "faction_cost": 1, "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "rar", "position": 25, "quantity": 1, "side_code": "runner", "stripped_text": "Host a g-mod identity that does not match the faction of your identity on DJ Fenris when he is installed. Remove hosted identity from the game if DJ Fenris is uninstalled. DJ Fenris gains the text of hosted identity. Limit 1 per deck.", "stripped_title": "DJ Fenris", "text": "Host a <strong>g-mod</strong> identity that does not match the faction of your identity on DJ Fenris when he is installed. Remove hosted identity from the game if DJ Fenris is uninstalled.\nDJ Fenris gains the text of hosted identity.\nLimit 1 per deck.", "title": "DJ Fenris", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_crowdfunding_23013(Resource):
    '''
    Cost: 0
    Text: When you install this resource, load 3 credits onto it. When it is empty, trash it and draw 1 card. When your turn begins, take 1 credit from this resource. When your turn ends, if you made at least 3 successful runs this turn and this card is in your heap, you may install it, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "23013", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "<strong>Designed by 2017 GenCon Champion Sam Suied</strong>", "illustrator": "Mariusz Siergiejew", "keywords": "Seedy - Virtual", "pack_code": "mo", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 3 credits onto it. When it is empty, trash it and draw 1 card. When your turn begins, take 1 credit from this resource. When your turn ends, if you made at least 3 successful runs this turn and this card is in your heap, you may install it, ignoring all costs.", "stripped_title": "Crowdfunding", "text": "When you install this resource, load 3[credit] onto it. When it is empty, trash it and draw 1 card.\nWhen your turn begins, take 1[credit] from this resource.\nWhen your turn ends, if you made at least 3 successful runs this turn and this card is in your heap, you may install it, ignoring all costs.", "title": "Crowdfunding", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_ice_carver_25016(Resource):
    '''
    Cost: 3
    Text: While you are encountering a piece of ice, it gets -1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25016", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "In the public consciousness, there's a hard line between corp and runner. In the real world, things are a little more porous. The corps need the best hackers to run their networks, and some of the best hackers are ex-runners who like the idea of a regular paycheck. But sometimes things run the other way, and someone on the inside makes something like this.", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "sc19", "position": 16, "quantity": 1, "side_code": "runner", "stripped_text": "While you are encountering a piece of ice, it gets -1 strength.", "stripped_title": "Ice Carver", "text": "While you are encountering a piece of ice, it gets -1 strength.", "title": "Ice Carver", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_liberated_account_25017(Resource):
    '''
    Cost: 6
    Text: When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25017", "cost": 6, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "It's easier to spend when it's not your money.", "illustrator": "Matt Zeilinger", "pack_code": "sc19", "position": 17, "quantity": 2, "side_code": "runner", "stripped_text": "When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.", "stripped_title": "Liberated Account", "text": "When you install this resource, load 16[credit] onto it. When it is empty, trash it.\n[click]<strong>:</strong> Take 4[credit] from this resource.", "title": "Liberated Account", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_scrubber_25018(Resource):
    '''
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25018", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"They're mindless tools of destruction, good for little else. Nice guys, though. Some of my best friends are scrubbers.\" -Ji \"Noise\" Reilly", "illustrator": "Kate Laird", "keywords": "Connection - Seedy", "pack_code": "sc19", "position": 18, "quantity": 2, "side_code": "runner", "stripped_text": "2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.", "stripped_title": "Scrubber", "text": "2[recurring-credit] <em>(When you install this card and before your turn begins, refill to 2 hosted credits.)</em>\nYou can spend hosted credits to pay trash costs.", "title": "Scrubber", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_xanadu_25019(Resource):
    '''
    Cost: 3
    Text: The rez cost of each piece of ice is increased by 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25019", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "And all should cry, Beware! Beware!\nHis flashing eyes, his floating hair!\nWeave a circle round him thrice,\nAnd close your eyes with holy dread,\nFor he on honey-dew hath fed,\nAnd drunk the milk of Paradise.\n-Samuel Taylor Coleridge", "illustrator": "Andrew Mar", "keywords": "Virtual", "pack_code": "sc19", "position": 19, "quantity": 1, "side_code": "runner", "stripped_text": "The rez cost of each piece of ice is increased by 1 credit.", "stripped_title": "Xanadu", "text": "The rez cost of each piece of ice is increased by 1[credit].", "title": "Xanadu", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_bank_job_25038(Resource):
    '''
    Cost: 1
    Text: When you install this resource, load 8 credits on it. When it is empty, trash it. Whenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25038", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Kate Laird", "keywords": "Job", "pack_code": "sc19", "position": 38, "quantity": 2, "side_code": "runner", "stripped_text": "When you install this resource, load 8 credits on it. When it is empty, trash it. Whenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.", "stripped_title": "Bank Job", "text": "When you install this resource, load 8[credit] on it. When it is empty, trash it.\nWhenever you make a successful run on a remote server, instead of breaching that server, you may take any number of credits from this resource.", "title": "Bank Job", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_data_dealer_25039(Resource):
    '''
    Cost: 0
    Text: click, forfeit 1 agenda: Gain 9 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25039", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Shadier the dealer, better the price. Unless the dealer's too shady. Then there might be a hidden fee after they take your scrip.", "illustrator": "Mauricio Herrera", "keywords": "Connection - Seedy", "pack_code": "sc19", "position": 39, "quantity": 1, "side_code": "runner", "stripped_text": "click, forfeit 1 agenda: Gain 9 credits.", "stripped_title": "Data Dealer", "text": "<strong>[click]</strong>, <strong>forfeit 1 agenda:</strong> Gain 9[credit].", "title": "Data Dealer", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_aesops_pawnshop_25056(Resource):
    '''
    Cost: 1
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25056", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "You didn't mention Aesop's arm unless you wanted an earful. Sometimes he talked about it in such a way that you wondered why he didn't laser his other arm off as well.", "illustrator": "Adam Schumpert", "keywords": "Connection - Location", "pack_code": "sc19", "position": 56, "quantity": 2, "side_code": "runner", "stripped_text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.", "stripped_title": "Aesop's Pawnshop", "text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3[credit].", "title": "Aesop's Pawnshop", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_ice_analyzer_25057(Resource):
    '''
    Cost: 0
    Text: Whenever the Corp rezzes a piece of ice, place 1 credit on Ice Analyzer. You may use credits on Ice Analyzer to install programs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25057", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"If you know the source code you can write to beat it, or just rejigger it a little and make it yours. That works, too.\" -Exile", "illustrator": "Ed Mattinian", "keywords": "Virtual", "pack_code": "sc19", "position": 57, "quantity": 2, "side_code": "runner", "stripped_text": "Whenever the Corp rezzes a piece of ice, place 1 credit on Ice Analyzer. You may use credits on Ice Analyzer to install programs.", "stripped_title": "Ice Analyzer", "text": "Whenever the Corp rezzes a piece of ice, place 1[credit] on Ice Analyzer.\nYou may use credits on Ice Analyzer to install programs.", "title": "Ice Analyzer", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_professional_contacts_25058(Resource):
    '''
    Cost: 5
    Text: click: Gain 1 credit and draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25058", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Sometimes it doesn't matter how expensive your rig is, or how many credits are in your account, or even your skill as a runner. Most of the time, a simple handshake and a name are all you need.", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "sc19", "position": 58, "quantity": 2, "side_code": "runner", "stripped_text": "click: Gain 1 credit and draw 1 card.", "stripped_title": "Professional Contacts", "text": "[click]<strong>:</strong> Gain 1[credit] and draw 1 card.", "title": "Professional Contacts", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_armitage_codebusting_25062(Resource):
    '''
    Cost: 1
    Text: Place 12 credits from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it. click: Take 2 credits from Armitage Codebusting.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25062", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Drudge work, but it pays the bills.", "illustrator": "Dmitry Prosvirnin, Atha Kanaani", "keywords": "Job", "pack_code": "sc19", "position": 62, "quantity": 2, "side_code": "runner", "stripped_text": "Place 12 credits from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it. click: Take 2 credits from Armitage Codebusting.", "stripped_title": "Armitage Codebusting", "text": "Place 12[credit] from the bank on Armitage Codebusting when it is installed. When there are no credits left on Armitage Codebusting, trash it.\n[click]: Take 2[credit] from Armitage Codebusting.", "title": "Armitage Codebusting", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_earthrise_hotel_25063(Resource):
    '''
    Cost: 4
    Text: When you install this resource, load 3 power counters onto it. When it is empty, trash it. When your turn begins, remove 1 hosted power counter and draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25063", "cost": 4, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Simon Boxer", "keywords": "Location - Ritzy", "pack_code": "sc19", "position": 63, "quantity": 2, "side_code": "runner", "stripped_text": "When you install this resource, load 3 power counters onto it. When it is empty, trash it. When your turn begins, remove 1 hosted power counter and draw 2 cards.", "stripped_title": "Earthrise Hotel", "text": "When you install this resource, load 3 power counters onto it. When it is empty, trash it.\nWhen your turn begins, remove 1 hosted power counter and draw 2 cards.", "title": "Earthrise Hotel", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_john_masanori_25064(Resource):
    '''
    Cost: 2
    Text: The first time you make a successful run each turn, draw 1 card. The first time you make an unsuccessful run each turn, take 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25064", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"I've been logging online with babes all day. Don't worry, the connections are clean. I guarantee it.\"", "illustrator": "Zefanya Langkan Maega", "keywords": "Connection", "pack_code": "sc19", "position": 64, "quantity": 2, "side_code": "runner", "stripped_text": "The first time you make a successful run each turn, draw 1 card. The first time you make an unsuccessful run each turn, take 1 tag.", "stripped_title": "John Masanori", "text": "The first time you make a successful run each turn, draw 1 card.\nThe first time you make an unsuccessful run each turn, take 1 tag.", "title": "John Masanori", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_kati_jones_25065(Resource):
    '''
    Cost: 2
    Text: You cannot use Kati Jones more than once per turn. click: Place 3 credits from the bank on Kati Jones. click: Take all credits from Kati Jones.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25065", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"You aren't the only type of runner in New Angeles.\"", "illustrator": "Matt Zeilinger", "keywords": "Connection", "pack_code": "sc19", "position": 65, "quantity": 2, "side_code": "runner", "stripped_text": "You cannot use Kati Jones more than once per turn. click: Place 3 credits from the bank on Kati Jones. click: Take all credits from Kati Jones.", "stripped_title": "Kati Jones", "text": "You cannot use Kati Jones more than once per turn.\n[click]: Place 3[credit] from the bank on Kati Jones.\n[click]: Take all credits from Kati Jones.", "title": "Kati Jones", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_climactic_showdown_26006(Resource):
    '''
    Cost: 2
    Text: When your turn begins, remove this resource from the game. Choose a server protected by ice. The Corp may trash 1 piece of ice protecting that server. If they do not, the first time this turn you breach either R&D or HQ, access 2 additional cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26006", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 5, "illustrator": "Diana Simonova (Antheia Vaulor)", "pack_code": "df", "position": 6, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, remove this resource from the game. Choose a server protected by ice. The Corp may trash 1 piece of ice protecting that server. If they do not, the first time this turn you breach either R&D or HQ, access 2 additional cards.", "stripped_title": "Climactic Showdown", "text": "When your turn begins, remove this resource from the game. Choose a server protected by ice. The Corp may trash 1 piece of ice protecting that server. If they do not, the first time this turn you breach either R&D or HQ, access 2 additional cards.", "title": "Climactic Showdown", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_fencer_fueno_26007(Resource):
    '''
    Cost: 0
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Whenever you make a successful run, you may spend hosted credits for the remainder of that run. When your turn ends, if there are 3 or more hosted credits, you must pay 1 credit or trash this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26007", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "Friends break your walls.", "illustrator": "Izzy Pruett", "keywords": "Companion - Virtual", "pack_code": "df", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins or you steal an agenda, place 1 credit on this resource. Whenever you make a successful run, you may spend hosted credits for the remainder of that run. When your turn ends, if there are 3 or more hosted credits, you must pay 1 credit or trash this resource.", "stripped_title": "Fencer Fueno", "text": "When your turn begins or you steal an agenda, place 1[credit] on this resource.\nWhenever you make a successful run, you may spend hosted credits for the remainder of that run.\nWhen your turn ends, if there are 3 or more hosted credits, you must pay 1[credit] or trash this resource.", "title": "Fencer Fueno", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_nihilist_26008(Resource):
    '''
    Cost: 4
    Text: The first time each turn you install a virus program, place 2 virus counters on this resource. When your turn begins, you may remove any 2 virus counters from your installed cards. If you do, draw 2 cards unless the Corp trashes the top card of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26008", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 5, "flavor": "\"...well, <em>I'm</em> laughing.\"", "illustrator": "Wyn Lacabra", "keywords": "Connection - Seedy", "pack_code": "df", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you install a virus program, place 2 virus counters on this resource. When your turn begins, you may remove any 2 virus counters from your installed cards. If you do, draw 2 cards unless the Corp trashes the top card of R&D.", "stripped_title": "The Nihilist", "text": "The first time each turn you install a <strong>virus</strong> program, place 2 virus counters on this resource.\nWhen your turn begins, you may remove any 2 virus counters from your installed cards. If you do, draw 2 cards unless the Corp trashes the top card of R&D.", "title": "The Nihilist", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_trickster_taka_26009(Resource):
    '''
    Cost: 1
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to use programs during runs. When your turn ends, if there are 3 or more hosted credits, you must take 1 tag or trash this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26009", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Friends hide your fears.", "illustrator": "Izzy Pruett", "keywords": "Stealth - Companion - Virtual", "pack_code": "df", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to use programs during runs. When your turn ends, if there are 3 or more hosted credits, you must take 1 tag or trash this resource.", "stripped_title": "Trickster Taka", "text": "When your turn begins or you steal an agenda, place 1[credit] on this resource.\nSpend hosted credits to use programs during runs.\nWhen your turn ends, if there are 3 or more hosted credits, you must take 1 tag or trash this resource.", "title": "Trickster Taka", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_baklan_bochkin_26017(Resource):
    '''
    Cost: 2
    Text: The first time each run you encounter a piece of ice, place 1 power counter on this resource. trash: Derez the ice you are encountering if its strength is equal to or less than the number of hosted power counters. Take 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26017", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Psh, let them gossip. The cat knows whose meat it has eaten.\" -\"Baklan\" Bochkin", "illustrator": "Janet Bruesselbach", "keywords": "Connection", "pack_code": "df", "position": 17, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each run you encounter a piece of ice, place 1 power counter on this resource. trash: Derez the ice you are encountering if its strength is equal to or less than the number of hosted power counters. Take 1 tag.", "stripped_title": "\"Baklan\" Bochkin", "text": "The first time each run you encounter a piece of ice, place 1 power counter on this resource.\n[trash]<strong>:</strong> Derez the ice you are encountering if its strength is equal to or less than the number of hosted power counters. Take 1 tag.", "title": "\"Baklan\" Bochkin", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_class_act_26018(Resource):
    '''
    Cost: 4
    Text: When your discard phase ends, if you installed this resource this turn, draw 4 cards. Interrupt -> The first time each turn you would draw any number of cards, look at the top X cards of your stack. Add 1 of those cards to the bottom of your stack. X is equal to the number of cards you will draw plus 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26018", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 5, "flavor": "\"...but I am without compare.\"", "illustrator": "Wyn Lacabra", "keywords": "Connection - Ritzy", "pack_code": "df", "position": 18, "quantity": 3, "side_code": "runner", "stripped_text": "When your discard phase ends, if you installed this resource this turn, draw 4 cards. Interrupt -> The first time each turn you would draw any number of cards, look at the top X cards of your stack. Add 1 of those cards to the bottom of your stack. X is equal to the number of cards you will draw plus 1.", "stripped_title": "The Class Act", "text": "When your discard phase ends, if you installed this resource this turn, draw 4 cards.\n[interrupt] \u2192 The first time each turn you would draw any number of cards, look at the top X cards of your stack. Add 1 of those cards to the bottom of your stack. X is equal to the number of cards you will draw plus 1.", "title": "The Class Act", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_artist_26027(Resource):
    '''
    Cost: 4
    Text: Use each ability on this resource only once per turn. click: Gain 2 credits. click: Install a program or piece of hardware, paying 1 credit less.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26027", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 5, "flavor": "\"...then let me paint you a picture.\"", "illustrator": "Wyn Lacabra", "keywords": "Connection", "pack_code": "df", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "Use each ability on this resource only once per turn. click: Gain 2 credits. click: Install a program or piece of hardware, paying 1 credit less.", "stripped_title": "The Artist", "text": "Use each ability on this resource only once per turn.\n[click]<strong>:</strong> Gain 2[credit].\n[click]<strong>:</strong> Install a program or piece of hardware, paying 1[credit] less.", "title": "The Artist", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_whistleblower_26030(Resource):
    '''
    Cost: 2
    Text: Whenever you make a successful run, you may trash this resource to name an agenda. The next time this run you access a copy of the named agenda, steal it, ignoring all costs. (You are no longer accessing it.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26030", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "\"Corporations are made of people; just normal people doing their 6-to-6. The right truths, the right critique, and they can be redeemed.\" -Lat", "illustrator": "Olie Boldador", "keywords": "Connection", "pack_code": "df", "position": 30, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run, you may trash this resource to name an agenda. The next time this run you access a copy of the named agenda, steal it, ignoring all costs. (You are no longer accessing it.)", "stripped_title": "Whistleblower", "text": "Whenever you make a successful run, you may trash this resource to name an agenda. The next time this run you access a copy of the named agenda, steal it, ignoring all costs. <em>(You are no longer accessing it.)</em>", "title": "Whistleblower", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_mystic_maemi_26072(Resource):
    '''
    Cost: 1
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to play events. When your turn ends, if there are 3 or more hosted credits, you must trash 1 card from your grip at random or trash this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26072", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Friends lift your spirits.", "illustrator": "Izzy Pruett", "keywords": "Companion - Virtual", "pack_code": "ur", "position": 72, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to play events. When your turn ends, if there are 3 or more hosted credits, you must trash 1 card from your grip at random or trash this resource.", "stripped_title": "Mystic Maemi", "text": "When your turn begins or you steal an agenda, place 1[credit] on this resource.\nSpend hosted credits to play events.\nWhen your turn ends, if there are 3 or more hosted credits, you must trash 1 card from your grip at random or trash this resource.", "title": "Mystic Maemi", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_paladin_poemu_26073(Resource):
    '''
    Cost: 1
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to install non-connection cards. When your turn ends, if there are 3 or more hosted credits, you must trash 1 of your installed cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26073", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Friends guard your passions.", "illustrator": "Izzy Pruett", "keywords": "Companion - Virtual", "pack_code": "ur", "position": 73, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to install non-connection cards. When your turn ends, if there are 3 or more hosted credits, you must trash 1 of your installed cards.", "stripped_title": "Paladin Poemu", "text": "When your turn begins or you steal an agenda, place 1[credit] on this resource.\nSpend hosted credits to install non-<strong>connection</strong> cards.\nWhen your turn ends, if there are 3 or more hosted credits, you must trash 1 of your installed cards.", "title": "Paladin Poemu", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_penumbral_toolkit_26081(Resource):
    '''
    Cost: 2
    Text: This card costs 2 credits less to install if you made a successful run on HQ this turn. When you install this resource, load 4 credits onto it. When it is empty, trash it. Spend hosted credits during runs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26081", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Shadow Net marketplaces have such venerability that they differ from legal platforms only in the products offered.", "illustrator": "Kevin Tame", "keywords": "Stealth - Virtual", "pack_code": "ur", "position": 81, "quantity": 3, "side_code": "runner", "stripped_text": "This card costs 2 credits less to install if you made a successful run on HQ this turn. When you install this resource, load 4 credits onto it. When it is empty, trash it. Spend hosted credits during runs.", "stripped_title": "Penumbral Toolkit", "text": "This card costs 2[credit] less to install if you made a successful run on HQ this turn.\nWhen you install this resource, load 4[credit] onto it. When it is empty, trash it.\nSpend hosted credits during runs.", "title": "Penumbral Toolkit", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_back_26082(Resource):
    '''
    Cost: 1
    Text: The first time each turn you use hardware during a run, place 1 power counter on this resource. click, remove this resource from the game: Shuffle up to X cards with trash abilities from your heap into your stack. X is double the number of hosted power counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26082", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "flavor": "\"Junk plus undiscerning buyers equals profit.\"\n-Az McCaffrey", "illustrator": "Izzy Pruett", "keywords": "Job - Location", "pack_code": "ur", "position": 82, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you use hardware during a run, place 1 power counter on this resource. click, remove this resource from the game: Shuffle up to X cards with trash abilities from your heap into your stack. X is double the number of hosted power counters.", "stripped_title": "The Back", "text": "The first time each turn you use hardware during a run, place 1 power counter on this resource.\n[click], <strong>remove this resource from the game:</strong> Shuffle up to X cards with [trash] abilities from your heap into your stack. X is double the number of hosted power counters.", "title": "The Back", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_cybertrooper_talut_26091(Resource):
    '''
    Cost: 2
    Text: +1 link Whenever you install a non-AI icebreaker, that icebreaker gets +2 strength for the remainder of the turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26091", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "He's nice enough, but not when there are 5,187 of him.", "illustrator": "Owen Sinodov", "keywords": "Connection - Virtual", "pack_code": "ur", "position": 91, "quantity": 3, "side_code": "runner", "stripped_text": "+1 link Whenever you install a non-AI icebreaker, that icebreaker gets +2 strength for the remainder of the turn.", "stripped_title": "Cybertrooper Talut", "text": "+1[link]\nWhenever you install a non-<strong>AI</strong> <strong>icebreaker</strong>, that <strong>icebreaker</strong> gets +2 strength for the remainder of the turn.", "title": "Cybertrooper Talut", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_paules_cafe_26092(Resource):
    '''
    Cost: 1
    Text: click: Host 1 program or piece of hardware from your grip on this resource. 1 credit: Install 1 hosted card. The first card you install this way during each of your turns costs 1 credit less to install for each unique () connection you have installed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26092", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "<strong>Designed by 2018 Eternal Champion Oguz Han Asnaz</strong>", "illustrator": "Matt Zeilinger", "keywords": "Location - Seedy", "pack_code": "ur", "position": 92, "quantity": 3, "side_code": "runner", "stripped_text": "click: Host 1 program or piece of hardware from your grip on this resource. 1 credit: Install 1 hosted card. The first card you install this way during each of your turns costs 1 credit less to install for each unique () connection you have installed.", "stripped_title": "Paule's Cafe", "text": "[click]: Host 1 program or piece of hardware from your grip on this resource.\n1[credit]: Install 1 hosted card. The first card you install this way during each of your turns costs 1[credit] less to install for each unique <em>(\u2666)</em> <strong>connection</strong> you have installed.", "title": "Paule's Caf\u00e9", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_daily_casts_26094(Resource):
    '''
    Cost: 3
    Text: When you install this resource, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26094", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "To strike another blow to the corporatocracy tomorrow night, don't forget to like and subscribe!", "illustrator": "Olie Boldador", "pack_code": "ur", "position": 94, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this resource.", "stripped_title": "Daily Casts", "text": "When you install this resource, load 8[credit] onto it. When it is empty, trash it.\nWhen your turn begins, take 2[credit] from this resource.", "title": "Daily Casts", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_dreamnet_26095(Resource):
    '''
    Cost: 3
    Text: The first time each turn you make a successful run, draw 1 card. If you have at least 2 link or your identity is digital, also gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26095", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Did I dream that dance through virtual space, or does that program now dream of flesh?", "illustrator": "Janet Bruesselbach", "keywords": "Virtual", "pack_code": "ur", "position": 95, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you make a successful run, draw 1 card. If you have at least 2 link or your identity is digital, also gain 1 credit.", "stripped_title": "DreamNet", "text": "The first time each turn you make a successful run, draw 1 card. If you have at least 2[link] or your identity is <strong>digital</strong>, also gain 1[credit].", "title": "DreamNet", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_mystic_maemi_27001(Resource):
    '''
    Cost: 1
    Text: When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to play events. When your turn ends, if there are 3 or more hosted credits, you must trash 1 card from your grip at random or trash this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "27001", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Friends lift your spirits.", "illustrator": "Izzy Pruett", "keywords": "Companion - Virtual", "pack_code": "urbp", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins or you steal an agenda, place 1 credit on this resource. Spend hosted credits to play events. When your turn ends, if there are 3 or more hosted credits, you must trash 1 card from your grip at random or trash this resource.", "stripped_title": "Mystic Maemi", "text": "When your turn begins or you steal an agenda, place 1[credit] on this resource.\nSpend hosted credits to play events.\nWhen your turn ends, if there are 3 or more hosted credits, you must trash 1 card from your grip at random or trash this resource.", "title": "Mystic Maemi", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_cybertrooper_talut_27003(Resource):
    '''
    Cost: 2
    Text: +1 link Whenever you install a non-AI icebreaker, that icebreaker gets +2 strength for the remainder of the turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "27003", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "He's nice enough, but not when there are 5,187 of him.", "illustrator": "Owen Sinodov", "keywords": "Connection - Virtual", "pack_code": "urbp", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "+1 link Whenever you install a non-AI icebreaker, that icebreaker gets +2 strength for the remainder of the turn.", "stripped_title": "Cybertrooper Talut", "text": "+1[link]\nWhenever you install a non-<strong>AI</strong> <strong>icebreaker</strong>, that <strong>icebreaker</strong> gets +2 strength for the remainder of the turn.", "title": "Cybertrooper Talut", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_crowdfunding_28002(Resource):
    '''
    Cost: 0
    Text: When you install this resource, load 3 credits onto it. When it is empty, trash it and draw 1 card. When your turn begins, take 1 credit from this resource. When your turn ends, if you made at least 3 successful runs this turn and this card is in your heap, you may install it, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "28002", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "<strong>Designed by 2017 GenCon Champion Sam Suied</strong>", "illustrator": "Patrick Burk, Mark Chandler", "keywords": "Seedy - Virtual", "pack_code": "mor", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 3 credits onto it. When it is empty, trash it and draw 1 card. When your turn begins, take 1 credit from this resource. When your turn ends, if you made at least 3 successful runs this turn and this card is in your heap, you may install it, ignoring all costs.", "stripped_title": "Crowdfunding", "text": "When you install this resource, load 3[credit] onto it. When it is empty, trash it and draw 1 card.\nWhen your turn begins, take 1[credit] from this resource.\nWhen your turn ends, if you made at least 3 successful runs this turn and this card is in your heap, you may install it, ignoring all costs.", "title": "Crowdfunding", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_cookbook_30009(Resource):
    '''
    Cost: 1
    Text: Whenever you install a virus program, you may place 1 virus counter on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30009", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"It waits on an unlabelled memstrip far below the deepest hab. Angry, desperate souls seek it out, hungry for power to change a brutal world. Once they can stomach no more bitter revenge, they return to that nameless tunnel, the book a recipe thicker.\"\n\u2014Heinlein urban legend", "illustrator": "Cat Shen", "keywords": "Virtual", "pack_code": "sg", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you install a virus program, you may place 1 virus counter on it.", "stripped_title": "Cookbook", "text": "Whenever you install a <strong>virus</strong> program, you may place 1 virus counter on it.", "title": "Cookbook", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_red_team_30018(Resource):
    '''
    Cost: 5
    Text: When you install this resource, load 12 credits onto it. When it is empty, trash it. click: Run a central server you have not run this turn. If successful, take 3 credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30018", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "The Domes of Heinlein are a pressure cooker of cutthroat capitalism. Prospective employers rarely have time for background checks.", "illustrator": "David Lei", "keywords": "Job", "pack_code": "sg", "position": 18, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 12 credits onto it. When it is empty, trash it. click: Run a central server you have not run this turn. If successful, take 3 credits from this resource.", "stripped_title": "Red Team", "text": "When you install this resource, load 12[credit] onto it. When it is empty, trash it.\n[click]<strong>:</strong> Run a central server you have not run this turn. If successful, take 3[credit] from this resource.", "title": "Red Team", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_telework_contract_30027(Resource):
    '''
    Cost: 1
    Text: When you install this resource, load 9 credits onto it. When it is empty, trash it. click: Take 3 credits from this resource. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30027", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"For all I know, I could spend a shift digging next to old Weyland himself.\"\n\u2014Lane", "illustrator": "Benjamin Giletti", "keywords": "Job", "pack_code": "sg", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 9 credits onto it. When it is empty, trash it. click: Take 3 credits from this resource. Use this ability only once per turn.", "stripped_title": "Telework Contract", "text": "When you install this resource, load 9[credit] onto it. When it is empty, trash it.\n[click]<strong>:</strong> Take 3[credit] from this resource. Use this ability only once per turn.", "title": "Telework Contract", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_smartware_distributor_30033(Resource):
    '''
    Cost: 0
    Text: click: Place 3 credits on this resource. When your turn begins, take 1 credit from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30033", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "The beauty of 22nd-century tech: if it still functions after all these decades, you know the build quality is solid.", "illustrator": "Benjamin Giletti", "keywords": "Connection", "pack_code": "sg", "position": 33, "quantity": 3, "side_code": "runner", "stripped_text": "click: Place 3 credits on this resource. When your turn begins, take 1 credit from this resource.", "stripped_title": "Smartware Distributor", "text": "[click]<strong>:</strong> Place 3[credit] on this resource.\nWhen your turn begins, take 1[credit] from this resource.", "title": "Smartware Distributor", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_verbal_plasticity_30034(Resource):
    '''
    Cost: 3
    Text: The first time each turn you take the basic action to draw 1 card, instead draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30034", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Some kids got g-mods for beauty, sports, or staying up all night. My parents thought Broca-mods were cool. Hah. Fluent in ten languages so far, and still searching for the words to thank them.\"\n\u2014Patrick Blue, Solar Artist", "illustrator": "David Lei", "keywords": "Genetics", "pack_code": "sg", "position": 34, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you take the basic action to draw 1 card, instead draw 2 cards.", "stripped_title": "Verbal Plasticity", "text": "The first time each turn you take the basic action to draw 1 card, instead draw 2 cards.", "title": "Verbal Plasticity", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_ice_carver_31009(Resource):
    '''
    Cost: 3
    Text: While you are encountering a piece of ice, it gets -1 strength.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31009", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "At the code level, all ice manifests via a small number of common protocols. Security managers are kept awake by nightmares of a disgruntled sysop walking out the door with the core infosec library.", "illustrator": "Krembler", "keywords": "Virtual", "pack_code": "su21", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "While you are encountering a piece of ice, it gets -1 strength.", "stripped_title": "Ice Carver", "text": "While you are encountering a piece of ice, it gets -1 strength.", "title": "Ice Carver", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_liberated_account_31010(Resource):
    '''
    Cost: 6
    Text: When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31010", "cost": 6, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Money is like gravity, it accretes.\nJustice is like resisting gravity, it takes <strong>force</strong>.", "illustrator": "Zoe Cohen", "pack_code": "su21", "position": 10, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 16 credits onto it. When it is empty, trash it. click: Take 4 credits from this resource.", "stripped_title": "Liberated Account", "text": "When you install this resource, load 16[credit] onto it. When it is empty, trash it.\n[click]<strong>:</strong> Take 4[credit] from this resource.", "title": "Liberated Account", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_scrubber_31011(Resource):
    '''
    Cost: 2
    Text: 2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31011", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "Destruction is forever.", "illustrator": "Krembler, Zoe Cohen", "keywords": "Connection - Seedy", "pack_code": "su21", "position": 11, "quantity": 3, "side_code": "runner", "stripped_text": "2 recurring credits (When you install this card and before your turn begins, refill to 2 hosted credits.) You can spend hosted credits to pay trash costs.", "stripped_title": "Scrubber", "text": "2[recurring-credit] <em>(When you install this card and before your turn begins, refill to 2 hosted credits.)</em>\nYou can spend hosted credits to pay trash costs.", "title": "Scrubber", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_xanadu_31012(Resource):
    '''
    Cost: 3
    Text: The rez cost of each piece of ice is increased by 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31012", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Nobles born foolish cared not for their state\nI was left alone weeping\n\u2014Toghon Temur", "illustrator": "Nedliv Audiovisuell", "keywords": "Virtual", "pack_code": "su21", "position": 12, "quantity": 3, "side_code": "runner", "stripped_text": "The rez cost of each piece of ice is increased by 1 credit.", "stripped_title": "Xanadu", "text": "The rez cost of each piece of ice is increased by 1[credit].", "title": "Xanadu", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_security_testing_31024(Resource):
    '''
    Cost: 0
    Text: When your turn begins, you may choose a server. The first time each turn you make a successful run on the chosen server, instead of breaching it, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31024", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "They pay you for the practice run, then you do it again for the real reward.", "illustrator": "Krembler", "keywords": "Job", "pack_code": "su21", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may choose a server. The first time each turn you make a successful run on the chosen server, instead of breaching it, gain 2 credits.", "stripped_title": "Security Testing", "text": "When your turn begins, you may choose a server.\nThe first time each turn you make a successful run on the chosen server, instead of breaching it, gain 2[credit].", "title": "Security Testing", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_aesops_pawnshop_31035(Resource):
    '''
    Cost: 1
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31035", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "If you have something to sell, Aesop is interested in buying. The only detail he won't ask is where you got it.", "illustrator": "Krembler, Alexis Spicer", "keywords": "Connection - Location", "pack_code": "su21", "position": 35, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.", "stripped_title": "Aesop's Pawnshop", "text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3[credit].", "title": "Aesop's Pawnshop", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_professional_contacts_31036(Resource):
    '''
    Cost: 5
    Text: click: Gain 1 credit and draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31036", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "You can hack a social network, but hard work, collaboration, and a sympathetic ear gets you there faster.", "illustrator": "Nedliv Audiovisuell", "keywords": "Connection", "pack_code": "su21", "position": 36, "quantity": 3, "side_code": "runner", "stripped_text": "click: Gain 1 credit and draw 1 card.", "stripped_title": "Professional Contacts", "text": "[click]<strong>:</strong> Gain 1[credit] and draw 1 card.", "title": "Professional Contacts", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_earthrise_hotel_31039(Resource):
    '''
    Cost: 4
    Text: When you install this resource, load 3 power counters onto it. When it is empty, trash it. When your turn begins, remove 1 hosted power counter and draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31039", "cost": 4, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "The best view in the system. Priced accordingly.", "illustrator": "Zoe Cohen", "keywords": "Location - Ritzy", "pack_code": "su21", "position": 39, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 3 power counters onto it. When it is empty, trash it. When your turn begins, remove 1 hosted power counter and draw 2 cards.", "stripped_title": "Earthrise Hotel", "text": "When you install this resource, load 3 power counters onto it. When it is empty, trash it.\nWhen your turn begins, remove 1 hosted power counter and draw 2 cards.", "title": "Earthrise Hotel", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_light_the_fire_32001(Resource):
    '''
    Cost: 1
    Text: click, trash, suffer 1 core damage: Run a remote server. During that run, cards in the root of the attacked server lose all abilities. When that run is successful, trash all cards in the root of the attacked server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "32001", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "A single spark is all it takes...", "illustrator": "Olie Boldador", "keywords": "Sabotage", "pack_code": "msbp", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "click, trash, suffer 1 core damage: Run a remote server. During that run, cards in the root of the attacked server lose all abilities. When that run is successful, trash all cards in the root of the attacked server.", "stripped_title": "Light the Fire!", "text": "[click], [trash], <strong>suffer 1 core damage:</strong> Run a remote server. During that run, cards in the root of the attacked server lose all abilities. When that run is successful, trash all cards in the root of the attacked server.", "title": "Light the Fire!", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_avgustina_ivanovskaya_33008(Resource):
    '''
    Cost: 1
    Text: The first time each turn you install a virus program, sabotage 1. (The Corp trashes 1 card of their choice from HQ or the top of R&D.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33008", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"Sometimes being a union rep calls for action even more... direct.\"", "illustrator": "Dave Lee", "keywords": "Connection", "pack_code": "ms", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you install a virus program, sabotage 1. (The Corp trashes 1 card of their choice from HQ or the top of R&D.)", "stripped_title": "Avgustina Ivanovskaya", "text": "The first time each turn you install a <strong>virus</strong> program, sabotage 1. <em>(The Corp trashes 1 card of their choice from HQ or the top of R&D.)</em>", "title": "Avgustina Ivanovskaya", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_light_the_fire_33009(Resource):
    '''
    Cost: 1
    Text: click, trash, suffer 1 core damage: Run a remote server. During that run, cards in the root of the attacked server lose all abilities. When that run is successful, trash all cards in the root of the attacked server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33009", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "A single spark is all that it takes to destroy billions of credits... or to burn away the rot that ravages our world.", "illustrator": "Olie Boldador", "keywords": "Sabotage", "pack_code": "ms", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "click, trash, suffer 1 core damage: Run a remote server. During that run, cards in the root of the attacked server lose all abilities. When that run is successful, trash all cards in the root of the attacked server.", "stripped_title": "Light the Fire!", "text": "[click], [trash], <strong>suffer 1 core damage:</strong> Run a remote server. During that run, cards in the root of the attacked server lose all abilities. When that run is successful, trash all cards in the root of the attacked server.", "title": "Light the Fire!", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_the_twinning_33010(Resource):
    '''
    Cost: 3
    Text: The first time each turn you spend credits from an installed card, place 1 power counter on this resource. Whenever you breach HQ or R&D, you may remove up to 2 hosted power counters to access that many additional cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33010", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "All is folding back, ever back; together as one.", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "ms", "position": 10, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you spend credits from an installed card, place 1 power counter on this resource. Whenever you breach HQ or R&D, you may remove up to 2 hosted power counters to access that many additional cards.", "stripped_title": "The Twinning", "text": "The first time each turn you spend credits from an installed card, place 1 power counter on this resource.\nWhenever you breach HQ or R&D, you may remove up to 2 hosted power counters to access that many additional cards.", "title": "The Twinning", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_backstitching_33019(Resource):
    '''
    Cost: 2
    Text: When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) Whenever you encounter a piece of ice during a run on your mark, you may trash this resource to bypass that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33019", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "One step back. Take cover. Two steps forward. Repeat, then secure well.", "illustrator": "Adam S. Doyle", "keywords": "Virtual", "pack_code": "ms", "position": 19, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) Whenever you encounter a piece of ice during a run on your mark, you may trash this resource to bypass that ice.", "stripped_title": "Backstitching", "text": "When your turn begins, identify your mark. <em>(If you don\u2019t have a mark, a random central server becomes your mark for this turn.)</em>\nWhenever you encounter a piece of ice during a run on your mark, you may trash this resource to bypass that ice.", "title": "Backstitching", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_no_free_lunch_33020(Resource):
    '''
    Cost: 0
    Text: trash: Gain 3 credits. trash: Remove 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33020", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "If there's anything to be learned from our android cousins, it's that there's no shortcut to perfection. Consider all your options.", "illustrator": "Bruno Balixa", "pack_code": "ms", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Gain 3 credits. trash: Remove 1 tag.", "stripped_title": "No Free Lunch", "text": "[trash]<strong>:</strong> Gain 3[credit].\n[trash]<strong>:</strong> Remove 1 tag.", "title": "No Free Lunch", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_daeg_first_netcat_33028(Resource):
    '''
    Cost: 1
    Text: Whenever an agenda is scored or stolen, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33028", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"That's him at the front, then there's Scout, Jonesy, Parker, Bu\u010da, Squee, Boots... you get the idea.\"", "illustrator": "Cat Shen", "keywords": "Companion - Virtual", "pack_code": "ms", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever an agenda is scored or stolen, you may charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)", "stripped_title": "Daeg, First Net-Cat", "text": "Whenever an agenda is scored or stolen, you may charge 1 of your installed cards. <em>(Add 1 power counter to a card that already has one.)</em>", "title": "Daeg, First Net-Cat", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_environmental_testing_33029(Resource):
    '''
    Cost: 3
    Text: Whenever you install a program or piece of hardware, place 1 power counter on this resource. When there are 4 or more hosted power counters, trash this resource and gain 9 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33029", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Why are we here? No one else is going to do independent testing, that's why.\"\n\u2013Padma Isbister", "illustrator": "Anna Butova", "pack_code": "ms", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you install a program or piece of hardware, place 1 power counter on this resource. When there are 4 or more hosted power counters, trash this resource and gain 9 credits.", "stripped_title": "Environmental Testing", "text": "Whenever you install a program or piece of hardware, place 1 power counter on this resource.\nWhen there are 4 or more hosted power counters, trash this resource and gain 9[credit].", "title": "Environmental Testing", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_stoneship_chart_room_33030(Resource):
    '''
    Cost: 0
    Text: trash: Draw 2 cards. trash: Charge 1 of your installed cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33030", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Every ship is a home, and every home needs a heart.", "illustrator": "Elizaveta Sokolova", "keywords": "Location", "pack_code": "ms", "position": 30, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Draw 2 cards. trash: Charge 1 of your installed cards.", "stripped_title": "Stoneship Chart Room", "text": "[trash]<strong>:</strong> Draw 2 cards.\n[trash]<strong>:</strong> Charge 1 of your installed cards.", "title": "Stoneship Chart Room", "type_code": "resource", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_tsakhia_bankhar_gantulga_33074(Resource):
    '''
    Cost: 1
    Text: When your turn begins, you may choose a server. During the first encounter each turn with a piece of ice protecting the chosen server, whenever the Corp would resolve a subroutine, instead they resolve Subroutine Do 1 net damage..
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33074", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"With these two by my side, I\u02bcve sworn never to fail. I can bear any pain so long as it has meaning.\"", "illustrator": "Dimik", "keywords": "Connection", "pack_code": "ph", "position": 74, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may choose a server. During the first encounter each turn with a piece of ice protecting the chosen server, whenever the Corp would resolve a subroutine, instead they resolve Subroutine Do 1 net damage..", "stripped_title": "Tsakhia Bankhar Gantulga", "text": "When your turn begins, you may choose a server.\nDuring the first encounter each turn with a piece of ice protecting the chosen server, whenever the Corp would resolve a subroutine, instead they resolve \"[subroutine] Do 1 net damage.\".", "title": "Tsakhia \"Bankhar\" Gantulga", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_asmund_pudlat_33082(Resource):
    '''
    Cost: 2
    Text: When you install this resource, search your stack for up to 2 virus or weapon cards with different names. Host those cards faceup on this resource. (They are not installed.) When your turn begins, you may add 1 hosted card to your grip. If there are no more hosted cards, trash this resource.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33082", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Marlon Ruiz", "keywords": "Connection - Seedy", "pack_code": "ph", "position": 82, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, search your stack for up to 2 virus or weapon cards with different names. Host those cards faceup on this resource. (They are not installed.) When your turn begins, you may add 1 hosted card to your grip. If there are no more hosted cards, trash this resource.", "stripped_title": "Asmund Pudlat", "text": "When you install this resource, search your stack for up to 2 <strong>virus</strong> or <strong>weapon</strong> cards with different names. Host those cards faceup on this resource. <em>(They are not installed.)</em>\nWhen your turn begins, you may add 1 hosted card to your grip. If there are no more hosted cards, trash this resource.", "title": "Asmund Pudlat", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_info_bounty_33083(Resource):
    '''
    Cost: 2
    Text: When your turn begins, identify your mark. (If you don't have a mark, a random central server becomes your mark for this turn.) The first time each turn a run on your mark ends, gain 2 credits if you breached that server during that run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33083", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "It was a relief, really, deciding on that one place in the world to definitely never visit again.", "illustrator": "Elliott Birt", "keywords": "Job", "pack_code": "ph", "position": 83, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, identify your mark. (If you don't have a mark, a random central server becomes your mark for this turn.) The first time each turn a run on your mark ends, gain 2 credits if you breached that server during that run.", "stripped_title": "Info Bounty", "text": "When your turn begins, identify your mark. <em>(If you don\u02bct have a mark, a random central server becomes your mark for this turn.)</em>\nThe first time each turn a run on your mark ends, gain 2[credit] if you breached that server during that run.", "title": "Info Bounty", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class resource_dr_nuka_vrolyck_33092(Resource):
    '''
    Cost: 1
    Text: When you install this resource, load 2 power counters onto it. When it is empty, trash it. click, hosted power counter: Draw 3 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33092", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"There is another world under the waves, vanishing as we speak. I want to map it before it\u02bcs gone.\"", "illustrator": "Dave Lee", "keywords": "Connection", "pack_code": "ph", "position": 92, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this resource, load 2 power counters onto it. When it is empty, trash it. click, hosted power counter: Draw 3 cards.", "stripped_title": "Dr. Nuka Vrolyck", "text": "When you install this resource, load 2 power counters onto it. When it is empty, trash it.\n[click], <strong>hosted power counter:</strong> Draw 3 cards.", "title": "Dr. Nuka Vrolyck", "type_code": "resource", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"
