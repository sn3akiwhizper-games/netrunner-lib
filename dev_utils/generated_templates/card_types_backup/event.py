
'''
card classes of type event
'''
from netrunner_lib.cards._base_card_classes import Event

            
class event_deja_vu_01002(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01002", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Anything worth doing is worth doing twice.", "illustrator": "Tim Durning", "pack_code": "core", "position": 2, "quantity": 2, "side_code": "runner", "stripped_text": "Add 1 card (or up to 2 virus cards) from your heap to your grip.", "stripped_title": "Deja Vu", "text": "Add 1 card (or up to 2 <strong>virus</strong> cards) from your heap to your grip.", "title": "D\u00e9j\u00e0 Vu", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_demolition_run_01003(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01003", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "You ever set something on fire just to watch it burn?", "illustrator": "Anna Ignatieva", "keywords": "Run - Sabotage", "pack_code": "core", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ or R&D. Access -> 0 credits: Trash the card you are accessing.", "stripped_title": "Demolition Run", "text": "Run HQ or R&D.\nAccess \u2192 <strong>0[credit]:</strong> Trash the card you are accessing.", "title": "Demolition Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_stimhack_01004(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01004", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Rachel Borovic", "keywords": "Run", "pack_code": "core", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "Place 9 credits on this event, then run any server. During that run, hosted credits are considered to be in your credit pool. When that run ends, suffer 1 core damage. This damage cannot be prevented.", "stripped_title": "Stimhack", "text": "Place 9[credit] on this event, then run any server. During that run, hosted credits are considered to be in your credit pool. When that run ends, suffer 1 core damage. This damage cannot be prevented.", "title": "Stimhack", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_account_siphon_01018(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01018", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "illustrator": "Outland Entertainment LLC", "keywords": "Run - Sabotage", "pack_code": "core", "position": 18, "quantity": 2, "side_code": "runner", "stripped_text": "Run HQ. If successful, instead of breaching HQ, you may force the Corp to lose up to 5 credits, then you gain 2 credits for each credit lost and take 2 tags.", "stripped_title": "Account Siphon", "text": "Run HQ. If successful, instead of breaching HQ, you may force the Corp to lose up to 5[credit], then you gain 2[credit] for each credit lost and take 2 tags.", "title": "Account Siphon", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_easy_mark_01019(Event):
    '''
    Gain 3 credits.
    '''
    def __init__(self):
        super().__init__(r'''{"code": "01019", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"Hey kid, you fire that up now, bound to be vamped real bad. Some real pathetic individuals around here. But thankfully I got just the ticket\u2026\"", "illustrator": "Matt Zeilinger", "keywords": "Job", "pack_code": "core", "position": 19, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 3 credits.", "stripped_title": "Easy Mark", "text": "Gain 3[credit].", "title": "Easy Mark", "type_code": "event", "uniqueness": false}''')

    def play(self, player, kwargs):
        '''
        do play actions?
        '''
        print(f'playing card: {self.title} || PARTIAL!')
        super_result = super().play(player,kwargs)
        if super_result != "nop":
            return super_result
        player.credit_pool += 3
        return self.trash(player)

class event_forged_activation_orders_01020(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01020", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "As the hysteria in the room climbed higher up the corporate chain, an uneasy feeling of joblessness began to sink in on the lower rungs.", "illustrator": "Ed Mattinian", "keywords": "Sabotage", "pack_code": "core", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "Choose 1 unrezzed piece of ice. The Corp may rez that ice. If they do not, they trash it.", "stripped_title": "Forged Activation Orders", "text": "Choose 1 unrezzed piece of ice. The Corp may rez that ice. If they do not, they trash it.", "title": "Forged Activation Orders", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_inside_job_01021(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01021", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Hey, listen, I'm not asking you to do anything dangerous. Just let me into the building. And tell me which room has the weakest security. And please don't say 'the bathroom' again.\"", "illustrator": "Clark Huggins", "keywords": "Run", "pack_code": "core", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. The first time this run you encounter a piece of ice, bypass it.", "stripped_title": "Inside Job", "text": "Run any server. The first time this run you encounter a piece of ice, bypass it.", "title": "Inside Job", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_special_order_01022(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01022", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Feverishly tracking its frustratingly slow progress across the Pacific, the package finally shows up hours later\u2026", "illustrator": "Kate Niemczyk", "pack_code": "core", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "Search your stack for an icebreaker, reveal it, and add it to your grip. Shuffle your stack.", "stripped_title": "Special Order", "text": "Search your stack for an <strong>icebreaker</strong>, reveal it, and add it to your grip. Shuffle your stack.", "title": "Special Order", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_diesel_01034(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01034", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Diesel gives you flames.", "illustrator": "Tim Durning", "pack_code": "core", "position": 34, "quantity": 3, "side_code": "runner", "stripped_text": "Draw 3 cards.", "stripped_title": "Diesel", "text": "Draw 3 cards.", "title": "Diesel", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_modded_01035(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01035", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "There's no replacement for a home-grown program. Fed on late nights, oaty bars, and single-minded determination. Cheaper, too.", "illustrator": "Ralph Beisner", "keywords": "Mod", "pack_code": "core", "position": 35, "quantity": 2, "side_code": "runner", "stripped_text": "Install a program or piece of hardware, lowering the install cost by 3.", "stripped_title": "Modded", "text": "Install a program or piece of hardware, lowering the install cost by 3.", "title": "Modded", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_the_makers_eye_01036(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01036", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Some of the professionals have good instincts, but they can't see beyond the data. They can't see the matrix.\" -Ele \"Smoke\" Scovak", "illustrator": "Yue Wang", "keywords": "Run", "pack_code": "core", "position": 36, "quantity": 3, "side_code": "runner", "stripped_text": "Run R&D. If successful, access 2 additional cards when you breach R&D.", "stripped_title": "The Maker's Eye", "text": "Run R&D. If successful, access 2 additional cards when you breach R&D.", "title": "The Maker's Eye", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_tinkering_01037(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01037", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "\"There's that moment, you know, when the whole world seems to fall away and it is only you and your mod, and the mod is the world.\"", "illustrator": "Christina Davis", "keywords": "Mod", "pack_code": "core", "position": 37, "quantity": 3, "side_code": "runner", "stripped_text": "Choose a piece of ice. That ice gains sentry, code gate, and barrier until the end of the turn.", "stripped_title": "Tinkering", "text": "Choose a piece of ice. That ice gains <strong>sentry</strong>, <strong>code gate</strong>, and <strong>barrier</strong> until the end of the turn.", "title": "Tinkering", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_infiltration_01049(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01049", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Bring back any memories, Monica?\" -John \"Animal\" McEvoy", "illustrator": "Imaginary FS Pte Ltd", "pack_code": "core", "position": 49, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 2 credits or expose 1 card.", "stripped_title": "Infiltration", "text": "Gain 2[credit] or expose 1 card.", "title": "Infiltration", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_sure_gamble_01050(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01050", "cost": 5, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Lady Luck took the form of a hifi quantum manipulation ring that she wore on her middle finger.", "illustrator": "Kate Niemczyk", "pack_code": "core", "position": 50, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 9 credits.", "stripped_title": "Sure Gamble", "text": "Gain 9[credit].", "title": "Sure Gamble", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_vamp_02021(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02021", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "There was a certain schadenfreude about throwing away your credits.", "illustrator": "Ed Mattinian", "keywords": "Run - Sabotage", "pack_code": "ta", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, instead of breaching HQ, you may spend X credits. If you do, the Corp loses X credits. If you spent credits, take 1 tag.", "stripped_title": "Vamp", "text": "Run HQ. If successful, instead of breaching HQ, you may spend X[credit]. If you do, the Corp loses X[credit]. If you spent credits, take 1 tag.", "title": "Vamp", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_satellite_uplink_02023(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02023", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "T-minus 13 seconds. Leela had to work fast. She jacked in the mesa wire and activated the screen. 7 seconds. The internal SLD was still booting. 4 seconds. The interface flickered to life with an orange glow. 2 seconds. With a tap of a finger she was in.", "illustrator": "Matt Zeilinger", "pack_code": "ta", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "Expose up to 2 cards.", "stripped_title": "Satellite Uplink", "text": "Expose up to 2 cards.", "title": "Satellite Uplink", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_notoriety_02026(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02026", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "When you're this good, it's hard not to grow a fan base.", "illustrator": "Matt Zeilinger", "pack_code": "ta", "position": 26, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on R&D, HQ, and Archives this turn. Add Notoriety to your score area as an agenda worth 1 agenda point.", "stripped_title": "Notoriety", "text": "Play only if you made a successful run on R&D, HQ, and Archives this turn.\nAdd Notoriety to your score area as an agenda worth 1 agenda point.", "title": "Notoriety", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_emergency_shutdown_02043(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02043", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Think of it as a virtual shock collar for punishing corporate pets.\" -Andromeda", "illustrator": "Adam S. Doyle", "keywords": "Sabotage", "pack_code": "ce", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on HQ this turn. Derez 1 installed piece of ice.", "stripped_title": "Emergency Shutdown", "text": "Play only if you made a successful run on HQ this turn.\nDerez 1 installed piece of ice.", "title": "Emergency Shutdown", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_test_run_02047(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02047", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Eko Puteh", "pack_code": "ce", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "Search either your stack or your heap for 1 program. (Shuffle your stack if you searched it.) Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.", "stripped_title": "Test Run", "text": "Search either your stack or your heap for 1 program. <em>(Shuffle your stack if you searched it.)</em> Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.", "title": "Test Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_surge_02081(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02081", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "You must yell \"surge\" to get the full effect.", "illustrator": "Andrew Mar", "pack_code": "hs", "position": 81, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you placed at least 1 virus counter on a program this turn. Place 2 virus counters on that program.", "stripped_title": "Surge", "text": "Play only if you placed at least 1 virus counter on a program this turn.\nPlace 2 virus counters on that program.", "title": "Surge", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_networking_02084(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02084", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "She preferred to do business in a club. Something about the lights and dancers clouded the judgment of the corporate simpletons she met there.", "illustrator": "Gong Studios", "pack_code": "hs", "position": 84, "quantity": 3, "side_code": "runner", "stripped_text": "Remove 1 tag. Then, you may pay 1 credit to add this event to your grip.", "stripped_title": "Networking", "text": "Remove 1 tag. Then, you may pay 1[credit] to add this event to your grip.", "title": "Networking", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_quality_time_02087(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02087", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "She at her P.A.D. I at my rig. Low lights. Smooth jazz. Love blooms.", "illustrator": "Erfan Fajar", "pack_code": "hs", "position": 87, "quantity": 3, "side_code": "runner", "stripped_text": "Draw 5 cards.", "stripped_title": "Quality Time", "text": "Draw 5 cards.", "title": "Quality Time", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_kraken_02090(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02090", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Early permutations of the kraken proved to be insatiable, ice-devouring marauders. Not much has changed.", "illustrator": "Liiga Smilshkalne", "pack_code": "hs", "position": 90, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you stole an agenda this turn. Choose a server. The Corp trashes 1 piece of ice protecting that server.", "stripped_title": "Kraken", "text": "Play only if you stole an agenda this turn.\nChoose a server. The Corp trashes 1 piece of ice protecting that server.", "title": "Kraken", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_retrieval_run_02101(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02101", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Outland Entertainment LLC", "keywords": "Run", "pack_code": "fp", "position": 101, "quantity": 3, "side_code": "runner", "stripped_text": "Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.", "stripped_title": "Retrieval Run", "text": "Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.", "title": "Retrieval Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_indexing_02106(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02106", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "A little corporate restructuring is necessary once in a while.", "illustrator": "Mauricio Herrera", "keywords": "Run", "pack_code": "fp", "position": 106, "quantity": 3, "side_code": "runner", "stripped_text": "Run R&D. If successful, instead of breaching R&D, you may look at the top 5 cards of R&D and arrange them in any order.", "stripped_title": "Indexing", "text": "Run R&D. If successful, instead of breaching R&D, you may look at the top 5 cards of R&D and arrange them in any order.", "title": "Indexing", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_escher_03031(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03031", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 5, "illustrator": "Shawn Ye Zhongyi", "keywords": "Run", "pack_code": "cac", "position": 31, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, instead of breaching HQ, rearrange any number of ice protecting all servers. (Do not rez or derez any ice or change the number of ice protecting any server.)", "stripped_title": "Escher", "text": "Run HQ. If successful, instead of breaching HQ, rearrange any number of ice protecting all servers. <em>(Do not rez or derez any ice or change the number of ice protecting any server.)</em>", "title": "Escher", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_exploratory_romp_03032(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03032", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Wheeeee!", "illustrator": "Matt Zeilinger", "keywords": "Run", "pack_code": "cac", "position": 32, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. If successful, instead of breaching that server, remove up to 3 advancement counters from 1 card in the root of or protecting the attacked server.", "stripped_title": "Exploratory Romp", "text": "Run any server. If successful, instead of breaching that server, remove up to 3 advancement counters from 1 card in the root of or protecting the attacked server.", "title": "Exploratory Romp", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_freelance_coding_contract_03033(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03033", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"Idealism's great, but it don't keep you in soybeef tacos.\" -Matt \"TheMerc\" Thomas", "illustrator": "Jason Rumpff", "keywords": "Job", "pack_code": "cac", "position": 33, "quantity": 3, "side_code": "runner", "stripped_text": "Trash up to 5 programs from your grip. Gain 2 credits for each program trashed.", "stripped_title": "Freelance Coding Contract", "text": "Trash up to 5 programs from your grip. Gain 2[credit] for each program trashed.", "title": "Freelance Coding Contract", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_scavenge_03034(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03034", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "One man's trash.", "illustrator": "Matt Zeilinger", "pack_code": "cac", "position": 34, "quantity": 3, "side_code": "runner", "stripped_text": "Trash 1 installed program. If you do, install 1 program from your grip or heap, paying X credits less. X is equal to the install cost of the program you trashed.", "stripped_title": "Scavenge", "text": "Trash 1 installed program. If you do, install 1 program from your grip or heap, paying X[credit] less. X is equal to the install cost of the program you trashed.", "title": "Scavenge", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_levy_ar_lab_access_03035(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03035", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Spend too much time in the AR Lab and someone might notice. Unless you're the head of it, that is.", "illustrator": "Lili Ibrahim", "pack_code": "cac", "position": 35, "quantity": 3, "side_code": "runner", "stripped_text": "Shuffle your grip and heap into your stack. Draw 5 cards. Remove Levy AR Lab Access from the game instead of trashing it.", "stripped_title": "Levy AR Lab Access", "text": "Shuffle your grip and heap into your stack. Draw 5 cards. Remove Levy AR Lab Access from the game instead of trashing it.", "title": "Levy AR Lab Access", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_dirty_laundry_03052(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03052", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "The data was better than she could have ever imagined. This Santiago fellow really knew what he was doing. She began to imagine the havoc she could wreak at the upcoming charity dinner\u2026", "illustrator": "Christina Davis", "keywords": "Run", "pack_code": "cac", "position": 52, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. When that run ends, if it was successful, gain 5 credits.", "stripped_title": "Dirty Laundry", "text": "Run any server. When that run ends, if it was successful, gain 5[credit].", "title": "Dirty Laundry", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_frame_job_04001(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04001", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"Bioroid intrusion isn't impossible, despite the bluster of Haas-Bioroid. But it is dangerous.\" -Noise", "illustrator": "Gong Studios", "keywords": "Double", "pack_code": "om", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Forfeit an agenda. If you do, give the Corp 1 bad publicity.", "stripped_title": "Frame Job", "text": "As an additional cost to play this event, spend [click].\nForfeit an agenda. If you do, give the Corp 1 bad publicity.", "title": "Frame Job", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_hostage_04004(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04004", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "om", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Search your stack for a connection, reveal it, and add it to your grip. You may install that connection (paying its install cost). Shuffle your stack.", "stripped_title": "Hostage", "text": "As an additional cost to play this event, spend [click].\nSearch your stack for a <strong>connection</strong>, reveal it, and add it to your grip. You may install that <strong>connection</strong> (paying its install cost). Shuffle your stack.", "title": "Hostage", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_recon_04024(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04024", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Just like in the real world, sometimes it is best to send in the clone to do the dirty work.", "illustrator": "Irys Ching", "keywords": "Run", "pack_code": "st", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. You may jack out when you encounter the first piece of ice.", "stripped_title": "Recon", "text": "Make a run. You may jack out when you encounter the first piece of ice.", "title": "Recon", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_eureka_04027(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04027", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"I've got a surprise for you.\"", "illustrator": "Del Borovic", "keywords": "Double", "pack_code": "st", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Reveal the top card of your stack. You may install that card, lowering the install cost by 10 credits, if able; otherwise, trash it.", "stripped_title": "Eureka!", "text": "As an additional cost to play this event, spend [click].\nReveal the top card of your stack. You may install that card, lowering the install cost by 10[credit], if able; otherwise, trash it.", "title": "Eureka!", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_running_interference_04044(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04044", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "illustrator": "Liiga Smilshkalne", "keywords": "Double - Run", "pack_code": "mt", "position": 44, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Make a run. During this run, the Corp must pay X credits as an additional cost to rez each piece of ice, where X is the rez cost of that ice.", "stripped_title": "Running Interference", "text": "As an additional cost to play this event, spend [click].\nMake a run. During this run, the Corp must pay X[credit] as an additional cost to rez each piece of ice, where X is the rez cost of that ice.", "title": "Running Interference", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_lawyer_up_04063(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04063", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "Pros don't need to call their lawyer. Pros have their secretary rigged to do it for them if they ever go off-grid.", "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "tc", "position": 63, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Remove up to 2 tags and draw 3 cards.", "stripped_title": "Lawyer Up", "text": "As an additional cost to play this event, spend [click].\nRemove up to 2 tags and draw 3 cards.", "title": "Lawyer Up", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_leverage_04064(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04064", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Care to have a look?\"", "illustrator": "Gong Studios", "pack_code": "tc", "position": 64, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on HQ this turn. Prevent all damage until the beginning of your next turn unless the Corp takes 2 bad publicity.", "stripped_title": "Leverage", "text": "Play only if you made a successful run on HQ this turn.\nPrevent all damage until the beginning of your next turn unless the Corp takes 2 bad publicity.", "title": "Leverage", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_quest_completed_04081(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04081", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "That moment of bliss. That feeling of accomplishment. That certainty of purpose.\nWhat's next?", "illustrator": "Gong Studios", "pack_code": "fal", "position": 81, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on R&D, HQ, and Archives this turn. Access 1 installed card (non-ice).", "stripped_title": "Quest Completed", "text": "Play only if you made a successful run on R&D, HQ, and Archives this turn.\nAccess 1 installed card (non-ice).", "title": "Quest Completed", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_executive_wiretaps_04084(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04084", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"When you need someone who is a little more hands on, look me up.\" -Silhouette", "illustrator": "Smirtouille", "keywords": "Double", "pack_code": "fal", "position": 84, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Reveal all cards in HQ.", "stripped_title": "Executive Wiretaps", "text": "As an additional cost to play this event, spend [click].\nReveal all cards in HQ.", "title": "Executive Wiretaps", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_blackmail_04089(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04089", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Gong Studios", "keywords": "Run", "pack_code": "fal", "position": 89, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if the Corp has at least 1 bad publicity. Make a run. The Corp cannot rez ice for the duration of this run.", "stripped_title": "Blackmail", "text": "Play only if the Corp has at least 1 bad publicity.\nMake a run. The Corp cannot rez ice for the duration of this run.", "title": "Blackmail", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_singularity_04101(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04101", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Adam S. Doyle", "keywords": "Double - Run", "pack_code": "dt", "position": 101, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Run a remote server. If successful, instead of breaching that server, trash all cards installed in the root of that server.", "stripped_title": "Singularity", "text": "As an additional cost to play this event, spend [click].\nRun a remote server. If successful, instead of breaching that server, trash all cards installed in the root of that server.", "title": "Singularity", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_queens_gambit_04102(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04102", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "dt", "position": 102, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Place up to 3 advancement counters on 1 unrezzed card in the root of a remote server. Gain 2 credits for each counter placed this way. You cannot access that card for the remainder of the turn.", "stripped_title": "Queen's Gambit", "text": "As an additional cost to play this event, spend [click].\nPlace up to 3 advancement counters on 1 unrezzed card in the root of a remote server. Gain 2[credit] for each counter placed this way. You cannot access that card for the remainder of the turn.", "title": "Queen's Gambit", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_power_nap_04107(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04107", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"When I said I could hack it in my sleep, did you think I was joking?\" -Chaos Theory", "illustrator": "Gong Studios", "keywords": "Double", "pack_code": "dt", "position": 107, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Gain 2 credits. Gain an additional 1 credit for each double event in your heap.", "stripped_title": "Power Nap", "text": "As an additional cost to play this event, spend [click].\nGain 2[credit]. Gain an additional 1[credit] for each <strong>double</strong> event in your heap.", "title": "Power Nap", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_lucky_find_04109(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04109", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 2, "flavor": "Data hunters always pay top dollar for old drives. The more useless the data, the higher the payout.", "illustrator": "Gong Studios", "keywords": "Double", "pack_code": "dt", "position": 109, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Gain 9 credits.", "stripped_title": "Lucky Find", "text": "As an additional cost to play this event, spend [click].\nGain 9[credit].", "title": "Lucky Find", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_calling_in_favors_05031(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05031", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "A job is only as strong as the weakest link. Thankfully Ms. Jones is always on time.", "illustrator": "Jon Bosco", "pack_code": "hap", "position": 31, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 1 credit for each installed connection resource.", "stripped_title": "Calling in Favors", "text": "Gain 1[credit] for each installed <strong>connection</strong> resource.", "title": "Calling in Favors", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_early_bird_05032(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05032", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Tenma clones are excellent at multitasking, their brains custom-made for parallel processing.", "illustrator": "Samuel R. Shimota", "keywords": "Priority - Run", "pack_code": "hap", "position": 32, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. Gain click. Run any server.", "stripped_title": "Early Bird", "text": "Play only as your first click.\nGain [click]. Run any server.", "title": "Early Bird", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_express_delivery_05033(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05033", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "The clone was surprised to see the red-jacketed man. It was like looking in a mirror, only the mirror made him look\u2026cool. Confident. Individual.", "illustrator": "Agri Karuniawan", "pack_code": "hap", "position": 33, "quantity": 3, "side_code": "runner", "stripped_text": "Look at the top 4 cards of your stack and add 1 of those cards to your grip. Shuffle your stack.", "stripped_title": "Express Delivery", "text": "Look at the top 4 cards of your stack and add 1 of those cards to your grip. Shuffle your stack.", "title": "Express Delivery", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_feint_05034(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05034", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Stirling entered the server, passing a growling piece of ice. He was unarmed\u2026or so it seemed.", "illustrator": "Ed Mattinian", "keywords": "Run", "pack_code": "hap", "position": 34, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. The first 2 times this run you encounter a piece of ice, bypass that ice. If successful, you cannot breach HQ.", "stripped_title": "Feint", "text": "Run HQ. The first 2 times this run you encounter a piece of ice, bypass that ice. If successful, you cannot breach HQ.", "title": "Feint", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_legwork_05035(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05035", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"I work by referral only, with an up-front fee. The fee is reasonable if you value results.\" -Silhouette", "illustrator": "Gong Studios", "keywords": "Run", "pack_code": "hap", "position": 35, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, access 2 additional cards when you breach HQ.", "stripped_title": "Legwork", "text": "Run HQ. If successful, access 2 additional cards when you breach HQ.", "title": "Legwork", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_planned_assault_05036(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05036", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Magali Villeneuve", "keywords": "Double", "pack_code": "hap", "position": 36, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Search your stack for a run event and play that run event (paying its play cost), ignoring any additional costs. Shuffle your stack.", "stripped_title": "Planned Assault", "text": "As an additional cost to play this event, spend [click].\nSearch your stack for a <strong>run</strong> event and play that <strong>run</strong> event (paying its play cost), ignoring any additional costs. Shuffle your stack.", "title": "Planned Assault", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_push_your_luck_05047(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05047", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Matt Zeilinger", "pack_code": "hap", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "Secretly spend any number of credits. The Corp guesses if you spent an even or odd amount. Reveal spent credits. If the Corp guessed incorrectly, gain credits equal to twice the amount spent.", "stripped_title": "Push Your Luck", "text": "Secretly spend any number of credits. The Corp guesses if you spent an even or odd amount. Reveal spent credits. If the Corp guessed incorrectly, gain credits equal to twice the amount spent.", "title": "Push Your Luck", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_mass_install_05051(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05051", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Welcome to the mass install wizard! This wizard will guide you through the process of installing a whole mess of programs onto your almost-certainly inadequate rig. When you're ready to continue, say-oops, too late, here we go!\"", "illustrator": "Ed Mattinian", "pack_code": "hap", "position": 51, "quantity": 3, "side_code": "runner", "stripped_text": "Install up to 3 programs from your grip (paying the install costs).", "stripped_title": "Mass Install", "text": "Install up to 3 programs from your grip (paying the install costs).", "title": "Mass Install", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_cyber_threat_06013(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06013", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Matt Zeilinger", "keywords": "Priority", "pack_code": "up", "position": 13, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. Choose a server. The Corp may rez 1 piece of ice protecting that server. If they do not, run that server. The Corp cannot rez ice during that run.", "stripped_title": "Cyber Threat", "text": "Play only as your first [click].\nChoose a server. The Corp may rez 1 piece of ice protecting that server. If they do not, run that server. The Corp cannot rez ice during that run.", "title": "Cyber Threat", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_paper_tripping_06015(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06015", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "His eyes were beginning to blur, as he duplicated the credentials for what seemed like the fiftieth time. Perhaps a genetic refit would have been easier.", "illustrator": "Gong Studios", "keywords": "Priority", "pack_code": "up", "position": 15, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. Remove all tags.", "stripped_title": "Paper Tripping", "text": "Play only as your first [click].\nRemove all tags.", "title": "Paper Tripping", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_social_engineering_06018(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06018", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Ralph Beisner", "keywords": "Priority", "pack_code": "up", "position": 18, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. Choose an unrezzed piece of ice. If the Corp rezzes that piece of ice this turn, gain credits equal to its rez cost.", "stripped_title": "Social Engineering", "text": "Play only as your first [click].\nChoose an unrezzed piece of ice. If the Corp rezzes that piece of ice this turn, gain credits equal to its rez cost.", "title": "Social Engineering", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_scrubbed_06034(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06034", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Chris Newman", "keywords": "Current", "pack_code": "tsb", "position": 34, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. The first piece of ice encountered each turn has -2 strength for the remainder of the run.", "stripped_title": "Scrubbed", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nThe first piece of ice encountered each turn has -2 strength for the remainder of the run.", "title": "Scrubbed", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_three_steps_ahead_06035(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06035", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "In this business, you had to anticipate. If you weren't three steps ahead, you were three steps behind.", "illustrator": "Beny Maulana", "keywords": "Priority", "pack_code": "tsb", "position": 35, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. When this turn ends, gain 2 credits for each successful run you made during it.", "stripped_title": "Three Steps Ahead", "text": "Play only as your first [click].\nWhen this turn ends, gain 2[credit] for each successful run you made during it.", "title": "Three Steps Ahead", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_unscheduled_maintenance_06036(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06036", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "What goes up must always go down.", "illustrator": "Aaron Agregado", "keywords": "Current", "pack_code": "tsb", "position": 36, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. The Corp cannot install more than 1 piece of ice each turn.", "stripped_title": "Unscheduled Maintenance", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nThe Corp cannot install more than 1 piece of ice each turn.", "title": "Unscheduled Maintenance", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_net_celebrity_06038(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06038", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Fifteen seconds of fame.", "illustrator": "Isuardi Therianto", "keywords": "Current", "pack_code": "tsb", "position": 38, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. 1 recurring credit Use this credit during a run.", "stripped_title": "Net Celebrity", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\n1[recurring-credit]\nUse this credit during a run.", "title": "Net Celebrity", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_inject_06073(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06073", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"Knowledge comes in many different shapes and sizes.\" -Quetzal", "illustrator": "Ralph Beisner", "pack_code": "uao", "position": 73, "quantity": 3, "side_code": "runner", "stripped_text": "Reveal the top 4 cards of your stack and trash all programs revealed. Gain 1 credit for each program trashed, and add the rest of the revealed cards to your grip.", "stripped_title": "Inject", "text": "Reveal the top 4 cards of your stack and trash all programs revealed. Gain 1[credit] for each program trashed, and add the rest of the revealed cards to your grip.", "title": "Inject", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_tradein_06078(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06078", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Ralph Beisner", "pack_code": "uao", "position": 78, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, trash an installed piece of hardware. Gain credits equal to half the install cost of the trashed hardware (rounded down) and search your stack for a piece of hardware, reveal it, and add it to your grip. Shuffle your stack.", "stripped_title": "Trade-In", "text": "As an additional cost to play this event, trash an installed piece of hardware.\nGain credits equal to half the install cost of the trashed hardware (rounded down) and search your stack for a piece of hardware, reveal it, and add it to your grip. Shuffle your stack.", "title": "Trade-In", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_code_siphon_06115(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06115", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "illustrator": "Shawn Ye Zhongyi", "keywords": "Run", "pack_code": "ts", "position": 115, "quantity": 3, "side_code": "runner", "stripped_text": "Run R&D. If successful, instead of breaching R&D, you may search your stack for 1 program. Install it, paying 3 credits less for each piece of ice protecting R&D, and then take 1 tag.", "stripped_title": "Code Siphon", "text": "Run R&D. If successful, instead of breaching R&D, you may search your stack for 1 program. Install it, paying 3[credit] less for each piece of ice protecting R&D, and then take 1 tag.", "title": "Code Siphon", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_bribery_06118(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06118", "cost": null, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Sometimes it's helpful to remember that you're not the only one who loves money.\" -Gabriel Santiago", "illustrator": "Bruno Balixa", "keywords": "Run", "pack_code": "ts", "position": 118, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. During this run, the Corp must pay X credits as an additional cost to rez the first unrezzed piece of ice approached.", "stripped_title": "Bribery", "text": "Make a run. During this run, the Corp must pay X[credit] as an additional cost to rez the first unrezzed piece of ice approached.", "title": "Bribery", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_amped_up_07031(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07031", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"The human brain only uses like a quarter of its capacity anyway, right?\" -MaxX", "illustrator": "Wylie Beckert", "pack_code": "oac", "position": 31, "quantity": 3, "side_code": "runner", "stripped_text": "Gain click click click and suffer 1 core damage. This damage cannot be prevented.", "stripped_title": "Amped Up", "text": "Gain [click][click][click] and suffer 1 core damage. This damage cannot be prevented.", "title": "Amped Up", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_ive_had_worse_07032(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07032", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Matt Zeilinger", "pack_code": "oac", "position": 32, "quantity": 3, "side_code": "runner", "stripped_text": "Draw 3 cards. Whenever I've Had Worse is trashed by taking net or meat damage, draw 3 cards.", "stripped_title": "I've Had Worse", "text": "Draw 3 cards.\nWhenever I've Had Worse is trashed by taking net or meat damage, draw 3 cards.", "title": "I've Had Worse", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_itinerant_protesters_07033(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07033", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "No one knows what they want-least of all them.", "illustrator": "Adam Schumpert", "keywords": "Current", "pack_code": "oac", "position": 33, "quantity": 3, "side_code": "runner", "stripped_text": "This event is not trashed until another current is played or an agenda is scored. The Corp gets -1 maximum hand size for each bad publicity they have.", "stripped_title": "Itinerant Protesters", "text": "This event is not trashed until another <strong>current</strong> is played or an agenda is scored.\nThe Corp gets -1 maximum hand size for each bad publicity they have.", "title": "Itinerant Protesters", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_showing_off_07034(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07034", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Adam Schumpert", "keywords": "Run", "pack_code": "oac", "position": 34, "quantity": 3, "side_code": "runner", "stripped_text": "Run R&D. If successful, when you breach R&D, access cards from the bottom of R&D instead of the top.", "stripped_title": "Showing Off", "text": "Run R&D. If successful, when you breach R&D, access cards from the bottom of R&D instead of the top.", "title": "Showing Off", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_wanton_destruction_07035(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07035", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "illustrator": "Chris Newman", "keywords": "Run - Sabotage", "pack_code": "oac", "position": 35, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, instead of breaching HQ, you may spend any number of click to force the Corp to trash that many cards from HQ at random.", "stripped_title": "Wanton Destruction", "text": "Run HQ. If successful, instead of breaching HQ, you may spend any number of [click] to force the Corp to trash that many cards from HQ at random.", "title": "Wanton Destruction", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_day_job_07036(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07036", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"Hello thank you for vidding MegaBuy I'm Carol how can I help you.\"", "illustrator": "Matt Zeilinger", "pack_code": "oac", "position": 36, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click click click. Gain 10 credits.", "stripped_title": "Day Job", "text": "As an additional cost to play this event, spend [click][click][click].\nGain 10[credit].", "title": "Day Job", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_forked_07037(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07037", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Adam S. Doyle", "keywords": "Run - Sabotage", "pack_code": "oac", "position": 37, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. The first time you fully break a sentry during that run, trash that sentry.", "stripped_title": "Forked", "text": "Run any server. The first time you fully break a <strong>sentry</strong> during that run, trash that <strong>sentry</strong>.", "title": "Forked", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_knifed_07038(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07038", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Adam S. Doyle", "keywords": "Run - Sabotage", "pack_code": "oac", "position": 38, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. The first time you fully break a barrier during that run, trash that barrier.", "stripped_title": "Knifed", "text": "Run any server. The first time you fully break a <strong>barrier</strong> during that run, trash that <strong>barrier</strong>.", "title": "Knifed", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_spooned_07039(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07039", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Adam S. Doyle", "keywords": "Run - Sabotage", "pack_code": "oac", "position": 39, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. The first time you fully break a code gate during that run, trash that code gate.", "stripped_title": "Spooned", "text": "Run any server. The first time you fully break a <strong>code gate</strong> during that run, trash that <strong>code gate</strong>.", "title": "Spooned", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_uninstall_07053(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07053", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Runner software is notoriously scratch-built and under-tested, and the shadow net has no tech support. It works, mostly, but sometimes a fresh install is just the ticket.", "illustrator": "Andreas Zafiratos", "pack_code": "oac", "position": 53, "quantity": 3, "side_code": "runner", "stripped_text": "Add an installed program or piece of hardware to your grip.", "stripped_title": "Uninstall", "text": "Add an installed program or piece of hardware to your grip.", "title": "Uninstall", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_traffic_jam_08008(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08008", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "BalanceSheet", "keywords": "Current", "pack_code": "val", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. The advancement requirement of each agenda is increased by 1 for each copy of that agenda in the Corp's score area.", "stripped_title": "Traffic Jam", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nThe advancement requirement of each agenda is increased by 1 for each copy of that agenda in the Corp's score area.", "title": "Traffic Jam", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_hacktivist_meeting_08021(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08021", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "John Ariosa", "keywords": "Current", "pack_code": "bb", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. As an additional cost to rez non-ice cards, the Corp must randomly trash a card from HQ.", "stripped_title": "Hacktivist Meeting", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nAs an additional cost to rez non-ice cards, the Corp must randomly trash a card from HQ.", "title": "Hacktivist Meeting", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_career_fair_08023(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08023", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"You can help Jinteki shape the future. Your future.\"", "illustrator": "Dmitry Prosvirnin", "pack_code": "bb", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "Install 1 resource from your grip, paying 3 credits less.", "stripped_title": "Career Fair", "text": "Install 1 resource from your grip, paying 3[credit] less.", "title": "Career Fair", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_game_day_08026(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08026", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "bb", "position": 26, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. If you have fewer cards in your grip than your maximum hand size, draw cards until you have cards in your grip equal to your maximum hand size.", "stripped_title": "Game Day", "text": "As an additional cost to play this event, spend [click].\nIf you have fewer cards in your grip than your maximum hand size, draw cards until you have cards in your grip equal to your maximum hand size.", "title": "Game Day", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_immolation_script_08041(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08041", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "The most potent scripts are indistinguishable from magic to the sysop on the other side.", "illustrator": "Hannah Christenson", "keywords": "Run", "pack_code": "cc", "position": 41, "quantity": 3, "side_code": "runner", "stripped_text": "Run Archives. If successful, whenever you would access a faceup piece of ice in Archives this run, you may instead trash 1 rezzed copy of that ice. Use this ability only once this run.", "stripped_title": "Immolation Script", "text": "Run Archives. If successful, whenever you would access a faceup piece of ice in Archives this run, you may instead trash 1 rezzed copy of that ice. Use this ability only once this run.", "title": "Immolation Script", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_drive_by_08064(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08064", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Mitchell Malloy", "keywords": "Double", "pack_code": "uw", "position": 64, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Expose 1 card installed in the root of a remote server. If you do and that card is an asset or upgrade, trash it.", "stripped_title": "Drive By", "text": "As an additional cost to play this event, spend [click].\nExpose 1 card installed in the root of a remote server. If you do and that card is an asset or upgrade, trash it.", "title": "Drive By", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_power_to_the_people_08101(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08101", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "As the sun sank towards the horizon, the glittering lights of the expo remained dark. But the shanty city bloomed to life.", "illustrator": "Maciej Rebisz", "keywords": "Priority", "pack_code": "uot", "position": 101, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. The first time you access an agenda this turn, gain 7 credits.", "stripped_title": "Power to the People", "text": "Play only as your first [click].\nThe first time you access an agenda this turn, gain 7[credit].", "title": "Power to the People", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_fisk_investment_seminar_08105(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08105", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"The secret to investing is networking.\" -Laramy Fisk", "illustrator": "Bruno Balixa", "keywords": "Priority", "pack_code": "uot", "position": 105, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. Each player draws 3 cards.", "stripped_title": "Fisk Investment Seminar", "text": "Play only as your first [click].\nEach player draws 3 cards.", "title": "Fisk Investment Seminar", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_apocalypse_09030(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09030", "cost": 3, "deck_limit": 3, "faction_code": "apex", "faction_cost": 3, "flavor": "THE DESTROYER OF WORLDS", "illustrator": "Shawn Ye Zhongyi", "pack_code": "dad", "position": 30, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on HQ, R&D and Archives this turn. Trash all installed Corp cards. Turn all installed Runner cards facedown.", "stripped_title": "Apocalypse", "text": "Play only if you made a successful run on HQ, R&D and Archives this turn.\nTrash all installed Corp cards. Turn all installed Runner cards facedown.", "title": "Apocalypse", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_prey_09031(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09031", "cost": 0, "deck_limit": 3, "faction_code": "apex", "faction_cost": 2, "illustrator": "Ethan Patrick Harris", "keywords": "Run", "pack_code": "dad", "position": 31, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. Once during this run, when you pass a piece of ice, you may trash a number of your installed cards equal to the strength of that ice. If you do, trash that ice.", "stripped_title": "Prey", "text": "Make a run. Once during this run, when you pass a piece of ice, you may trash a number of your installed cards equal to the strength of that ice. If you do, trash that ice.", "title": "Prey", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_independent_thinking_09038(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09038", "cost": 1, "deck_limit": 3, "faction_code": "adam", "faction_cost": 1, "flavor": "Adam raised the hammer. He was free.", "illustrator": "Del Borovic", "pack_code": "dad", "position": 38, "quantity": 3, "side_code": "runner", "stripped_text": "Trash up to 5 of your installed cards. Draw 1 card for each card trashed (or 2 cards for each card trashed if you trashed at least 1 directive).", "stripped_title": "Independent Thinking", "text": "Trash up to 5 of your installed cards. Draw 1 card for each card trashed (or 2 cards for each card trashed if you trashed at least 1 <strong>directive</strong>).", "title": "Independent Thinking", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_employee_strike_09053(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09053", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "\"Are you crazy? We can't send in prisec until the media gets bored and goes home.\"", "illustrator": "Dmitry Prosvirnin", "keywords": "Current", "pack_code": "dad", "position": 53, "quantity": 3, "side_code": "runner", "stripped_text": "This event is not trashed until another current is played or an agenda is scored. The Corp's identity loses its printed abilities.", "stripped_title": "Employee Strike", "text": "This event is not trashed until another <strong>current</strong> is played or an agenda is scored.\nThe Corp's identity loses its printed abilities.", "title": "Employee Strike", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_windfall_09054(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09054", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "She tried to remember who he was. Not that it mattered anymore.", "illustrator": "Rebecca Sorge", "pack_code": "dad", "position": 54, "quantity": 3, "side_code": "runner", "stripped_text": "Shuffle your stack. Trash the top card of your stack. Gain X credits where X is equal to the install cost of that card.", "stripped_title": "Windfall", "text": "Shuffle your stack. Trash the top card of your stack. Gain X[credit] where X is equal to the install cost of that card.", "title": "Windfall", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_run_amok_10001(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10001", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"While there have been other anti-corporation movements before, like the Maroon Wave, this new one is different. It's organized.\" -Ramesh Gupta, One World Economy", "illustrator": "RC Torres", "keywords": "Run - Sabotage", "pack_code": "kg", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. When the run ends, trash 1 piece of ice that was rezzed during this run.", "stripped_title": "Run Amok", "text": "Make a run. When the run ends, trash 1 piece of ice that was rezzed during this run.", "title": "Run Amok", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_highstakes_job_10004(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10004", "cost": 6, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "illustrator": "Adam S. Doyle", "keywords": "Run - Job", "pack_code": "kg", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run on a server with at least 1 piece of unrezzed ice. When the run ends, gain 12 credits if it was successful.", "stripped_title": "High-Stakes Job", "text": "Make a run on a server with at least 1 piece of unrezzed ice. When the run ends, gain 12[credit] if it was successful.", "title": "High-Stakes Job", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_cbi_raid_10022(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10022", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "<strong>Designed by 2013 World Champion Jens Erickson</strong>", "illustrator": "Mike Nesbitt", "keywords": "Run - Sabotage", "pack_code": "bf", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, instead of breaching HQ, the Corp adds all cards in HQ to the top of R&D in the order of their choice.", "stripped_title": "CBI Raid", "text": "Run HQ. If successful, instead of breaching HQ, the Corp adds all cards in HQ to the top of R&D in the order of their choice.", "title": "CBI Raid", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_corporate_scandal_10025(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10025", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "\"We may be outraged, but we're not surprised.\" -Sunder", "illustrator": "Micah Epstein", "keywords": "Current", "pack_code": "bf", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. The Corp has 1 additional bad publicity (even if they have 0).", "stripped_title": "Corporate Scandal", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nThe Corp has 1 additional bad publicity (even if they have 0).", "title": "Corporate Scandal", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_populist_rally_10026(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10026", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"The corporations may be stronger than any of us, but they are not stronger than all of us.\" -Akshara Sareen\u00a0", "illustrator": "Anna Edwards", "pack_code": "bf", "position": 26, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you have a seedy card installed. The Corp gets -1 allotted click for their next turn.", "stripped_title": "Populist Rally", "text": "Play only if you have a <strong>seedy</strong> card installed.\nThe Corp gets -1 allotted [click] for their next turn.", "title": "Populist Rally", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_political_graffiti_10039(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10039", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Chris Newman", "keywords": "Run", "pack_code": "dag", "position": 39, "quantity": 3, "side_code": "runner", "stripped_text": "Run Archives. If successful, instead of breaching Archives, host this event on an agenda in the Corp's score area as a condition counter with \"Host agenda is worth 1 less agenda point. When the Corp purges virus counters, trash this counter.\"", "stripped_title": "Political Graffiti", "text": "Run Archives. If successful, instead of breaching Archives, host this event on an agenda in the Corp's score area as a condition counter with \"Host agenda is worth 1 less agenda point. When the Corp purges virus counters, trash this counter.\"", "title": "Political Graffiti", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_freedom_through_equality_10045(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10045", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Dane Cozens", "keywords": "Current", "pack_code": "dag", "position": 45, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. When you steal an agenda, add \"Freedom Through Equality\" to your score area as an agenda worth 1 agenda point.", "stripped_title": "\"Freedom Through Equality\"", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nWhen you steal an agenda, add \"Freedom Through Equality\" to your score area as an agenda worth 1 agenda point.", "title": "\"Freedom Through Equality\"", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_making_an_entrance_10058(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10058", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Sometimes in an instant you realize who your friends really are.", "illustrator": "Kate Laird", "keywords": "Priority", "pack_code": "si", "position": 58, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. Look at the top 6 cards of your stack. You may trash any of those cards and arrange the rest in any order.", "stripped_title": "Making an Entrance", "text": "Play only as your first [click].\nLook at the top 6 cards of your stack. You may trash any of those cards and arrange the rest in any order.", "title": "Making an Entrance", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_exclusive_party_10060(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10060", "cost": 0, "deck_limit": 6, "faction_code": "criminal", "faction_cost": 1, "flavor": "The more parties she attended, the more they trusted her. The more they trusted her, the more entertaining her scams became.", "illustrator": "Caroline Gariba", "pack_code": "si", "position": 60, "quantity": 6, "side_code": "runner", "stripped_text": "Draw 1 card. Gain 1 credit for each copy of Exclusive Party in your heap. Limit 6 per deck.", "stripped_title": "Exclusive Party", "text": "Draw 1 card. Gain 1[credit] for each copy of Exclusive Party in your heap.\nLimit 6 per deck.", "title": "Exclusive Party", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_the_noble_path_10077(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10077", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"He with nothing to lose has strength beyond imagining.\"\n-The Saffron Sutra", "illustrator": "Chris Knight", "keywords": "Run", "pack_code": "tlm", "position": 77, "quantity": 3, "side_code": "runner", "stripped_text": "Trash your grip. Make a run. Prevent all damage during this run.", "stripped_title": "The Noble Path", "text": "Trash your grip. Make a run. Prevent all damage during this run.", "title": "The Noble Path", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_information_sifting_10079(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10079", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "illustrator": "A. Jones", "keywords": "Run", "pack_code": "tlm", "position": 79, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, instead of breaching HQ, the Corp separates all cards in HQ into 2 facedown piles. Choose 1 of the piles. Access each card in the chosen pile.", "stripped_title": "Information Sifting", "text": "Run HQ. If successful, instead of breaching HQ, the Corp separates all cards in HQ into 2 facedown piles. Choose 1 of the piles. Access each card in the chosen pile.", "title": "Information Sifting", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_out_of_the_ashes_10080(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10080", "cost": 1, "deck_limit": 6, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Kari Guenther", "keywords": "Run", "pack_code": "tlm", "position": 80, "quantity": 6, "side_code": "runner", "stripped_text": "Make a run. When your turn begins, if Out of the Ashes is in your heap, you may remove it from the game to make a run. Limit 6 per deck.", "stripped_title": "Out of the Ashes", "text": "Make a run.\nWhen your turn begins, if Out of the Ashes is in your heap, you may remove it from the game to make a run.\nLimit 6 per deck.", "title": "Out of the Ashes", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_rebirth_10083(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10083", "cost": 0, "deck_limit": 1, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "\"Who were you when you realized everything you knew was a lie?\"", "illustrator": "Hannah Christenson", "pack_code": "tlm", "position": 83, "quantity": 3, "side_code": "runner", "stripped_text": "Switch your identity with another identity from the same faction. Remove Rebirth from the game instead of trashing it. Limit 1 per deck.", "stripped_title": "Rebirth", "text": "Switch your identity with another identity from the same faction. Remove Rebirth from the game instead of trashing it.\nLimit 1 per deck.", "title": "Rebirth", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_fear_the_masses_10096(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10096", "cost": 1, "deck_limit": 6, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Maciej Rebisz", "keywords": "Run - Sabotage", "pack_code": "ftm", "position": 96, "quantity": 6, "side_code": "runner", "stripped_text": "Run HQ. If successful, instead of breaching HQ, reveal any number of copies of Fear the Masses from your grip. The Corp trashes X cards from the top of R&D, where X is equal to 1 plus the number of cards you revealed. Limit 6 per deck.", "stripped_title": "Fear the Masses", "text": "Run HQ. If successful, instead of breaching HQ, reveal any number of copies of Fear the Masses from your grip. The Corp trashes X cards from the top of R&D, where X is equal to 1 plus the number of cards you revealed.\nLimit 6 per deck.", "title": "Fear the Masses", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_the_price_of_freedom_10100(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10100", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Adam Schumpert", "pack_code": "ftm", "position": 100, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, trash 1 installed connection resource. The Corp cannot advance cards during their next turn. Remove this event from the game.", "stripped_title": "The Price of Freedom", "text": "As an additional cost to play this event, trash 1 installed <strong>connection</strong> resource.\nThe Corp cannot advance cards during their next turn.\nRemove this event from the game.", "title": "The Price of Freedom", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_rigged_results_10102(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10102", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "illustrator": "Nasrul Hakim", "pack_code": "ftm", "position": 102, "quantity": 3, "side_code": "runner", "stripped_text": "Secretly spend up to 2 credits. The Corp guesses how much you spent. Reveal spent credits. If the Corp guessed incorrectly, choose a piece of ice protecting a server and run that server. The first time during this run you encounter the chosen ice, bypass it.", "stripped_title": "Rigged Results", "text": "Secretly spend up to 2[credit]. The Corp guesses how much you spent. Reveal spent credits. If the Corp guessed incorrectly, choose a piece of ice protecting a server and run that server. The first time during this run you encounter the chosen ice, bypass it.", "title": "Rigged Results", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_system_outage_11001(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11001", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Meg Owenson", "keywords": "Current", "pack_code": "23s", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "This event is not trashed until another current is played or an agenda is scored. Whenever the Corp draws 1 or more cards, if it is not the first time they have drawn cards this turn, they lose 1 credit.", "stripped_title": "System Outage", "text": "This event is not trashed until another <strong>current</strong> is played or an agenda is scored.\nWhenever the Corp draws 1 or more cards, if it is not the first time they have drawn cards this turn, they lose 1[credit].", "title": "System Outage", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_another_day_another_paycheck_11007(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11007", "cost": 0, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 3, "illustrator": "Caroline Gariba", "keywords": "Current", "pack_code": "23s", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. Whenever you steal an agenda, force the Corp to \"Trace[0]. If unsuccessful, the Runner gains credits equal to the number of agenda points in both players' score areas.\"", "stripped_title": "Another Day, Another Paycheck", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nWhenever you steal an agenda, force the Corp to \"Trace[0]. If unsuccessful, the Runner gains credits equal to the number of agenda points in both players' score areas.\"", "title": "Another Day, Another Paycheck", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_deuces_wild_11008(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11008", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "<strong>Designed by 2014 World Champion Dan D'Argenio</strong>", "illustrator": "Marjorie Davis", "pack_code": "23s", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "Resolve two of the following in any order: * Gain 3 credits. * Draw 2 cards. * Remove 1 tag. * Expose 1 piece of ice, then make a run.", "stripped_title": "Deuces Wild", "text": "Resolve two of the following in any order:<ul><li>Gain 3[credit].</li><li>Draw 2 cards.</li><li>Remove 1 tag.</li><li>Expose 1 piece of ice, then make a run.</li></ul>", "title": "Deuces Wild", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_injection_attack_11009(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11009", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "They call it \"running\" because jacking in is mentally and physically exhausting.", "illustrator": "Chris Newman", "keywords": "Run", "pack_code": "23s", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "Choose 1 installed icebreaker and run any server. During that run, the chosen icebreaker gets +2 strength.", "stripped_title": "Injection Attack", "text": "Choose 1 installed <strong>icebreaker</strong> and run any server. During that run, the chosen <strong>icebreaker</strong> gets +2 strength.", "title": "Injection Attack", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_credit_crash_11021(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11021", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Jenn Tran", "keywords": "Run", "pack_code": "bm", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. Trash the first non-agenda card you access during this run at no cost. The Corp can spend credits equal to the rez or play cost of the accessed card to prevent this trash.", "stripped_title": "Credit Crash", "text": "Make a run. Trash the first non-agenda card you access during this run at no cost. The Corp can spend credits equal to the rez or play cost of the accessed card to prevent this trash.", "title": "Credit Crash", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_rumor_mill_11022(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11022", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"You can have a lot of fun in 23 seconds.\" -Princess Space Kitten", "illustrator": "Tim Durning", "keywords": "Current", "pack_code": "bm", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. Each unique non-region asset and upgrade loses its printed abilities.", "stripped_title": "Rumor Mill", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nEach unique (\u2666) non-<strong>region</strong> asset and upgrade loses its printed abilities.", "title": "Rumor Mill", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_data_breach_11028(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11028", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Once a security flaw is identified, there's only a limited window to exploit it before it's patched. Runners call this period \"open season.\"", "illustrator": "Juan Novelletto", "keywords": "Run", "pack_code": "bm", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run on R&D. If successful, you may make another run on R&D when this run ends.", "stripped_title": "Data Breach", "text": "Make a run on R&D. If successful, you may make another run on R&D when this run ends.", "title": "Data Breach", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_en_passant_11061(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11061", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"When your opponent is weak, strike. If you do not, he will become strong.\" - the Playbook", "illustrator": "Lili Ibrahim", "keywords": "Sabotage", "pack_code": "in", "position": 61, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run this turn. Trash 1 unrezzed piece of ice you passed during your last run.", "stripped_title": "En Passant", "text": "Play only if you made a successful run this turn.\nTrash 1 unrezzed piece of ice you passed during your last run.", "title": "En Passant", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_frantic_coding_11062(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11062", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Omar goes through four, five keyboards per week, no two from the same decade.", "illustrator": "Nasrul Hakim", "pack_code": "in", "position": 62, "quantity": 3, "side_code": "runner", "stripped_text": "Look at the top 10 cards of your stack. If any of those cards are programs, you may install one of them, lowering the install cost by 5. Trash the rest of those cards.", "stripped_title": "Frantic Coding", "text": "Look at the top 10 cards of your stack. If any of those cards are programs, you may install one of them, lowering the install cost by 5. Trash the rest of those cards.", "title": "Frantic Coding", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_government_investigations_11069(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11069", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Take this to Inez Delgado in Netcrimes. No one else.\"", "illustrator": "Leanna Crossan", "keywords": "Current", "pack_code": "in", "position": 69, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. While secretly spending credits, players cannot spend 2 credits.", "stripped_title": "Government Investigations", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nWhile secretly spending credits, players cannot spend 2[credit].", "title": "Government Investigations", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_on_the_lam_11082(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11082", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Never, ever, overstay your welcome.\" -Andromeda", "illustrator": "A. Jones", "keywords": "Condition", "pack_code": "ml", "position": 82, "quantity": 3, "side_code": "runner", "stripped_text": "Install On the Lam on a resource as a hosted condition counter with the text \"trash: Avoid up to 3 tags or prevent up to 3 damage.\"", "stripped_title": "On the Lam", "text": "Install On the Lam on a resource as a hosted condition counter with the text \"[trash]: Avoid up to 3 tags or prevent up to 3 damage.\"", "title": "On the Lam", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_cold_read_11083(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11083", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Her ability to analyze and adapt mid-run bordered on the paranormal.", "illustrator": "Hannah Christenson", "keywords": "Run - Stealth", "pack_code": "ml", "position": 83, "quantity": 3, "side_code": "runner", "stripped_text": "Place 4 credits on this event, then run any server. You can spend hosted credits during that run. When that run ends, trash 1 installed program you used during that run. Trashing a program this way cannot be prevented.", "stripped_title": "Cold Read", "text": "Place 4[credit] on this event, then run any server. You can spend hosted credits during that run. When that run ends, trash 1 installed program you used during that run. Trashing a program this way cannot be prevented.", "title": "Cold Read", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_interdiction_11087(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11087", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "This is my USMC-XOB32. There are many like it, but this one is mine.", "illustrator": "VIKO", "keywords": "Current", "pack_code": "ml", "position": 87, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. The Corp cannot rez non-ice cards during the Runner's turn.", "stripped_title": "Interdiction", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nThe Corp cannot rez non-ice cards during the Runner's turn.", "title": "Interdiction", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_encore_11107(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11107", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "illustrator": "Aurore Folny", "pack_code": "qu", "position": 107, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on R&D, HQ, and Archives this turn. Take an additional turn after this one. Remove Encore from the game instead of trashing it.", "stripped_title": "Encore", "text": "Play only if you made a successful run on R&D, HQ, and Archives this turn.\nTake an additional turn after this one. Remove Encore from the game instead of trashing it.", "title": "Encore", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_peace_in_our_time_11109(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11109", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "illustrator": "Alexandr Elichev", "keywords": "Priority", "pack_code": "qu", "position": 109, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click and only if the Corp scored no agendas during their last turn. Gain 10 credits. The Corp gains 5 credits. You cannot make any runs this turn.", "stripped_title": "Peace in Our Time", "text": "Play only as your first [click] and only if the Corp scored no agendas during their last turn.\nGain 10[credit]. The Corp gains 5[credit]. You cannot make any runs this turn.", "title": "Peace in Our Time", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_pushing_the_envelope_12001(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12001", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"Hitting them when they are weakest sometimes means acting before you want to.\" -Alice Merchant", "illustrator": "Adam S. Doyle", "keywords": "Run", "pack_code": "dc", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. If you have 2 or fewer cards in your grip, each installed icebreaker has +2 strength until the end of the run.", "stripped_title": "Pushing the Envelope", "text": "Make a run. If you have 2 or fewer cards in your grip, each installed <strong>icebreaker</strong> has +2 strength until the end of the run.", "title": "Pushing the Envelope", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_exploit_12004(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12004", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "1) Find the weakness.\n2) Exploit the weakness.\n3) Repeat.", "illustrator": "Nasrul Hakim", "pack_code": "dc", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on R&D, HQ, and Archives this turn. Derez up to 3 pieces of ice.", "stripped_title": "Exploit", "text": "Play only if you made a successful run on R&D, HQ, and Archives this turn.\nDerez up to 3 pieces of ice.", "title": "Exploit", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_spot_the_prey_12005(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12005", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"So, yeah, I just reverse engineered a tracer, and then built it back up with some new lines of code. Pretty stellar.\" -Los", "illustrator": "Camille Kuo", "pack_code": "dc", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "Expose 1 non-ice card, then make a run.", "stripped_title": "Spot the Prey", "text": "Expose 1 non-ice card, then make a run.", "title": "Spot the Prey", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_mad_dash_12008(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12008", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Alexandr Elichev", "keywords": "Run", "pack_code": "dc", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. When this run ends, add Mad Dash to your score area as an agenda worth 1 agenda point if you stole at least 1 agenda during the run; otherwise, suffer 1 meat damage.", "stripped_title": "Mad Dash", "text": "Make a run. When this run ends, add Mad Dash to your score area as an agenda worth 1 agenda point if you stole at least 1 agenda during the run; otherwise, suffer 1 meat damage.", "title": "Mad Dash", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_mobius_12024(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12024", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Liiga Smilshkalne", "keywords": "Run", "pack_code": "so", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run on R&D. If successful, you may make another run on R&D when this run ends. If the second run is successful, gain 4 credits.", "stripped_title": "Mobius", "text": "Make a run on R&D. If successful, you may make another run on R&D when this run ends. If the second run is successful, gain 4[credit].", "title": "M\u00f6bius", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_system_seizure_12026(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12026", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "illustrator": "Ethan Patrick Harris", "keywords": "Current", "pack_code": "so", "position": 26, "quantity": 3, "side_code": "runner", "stripped_text": "This event is not trashed until another current is played or an agenda is scored. Interrupt -> The first time each turn you would increase the strength of an icebreaker, for the remainder of the run that icebreaker gains \"Abilities that increase this program's strength last for the remainder of the run (instead of any shorter duration).\"", "stripped_title": "System Seizure", "text": "This event is not trashed until another <strong>current</strong> is played or an agenda is scored.\n[interrupt] \u2192 The first time each turn you would increase the strength of an <strong>icebreaker</strong>, for the remainder of the run that <strong>icebreaker</strong> gains \"Abilities that increase this program's strength last for the remainder of the run <em>(instead of any shorter duration)</em>.\"", "title": "System Seizure", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_build_script_12028(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12028", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "Sometimes efficiency is as easy as offloading routine work to a dedicated handler.", "illustrator": "Ed Mattinian", "pack_code": "so", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 1 credit and draw 2 cards.", "stripped_title": "Build Script", "text": "Gain 1[credit] and draw 2 cards.", "title": "Build Script", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_mars_for_martians_12081(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12081", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"We don't want you! We don't need you!\"", "illustrator": "Darren Tan", "keywords": "Priority", "pack_code": "fm", "position": 81, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. Draw 1 card for each installed clan resource. Gain 1 credit for each tag you have.", "stripped_title": "Mars for Martians", "text": "Play only as your first [click].\nDraw 1 card for each installed <strong>clan</strong> resource. Gain 1[credit] for each tag you have.", "title": "Mars for Martians", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_leave_no_trace_12083(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12083", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"The Perfect Run is when you get in, take something of value, and get back out, with no one knowing you've ever been there.\" -g00ru", "illustrator": "Shawn Ye Zhongyi", "keywords": "Run", "pack_code": "fm", "position": 83, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. When the run ends, derez all ice that was rezzed during this run.", "stripped_title": "Leave No Trace", "text": "Make a run. When the run ends, derez all ice that was rezzed during this run.", "title": "Leave No Trace", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_rip_deal_12084(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12084", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Hannah Christenson", "keywords": "Run", "pack_code": "fm", "position": 84, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, when you determine the number of cards in HQ you are allowed to access during this run's breach of HQ, you may add that many cards from your heap to your grip. If you do, you cannot access any cards in HQ during this breach. (You can still access cards in the root of HQ.) When the run ends, remove this event from the game.", "stripped_title": "Rip Deal", "text": "Run HQ. If successful, when you determine the number of cards in HQ you are allowed to access during this run's breach of HQ, you may add that many cards from your heap to your grip. If you do, you cannot access any cards in HQ during this breach. <em>(You can still access cards in the root of HQ.)</em>\nWhen the run ends, remove this event from the game.", "title": "Rip Deal", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_lean_and_mean_12086(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12086", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"The question isn't 'should I do it?' the question is 'can I do it?'\" -Kabonesa Wu", "illustrator": "Aurore Folny", "keywords": "Run", "pack_code": "fm", "position": 86, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. If you have 3 or fewer programs installed, all icebreakers have +2 strength during this run.", "stripped_title": "Lean and Mean", "text": "Make a run. If you have 3 or fewer programs installed, all <strong>icebreakers</strong> have +2 strength during this run.", "title": "Lean and Mean", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_mining_accident_12101(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12101", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Ed Mattinian", "pack_code": "cd", "position": 101, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on a central server this turn. The Corp must pay 5 credits or take 1 bad publicity. Remove Mining Accident from the game instead of trashing it.", "stripped_title": "Mining Accident", "text": "Play only if you made a successful run on a central server this turn.\nThe Corp must pay 5[credit] or take 1 bad publicity. Remove Mining Accident from the game instead of trashing it.", "title": "Mining Accident", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_dianas_hunt_12106(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12106", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "illustrator": "Ethan Patrick Harris", "keywords": "Run", "pack_code": "cd", "position": 106, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. Whenever you encounter a piece of ice during this run, you may install a program from your grip, ignoring all costs. When this run ends, trash all programs installed using Diana's Hunt.", "stripped_title": "Diana's Hunt", "text": "Make a run. Whenever you encounter a piece of ice during this run, you may install a program from your grip, ignoring all costs. When this run ends, trash all programs installed using Diana's Hunt.", "title": "Diana's Hunt", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_reshape_12107(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12107", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "\"I wield the power cosmic\u2014a galactic force that can reshape the Net!\" -S'onge Galaxy", "illustrator": "Alexander Tooth", "pack_code": "cd", "position": 107, "quantity": 3, "side_code": "runner", "stripped_text": "Swap 2 pieces of unrezzed ice.", "stripped_title": "Reshape", "text": "Swap 2 pieces of unrezzed ice.", "title": "Reshape", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_bruteforcehack_13002(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13002", "cost": null, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Bypassing a system's defenses by cutting physical wires is what I like to call old school.\" - Steve Cambridge", "illustrator": "Jason Juta", "keywords": "Double", "pack_code": "td", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Derez a piece of ice that has a rez cost of X or lower.", "stripped_title": "Brute-Force-Hack", "text": "As an additional cost to play this event, spend [click].\nDerez a piece of ice that has a rez cost of X or lower.", "title": "Brute-Force-Hack", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_spear_phishing_13003(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13003", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Targeted attacks make system breaches so much easier, especially if you can spoof an authorized user.", "illustrator": "Andreas Zafiratos", "keywords": "Run", "pack_code": "td", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. When you encounter the innermost piece of ice protecting that server, bypass it.", "stripped_title": "Spear Phishing", "text": "Make a run. When you encounter the innermost piece of ice protecting that server, bypass it.", "title": "Spear Phishing", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_syn_attack_13004(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13004", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Flooding the system with synchronized request messages makes it unresponsive to legitimate requests.", "illustrator": "Alexandr Elichev", "keywords": "Double", "pack_code": "td", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. The Corp must either discard 2 cards or draw 4 cards.", "stripped_title": "SYN Attack", "text": "As an additional cost to play this event, spend [click].\nThe Corp must either discard 2 cards or draw 4 cards.", "title": "SYN Attack", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_careful_planning_13013(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13013", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "Each AI had been tasked with finding a solution to the same problem but with different variables.", "illustrator": "Mark Molnar", "keywords": "Priority", "pack_code": "td", "position": 13, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. Choose 1 card installed in the root of or protecting a remote server. That card cannot be rezzed this turn.", "stripped_title": "Careful Planning", "text": "Play only as your first [click].\nChoose 1 card installed in the root of or protecting a remote server. That card cannot be rezzed this turn.", "title": "Careful Planning", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_deep_data_mining_13014(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13014", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "Extracting data from complex systems is what running is all about.", "illustrator": "Alexandr Elichev", "keywords": "Run", "pack_code": "td", "position": 14, "quantity": 3, "side_code": "runner", "stripped_text": "Run R&D. If successful, access X additional cards when you breach R&D. X is equal to your unused MU or 4, whichever is less.", "stripped_title": "Deep Data Mining", "text": "Run R&D. If successful, access X additional cards when you breach R&D. X is equal to your unused MU or 4, whichever is less.", "title": "Deep Data Mining", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_process_automation_13023(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13023", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "Restructuring labor resources.", "illustrator": "Ed Mattinian", "pack_code": "td", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 2 credits and draw 1 card.", "stripped_title": "Process Automation", "text": "Gain 2[credit] and draw 1 card.", "title": "Process Automation", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_security_leak_14009(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "14009", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Jason Juta", "keywords": "Current", "pack_code": "tdc", "position": 24, "quantity": 1, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. As an additional cost to advance a card, the Corp must pay 1 credit.", "stripped_title": "Security Leak", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nAs an additional cost to advance a card, the Corp must pay 1[credit].", "title": "Security Leak", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_demolition_run_20002(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20002", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "You ever set something on fire just to watch it burn?", "illustrator": "Anna Ignatieva", "keywords": "Run - Sabotage", "pack_code": "core2", "position": 2, "quantity": 2, "side_code": "runner", "stripped_text": "Run HQ or R&D. Access -> 0 credits: Trash the card you are accessing.", "stripped_title": "Demolition Run", "text": "Run HQ or R&D.\nAccess \u2192 <strong>0[credit]:</strong> Trash the card you are accessing.", "title": "Demolition Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_retrieval_run_20003(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20003", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Outland Entertainment LLC", "keywords": "Run", "pack_code": "core2", "position": 3, "quantity": 2, "side_code": "runner", "stripped_text": "Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.", "stripped_title": "Retrieval Run", "text": "Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.", "title": "Retrieval Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_singularity_20004(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20004", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Adam S. Doyle", "keywords": "Double - Run", "pack_code": "core2", "position": 4, "quantity": 1, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Run a remote server. If successful, instead of breaching that server, trash all cards installed in the root of that server.", "stripped_title": "Singularity", "text": "As an additional cost to play this event, spend [click].\nRun a remote server. If successful, instead of breaching that server, trash all cards installed in the root of that server.", "title": "Singularity", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_stimhack_20005(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20005", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Andreas Zafiratos", "keywords": "Run", "pack_code": "core2", "position": 5, "quantity": 1, "side_code": "runner", "stripped_text": "Place 9 credits on this event, then run any server. During that run, hosted credits are considered to be in your credit pool. When that run ends, suffer 1 core damage. This damage cannot be prevented.", "stripped_title": "Stimhack", "text": "Place 9[credit] on this event, then run any server. During that run, hosted credits are considered to be in your credit pool. When that run ends, suffer 1 core damage. This damage cannot be prevented.", "title": "Stimhack", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_easy_mark_20020(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20020", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"Hey kid, you fire that up now, bound to be vamped real bad. Some real pathetic individuals around here. But thankfully I got just the ticket\u2026\"", "illustrator": "Matt Zeilinger", "keywords": "Job", "pack_code": "core2", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 3 credits.", "stripped_title": "Easy Mark", "text": "Gain 3[credit].", "title": "Easy Mark", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_emergency_shutdown_20021(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20021", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Think of it as a virtual shock collar for punishing corporate pets.\" -Andromeda", "illustrator": "Adam S. Doyle", "keywords": "Sabotage", "pack_code": "core2", "position": 21, "quantity": 2, "side_code": "runner", "stripped_text": "Play only if you made a successful run on HQ this turn. Derez 1 installed piece of ice.", "stripped_title": "Emergency Shutdown", "text": "Play only if you made a successful run on HQ this turn.\nDerez 1 installed piece of ice.", "title": "Emergency Shutdown", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_forged_activation_orders_20022(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20022", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "As the hysteria in the room climbed higher up the corporate chain, an uneasy feeling of joblessness began to sink in on the lower rungs.", "illustrator": "Antonio De Luca", "keywords": "Sabotage", "pack_code": "core2", "position": 22, "quantity": 2, "side_code": "runner", "stripped_text": "Choose 1 unrezzed piece of ice. The Corp may rez that ice. If they do not, they trash it.", "stripped_title": "Forged Activation Orders", "text": "Choose 1 unrezzed piece of ice. The Corp may rez that ice. If they do not, they trash it.", "title": "Forged Activation Orders", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_inside_job_20023(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20023", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Hey, listen, I'm not asking you to do anything dangerous. Just let me into the building. And tell me which room has the weakest security. And please don't say 'the bathroom' again.\"", "illustrator": "Clark Huggins", "keywords": "Run", "pack_code": "core2", "position": 23, "quantity": 2, "side_code": "runner", "stripped_text": "Run any server. The first time this run you encounter a piece of ice, bypass it.", "stripped_title": "Inside Job", "text": "Run any server. The first time this run you encounter a piece of ice, bypass it.", "title": "Inside Job", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_special_order_20024(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20024", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Feverishly tracking its frustratingly slow progress across the Pacific, the package finally shows up hours later\u2026", "illustrator": "Steve Hamilton", "pack_code": "core2", "position": 24, "quantity": 1, "side_code": "runner", "stripped_text": "Search your stack for an icebreaker, reveal it, and add it to your grip. Shuffle your stack.", "stripped_title": "Special Order", "text": "Search your stack for an <strong>icebreaker</strong>, reveal it, and add it to your grip. Shuffle your stack.", "title": "Special Order", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_diesel_20038(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20038", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Diesel gives you flames.", "illustrator": "Tim Durning", "pack_code": "core2", "position": 38, "quantity": 2, "side_code": "runner", "stripped_text": "Draw 3 cards.", "stripped_title": "Diesel", "text": "Draw 3 cards.", "title": "Diesel", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_indexing_20039(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20039", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "A little corporate restructuring is necessary once in a while.", "illustrator": "Mauricio Herrera", "keywords": "Run", "pack_code": "core2", "position": 39, "quantity": 2, "side_code": "runner", "stripped_text": "Run R&D. If successful, instead of breaching R&D, you may look at the top 5 cards of R&D and arrange them in any order.", "stripped_title": "Indexing", "text": "Run R&D. If successful, instead of breaching R&D, you may look at the top 5 cards of R&D and arrange them in any order.", "title": "Indexing", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_modded_20040(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20040", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "There's no replacement for a home-grown program. Fed on late nights, oaty bars, and single-minded determination. Cheaper, too.", "illustrator": "Kate Laird", "keywords": "Mod", "pack_code": "core2", "position": 40, "quantity": 3, "side_code": "runner", "stripped_text": "Install a program or piece of hardware, lowering the install cost by 3.", "stripped_title": "Modded", "text": "Install a program or piece of hardware, lowering the install cost by 3.", "title": "Modded", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_notoriety_20041(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20041", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "When you're this good, it's hard not to grow a fan base.", "illustrator": "Matt Zeilinger", "pack_code": "core2", "position": 41, "quantity": 1, "side_code": "runner", "stripped_text": "Play only if you made a successful run on R&D, HQ, and Archives this turn. Add Notoriety to your score area as an agenda worth 1 agenda point.", "stripped_title": "Notoriety", "text": "Play only if you made a successful run on R&D, HQ, and Archives this turn.\nAdd Notoriety to your score area as an agenda worth 1 agenda point.", "title": "Notoriety", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_test_run_20042(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20042", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Kate Laird", "pack_code": "core2", "position": 42, "quantity": 2, "side_code": "runner", "stripped_text": "Search either your stack or your heap for 1 program. (Shuffle your stack if you searched it.) Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.", "stripped_title": "Test Run", "text": "Search either your stack or your heap for 1 program. <em>(Shuffle your stack if you searched it.)</em> Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.", "title": "Test Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_the_makers_eye_20043(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20043", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Some of the professionals have good instincts, but they can't see beyond the data. They can't see the matrix.\" -Ele \"Smoke\" Scovak", "illustrator": "Liiga Smilshkalne", "keywords": "Run", "pack_code": "core2", "position": 43, "quantity": 1, "side_code": "runner", "stripped_text": "Run R&D. If successful, access 2 additional cards when you breach R&D.", "stripped_title": "The Maker's Eye", "text": "Run R&D. If successful, access 2 additional cards when you breach R&D.", "title": "The Maker's Eye", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_tinkering_20044(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20044", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "\"There's that moment, you know, when the whole world seems to fall away and it is only you and your mod, and the mod is the world.\"", "illustrator": "Christina Davis", "keywords": "Mod", "pack_code": "core2", "position": 44, "quantity": 2, "side_code": "runner", "stripped_text": "Choose a piece of ice. That ice gains sentry, code gate, and barrier until the end of the turn.", "stripped_title": "Tinkering", "text": "Choose a piece of ice. That ice gains <strong>sentry</strong>, <strong>code gate</strong>, and <strong>barrier</strong> until the end of the turn.", "title": "Tinkering", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_infiltration_20055(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20055", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Bring back any memories, Monica?\" -John \"Animal\" McEvoy", "illustrator": "Imaginary FS Pte Ltd", "pack_code": "core2", "position": 55, "quantity": 2, "side_code": "runner", "stripped_text": "Gain 2 credits or expose 1 card.", "stripped_title": "Infiltration", "text": "Gain 2[credit] or expose 1 card.", "title": "Infiltration", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_sure_gamble_20056(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20056", "cost": 5, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Lady Luck took the form of a hifi quantum manipulation ring that she wore on her middle finger.", "illustrator": "Kate Niemczyk", "pack_code": "core2", "position": 56, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 9 credits.", "stripped_title": "Sure Gamble", "text": "Gain 9[credit].", "title": "Sure Gamble", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_by_any_means_21001(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21001", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 5, "illustrator": "Le Vuong", "keywords": "Priority - Sabotage", "pack_code": "ss", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. For the remainder of the turn, whenever you access a card not in Archives, trash it and suffer 1 meat damage.", "stripped_title": "By Any Means", "text": "Play only as your first [click].\nFor the remainder of the turn, whenever you access a card not in Archives, trash it and suffer 1 meat damage.", "title": "By Any Means", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_credit_kiting_21023(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21023", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "The gap of 0.19 seconds was all he needed.", "illustrator": "Caravan Studio", "pack_code": "dtwn", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on a central server this turn. Install a card from your grip, lowering its install cost by 8 credits, and take 1 tag.", "stripped_title": "Credit Kiting", "text": "Play only if you made a successful run on a central server this turn.\nInstall a card from your grip, lowering its install cost by 8[credit], and take 1 tag.", "title": "Credit Kiting", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_emergent_creativity_21028(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21028", "cost": 2, "deck_limit": 3, "faction_code": "adam", "faction_cost": 5, "illustrator": "Caravan Studio", "keywords": "Double", "pack_code": "dtwn", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Trash any number of programs and/or pieces of hardware from your grip. Search your stack for 1 program or piece of hardware. Install it, paying X credits less. X is equal to the total install cost of the trashed cards.", "stripped_title": "Emergent Creativity", "text": "As an additional cost to play this event, spend [click].\nTrash any number of programs and/or pieces of hardware from your grip. Search your stack for 1 program or piece of hardware. Install it, paying X[credit] less. X is equal to the total install cost of the trashed cards.", "title": "Emergent Creativity", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_corporate_grant_21044(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21044", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "You'd think someone would have noticed a program entitled \"Career Opportunities in Hacking\" earlier.", "illustrator": "PxelSlayer", "keywords": "Current", "pack_code": "cotc", "position": 44, "quantity": 3, "side_code": "runner", "stripped_text": "This card is not trashed until another current is played or an agenda is scored. The first time you install a card each turn, the Corp loses 1 credit.", "stripped_title": "Corporate \"Grant\"", "text": "This card is not trashed until another <strong>current</strong> is played or an agenda is scored.\nThe first time you install a card each turn, the Corp loses 1[credit].", "title": "Corporate \"Grant\"", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_marathon_21046(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21046", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 5, "illustrator": "Liiga Smilshkalne", "keywords": "Run", "pack_code": "cotc", "position": 46, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run on a remote server. When the run ends, gain click and add Marathon to your grip instead of trashing it if the run was successful. You may not make another run on that server for the remainder of this turn.", "stripped_title": "Marathon", "text": "Make a run on a remote server. When the run ends, gain [click] and add Marathon to your grip instead of trashing it if the run was successful. You may not make another run on that server for the remainder of this turn.", "title": "Marathon", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_white_hat_21048(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21048", "cost": 0, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 5, "illustrator": "Ed Mattinian", "pack_code": "cotc", "position": 48, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on a central server this turn. Force the Corp to \"Trace[3]. If unsuccessful, reveal all cards in HQ. The Runner may choose up to 2 of the revealed cards. Shuffle those cards into R&D.\"", "stripped_title": "White Hat", "text": "Play only if you made a successful run on a central server this turn.\nForce the Corp to \"Trace[3]. If unsuccessful, reveal all cards in HQ. The Runner may choose up to 2 of the revealed cards. Shuffle those cards into R&D.\"", "title": "White Hat", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_glut_cipher_21061(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21061", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "\"Ever watch a server vomit?\"", "illustrator": "Donald Crank", "keywords": "Run - Sabotage", "pack_code": "tdatd", "position": 61, "quantity": 3, "side_code": "runner", "stripped_text": "Run Archives. If successful, instead of breaching Archives, the Corp adds exactly 5 cards from Archives to HQ, if able. If they do, they trash 5 cards from HQ at random.", "stripped_title": "Glut Cipher", "text": "Run Archives. If successful, instead of breaching Archives, the Corp adds exactly 5 cards from Archives to HQ, if able. If they do, they trash 5 cards from HQ at random.", "title": "Glut Cipher", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_falsified_credentials_21064(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21064", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"I'm sorry, sir, we weren't expecting you! You look different than I remember...\"\n\"Haircut.\"", "illustrator": "Nasrul Hakim", "pack_code": "tdatd", "position": 64, "quantity": 3, "side_code": "runner", "stripped_text": "Name a card type. Expose a card in a remote server, then gain 5 credits if the exposed card has the named card type.", "stripped_title": "Falsified Credentials", "text": "Name a card type. Expose a card in a remote server, then gain 5[credit] if the exposed card has the named card type.", "title": "Falsified Credentials", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_because_i_can_21066(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21066", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "At least this time around, the graphic was family-friendly.", "illustrator": "Caravan Studio", "keywords": "Run", "pack_code": "tdatd", "position": 66, "quantity": 3, "side_code": "runner", "stripped_text": "Run a remote server. If successful, instead of breaching that server, you may force the Corp to shuffle all cards in the root of that server into R&D.", "stripped_title": "Because I Can", "text": "Run a remote server. If successful, instead of breaching that server, you may force the Corp to shuffle all cards in the root of that server into R&D.", "title": "Because I Can", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_contaminate_21083(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21083", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "\"What kind of maniac infects their own rig?!\"", "illustrator": "Adam S. Doyle", "pack_code": "win", "position": 83, "quantity": 3, "side_code": "runner", "stripped_text": "Place 3 virus counters on an installed Runner card with no hosted virus counters.", "stripped_title": "Contaminate", "text": "Place 3 virus counters on an installed Runner card with no hosted virus counters.", "title": "Contaminate", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_embezzle_21084(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21084", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "illustrator": "Caroline Gariba", "keywords": "Run - Sabotage", "pack_code": "win", "position": 84, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, instead of breaching HQ, name asset, ice, operation or upgrade, then reveal 2 cards from HQ at random. Trash each revealed card that has the named type, then gain 4 credits for each card trashed this way.", "stripped_title": "Embezzle", "text": "Run HQ. If successful, instead of breaching HQ, name asset, ice, operation or upgrade, then reveal 2 cards from HQ at random. Trash each revealed card that has the named type, then gain 4[credit] for each card trashed this way.", "title": "Embezzle", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_compile_21088(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21088", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Liiga Smilshkalne", "keywords": "Run", "pack_code": "win", "position": 88, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run. The first time you encounter a piece of ice during this run, you may search your stack or heap for a program and install it, ignoring all costs. When the run ends, add that program to the bottom of your stack if it is still installed.", "stripped_title": "Compile", "text": "Make a run. The first time you encounter a piece of ice during this run, you may search your stack or heap for a program and install it, ignoring all costs. When the run ends, add that program to the bottom of your stack if it is still installed.", "title": "Compile", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_diversion_of_funds_21105(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21105", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 5, "illustrator": "Fei F. Ou", "keywords": "Double - Run - Sabotage", "pack_code": "ka", "position": 105, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Run HQ. If successful, instead of breaching HQ, you may force the Corp to lose up to 5 credits, then you gain 1 credit for each credit lost.", "stripped_title": "Diversion of Funds", "text": "As an additional cost to play this event, spend [click].\nRun HQ. If successful, instead of breaching HQ, you may force the Corp to lose up to 5[credit], then you gain 1[credit] for each credit lost.", "title": "Diversion of Funds", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_black_hat_21110(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21110", "cost": 2, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 5, "flavor": "\"The way I see it, I'm teaching them a lesson in the importance of basic security.\" - Sunny Lebeau", "illustrator": "Ed Mattinian", "pack_code": "ka", "position": 110, "quantity": 3, "side_code": "runner", "stripped_text": "The Corp must trace[4]. If unsuccessful, for the remainder of the turn, access 2 additional cards whenever you breach HQ or R&D.", "stripped_title": "Black Hat", "text": "The Corp must trace[4]. If unsuccessful, for the remainder of the turn, access 2 additional cards whenever you breach HQ or R&D.", "title": "Black Hat", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_divide_and_conquer_22002(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22002", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "All roads lead to Rome.", "illustrator": "Adam S. Doyle", "keywords": "Run", "pack_code": "rar", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "Run Archives. If successful, after breaching Archives, breach HQ, then breach R&D. You cannot access cards in the root of HQ or R&D during these breaches.", "stripped_title": "Divide and Conquer", "text": "Run Archives. If successful, after breaching Archives, breach HQ, then breach R&D. You cannot access cards in the root of HQ or R&D during these breaches.", "title": "Divide and Conquer", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_guinea_pig_22003(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22003", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"Worth it.\"", "illustrator": "Reiko Murakami", "pack_code": "rar", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "Trash your grip. Gain 10 credits.", "stripped_title": "Guinea Pig", "text": "Trash your grip.\nGain 10[credit].", "title": "Guinea Pig", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_hot_pursuit_22009(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22009", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"We have you surrounded! For real, this time.\"", "illustrator": "Adam Schumpert", "keywords": "Run", "pack_code": "rar", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "Make a run on HQ. If successful, gain 9 credits and take 1 tag.", "stripped_title": "Hot Pursuit", "text": "Make a run on HQ. If successful, gain 9[credit] and take 1 tag.", "title": "Hot Pursuit", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_insight_22016(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22016", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Adam Schumpert", "keywords": "Double", "pack_code": "rar", "position": 16, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. The Corp may look at the top 4 cards of R&D and arrange them in any order. Reveal the top 4 cards of R&D.", "stripped_title": "Insight", "text": "As an additional cost to play this event, spend [click].\nThe Corp may look at the top 4 cards of R&D and arrange them in any order.\nReveal the top 4 cards of R&D.", "title": "Insight", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_reboot_22023(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22023", "cost": 1, "deck_limit": 3, "faction_code": "apex", "faction_cost": 5, "flavor": "I LIVE AGAIN", "illustrator": "Liiga Smilshkalne", "keywords": "Run", "pack_code": "rar", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "Run Archives. If successful, instead of breaching Archives, install up to 5 cards from your heap facedown. Remove this event from the game.", "stripped_title": "Reboot", "text": "Run Archives. If successful, instead of breaching Archives, install up to 5 cards from your heap facedown.\nRemove this event from the game.", "title": "Reboot", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_office_supplies_22024(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22024", "cost": 4, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 3, "flavor": "\"So, Miriam, hear anything good lately?\"", "illustrator": "James Cory Webster", "pack_code": "rar", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "Reduce the play cost of Office Supplies by 1 for each link you have. Gain 4 credits or draw 4 cards.", "stripped_title": "Office Supplies", "text": "Reduce the play cost of Office Supplies by 1 for each [link] you have.\nGain 4[credit] or draw 4 cards.", "title": "Office Supplies", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_labor_rights_23001(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "23001", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "<strong>Designed by 2017 European Champion Mike Sheehan</strong>", "illustrator": "Amelie Hutt", "pack_code": "mo", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "Trash the top 3 cards of your stack. Shuffle 3 cards from your heap into your stack. Draw 1 card. Remove this event from the game instead of trashing it.", "stripped_title": "Labor Rights", "text": "Trash the top 3 cards of your stack. Shuffle 3 cards from your heap into your stack. Draw 1 card. Remove this event from the game instead of trashing it.", "title": "Labor Rights", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_watch_the_world_burn_23100(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "23100", "cost": 3, "deck_limit": 1, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "<strong>Designed by the Day 1A players at Magnum Opus</strong>", "illustrator": "Emilio Rodriguez", "keywords": "Orgcrime - Run - Terminal", "pack_code": "mo", "position": 7, "quantity": 1, "side_code": "runner", "stripped_text": "After you resolve this event, end your action phase. Make a run on a remote server. If successful, remove the first non-agenda card that you access from the game. Until the game ends, whenever you access a copy of that card, remove it from the game. Limit 1 per deck.", "stripped_title": "Watch the World Burn", "text": "After you resolve this event, end your action phase.\nMake a run on a remote server. If successful, remove the first non-agenda card that you access from the game.\nUntil the game ends, whenever you access a copy of that card, remove it from the game.\nLimit 1 per deck.", "title": "Watch the World Burn", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_queens_gambit_25003(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25003", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "sc19", "position": 3, "quantity": 1, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Place up to 3 advancement counters on 1 unrezzed card in the root of a remote server. Gain 2 credits for each counter placed this way. You cannot access that card for the remainder of the turn.", "stripped_title": "Queen's Gambit", "text": "As an additional cost to play this event, spend [click].\nPlace up to 3 advancement counters on 1 unrezzed card in the root of a remote server. Gain 2[credit] for each counter placed this way. You cannot access that card for the remainder of the turn.", "title": "Queen's Gambit", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_quest_completed_25004(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25004", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "That moment of bliss. That feeling of accomplishment. That certainty of purpose.\nWhat's next?", "illustrator": "Gong Studios", "pack_code": "sc19", "position": 4, "quantity": 1, "side_code": "runner", "stripped_text": "Play only if you made a successful run on R&D, HQ, and Archives this turn. Access 1 installed card (non-ice).", "stripped_title": "Quest Completed", "text": "Play only if you made a successful run on R&D, HQ, and Archives this turn.\nAccess 1 installed card (non-ice).", "title": "Quest Completed", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_retrieval_run_25005(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25005", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Outland Entertainment LLC", "keywords": "Run", "pack_code": "sc19", "position": 5, "quantity": 2, "side_code": "runner", "stripped_text": "Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.", "stripped_title": "Retrieval Run", "text": "Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.", "title": "Retrieval Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_run_amok_25006(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25006", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"While there have been other anti-corporation movements before, like the Maroon Wave, this new one is different. It's organized.\" -Ramesh Gupta, One World Economy", "illustrator": "RC Torres", "keywords": "Run - Sabotage", "pack_code": "sc19", "position": 6, "quantity": 1, "side_code": "runner", "stripped_text": "Make a run. When the run ends, trash 1 piece of ice that was rezzed during this run.", "stripped_title": "Run Amok", "text": "Make a run. When the run ends, trash 1 piece of ice that was rezzed during this run.", "title": "Run Amok", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_stimhack_25007(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25007", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Andreas Zafiratos", "keywords": "Run", "pack_code": "sc19", "position": 7, "quantity": 1, "side_code": "runner", "stripped_text": "Place 9 credits on this event, then run any server. During that run, hosted credits are considered to be in your credit pool. When that run ends, suffer 1 core damage. This damage cannot be prevented.", "stripped_title": "Stimhack", "text": "Place 9[credit] on this event, then run any server. During that run, hosted credits are considered to be in your credit pool. When that run ends, suffer 1 core damage. This damage cannot be prevented.", "title": "Stimhack", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_career_fair_25022(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25022", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"You can help Jinteki shape the future. Your future.\"", "illustrator": "Dmitry Prosvirnin", "pack_code": "sc19", "position": 22, "quantity": 1, "side_code": "runner", "stripped_text": "Install 1 resource from your grip, paying 3 credits less.", "stripped_title": "Career Fair", "text": "Install 1 resource from your grip, paying 3[credit] less.", "title": "Career Fair", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_easy_mark_25023(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25023", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"Hey kid, you fire that up now, bound to be vamped real bad. Some real pathetic individuals around here. But thankfully I got just the ticket\u2026\"", "illustrator": "Matt Zeilinger", "keywords": "Job", "pack_code": "sc19", "position": 23, "quantity": 2, "side_code": "runner", "stripped_text": "Gain 3 credits.", "stripped_title": "Easy Mark", "text": "Gain 3[credit].", "title": "Easy Mark", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_emergency_shutdown_25024(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25024", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Think of it as a virtual shock collar for punishing corporate pets.\" -Andromeda", "illustrator": "Adam S. Doyle", "keywords": "Sabotage", "pack_code": "sc19", "position": 24, "quantity": 1, "side_code": "runner", "stripped_text": "Play only if you made a successful run on HQ this turn. Derez 1 installed piece of ice.", "stripped_title": "Emergency Shutdown", "text": "Play only if you made a successful run on HQ this turn.\nDerez 1 installed piece of ice.", "title": "Emergency Shutdown", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_hostage_25025(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25025", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Matt Zeilinger", "keywords": "Double", "pack_code": "sc19", "position": 25, "quantity": 1, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Search your stack for a connection, reveal it, and add it to your grip. You may install that connection (paying its install cost). Shuffle your stack.", "stripped_title": "Hostage", "text": "As an additional cost to play this event, spend [click].\nSearch your stack for a <strong>connection</strong>, reveal it, and add it to your grip. You may install that <strong>connection</strong> (paying its install cost). Shuffle your stack.", "title": "Hostage", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_inside_job_25026(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25026", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Hey, listen, I'm not asking you to do anything dangerous. Just let me into the building. And tell me which room has the weakest security. And please don't say 'the bathroom' again.\"", "illustrator": "Clark Huggins", "keywords": "Run", "pack_code": "sc19", "position": 26, "quantity": 2, "side_code": "runner", "stripped_text": "Run any server. The first time this run you encounter a piece of ice, bypass it.", "stripped_title": "Inside Job", "text": "Run any server. The first time this run you encounter a piece of ice, bypass it.", "title": "Inside Job", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_legwork_25027(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25027", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"I work by referral only, with an up-front fee. The fee is reasonable if you value results.\" -Silhouette", "illustrator": "Gong Studios", "keywords": "Run", "pack_code": "sc19", "position": 27, "quantity": 2, "side_code": "runner", "stripped_text": "Run HQ. If successful, access 2 additional cards when you breach HQ.", "stripped_title": "Legwork", "text": "Run HQ. If successful, access 2 additional cards when you breach HQ.", "title": "Legwork", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_networking_25028(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25028", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "She preferred to do business in a club. Something about the lights and dancers clouded the judgment of the corporate simpletons she met there.", "illustrator": "Gong Studios", "pack_code": "sc19", "position": 28, "quantity": 1, "side_code": "runner", "stripped_text": "Remove 1 tag. Then, you may pay 1 credit to add this event to your grip.", "stripped_title": "Networking", "text": "Remove 1 tag. Then, you may pay 1[credit] to add this event to your grip.", "title": "Networking", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_spear_phishing_25029(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25029", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Targeted attacks make system breaches so much easier, especially if you can spoof an authorized user.", "illustrator": "Andreas Zafiratos", "keywords": "Run", "pack_code": "sc19", "position": 29, "quantity": 1, "side_code": "runner", "stripped_text": "Make a run. When you encounter the innermost piece of ice protecting that server, bypass it.", "stripped_title": "Spear Phishing", "text": "Make a run. When you encounter the innermost piece of ice protecting that server, bypass it.", "title": "Spear Phishing", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_special_order_25030(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25030", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Feverishly tracking its frustratingly slow progress across the Pacific, the package finally shows up hours later\u2026", "illustrator": "Steve Hamilton", "pack_code": "sc19", "position": 30, "quantity": 2, "side_code": "runner", "stripped_text": "Search your stack for an icebreaker, reveal it, and add it to your grip. Shuffle your stack.", "stripped_title": "Special Order", "text": "Search your stack for an <strong>icebreaker</strong>, reveal it, and add it to your grip. Shuffle your stack.", "title": "Special Order", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_diesel_25042(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25042", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Diesel gives you flames.", "illustrator": "Tim Durning", "pack_code": "sc19", "position": 42, "quantity": 2, "side_code": "runner", "stripped_text": "Draw 3 cards.", "stripped_title": "Diesel", "text": "Draw 3 cards.", "title": "Diesel", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_modded_25043(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25043", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "There's no replacement for a home-grown program. Fed on late nights, oaty bars, and single-minded determination. Cheaper, too.", "illustrator": "Kate Laird", "keywords": "Mod", "pack_code": "sc19", "position": 43, "quantity": 2, "side_code": "runner", "stripped_text": "Install a program or piece of hardware, lowering the install cost by 3.", "stripped_title": "Modded", "text": "Install a program or piece of hardware, lowering the install cost by 3.", "title": "Modded", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_notoriety_25044(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25044", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "When you're this good, it's hard not to grow a fan base.", "illustrator": "Matt Zeilinger", "pack_code": "sc19", "position": 44, "quantity": 1, "side_code": "runner", "stripped_text": "Play only if you made a successful run on R&D, HQ, and Archives this turn. Add Notoriety to your score area as an agenda worth 1 agenda point.", "stripped_title": "Notoriety", "text": "Play only if you made a successful run on R&D, HQ, and Archives this turn.\nAdd Notoriety to your score area as an agenda worth 1 agenda point.", "title": "Notoriety", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_test_run_25045(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25045", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Kate Laird", "pack_code": "sc19", "position": 45, "quantity": 1, "side_code": "runner", "stripped_text": "Search either your stack or your heap for 1 program. (Shuffle your stack if you searched it.) Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.", "stripped_title": "Test Run", "text": "Search either your stack or your heap for 1 program. <em>(Shuffle your stack if you searched it.)</em> Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.", "title": "Test Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_the_makers_eye_25046(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25046", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Some of the professionals have good instincts, but they can't see beyond the data. They can't see the matrix.\" -Ele \"Smoke\" Scovak", "illustrator": "Liiga Smilshkalne", "keywords": "Run", "pack_code": "sc19", "position": 46, "quantity": 2, "side_code": "runner", "stripped_text": "Run R&D. If successful, access 2 additional cards when you breach R&D.", "stripped_title": "The Maker's Eye", "text": "Run R&D. If successful, access 2 additional cards when you breach R&D.", "title": "The Maker's Eye", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_tinkering_25047(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25047", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "\"There's that moment, you know, when the whole world seems to fall away and it is only you and your mod, and the mod is the world.\"", "illustrator": "Christina Davis", "keywords": "Mod", "pack_code": "sc19", "position": 47, "quantity": 2, "side_code": "runner", "stripped_text": "Choose a piece of ice. That ice gains sentry, code gate, and barrier until the end of the turn.", "stripped_title": "Tinkering", "text": "Choose a piece of ice. That ice gains <strong>sentry</strong>, <strong>code gate</strong>, and <strong>barrier</strong> until the end of the turn.", "title": "Tinkering", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_sure_gamble_25059(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25059", "cost": 5, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Lady Luck took the form of a hifi quantum manipulation ring that she wore on her middle finger.", "illustrator": "Kate Niemczyk", "pack_code": "sc19", "position": 59, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 9 credits.", "stripped_title": "Sure Gamble", "text": "Gain 9[credit].", "title": "Sure Gamble", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_dirty_laundry_25060(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25060", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "The data was better than she could have ever imagined. This Santiago fellow really knew what he was doing. She began to imagine the havoc she could wreak at the upcoming charity dinner\u2026", "illustrator": "Christina Davis", "keywords": "Run", "pack_code": "sc19", "position": 60, "quantity": 2, "side_code": "runner", "stripped_text": "Run any server. When that run ends, if it was successful, gain 5 credits.", "stripped_title": "Dirty Laundry", "text": "Run any server. When that run ends, if it was successful, gain 5[credit].", "title": "Dirty Laundry", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_isolation_26001(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26001", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "With each passing day alone, Hoshiko found it harder to think. With each hour, the static grew louder.", "illustrator": "Photo Tammy Gann/Unsplash & Deep Dream", "pack_code": "df", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, trash an installed resource. Gain 7 credits.", "stripped_title": "Isolation", "text": "As an additional cost to play this event, trash an installed resource.\nGain 7[credit].", "title": "Isolation", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_always_have_a_backup_plan_26011(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26011", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Everyone told me she was reliable in a pinch.\"\n -Az McCaffrey", "illustrator": "Olie Boldador", "keywords": "Run", "pack_code": "df", "position": 11, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. When that run ends, if it was unsuccessful, you may run that server again, ignoring any additional costs to run. During the second run, when you encounter the last ice you encountered in the first run, bypass it.", "stripped_title": "Always Have a Backup Plan", "text": "Run any server. When that run ends, if it was unsuccessful, you may run that server again, ignoring any additional costs to run. During the second run, when you encounter the last ice you encountered in the first run, bypass it.", "title": "Always Have a Backup Plan", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_blueberry_diesel_26012(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26012", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Blue flames burn the hottest!", "illustrator": "Patrick Burk", "pack_code": "df", "position": 12, "quantity": 3, "side_code": "runner", "stripped_text": "Look at the top 2 cards of your stack. You may add 1 of those cards to the bottom of your stack. Draw 2 cards.", "stripped_title": "Blueberry! Diesel", "text": "Look at the top 2 cards of your stack. You may add 1 of those cards to the bottom of your stack. Draw 2 cards.", "title": "Blueberry!\u2122 Diesel", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_in_the_groove_26020(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26020", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "Do you know how many food deliveries I've missed this week?", "illustrator": "Olie Boldador", "keywords": "Priority", "pack_code": "df", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "Play only as your first click. Whenever you install a card with a printed install cost of 1 or greater this turn, draw 1 card or gain 1 credit.", "stripped_title": "In the Groove", "text": "Play only as your first [click].\nWhenever you install a card with a printed install cost of 1 or greater this turn, draw 1 card or gain 1[credit].", "title": "In the Groove", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_khusyuk_26021(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26021", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Iain Fairclough", "keywords": "Run", "pack_code": "df", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "Run R&D. If successful, instead of breaching R&D, choose a number greater than 0. For each installed card you have with a printed install cost matching that number, reveal 1 card from the top of R&D (max 6). Access 1 of the revealed cards, then the Corp shuffles R&D.", "stripped_title": "Khusyuk", "text": "Run R&D. If successful, instead of breaching R&D, choose a number greater than 0. For each installed card you have with a printed install cost matching that number, reveal 1 card from the top of R&D (max 6). Access 1 of the revealed cards, then the Corp shuffles R&D.", "title": "Khusyuk", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_spec_work_26022(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26022", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"There is never a wasted program. Someone, somewhere, will have a use for that code. Even corps are scrambling for quick fixes nowadays.\"\n-Lat", "illustrator": "Krembler", "keywords": "Job", "pack_code": "df", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, trash an installed program. Gain 4 credits and draw 2 cards.", "stripped_title": "Spec Work", "text": "As an additional cost to play this event, trash an installed program.\nGain 4[credit] and draw 2 cards.", "title": "Spec Work", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_direct_access_26028(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26028", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "Get into the ducts on the roof and keep crawling till you hit that old network root. Dirty work, I know, but it beats playing by the rules.", "illustrator": "Olie Boldador", "keywords": "Run", "pack_code": "df", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "While you are resolving this event, each player's identity loses all abilities. Run any server. When that run ends, you may shuffle this event into your stack.", "stripped_title": "Direct Access", "text": "While you are resolving this event, each player's identity loses all abilities.\nRun any server. When that run ends, you may shuffle this event into your stack.", "title": "Direct Access", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_rejig_26029(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26029", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "I didn't say your hopper should be hauling garbage. I said it should be hauled away <em>as</em> garbage.", "illustrator": "Krembler", "pack_code": "df", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "Add an installed program or piece of hardware to your grip. If you do, you may install a program or piece of hardware, paying X credits less. X is equal to the printed install cost of the uninstalled card.", "stripped_title": "Rejig", "text": "Add an installed program or piece of hardware to your grip. If you do, you may install a program or piece of hardware, paying X[credit] less. X is equal to the printed install cost of the uninstalled card.", "title": "Rejig", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_moshing_26067(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26067", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Let's start a <strong>RIOT</strong>.", "illustrator": "Patrick Burk", "pack_code": "ur", "position": 67, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, trash 3 cards from your grip. Draw 3 cards and gain 3 credits.", "stripped_title": "Moshing", "text": "As an additional cost to play this event, trash 3 cards from your grip.\nDraw 3 cards and gain 3[credit].", "title": "Moshing", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_bravado_26074(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26074", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Hold my wine. I'm going in.\" -Red Comyn", "illustrator": "Kevin Tame", "keywords": "Run", "pack_code": "ur", "position": 74, "quantity": 3, "side_code": "runner", "stripped_text": "Run a server protected by ice. When that run ends, gain 6 credits, plus 1 credit for each piece of ice you passed during that run.", "stripped_title": "Bravado", "text": "Run a server protected by ice. When that run ends, gain 6[credit], plus 1[credit] for each piece of ice you passed during that run.", "title": "Bravado", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_harmony_ar_therapy_26083(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26083", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Breathe in and visualise your happy place. Breathe out. It's safe and calm and all your best days are there. Breathe in. Very good. The cortex scan has finished. Breathe out and open your eyes...", "illustrator": "Patrick Burk, Krembler", "pack_code": "ur", "position": 83, "quantity": 3, "side_code": "runner", "stripped_text": "Search your heap for up to 5 cards with different names. Shuffle those cards into your stack. Remove this card from the game instead of trashing it.", "stripped_title": "Harmony AR Therapy", "text": "Search your heap for up to 5 cards with different names. Shuffle those cards into your stack. Remove this card from the game instead of trashing it.", "title": "Harmony AR Therapy", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_labor_rights_28001(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "28001", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "<strong>Designed by 2017 European Champion Mike Sheehan</strong>", "illustrator": "Krembler", "pack_code": "mor", "position": 1, "quantity": 3, "side_code": "runner", "stripped_text": "Trash the top 3 cards of your stack. Shuffle 3 cards from your heap into your stack. Draw 1 card. Remove this event from the game instead of trashing it.", "stripped_title": "Labor Rights", "text": "Trash the top 3 cards of your stack. Shuffle 3 cards from your heap into your stack. Draw 1 card. Remove this event from the game instead of trashing it.", "title": "Labor Rights", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_indexing_29005(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "29005", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "A little corporate restructuring is necessary once in a while.", "illustrator": "Mauricio Herrera", "keywords": "Run", "pack_code": "sm", "position": 5, "quantity": 2, "side_code": "runner", "stripped_text": "Run R&D. If successful, instead of breaching R&D, you may look at the top 5 cards of R&D and arrange them in any order.", "stripped_title": "Indexing", "text": "Run R&D. If successful, instead of breaching R&D, you may look at the top 5 cards of R&D and arrange them in any order.", "title": "Indexing", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_lucky_find_29007(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "29007", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 2, "flavor": "Data hunters always pay top dollar for old drives. The more useless the data, the higher the payout.", "illustrator": "Gong Studios", "keywords": "Double", "pack_code": "sm", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, spend click. Gain 9 credits.", "stripped_title": "Lucky Find", "text": "As an additional cost to play this event, spend [click].\nGain 9[credit].", "title": "Lucky Find", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_wildcat_strike_30002(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30002", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "They can buy off union leadership, but they can't stop us walking out!", "illustrator": "David Lei", "pack_code": "sg", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "Resolve 1 of the following of the Corp's choice: * Gain 6 credits. * Draw 4 cards.", "stripped_title": "Wildcat Strike", "text": "Resolve 1 of the following of the Corp's choice:<ul><li>Gain 6[credit].</li><li>Draw 4 cards.</li></ul>", "title": "Wildcat Strike", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_mutual_favor_30011(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30011", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "The real reward is the friends you make along the way.", "illustrator": "David Lei", "pack_code": "sg", "position": 11, "quantity": 3, "side_code": "runner", "stripped_text": "Search your stack for 1 icebreaker program and reveal it. (Shuffle your stack after searching it.) If you made a successful run this turn, you may install it. If you do not, add it to your grip.", "stripped_title": "Mutual Favor", "text": "Search your stack for 1 <strong>icebreaker</strong> program and reveal it. <em>(Shuffle your stack after searching it.)</em> If you made a successful run this turn, you may install it. If you do not, add it to your grip.", "title": "Mutual Favor", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_tread_lightly_30012(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30012", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"A mirrorfiber mod or high-end mantle can be helpful, but nothing beats a good dose of 'keeping your damn head down.'\"\n\u2014\"G0ph3r\" O'Ryan", "illustrator": "Jack Reeves", "keywords": "Run", "pack_code": "sg", "position": 12, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. During that run, the rez cost of each piece of ice is increased by 3 credits.", "stripped_title": "Tread Lightly", "text": "Run any server. During that run, the rez cost of each piece of ice is increased by 3[credit].", "title": "Tread Lightly", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_creative_commission_30020(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30020", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "The challenge of my art is what I live for, but I'm not going to say no to a patron with taste.", "illustrator": "Benjamin Giletti", "pack_code": "sg", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 5 credits. If you have any click remaining, lose click.", "stripped_title": "Creative Commission", "text": "Gain 5[credit]. If you have any [click] remaining, lose [click].", "title": "Creative Commission", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_vrcation_30021(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30021", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"You know there's no water in the Sea of Tranquility, right?\"\n\"That doesn't mean there's no beach.\"", "illustrator": "Benjamin Giletti", "pack_code": "sg", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "Draw 4 cards. If you have any click remaining, lose click.", "stripped_title": "VRcation", "text": "Draw 4 cards. If you have any [click] remaining, lose [click].", "title": "VRcation", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_jailbreak_30028(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30028", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"We'll take the access codes from their own prisec\u2014privilege escalation through local application of force.\"\n\u2014The Catalyst", "illustrator": "David Lei", "keywords": "Run", "pack_code": "sg", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ or R&D. If successful, draw 1 card and when you breach the attacked server, access 1 additional card.", "stripped_title": "Jailbreak", "text": "Run HQ or R&D. If successful, draw 1 card and when you breach the attacked server, access 1 additional card.", "title": "Jailbreak", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_overclock_30029(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30029", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"After 381FS4 started acting independently, all bets were off. Rethreading its own brain chip... even probing <strong>our</strong> nodes. I had to shut it down.\"\n\u2014Linus Lovegood, NBN Novelties&Acquisitions", "illustrator": "Scott Uminga", "keywords": "Run", "pack_code": "sg", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "Place 5 credits on this event, then run any server. You can spend hosted credits during that run.", "stripped_title": "Overclock", "text": "Place 5[credit] on this event, then run any server. You can spend hosted credits during that run.", "title": "Overclock", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_sure_gamble_30030(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30030", "cost": 5, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Anyone can put in the hours of planning, practice, and preparation\u2014but making it all look like luck takes <strong>style</strong>.", "illustrator": "Kira L. Nguyen", "pack_code": "sg", "position": 30, "quantity": 3, "side_code": "runner", "stripped_text": "Gain 9 credits.", "stripped_title": "Sure Gamble", "text": "Gain 9[credit].", "title": "Sure Gamble", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_en_passant_31003(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31003", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"If you're not in position to press the advantage, you'll never gain the upper hand.\"\n\u2014The Playbook", "illustrator": "Seojun Park", "keywords": "Sabotage", "pack_code": "su21", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run this turn. Trash 1 unrezzed piece of ice you passed during your last run.", "stripped_title": "En Passant", "text": "Play only if you made a successful run this turn.\nTrash 1 unrezzed piece of ice you passed during your last run.", "title": "En Passant", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_retrieval_run_31004(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31004", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Someone's trash is another's treasure.", "illustrator": "Zoe Cohen", "keywords": "Run", "pack_code": "su21", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.", "stripped_title": "Retrieval Run", "text": "Run Archives. If successful, instead of breaching Archives, you may install 1 program from your heap, ignoring all costs.", "title": "Retrieval Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_career_fair_31015(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31015", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"I see great opportunities ahead for you.\"", "illustrator": "Zoe Cohen", "pack_code": "su21", "position": 15, "quantity": 3, "side_code": "runner", "stripped_text": "Install 1 resource from your grip, paying 3 credits less.", "stripped_title": "Career Fair", "text": "Install 1 resource from your grip, paying 3[credit] less.", "title": "Career Fair", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_emergency_shutdown_31016(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31016", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Did you order the defrag?\"\n\"...I thought you did?\"", "illustrator": "Nedliv Audiovisuell", "keywords": "Sabotage", "pack_code": "su21", "position": 16, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on HQ this turn. Derez 1 installed piece of ice.", "stripped_title": "Emergency Shutdown", "text": "Play only if you made a successful run on HQ this turn.\nDerez 1 installed piece of ice.", "title": "Emergency Shutdown", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_forged_activation_orders_31017(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31017", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Electronic warfare, like all warfare, is based on deception.\"\n\u2014The Playbook", "illustrator": "Seojun Park", "keywords": "Sabotage", "pack_code": "su21", "position": 17, "quantity": 3, "side_code": "runner", "stripped_text": "Choose 1 unrezzed piece of ice. The Corp may rez that ice. If they do not, they trash it.", "stripped_title": "Forged Activation Orders", "text": "Choose 1 unrezzed piece of ice. The Corp may rez that ice. If they do not, they trash it.", "title": "Forged Activation Orders", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_inside_job_31018(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31018", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"I'm not an actor, but I <strong>am</strong> a professional.\"\n\u2014Gabriel Santiago", "illustrator": "Benjamin Giletti", "keywords": "Run", "pack_code": "su21", "position": 18, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. The first time this run you encounter a piece of ice, bypass it.", "stripped_title": "Inside Job", "text": "Run any server. The first time this run you encounter a piece of ice, bypass it.", "title": "Inside Job", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_legwork_31019(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31019", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Go outside. Work with your hands. It'll do you good.", "illustrator": "Zoe Cohen", "keywords": "Run", "pack_code": "su21", "position": 19, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, access 2 additional cards when you breach HQ.", "stripped_title": "Legwork", "text": "Run HQ. If successful, access 2 additional cards when you breach HQ.", "title": "Legwork", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_networking_31020(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31020", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "It's not what you know. It's who you know.", "illustrator": "Nedliv Audiovisuell", "pack_code": "su21", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "Remove 1 tag. Then, you may pay 1 credit to add this event to your grip.", "stripped_title": "Networking", "text": "Remove 1 tag. Then, you may pay 1[credit] to add this event to your grip.", "title": "Networking", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_diesel_31027(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31027", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "No Diesel? No fire!", "illustrator": "Krembler", "pack_code": "su21", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "Draw 3 cards.", "stripped_title": "Diesel", "text": "Draw 3 cards.", "title": "Diesel", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_test_run_31028(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31028", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "No code survives contact with the user.", "illustrator": "Nedliv Audiovisuell", "pack_code": "su21", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "Search either your stack or your heap for 1 program. (Shuffle your stack if you searched it.) Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.", "stripped_title": "Test Run", "text": "Search either your stack or your heap for 1 program. <em>(Shuffle your stack if you searched it.)</em> Install that program, ignoring all costs. When your turn ends, if that program has not been uninstalled, add it to the top of your stack.", "title": "Test Run", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_the_makers_eye_31029(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31029", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "The incoming datafeed is blunted, rendered into a soft lie our brains can understand. Seeing the Reality beyond takes dedication and practice.", "illustrator": "N. Hopkins", "keywords": "Run", "pack_code": "su21", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "Run R&D. If successful, access 2 additional cards when you breach R&D.", "stripped_title": "The Maker's Eye", "text": "Run R&D. If successful, access 2 additional cards when you breach R&D.", "title": "The Maker's Eye", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_dirty_laundry_31037(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31037", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "I thought I'd feel bad about this. I don't.", "illustrator": "Chelsea Geter", "keywords": "Run", "pack_code": "su21", "position": 37, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. When that run ends, if it was successful, gain 5 credits.", "stripped_title": "Dirty Laundry", "text": "Run any server. When that run ends, if it was successful, gain 5[credit].", "title": "Dirty Laundry", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_deep_dive_32003(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "32003", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 5, "illustrator": "Cat Shen", "pack_code": "msbp", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on HQ, R&D, and Archives this turn. The Corp must set aside the top 8 cards of R&D faceup. Access 1 of those cards. You may spend click to access another 1 of those cards. Then, the Corp shuffles the set-aside cards into R&D.", "stripped_title": "Deep Dive", "text": "Play only if you made a successful run on HQ, R&D, and Archives this turn.\nThe Corp must set aside the top 8 cards of R&D faceup. Access 1 of those cards. You may spend [click] to access another 1 of those cards. Then, the Corp shuffles the set-aside cards into R&D.", "title": "Deep Dive", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_chastushka_33002(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33002", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "We're all alike down here\nAndroids are friends we salute\nGive us all a f***ing break\nOl' Jack is the s*** on my boot.", "illustrator": "Adam S. Doyle", "keywords": "Run - Sabotage", "pack_code": "ms", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "Run HQ. If successful, instead of breaching HQ, sabotage 4. (The Corp trashes 4 cards of their choice from HQ and/or the top of R&D.)", "stripped_title": "Chastushka", "text": "Run HQ. If successful, instead of breaching HQ, sabotage 4. <em>(The Corp trashes 4 cards of their choice from HQ and/or the top of R&D.)</em>", "title": "Chastushka", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_running_hot_33003(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33003", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "We can change the world, if we're willing to be changed in return.", "illustrator": "Elizaveta Sokolova", "pack_code": "ms", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, suffer 1 core damage. Gain clickclickclick.", "stripped_title": "Running Hot", "text": "As an additional cost to play this event, suffer 1 core damage.\nGain [click][click][click].", "title": "Running Hot", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_steelskin_scarring_33004(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33004", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Reactive implants reclaim the memories of our fallen comrades. Their sacrifice is our shield.", "illustrator": "Elliott Birt", "pack_code": "ms", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "Draw 3 cards. When this event is trashed from your grip or stack, you may draw 2 cards.", "stripped_title": "Steelskin Scarring", "text": "Draw 3 cards.\nWhen this event is trashed from your grip or stack, you may draw 2 cards.", "title": "Steelskin Scarring", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_carpe_diem_33012(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33012", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "The best moment to listen is when others are listening to you.", "illustrator": "Benjamin Giletti", "keywords": "Run", "pack_code": "ms", "position": 12, "quantity": 3, "side_code": "runner", "stripped_text": "Identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) Gain 4 credits. You may run your mark.", "stripped_title": "Carpe Diem", "text": "Identify your mark. <em>(If you don\u2019t have a mark, a random central server becomes your mark for this turn.)</em>\nGain 4[credit]. You may run your mark.", "title": "Carpe Diem", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_pinhole_threading_33013(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33013", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "Neneci\u011fim would be proud.", "illustrator": "Bruno Balixa", "keywords": "Run", "pack_code": "ms", "position": 13, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. If successful, instead of breaching the attacked server, access 1 card in the root of another server. If that card is an agenda, you cannot steal or trash it during this access.", "stripped_title": "Pinhole Threading", "text": "Run any server. If successful, instead of breaching the attacked server, access 1 card in the root of another server. If that card is an agenda, you cannot steal or trash it during this access.", "title": "Pinhole Threading", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_deep_dive_33022(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33022", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 5, "illustrator": "Cat Shen", "pack_code": "ms", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you made a successful run on HQ, R&D, and Archives this turn. The Corp must set aside the top 8 cards of R&D faceup. Access 1 of those cards. You may spend click to access another 1 of those cards. Then, the Corp shuffles the set-aside cards into R&D.", "stripped_title": "Deep Dive", "text": "Play only if you made a successful run on HQ, R&D, and Archives this turn.\nThe Corp must set aside the top 8 cards of R&D faceup. Access 1 of those cards. You may spend [click] to access another 1 of those cards. Then, the Corp shuffles the set-aside cards into R&D.", "title": "Deep Dive", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_into_the_depths_33023(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33023", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Kira L. Nguyen", "keywords": "Run", "pack_code": "ms", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. If successful, for each time you passed ice this run, resolve 1 of the following that you have not yet resolved this run: * Gain 4 credits. * Search your stack for a program. Install it. (Shuffle your stack after searching it.) * Charge 1 of your installed cards. (Add 1 power counter to a card that already has one.)", "stripped_title": "Into the Depths", "text": "Run any server. If successful, for each time you passed ice this run, resolve 1 of the following that you have not yet resolved this run:<ul><li>Gain 4[credit].</li><li>Search your stack for a program. Install it. <em>(Shuffle your stack after searching it.)</em></li><li>Charge 1 of your installed cards. <em>(Add 1 power counter to a card that already has one.)</em></li></ul>", "title": "Into the Depths", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_rigging_up_33024(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33024", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Edie doesn't mind the noise. She's happy just being nearby.", "illustrator": "Benjamin Giletti", "keywords": "Mod", "pack_code": "ms", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "Install 1 program or piece of hardware from your grip, paying 3 credits less. You may charge that card if able. (If it has a power counter on it, add another.)", "stripped_title": "Rigging Up", "text": "Install 1 program or piece of hardware from your grip, paying 3[credit] less. You may charge that card if able. <em>(If it has a power counter on it, add another.)</em>", "title": "Rigging Up", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_finality_33066(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33066", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"My guilt is never to be doubted.\"", "illustrator": "Ferenc Patk\u00f3s", "keywords": "Run", "pack_code": "ph", "position": 66, "quantity": 3, "side_code": "runner", "stripped_text": "As an additional cost to play this event, suffer 1 core damage. Run R&D. If successful, access 3 additional cards when you breach R&D.", "stripped_title": "Finality", "text": "As an additional cost to play this event, suffer 1 core damage.\nRun R&D. If successful, access 3 additional cards when you breach R&D.", "title": "Finality", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_katorga_breakout_33067(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33067", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"I promised I would come back for you, no matter the cost.\"\n\u2014Es\u00e2 Afontov", "illustrator": "Olie Boldador", "keywords": "Run", "pack_code": "ph", "position": 67, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. If successful, add 1 card from your heap to your grip.", "stripped_title": "Katorga Breakout", "text": "Run any server. If successful, add 1 card from your heap to your grip.", "title": "Katorga Breakout", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_raindrops_cut_stone_33068(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33068", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "With every step closer to their prize, Bankhar felt the ice slicing white-hot through their synapses. It was worth it.", "illustrator": "Scott Uminga", "keywords": "Run", "pack_code": "ph", "position": 68, "quantity": 3, "side_code": "runner", "stripped_text": "Run any server. Whenever a subroutine resolves during that run (including a subroutine that ends the run), place 1 power counter on this event. When that run ends, draw 1 card for each hosted power counter and gain 3 credits.", "stripped_title": "Raindrops Cut Stone", "text": "Run any server. Whenever a subroutine resolves during that run <em>(including a subroutine that ends the run)</em>, place 1 power counter on this event.\nWhen that run ends, draw 1 card for each hosted power counter and gain 3[credit].", "title": "Raindrops Cut Stone", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_concerto_33075(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33075", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Roslavets\u02bc Concerto No. 2. Breakneck, brilliant, enchanting. The perfect finale for Virtuoso.\"", "illustrator": "Olie Boldador", "keywords": "Run", "pack_code": "ph", "position": 75, "quantity": 3, "side_code": "runner", "stripped_text": "Reveal the top card of your stack and place credits equal to its printed play or install cost on this event. Add the revealed card to your grip. Run any server. You can spend hosted credits during that run.", "stripped_title": "Concerto", "text": "Reveal the top card of your stack and place credits equal to its printed play or install cost on this event. Add the revealed card to your grip.\nRun any server. You can spend hosted credits during that run.", "title": "Concerto", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_reprise_33076(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33076", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"I may bow like I\u02bcve accomplished the impossible, but the truth is it\u02bcs not that hard.\"\n", "illustrator": "Ferenc Patk\u00f3s", "keywords": "Run", "pack_code": "ph", "position": 76, "quantity": 3, "side_code": "runner", "stripped_text": "Play only if you stole an agenda this turn. Add 1 installed Corp card to HQ. You may run any server.", "stripped_title": "Reprise", "text": "Play only if you stole an agenda this turn.\nAdd 1 installed Corp card to HQ. You may run any server.", "title": "Reprise", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class event_spark_of_inspiration_33084(Event):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33084", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"The best ideas float to the top, if you give them time.\"\n\u2014Ar<h1m3d3s  JAR", "illustrator": "Oliver Morit", "keywords": "Mod", "pack_code": "ph", "position": 84, "quantity": 3, "side_code": "runner", "stripped_text": "Set aside cards from the top of your stack faceup until you set aside a program. You may install that program, paying 10 credits less. Shuffle the set-aside cards into your stack.", "stripped_title": "Spark of Inspiration", "text": "Set aside cards from the top of your stack faceup until you set aside a program. You may install that program, paying 10[credit] less. Shuffle the set-aside cards into your stack.", "title": "Spark of Inspiration", "type_code": "event", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                