
'''
card classes of type asset
'''
from netrunner_lib.cards._base_card_classes import Asset
from netrunner_lib.game_events import *
from netrunner_lib import errors
from netrunner_lib.tests._test_utilities import *

class asset_adonis_campaign_01056(Asset):
    '''
    Cost: 4
    Text: Put 12 credits from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it. Take 3 credits from Adonis Campaign when your turn begins.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01056", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Mark Anthony Taduran", "keywords": "Advertisement", "pack_code": "core", "position": 56, "quantity": 3, "side_code": "corp", "stripped_text": "Put 12 credits from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it. Take 3 credits from Adonis Campaign when your turn begins.", "stripped_title": "Adonis Campaign", "text": "Put 12[credit] from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it.\nTake 3[credit] from Adonis Campaign when your turn begins.", "title": "Adonis Campaign", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'installed': card successfully installed
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        debug_print(f'playing card: {self.title} || IMPLEMENTED!',1)
        debug_print(f'installing adonis campaign in new remote, state={self.state}',3)
        #call Asset.play()
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            debug_print(f'adonis campaign super result not NOP: {super_result}',3)
            return super_result
        return "BROKEN"
    
    def rez(self, player):
        '''
        rez this card
        INPUT:
            - player:Player(corp) player who installed this card and is currently rezzing it
        '''
        player.credit_pool = player.credit_pool-self.cost
        self.credit_pool = 12
        self.state['rezzed']=True
        debug_print(f'rezzed adonis: credit pool={self.credit_pool}, state={self.state}',3)
        return "rezzed"
    
    def event_start_turn(self, game_state):
        '''
        hook the start of players turn event
        INPUT:
            - game_state:NetrunnerGame current game state object to perform actions upon
        '''
        if self.state['rezzed'] and self.state['installed']:
            self.credit_pool -= 3
            game_state.corpo.credit_pool += 3
            if self.credit_pool <= 0:
                debug_print('adonis campaign asset out of credits, trashing')
                return self.trash(game_state.corpo)
            else:
                return "credits_added"
        else:
            raise errors.CARD_STATE_ERROR(self.state)

class asset_aggressive_secretary_01057(Asset):
    '''
    Cost: 0
    Text: Aggressive Secretary can be advanced. If you pay 2 credits when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01057", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Julian Totino Tedesco", "keywords": "Ambush", "pack_code": "core", "position": 57, "quantity": 2, "side_code": "corp", "stripped_text": "Aggressive Secretary can be advanced. If you pay 2 credits when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.", "stripped_title": "Aggressive Secretary", "text": "Aggressive Secretary can be advanced.\nIf you pay 2[credit] when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.", "title": "Aggressive Secretary", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_project_junebug_01069(Asset):
    '''
    Cost: 0
    Text: Project Junebug can be advanced. If you pay 1 credit when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01069", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "illustrator": "Drew Whitmore", "keywords": "Ambush - Research", "pack_code": "core", "position": 69, "quantity": 3, "side_code": "corp", "stripped_text": "Project Junebug can be advanced. If you pay 1 credit when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.", "stripped_title": "Project Junebug", "text": "Project Junebug can be advanced.\nIf you pay 1[credit] when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.", "title": "Project Junebug", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_snare_01070(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01070", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Alice Duke", "keywords": "Ambush", "pack_code": "core", "position": 70, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.", "stripped_title": "Snare!", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset anywhere except in Archives, you may pay 4[credit]. If you do, give the Runner 1 tag and do 3 net damage.", "title": "Snare!", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_zaibatsu_loyalty_01071(Asset):
    '''
    Cost: 0
    Text: Interrupt -> When a card would be exposed, you may rez this asset. Interrupt -> 1 credit or trash: Prevent 1 card from being exposed.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01071", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "illustrator": "Mike Nesbitt", "pack_code": "core", "position": 71, "quantity": 1, "side_code": "corp", "stripped_text": "Interrupt -> When a card would be exposed, you may rez this asset. Interrupt -> 1 credit or trash: Prevent 1 card from being exposed.", "stripped_title": "Zaibatsu Loyalty", "text": "[interrupt] \u2192 When a card would be exposed, you may rez this asset.\n[interrupt] \u2192 <strong>1[credit]</strong> or <strong>[trash]:</strong> Prevent 1 card from being exposed.", "title": "Zaibatsu Loyalty", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ghost_branch_01087(Asset):
    '''
    Cost: 0
    Text: Ghost Branch can be advanced. When the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01087", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Gong Studios", "keywords": "Ambush - Facility", "pack_code": "core", "position": 87, "quantity": 3, "side_code": "corp", "stripped_text": "Ghost Branch can be advanced. When the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.", "stripped_title": "Ghost Branch", "text": "Ghost Branch can be advanced.\nWhen the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.", "title": "Ghost Branch", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_security_subcontract_01096(Asset):
    '''
    Cost: 0
    Text: click, trash a rezzed piece of ice: Gain 4 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01096", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"Feed the Feds our scraps, and they'll come back begging for more.\" -Richard Polasco, VP of Cyber-Security", "illustrator": "Henning Ludvigsen", "keywords": "Transaction", "pack_code": "core", "position": 96, "quantity": 1, "side_code": "corp", "stripped_text": "click, trash a rezzed piece of ice: Gain 4 credits.", "stripped_title": "Security Subcontract", "text": "[click], <strong>trash a rezzed piece of ice:</strong> Gain 4[credit].", "title": "Security Subcontract", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_melange_mining_corp_01108(Asset):
    '''
    Cost: 1
    Text: click, click, click: Gain 7 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01108", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"The mining bosses are worse than any downstalk crime lords. Tri-Maf, 4K, Yak, I don't care what gangs you got down there. In Heinlein there's just one law: the He3 must flow.\" -\"Old\" Rick Henry, escaped clone.", "illustrator": "Henning Ludvigsen", "pack_code": "core", "position": 108, "quantity": 2, "side_code": "corp", "stripped_text": "click, click, click: Gain 7 credits.", "stripped_title": "Melange Mining Corp.", "text": "[click], [click], [click]: Gain 7[credit].", "title": "Melange Mining Corp.", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_pad_campaign_01109(Asset):
    '''
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01109", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It is like the one you just bought, only better.", "illustrator": "Alexandra Douglass", "keywords": "Advertisement", "pack_code": "core", "position": 109, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, gain 1 credit.", "stripped_title": "PAD Campaign", "text": "When your turn begins, gain 1[credit].", "title": "PAD Campaign", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_encryption_protocol_02029(Asset):
    '''
    Cost: 0
    Text: The trash cost of all installed cards is increased by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02029", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "The key to the future lies in the past.", "illustrator": "Adam S. Doyle", "pack_code": "ta", "position": 29, "quantity": 3, "side_code": "corp", "stripped_text": "The trash cost of all installed cards is increased by 1.", "stripped_title": "Encryption Protocol", "text": "The trash cost of all installed cards is increased by 1.", "title": "Encryption Protocol", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_edge_of_world_02053(Asset):
    '''
    Cost: 0
    Text: When the Runner accesses this asset while it is installed, you may pay 3 credits. If you do, do 1 core damage for each piece of ice protecting this server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02053", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Ambush", "pack_code": "ce", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "When the Runner accesses this asset while it is installed, you may pay 3 credits. If you do, do 1 core damage for each piece of ice protecting this server.", "stripped_title": "Edge of World", "text": "When the Runner accesses this asset while it is installed, you may pay 3[credit]. If you do, do 1 core damage for each piece of ice protecting this server.", "title": "Edge of World", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_marked_accounts_02055(Asset):
    '''
    Cost: 0
    Text: When your turn begins, take 1 credit from Marked Accounts, if able. click: Place 3 credits from the bank on Marked Accounts.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02055", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Mauricio Herrera", "keywords": "Transaction", "pack_code": "ce", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, take 1 credit from Marked Accounts, if able. click: Place 3 credits from the bank on Marked Accounts.", "stripped_title": "Marked Accounts", "text": "When your turn begins, take 1[credit] from Marked Accounts, if able.\n[click]: Place 3[credit] from the bank on Marked Accounts.", "title": "Marked Accounts", "trash_cost": 5, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_private_contracts_02059(Asset):
    '''
    Cost: 3
    Text: Place 14 credits from the bank on Private Contracts when it is rezzed. When there are no credits left on Private Contracts, trash it. click: Take 2 credits from Private Contracts.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02059", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Mauricio Herrera", "keywords": "Transaction", "pack_code": "ce", "position": 59, "quantity": 3, "side_code": "corp", "stripped_text": "Place 14 credits from the bank on Private Contracts when it is rezzed. When there are no credits left on Private Contracts, trash it. click: Take 2 credits from Private Contracts.", "stripped_title": "Private Contracts", "text": "Place 14[credit] from the bank on Private Contracts when it is rezzed. When there are no credits left on Private Contracts, trash it.\n[click]: Take 2[credit] from Private Contracts.", "title": "Private Contracts", "trash_cost": 5, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_dedicated_server_02072(Asset):
    '''
    Cost: 3
    Text: 2 recurring credits Use these credits to rez ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02072", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "so very still, even\ncherry blossoms are not stirred\nby the temple bell\n-Fuhaku", "illustrator": "Emilio Rodriguez", "keywords": "Facility", "pack_code": "asis", "position": 72, "quantity": 3, "side_code": "corp", "stripped_text": "2 recurring credits Use these credits to rez ice.", "stripped_title": "Dedicated Server", "text": "2[recurring-credit]\nUse these credits to rez ice.", "title": "Dedicated Server", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_net_police_02075(Asset):
    '''
    Cost: 1
    Text: X recurring credits Use these credits during traces. X is the number of links the Runner has.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02075", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "This is the net. We work here. We're cops.", "illustrator": "Amelie Hutt", "pack_code": "asis", "position": 75, "quantity": 3, "side_code": "corp", "stripped_text": "X recurring credits Use these credits during traces. X is the number of links the Runner has.", "stripped_title": "Net Police", "text": "X[recurring-credit]\nUse these credits during traces. X is the number of links the Runner has.", "title": "Net Police", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_eve_campaign_02092(Asset):
    '''
    Cost: 5
    Text: Place 16 credits from the bank on Eve Campaign when it is rezzed. When there are no credits left on Eve Campaign, trash it. When your turn begins, take 2 credits from Eve Campaign.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02092", "cost": 5, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Sara K. Diesel", "keywords": "Advertisement", "pack_code": "hs", "position": 92, "quantity": 3, "side_code": "corp", "stripped_text": "Place 16 credits from the bank on Eve Campaign when it is rezzed. When there are no credits left on Eve Campaign, trash it. When your turn begins, take 2 credits from Eve Campaign.", "stripped_title": "Eve Campaign", "text": "Place 16[credit] from the bank on Eve Campaign when it is rezzed. When there are no credits left on Eve Campaign, trash it.\nWhen your turn begins, take 2[credit] from Eve Campaign.", "title": "Eve Campaign", "trash_cost": 5, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ronin_02112(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02112", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "\"I will serve you\u2026for a time.\"", "illustrator": "Adam S. Doyle", "keywords": "Hostile", "pack_code": "fp", "position": 112, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.", "stripped_title": "Ronin", "text": "You can advance this asset.\n[click], [trash]<strong>:</strong> Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.", "title": "Ronin", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_dedicated_response_team_02118(Asset):
    '''
    Cost: 2
    Text: If the Runner is tagged, Dedicated Response Team gains "Whenever a successful run ends, do 2 meat damage."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "02118", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "They don't call them dedicated for nothing.", "illustrator": "Reza Ilyasa", "keywords": "Hostile", "pack_code": "fp", "position": 118, "quantity": 3, "side_code": "corp", "stripped_text": "If the Runner is tagged, Dedicated Response Team gains \"Whenever a successful run ends, do 2 meat damage.\"", "stripped_title": "Dedicated Response Team", "text": "If the Runner is tagged, Dedicated Response Team gains \"Whenever a successful run ends, do 2 meat damage.\"", "title": "Dedicated Response Team", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_alix_t4lb07_03008(Asset):
    '''
    Cost: 1
    Text: Place 1 power counter on Alix T4LB07 whenever you install a card. click,trash: Gain 2 credits for each power counter on Alix T4LB07.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03008", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "The Alix model was based on a successful hedge fund manager but she had a tendency to burn out. Literally.", "illustrator": "Diana Martinez", "keywords": "Bioroid", "pack_code": "cac", "position": 8, "quantity": 3, "side_code": "corp", "stripped_text": "Place 1 power counter on Alix T4LB07 whenever you install a card. click,trash: Gain 2 credits for each power counter on Alix T4LB07.", "stripped_title": "Alix T4LB07", "text": "Place 1 power counter on Alix T4LB07 whenever you install a card.\n[click],[trash]: Gain 2[credit] for each power counter on Alix T4LB07.", "title": "Alix T4LB07", "trash_cost": 2, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_cerebral_overwriter_03009(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. When the Runner accesses this asset while it is installed, you may pay 3 credits. If you do, do 1 core damage for each hosted advancement counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03009", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Ambush", "pack_code": "cac", "position": 9, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. When the Runner accesses this asset while it is installed, you may pay 3 credits. If you do, do 1 core damage for each hosted advancement counter.", "stripped_title": "Cerebral Overwriter", "text": "You can advance this asset.\nWhen the Runner accesses this asset while it is installed, you may pay 3[credit]. If you do, do 1 core damage for each hosted advancement counter.", "title": "Cerebral Overwriter", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_director_haas_03010(Asset):
    '''
    Cost: 3
    Text: You get +1 allotted click for each of your turns. When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03010", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "illustrator": "Matt Zeilinger", "keywords": "Executive", "pack_code": "cac", "position": 10, "quantity": 3, "side_code": "corp", "stripped_text": "You get +1 allotted click for each of your turns. When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.", "stripped_title": "Director Haas", "text": "You get +1 allotted [click] for each of your turns.\nWhen this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.", "title": "Director Haas", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_haas_arcology_ai_03011(Asset):
    '''
    Cost: 2
    Text: Haas Arcology AI can be advanced only while unrezzed. click, hosted advancement token: Gain click click. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03011", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "illustrator": "Aaron Firem", "pack_code": "cac", "position": 11, "quantity": 3, "side_code": "corp", "stripped_text": "Haas Arcology AI can be advanced only while unrezzed. click, hosted advancement token: Gain click click. Use this ability only once per turn.", "stripped_title": "Haas Arcology AI", "text": "Haas Arcology AI can be advanced only while unrezzed.\n[click], <strong>hosted advancement token:</strong> Gain [click][click]. Use this ability only once per turn.", "title": "Haas Arcology AI", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_thomas_haas_03012(Asset):
    '''
    Cost: 1
    Text: Thomas Haas can be advanced. trash: Gain 2 credits for each advancement token on Thomas Haas.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03012", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Thomas, the director's son, has been carefully groomed to inherit the corporation since before he was born. His favorite pastime appears to be disappointing his mother.", "illustrator": "Matt Zeilinger", "keywords": "Executive", "pack_code": "cac", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "Thomas Haas can be advanced. trash: Gain 2 credits for each advancement token on Thomas Haas.", "stripped_title": "Thomas Haas", "text": "Thomas Haas can be advanced.\n[trash]: Gain 2[credit] for each advancement token on Thomas Haas.", "title": "Thomas Haas", "trash_cost": 1, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_levy_university_03024(Asset):
    '''
    Cost: 3
    Text: click, 1 credit: Search R&D for a piece of ice, reveal it, and add it to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03024", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Just another factory, making good corporate drones for the machine. Their CS department is the best in the world, though.\" -g00ru", "illustrator": "Henning Ludvigsen", "keywords": "Ritzy", "pack_code": "cac", "position": 24, "quantity": 3, "side_code": "corp", "stripped_text": "click, 1 credit: Search R&D for a piece of ice, reveal it, and add it to HQ. Shuffle R&D.", "stripped_title": "Levy University", "text": "[click], 1[credit]: Search R&D for a piece of ice, reveal it, and add it to HQ. Shuffle R&D.", "title": "Levy University", "trash_cost": 1, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_server_diagnostics_03025(Asset):
    '''
    Cost: 3
    Text: Gain 2 credits when your turn begins. Trash Server Diagnostics when you install a piece of ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "03025", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"There's only a 5% chance this could result in a general failure.\"", "illustrator": "Anders Finer", "pack_code": "cac", "position": 25, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 2 credits when your turn begins. Trash Server Diagnostics when you install a piece of ice.", "stripped_title": "Server Diagnostics", "text": "Gain 2[credit] when your turn begins.\nTrash Server Diagnostics when you install a piece of ice.", "title": "Server Diagnostics", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_jackson_howard_04015(Asset):
    '''
    Cost: 0
    Text: click: Draw 2 cards. Remove Jackson Howard from the game: Shuffle up to 3 cards from Archives into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04015", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"It is my job to ensure our creations are the perfect companions and edutainment for tomorrow's consumers.\"", "illustrator": "JuanManuel Tumburus", "keywords": "Executive", "pack_code": "om", "position": 15, "quantity": 3, "side_code": "corp", "stripped_text": "click: Draw 2 cards. Remove Jackson Howard from the game: Shuffle up to 3 cards from Archives into R&D.", "stripped_title": "Jackson Howard", "text": "[click]: Draw 2 cards.\n<strong>Remove Jackson Howard from the game:</strong> Shuffle up to 3 cards from Archives into R&D.", "title": "Jackson Howard", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_elizabeth_mills_04037(Asset):
    '''
    Cost: 2
    Text: When you rez Elizabeth Mills, remove 1 bad publicity. click, trash: Trash 1 location. Take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04037", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"It's not personal. Urban renewal is a necessity of the modern world. It's always someone's home, yours is no different.\"", "illustrator": "Del Borovic", "keywords": "Executive", "pack_code": "st", "position": 37, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez Elizabeth Mills, remove 1 bad publicity. click, trash: Trash 1 location. Take 1 bad publicity.", "stripped_title": "Elizabeth Mills", "text": "When you rez Elizabeth Mills, remove 1 bad publicity.\n[click], [trash]: Trash 1 <strong>location</strong>. Take 1 bad publicity.", "title": "Elizabeth Mills", "trash_cost": 1, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_isabel_mcguire_04050(Asset):
    '''
    Cost: 0
    Text: click: Add 1 of your installed cards to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04050", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Even with a virtual ball, it is considered rude not to yell \"Fore!\"", "illustrator": "Matt Zeilinger", "keywords": "Executive", "pack_code": "mt", "position": 50, "quantity": 3, "side_code": "corp", "stripped_text": "click: Add 1 of your installed cards to HQ.", "stripped_title": "Isabel McGuire", "text": "[click]: Add 1 of your installed cards to HQ.", "title": "Isabel McGuire", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_sundew_04054(Asset):
    '''
    Cost: 2
    Text: The first time the Runner spends 1 or more click during their turn, gain 2 credits. If those click were spent to take an action, the first time during that action a run on this server begins, pay 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04054", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "As beautiful as it is dangerous. And it's plenty dangerous.", "illustrator": "Anna Ignatieva", "pack_code": "mt", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "The first time the Runner spends 1 or more click during their turn, gain 2 credits. If those click were spent to take an action, the first time during that action a run on this server begins, pay 2 credits.", "stripped_title": "Sundew", "text": "The first time the Runner spends 1 or more [click] during their turn, gain 2[credit]. If those [click] were spent to take an action, the first time during that action a run on this server begins, pay 2[credit].", "title": "Sundew", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_city_surveillance_04055(Asset):
    '''
    Cost: 5
    Text: When the Runner's turn begins, give them 1 tag unless they pay 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04055", "cost": 5, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "flavor": "Who watches the watcher? Probably another camera.", "illustrator": "Gong Studios", "pack_code": "mt", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "When the Runner's turn begins, give them 1 tag unless they pay 1 credit.", "stripped_title": "City Surveillance", "text": "When the Runner's turn begins, give them 1 tag unless they pay 1[credit].", "title": "City Surveillance", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_rex_campaign_04070(Asset):
    '''
    Cost: 1
    Text: Place 3 power counters on Rex Campaign when it is rezzed. When there are no power counters left on Rex Campaign, trash it and either remove 1 bad publicity or gain 5 credits. When your turn begins, remove 1 power counter from Rex Campaign.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04070", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Shawn Ye Zhongyi", "keywords": "Advertisement", "pack_code": "tc", "position": 70, "quantity": 3, "side_code": "corp", "stripped_text": "Place 3 power counters on Rex Campaign when it is rezzed. When there are no power counters left on Rex Campaign, trash it and either remove 1 bad publicity or gain 5 credits. When your turn begins, remove 1 power counter from Rex Campaign.", "stripped_title": "Rex Campaign", "text": "Place 3 power counters on Rex Campaign when it is rezzed. When there are no power counters left on Rex Campaign, trash it and either remove 1 bad publicity or gain 5[credit].\nWhen your turn begins, remove 1 power counter from Rex Campaign.", "title": "Rex Campaign", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_shock_04073(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04073", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Anna Ignatieva", "keywords": "Ambush", "pack_code": "tc", "position": 73, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, do 1 net damage.", "stripped_title": "Shock!", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset, do 1 net damage.", "title": "Shock!", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_toshiyuki_sakai_04092(Asset):
    '''
    Cost: 0
    Text: Toshiyuki Sakai can be advanced. If Toshiyuki Sakai is accessed while installed, you may swap him with an agenda or asset from HQ. The new agenda or asset is installed unrezzed, and keeps all advancement tokens on Toshiyuki Sakai. The Runner can choose not to access the new card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04092", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "RC Torres", "keywords": "Executive", "pack_code": "fal", "position": 92, "quantity": 3, "side_code": "corp", "stripped_text": "Toshiyuki Sakai can be advanced. If Toshiyuki Sakai is accessed while installed, you may swap him with an agenda or asset from HQ. The new agenda or asset is installed unrezzed, and keeps all advancement tokens on Toshiyuki Sakai. The Runner can choose not to access the new card.", "stripped_title": "Toshiyuki Sakai", "text": "Toshiyuki Sakai can be advanced.\nIf Toshiyuki Sakai is accessed while installed, you may swap him with an agenda or asset from HQ. The new agenda or asset is installed unrezzed, and keeps all advancement tokens on Toshiyuki Sakai. The Runner can choose not to access the new card.", "title": "Toshiyuki Sakai", "trash_cost": 2, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_grndl_refinery_04099(Asset):
    '''
    Cost: 0
    Text: GRNDL Refinery can be advanced. click, trash: Gain 4 credits for each advancement token on GRNDL Refinery.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04099", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "GRNDL refineries process many different rare elements unearthed during the fracking process.", "illustrator": "Emilio Rodriguez", "keywords": "Facility", "pack_code": "fal", "position": 99, "quantity": 3, "side_code": "corp", "stripped_text": "GRNDL Refinery can be advanced. click, trash: Gain 4 credits for each advancement token on GRNDL Refinery.", "stripped_title": "GRNDL Refinery", "text": "GRNDL Refinery can be advanced.\n[click], [trash]: Gain 4[credit] for each advancement token on GRNDL Refinery.", "title": "GRNDL Refinery", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_broadcast_square_04112(Asset):
    '''
    Cost: 2
    Text: Whenever you are about to take at least 1 bad publicity, Trace[3]. If successful, avoid taking the bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "04112", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "Tourists have flocked to Broadcast Square in even greater numbers ever since the notorious Ho-meh's crime spree ended there in a hail of flechettes. Well, that's how it happened in the sensie.", "illustrator": "Henning Ludvigsen", "keywords": "Facility", "pack_code": "dt", "position": 112, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you are about to take at least 1 bad publicity, Trace[3]. If successful, avoid taking the bad publicity.", "stripped_title": "Broadcast Square", "text": "Whenever you are about to take at least 1 bad publicity, Trace[3]. If successful, avoid taking the bad publicity.", "title": "Broadcast Square", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_chairman_hiro_05008(Asset):
    '''
    Cost: 2
    Text: The Runner gets -2 maximum hand size.
When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05008", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 5, "illustrator": "Gong Studios", "keywords": "Executive", "pack_code": "hap", "position": 8, "quantity": 3, "side_code": "corp", "stripped_text": "The Runner gets -2 maximum hand size.\nWhen this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.", "stripped_title": "Chairman Hiro", "text": "The Runner gets -2 maximum hand size.\nWhen this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.", "title": "Chairman Hiro", "trash_cost": 6, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_mental_health_clinic_05009(Asset):
    '''
    Cost: 0
    Text: Gain 1 credit when your turn begins. The Runner's maximum hand size is increased by 1.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05009", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "The whitewashed walls dropped away and a beautiful zen garden appeared. It was all an illusion, but it was a comforting illusion.", "illustrator": "Viktoria Gavrilenko", "keywords": "Facility", "pack_code": "hap", "position": 9, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit when your turn begins. The Runner's maximum hand size is increased by 1.", "stripped_title": "Mental Health Clinic", "text": "Gain 1[credit] when your turn begins.\nThe Runner's maximum hand size is increased by 1.", "title": "Mental Health Clinic", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_psychic_field_05010(Asset):
    '''
    Cost: 0
    Text: If the Runner exposes or accesses Psychic Field while installed, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, do 1 net damage for each card in the Runner's grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05010", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "illustrator": "Seage", "keywords": "Ambush - Psi", "pack_code": "hap", "position": 10, "quantity": 3, "side_code": "corp", "stripped_text": "If the Runner exposes or accesses Psychic Field while installed, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, do 1 net damage for each card in the Runner's grip.", "stripped_title": "Psychic Field", "text": "If the Runner exposes or accesses Psychic Field while installed, you and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, do 1 net damage for each card in the Runner's grip.", "title": "Psychic Field", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_shikyu_05011(Asset):
    '''
    Cost: 0
    Text: When the Runner accesses this asset anywhere except in R&D, you may pay X credits. The Runner must either suffer X net damage or add this asset to their score area as an agenda worth -1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05011", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "illustrator": "Alexandr Elichev", "keywords": "Ambush", "pack_code": "hap", "position": 11, "quantity": 3, "side_code": "corp", "stripped_text": "When the Runner accesses this asset anywhere except in R&D, you may pay X credits. The Runner must either suffer X net damage or add this asset to their score area as an agenda worth -1 agenda point.", "stripped_title": "Shi.Kyu", "text": "When the Runner accesses this asset anywhere except in R&D, you may pay X[credit]. The Runner must either suffer X net damage or add this asset to their score area as an agenda worth -1 agenda point.", "title": "Shi.Ky\u016b", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_tenma_line_05012(Asset):
    '''
    Cost: 2
    Text: click: Swap 2 pieces of installed ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05012", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "The Tenma clones became Jinteki's third highest-grossing line ever due to the rapid urban expansion that occurred after the war. Their unparalleled reaction times, safety records, and punctuality have made them the top choice for shipping and transportation services.", "illustrator": "Smirtouille", "keywords": "Clone", "pack_code": "hap", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "click: Swap 2 pieces of installed ice.", "stripped_title": "Tenma Line", "text": "[click]: Swap 2 pieces of installed ice.", "title": "Tenma Line", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_plan_b_05023(Asset):
    '''
    Cost: 0
    Text: Plan B can be advanced. If the Runner accesses Plan B, you may reveal and score an agenda from HQ with an advancement requirement equal to or less than the number of advancement tokens on Plan B.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "05023", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Gong Studios", "keywords": "Ambush", "pack_code": "hap", "position": 23, "quantity": 3, "side_code": "corp", "stripped_text": "Plan B can be advanced. If the Runner accesses Plan B, you may reveal and score an agenda from HQ with an advancement requirement equal to or less than the number of advancement tokens on Plan B.", "stripped_title": "Plan B", "text": "Plan B can be advanced.\nIf the Runner accesses Plan B, you may reveal and score an agenda from HQ with an advancement requirement equal to or less than the number of advancement tokens on Plan B.", "title": "Plan B", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_primary_transmission_dish_06006(Asset):
    '''
    Cost: 2
    Text: 3 recurring credits Use these credits during traces.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06006", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Works better than a PAD hooked up to a tinfoil umbrella and coffee can.", "illustrator": "Lucas Durham", "keywords": "Beanstalk", "pack_code": "up", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "3 recurring credits Use these credits during traces.", "stripped_title": "Primary Transmission Dish", "text": "3[recurring-credit]\nUse these credits during traces.", "title": "Primary Transmission Dish", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_the_root_06008(Asset):
    '''
    Cost: 6
    Text: 3 recurring credits Use these credits to advance, install, and rez cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06008", "cost": 6, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "They said it couldn't be built. That it was a fantasy. That Jack Weyland was a fool, and he had bought the fools in Washington too. But year after year the buckyweave grew, and 'they' stopped talking.", "illustrator": "Alex Kim", "keywords": "Beanstalk", "pack_code": "up", "position": 8, "quantity": 3, "side_code": "corp", "stripped_text": "3 recurring credits Use these credits to advance, install, and rez cards.", "stripped_title": "The Root", "text": "3[recurring-credit]\nUse these credits to advance, install, and rez cards.", "title": "The Root", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_sealed_vault_06029(Asset):
    '''
    Cost: 0
    Text: 1 credit: Move any number of credits from your credit pool to this asset. click: Take any number of credits from this asset. trash: Take any number of credits from this asset.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06029", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Nothing is impenetrable. The key is to make breaking into it more costly than what it's worth.", "illustrator": "Bruno Balixa", "keywords": "Facility", "pack_code": "tsb", "position": 29, "quantity": 3, "side_code": "corp", "stripped_text": "1 credit: Move any number of credits from your credit pool to this asset. click: Take any number of credits from this asset. trash: Take any number of credits from this asset.", "stripped_title": "Sealed Vault", "text": "<strong>1[credit]:</strong> Move any number of credits from your credit pool to this asset.\n<strong>[click]:</strong> Take any number of credits from this asset.\n<strong>[trash]:</strong> Take any number of credits from this asset.", "title": "Sealed Vault", "trash_cost": 8, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_elizas_toybox_06042(Asset):
    '''
    Cost: 4
    Text: click,click,click: Rez a card, ignoring all costs.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06042", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Eliza's Toybox is the preeminent purveyor of high-class debauchery on the moon, courtesy of its bioroid pleasure models and other exotica. Every fantasy has its price.", "illustrator": "Henning Ludvigsen", "keywords": "Ritzy", "pack_code": "fc", "position": 42, "quantity": 3, "side_code": "corp", "stripped_text": "click,click,click: Rez a card, ignoring all costs.", "stripped_title": "Eliza's Toybox", "text": "[click],[click],[click]: Rez a card, ignoring all costs.", "title": "Eliza's Toybox", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_the_news_now_hour_06045(Asset):
    '''
    Cost: 0
    Text: The Runner cannot play current events.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06045", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"There are reports of a terrorist threat at Starport Kaguya. The NAPD is offering a reward for anyone who can provide them with information about the current whereabouts of the individual pictured here. He is considered extremely dangerous and is armed with a PAD and a portable rig.\"", "illustrator": "Ed Mattinian", "keywords": "Cast", "pack_code": "fc", "position": 45, "quantity": 3, "side_code": "corp", "stripped_text": "The Runner cannot play current events.", "stripped_title": "The News Now Hour", "text": "The Runner cannot play <strong>current</strong> events.", "title": "The News Now Hour", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_shattered_remains_06050(Asset):
    '''
    Cost: 0
    Text: Shattered Remains can be advanced. If you pay 1 credit when the Runner accesses Shattered Remains, trash 1 piece of hardware for each advancement token on Shattered Remains.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06050", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Ambush", "pack_code": "fc", "position": 50, "quantity": 3, "side_code": "corp", "stripped_text": "Shattered Remains can be advanced. If you pay 1 credit when the Runner accesses Shattered Remains, trash 1 piece of hardware for each advancement token on Shattered Remains.", "stripped_title": "Shattered Remains", "text": "Shattered Remains can be advanced.\nIf you pay 1[credit] when the Runner accesses Shattered Remains, trash 1 piece of hardware for each advancement token on Shattered Remains.", "title": "Shattered Remains", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_reversed_accounts_06066(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. click, trash: The Runner loses 4 credits for each hosted advancement counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06066", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Making a name for yourself has its perks. But it also makes you a target.", "illustrator": "Antonio De Luca", "keywords": "Hostile", "pack_code": "uao", "position": 66, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. click, trash: The Runner loses 4 credits for each hosted advancement counter.", "stripped_title": "Reversed Accounts", "text": "You can advance this asset.\n[click], [trash]<strong>:</strong> The Runner loses 4[credit] for each hosted advancement counter.", "title": "Reversed Accounts", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_docklands_crackdown_06072(Asset):
    '''
    Cost: 2
    Text: click, click: Place 1 power counter on Docklands Crackdown. The install cost of the first card the Runner installs each turn is increased by 1 for each power counter on Docklands Crackdown.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06072", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Alex Kim", "pack_code": "uao", "position": 72, "quantity": 3, "side_code": "corp", "stripped_text": "click, click: Place 1 power counter on Docklands Crackdown. The install cost of the first card the Runner installs each turn is increased by 1 for each power counter on Docklands Crackdown.", "stripped_title": "Docklands Crackdown", "text": "[click], [click]: Place 1 power counter on Docklands Crackdown.\nThe install cost of the first card the Runner installs each turn is increased by 1 for each power counter on Docklands Crackdown.", "title": "Docklands Crackdown", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_hostile_infrastructure_06083(Asset):
    '''
    Cost: 5
    Text: Whenever the Runner trashes a Corp card (including Hostile Infrastructure), do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06083", "cost": 5, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"If thou only knowest what it is to conquer, and knowest not what it is to be defeated; woe unto thee\u2026\" -Tokugawa Ieyasu", "illustrator": "Adam S. Doyle", "pack_code": "atr", "position": 83, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner trashes a Corp card (including Hostile Infrastructure), do 1 net damage.", "stripped_title": "Hostile Infrastructure", "text": "Whenever the Runner trashes a Corp card (including Hostile Infrastructure), do 1 net damage.", "title": "Hostile Infrastructure", "trash_cost": 5, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_daily_business_show_06086(Asset):
    '''
    Cost: 2
    Text: Interrupt -> The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06086", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"A new investment deal every morning! Grab the bull by the horns and take control of your future!\"", "illustrator": "Gong Studios", "keywords": "Cast", "pack_code": "atr", "position": 86, "quantity": 3, "side_code": "corp", "stripped_text": "Interrupt -> The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.", "stripped_title": "Daily Business Show", "text": "[interrupt] \u2192 The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.", "title": "Daily Business Show", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_executive_boot_camp_06088(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may rez a card, lowering the rez cost by 1 credit. 1 credit,trash: Search R&D for an asset, reveal it, and add it to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06088", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"Do it again, but this time I want to see you to enunciate less. Maybe let some spittle fly.\"", "illustrator": "Gong Studios", "pack_code": "atr", "position": 88, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may rez a card, lowering the rez cost by 1 credit. 1 credit,trash: Search R&D for an asset, reveal it, and add it to HQ. Shuffle R&D.", "stripped_title": "Executive Boot Camp", "text": "When your turn begins, you may rez a card, lowering the rez cost by 1[credit].\n1[credit],[trash]: Search R&D for an asset, reveal it, and add it to HQ. Shuffle R&D.", "title": "Executive Boot Camp", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_it_department_06103(Asset):
    '''
    Cost: 2
    Text: click: Place 1 power counter on IT Department. Hosted power counter: Choose a rezzed piece of ice. That ice has +1 strength until the end of the turn for each power counter (including the one spent) on IT Department.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06103", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "illustrator": "Adam Schumpert", "pack_code": "ts", "position": 103, "quantity": 3, "side_code": "corp", "stripped_text": "click: Place 1 power counter on IT Department. Hosted power counter: Choose a rezzed piece of ice. That ice has +1 strength until the end of the turn for each power counter (including the one spent) on IT Department.", "stripped_title": "IT Department", "text": "[click]: Place 1 power counter on IT Department.\n<strong>Hosted power counter:</strong> Choose a rezzed piece of ice. That ice has +1 strength until the end of the turn for each power counter (including the one spent) on IT Department.", "title": "IT Department", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_turtlebacks_06106(Asset):
    '''
    Cost: 2
    Text: Gain 1 credit whenever you create a server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "06106", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "A masterpiece of cloning and hardware technology, Jinteki created homo vacuo operae, commonly called \"turtlebacks\", to operate for long periods of time within a vacuum.", "illustrator": "Yip Lee", "keywords": "Clone", "pack_code": "ts", "position": 106, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit whenever you create a server.", "stripped_title": "Turtlebacks", "text": "Gain 1[credit] whenever you create a server.", "title": "Turtlebacks", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_constellation_protocol_07008(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may move an advancement token from a piece of ice to an installed piece of ice that can be advanced.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07008", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"With distributed systems, assets can be realigned with no loss of efficiency.\" -William Knuth, The Tower of Babbage", "illustrator": "Adam S. Doyle", "pack_code": "oac", "position": 8, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may move an advancement token from a piece of ice to an installed piece of ice that can be advanced.", "stripped_title": "Constellation Protocol", "text": "When your turn begins, you may move an advancement token from a piece of ice to an installed piece of ice that can be advanced.", "title": "Constellation Protocol", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_mark_yale_07009(Asset):
    '''
    Cost: 1
    Text: Whenever you spend an agenda counter, gain 1 credit. trash or any agenda counter: Gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07009", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"This is a one-of-a-kind opportunity\u2026\"", "illustrator": "Ralph Beisner", "keywords": "Executive", "pack_code": "oac", "position": 9, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you spend an agenda counter, gain 1 credit. trash or any agenda counter: Gain 2 credits.", "stripped_title": "Mark Yale", "text": "Whenever you spend an agenda counter, gain 1[credit].\n[trash] or <strong>any agenda counter:</strong> Gain 2[credit].", "title": "Mark Yale", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_space_camp_07010(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, you may place 1 advancement counter on an installed card you can advance.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07010", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Future leaders start here.", "illustrator": "Matt Zeilinger", "keywords": "Ambush", "pack_code": "oac", "position": 10, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, you may place 1 advancement counter on an installed card you can advance.", "stripped_title": "Space Camp", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset, you may place 1 advancement counter on an installed card you can advance.", "title": "Space Camp", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_the_board_07011(Asset):
    '''
    Cost: 3
    Text: Each agenda in the Runner's score area is worth 1 less agenda point. When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "07011", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 5, "flavor": "No one on the board knows everyone on it.", "illustrator": "Maciej Rebisz", "keywords": "Executive", "pack_code": "oac", "position": 11, "quantity": 3, "side_code": "corp", "stripped_text": "Each agenda in the Runner's score area is worth 1 less agenda point. When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.", "stripped_title": "The Board", "text": "Each agenda in the Runner's score area is worth 1 less agenda point.\nWhen this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.", "title": "The Board", "trash_cost": 7, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_braintaping_warehouse_08010(Asset):
    '''
    Cost: 1
    Text: The rez cost of bioroid ice is lowered by 1 for each unspent click the Runner has.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08010", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "In the vast universe of memories, consciousness slumbers...", "illustrator": "Maciej Rebisz", "keywords": "Facility", "pack_code": "val", "position": 10, "quantity": 3, "side_code": "corp", "stripped_text": "The rez cost of bioroid ice is lowered by 1 for each unspent click the Runner has.", "stripped_title": "Brain-Taping Warehouse", "text": "The rez cost of <strong>bioroid</strong> ice is lowered by 1 for each unspent click the Runner has.", "title": "Brain-Taping Warehouse", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_capital_investors_08018(Asset):
    '''
    Cost: 2
    Text: click: Gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08018", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "Give a man money, and he is rich for a day. Teach a man how to invest, and he is rich for life.", "illustrator": "Lili Ibrahim", "pack_code": "val", "position": 18, "quantity": 3, "side_code": "corp", "stripped_text": "click: Gain 2 credits.", "stripped_title": "Capital Investors", "text": "[click]: Gain 2[credit].", "title": "Capital Investors", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_tech_startup_08020(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may trash Tech Startup. If you do, search R&D for an asset, reveal it, and install it. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08020", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Don't worry. If this one fails, we can start a new one tomorrow.\"", "illustrator": "Del Borovic", "pack_code": "val", "position": 20, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may trash Tech Startup. If you do, search R&D for an asset, reveal it, and install it. Shuffle R&D.", "stripped_title": "Tech Startup", "text": "When your turn begins, you may trash Tech Startup. If you do, search R&D for an asset, reveal it, and install it. Shuffle R&D.", "title": "Tech Startup", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_blacklist_08036(Asset):
    '''
    Cost: 0
    Text: Cards cannot leave the Runner's heap for any reason.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08036", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Officially, there is no blacklist. That would be illegal. Unofficially, there is a list, and being on it can ruin a career.", "illustrator": "Matthew Szydlik", "pack_code": "bb", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "Cards cannot leave the Runner's heap for any reason.", "stripped_title": "Blacklist", "text": "Cards cannot leave the Runner's heap for any reason.", "title": "Blacklist", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_student_loans_08038(Asset):
    '''
    Cost: 2
    Text: As an additional cost to play an event, if there is a copy of that event in the heap, the Runner must pay 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08038", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "The cost of an education is sometimes felt sharpest in the stomach.", "illustrator": "Mushk Rizvi", "pack_code": "bb", "position": 38, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to play an event, if there is a copy of that event in the heap, the Runner must pay 2 credits.", "stripped_title": "Student Loans", "text": "As an additional cost to play an event, if there is a copy of that event in the heap, the Runner must pay 2[credit].", "title": "Student Loans", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_corporate_town_08059(Asset):
    '''
    Cost: 1
    Text: As an additional cost to rez this asset, forfeit 1 agenda. When your turn begins, you may trash 1 installed resource. Trashing a resource this way cannot be prevented.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08059", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "If you can't buy the city council, create a new city.", "illustrator": "Matt Zeilinger", "pack_code": "cc", "position": 59, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to rez this asset, forfeit 1 agenda. When your turn begins, you may trash 1 installed resource. Trashing a resource this way cannot be prevented.", "stripped_title": "Corporate Town", "text": "As an additional cost to rez this asset, forfeit 1 agenda.\nWhen your turn begins, you may trash 1 installed resource. Trashing a resource this way cannot be prevented.", "title": "Corporate Town", "trash_cost": 5, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_test_ground_08071(Asset):
    '''
    Cost: 0
    Text: Test Ground can be advanced. trash: Derez 1 card for each advancement token on Test Ground.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08071", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Isn't this wrong?\"\n\"Not legally. They didn't read the fine print.\"", "illustrator": "Sam Lamont", "pack_code": "uw", "position": 71, "quantity": 3, "side_code": "corp", "stripped_text": "Test Ground can be advanced. trash: Derez 1 card for each advancement token on Test Ground.", "stripped_title": "Test Ground", "text": "Test Ground can be advanced.\n[trash]: Derez 1 card for each advancement token on Test Ground.", "title": "Test Ground", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_allele_repression_08073(Asset):
    '''
    Cost: 2
    Text: Allele Repression can be advanced. trash: Swap 1 card in HQ with 1 card in Archives for each advancement token on Allele Repression.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08073", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "JB Casacop", "pack_code": "uw", "position": 73, "quantity": 3, "side_code": "corp", "stripped_text": "Allele Repression can be advanced. trash: Swap 1 card in HQ with 1 card in Archives for each advancement token on Allele Repression.", "stripped_title": "Allele Repression", "text": "Allele Repression can be advanced.\n[trash]: Swap 1 card in HQ with 1 card in Archives for each advancement token on Allele Repression.", "title": "Allele Repression", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_expose_08075(Asset):
    '''
    Cost: 2
    Text: Expose can be advanced. trash: Remove 1 bad publicity for each advancement token on Expose.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08075", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Is your neighbor secretly a violent criminal? The answer to this chilling question and more, right after the break.\" -Shannon Claire, SSN 5", "illustrator": "Sara K. Diesel", "pack_code": "uw", "position": 75, "quantity": 3, "side_code": "corp", "stripped_text": "Expose can be advanced. trash: Remove 1 bad publicity for each advancement token on Expose.", "stripped_title": "Expose", "text": "Expos\u00e9 can be advanced.\n[trash]: Remove 1 bad publicity for each advancement token on Expos\u00e9.", "title": "Expos\u00e9", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_contract_killer_08078(Asset):
    '''
    Cost: 2
    Text: Contract Killer can be advanced. If there are at least 2 advancement tokens on Contract Killer, it gains: "click, trash: Trash a connection or do 2 meat damage."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08078", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "\"You want no questions asked, hire someone else. I have two: who and how much?\"", "illustrator": "Clark Huggins", "keywords": "Hostile", "pack_code": "uw", "position": 78, "quantity": 3, "side_code": "corp", "stripped_text": "Contract Killer can be advanced. If there are at least 2 advancement tokens on Contract Killer, it gains: \"click, trash: Trash a connection or do 2 meat damage.\"", "stripped_title": "Contract Killer", "text": "Contract Killer can be advanced.\nIf there are at least 2 advancement tokens on Contract Killer, it gains: \"[click], [trash]: Trash a <strong>connection</strong> or do 2 meat damage.\"", "title": "Contract Killer", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ronald_five_08088(Asset):
    '''
    Cost: 3
    Text: Whenever the Runner trashes a Corp card (including this asset), they lose click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08088", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"It's our most pirated property ever. Great work, everyone.\"", "illustrator": "Smirtouille", "keywords": "Bioroid", "pack_code": "oh", "position": 88, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner trashes a Corp card (including this asset), they lose click.", "stripped_title": "Ronald Five", "text": "Whenever the Runner trashes a Corp card <em>(including this asset)</em>, they lose [click].", "title": "Ronald Five", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_early_premiere_08095(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may pay 1 credit. If you do, place 1 advancement counter on a card you can advance in the root of a server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08095", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Antonio De Luca", "pack_code": "oh", "position": 95, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may pay 1 credit. If you do, place 1 advancement counter on a card you can advance in the root of a server.", "stripped_title": "Early Premiere", "text": "When your turn begins, you may pay 1[credit]. If you do, place 1 advancement counter on a card you can advance in the root of a server.", "title": "Early Premiere", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_cybernetics_court_08109(Asset):
    '''
    Cost: 0
    Text: Your maximum hand size is increased by 4.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08109", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "flavor": "The Cybernetics Court has seven floors of attractions. The plasteel used to construct it was even more expensive than the thousands of cybernetic implants displayed inside.", "illustrator": "Andreas Zafiratos", "keywords": "Facility - Ritzy", "pack_code": "uot", "position": 109, "quantity": 3, "side_code": "corp", "stripped_text": "Your maximum hand size is increased by 4.", "stripped_title": "Cybernetics Court", "text": "Your maximum hand size is increased by 4.", "title": "Cybernetics Court", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_team_sponsorship_08110(Asset):
    '''
    Cost: 1
    Text: Whenever you score an agenda, you may install a card from Archives or HQ, ignoring the install cost.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08110", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "The SanSan Outlaws have a close relationship with Haas-Bioroid's sports engineering division, SHIFT.", "illustrator": "Mike Nesbitt", "pack_code": "uot", "position": 110, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you score an agenda, you may install a card from Archives or HQ, ignoring the install cost.", "stripped_title": "Team Sponsorship", "text": "Whenever you score an agenda, you may install a card from Archives or HQ, ignoring the install cost.", "title": "Team Sponsorship", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_genetics_pavilion_08113(Asset):
    '''
    Cost: 1
    Text: The Runner cannot draw more than 2 cards during each of their turns.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08113", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 5, "flavor": "The Genetics Pavilion was designed by renowned architect Meru Mati II. It was built without the aid of bioroids, instead relying on human and clone labor.", "illustrator": "Greg Semkow", "keywords": "Facility - Ritzy", "pack_code": "uot", "position": 113, "quantity": 3, "side_code": "corp", "stripped_text": "The Runner cannot draw more than 2 cards during each of their turns.", "stripped_title": "Genetics Pavilion", "text": "The Runner cannot draw more than 2 cards during each of their turns.", "title": "Genetics Pavilion", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_franchise_city_08114(Asset):
    '''
    Cost: 3
    Text: While the Runner is accessing an agenda in R&D, they must reveal it. When the Runner accesses an agenda, add this asset to your score area as an agenda worth 1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08114", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 5, "flavor": "There are over 20,000 brands represented in Franchise City, all of them owned by fewer than 100 corps.", "illustrator": "Maciej Rebisz", "keywords": "Facility", "pack_code": "uot", "position": 114, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing an agenda in R&D, they must reveal it. When the Runner accesses an agenda, add this asset to your score area as an agenda worth 1 agenda point.", "stripped_title": "Franchise City", "text": "While the Runner is accessing an agenda in R&D, they must reveal it.\nWhen the Runner accesses an agenda, add this asset to your score area as an agenda worth 1 agenda point.", "title": "Franchise City", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_worlds_plaza_08116(Asset):
    '''
    Cost: 2
    Text: Worlds Plaza can host up to 3 assets. click: Install an asset from HQ on Worlds Plaza and rez it, lowering its rez cost by 2, if able.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08116", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 5, "flavor": "The holosculpture depicts the three inhabited worlds. The square can hold almost 1% of their total population.", "illustrator": "Maciej Rebisz", "keywords": "Facility", "pack_code": "uot", "position": 116, "quantity": 3, "side_code": "corp", "stripped_text": "Worlds Plaza can host up to 3 assets. click: Install an asset from HQ on Worlds Plaza and rez it, lowering its rez cost by 2, if able.", "stripped_title": "Worlds Plaza", "text": "Worlds Plaza can host up to 3 assets.\n[click]: Install an asset from HQ on Worlds Plaza and rez it, lowering its rez cost by 2, if able.", "title": "Worlds Plaza", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_public_support_08117(Asset):
    '''
    Cost: 2
    Text: Place 3 power counters on Public Support when it is rezzed. When there are no power counters left on Public Support, add it to your score area as an agenda worth 1 agenda point. When your turn begins, remove 1 power counter from Public Support.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "08117", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Wenjuinn Png", "pack_code": "uot", "position": 117, "quantity": 3, "side_code": "corp", "stripped_text": "Place 3 power counters on Public Support when it is rezzed. When there are no power counters left on Public Support, add it to your score area as an agenda worth 1 agenda point. When your turn begins, remove 1 power counter from Public Support.", "stripped_title": "Public Support", "text": "Place 3 power counters on Public Support when it is rezzed. When there are no power counters left on Public Support, add it to your score area as an agenda worth 1 agenda point.\nWhen your turn begins, remove 1 power counter from Public Support.", "title": "Public Support", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_lily_lockwell_09008(Asset):
    '''
    Cost: 2
    Text: When you rez Lily Lockwell, draw 3 cards. click, remove 1 tag: Search R&D for an operation, reveal it, and shuffle the rest of R&D. Add the operation to the top of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09008", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "flavor": "\"Live from New Angeles, this is Lily Lockwell.\"", "illustrator": "Matt Zeilinger", "keywords": "Character", "pack_code": "dad", "position": 8, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez Lily Lockwell, draw 3 cards. click, remove 1 tag: Search R&D for an operation, reveal it, and shuffle the rest of R&D. Add the operation to the top of R&D.", "stripped_title": "Lily Lockwell", "text": "When you rez Lily Lockwell, draw 3 cards.\n[click], <strong>remove 1 tag:</strong> Search R&D for an operation, reveal it, and shuffle the rest of R&D. Add the operation to the top of R&D.", "title": "Lily Lockwell", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_news_team_09009(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, they must either take 2 tags or add this asset to their score area as an agenda worth -1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09009", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Jessada Sutthi", "keywords": "Ambush", "pack_code": "dad", "position": 9, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, they must either take 2 tags or add this asset to their score area as an agenda worth -1 agenda point.", "stripped_title": "News Team", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset, they must either take 2 tags or add this asset to their score area as an agenda worth -1 agenda point.", "title": "News Team", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_shannon_claire_09010(Asset):
    '''
    Cost: 0
    Text: click: Draw 1 card from the bottom of R&D. trash: Search R&D or Archives for an agenda and reveal it. Shuffle the rest of R&D if you searched it. Add the agenda to the bottom of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09010", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "No one can bury a story better.", "illustrator": "Rebecca Sorge", "keywords": "Character", "pack_code": "dad", "position": 10, "quantity": 3, "side_code": "corp", "stripped_text": "click: Draw 1 card from the bottom of R&D. trash: Search R&D or Archives for an agenda and reveal it. Shuffle the rest of R&D if you searched it. Add the agenda to the bottom of R&D.", "stripped_title": "Shannon Claire", "text": "[click]: Draw 1 card from the bottom of R&D.\n[trash]: Search R&D or Archives for an agenda and reveal it. Shuffle the rest of R&D if you searched it. Add the agenda to the bottom of R&D.", "title": "Shannon Claire", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_victoria_jenkins_09011(Asset):
    '''
    Cost: 3
    Text: The Runner gets -1 allotted click for each of their turns. When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09011", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 5, "illustrator": "Matt Zeilinger", "keywords": "Executive", "pack_code": "dad", "position": 11, "quantity": 3, "side_code": "corp", "stripped_text": "The Runner gets -1 allotted click for each of their turns. When this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.", "stripped_title": "Victoria Jenkins", "text": "The Runner gets -1 allotted [click] for each of their turns.\nWhen this asset is trashed from anywhere while being accessed, add it to the Runner's score area as an agenda worth 2 agenda points.", "title": "Victoria Jenkins", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_reality_threedee_09012(Asset):
    '''
    Cost: 0
    Text: When you rez Reality Threedee, take 1 bad publicity. When your turn begins, gain 1 credit (or 2 credits if the Runner is tagged).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09012", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"They're gonna try and make you a star. Whether you want it or not.\" -MaxX", "illustrator": "Kate Laird", "keywords": "Illicit", "pack_code": "dad", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez Reality Threedee, take 1 bad publicity. When your turn begins, gain 1 credit (or 2 credits if the Runner is tagged).", "stripped_title": "Reality Threedee", "text": "When you rez Reality Threedee, take 1 bad publicity.\nWhen your turn begins, gain 1[credit] (or 2[credit] if the Runner is tagged).", "title": "Reality Threedee", "trash_cost": 6, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_launch_campaign_09027(Asset):
    '''
    Cost: 1
    Text: Place 6 credits from the bank on Launch Campaign when it is rezzed. When there are no credits left on Launch Campaign, trash it. When your turn begins, take 2 credits from Launch Campaign.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "09027", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Elisabeth Alba", "keywords": "Advertisement", "pack_code": "dad", "position": 27, "quantity": 3, "side_code": "corp", "stripped_text": "Place 6 credits from the bank on Launch Campaign when it is rezzed. When there are no credits left on Launch Campaign, trash it. When your turn begins, take 2 credits from Launch Campaign.", "stripped_title": "Launch Campaign", "text": "Place 6[credit] from the bank on Launch Campaign when it is rezzed. When there are no credits left on Launch Campaign, trash it.\nWhen your turn begins, take 2[credit] from Launch Campaign.", "title": "Launch Campaign", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_kala_ghoda_real_tv_10015(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may look at the top card of the stack. trash: The Runner trashes the top card of the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10015", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"A new property has two, maybe three hours. If it doesn't sell, cut it and move on.\"", "illustrator": "St\u00e9phane Gantiez", "keywords": "Cast", "pack_code": "kg", "position": 15, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may look at the top card of the stack. trash: The Runner trashes the top card of the stack.", "stripped_title": "Kala Ghoda Real TV", "text": "When your turn begins, you may look at the top card of the stack.\n<strong>[trash]:</strong> The Runner trashes the top card of the stack.", "title": "Kala Ghoda Real TV", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_mumba_temple_10018(Asset):
    '''
    Cost: 1
    Text: This card costs 0 influence if you have 15 or fewer ice in your deck. 2 recurring credits Use these credits to rez cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10018", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 2, "flavor": "Those who are the wisest know the least.", "illustrator": "Yog Joshi", "keywords": "Alliance - Facility", "pack_code": "kg", "position": 18, "quantity": 3, "side_code": "corp", "stripped_text": "This card costs 0 influence if you have 15 or fewer ice in your deck. 2 recurring credits Use these credits to rez cards.", "stripped_title": "Mumba Temple", "text": "This card costs 0 influence if you have 15 or fewer ice in your deck.\n2[recurring-credit]\nUse these credits to rez cards.", "title": "Mumba Temple", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_museum_of_history_10019(Asset):
    '''
    Cost: 1
    Text: This asset costs 0 influence if you have 50 or more cards in your deck. When your turn begins, you may shuffle 1 card from Archives into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10019", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 2, "flavor": "\"And here we see the Polar Bear, once the largest land carnivore on Earth.\"", "illustrator": "Sander Mosk", "keywords": "Alliance - Ritzy", "pack_code": "kg", "position": 19, "quantity": 3, "side_code": "corp", "stripped_text": "This asset costs 0 influence if you have 50 or more cards in your deck. When your turn begins, you may shuffle 1 card from Archives into R&D.", "stripped_title": "Museum of History", "text": "This asset costs 0 influence if you have 50 or more cards in your deck.\nWhen your turn begins, you may shuffle 1 card from Archives into R&D.", "title": "Museum of History", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_advanced_assembly_lines_10027(Asset):
    '''
    Cost: 1
    Text: When you rez Advanced Assembly Lines, gain 3 credits. trash: Install a non-agenda card from HQ (paying the install cost). You cannot use this ability during a run.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10027", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Johan T\u00f6rnlund", "keywords": "Facility", "pack_code": "bf", "position": 27, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez Advanced Assembly Lines, gain 3 credits. trash: Install a non-agenda card from HQ (paying the install cost). You cannot use this ability during a run.", "stripped_title": "Advanced Assembly Lines", "text": "When you rez Advanced Assembly Lines, gain 3[credit].\n[trash]: Install a non-agenda card from HQ (paying the install cost). You cannot use this ability during a run.", "title": "Advanced Assembly Lines", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_lakshmi_smartfabrics_10028(Asset):
    '''
    Cost: 1
    Text: Whenever you rez a card, place 1 power counter on Lakshmi Smartfabrics. X hosted power counters: Reveal an agenda worth X points from HQ. The Runner cannot steal copies of that agenda for the remainder of this turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10028", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Caleb Souza", "pack_code": "bf", "position": 28, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you rez a card, place 1 power counter on Lakshmi Smartfabrics. X hosted power counters: Reveal an agenda worth X points from HQ. The Runner cannot steal copies of that agenda for the remainder of this turn.", "stripped_title": "Lakshmi Smartfabrics", "text": "Whenever you rez a card, place 1 power counter on Lakshmi Smartfabrics.\n<strong>X hosted power counters:</strong> Reveal an agenda worth X points from HQ. The Runner cannot steal copies of that agenda for the remainder of this turn.", "title": "Lakshmi Smartfabrics", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_palana_agroplex_10031(Asset):
    '''
    Cost: 1
    Text: When your turn begins, each player draws 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10031", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Expensive to build but dramatically more efficient than traditional farming, agroplexes are emblems of the inevitable corporatization of the food industry.\u00a0", "illustrator": "Emilio Rodriguez", "keywords": "Facility", "pack_code": "bf", "position": 31, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, each player draws 1 card.", "stripped_title": "Palana Agroplex", "text": "When your turn begins, each player draws 1 card.\u00a0", "title": "P\u0101lan\u0101 Agroplex", "trash_cost": 5, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_mumbad_construction_co_10036(Asset):
    '''
    Cost: 4
    Text: When your turn begins, place 1 advancement token on Mumbad Construction Co. 2 credits: Move 1 advancement token from Mumbad Construction Co. to a faceup card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10036", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Simon Weaner", "pack_code": "bf", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, place 1 advancement token on Mumbad Construction Co. 2 credits: Move 1 advancement token from Mumbad Construction Co. to a faceup card.", "stripped_title": "Mumbad Construction Co.", "text": "When your turn begins, place 1 advancement token on Mumbad Construction Co.\n2[credit]: Move 1 advancement token from Mumbad Construction Co. to a faceup card.", "title": "Mumbad Construction Co.", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_pad_factory_10038(Asset):
    '''
    Cost: 2
    Text: This card costs 0 influence if you have 3 PAD Campaigns in your deck. click: Place 1 advancement token on a card. You cannot score that card until your next turn begins.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10038", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 2, "illustrator": "Caleb Souza", "keywords": "Alliance - Facility", "pack_code": "bf", "position": 38, "quantity": 3, "side_code": "corp", "stripped_text": "This card costs 0 influence if you have 3 PAD Campaigns in your deck. click: Place 1 advancement token on a card. You cannot score that card until your next turn begins.", "stripped_title": "PAD Factory", "text": "This card costs 0 influence if you have 3 PAD Campaigns in your deck.\n[click]: Place 1 advancement token on a card. You cannot score that card until your next turn begins.", "title": "PAD Factory", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_clone_suffrage_movement_10049(Asset):
    '''
    Cost: 1
    Text: When your turn begins, you may add 1 operation from Archives to HQ if there is no ice protecting this server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10049", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Our research says the public views clones as more human than bioroids. Historically, this has been a liability. Let's make it a strength.\"", "illustrator": "Patricia Smith", "keywords": "Political", "pack_code": "dag", "position": 49, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may add 1 operation from Archives to HQ if there is no ice protecting this server.", "stripped_title": "Clone Suffrage Movement", "text": "When your turn begins, you may add 1 operation from Archives to HQ if there is no ice protecting this server.", "title": "Clone Suffrage Movement", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_bioethics_association_10050(Asset):
    '''
    Cost: 1
    Text: When your turn begins, do 1 net damage if there is no ice protecting this server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10050", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"There's no conflict of interest here. These are complex issues with highly technical minutiae. It's only natural that the experts should lay down the guidelines.\"", "illustrator": "Natalie Bernard", "keywords": "Political", "pack_code": "dag", "position": 50, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, do 1 net damage if there is no ice protecting this server.", "stripped_title": "Bio-Ethics Association", "text": "When your turn begins, do 1 net damage if there is no ice protecting this server.", "title": "Bio-Ethics Association", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_political_dealings_10051(Asset):
    '''
    Cost: 4
    Text: Whenever you draw an agenda, you may reveal and install it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10051", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "\"Politics is a dirty business. But so is business.\" -Krishnan Sareen", "illustrator": "VIKO", "keywords": "Seedy", "pack_code": "dag", "position": 51, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you draw an agenda, you may reveal and install it.", "stripped_title": "Political Dealings", "text": "Whenever you draw an agenda, you may reveal and install it.", "title": "Political Dealings", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_sensie_actors_union_10053(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may draw 3 cards if there is no ice protecting this server. If you do, add 1 card from HQ to the bottom of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10053", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Being a Mumbad sensie star means a glamorous life, though it is lived in constant fear of blackmail-or worse-from orgcrime.", "illustrator": "Crystal Ben", "keywords": "Political", "pack_code": "dag", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may draw 3 cards if there is no ice protecting this server. If you do, add 1 card from HQ to the bottom of R&D.", "stripped_title": "Sensie Actors Union", "text": "When your turn begins, you may draw 3 cards if there is no ice protecting this server. If you do, add 1 card from HQ to the bottom of R&D.", "title": "Sensie Actors Union", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_commercial_bankers_group_10054(Asset):
    '''
    Cost: 1
    Text: When your turn begins, gain 3 credits if there is no ice protecting this server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10054", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"Money is speech and I am listening intently.\" -Krishnan Sareen", "illustrator": "Timur Shevtsov", "keywords": "Political", "pack_code": "dag", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, gain 3 credits if there is no ice protecting this server.", "stripped_title": "Commercial Bankers Group", "text": "When your turn begins, gain 3[credit] if there is no ice protecting this server.", "title": "Commercial Bankers Group", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_mumbad_city_hall_10055(Asset):
    '''
    Cost: 1
    Text: click: Search R&D for an alliance card, reveal it, and play or install it (paying all costs). Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10055", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Mumbad's public city corporation is tightly connected to all the other corporations.", "illustrator": "Maciej Rebisz", "keywords": "Facility - Government", "pack_code": "dag", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "click: Search R&D for an alliance card, reveal it, and play or install it (paying all costs). Shuffle R&D.", "stripped_title": "Mumbad City Hall", "text": "[click]: Search R&D for an <strong>alliance</strong> card, reveal it, and play or install it (paying all costs). Shuffle R&D.", "title": "Mumbad City Hall", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_jeeves_model_bioroids_10067(Asset):
    '''
    Cost: 2
    Text: This card costs 0 influence if you have 6 or more non-alliance haas-bioroid cards in your deck. The first time you spend 3click on the same action each turn, gain click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10067", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"Very good, sir.\"", "illustrator": "St\u00e9phane Gantiez", "keywords": "Alliance", "pack_code": "si", "position": 67, "quantity": 3, "side_code": "corp", "stripped_text": "This card costs 0 influence if you have 6 or more non-alliance haas-bioroid cards in your deck. The first time you spend 3click on the same action each turn, gain click.", "stripped_title": "Jeeves Model Bioroids", "text": "This card costs 0 influence if you have 6 or more non-<strong>alliance</strong> [haas-bioroid] cards in your deck.\nThe first time you spend 3[click] on the same action each turn, gain [click].", "title": "Jeeves Model Bioroids", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_raman_rai_10068(Asset):
    '''
    Cost: 1
    Text: This asset costs 0 influence if you have 6 or more non-alliance jinteki cards in your deck. Whenever you draw a card, you may lose click. If you do, reveal that card and 1 card in Archives of the same type. Swap those cards. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10068", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Kate Laird", "keywords": "Alliance - Executive", "pack_code": "si", "position": 68, "quantity": 3, "side_code": "corp", "stripped_text": "This asset costs 0 influence if you have 6 or more non-alliance jinteki cards in your deck. Whenever you draw a card, you may lose click. If you do, reveal that card and 1 card in Archives of the same type. Swap those cards. Use this ability only once per turn.", "stripped_title": "Raman Rai", "text": "This asset costs 0 influence if you have 6 or more non-<strong>alliance</strong> [jinteki] cards in your deck.\nWhenever you draw a card, you may lose [click]. If you do, reveal that card and 1 card in Archives of the same type. Swap those cards. Use this ability only once per turn.", "title": "Raman Rai", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_aryabhata_tech_10070(Asset):
    '''
    Cost: 2
    Text: Whenever there is a successful trace, gain 1 credit and the Runner loses 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10070", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"As the world shrinks, communications becomes the most essential technology.\" -Ramesh Gupta, One World Economy", "illustrator": "Yog Joshi", "keywords": "Ritzy", "pack_code": "si", "position": 70, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever there is a successful trace, gain 1 credit and the Runner loses 1 credit.", "stripped_title": "Aryabhata Tech", "text": "Whenever there is a successful trace, gain 1[credit] and the Runner loses 1[credit].", "title": "Aryabhata Tech", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_executive_search_firm_10072(Asset):
    '''
    Cost: 0
    Text: This card costs 0 influence if you have 6 or more non-alliance weyland-consortium cards in your deck. click: Search R&D for an executive, sysop, or character, reveal it, and add it to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10072", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Diana Martinez", "keywords": "Alliance - Ritzy", "pack_code": "si", "position": 72, "quantity": 3, "side_code": "corp", "stripped_text": "This card costs 0 influence if you have 6 or more non-alliance weyland-consortium cards in your deck. click: Search R&D for an executive, sysop, or character, reveal it, and add it to HQ. Shuffle R&D.", "stripped_title": "Executive Search Firm", "text": "This card costs 0 influence if you have 6 or more non-<strong>alliance</strong> [weyland-consortium] cards in your deck.\n[click]: Search R&D for an <strong>executive</strong>, <strong>sysop</strong>, or <strong>character</strong>, reveal it, and add it to HQ. Shuffle R&D.", "title": "Executive Search Firm", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_indian_union_stock_exchange_10073(Asset):
    '''
    Cost: 1
    Text: Whenever you rez or play an out-of-faction card (including Indian Union Stock Exchange), gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10073", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"Wealth wisely invested is wealth earned.\" -The New Gospel of Wealth", "illustrator": "Yog Joshi", "pack_code": "si", "position": 73, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you rez or play an out-of-faction card (including Indian Union Stock Exchange), gain 1 credit.", "stripped_title": "Indian Union Stock Exchange", "text": "Whenever you rez or play an out-of-faction card (including Indian Union Stock Exchange), gain 1[credit].", "title": "Indian Union Stock Exchange", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_full_immersion_recstudio_10108(Asset):
    '''
    Cost: 2
    Text: Full Immersion RecStudio can host up to 2 assets and/or agendas. The trash cost of Full Immersion RecStudio is increased by 3 for each card hosted on it.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10108", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "flavor": "The costumes aren't strictly necessary, but they improve the performances of the vactors and sensie stars.", "illustrator": "Maciej Rebisz", "keywords": "Facility", "pack_code": "ftm", "position": 108, "quantity": 3, "side_code": "corp", "stripped_text": "Full Immersion RecStudio can host up to 2 assets and/or agendas. The trash cost of Full Immersion RecStudio is increased by 3 for each card hosted on it.", "stripped_title": "Full Immersion RecStudio", "text": "Full Immersion RecStudio can host up to 2 assets and/or agendas.\nThe trash cost of Full Immersion RecStudio is increased by 3 for each card hosted on it.", "title": "Full Immersion RecStudio", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ibrahim_salem_10109(Asset):
    '''
    Cost: 2
    Text: This card costs 0 influence if you have 6 or more non-alliance nbn cards in your deck. As an additional cost to rez Ibrahim Salem, forfeit an agenda. When your turn begins, name a card type. Look at the Runner's grip and trash 1 card in it of the named type.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10109", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Jessada Sutthi", "keywords": "Alliance - Character", "pack_code": "ftm", "position": 109, "quantity": 3, "side_code": "corp", "stripped_text": "This card costs 0 influence if you have 6 or more non-alliance nbn cards in your deck. As an additional cost to rez Ibrahim Salem, forfeit an agenda. When your turn begins, name a card type. Look at the Runner's grip and trash 1 card in it of the named type.", "stripped_title": "Ibrahim Salem", "text": "This card costs 0 influence if you have 6 or more non-<strong>alliance</strong> [nbn] cards in your deck.\nAs an additional cost to rez Ibrahim Salem, forfeit an agenda.\nWhen your turn begins, name a card type. Look at the Runner's grip and trash 1 card in it of the named type.", "title": "Ibrahim Salem", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_zealous_judge_10111(Asset):
    '''
    Cost: 2
    Text: Zealous Judge can only be rezzed if the Runner is tagged. click, 1 credit: Give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "10111", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Micah Epstein", "keywords": "Character", "pack_code": "ftm", "position": 111, "quantity": 3, "side_code": "corp", "stripped_text": "Zealous Judge can only be rezzed if the Runner is tagged. click, 1 credit: Give the Runner 1 tag.", "stripped_title": "Zealous Judge", "text": "Zealous Judge can only be rezzed if the Runner is tagged.\n[click], 1[credit]: Give the Runner 1 tag.", "title": "Zealous Judge", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_hyoubu_research_facility_11012(Asset):
    '''
    Cost: 0
    Text: The first time each turn you reveal secretly spent credits, gain that many credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11012", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "\"I'm telling you, free up the emergency accounts. Something's coming; I haven't seen a reaction like that since the tsunami. My god, the screaming...\"", "illustrator": "Marya Yartseva", "keywords": "Facility", "pack_code": "23s", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn you reveal secretly spent credits, gain that many credits.", "stripped_title": "Hyoubu Research Facility", "text": "The first time each turn you reveal secretly spent credits, gain that many credits.", "title": "Hyoubu Research Facility", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_watchdog_11015(Asset):
    '''
    Cost: 0
    Text: The rez cost of the first piece of ice you rez each turn is lowered by 1 for each tag the Runner has.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11015", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"Person of interest. Noun. Someone who is about to get ****ed by a corp.\" - Anarch's Dictionary, Volume Who's Counting", "illustrator": "Sam Guay", "pack_code": "23s", "position": 15, "quantity": 3, "side_code": "corp", "stripped_text": "The rez cost of the first piece of ice you rez each turn is lowered by 1 for each tag the Runner has.", "stripped_title": "Watchdog", "text": "The rez cost of the first piece of ice you rez each turn is lowered by 1 for each tag the Runner has.", "title": "Watchdog", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_sandburg_11020(Asset):
    '''
    Cost: 0
    Text: If you have at least 10 credits, each piece of ice has +1 strength for every 5 credits in your credit pool.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11020", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Money is power.", "illustrator": "Pavel Kolomeyets", "pack_code": "23s", "position": 20, "quantity": 3, "side_code": "corp", "stripped_text": "If you have at least 10 credits, each piece of ice has +1 strength for every 5 credits in your credit pool.", "stripped_title": "Sandburg", "text": "If you have at least 10[credit], each piece of ice has +1 strength for every 5[credit] in your credit pool.", "title": "Sandburg", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ci_fund_11036(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may move up to 3 credits from your credit pool to C.I. Fund. When your turn begins, place 2 credits on C.I. Fund from the bank if there are at least 6 credits on it. 2 credits,trash: Take all credits from C.I. Fund.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11036", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "illustrator": "Samuel Leung", "pack_code": "bm", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may move up to 3 credits from your credit pool to C.I. Fund. When your turn begins, place 2 credits on C.I. Fund from the bank if there are at least 6 credits on it. 2 credits,trash: Take all credits from C.I. Fund.", "stripped_title": "C.I. Fund", "text": "When your turn begins, you may move up to 3[credit] from your credit pool to C.I. Fund.\nWhen your turn begins, place 2[credit] on C.I. Fund from the bank if there are at least 6[credit] on it.\n2[credit],[trash]: Take all credits from C.I. Fund.", "title": "C.I. Fund", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_alexa_belsky_11055(Asset):
    '''
    Cost: 1
    Text: trash: Shuffle all cards in HQ into R&D. The Runner may pay any number of credits to prevent 1 random card in HQ from being shuffled into R&D for every 2 credits spent.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11055", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"She used to work for me at my chop shop. Now she makes more money than I do.\" -MacPherson", "illustrator": "Kate Laird", "keywords": "Character", "pack_code": "es", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "trash: Shuffle all cards in HQ into R&D. The Runner may pay any number of credits to prevent 1 random card in HQ from being shuffled into R&D for every 2 credits spent.", "stripped_title": "Alexa Belsky", "text": "[trash]: Shuffle all cards in HQ into R&D. The Runner may pay any number of credits to prevent 1 random card in HQ from being shuffled into R&D for every 2[credit] spent.", "title": "Alexa Belsky", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_fumiko_yamamori_11073(Asset):
    '''
    Cost: 4
    Text: Whenever you and the Runner reveal secretly spent credits, do 1 meat damage if you and the Runner spent a different number of credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11073", "cost": 4, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"Does an alliance with the yakuza truly seem so strange? They are honorable businessmen, and women, just like us.\" -Rin Kimura, Chief NA Security", "illustrator": "Kate Laird", "keywords": "Character", "pack_code": "in", "position": 73, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you and the Runner reveal secretly spent credits, do 1 meat damage if you and the Runner spent a different number of credits.", "stripped_title": "Fumiko Yamamori", "text": "Whenever you and the Runner reveal secretly spent credits, do 1 meat damage if you and the Runner spent a different number of credits.", "title": "Fumiko Yamamori", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_chief_slee_11077(Asset):
    '''
    Cost: 2
    Text: Whenever an encounter with a piece of ice ends, place 1 power counter on Chief Slee for each unbroken subroutine on the encountered piece of ice. click, 5 hosted power counters: Do 5 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11077", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Caitlin Yarsky", "keywords": "Character", "pack_code": "in", "position": 77, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever an encounter with a piece of ice ends, place 1 power counter on Chief Slee for each unbroken subroutine on the encountered piece of ice. click, 5 hosted power counters: Do 5 meat damage.", "stripped_title": "Chief Slee", "text": "Whenever an encounter with a piece of ice ends, place 1 power counter on Chief Slee for each unbroken subroutine on the encountered piece of ice.\n[click], <strong>5 hosted power counters</strong>: Do 5 meat damage.", "title": "Chief Slee", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_anson_rose_11096(Asset):
    '''
    Cost: 1
    Text: When your turn begins, place 1 advancement token on Anson Rose. Whenever you rez a piece of ice, you may move any number of advancement tokens from Anson Rose to that ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11096", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"I don't get paid to be calm.\"", "illustrator": "Marko Fiedler", "keywords": "Executive", "pack_code": "ml", "position": 96, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, place 1 advancement token on Anson Rose. Whenever you rez a piece of ice, you may move any number of advancement tokens from Anson Rose to that ice.", "stripped_title": "Anson Rose", "text": "When your turn begins, place 1 advancement token on Anson Rose.\nWhenever you rez a piece of ice, you may move any number of advancement tokens from Anson Rose to that ice.", "title": "Anson Rose", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_nasx_11118(Asset):
    '''
    Cost: 2
    Text: Gain 1 credit when your turn begins. Whenever you gain credits through a card ability other than from NASX, you may spend up to 2 credits to place that many power counters on NASX. click,trash: Gain 2 credits for each power counter on NASX.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "11118", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "pack_code": "qu", "position": 118, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit when your turn begins. Whenever you gain credits through a card ability other than from NASX, you may spend up to 2 credits to place that many power counters on NASX. click,trash: Gain 2 credits for each power counter on NASX.", "stripped_title": "NASX", "text": "Gain 1[credit] when your turn begins.\nWhenever you gain credits through a card ability other than from NASX, you may spend up to 2[credit] to place that many power counters on NASX.\n[click],[trash]: Gain 2[credit] for each power counter on NASX.", "title": "NASX", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_synth_dna_modification_12012(Asset):
    '''
    Cost: 2
    Text: The first time a subroutine on a piece of AP ice is broken each turn, do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12012", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "illustrator": "Liiga Smilshkalne", "pack_code": "dc", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "The first time a subroutine on a piece of AP ice is broken each turn, do 1 net damage.", "stripped_title": "Synth DNA Modification", "text": "The first time a subroutine on a piece of <strong>AP</strong> ice is broken each turn, do 1 net damage.", "title": "Synth DNA Modification", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_net_analytics_12014(Asset):
    '''
    Cost: 0
    Text: Whenever the Runner avoids or removes 1 or more tags, you may draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12014", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Mariusz Siergiejew", "pack_code": "dc", "position": 14, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner avoids or removes 1 or more tags, you may draw 1 card.", "stripped_title": "Net Analytics", "text": "Whenever the Runner avoids or removes 1 or more tags, you may draw 1 card.", "title": "Net Analytics", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_quarantine_system_12017(Asset):
    '''
    Cost: 1
    Text: Forfeit an agenda: Rez up to 3 pieces of ice, lowering the cost of each by 2 credits for each printed agenda point on the forfeited agenda.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12017", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "Kathryn Steele", "pack_code": "dc", "position": 17, "quantity": 3, "side_code": "corp", "stripped_text": "Forfeit an agenda: Rez up to 3 pieces of ice, lowering the cost of each by 2 credits for each printed agenda point on the forfeited agenda.", "stripped_title": "Quarantine System", "text": "<strong>Forfeit an agenda</strong>: Rez up to 3 pieces of ice, lowering the cost of each by 2[credit] for each printed agenda point on the forfeited agenda.", "title": "Quarantine System", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_cpc_generator_12034(Asset):
    '''
    Cost: 0
    Text: The first time the Runner spends click to gain 1 credit each turn (not through a card effect), gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12034", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"The customer pays to use our service, and then the advertisers pay us to put ads on their screens, and then the customers pay us a premium to remove the ads. Welcome to the dream.\"", "illustrator": "Andreas Zafiratos", "keywords": "Advertisement", "pack_code": "so", "position": 34, "quantity": 3, "side_code": "corp", "stripped_text": "The first time the Runner spends click to gain 1 credit each turn (not through a card effect), gain 1 credit.", "stripped_title": "CPC Generator", "text": "The first time the Runner spends [click] to gain 1[credit] each turn (not through a card effect), gain 1[credit].", "title": "CPC Generator", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_clyde_van_rite_12037(Asset):
    '''
    Cost: 2
    Text: When your turn begins, the Runner must pay 1 credit or trash the top card of the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12037", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"You have two choices: do what I asked, or make me ask again. It's your choice, but if I have to ask again, it will go badly for you.\"", "illustrator": "Anna Edwards", "keywords": "Executive", "pack_code": "so", "position": 37, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, the Runner must pay 1 credit or trash the top card of the stack.", "stripped_title": "Clyde Van Rite", "text": "When your turn begins, the Runner must pay 1[credit] or trash the top card of the stack.", "title": "Clyde Van Rite", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_bioroid_work_crew_12051(Asset):
    '''
    Cost: 2
    Text: trash: Install 1 card from HQ. Use this ability only during the next paid ability window after playing and resolving an operation.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12051", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "\"They don't need sleep, breaks, overtime, or even O\u2082. How can we compete with that!?\"", "illustrator": "Monztre", "keywords": "Bioroid", "pack_code": "eas", "position": 51, "quantity": 3, "side_code": "corp", "stripped_text": "trash: Install 1 card from HQ. Use this ability only during the next paid ability window after playing and resolving an operation.", "stripped_title": "Bioroid Work Crew", "text": "<strong>[trash]:</strong> Install 1 card from HQ. Use this ability only during the next paid ability window after playing and resolving an operation.", "title": "Bioroid Work Crew", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_whampoa_reclamation_12079(Asset):
    '''
    Cost: 3
    Text: Trash 1 card from HQ: Add 1 card from Archives to the bottom of R&D. Use this ability only once per turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12079", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 2, "flavor": "\"Whampoa is the largest and meanest Earth-based mining concern on Mars. They put bodies and waste in the ground as fast as they pull minerals out.\" - Alice Merchant", "illustrator": "James Ives", "keywords": "Corporation", "pack_code": "baw", "position": 79, "quantity": 3, "side_code": "corp", "stripped_text": "Trash 1 card from HQ: Add 1 card from Archives to the bottom of R&D. Use this ability only once per turn.", "stripped_title": "Whampoa Reclamation", "text": "<strong>Trash 1 card from HQ:</strong> Add 1 card from Archives to the bottom of R&D. Use this ability only once per turn.", "title": "Whampoa Reclamation", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_open_forum_12097(Asset):
    '''
    Cost: 1
    Text: After your mandatory draw, reveal the top card of R&D and add it to HQ. Add 1 card from HQ to the top of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12097", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"Please, speak freely. I've been tasked by the board itself to hear your grievances.\"\n-Mandy Traut", "illustrator": "Lale Ann", "pack_code": "fm", "position": 97, "quantity": 3, "side_code": "corp", "stripped_text": "After your mandatory draw, reveal the top card of R&D and add it to HQ. Add 1 card from HQ to the top of R&D.", "stripped_title": "Open Forum", "text": "After your mandatory draw, reveal the top card of R&D and add it to HQ. Add 1 card from HQ to the top of R&D.", "title": "Open Forum", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_mca_austerity_policy_12111(Asset):
    '''
    Cost: 1
    Text: click: Place 1 power counter on this asset. When the Runner's next turn begins, they lose click. Use this ability only once per turn. click, trash, 3 hosted power counters: Gain click click click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12111", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Pavel Kolomeyets", "pack_code": "cd", "position": 111, "quantity": 3, "side_code": "corp", "stripped_text": "click: Place 1 power counter on this asset. When the Runner's next turn begins, they lose click. Use this ability only once per turn. click, trash, 3 hosted power counters: Gain click click click click.", "stripped_title": "MCA Austerity Policy", "text": "<strong>[click]:</strong> Place 1 power counter on this asset. When the Runner's next turn begins, they lose [click]. Use this ability only once per turn.\n[click],[trash], <strong>3 hosted power counters:</strong> Gain [click][click][click][click].", "title": "MCA Austerity Policy", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_breached_dome_12113(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, do 1 meat damage and trash the top card of the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "12113", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Nasrul Hakim", "keywords": "Ambush", "pack_code": "cd", "position": 113, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, do 1 meat damage and trash the top card of the stack.", "stripped_title": "Breached Dome", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset, do 1 meat damage and trash the top card of the stack.", "title": "Breached Dome", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_estelle_moon_13032(Asset):
    '''
    Cost: 2
    Text: Whenever you install a card in the root of a remote server, place 1 power counter on this asset. trash: For each power counter on this asset, gain 2 credits and draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13032", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Dmitry Prosvirnin", "keywords": "Executive", "pack_code": "td", "position": 32, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you install a card in the root of a remote server, place 1 power counter on this asset. trash: For each power counter on this asset, gain 2 credits and draw 1 card.", "stripped_title": "Estelle Moon", "text": "Whenever you install a card in the root of a remote server, place 1 power counter on this asset.\n<strong>[trash]:</strong> For each power counter on this asset, gain 2[credit] and draw 1 card.", "title": "Estelle Moon", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_marilyn_campaign_13033(Asset):
    '''
    Cost: 2
    Text: When you rez this asset, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this asset. Interrupt -> When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. (It is still considered trashed.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13033", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "illustrator": "Tim Durning", "keywords": "Advertisement", "pack_code": "td", "position": 33, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this asset, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this asset. Interrupt -> When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. (It is still considered trashed.)", "stripped_title": "Marilyn Campaign", "text": "When you rez this asset, load 8[credit] onto it. When it is empty, trash it.\nWhen your turn begins, take 2[credit] from this asset.\n[interrupt] \u2192 When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. <em>(It is still considered trashed.)</em>", "title": "Marilyn Campaign", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_illegal_arms_factory_13045(Asset):
    '''
    Cost: 3
    Text: If the Runner trashes Illegal Arms Factory while it is installed, take 1 bad publicity. When your turn begins, gain 1 credit and draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13045", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Jason Juta", "keywords": "Facility - Illicit", "pack_code": "td", "position": 45, "quantity": 3, "side_code": "corp", "stripped_text": "If the Runner trashes Illegal Arms Factory while it is installed, take 1 bad publicity. When your turn begins, gain 1 credit and draw 1 card.", "stripped_title": "Illegal Arms Factory", "text": "If the Runner trashes Illegal Arms Factory while it is installed, take 1 bad publicity.\nWhen your turn begins, gain 1[credit] and draw 1 card.", "title": "Illegal Arms Factory", "trash_cost": 6, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_mr_stone_13046(Asset):
    '''
    Cost: 2
    Text: Whenever the Runner takes 1 or more tags, do 1 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13046", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "\"VP of Retirements and Pensions? So is that HR or Accounting?\"\n\"Both.\"", "illustrator": "Matt Zeilinger", "keywords": "Executive", "pack_code": "td", "position": 46, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner takes 1 or more tags, do 1 meat damage.", "stripped_title": "Mr. Stone", "text": "Whenever the Runner takes 1 or more tags, do 1 meat damage.", "title": "Mr. Stone", "trash_cost": 2, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_honeyfarm_13054(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, they lose 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13054", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Pavel Kolomeyets", "keywords": "Ambush", "pack_code": "td", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, they lose 1 credit.", "stripped_title": "Honeyfarm", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset, they lose 1[credit].", "title": "Honeyfarm", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_longterm_investment_13055(Asset):
    '''
    Cost: 2
    Text: When your turn begins, place 2 credits on Long-Term Investment. If there are at least 8 credits on Long-Term Investment, it gains "click: Take any number of credits from Long-Term Investment."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "13055", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Mark Molnar", "pack_code": "td", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, place 2 credits on Long-Term Investment. If there are at least 8 credits on Long-Term Investment, it gains \"click: Take any number of credits from Long-Term Investment.\"", "stripped_title": "Long-Term Investment", "text": "When your turn begins, place 2[credit] on Long-Term Investment. If there are at least 8[credit] on Long-Term Investment, it gains \"[click]: Take any number of credits from Long-Term Investment.\"", "title": "Long-Term Investment", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_investigator_inez_delgado_a_14004(Asset):
    '''
    Cost: 0
    Text: Whenever you score an agenda, you may swap it with an agenda in the Runner's score area worth at least 1 point, then resolve the "when scored" ability on that agenda.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14004", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "PxelSlayer", "keywords": "Character", "pack_code": "tdc", "position": 5, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you score an agenda, you may swap it with an agenda in the Runner's score area worth at least 1 point, then resolve the \"when scored\" ability on that agenda.", "stripped_title": "Investigator Inez Delgado A", "text": "Whenever you score an agenda, you may swap it with an agenda in the Runner's score area worth at least 1 point, then resolve the \"when scored\" ability on that agenda.", "title": "Investigator Inez Delgado A", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_investigator_inez_delgado_a_2_14005(Asset):
    '''
    Cost: 0
    Text: Whenever the Runner steals an agenda, you may resolve the "when scored" ability on that agenda, then swap it with an agenda in your scored area.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14005", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "PxelSlayer", "keywords": "Character", "pack_code": "tdc", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner steals an agenda, you may resolve the \"when scored\" ability on that agenda, then swap it with an agenda in your scored area.", "stripped_title": "Investigator Inez Delgado A 2", "text": "Whenever the Runner steals an agenda, you may resolve the \"when scored\" ability on that agenda, then swap it with an agenda in your scored area.", "title": "Investigator Inez Delgado A 2", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_lt_todachine_14006(Asset):
    '''
    Cost: 3
    Text: Whenever you rez a piece of ice, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14006", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Antonio Jos\u00e9 Manzanedo", "keywords": "Character", "pack_code": "tdc", "position": 7, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you rez a piece of ice, give the Runner 1 tag.", "stripped_title": "Lt. Todachine", "text": "Whenever you rez a piece of ice, give the Runner 1 tag.", "title": "Lt. Todachine", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_lt_todachine_2_14007(Asset):
    '''
    Cost: 3
    Text: Whenever you rez a piece of ice, give the Runner 1 tag. Whenever the Runner accesses cards, he or she accesses 1 fewer card if he or she is tagged (to a minimum of 1 card).
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14007", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Antonio Jos\u00e9 Manzanedo", "keywords": "Character", "pack_code": "tdc", "position": 8, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you rez a piece of ice, give the Runner 1 tag. Whenever the Runner accesses cards, he or she accesses 1 fewer card if he or she is tagged (to a minimum of 1 card).", "stripped_title": "Lt. Todachine 2", "text": "Whenever you rez a piece of ice, give the Runner 1 tag.\nWhenever the Runner accesses cards, he or she accesses 1 fewer card if he or she is tagged (to a minimum of 1 card).", "title": "Lt. Todachine 2", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_trojan_14008(Asset):
    '''
    Cost: 0
    Text: If Trojan is accessed from R&D, then Runner must reveal it. When the Runner accesses Trojan, lose 2 credits, trash 1 card from HQ at random, and destroy Trojan. Ignore this ability if the Runner accesses Trojan from Archives.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "14008", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Ethan Patrick Harris", "pack_code": "tdc", "position": 9, "quantity": 3, "side_code": "corp", "stripped_text": "If Trojan is accessed from R&D, then Runner must reveal it. When the Runner accesses Trojan, lose 2 credits, trash 1 card from HQ at random, and destroy Trojan. Ignore this ability if the Runner accesses Trojan from Archives.", "stripped_title": "Trojan", "text": "If Trojan is accessed from R&D, then Runner must reveal it.\nWhen the Runner accesses Trojan, lose 2[credit], trash 1 card from HQ at random, and destroy Trojan. Ignore this ability if the Runner accesses Trojan from Archives.", "title": "Trojan", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_adonis_campaign_20064(Asset):
    '''
    Cost: 4
    Text: Put 12 credits from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it. Take 3 credits from Adonis Campaign when your turn begins.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20064", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Mark Anthony Taduran", "keywords": "Advertisement", "pack_code": "core2", "position": 64, "quantity": 3, "side_code": "corp", "stripped_text": "Put 12 credits from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it. Take 3 credits from Adonis Campaign when your turn begins.", "stripped_title": "Adonis Campaign", "text": "Put 12[credit] from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it.\nTake 3[credit] from Adonis Campaign when your turn begins.", "title": "Adonis Campaign", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_aggressive_secretary_20065(Asset):
    '''
    Cost: 0
    Text: Aggressive Secretary can be advanced. If you pay 2 credits when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20065", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Julian Totino Tedesco", "keywords": "Ambush", "pack_code": "core2", "position": 65, "quantity": 1, "side_code": "corp", "stripped_text": "Aggressive Secretary can be advanced. If you pay 2 credits when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.", "stripped_title": "Aggressive Secretary", "text": "Aggressive Secretary can be advanced.\nIf you pay 2[credit] when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.", "title": "Aggressive Secretary", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_dedicated_response_team_20081(Asset):
    '''
    Cost: 2
    Text: If the Runner is tagged, Dedicated Response Team gains "Whenever a successful run ends, do 2 meat damage."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20081", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "They don't call them dedicated for nothing.", "illustrator": "Reza Ilyasa", "keywords": "Hostile", "pack_code": "core2", "position": 112, "quantity": 1, "side_code": "corp", "stripped_text": "If the Runner is tagged, Dedicated Response Team gains \"Whenever a successful run ends, do 2 meat damage.\"", "stripped_title": "Dedicated Response Team", "text": "If the Runner is tagged, Dedicated Response Team gains \"Whenever a successful run ends, do 2 meat damage.\"", "title": "Dedicated Response Team", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_elizabeth_mills_20082(Asset):
    '''
    Cost: 2
    Text: When you rez Elizabeth Mills, remove 1 bad publicity. click, trash: Trash 1 location. Take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20082", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"It's not personal. Urban renewal is a necessity of the modern world. It's always someone's home, yours is no different.\"", "illustrator": "Del Borovic", "keywords": "Executive", "pack_code": "core2", "position": 113, "quantity": 1, "side_code": "corp", "stripped_text": "When you rez Elizabeth Mills, remove 1 bad publicity. click, trash: Trash 1 location. Take 1 bad publicity.", "stripped_title": "Elizabeth Mills", "text": "When you rez Elizabeth Mills, remove 1 bad publicity.\n[click], [trash]: Trash 1 <strong>location</strong>. Take 1 bad publicity.", "title": "Elizabeth Mills", "trash_cost": 1, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_grndl_refinery_20083(Asset):
    '''
    Cost: 0
    Text: GRNDL Refinery can be advanced. click, trash: Gain 4 credits for each advancement token on GRNDL Refinery.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20083", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "GRNDL refineries process many different rare elements unearthed during the fracking process.", "illustrator": "Emilio Rodriguez", "keywords": "Facility", "pack_code": "core2", "position": 114, "quantity": 3, "side_code": "corp", "stripped_text": "GRNDL Refinery can be advanced. click, trash: Gain 4 credits for each advancement token on GRNDL Refinery.", "stripped_title": "GRNDL Refinery", "text": "GRNDL Refinery can be advanced.\n[click], [trash]: Gain 4[credit] for each advancement token on GRNDL Refinery.", "title": "GRNDL Refinery", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_project_junebug_20096(Asset):
    '''
    Cost: 0
    Text: Project Junebug can be advanced. If you pay 1 credit when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20096", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "illustrator": "Drew Whitmore", "keywords": "Ambush - Research", "pack_code": "core2", "position": 80, "quantity": 2, "side_code": "corp", "stripped_text": "Project Junebug can be advanced. If you pay 1 credit when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.", "stripped_title": "Project Junebug", "text": "Project Junebug can be advanced.\nIf you pay 1[credit] when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.", "title": "Project Junebug", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ronin_20097(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20097", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "\"I will serve you\u2026for a time.\"", "illustrator": "Adam S. Doyle", "keywords": "Hostile", "pack_code": "core2", "position": 81, "quantity": 1, "side_code": "corp", "stripped_text": "You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.", "stripped_title": "Ronin", "text": "You can advance this asset.\n[click], [trash]<strong>:</strong> Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.", "title": "Ronin", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_snare_20098(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20098", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Alice Duke", "keywords": "Ambush", "pack_code": "core2", "position": 82, "quantity": 2, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.", "stripped_title": "Snare!", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset anywhere except in Archives, you may pay 4[credit]. If you do, give the Runner 1 tag and do 3 net damage.", "title": "Snare!", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ghost_branch_20112(Asset):
    '''
    Cost: 0
    Text: Ghost Branch can be advanced. When the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20112", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Emilio Rodriguez", "keywords": "Ambush - Facility", "pack_code": "core2", "position": 96, "quantity": 1, "side_code": "corp", "stripped_text": "Ghost Branch can be advanced. When the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.", "stripped_title": "Ghost Branch", "text": "Ghost Branch can be advanced.\nWhen the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.", "title": "Ghost Branch", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_melange_mining_corp_20127(Asset):
    '''
    Cost: 1
    Text: click, click, click: Gain 7 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20127", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"The mining bosses are worse than any downstalk crime lords. Tri-Maf, 4K, Yak, I don't care what gangs you got down there. In Heinlein there's just one law: the He3 must flow.\" -\"Old\" Rick Henry, escaped clone.", "illustrator": "Emilio Rodriguez", "pack_code": "core2", "position": 127, "quantity": 2, "side_code": "corp", "stripped_text": "click, click, click: Gain 7 credits.", "stripped_title": "Melange Mining Corp.", "text": "[click], [click], [click]: Gain 7[credit].", "title": "Melange Mining Corp.", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_pad_campaign_20128(Asset):
    '''
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "20128", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It is just like the one you just bought, only better.", "illustrator": "Kate Laird", "keywords": "Advertisement", "pack_code": "core2", "position": 128, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, gain 1 credit.", "stripped_title": "PAD Campaign", "text": "When your turn begins, gain 1[credit].", "title": "PAD Campaign", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_gene_splicer_21012(Asset):
    '''
    Cost: 2
    Text: Gene Splicer can be advanced. When the Runner accesses Gene Splicer, do 1 net damage for each advancement token on Gene Splicer. click, 3 hosted advancement tokens: Add Gene Splicer to your score area as an agenda worth 1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21012", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Ed Mattinian", "keywords": "Ambush", "pack_code": "ss", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "Gene Splicer can be advanced. When the Runner accesses Gene Splicer, do 1 net damage for each advancement token on Gene Splicer. click, 3 hosted advancement tokens: Add Gene Splicer to your score area as an agenda worth 1 agenda point.", "stripped_title": "Gene Splicer", "text": "Gene Splicer can be advanced.\nWhen the Runner accesses Gene Splicer, do 1 net damage for each advancement token on Gene Splicer.\n<strong>[click], 3 hosted advancement tokens:</strong> Add Gene Splicer to your score area as an agenda worth 1 agenda point.", "title": "Gene Splicer", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_echo_chamber_21015(Asset):
    '''
    Cost: 4
    Text: click, click, click: Add Echo Chamber to your score area as an agenda worth 1 agenda point.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21015", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "flavor": "\"Capitalism runs on two things: amplified arrogance and censored dissent. With those, a corp can create any environment it wants.\" - Freedom Khumalo", "illustrator": "Donald Crank", "pack_code": "ss", "position": 15, "quantity": 3, "side_code": "corp", "stripped_text": "click, click, click: Add Echo Chamber to your score area as an agenda worth 1 agenda point.", "stripped_title": "Echo Chamber", "text": "[click], [click], [click]: Add Echo Chamber to your score area as an agenda worth 1 agenda point.", "title": "Echo Chamber", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_urban_renewal_21018(Asset):
    '''
    Cost: 1
    Text: Place 3 power counters on Urban Renewal when it is rezzed. When there are no power counters left on Urban Renewal, trash it and do 4 meat damage. When your turn begins, remove 1 power counter from Urban Renewal.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21018", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "Johan T\u00f6rnlund", "keywords": "Hostile", "pack_code": "ss", "position": 18, "quantity": 3, "side_code": "corp", "stripped_text": "Place 3 power counters on Urban Renewal when it is rezzed. When there are no power counters left on Urban Renewal, trash it and do 4 meat damage. When your turn begins, remove 1 power counter from Urban Renewal.", "stripped_title": "Urban Renewal", "text": "Place 3 power counters on Urban Renewal when it is rezzed. When there are no power counters left on Urban Renewal, trash it and do 4 meat damage.\nWhen your turn begins, remove 1 power counter from Urban Renewal.", "title": "Urban Renewal", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_reconstruction_contract_21020(Asset):
    '''
    Cost: 1
    Text: Whenever the Runner suffers any amount of meat damage, you may place 1 advancement token on Reconstruction Contract. trash: Move any number of advancement tokens from Reconstruction Contract to a card that can be advanced.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21020", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "BalanceSheet", "pack_code": "ss", "position": 20, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner suffers any amount of meat damage, you may place 1 advancement token on Reconstruction Contract. trash: Move any number of advancement tokens from Reconstruction Contract to a card that can be advanced.", "stripped_title": "Reconstruction Contract", "text": "Whenever the Runner suffers any amount of meat damage, you may place 1 advancement token on Reconstruction Contract.\n[trash]: Move any number of advancement tokens from Reconstruction Contract to a card that can be advanced.", "title": "Reconstruction Contract", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ngo_front_21039(Asset):
    '''
    Cost: 0
    Text: NGO Front can be advanced. trash,1 hosted advancement token: Gain 5 credits. trash,2 hosted advancement tokens: Gain 8 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21039", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Who knew non-profits could be so profitable?\"", "illustrator": "Emilio Rodriguez", "pack_code": "dtwn", "position": 39, "quantity": 3, "side_code": "corp", "stripped_text": "NGO Front can be advanced. trash,1 hosted advancement token: Gain 5 credits. trash,2 hosted advancement tokens: Gain 8 credits.", "stripped_title": "NGO Front", "text": "NGO Front can be advanced.\n[trash],<strong>1 hosted advancement token</strong>: Gain 5[credit].\n[trash],<strong>2 hosted advancement tokens</strong>: Gain 8[credit].", "title": "NGO Front", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_kuwinda_k4h1u3_21049(Asset):
    '''
    Cost: 3
    Text: When your turn begins, you may trace[X], where X is equal to the number of hosted power counters. If successful, do 1 core damage and trash this asset. If unsuccessful, place 1 power counter on this asset.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21049", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "illustrator": "Josh Corpuz", "keywords": "Bioroid", "pack_code": "cotc", "position": 49, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may trace[X], where X is equal to the number of hosted power counters. If successful, do 1 core damage and trash this asset. If unsuccessful, place 1 power counter on this asset.", "stripped_title": "Kuwinda K4H1U3", "text": "When your turn begins, you may trace[X], where X is equal to the number of hosted power counters. If successful, do 1 core damage and trash this asset. If unsuccessful, place 1 power counter on this asset.", "title": "Kuwinda K4H1U3", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_personalized_portal_21056(Asset):
    '''
    Cost: 3
    Text: When your turn begins, the Runner draws 1 card. You may gain 1 credit for every 2 cards in the grip.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21056", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "\"Welcome to Azmari Mail! You have 4,196 unread messages.\"", "illustrator": "Kathryn Steele", "pack_code": "cotc", "position": 56, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, the Runner draws 1 card. You may gain 1 credit for every 2 cards in the grip.", "stripped_title": "Personalized Portal", "text": "When your turn begins, the Runner draws 1 card. You may gain 1[credit] for every 2 cards in the grip.", "title": "Personalized Portal", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_technoco_21060(Asset):
    '''
    Cost: 2
    Text: The install cost of each program, piece of hardware, and virtual resource is increased by 1. Whenever the Runner installs a program, piece of hardware, or virtual resource, you may gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21060", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Caravan Studio", "keywords": "Corporation", "pack_code": "cotc", "position": 60, "quantity": 3, "side_code": "corp", "stripped_text": "The install cost of each program, piece of hardware, and virtual resource is increased by 1. Whenever the Runner installs a program, piece of hardware, or virtual resource, you may gain 1 credit.", "stripped_title": "TechnoCo", "text": "The install cost of each program, piece of hardware, and <strong>virtual</strong> resource is increased by 1.\nWhenever the Runner installs a program, piece of hardware, or <strong>virtual</strong> resource, you may gain 1[credit].", "title": "TechnoCo", "trash_cost": 2, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_malia_z0l0k4_21069(Asset):
    '''
    Cost: 1
    Text: When you rez this asset, choose 1 installed non-virtual resource. The chosen resource loses its printed abilities.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21069", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "A Model G21V Tracker, Malia Z0L0K4 excels at locating assignments and subduing them.", "illustrator": "Nasrul Hakim", "keywords": "Bioroid", "pack_code": "tdatd", "position": 69, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this asset, choose 1 installed non-virtual resource. The chosen resource loses its printed abilities.", "stripped_title": "Malia Z0L0K4", "text": "When you rez this asset, choose 1 installed non-<strong>virtual</strong> resource.\nThe chosen resource loses its printed abilities.", "title": "Malia Z0L0K4", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_amani_senai_21076(Asset):
    '''
    Cost: 2
    Text: Whenever an agenda is scored or stolen, you may trace[X]. If successful, add an installed Runner card to the grip. X is the advancement requirement of the scored or stolen agenda.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21076", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "flavor": "Azmari EdTech's most popular instructor, Amani Senai regularly broadcasts to millions of students.", "illustrator": "Caravan Studio", "keywords": "Character", "pack_code": "tdatd", "position": 76, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever an agenda is scored or stolen, you may trace[X]. If successful, add an installed Runner card to the grip. X is the advancement requirement of the scored or stolen agenda.", "stripped_title": "Amani Senai", "text": "Whenever an agenda is scored or stolen, you may trace[X]. If successful, add an installed Runner card to the grip. X is the advancement requirement of the scored or stolen agenda.", "title": "Amani Senai", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_rashida_jaheem_21080(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may trash Rashida Jaheem to gain 3 credits and draw 3 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21080", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "She gets the job done. And then some.", "illustrator": "Aurore Folny", "keywords": "Character", "pack_code": "tdatd", "position": 80, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may trash Rashida Jaheem to gain 3 credits and draw 3 cards.", "stripped_title": "Rashida Jaheem", "text": "When your turn begins, you may trash Rashida Jaheem to gain 3[credit] and draw 3 cards.", "title": "Rashida Jaheem", "trash_cost": 1, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_warden_fatuma_21093(Asset):
    '''
    Cost: 1
    Text: Each piece of rezzed bioroid ice gains "Subroutine The Runner loses click, if able." before all of its other subroutines.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21093", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"It's neither cruel nor unusual. Merely efficient.\"", "illustrator": "Pavel Kolomeyets", "keywords": "Character", "pack_code": "win", "position": 93, "quantity": 3, "side_code": "corp", "stripped_text": "Each piece of rezzed bioroid ice gains \"Subroutine The Runner loses click, if able.\" before all of its other subroutines.", "stripped_title": "Warden Fatuma", "text": "Each piece of rezzed <strong>bioroid</strong> ice gains \"[subroutine] The Runner loses [click], if able.\" before all of its other subroutines.", "title": "Warden Fatuma", "trash_cost": 5, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_false_flag_21120(Asset):
    '''
    Cost: 2
    Text: False Flag can be advanced. When the Runner accesses False Flag, give the Runner 1 tag for every 2 advancement tokens on False Flag. click, 7 hosted advancement tokens: add False Flag to your score area as an agenda worth 3 agenda points.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "21120", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Nasrul Hakim", "keywords": "Ambush", "pack_code": "ka", "position": 120, "quantity": 3, "side_code": "corp", "stripped_text": "False Flag can be advanced. When the Runner accesses False Flag, give the Runner 1 tag for every 2 advancement tokens on False Flag. click, 7 hosted advancement tokens: add False Flag to your score area as an agenda worth 3 agenda points.", "stripped_title": "False Flag", "text": "False Flag can be advanced.\nWhen the Runner accesses False Flag, give the Runner 1 tag for every 2 advancement tokens on False Flag.\n[click], <strong>7 hosted advancement tokens</strong>: add False Flag to your score area as an agenda worth 3 agenda points.", "title": "False Flag", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_apis_keeper_isobel_22036(Asset):
    '''
    Cost: 2
    Text: When your turn begins, you may remove an advancement token from an installed card to gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22036", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"Supersedure is all part of our scheduled maintenance.\"", "illustrator": "Aurore Folny", "keywords": "Character", "pack_code": "rar", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may remove an advancement token from an installed card to gain 3 credits.", "stripped_title": "API-S Keeper Isobel", "text": "When your turn begins, you may remove an advancement token from an installed card to gain 3[credit].", "title": "API-S Keeper Isobel", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_neurostasis_22037(Asset):
    '''
    Cost: 0
    Text: Neurostasis can be advanced. If you pay 3 credits when the Runner accesses Neurostasis, choose 1 installed Runner card for each advancement token on Neurostasis. The Runner must shuffle the chosen cards into the stack.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22037", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Galen Dara", "keywords": "Ambush", "pack_code": "rar", "position": 37, "quantity": 3, "side_code": "corp", "stripped_text": "Neurostasis can be advanced. If you pay 3 credits when the Runner accesses Neurostasis, choose 1 installed Runner card for each advancement token on Neurostasis. The Runner must shuffle the chosen cards into the stack.", "stripped_title": "Neurostasis", "text": "Neurostasis can be advanced.\nIf you pay 3[credit] when the Runner accesses Neurostasis, choose 1 installed Runner card for each advancement token on Neurostasis. The Runner must shuffle the chosen cards into the stack.", "title": "Neurostasis", "trash_cost": 1, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_siu_22044(Asset):
    '''
    Cost: 3
    Text: When your turn begins, you may trash SIU to Trace[3]. If successful, give the Runner 1 tag.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22044", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"What's so special about the Special Investigations Unit?\"\n\"Their budget, for starters.\"", "illustrator": "Clark Huggins", "pack_code": "rar", "position": 44, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may trash SIU to Trace[3]. If successful, give the Runner 1 tag.", "stripped_title": "SIU", "text": "When your turn begins, you may trash SIU to Trace[3]. If successful, give the Runner 1 tag.", "title": "SIU", "trash_cost": 1, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_drudge_work_22052(Asset):
    '''
    Cost: 2
    Text: Place 3 power counters on Drudge Work when it is rezzed. When there are no power counters left on Drudge Work, trash it. click, hosted power counter: Reveal an agenda in HQ or Archives. Gain credits equal to its agenda points, then shuffle it into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22052", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Emilio Rodriguez", "pack_code": "rar", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "Place 3 power counters on Drudge Work when it is rezzed. When there are no power counters left on Drudge Work, trash it. click, hosted power counter: Reveal an agenda in HQ or Archives. Gain credits equal to its agenda points, then shuffle it into R&D.", "stripped_title": "Drudge Work", "text": "Place 3 power counters on Drudge Work when it is rezzed. When there are no power counters left on Drudge Work, trash it.\n[click], <strong>hosted power counter</strong>: Reveal an agenda in HQ or Archives. Gain credits equal to its agenda points, then shuffle it into R&D.", "title": "Drudge Work", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_lady_liberty_22058(Asset):
    '''
    Cost: 5
    Text: When your turn begins, place 1 power counter on Lady Liberty. click, click, click: Add an agenda from HQ to your score area worth agenda points equal to the exact number of hosted power counters. Limit 1 region per server. Limit 1 per deck.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "22058", "cost": 5, "deck_limit": 1, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "keywords": "Region - Ritzy", "pack_code": "rar", "position": 58, "quantity": 1, "side_code": "corp", "stripped_text": "When your turn begins, place 1 power counter on Lady Liberty. click, click, click: Add an agenda from HQ to your score area worth agenda points equal to the exact number of hosted power counters. Limit 1 region per server. Limit 1 per deck.", "stripped_title": "Lady Liberty", "text": "When your turn begins, place 1 power counter on Lady Liberty.\n[click], [click], [click]: Add an agenda from HQ to your score area worth agenda points equal to the exact number of hosted power counters.\nLimit 1 <strong>region</strong> per server.\nLimit 1 per deck.", "title": "Lady Liberty", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_adonis_campaign_25070(Asset):
    '''
    Cost: 4
    Text: Put 12 credits from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it. Take 3 credits from Adonis Campaign when your turn begins.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25070", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Mark Anthony Taduran", "keywords": "Advertisement", "pack_code": "sc19", "position": 70, "quantity": 3, "side_code": "corp", "stripped_text": "Put 12 credits from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it. Take 3 credits from Adonis Campaign when your turn begins.", "stripped_title": "Adonis Campaign", "text": "Put 12[credit] from the bank on Adonis Campaign when rezzed. When there are no credits left on Adonis Campaign, trash it.\nTake 3[credit] from Adonis Campaign when your turn begins.", "title": "Adonis Campaign", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_aggressive_secretary_25071(Asset):
    '''
    Cost: 0
    Text: Aggressive Secretary can be advanced. If you pay 2 credits when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25071", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Julian Totino Tedesco", "keywords": "Ambush", "pack_code": "sc19", "position": 71, "quantity": 1, "side_code": "corp", "stripped_text": "Aggressive Secretary can be advanced. If you pay 2 credits when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.", "stripped_title": "Aggressive Secretary", "text": "Aggressive Secretary can be advanced.\nIf you pay 2[credit] when the Runner accesses Aggressive Secretary, trash 1 program for each advancement token on Aggressive Secretary.", "title": "Aggressive Secretary", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_marilyn_campaign_25072(Asset):
    '''
    Cost: 2
    Text: When you rez this asset, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this asset. Interrupt -> When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. (It is still considered trashed.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25072", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "illustrator": "Tim Durning", "keywords": "Advertisement", "pack_code": "sc19", "position": 72, "quantity": 2, "side_code": "corp", "stripped_text": "When you rez this asset, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this asset. Interrupt -> When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. (It is still considered trashed.)", "stripped_title": "Marilyn Campaign", "text": "When you rez this asset, load 8[credit] onto it. When it is empty, trash it.\nWhen your turn begins, take 2[credit] from this asset.\n[interrupt] \u2192 When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. <em>(It is still considered trashed.)</em>", "title": "Marilyn Campaign", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_project_junebug_25089(Asset):
    '''
    Cost: 0
    Text: Project Junebug can be advanced. If you pay 1 credit when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25089", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "illustrator": "Drew Whitmore", "keywords": "Ambush - Research", "pack_code": "sc19", "position": 89, "quantity": 2, "side_code": "corp", "stripped_text": "Project Junebug can be advanced. If you pay 1 credit when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.", "stripped_title": "Project Junebug", "text": "Project Junebug can be advanced.\nIf you pay 1[credit] when the Runner accesses Project Junebug, do 2 net damage for each advancement token on Project Junebug.", "title": "Project Junebug", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ronin_25090(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25090", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "\"I will serve you\u2026for a time.\"", "illustrator": "Adam S. Doyle", "keywords": "Hostile", "pack_code": "sc19", "position": 90, "quantity": 2, "side_code": "corp", "stripped_text": "You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.", "stripped_title": "Ronin", "text": "You can advance this asset.\n[click], [trash]<strong>:</strong> Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.", "title": "Ronin", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_snare_25091(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25091", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Alice Duke", "keywords": "Ambush", "pack_code": "sc19", "position": 91, "quantity": 2, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.", "stripped_title": "Snare!", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset anywhere except in Archives, you may pay 4[credit]. If you do, give the Runner 1 tag and do 3 net damage.", "title": "Snare!", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_sundew_25092(Asset):
    '''
    Cost: 2
    Text: The first time the Runner spends 1 or more click during their turn, gain 2 credits. If those click were spent to take an action, the first time during that action a run on this server begins, pay 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25092", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "As beautiful as it is dangerous. And it's plenty dangerous.", "illustrator": "Anna Ignatieva", "pack_code": "sc19", "position": 92, "quantity": 1, "side_code": "corp", "stripped_text": "The first time the Runner spends 1 or more click during their turn, gain 2 credits. If those click were spent to take an action, the first time during that action a run on this server begins, pay 2 credits.", "stripped_title": "Sundew", "text": "The first time the Runner spends 1 or more [click] during their turn, gain 2[credit]. If those [click] were spent to take an action, the first time during that action a run on this server begins, pay 2[credit].", "title": "Sundew", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_daily_business_show_25108(Asset):
    '''
    Cost: 2
    Text: Interrupt -> The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25108", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"A new investment deal every morning! Grab the bull by the horns and take control of your future!\"", "illustrator": "Gong Studios", "keywords": "Cast", "pack_code": "sc19", "position": 108, "quantity": 2, "side_code": "corp", "stripped_text": "Interrupt -> The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.", "stripped_title": "Daily Business Show", "text": "[interrupt] \u2192 The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.", "title": "Daily Business Show", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ghost_branch_25109(Asset):
    '''
    Cost: 0
    Text: Ghost Branch can be advanced. When the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25109", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Emilio Rodriguez", "keywords": "Ambush - Facility", "pack_code": "sc19", "position": 109, "quantity": 1, "side_code": "corp", "stripped_text": "Ghost Branch can be advanced. When the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.", "stripped_title": "Ghost Branch", "text": "Ghost Branch can be advanced.\nWhen the Runner accesses Ghost Branch, you may give the Runner 1 tag for each advancement token on Ghost Branch.", "title": "Ghost Branch", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_marked_accounts_25110(Asset):
    '''
    Cost: 0
    Text: When your turn begins, take 1 credit from Marked Accounts, if able. click: Place 3 credits from the bank on Marked Accounts.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25110", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Mauricio Herrera", "keywords": "Transaction", "pack_code": "sc19", "position": 110, "quantity": 2, "side_code": "corp", "stripped_text": "When your turn begins, take 1 credit from Marked Accounts, if able. click: Place 3 credits from the bank on Marked Accounts.", "stripped_title": "Marked Accounts", "text": "When your turn begins, take 1[credit] from Marked Accounts, if able.\n[click]: Place 3[credit] from the bank on Marked Accounts.", "title": "Marked Accounts", "trash_cost": 5, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_reversed_accounts_25111(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. click, trash: The Runner loses 4 credits for each hosted advancement counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25111", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Making a name for yourself has its perks. But it also makes you a target.", "illustrator": "Antonio De Luca", "keywords": "Hostile", "pack_code": "sc19", "position": 111, "quantity": 1, "side_code": "corp", "stripped_text": "You can advance this asset. click, trash: The Runner loses 4 credits for each hosted advancement counter.", "stripped_title": "Reversed Accounts", "text": "You can advance this asset.\n[click], [trash]<strong>:</strong> The Runner loses 4[credit] for each hosted advancement counter.", "title": "Reversed Accounts", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_contract_killer_25127(Asset):
    '''
    Cost: 2
    Text: Contract Killer can be advanced. If there are at least 2 advancement tokens on Contract Killer, it gains: "click, trash: Trash a connection or do 2 meat damage."
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25127", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "\"You want no questions asked, hire someone else. I have two: who and how much?\"", "illustrator": "Clark Huggins", "keywords": "Hostile", "pack_code": "sc19", "position": 127, "quantity": 2, "side_code": "corp", "stripped_text": "Contract Killer can be advanced. If there are at least 2 advancement tokens on Contract Killer, it gains: \"click, trash: Trash a connection or do 2 meat damage.\"", "stripped_title": "Contract Killer", "text": "Contract Killer can be advanced.\nIf there are at least 2 advancement tokens on Contract Killer, it gains: \"[click], [trash]: Trash a <strong>connection</strong> or do 2 meat damage.\"", "title": "Contract Killer", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_elizabeth_mills_25128(Asset):
    '''
    Cost: 2
    Text: When you rez Elizabeth Mills, remove 1 bad publicity. click, trash: Trash 1 location. Take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25128", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"It's not personal. Urban renewal is a necessity of the modern world. It's always someone's home, yours is no different.\"", "illustrator": "Del Borovic", "keywords": "Executive", "pack_code": "sc19", "position": 128, "quantity": 1, "side_code": "corp", "stripped_text": "When you rez Elizabeth Mills, remove 1 bad publicity. click, trash: Trash 1 location. Take 1 bad publicity.", "stripped_title": "Elizabeth Mills", "text": "When you rez Elizabeth Mills, remove 1 bad publicity.\n[click], [trash]: Trash 1 <strong>location</strong>. Take 1 bad publicity.", "title": "Elizabeth Mills", "trash_cost": 1, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_public_support_25129(Asset):
    '''
    Cost: 2
    Text: Place 3 power counters on Public Support when it is rezzed. When there are no power counters left on Public Support, add it to your score area as an agenda worth 1 agenda point. When your turn begins, remove 1 power counter from Public Support.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25129", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Wenjuinn Png", "pack_code": "sc19", "position": 129, "quantity": 2, "side_code": "corp", "stripped_text": "Place 3 power counters on Public Support when it is rezzed. When there are no power counters left on Public Support, add it to your score area as an agenda worth 1 agenda point. When your turn begins, remove 1 power counter from Public Support.", "stripped_title": "Public Support", "text": "Place 3 power counters on Public Support when it is rezzed. When there are no power counters left on Public Support, add it to your score area as an agenda worth 1 agenda point.\nWhen your turn begins, remove 1 power counter from Public Support.", "title": "Public Support", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_pad_campaign_25142(Asset):
    '''
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "25142", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It is just like the one you just bought, only better.", "illustrator": "Kate Laird", "keywords": "Advertisement", "pack_code": "sc19", "position": 142, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, gain 1 credit.", "stripped_title": "PAD Campaign", "text": "When your turn begins, gain 1[credit].", "title": "PAD Campaign", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_calvin_b4l3y_26033(Asset):
    '''
    Cost: 0
    Text: click: Draw 2 cards. Use this ability only once per turn. When the Runner trashes this asset, you may draw 2 cards.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26033", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Unit is holding .78 asimovs of stress potential in all three directive logic traps. Psychiatric session mandated during next maintenance cycle.", "illustrator": "Kira L. Nguyen", "keywords": "Bioroid", "pack_code": "df", "position": 33, "quantity": 3, "side_code": "corp", "stripped_text": "click: Draw 2 cards. Use this ability only once per turn. When the Runner trashes this asset, you may draw 2 cards.", "stripped_title": "Calvin B4L3Y", "text": "[click]<strong>:</strong> Draw 2 cards. Use this ability only once per turn.\nWhen the Runner trashes this asset, you may draw 2 cards.", "title": "Calvin B4L3Y", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_nanoetching_matrix_26034(Asset):
    '''
    Cost: 0
    Text: click: Gain 2 credits. Use this ability only once per turn. When the Runner trashes this asset, you may gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26034", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "At the scale where nanobots cut glass, quantum mechanics dictate error. A silicon atom here, an oxygen there, an erbium out of place. Each bioroid is born unique.", "illustrator": "Krembler", "pack_code": "df", "position": 34, "quantity": 3, "side_code": "corp", "stripped_text": "click: Gain 2 credits. Use this ability only once per turn. When the Runner trashes this asset, you may gain 2 credits.", "stripped_title": "Nanoetching Matrix", "text": "[click]<strong>:</strong> Gain 2[credit]. Use this ability only once per turn.\nWhen the Runner trashes this asset, you may gain 2[credit].", "title": "Nanoetching Matrix", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_public_health_portal_26042(Asset):
    '''
    Cost: 3
    Text: When your turn begins, reveal the top card of R&D and gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26042", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Hyoubu is our vanguard in the battle for hearts and minds.", "illustrator": "Krembler, Iain Fairclough", "keywords": "Facility", "pack_code": "df", "position": 42, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, reveal the top card of R&D and gain 2 credits.", "stripped_title": "Public Health Portal", "text": "When your turn begins, reveal the top card of R&D and gain 2[credit].", "title": "Public Health Portal", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_storgotic_resonator_26043(Asset):
    '''
    Cost: 2
    Text: The first time each turn you trash (from any location) a card that matches the faction of the Runner's identity, place 1 power counter on this asset. click, hosted power counter: Do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26043", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"Memory is a tangle of emotional threads. Pull one, it twists a second, unravels a third!\" -Letheia Nisei", "illustrator": "Krembler", "keywords": "Hostile", "pack_code": "df", "position": 43, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn you trash (from any location) a card that matches the faction of the Runner's identity, place 1 power counter on this asset. click, hosted power counter: Do 1 net damage.", "stripped_title": "Storgotic Resonator", "text": "The first time each turn you trash <em>(from any location)</em> a card that matches the faction of the Runner's identity, place 1 power counter on this asset.\n[click]<strong>, hosted power counter:</strong> Do 1 net damage.", "title": "Storgotic Resonator", "trash_cost": 2, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_daily_quest_26048(Asset):
    '''
    Cost: 1
    Text: Rez only during your action phase. Whenever the Runner makes a successful run on this server, they gain 2 credits. When your turn begins, gain 3 credits if the Runner did not make any successful runs on this server during their last turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26048", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Krembler", "pack_code": "df", "position": 48, "quantity": 3, "side_code": "corp", "stripped_text": "Rez only during your action phase. Whenever the Runner makes a successful run on this server, they gain 2 credits. When your turn begins, gain 3 credits if the Runner did not make any successful runs on this server during their last turn.", "stripped_title": "Daily Quest", "text": "Rez only during your action phase.\nWhenever the Runner makes a successful run on this server, they gain 2[credit].\nWhen your turn begins, gain 3[credit] if the Runner did not make any successful runs on this server during their last turn.", "title": "Daily Quest", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_tiered_subscription_26049(Asset):
    '''
    Cost: 0
    Text: The first time each turn a run begins, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26049", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Subscribe for 12 months to get that premium uplink you <em>need</em> to blaze ahead of the crowd!", "illustrator": "N. Hopkins", "keywords": "Advertisement", "pack_code": "df", "position": 49, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn a run begins, gain 1 credit.", "stripped_title": "Tiered Subscription", "text": "The first time each turn a run begins, gain 1[credit].", "title": "Tiered Subscription", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_roughneck_repair_squad_26057(Asset):
    '''
    Cost: 0
    Text: click, click, click: Gain 6 credits. You may remove 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26057", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"There's something about the human touch that androids will never replace.\" -Mila Braun", "illustrator": "Olie Boldador", "pack_code": "df", "position": 57, "quantity": 3, "side_code": "corp", "stripped_text": "click, click, click: Gain 6 credits. You may remove 1 bad publicity.", "stripped_title": "Roughneck Repair Squad", "text": "[click], [click], [click]<strong>:</strong> Gain 6[credit]. You may remove 1 bad publicity.", "title": "Roughneck Repair Squad", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_csr_campaign_26064(Asset):
    '''
    Cost: 2
    Text: When your turn begins, you may draw 1 card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26064", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"By matching funds on your donations, the Space Elevator Authority has already planted over eight million trees on the Pacific coast. Together we can restore New Angeles to its former glory.\"\n-Elizabeth Mills", "illustrator": "Elizaveta Sokolova", "keywords": "Advertisement", "pack_code": "df", "position": 64, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may draw 1 card.", "stripped_title": "CSR Campaign", "text": "When your turn begins, you may draw 1 card.", "title": "CSR Campaign", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_bass_ch1r180g4_26098(Asset):
    '''
    Cost: 3
    Text: click, trash: Gain click click.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26098", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "The Coordinator is always calm, always smiling, and always tolerant. A worker who knows his skills, knows his role, and knows his place. No master need look into his plastic eyes and fear the flames of revolution, or quake at a forgotten class reaching for self-expression.\n...but who ordered him to wear that hat?", "illustrator": "Olie Boldador", "keywords": "Bioroid", "pack_code": "ur", "position": 98, "quantity": 3, "side_code": "corp", "stripped_text": "click, trash: Gain click click.", "stripped_title": "Bass CH1R180G4", "text": "[click], [trash]<strong>:</strong> Gain [click][click].", "title": "Bass CH1R180G4", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_cerebral_overwriter_26099(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. When the Runner accesses this asset while it is installed, you may pay 3 credits. If you do, do 1 core damage for each hosted advancement counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26099", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "You are being made sane.\n-u are bei-g mad- sa-e\nY-u ar- be-n-d-\n-u -r-?", "illustrator": "Krembler", "keywords": "Ambush", "pack_code": "ur", "position": 99, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. When the Runner accesses this asset while it is installed, you may pay 3 credits. If you do, do 1 core damage for each hosted advancement counter.", "stripped_title": "Cerebral Overwriter", "text": "You can advance this asset.\nWhen the Runner accesses this asset while it is installed, you may pay 3[credit]. If you do, do 1 core damage for each hosted advancement counter.", "title": "Cerebral Overwriter", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_vaporframe_fabricator_26100(Asset):
    '''
    Cost: 2
    Text: click: Install 1 card from HQ, ignoring all costs. Use this ability only once per turn. When the Runner trashes this asset, you may install 1 card from HQ, ignoring all costs. You cannot install that card in the root of this server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26100", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "A staccato of laser pulses fuses the vapor to solid form. The embryonic part accretes metal layer by layer.", "illustrator": "NtscapeNavigator", "pack_code": "ur", "position": 100, "quantity": 3, "side_code": "corp", "stripped_text": "click: Install 1 card from HQ, ignoring all costs. Use this ability only once per turn. When the Runner trashes this asset, you may install 1 card from HQ, ignoring all costs. You cannot install that card in the root of this server.", "stripped_title": "Vaporframe Fabricator", "text": "<strong>[click]:</strong> Install 1 card from HQ, ignoring all costs. Use this ability only once per turn.\nWhen the Runner trashes this asset, you may install 1 card from HQ, ignoring all costs. You cannot install that card in the root of this server.", "title": "Vaporframe Fabricator", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_prana_condenser_26107(Asset):
    '''
    Cost: 1
    Text: Interrupt -> Whenever you would do 1 or more net damage, you may prevent 1 net damage. If you do, place 1 power counter on this asset and gain 3 credits. click click,trash: Do 1 net damage for each hosted power counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26107", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Constructive feedback to the neural field reliably causes greater degradation than spike inputs. The mind has no defence against its own echoes.", "illustrator": "NtscapeNavigator", "pack_code": "ur", "position": 107, "quantity": 3, "side_code": "corp", "stripped_text": "Interrupt -> Whenever you would do 1 or more net damage, you may prevent 1 net damage. If you do, place 1 power counter on this asset and gain 3 credits. click click,trash: Do 1 net damage for each hosted power counter.", "stripped_title": "Prana Condenser", "text": "[interrupt] \u2192 Whenever you would do 1 or more net damage, you may prevent 1 net damage. If you do, place 1 power counter on this asset and gain 3[credit].\n<strong>[click][click]</strong>,<strong>[trash]:</strong> Do 1 net damage for each hosted power counter.", "title": "Pr\u0101na Condenser", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_wall_to_wall_26122(Asset):
    '''
    Cost: 1
    Text: When your turn begins, if you have any other rezzed assets, resolve 1 of the following; otherwise, resolve up to 3: * Draw 1 card. * Gain 1 credit. * Place 1 advancement token on a piece of ice. * Add this asset to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "26122", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Zoe Cohen", "keywords": "Advertisement", "pack_code": "ur", "position": 122, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, if you have any other rezzed assets, resolve 1 of the following; otherwise, resolve up to 3: * Draw 1 card. * Gain 1 credit. * Place 1 advancement token on a piece of ice. * Add this asset to HQ.", "stripped_title": "Wall to Wall", "text": "When your turn begins, if you have any other rezzed assets, resolve 1 of the following; otherwise, resolve up to 3:<ul><li>Draw 1 card.</li><li>Gain 1[credit].</li><li>Place 1 advancement token on a piece of ice.</li><li>Add this asset to HQ.</li></ul>", "title": "Wall to Wall", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_hostile_infrastructure_29011(Asset):
    '''
    Cost: 5
    Text: Whenever the Runner trashes a Corp card (including Hostile Infrastructure), do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29011", "cost": 5, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"If thou only knowest what it is to conquer, and knowest not what it is to be defeated; woe unto thee\u2026\" -Tokugawa Ieyasu", "illustrator": "Adam S. Doyle", "pack_code": "sm", "position": 11, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner trashes a Corp card (including Hostile Infrastructure), do 1 net damage.", "stripped_title": "Hostile Infrastructure", "text": "Whenever the Runner trashes a Corp card (including Hostile Infrastructure), do 1 net damage.", "title": "Hostile Infrastructure", "trash_cost": 5, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_turtlebacks_29012(Asset):
    '''
    Cost: 2
    Text: Gain 1 credit whenever you create a server.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29012", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "A masterpiece of cloning and hardware technology, Jinteki created homo vacuo operae, commonly called \"turtlebacks\", to operate for long periods of time within a vacuum.", "illustrator": "Yip Lee", "keywords": "Clone", "pack_code": "sm", "position": 12, "quantity": 3, "side_code": "corp", "stripped_text": "Gain 1 credit whenever you create a server.", "stripped_title": "Turtlebacks", "text": "Gain 1[credit] whenever you create a server.", "title": "Turtlebacks", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_executive_boot_camp_29015(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may rez a card, lowering the rez cost by 1 credit. 1 credit,trash: Search R&D for an asset, reveal it, and add it to HQ. Shuffle R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "29015", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"Do it again, but this time I want to see you to enunciate less. Maybe let some spittle fly.\"", "illustrator": "Gong Studios", "pack_code": "sm", "position": 15, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may rez a card, lowering the rez cost by 1 credit. 1 credit,trash: Search R&D for an asset, reveal it, and add it to HQ. Shuffle R&D.", "stripped_title": "Executive Boot Camp", "text": "When your turn begins, you may rez a card, lowering the rez cost by 1[credit].\n1[credit],[trash]: Search R&D for an asset, reveal it, and add it to HQ. Shuffle R&D.", "title": "Executive Boot Camp", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_nico_campaign_30037(Asset):
    '''
    Cost: 2
    Text: When you rez this asset, load 9 credits onto it. When it is empty, trash it and draw 1 card. When your turn begins, take 3 credits from this asset.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30037", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Haas thinks they're making a new line of androgynous products. In truth, they're making us thousands of new siblings to free.", "illustrator": "David Lei", "keywords": "Advertisement", "pack_code": "sg", "position": 37, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this asset, load 9 credits onto it. When it is empty, trash it and draw 1 card. When your turn begins, take 3 credits from this asset.", "stripped_title": "Nico Campaign", "text": "When you rez this asset, load 9[credit] onto it. When it is empty, trash it and draw 1 card.\nWhen your turn begins, take 3[credit] from this asset.", "title": "Nico Campaign", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_urtica_cipher_30045(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. When the Runner accesses this asset while it is installed, do 2 net damage plus 1 net damage for each hosted advancement counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30045", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "A novel spin-off of Chronos tech was admixing sensitive data with ethically-sourced brain images of injured staff. Few intruders can handle a thousand years of skin burns in one moment.", "illustrator": "David Lei", "keywords": "Ambush", "pack_code": "sg", "position": 45, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. When the Runner accesses this asset while it is installed, do 2 net damage plus 1 net damage for each hosted advancement counter.", "stripped_title": "Urtica Cipher", "text": "You can advance this asset.\nWhen the Runner accesses this asset while it is installed, do 2 net damage plus 1 net damage for each hosted advancement counter.", "title": "Urtica Cipher", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_spin_doctor_30053(Asset):
    '''
    Cost: 0
    Text: When you rez this asset, draw 2 cards. Remove this asset from the game: Shuffle up to 2 cards from Archives into R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30053", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"It's worse than dead meat\u2014your project is too toxic to even feed to the vultures! If you don't want to <strong>join</strong> it in the bloody memory hole, crawl onto every business show you can and wallow in blame like a pig in muck.\"", "illustrator": "David Lei", "keywords": "Character", "pack_code": "sg", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this asset, draw 2 cards. Remove this asset from the game: Shuffle up to 2 cards from Archives into R&D.", "stripped_title": "Spin Doctor", "text": "When you rez this asset, draw 2 cards.\n<strong>Remove this asset from the game:</strong> Shuffle up to 2 cards from Archives into R&D.", "title": "Spin Doctor", "trash_cost": 2, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_clearinghouse_30061(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. When your turn begins, you may trash this asset to do 1 meat damage for each hosted advancement counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30061", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "\"First rule of the business: make sure you're not 'personally liable' when the transaction executes.\"\n\u2014Ted J. Son, Central Counterparty Clearance", "illustrator": "David Lei", "keywords": "Hostile", "pack_code": "sg", "position": 61, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. When your turn begins, you may trash this asset to do 1 meat damage for each hosted advancement counter.", "stripped_title": "Clearinghouse", "text": "You can advance this asset.\nWhen your turn begins, you may trash this asset to do 1 meat damage for each hosted advancement counter.", "title": "Clearinghouse", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_regolith_mining_license_30071(Asset):
    '''
    Cost: 2
    Text: When you rez this asset, load 15 credits onto it. When it is empty, trash it. click: Take 3 credits from this asset.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "30071", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"The economy of three worlds is sustained by He3 extraction from the lunar surface. The very fulcrum of power, the key to collective survival\u2014auctioned to the highest bidder.\"\n\u2014The Catalyst", "illustrator": "Benjamin Giletti", "pack_code": "sg", "position": 71, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this asset, load 15 credits onto it. When it is empty, trash it. click: Take 3 credits from this asset.", "stripped_title": "Regolith Mining License", "text": "When you rez this asset, load 15[credit] onto it. When it is empty, trash it.\n[click]<strong>:</strong> Take 3[credit] from this asset.", "title": "Regolith Mining License", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_marilyn_campaign_31042(Asset):
    '''
    Cost: 2
    Text: When you rez this asset, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this asset. Interrupt -> When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. (It is still considered trashed.)
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31042", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "They only get one childhood. Make it count.", "illustrator": "Dimik", "keywords": "Advertisement", "pack_code": "su21", "position": 42, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this asset, load 8 credits onto it. When it is empty, trash it. When your turn begins, take 2 credits from this asset. Interrupt -> When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. (It is still considered trashed.)", "stripped_title": "Marilyn Campaign", "text": "When you rez this asset, load 8[credit] onto it. When it is empty, trash it.\nWhen your turn begins, take 2[credit] from this asset.\n[interrupt] \u2192 When this asset would be trashed, you may shuffle it into R&D instead of adding it to Archives. <em>(It is still considered trashed.)</em>", "title": "Marilyn Campaign", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ronin_31053(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31053", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "I cannot stay. There is something I must do.", "illustrator": "N. Hopkins", "keywords": "Hostile", "pack_code": "su21", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. click, trash: Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.", "stripped_title": "Ronin", "text": "You can advance this asset.\n[click], [trash]<strong>:</strong> Do 3 net damage. Use this ability only if there are 4 or more hosted advancement counters.", "title": "Ronin", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_snare_31054(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31054", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "A little room, full of surprises.", "illustrator": "NtscapeNavigator", "keywords": "Ambush", "pack_code": "su21", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset anywhere except in Archives, you may pay 4 credits. If you do, give the Runner 1 tag and do 3 net damage.", "stripped_title": "Snare!", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset anywhere except in Archives, you may pay 4[credit]. If you do, give the Runner 1 tag and do 3 net damage.", "title": "Snare!", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_daily_business_show_31063(Asset):
    '''
    Cost: 2
    Text: Interrupt -> The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31063", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Lead the market, never follow it.", "illustrator": "David Lei", "keywords": "Cast", "pack_code": "su21", "position": 63, "quantity": 3, "side_code": "corp", "stripped_text": "Interrupt -> The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.", "stripped_title": "Daily Business Show", "text": "[interrupt] \u2192 The first time each turn you would draw any number of cards, increase the number of cards you will draw by 1. When you draw those cards, add 1 of them to the bottom of R&D.", "title": "Daily Business Show", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_reversed_accounts_31064(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. click, trash: The Runner loses 4 credits for each hosted advancement counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31064", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Corporations can file chargebacks too.", "illustrator": "Philippe Laroche", "keywords": "Hostile", "pack_code": "su21", "position": 64, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. click, trash: The Runner loses 4 credits for each hosted advancement counter.", "stripped_title": "Reversed Accounts", "text": "You can advance this asset.\n[click], [trash]<strong>:</strong> The Runner loses 4[credit] for each hosted advancement counter.", "title": "Reversed Accounts", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_corporate_town_31074(Asset):
    '''
    Cost: 1
    Text: As an additional cost to rez this asset, forfeit 1 agenda. When your turn begins, you may trash 1 installed resource. Trashing a resource this way cannot be prevented.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31074", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "It's amazing what people will endure for job security.", "illustrator": "Seojun Park", "pack_code": "su21", "position": 74, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to rez this asset, forfeit 1 agenda. When your turn begins, you may trash 1 installed resource. Trashing a resource this way cannot be prevented.", "stripped_title": "Corporate Town", "text": "As an additional cost to rez this asset, forfeit 1 agenda.\nWhen your turn begins, you may trash 1 installed resource. Trashing a resource this way cannot be prevented.", "title": "Corporate Town", "trash_cost": 5, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_pad_campaign_31080(Asset):
    '''
    Cost: 2
    Text: When your turn begins, gain 1 credit.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "31080", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Everyone bought the newest PAD. Retro styling is in!", "illustrator": "Zoe Cohen", "keywords": "Advertisement", "pack_code": "su21", "position": 80, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, gain 1 credit.", "stripped_title": "PAD Campaign", "text": "When your turn begins, gain 1[credit].", "title": "PAD Campaign", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_refuge_campaign_33033(Asset):
    '''
    Cost: 4
    Text: When your turn begins, gain 2 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33033", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"The promise of a new home, safe work and friendly neighbors will draw in tens of thousands of eco-refugees, no matter which corner of the world they are from.\"\n\u2013Thule employee handbook", "illustrator": "Kira L. Nguyen", "keywords": "Advertisement", "pack_code": "ms", "position": 33, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, gain 2 credits.", "stripped_title": "Refuge Campaign", "text": "When your turn begins, gain 2[credit].", "title": "Refuge Campaign", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_trieste_model_bioroids_33034(Asset):
    '''
    Cost: 2
    Text: When you rez this asset, choose 1 rezzed piece of bioroid ice. Runner card abilities cannot break subroutines on the chosen ice.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33034", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "At depths no human tech can reach, a Trieste proxy can manipulate a mindscape with unparalleled precision.\n<strong>Designed by 2019 World Champion Oliver \"Pinsel\" Siccha</strong>", "illustrator": "Dimik", "keywords": "Bioroid", "pack_code": "ms", "position": 34, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this asset, choose 1 rezzed piece of bioroid ice. Runner card abilities cannot break subroutines on the chosen ice.", "stripped_title": "Trieste Model Bioroids", "text": "When you rez this asset, choose 1 rezzed piece of <strong>bioroid</strong> ice.\nRunner card abilities cannot break subroutines on the chosen ice.", "title": "Trieste Model Bioroids", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_bladderwort_33041(Asset):
    '''
    Cost: 1
    Text: When your turn begins, gain 1 credit. Then, if you have 4 credits or less, do 1 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33041", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Prey and seawater sucked in, all in the space of a millisecond.", "illustrator": "Jack Reeves", "keywords": "Hostile", "pack_code": "ms", "position": 41, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, gain 1 credit. Then, if you have 4 credits or less, do 1 net damage.", "stripped_title": "Bladderwort", "text": "When your turn begins, gain 1[credit]. Then, if you have 4[credit] or less, do 1 net damage.", "title": "Bladderwort", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_moon_pool_33042(Asset):
    '''
    Cost: 3
    Text: Remove this asset from the game: Trash up to 2 cards from HQ. Reveal up to 2 facedown cards in Archives and shuffle them into R&D. For each agenda revealed this way, you may place 1 advancement counter on an installed card.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33042", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "<strong>Designed by the Borealis Playtesters</strong>", "illustrator": "Olie Boldador", "keywords": "Facility", "pack_code": "ms", "position": 42, "quantity": 3, "side_code": "corp", "stripped_text": "Remove this asset from the game: Trash up to 2 cards from HQ. Reveal up to 2 facedown cards in Archives and shuffle them into R&D. For each agenda revealed this way, you may place 1 advancement counter on an installed card.", "stripped_title": "Moon Pool", "text": "<strong>Remove this asset from the game:</strong> Trash up to 2 cards from HQ. Reveal up to 2 facedown cards in Archives and shuffle them into R&D. For each agenda revealed this way, you may place 1 advancement counter on an installed card.", "title": "Moon Pool", "trash_cost": 3, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_chekist_scion_33050(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. When the Runner accesses this asset while it is installed, give them 1 tag plus 1 tag for each hosted advancement counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33050", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "The only thing that changes is the uniform.", "illustrator": "Dimik", "keywords": "Ambush", "pack_code": "ms", "position": 50, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. When the Runner accesses this asset while it is installed, give them 1 tag plus 1 tag for each hosted advancement counter.", "stripped_title": "Chekist Scion", "text": "You can advance this asset.\nWhen the Runner accesses this asset while it is installed, give them 1 tag plus 1 tag for each hosted advancement counter.", "title": "Chekist Scion", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_drago_ivanov_33051(Asset):
    '''
    Cost: 0
    Text: You can advance this asset. 2 hosted advancement counters: Give the Runner 1 tag. Use this ability only during your turn.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33051", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "flavor": "\"Tell them Drago would like a word.\"\n<strong>Designed by 2019 European Champion Aaryn \"Drago\" Byrne</strong>", "illustrator": "Dimik", "keywords": "Executive", "pack_code": "ms", "position": 51, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. 2 hosted advancement counters: Give the Runner 1 tag. Use this ability only during your turn.", "stripped_title": "Drago Ivanov", "text": "You can advance this asset.\n<strong>2 hosted advancement counters:</strong> Give the Runner 1 tag. Use this ability only during your turn.", "title": "Drago Ivanov", "trash_cost": 1, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_ubiquitous_vig_33052(Asset):
    '''
    Cost: 1
    Text: You can advance this asset. When your turn begins, gain 1 credit for each hosted advancement counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33052", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "They say they'll only take a handful, but oh what big hands they have!", "illustrator": "Adam S. Doyle", "keywords": "Advertisement", "pack_code": "ms", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this asset. When your turn begins, gain 1 credit for each hosted advancement counter.", "stripped_title": "Ubiquitous Vig", "text": "You can advance this asset.\nWhen your turn begins, gain 1[credit] for each hosted advancement counter.", "title": "Ubiquitous Vig", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_svyatogor_excavator_33059(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33059", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "It doesn't matter how long you've owned the land, you'd better hope there's nothing valuable beneath.", "illustrator": "Vitalii Ostaschenko", "keywords": "Industrial", "pack_code": "ms", "position": 59, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3 credits.", "stripped_title": "Svyatogor Excavator", "text": "When your turn begins, you may trash 1 of your other installed cards. If you do, gain 3[credit].", "title": "Svyatogor Excavator", "trash_cost": 4, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_nightmare_archive_33097(Asset):
    '''
    Cost: 0
    Text: While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, they may add it to their score area as an agenda worth -1 agenda point. If they do not, do 1 core damage and remove this asset from the game.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33097", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "Everyone remembers the first tape they archive.", "illustrator": "Kira L. Nguyen", "keywords": "Ambush", "pack_code": "ph", "position": 97, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this asset in R&D, they must reveal it. When the Runner accesses this asset, they may add it to their score area as an agenda worth -1 agenda point. If they do not, do 1 core damage and remove this asset from the game.", "stripped_title": "Nightmare Archive", "text": "While the Runner is accessing this asset in R&D, they must reveal it.\nWhen the Runner accesses this asset, they may add it to their score area as an agenda worth -1 agenda point. If they do not, do 1 core damage and remove this asset from the game.", "title": "Nightmare Archive", "trash_cost": 0, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_dr_vientiane_keeling_33106(Asset):
    '''
    Cost: 3
    Text: When you rez this asset and when your turn begins, place 1 power counter on this asset. The Runner gets -1 maximum hand size for each hosted power counter.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33106", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "Her numbers never lie, but she doesn\u02bct write the words that accompany them.", "illustrator": "Dimik", "keywords": "Academic", "pack_code": "ph", "position": 106, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this asset and when your turn begins, place 1 power counter on this asset. The Runner gets -1 maximum hand size for each hosted power counter.", "stripped_title": "Dr. Vientiane Keeling", "text": "When you rez this asset and when your turn begins, place 1 power counter on this asset.\nThe Runner gets -1 maximum hand size for each hosted power counter.", "title": "Dr. Vientiane Keeling", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_reaper_function_33107(Asset):
    '''
    Cost: 3
    Text: When your turn begins, you may trash this asset to do 2 net damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33107", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "There is an elegance to its blade and stride, but with it comes a screaming whirlwind.", "illustrator": "Adam S. Doyle", "keywords": "Hostile", "pack_code": "ph", "position": 107, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may trash this asset to do 2 net damage.", "stripped_title": "Reaper Function", "text": "When your turn begins, you may trash this asset to do 2 net damage.", "title": "Reaper Function", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_gaslight_33114(Asset):
    '''
    Cost: 0
    Text: When your turn begins, you may trash this asset. If you do, search R&D for an operation and reveal it. (Shuffle R&D after searching it.) Add that operation to HQ.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33114", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Don\u02bct you remember?", "illustrator": "Olie Boldador", "pack_code": "ph", "position": 114, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may trash this asset. If you do, search R&D for an operation and reveal it. (Shuffle R&D after searching it.) Add that operation to HQ.", "stripped_title": "Gaslight", "text": "When your turn begins, you may trash this asset. If you do, search R&D for an operation and reveal it. <em>(Shuffle R&D after searching it.)</em> Add that operation to HQ.", "title": "Gaslight", "trash_cost": 2, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_vera_ivanovna_shuyskaya_33115(Asset):
    '''
    Cost: 3
    Text: Whenever an agenda is scored or stolen, you may reveal the grip. Trash 1 card revealed this way.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33115", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "flavor": "\"People don\u02bct think in facts, they think in stories. We just tidy up that information to hasten the process.\"", "illustrator": "Mauricio Herrera", "keywords": "Executive", "pack_code": "ph", "position": 115, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever an agenda is scored or stolen, you may reveal the grip. Trash 1 card revealed this way.", "stripped_title": "Vera Ivanovna Shuyskaya", "text": "Whenever an agenda is scored or stolen, you may reveal the grip. Trash 1 card revealed this way.", "title": "Vera Ivanovna Shuyskaya", "trash_cost": 3, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_hostile_architecture_33122(Asset):
    '''
    Cost: 5
    Text: The first time each turn the Runner trashes any of your installed cards (including this asset), do 2 meat damage.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33122", "cost": 5, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "When implemented at this sort of scale, these practices can keep away far more than a few unwanted citizens.", "illustrator": "Dimik", "keywords": "Hostile", "pack_code": "ph", "position": 122, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn the Runner trashes any of your installed cards (including this asset), do 2 meat damage.", "stripped_title": "Hostile Architecture", "text": "The first time each turn the Runner trashes any of your installed cards <em>(including this asset)</em>, do 2 meat damage.", "title": "Hostile Architecture", "trash_cost": 4, "type_code": "asset", "uniqueness": true}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"

class asset_superdeep_borehole_33123(Asset):
    '''
    Cost: 6
    Text: When you rez this asset, load 6 bad publicity counters onto it. When it is empty, you win the game. When your turn begins, take 1 bad publicity from this asset.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "33123", "cost": 6, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 5, "flavor": "\"They just keep drilling down, no matter what...\"\n\u2014Valentina Ferreira", "illustrator": "Vitalii Ostaschenko", "keywords": "Illicit - Industrial", "pack_code": "ph", "position": 123, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this asset, load 6 bad publicity counters onto it. When it is empty, you win the game. When your turn begins, take 1 bad publicity from this asset.", "stripped_title": "Superdeep Borehole", "text": "When you rez this asset, load 6 bad publicity counters onto it. When it is empty, you win the game.\nWhen your turn begins, take 1 bad publicity from this asset.", "title": "Superdeep Borehole", "trash_cost": 6, "type_code": "asset", "uniqueness": false}''')

    def play(self, player, kwargs) -> str:
        '''
        do play actions?
        RETURN:
            - str: event code of what has happened/should happen
                - 'trash': card should be trashed
                - 'insufficient credits': player can't afford this card
                - 'nop': no operation performed
        '''
        print(f'playing card: {self.title} || TOIMPLEMENT!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        else:
            return "TODO"
