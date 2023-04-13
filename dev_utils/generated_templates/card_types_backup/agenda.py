
'''
card classes of type agenda
'''
from netrunner_lib.cards._base_card_classes import Agenda

class agenda_accelerated_beta_test_01055(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "01055", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Rachel Borovic", "keywords": "Research", "pack_code": "core", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Accelerated Beta Test, you may look at the top 3 cards of R&D. If any of those cards are ice, you may install and rez them, ignoring all costs. Trash the rest of the cards you looked at.", "stripped_title": "Accelerated Beta Test", "text": "When you score Accelerated Beta Test, you may look at the top 3 cards of R&D. If any of those cards are ice, you may install and rez them, ignoring all costs. Trash the rest of the cards you looked at.", "title": "Accelerated Beta Test", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_nisei_mk_ii_01068(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "01068", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Alexandra Douglass", "keywords": "Initiative", "pack_code": "core", "position": 68, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: End the run.", "stripped_title": "Nisei MK II", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter:</strong> End the run.", "title": "Nisei MK II", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_astroscript_pilot_program_01081(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "01081", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Initiative", "pack_code": "core", "position": 81, "quantity": 2, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: Place 1 advancement counter on an installed card you can advance. Limit 1 per deck.", "stripped_title": "AstroScript Pilot Program", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter:</strong> Place 1 advancement counter on an installed card you can advance.\nLimit 1 per deck.", "title": "AstroScript Pilot Program", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_breaking_news_01082(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "01082", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Imaginary FS Pte Ltd", "pack_code": "core", "position": 82, "quantity": 2, "side_code": "corp", "stripped_text": "When you score Breaking News, give the Runner 2 tags. When the turn on which you scored Breaking News ends, the Runner loses 2 tags.", "stripped_title": "Breaking News", "text": "When you score Breaking News, give the Runner 2 tags.\nWhen the turn on which you scored Breaking News ends, the Runner loses 2 tags.", "title": "Breaking News", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_hostile_takeover_01094(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "01094", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "There are going to be some changes around here.", "illustrator": "Mauricio Herrera", "keywords": "Expansion", "pack_code": "core", "position": 94, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, gain 7 credits and take 1 bad publicity.", "stripped_title": "Hostile Takeover", "text": "When you score this agenda, gain 7[credit] and take 1 bad publicity.", "title": "Hostile Takeover", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_posted_bounty_01095(Agenda):
    '''
    When you score Posted Bounty, you may forfeit it to give the Runner 1 tag and take 1 bad publicity.
    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "01095", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"If some two-cred newsy picks it up, even better. The scum could be in the alleys of Guayaquil of the slums of BosWash. Not to mention off-planet.\"", "illustrator": "Mauricio Herrera", "keywords": "Security", "pack_code": "core", "position": 95, "quantity": 2, "side_code": "corp", "stripped_text": "When you score Posted Bounty, you may forfeit it to give the Runner 1 tag and take 1 bad publicity.", "stripped_title": "Posted Bounty", "text": "When you score Posted Bounty, you may forfeit it to give the Runner 1 tag and take 1 bad publicity.", "title": "Posted Bounty", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        print(f'playing card: {self.title} || PARTIAL!')
        return super().play(player,game)
                
class agenda_priority_requisition_01106(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "01106", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"If it isn't in my terminal by six p.m., heads are going to roll!\"", "illustrator": "Gong Studios", "keywords": "Security", "pack_code": "core", "position": 106, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Priority Requisition, you may rez a piece of ice ignoring all costs.", "stripped_title": "Priority Requisition", "text": "When you score Priority Requisition, you may rez a piece of ice ignoring all costs.", "title": "Priority Requisition", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_private_security_force_01107(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "01107", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Expensive? Not when you're protecting a fortune as large as ours.\"", "illustrator": "Mauricio Herrera", "keywords": "Security", "pack_code": "core", "position": 107, "quantity": 3, "side_code": "corp", "stripped_text": "If the Runner is tagged, Private Security Force gains: \"click: Do 1 meat damage.\"", "stripped_title": "Private Security Force", "text": "If the Runner is tagged, Private Security Force gains: \"[click]: Do 1 meat damage.\"", "title": "Private Security Force", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_mandatory_upgrades_02011(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 6, "agenda_points": 2, "code": "02011", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Sometimes employee reviews took a little bit longer than anticipated.", "illustrator": "Mauricio Herrera", "keywords": "Initiative", "pack_code": "wla", "position": 11, "quantity": 3, "side_code": "corp", "stripped_text": "You have 1 additional click to spend each turn.", "stripped_title": "Mandatory Upgrades", "text": "You have 1 additional [click] to spend each turn.", "title": "Mandatory Upgrades", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_braintrust_02014(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "02014", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Gong Studios", "keywords": "Research", "pack_code": "wla", "position": 14, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Braintrust, place 1 agenda counter on it for every 2 advancement tokens on it over 3. The rez cost of all ice is lowered by 1 for each agenda counter on Braintrust.", "stripped_title": "Braintrust", "text": "When you score Braintrust, place 1 agenda counter on it for every 2 advancement tokens on it over 3.\nThe rez cost of all ice is lowered by 1 for each agenda counter on Braintrust.", "title": "Braintrust", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_restructured_datapool_02016(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "02016", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"We're gonna need a bigger room.\"", "illustrator": "Ed Mattinian", "keywords": "Initiative", "pack_code": "wla", "position": 16, "quantity": 3, "side_code": "corp", "stripped_text": "click: Trace[2]. If successful, give the Runner 1 tag.", "stripped_title": "Restructured Datapool", "text": "[click]: Trace[2]. If successful, give the Runner 1 tag.", "title": "Restructured Datapool", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_atlas_02018(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "02018", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "keywords": "Research", "pack_code": "wla", "position": 18, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Search R&D for 1 card and reveal it. Add it to HQ.", "stripped_title": "Project Atlas", "text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3.\n<strong>Hosted agenda counter:</strong> Search R&D for 1 card and reveal it. Add it to HQ.", "title": "Project Atlas", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_fetal_ai_02032(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 2, "code": "02032", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Eko Puteh", "keywords": "Ambush", "pack_code": "ta", "position": 32, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda anywhere except in Archives, do 2 net damage. As an additional cost to steal this agenda, the Runner must pay 2 credits.", "stripped_title": "Fetal AI", "text": "While the Runner is accessing this agenda in R&D, they must reveal it.\nWhen the Runner accesses this agenda anywhere except in Archives, do 2 net damage.\nAs an additional cost to steal this agenda, the Runner must pay 2[credit].", "title": "Fetal AI", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_executive_retreat_02039(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "02039", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "JB Casacop", "pack_code": "ta", "position": 39, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Executive Retreat, place 1 agenda counter on it and shuffle HQ into R&D. click, hosted agenda counter: Draw 5 cards.", "stripped_title": "Executive Retreat", "text": "When you score Executive Retreat, place 1 agenda counter on it and shuffle HQ into R&D.\n[click], <strong>hosted agenda counter:</strong> Draw 5 cards.", "title": "Executive Retreat", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_vitruvius_02051(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "02051", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "keywords": "Research", "pack_code": "ce", "position": 51, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Add 1 card from Archives to HQ.", "stripped_title": "Project Vitruvius", "text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3.\n<strong>Hosted agenda counter:</strong> Add 1 card from Archives to HQ.", "title": "Project Vitruvius", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_government_contracts_02077(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "02077", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "It's really hard to lose a government contract.", "illustrator": "Mitchell Malloy", "pack_code": "asis", "position": 77, "quantity": 3, "side_code": "corp", "stripped_text": "click, click: Gain 4 credits.", "stripped_title": "Government Contracts", "text": "[click], [click]: Gain 4[credit].", "title": "Government Contracts", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_false_lead_02080(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "02080", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It didn't look like the headquarters of a multi-billion cred company. Probably because it wasn't.", "illustrator": "Bruno Balixa", "keywords": "Security", "pack_code": "asis", "position": 80, "quantity": 3, "side_code": "corp", "stripped_text": "Forfeit this agenda: If the Runner has 2 or more click remaining, they lose click click.", "stripped_title": "False Lead", "text": "<strong>Forfeit this agenda:</strong> If the Runner has 2 or more [click] remaining, they lose [click][click].", "title": "False Lead", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_beale_02115(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "02115", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Research", "pack_code": "fp", "position": 115, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3. This agenda is worth 1 more agenda point for each hosted agenda counter.", "stripped_title": "Project Beale", "text": "When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3.\nThis agenda is worth 1 more agenda point for each hosted agenda counter.", "title": "Project Beale", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_corporate_war_02120(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "02120", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "There were several ways to win a corporate war. One of them was to bring out the bazookas.", "illustrator": "Gong Studios", "keywords": "Expansion", "pack_code": "fp", "position": 120, "quantity": 3, "side_code": "corp", "stripped_text": "If you have at least 7 credits when you score Corporate War, gain 7 credits; otherwise, lose all credits in your credit pool.", "stripped_title": "Corporate War", "text": "If you have at least 7[credit] when you score Corporate War, gain 7[credit]; otherwise, lose all credits in your credit pool.", "title": "Corporate War", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_director_haas_pet_project_03004(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "03004", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Initiative", "pack_code": "cac", "position": 4, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may create a new remote server by installing up to 3 cards from HQ and/or Archives in the root of and/or protecting that server, ignoring all install costs. Limit 1 per deck.", "stripped_title": "Director Haas' Pet Project", "text": "When you score this agenda, you may create a new remote server by installing up to 3 cards from HQ and/or Archives in the root of and/or protecting that server, ignoring all install costs.\nLimit 1 per deck.", "title": "Director Haas' Pet Project", "type_code": "agenda", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_efficiency_committee_03005(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "03005", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Jason Rumpff", "keywords": "Initiative", "pack_code": "cac", "position": 5, "quantity": 3, "side_code": "corp", "stripped_text": "Place 3 agenda counters on Efficiency Committee when you score it. click, hosted agenda counter: Gain click click. You cannot advance cards for the remainder of this turn.", "stripped_title": "Efficiency Committee", "text": "Place 3 agenda counters on Efficiency Committee when you score it.\n[click], <strong>hosted agenda counter:</strong> Gain [click][click]. You cannot advance cards for the remainder of this turn.", "title": "Efficiency Committee", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_wotan_03006(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "03006", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Daniel Atanasov", "keywords": "Research", "pack_code": "cac", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "Place 3 agenda counters on Project Wotan when you score it. Hosted agenda counter: Choose a rezzed piece of bioroid ice currently being approached. For the remainder of this run, that ice gains \"Subroutine End the run.\" after all its other subroutines.", "stripped_title": "Project Wotan", "text": "Place 3 agenda counters on Project Wotan when you score it.\n<strong>Hosted agenda counter:</strong> Choose a rezzed piece of <strong>bioroid</strong> ice currently being approached. For the remainder of this run, that ice gains \"[subroutine] End the run.\" after all its other subroutines.", "title": "Project Wotan", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_sentinel_defense_program_03007(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "03007", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"Why limit our best assets to our own servers? The enemy doesn't stay passively at home, waiting for us to come to him. Why should we?\" -Director Haas", "illustrator": "Ed Mattinian", "keywords": "Security", "pack_code": "cac", "position": 7, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner suffers at least 1 core damage, do 1 net damage.", "stripped_title": "Sentinel Defense Program", "text": "Whenever the Runner suffers at least 1 core damage, do 1 net damage.", "title": "Sentinel Defense Program", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_gila_hands_arcology_03023(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "03023", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Sell the dream-show them how very much they want to be rich, and they'll convince themselves that someday, they will be. How can they revolt against their future selves? -the New Gospel of Wealth", "illustrator": "Emilio Rodriguez", "keywords": "Expansion", "pack_code": "cac", "position": 23, "quantity": 3, "side_code": "corp", "stripped_text": "click, click: Gain 3 credits.", "stripped_title": "Gila Hands Arcology", "text": "[click], [click]: Gain 3[credit].", "title": "Gila Hands Arcology", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_ares_04010(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "04010", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Who wants to start a war?", "illustrator": "Emilio Rodriguez", "keywords": "Security", "pack_code": "om", "position": 10, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, the Runner trashes 1 of their installed cards for each hosted advancement counter past 4. If the Runner trashes at least 1 card this way, take 1 bad publicity.", "stripped_title": "Project Ares", "text": "When you score this agenda, the Runner trashes 1 of their installed cards for each hosted advancement counter past 4. If the Runner trashes at least 1 card this way, take 1 bad publicity.", "title": "Project Ares", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_character_assassination_04014(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "04014", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"The thing about journalism is there's always a better story around the corner. Soon, they smelled blood elsewhere, and the world forgot about me. But I didn't forget.\" -The Professor", "illustrator": "Mike Nesbitt", "keywords": "Security", "pack_code": "om", "position": 14, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Character Assassination, trash 1 resource (cannot be prevented).", "stripped_title": "Character Assassination", "text": "When you score Character Assassination, trash 1 resource (cannot be prevented).", "title": "Character Assassination", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_geothermal_fracking_04017(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "04017", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Pumping water into deep sea thermal vents produced huge amounts of energy. A profitable side effect.", "illustrator": "Mike Nesbitt", "keywords": "Expansion", "pack_code": "om", "position": 17, "quantity": 3, "side_code": "corp", "stripped_text": "Place 2 agenda counters on Geothermal Fracking when you score it. click, hosted agenda counter: Gain 7 credits and take 1 bad publicity.", "stripped_title": "Geothermal Fracking", "text": "Place 2 agenda counters on Geothermal Fracking when you score it.\n[click], <strong>hosted agenda counter:</strong> Gain 7[credit] and take 1 bad publicity.", "title": "Geothermal Fracking", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_clone_retirement_04032(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "04032", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"They call it 'retirement'. I call it 'euthanasia'.\" -Ken \"Express\" Tenma", "illustrator": "Gong Studios", "keywords": "Initiative", "pack_code": "st", "position": 32, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Clone Retirement, you may remove 1 bad publicity. When the Runner steals Clone Retirement, the Corp takes 1 bad publicity.", "stripped_title": "Clone Retirement", "text": "When you score Clone Retirement, you may remove 1 bad publicity.\nWhen the Runner steals Clone Retirement, the Corp takes 1 bad publicity.", "title": "Clone Retirement", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_the_cleaners_04036(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "04036", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"I use bioroids because I can wipe their memories or just blow their brains out when the job is done. No witnesses means no witnesses.\"", "illustrator": "Gong Studios", "keywords": "Security", "pack_code": "st", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "Interrupt -> Whenever you would do meat damage, increase that damage by 1.", "stripped_title": "The Cleaners", "text": "[interrupt] \u2192 Whenever you would do meat damage, increase that damage by 1.", "title": "The Cleaners", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_profiteering_04039(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "04039", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It was surprisingly easy to make creds\u2026if you didn't care about how you made them.", "illustrator": "JuanManuel Tumburus", "pack_code": "st", "position": 39, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Profiteering, take up to 3 bad publicity. Gain 5 credits for each bad publicity taken.", "stripped_title": "Profiteering", "text": "When you score Profiteering, take up to 3 bad publicity. Gain 5[credit] for each bad publicity taken.", "title": "Profiteering", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_unorthodox_predictions_04053(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "04053", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Bruno Balixa", "keywords": "Security", "pack_code": "mt", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Unorthodox Predictions, choose sentry, code gate or barrier. Subroutines on ice of the chosen type cannot be broken until the beginning of your next turn.", "stripped_title": "Unorthodox Predictions", "text": "When you score Unorthodox Predictions, choose <strong>sentry</strong>, <strong>code gate</strong> or <strong>barrier</strong>. Subroutines on ice of the chosen type cannot be broken until the beginning of your next turn.", "title": "Unorthodox Predictions", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_tgtbt_04075(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "04075", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"The damn raven just kind of cawed at me as I went past. I should have known it was too good to be true.\"", "illustrator": "Adam S. Doyle", "keywords": "Ambush", "pack_code": "tc", "position": 75, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, give them 1 tag.", "stripped_title": "TGTBT", "text": "While the Runner is accessing this agenda in R&D, they must reveal it.\nWhen the Runner accesses this agenda, give them 1 tag.", "title": "TGTBT", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_veterans_program_04080(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "04080", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It's easy to replace limbs. It's more difficult to replace memories.", "illustrator": "Gong Studios", "keywords": "Initiative", "pack_code": "tc", "position": 80, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Veterans Program, you may remove up to 2 bad publicity.", "stripped_title": "Veterans Program", "text": "When you score Veterans Program, you may remove up to 2 bad publicity.", "title": "Veterans Program", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_market_research_04095(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "04095", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Gong Studios", "keywords": "Research", "pack_code": "fal", "position": 95, "quantity": 3, "side_code": "corp", "stripped_text": "If the Runner is tagged when you score Market Research, place 1 agenda counter on it. Market Research is worth 1 additional agenda point while it has an agenda counter on it.", "stripped_title": "Market Research", "text": "If the Runner is tagged when you score Market Research, place 1 agenda counter on it.\nMarket Research is worth 1 additional agenda point while it has an agenda counter on it.", "title": "Market Research", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_vulcan_coverup_04098(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "04098", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"I did warn you that leaks would have to be patched.\"", "illustrator": "Adam Schumpert", "keywords": "Security", "pack_code": "fal", "position": 98, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Vulcan Coverup, do 2 meat damage. When the Runner steals Vulcan Coverup, take 1 bad publicity.", "stripped_title": "Vulcan Coverup", "text": "When you score Vulcan Coverup, do 2 meat damage.\nWhen the Runner steals Vulcan Coverup, take 1 bad publicity.", "title": "Vulcan Coverup", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_napd_contract_04119(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "04119", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Viktoria Gavrilenko", "keywords": "Security", "pack_code": "dt", "position": 119, "quantity": 3, "side_code": "corp", "stripped_text": "The advancement requirement of NAPD Contract is increased by 1 for each bad publicity the Corp has. As an additional cost to steal NAPD Contract, the Runner must pay 4 credits.", "stripped_title": "NAPD Contract", "text": "The advancement requirement of NAPD Contract is increased by 1 for each bad publicity the Corp has.\nAs an additional cost to steal NAPD Contract, the Runner must pay 4[credit].", "title": "NAPD Contract", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_house_of_knives_05004(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "05004", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Alexandr Elichev", "keywords": "Security", "pack_code": "hap", "position": 4, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 3 agenda counters on it. Hosted agenda counter: Do 1 net damage. Use this ability only during a run and only once per run.", "stripped_title": "House of Knives", "text": "When you score this agenda, place 3 agenda counters on it.\n<strong>Hosted agenda counter:</strong> Do 1 net damage. Use this ability only during a run and only once per run.", "title": "House of Knives", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_medical_breakthrough_05005(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "05005", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"You won't feel it. Or anything else, for that matter.\"", "illustrator": "Gong Studios", "keywords": "Research", "pack_code": "hap", "position": 5, "quantity": 3, "side_code": "corp", "stripped_text": "Lower the advancement requirement of each Medical Breakthrough by 1. This ability is active even while Medical Breakthrough is in the Runner's score area.", "stripped_title": "Medical Breakthrough", "text": "Lower the advancement requirement of each Medical Breakthrough by 1. This ability is active even while Medical Breakthrough is in the Runner's score area.", "title": "Medical Breakthrough", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_philotic_entanglement_05006(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "05006", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Ed Mattinian", "keywords": "Security", "pack_code": "hap", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Philotic Entanglement, do 1 net damage for each agenda in the Runner's score area. Limit 1 Philotic Entanglement per deck.", "stripped_title": "Philotic Entanglement", "text": "When you score Philotic Entanglement, do 1 net damage for each agenda in the Runner's score area.\nLimit 1 Philotic Entanglement per deck.", "title": "Philotic Entanglement", "type_code": "agenda", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_the_future_perfect_05007(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "05007", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Christina Davis", "keywords": "Initiative - Psi", "pack_code": "hap", "position": 7, "quantity": 3, "side_code": "corp", "stripped_text": "When the Runner accesses The Future Perfect, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, prevent The Future Perfect from being stolen. Ignore this ability if the Runner accesses The Future Perfect while it is installed.", "stripped_title": "The Future Perfect", "text": "When the Runner accesses The Future Perfect, you and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, prevent The Future Perfect from being stolen. Ignore this ability if the Runner accesses The Future Perfect while it is installed.", "title": "The Future Perfect", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_domestic_sleepers_06001(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 0, "code": "06001", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Adrian Dadich", "pack_code": "up", "position": 1, "quantity": 3, "side_code": "corp", "stripped_text": "click,click,click: Place 1 agenda counter on Domestic Sleepers. Domestic Sleepers is worth 1 agenda point while it has at least 1 agenda counter on it.", "stripped_title": "Domestic Sleepers", "text": "[click],[click],[click]: Place 1 agenda counter on Domestic Sleepers.\nDomestic Sleepers is worth 1 agenda point while it has at least 1 agenda counter on it.", "title": "Domestic Sleepers", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_encrypted_portals_06024(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "06024", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"Binary computing is obsolete. I use a base-4 structure for this system; it's modeled on our DNA. Well, my DNA, anyway.\" -Doctor Endo, Jinteki researcher", "illustrator": "Adam S. Doyle", "keywords": "Security", "pack_code": "tsb", "position": 24, "quantity": 3, "side_code": "corp", "stripped_text": "All code gate ice have +1 strength. When you score Encrypted Portals, gain 1 credit for each rezzed code gate.", "stripped_title": "Encrypted Portals", "text": "All <strong>code gate</strong> ice have +1 strength.\nWhen you score Encrypted Portals, gain 1[credit] for each rezzed <strong>code gate</strong>.", "title": "Encrypted Portals", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_eden_fragment_06030(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "06030", "deck_limit": 1, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Seage", "keywords": "Source", "pack_code": "tsb", "position": 30, "quantity": 3, "side_code": "corp", "stripped_text": "Ignore the install cost of the first piece of ice you install each turn. Limit 1 per deck.", "stripped_title": "Eden Fragment", "text": "Ignore the install cost of the first piece of ice you install each turn.\nLimit 1 per deck.", "title": "Eden Fragment", "type_code": "agenda", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_chronos_project_06049(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "06049", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "The irony is that those who'd want to destroy certain memories can't afford to do so, and those who can afford it-well, they're too busy sipping on dreamwine.", "illustrator": "Adam S. Doyle", "keywords": "Research", "pack_code": "fc", "position": 49, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, the Runner removes all cards in the heap from the game.", "stripped_title": "Chronos Project", "text": "When you score this agenda, the Runner removes all cards in the heap from the game.", "title": "Chronos Project", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_labyrinthine_servers_06063(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "06063", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Lili Ibrahim", "keywords": "Security", "pack_code": "uao", "position": 63, "quantity": 3, "side_code": "corp", "stripped_text": "Place 2 power counters on Labyrinthine Servers when you score it. Hosted power counter: Prevent the Runner from jacking out. The Runner cannot jack out for the remainder of this run.", "stripped_title": "Labyrinthine Servers", "text": "Place 2 power counters on Labyrinthine Servers when you score it.\n<strong>Hosted power counter:</strong> Prevent the Runner from jacking out. The Runner cannot jack out for the remainder of this run.", "title": "Labyrinthine Servers", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_hades_fragment_06071(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "06071", "deck_limit": 1, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Seage", "keywords": "Source", "pack_code": "uao", "position": 71, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may add 1 card from Archives to the bottom of R&D. Limit 1 per deck.", "stripped_title": "Hades Fragment", "text": "When your turn begins, you may add 1 card from Archives to the bottom of R&D.\nLimit 1 per deck.", "title": "Hades Fragment", "type_code": "agenda", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_bifrost_array_06081(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "06081", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"'What does it do?' Whatever I bloody want it to do.\" -Director Haas", "illustrator": "Veli Nystr\u00f6m", "keywords": "Initiative", "pack_code": "atr", "position": 81, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Bifrost Array, you may trigger the \"when scored\" ability of another agenda that is not a copy of Bifrost Array in your score area.", "stripped_title": "Bifrost Array", "text": "When you score Bifrost Array, you may trigger the \"when scored\" ability of another agenda that is not a copy of Bifrost Array in your score area.", "title": "Bifrost Array", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_license_acquisition_06085(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "06085", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"We've received seventeen crates from ChiLo. We'll hit stores the same day we sign the license agreement.\"", "illustrator": "Crystal Ben", "keywords": "Expansion", "pack_code": "atr", "position": 85, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may reveal 1 asset or upgrade in HQ or Archives. Install and rez that card, ignoring all costs.", "stripped_title": "License Acquisition", "text": "When you score this agenda, you may reveal 1 asset or upgrade in HQ or Archives. Install and rez that card, ignoring all costs.", "title": "License Acquisition", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_superior_cyberwalls_06087(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "06087", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"Our new barriers will be built on the rubble of our enemies\".", "illustrator": "Gong Studios", "keywords": "Security", "pack_code": "atr", "position": 87, "quantity": 3, "side_code": "corp", "stripped_text": "All barrier ice have +1 strength. When you score Superior Cyberwalls, gain 1 credit for each rezzed barrier.", "stripped_title": "Superior Cyberwalls", "text": "All <strong>barrier</strong> ice have +1 strength.\nWhen you score Superior Cyberwalls, gain 1[credit] for each rezzed <strong>barrier</strong>.", "title": "Superior Cyberwalls", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_helium3_deposit_06101(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "06101", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "It takes power to create power.", "illustrator": "Emilio Rodriguez", "pack_code": "ts", "position": 101, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Helium-3 Deposit, place up to 2 power counters on a card with at least 1 power counter on it.", "stripped_title": "Helium-3 Deposit", "text": "When you score Helium-3 Deposit, place up to 2 power counters on a card with at least 1 power counter on it.", "title": "Helium-3 Deposit", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_utopia_fragment_06110(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "06110", "deck_limit": 1, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Seage", "keywords": "Source", "pack_code": "ts", "position": 110, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to steal an agenda, the Runner must pay 2 credits for each advancement token on that agenda. Limit 1 per deck.", "stripped_title": "Utopia Fragment", "text": "As an additional cost to steal an agenda, the Runner must pay 2[credit] for each advancement token on that agenda.\nLimit 1 per deck.", "title": "Utopia Fragment", "type_code": "agenda", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_firmware_updates_07004(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "07004", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Ed Mattinian", "keywords": "Security", "pack_code": "oac", "position": 4, "quantity": 3, "side_code": "corp", "stripped_text": "Place 3 agenda counters on Firmware Updates when you score it. Hosted agenda counter: Place 1 advancement token on a piece of ice that can be advanced. Use this ability only once per turn.", "stripped_title": "Firmware Updates", "text": "Place 3 agenda counters on Firmware Updates when you score it.\n<strong>Hosted agenda counter:</strong> Place 1 advancement token on a piece of ice that can be advanced. Use this ability only once per turn.", "title": "Firmware Updates", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_glenn_station_07005(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "07005", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Dawn Carlos", "keywords": "Expansion", "pack_code": "oac", "position": 5, "quantity": 3, "side_code": "corp", "stripped_text": "Glenn Station can host a single card. click: Host a card from HQ facedown on Glenn Station. click: Add a card on Glenn Station to HQ.", "stripped_title": "Glenn Station", "text": "Glenn Station can host a single card.\n[click]: Host a card from HQ facedown on Glenn Station.\n[click]: Add a card on Glenn Station to HQ.", "title": "Glenn Station", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_government_takeover_07006(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 9, "agenda_points": 6, "code": "07006", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "It is essential to liberate a populace from tyranny before that tyranny takes root.", "illustrator": "Matt Zeilinger", "keywords": "Expansion", "pack_code": "oac", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "click: Gain 3 credits. Limit 1 Government Takeover per deck.", "stripped_title": "Government Takeover", "text": "[click]: Gain 3[credit].\nLimit 1 Government Takeover per deck.", "title": "Government Takeover", "type_code": "agenda", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_highrisk_investment_07007(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "07007", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"Trust me. I know what I'm doing.\"", "illustrator": "Kate Laird", "keywords": "Expansion", "pack_code": "oac", "position": 7, "quantity": 3, "side_code": "corp", "stripped_text": "Place 1 agenda counter on High-Risk Investment when you score it. click, hosted agenda counter: Gain 1 credit for each credit in the Runner's credit pool.", "stripped_title": "High-Risk Investment", "text": "Place 1 agenda counter on High-Risk Investment when you score it.\n[click], <strong>hosted agenda counter:</strong> Gain 1[credit] for each credit in the Runner's credit pool.", "title": "High-Risk Investment", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_genetic_resequencing_08013(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "08013", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"The best part of our work is that nothing is ever wasted. A gene that is useful once will surely be useful again.\" -Wong Ya Ching", "illustrator": "Rovina Cai", "keywords": "Research", "pack_code": "val", "position": 13, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Genetic Resequencing, you may place 1 agenda counter on an agenda in your score area.", "stripped_title": "Genetic Resequencing", "text": "When you score Genetic Resequencing, you may place 1 agenda counter on an agenda in your score area.", "title": "Genetic Resequencing", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_research_grant_08032(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "08032", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"My research could make your corporation billions. And save lives, of course.\"", "illustrator": "Rebecca Sorge", "keywords": "Research", "pack_code": "bb", "position": 32, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Research Grant, you may score another copy of Research Grant that is installed.", "stripped_title": "Research Grant", "text": "When you score Research Grant, you may score another copy of Research Grant that is installed.", "title": "Research Grant", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_selfdestruct_chips_08051(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "08051", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Cyber enhancements can be dangerous in the wrong hands.", "illustrator": "Abrar Ajmal", "keywords": "Security", "pack_code": "cc", "position": 51, "quantity": 3, "side_code": "corp", "stripped_text": "The Runner's maximum hand size is reduced by 1.", "stripped_title": "Self-Destruct Chips", "text": "The Runner's maximum hand size is reduced by 1.", "title": "Self-Destruct Chips", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_oaktown_renovation_08058(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "08058", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Maciej Rebisz", "keywords": "Public - Initiative", "pack_code": "cc", "position": 58, "quantity": 3, "side_code": "corp", "stripped_text": "Install only faceup. (This agenda is neither rezzed nor unrezzed.) Whenever you advance this agenda, gain 2 credits. If there are 5 or more hosted advancement counters (including the counter just placed), gain 3 credits instead.", "stripped_title": "Oaktown Renovation", "text": "Install only faceup. <em>(This agenda is neither rezzed nor unrezzed.)</em>\nWhenever you advance this agenda, gain 2[credit]. If there are 5 or more hosted advancement counters <em>(including the counter just placed)</em>, gain 3[credit] instead.", "title": "Oaktown Renovation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_underway_renovation_08077(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "08077", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Alex Kim", "keywords": "Initiative - Public", "pack_code": "uw", "position": 77, "quantity": 3, "side_code": "corp", "stripped_text": "Install Underway Renovation faceup. Whenever you advance Underway Renovation, trash the top card of the Runner's stack (or top 2 cards instead if there are 4 or more advancement tokens on Underway Renovation).", "stripped_title": "Underway Renovation", "text": "Install Underway Renovation faceup.\nWhenever you advance Underway Renovation, trash the top card of the Runner's stack (or top 2 cards instead if there are 4 or more advancement tokens on Underway Renovation).", "title": "Underway Renovation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_award_bait_08093(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "08093", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Clark Huggins", "keywords": "Sensie", "pack_code": "oh", "position": 93, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, you may place up to 2 advancement counters on 1 installed card you can advance.", "stripped_title": "Award Bait", "text": "While the Runner is accessing this agenda in R&D, they must reveal it.\nWhen the Runner accesses this agenda, you may place up to 2 advancement counters on 1 installed card you can advance.", "title": "Award Bait", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_explodeapalooza_08094(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "08094", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "It's like Lethal Action 3, only with more explosions.", "illustrator": "Mike Nesbitt", "keywords": "Sensie", "pack_code": "oh", "position": 94, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, you may gain 5 credits.", "stripped_title": "Explode-a-palooza", "text": "While the Runner is accessing this agenda in R&D, they must reveal it.\nWhen the Runner accesses this agenda, you may gain 5[credit].", "title": "Explode-a-palooza", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_hollywood_renovation_08098(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "08098", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "David Ogilvie", "keywords": "Initiative - Public", "pack_code": "oh", "position": 98, "quantity": 3, "side_code": "corp", "stripped_text": "Install Hollywood Renovation faceup. Whenever you advance Hollywood Renovation, you may place 1 advancement token on another card that can be advanced (or 2 advancement tokens instead if there are 6 or more advancement tokens on Hollywood Renovation).", "stripped_title": "Hollywood Renovation", "text": "Install Hollywood Renovation faceup.\nWhenever you advance Hollywood Renovation, you may place 1 advancement token on another card that can be advanced (or 2 advancement tokens instead if there are 6 or more advancement tokens on Hollywood Renovation).", "title": "Hollywood Renovation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_vanity_project_08100(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 6, "agenda_points": 4, "code": "08100", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 1, "flavor": "EXT. KANSAS - DAY\nDOROTHY (Miranda) gazes out at the horizon. A sudden gust of wind catches her hair. Above the windblasted prairie loom ominous STORM CLOUDS.\nDOROTHY: If only I wasn't in Kansas anymore.\nShe begins to hum a haunting melody.", "illustrator": "Ashley Witter", "pack_code": "oh", "position": 100, "quantity": 3, "side_code": "corp", "stripped_title": "Vanity Project", "title": "Vanity Project", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_ancestral_imager_08112(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "08112", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "The more people submit their DNA and family history to the program, the more accurate it becomes.", "illustrator": "Alexandr Elichev", "keywords": "Security", "pack_code": "uot", "position": 112, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner jacks out, do 1 net damage.", "stripped_title": "Ancestral Imager", "text": "Whenever the Runner jacks out, do 1 net damage.", "title": "Ancestral Imager", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_the_future_is_now_08120(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "08120", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Tim Durning", "keywords": "Initiative", "pack_code": "uot", "position": 120, "quantity": 3, "side_code": "corp", "stripped_text": "When you score The Future is Now, search R&D for a card and add it to HQ. Shuffle R&D.", "stripped_title": "The Future is Now", "text": "When you score The Future is Now, search R&D for a card and add it to HQ. Shuffle R&D.", "title": "The Future is Now", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_15_minutes_09004(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "09004", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "You had your shot, and you blew it.", "illustrator": "Hannah Christenson", "pack_code": "dad", "position": 4, "quantity": 3, "side_code": "corp", "stripped_text": "click: Shuffle 15 Minutes into R&D. The Corp can trigger this ability while 15 Minutes is in the Runner's score area. Limit 1 per deck.", "stripped_title": "15 Minutes", "text": "[click]: Shuffle 15 Minutes into R&D. The Corp can trigger this ability while 15 Minutes is in the Runner's score area.\nLimit 1 per deck.", "title": "15 Minutes", "type_code": "agenda", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_improved_tracers_09005(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "09005", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"The trick isn't software, it's hardware. Cyberspace is a collection of physical machines. If we control the machines, we control it all.\" -KR Kane, \"Our Future\"", "illustrator": "Adam S. Doyle", "keywords": "Security", "pack_code": "dad", "position": 5, "quantity": 3, "side_code": "corp", "stripped_text": "All tracer ice have +1 strength. The base trace strength of each subroutine is increased by 1.", "stripped_title": "Improved Tracers", "text": "All <strong>tracer</strong> ice have +1 strength.\nThe base trace strength of each subroutine is increased by 1.", "title": "Improved Tracers", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_rebranding_team_09006(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "09006", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"Nobody ever lost a dollar by underestimating the taste of the public.\" -Phineas Taylor Barnum", "illustrator": "Tiffany Turrill", "keywords": "Initiative", "pack_code": "dad", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "All assets gain advertisement.", "stripped_title": "Rebranding Team", "text": "All assets gain <strong>advertisement</strong>.", "title": "Rebranding Team", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_quantum_predictive_model_09007(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "09007", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"Yes <strong>and</strong> No.\"", "illustrator": "Liiga Smilshkalne", "keywords": "Security", "pack_code": "dad", "position": 7, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda while they are tagged, add it to your score area.", "stripped_title": "Quantum Predictive Model", "text": "While the Runner is accessing this agenda in R&D, they must reveal it.\nWhen the Runner accesses this agenda while they are tagged, add it to your score area.", "title": "Quantum Predictive Model", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_global_food_initiative_09026(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "09026", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 1, "flavor": "\"Corporations are made up of people. It's ridiculous to think they'd be either all good or all bad.\" -Sunny Lebeau", "illustrator": "Meg Owenson", "keywords": "Initiative", "pack_code": "dad", "position": 26, "quantity": 3, "side_code": "corp", "stripped_text": "Global Food Initiative is worth 1 fewer agenda point while in the Runner's score area.", "stripped_title": "Global Food Initiative", "text": "Global Food Initiative is worth 1 fewer agenda point while in the Runner's score area.", "title": "Global Food Initiative", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_advanced_concept_hopper_10011(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "10011", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"I don't want a hopper. I've never even owned one. But every time I jack in, that same damn ad loads.\" -2xTiger", "illustrator": "BalanceSheet", "keywords": "Research", "pack_code": "kg", "position": 11, "quantity": 3, "side_code": "corp", "stripped_text": "The first time the Runner initiates a run each turn, you may draw 1 card or gain 1 credit.", "stripped_title": "Advanced Concept Hopper", "text": "The first time the Runner initiates a run each turn, you may draw 1 card or gain 1[credit].", "title": "Advanced Concept Hopper", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_remote_data_farm_10033(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "10033", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "Data, not food, is one of the biggest exports from the Gujarat district of Mumbad.", "illustrator": "Juan Novelletto", "keywords": "Expansion", "pack_code": "bf", "position": 33, "quantity": 3, "side_code": "corp", "stripped_text": "Your maximum hand size is increased by 2.", "stripped_title": "Remote Data Farm", "text": "Your maximum hand size is increased by 2.", "title": "Remote Data Farm", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_new_construction_10035(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "10035", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Kirsten Zirngibl", "keywords": "Public", "pack_code": "bf", "position": 35, "quantity": 3, "side_code": "corp", "stripped_text": "Install only faceup. (This agenda is neither rezzed nor unrezzed.) Whenever you advance this agenda, you may install 1 card from HQ in the root of a new server. If there are 5 or more hosted advancement counters, rez that card, ignoring all costs.", "stripped_title": "New Construction", "text": "Install only faceup. <em>(This agenda is neither rezzed nor unrezzed.)</em>\nWhenever you advance this agenda, you may install 1 card from HQ in the root of a new server. If there are 5 or more hosted advancement counters, rez that card, ignoring all costs.", "title": "New Construction", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_corporate_sales_team_10037(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "10037", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"You got it. We sell it. They buy it. Everyone wins.\"", "illustrator": "Samuel Leung", "keywords": "Expansion", "pack_code": "bf", "position": 37, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Corporate Sales Team, place 10 credits on it. When each player's turn begins, take 1 credit from Corporate Sales Team.", "stripped_title": "Corporate Sales Team", "text": "When you score Corporate Sales Team, place 10[credit] on it.\nWhen each player's turn begins, take 1[credit] from Corporate Sales Team.", "title": "Corporate Sales Team", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_voting_machine_initiative_10048(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "10048", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Marko Fiedler", "keywords": "Initiative", "pack_code": "dag", "position": 48, "quantity": 3, "side_code": "corp", "stripped_text": "Place 3 agenda counters on Voting Machine Initiative when you score it. When the Runner's turn begins, you may spend 1 hosted agenda counter. If you do, the Runner loses click, if able.", "stripped_title": "Voting Machine Initiative", "text": "Place 3 agenda counters on Voting Machine Initiative when you score it.\nWhen the Runner's turn begins, you may spend 1 hosted agenda counter. If you do, the Runner loses [click], if able.", "title": "Voting Machine Initiative", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_personality_profiles_10066(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "10066", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Sander Mosk", "keywords": "Security", "pack_code": "si", "position": 66, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner searches the stack or installs a card from the heap, they trash 1 card from the grip at random.", "stripped_title": "Personality Profiles", "text": "Whenever the Runner searches the stack or installs a card from the heap, they trash 1 card from the grip at random.", "title": "Personality Profiles", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_dedicated_neural_net_10088(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "10088", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "keywords": "Initiative - Psi", "pack_code": "tlm", "position": 88, "quantity": 3, "side_code": "corp", "stripped_text": "The first time there is a successful run on HQ each turn, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, you choose which cards the Runner accesses from HQ for the remainder of this run.", "stripped_title": "Dedicated Neural Net", "text": "The first time there is a successful run on HQ each turn, you and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, you choose which cards the Runner accesses from HQ for the remainder of this run.", "title": "Dedicated Neural Net", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_puppet_master_10090(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "10090", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Miguel Coronado III", "keywords": "Initiative", "pack_code": "tlm", "position": 90, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner makes a successful run, you may place 1 advancement token on a card that can be advanced.", "stripped_title": "Puppet Master", "text": "Whenever the Runner makes a successful run, you may place 1 advancement token on a card that can be advanced.", "title": "Puppet Master", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_improved_protein_source_10105(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 3, "code": "10105", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "They eat us, we eat them, the cycle goes on and on. -Omar Keung, \"the Flashpoint\"", "illustrator": "Johnny Morrow", "keywords": "Research", "pack_code": "ftm", "position": 105, "quantity": 3, "side_code": "corp", "stripped_text": "When Improved Protein Source is scored or stolen, the Runner gains 4 credits.", "stripped_title": "Improved Protein Source", "text": "When Improved Protein Source is scored or stolen, the Runner gains 4[credit].", "title": "Improved Protein Source", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_merger_10114(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "10114", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 1, "flavor": "Survival of the fittest' is so outdated; in finance it's 'survival of the fattest.' -Omar Keung, \"the Flashpoint\"", "illustrator": "Mariusz Siergiejew", "keywords": "Expansion", "pack_code": "ftm", "position": 114, "quantity": 3, "side_code": "corp", "stripped_text": "Merger is worth 1 additional agenda point while in the Runner's score area.", "stripped_title": "Merger", "text": "Merger is worth 1 additional agenda point while in the Runner's score area.", "title": "Merger", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_crisis_management_11018(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "11018", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"For the duration of the emergency\" is code for \"this is the way things are now.\"", "illustrator": "Natalie Bernard", "keywords": "Security", "pack_code": "23s", "position": 18, "quantity": 3, "side_code": "corp", "stripped_text": "If the Runner is tagged, Crisis Management gains \"When your turn begins, do 1 meat damage.\"", "stripped_title": "Crisis Management", "text": "If the Runner is tagged, Crisis Management gains \"When your turn begins, do 1 meat damage.\"", "title": "Crisis Management", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_kusanagi_11052(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 0, "code": "11052", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Priscilla Kim", "keywords": "Security", "pack_code": "es", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Project Kusanagi, place 1 agenda counter on it for each advancement token on it over 2. Hosted agenda counter: Choose 1 piece of ice to gain \"Subroutine Do 1 net damage.\" after all its other subroutines for the remainder of this run.", "stripped_title": "Project Kusanagi", "text": "When you score Project Kusanagi, place 1 agenda counter on it for each advancement token on it over 2.\n<strong>Hosted agenda counter:</strong> Choose 1 piece of ice to gain \"[subroutine] Do 1 net damage.\" after all its other subroutines for the remainder of this run.", "title": "Project Kusanagi", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_show_of_force_11099(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "11099", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Walk loudly and carry a bigger stick.", "illustrator": "Adam S. Doyle", "keywords": "Security", "pack_code": "ml", "position": 99, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Show of Force, do 2 meat damage.", "stripped_title": "Show of Force", "text": "When you score Show of Force, do 2 meat damage.", "title": "Show of Force", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_sensor_net_activation_11110(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "11110", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Samuel Leung", "keywords": "Security", "pack_code": "qu", "position": 110, "quantity": 3, "side_code": "corp", "stripped_text": "Place 1 agenda counter on Sensor Net Activation when you score it. Hosted agenda counter: Rez a bioroid, ignoring all costs. When the turn ends, derez that bioroid.", "stripped_title": "Sensor Net Activation", "text": "Place 1 agenda counter on Sensor Net Activation when you score it.\n<strong>Hosted agenda counter:</strong> Rez a <strong>bioroid</strong>, ignoring all costs. When the turn ends, derez that <strong>bioroid</strong>.", "title": "Sensor Net Activation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_net_quarantine_11114(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "11114", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Yog Joshi", "keywords": "Security", "pack_code": "qu", "position": 114, "quantity": 3, "side_code": "corp", "stripped_text": "For the first trace each turn, the Runner's link is treated as 0. (They can still increase their link strength by spending credits.) Whenever the Runner spends credits to increase their link strength, gain 1 credit for every 2 credits they spent.", "stripped_title": "Net Quarantine", "text": "For the first trace each turn, the Runner's [link] is treated as 0. <em>(They can still increase their link strength by spending credits.)</em>\nWhenever the Runner spends credits to increase their link strength, gain 1[credit] for every 2[credit] they spent.", "title": "Net Quarantine", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_next_wave_2_12009(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "12009", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"The newest electronic-warfare rollout from NEXT Design has us sysops drooling.\" -Mason Bellamy", "illustrator": "Shawn Ye Zhongyi", "keywords": "NEXT", "pack_code": "dc", "position": 9, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, if there is a rezzed piece of NEXT ice, you may do 1 core damage.", "stripped_title": "NEXT Wave 2", "text": "When you score this agenda, if there is a rezzed piece of <strong>NEXT</strong> ice, you may do 1 core damage.", "title": "NEXT Wave 2", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_obokata_protocol_12070(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "12070", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"Proper application of stress can create the most profound changes.\" - Tennin Institute Intern Brief", "illustrator": "Jan-Wah Li", "keywords": "Ambush", "pack_code": "baw", "position": 70, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to steal Obokata Protocol, the Runner must suffer 4 net damage.", "stripped_title": "Obokata Protocol", "text": "As an additional cost to steal Obokata Protocol, the Runner must suffer 4 net damage.", "title": "Obokata Protocol", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_escalate_vitriol_12073(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "12073", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"Of course words hurt.\" -Bex Gleeson", "illustrator": "Timur Shevtsov", "keywords": "Initiative", "pack_code": "baw", "position": 73, "quantity": 3, "side_code": "corp", "stripped_text": "click: Gain 1 credit for each tag the Runner has. Use this ability only once per turn.", "stripped_title": "Escalate Vitriol", "text": "[click]: Gain 1[credit] for each tag the Runner has. Use this ability only once per turn.", "title": "Escalate Vitriol", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_reeducation_12074(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "12074", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Wenjuinn Png", "keywords": "Initiative", "pack_code": "baw", "position": 74, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may add X cards from HQ to the bottom of R&D to draw X cards. The Runner adds X cards from the grip at random to the bottom of the stack, if able.", "stripped_title": "Reeducation", "text": "When you score this agenda, you may add X cards from HQ to the bottom of R&D to draw X cards. The Runner adds X cards from the grip at random to the bottom of the stack, if able.", "title": "Reeducation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_meteor_mining_12076(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 2, "code": "12076", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"I've got a rock!\" - Charles \"Mad Dog\" Brun, Comet Jockey", "illustrator": "Mark Molnar", "pack_code": "baw", "position": 76, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Meteor Mining, you may gain 7 credits. If the Runner has at least 2 tags, you may do 7 meat damage instead.", "stripped_title": "Meteor Mining", "text": "When you score Meteor Mining, you may gain 7[credit]. If the Runner has at least 2 tags, you may do 7 meat damage instead.", "title": "Meteor Mining", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_standoff_12077(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 0, "code": "12077", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Ed Mattinian", "pack_code": "baw", "position": 77, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, the Runner may trash 1 of their installed cards. If they do not, draw 1 card and gain 5 credits. Otherwise, you may trash 1 of your installed cards to repeat this process.", "stripped_title": "Standoff", "text": "When you score this agenda, the Runner may trash 1 of their installed cards. If they do not, draw 1 card and gain 5[credit]. Otherwise, you may trash 1 of your installed cards to repeat this process.", "title": "Standoff", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_mandatory_seed_replacement_12092(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "12092", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"As you'll see on page 276, section CDXXIX, paragraph 47, line 102 of your contract, you are overdue for your seed upgrade, and all growth from out of date seed is to be confiscated and destroyed.\"", "illustrator": "Ed Mattinian", "keywords": "Security", "pack_code": "fm", "position": 92, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Mandatory Seed Replacement, rearrange any number of ice protecting all servers.", "stripped_title": "Mandatory Seed Replacement", "text": "When you score Mandatory Seed Replacement, rearrange any number of ice protecting all servers.", "title": "Mandatory Seed Replacement", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_water_monopoly_12093(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "12093", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "AgInfusion doesn't just have patents on nearly every plant seed that is farmed on Mars\u2014they own most of the rights to the water that the farms use.", "illustrator": "Mark Molnar", "keywords": "Initiative", "pack_code": "fm", "position": 93, "quantity": 3, "side_code": "corp", "stripped_text": "The install cost of each non-virtual resource is increased by 1.", "stripped_title": "Water Monopoly", "text": "The install cost of each non-<strong>virtual</strong> resource is increased by 1.", "title": "Water Monopoly", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_cfc_excavation_contract_12110(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "12110", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"Sure, we also use human labor\u2014they are more easily replaced.\" -Emil Merk", "illustrator": "Mark Molnar", "pack_code": "cd", "position": 110, "quantity": 3, "side_code": "corp", "stripped_text": "When you score CFC Excavation Contract, gain 2 credits for each rezzed bioroid.", "stripped_title": "CFC Excavation Contract", "text": "When you score CFC Excavation Contract, gain 2[credit] for each rezzed <strong>bioroid</strong>.", "title": "CFC Excavation Contract", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_arenhanced_security_12115(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "12115", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "Only NBN's sec teams were outfitted with systems that could read data flows and see into the Net.", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Security", "pack_code": "cd", "position": 115, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn the Runner trashes a Corp card, give them 1 tag.", "stripped_title": "AR-Enhanced Security", "text": "The first time each turn the Runner trashes a Corp card, give them 1 tag.", "title": "AR-Enhanced Security", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_brain_rewiring_13029(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "13029", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "The black level clearance sub-sub-basement of Haas-Bioroid is a magical place.", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Security", "pack_code": "td", "position": 29, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may pay X credits. If you do, the Runner adds X cards from the grip at random to the bottom of the stack, then draws 1 card.", "stripped_title": "Brain Rewiring", "text": "When you score this agenda, you may pay X[credit]. If you do, the Runner adds X cards from the grip at random to the bottom of the stack, then draws 1 card.", "title": "Brain Rewiring", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_elective_upgrade_13030(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "13030", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Initiative", "pack_code": "td", "position": 30, "quantity": 3, "side_code": "corp", "stripped_text": "Place 2 agenda counters on Elective Upgrade when you score it. click, hosted agenda counter: Gain click click. Use this ability only once per turn.", "stripped_title": "Elective Upgrade", "text": "Place 2 agenda counters on Elective Upgrade when you score it.\n[click], <strong>hosted agenda counter</strong>: Gain [click][click]. Use this ability only once per turn.", "title": "Elective Upgrade", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_successful_field_test_13031(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "13031", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Clark Huggins", "keywords": "Research", "pack_code": "td", "position": 31, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Successful Field Test, install any number of cards from HQ, ignoring all costs.", "stripped_title": "Successful Field Test", "text": "When you score Successful Field Test, install any number of cards from HQ, ignoring all costs.", "title": "Successful Field Test", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_armored_servers_13042(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "13042", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Ed Mattinian", "keywords": "Security", "pack_code": "td", "position": 42, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: For the remainder of this run, the Runner must trash 1 card from the grip as an additional cost to jack out or break a subroutine. Use this ability only during a run.", "stripped_title": "Armored Servers", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter:</strong> For the remainder of this run, the Runner must trash 1 card from the grip as an additional cost to jack out or break a subroutine. Use this ability only during a run.", "title": "Armored Servers", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_illicit_sales_13043(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "13043", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"Anything, to anyone...for the right price.\"", "illustrator": "Ed Mattinian", "keywords": "Expansion", "pack_code": "td", "position": 43, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Illicit Sales, you may take 1 bad publicity. Gain 3 credits for each bad publicity that you have.", "stripped_title": "Illicit Sales", "text": "When you score Illicit Sales, you may take 1 bad publicity. Gain 3[credit] for each bad publicity that you have.", "title": "Illicit Sales", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_graft_13044(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "13044", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Del Borovic", "pack_code": "td", "position": 44, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Graft, you may search your deck for up to 3 cards, reveal them, and add them to HQ. Shuffle R&D.", "stripped_title": "Graft", "text": "When you score Graft, you may search your deck for up to 3 cards, reveal them, and add them to HQ. Shuffle R&D.", "title": "Graft", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_paper_trail_13053(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "13053", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Liiga Smilshkalne", "keywords": "Security", "pack_code": "td", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Paper Trail, Trace[6]. If successful, trash all connection and job resources.", "stripped_title": "Paper Trail", "text": "When you score Paper Trail, Trace[6]. If successful, trash all <strong>connection</strong> and <strong>job</strong> resources.", "title": "Paper Trail", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_evidence_collection_14000(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "14000", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Dmitry Burmak", "keywords": "Research", "pack_code": "tdc", "position": 1, "quantity": 3, "side_code": "corp", "stripped_text": "When you win a game with Evidence Collection in your score area, reveal set 2.", "stripped_title": "Evidence Collection", "text": "When you win a game with Evidence Collection in your score area, reveal set 2.", "title": "Evidence Collection", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_evidence_collection_2_14001(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "14001", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Dmitry Burmak", "keywords": "Research", "pack_code": "tdc", "position": 2, "quantity": 3, "side_code": "corp", "stripped_text": "When you win a game with Evidence Collection in your score area, reveal set 5.", "stripped_title": "Evidence Collection 2", "text": "When you win a game with Evidence Collection in your score area, reveal set 5.", "title": "Evidence Collection 2", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_evidence_collection_3_14002(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "14002", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Dmitry Burmak", "keywords": "Research", "pack_code": "tdc", "position": 3, "quantity": 3, "side_code": "corp", "stripped_text": "When you win a game with Evidence Collection in your score area, reveal set 8.", "stripped_title": "Evidence Collection 3", "text": "When you win a game with Evidence Collection in your score area, reveal set 8.", "title": "Evidence Collection 3", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_evidence_collection_4_14003(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "14003", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Dmitry Burmak", "keywords": "Research", "pack_code": "tdc", "position": 4, "quantity": 3, "side_code": "corp", "stripped_text": "Evidence Collection is worth 1 fewer agenda point while in the Runner's score area.", "stripped_title": "Evidence Collection 4", "text": "Evidence Collection is worth 1 fewer agenda point while in the Runner's score area.", "title": "Evidence Collection 4", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_corporate_oversight_a_14012(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 0, "code": "14012", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Initiative", "pack_code": "tdc", "position": 13, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Corporate Oversight, you may search R&D for a piece of ice. Install and rez it protecting a remote server, ignoring all costs. Shuffle R&D. If you win a game with Corporate Oversight in your score area, destroy it.", "stripped_title": "Corporate Oversight A", "text": "When you score Corporate Oversight, you may search R&D for a piece of ice. Install and rez it protecting a remote server, ignoring all costs. Shuffle R&D.\nIf you win a game with Corporate Oversight in your score area, destroy it.", "title": "Corporate Oversight A", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_corporate_oversight_b_14013(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 0, "code": "14013", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Initiative", "pack_code": "tdc", "position": 14, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Corporate Oversight, you may search R&D for a piece of ice. Install and rez it protecting a central server, ignoring all costs. Shuffle R&D. If you win a game with Corporate Oversight in your score area, destroy it.", "stripped_title": "Corporate Oversight B", "text": "When you score Corporate Oversight, you may search R&D for a piece of ice. Install and rez it protecting a central server, ignoring all costs. Shuffle R&D.\nIf you win a game with Corporate Oversight in your score area, destroy it.", "title": "Corporate Oversight B", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_ares_20062(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "20062", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Who wants to start a war?", "illustrator": "Emilio Rodriguez", "keywords": "Security", "pack_code": "core2", "position": 62, "quantity": 2, "side_code": "corp", "stripped_text": "When you score this agenda, the Runner trashes 1 of their installed cards for each hosted advancement counter past 4. If the Runner trashes at least 1 card this way, take 1 bad publicity.", "stripped_title": "Project Ares", "text": "When you score this agenda, the Runner trashes 1 of their installed cards for each hosted advancement counter past 4. If the Runner trashes at least 1 card this way, take 1 bad publicity.", "title": "Project Ares", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_vitruvius_20063(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "20063", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "keywords": "Research", "pack_code": "core2", "position": 63, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Add 1 card from Archives to HQ.", "stripped_title": "Project Vitruvius", "text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3.\n<strong>Hosted agenda counter:</strong> Add 1 card from Archives to HQ.", "title": "Project Vitruvius", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_hostile_takeover_20078(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "20078", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "There are going to be some changes around here.", "illustrator": "Antonio De Luca", "keywords": "Expansion", "pack_code": "core2", "position": 109, "quantity": 1, "side_code": "corp", "stripped_text": "When you score this agenda, gain 7 credits and take 1 bad publicity.", "stripped_title": "Hostile Takeover", "text": "When you score this agenda, gain 7[credit] and take 1 bad publicity.", "title": "Hostile Takeover", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_atlas_20079(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "20079", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "keywords": "Research", "pack_code": "core2", "position": 110, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Search R&D for 1 card and reveal it. Add it to HQ.", "stripped_title": "Project Atlas", "text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3.\n<strong>Hosted agenda counter:</strong> Search R&D for 1 card and reveal it. Add it to HQ.", "title": "Project Atlas", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_the_cleaners_20080(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "20080", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"I use bioroids because I can wipe their memories or just blow their brains out when the job is done. No witnesses means no witnesses.\"", "illustrator": "Gong Studios", "keywords": "Security", "pack_code": "core2", "position": 111, "quantity": 1, "side_code": "corp", "stripped_text": "Interrupt -> Whenever you would do meat damage, increase that damage by 1.", "stripped_title": "The Cleaners", "text": "[interrupt] \u2192 Whenever you would do meat damage, increase that damage by 1.", "title": "The Cleaners", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_braintrust_20094(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "20094", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Gong Studios", "keywords": "Research", "pack_code": "core2", "position": 78, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Braintrust, place 1 agenda counter on it for every 2 advancement tokens on it over 3. The rez cost of all ice is lowered by 1 for each agenda counter on Braintrust.", "stripped_title": "Braintrust", "text": "When you score Braintrust, place 1 agenda counter on it for every 2 advancement tokens on it over 3.\nThe rez cost of all ice is lowered by 1 for each agenda counter on Braintrust.", "title": "Braintrust", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_nisei_mk_ii_20095(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "20095", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Alexandra Douglass", "keywords": "Initiative", "pack_code": "core2", "position": 79, "quantity": 2, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: End the run.", "stripped_title": "Nisei MK II", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter:</strong> End the run.", "title": "Nisei MK II", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_beale_20110(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "20110", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Research", "pack_code": "core2", "position": 94, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3. This agenda is worth 1 more agenda point for each hosted agenda counter.", "stripped_title": "Project Beale", "text": "When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3.\nThis agenda is worth 1 more agenda point for each hosted agenda counter.", "title": "Project Beale", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_tgtbt_20111(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "20111", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"The damn raven just kind of cawed at me as I went past. I should have known it was too good to be true.\"", "illustrator": "Adam S. Doyle", "keywords": "Ambush", "pack_code": "core2", "position": 95, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, give them 1 tag.", "stripped_title": "TGTBT", "text": "While the Runner is accessing this agenda in R&D, they must reveal it.\nWhen the Runner accesses this agenda, give them 1 tag.", "title": "TGTBT", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_false_lead_20124(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "20124", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It didn't look like the headquarters of a multi-billion cred company. Probably because it wasn't.", "illustrator": "Bruno Balixa", "keywords": "Security", "pack_code": "core2", "position": 124, "quantity": 1, "side_code": "corp", "stripped_text": "Forfeit this agenda: If the Runner has 2 or more click remaining, they lose click click.", "stripped_title": "False Lead", "text": "<strong>Forfeit this agenda:</strong> If the Runner has 2 or more [click] remaining, they lose [click][click].", "title": "False Lead", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_priority_requisition_20125(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "20125", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"If it isn't in my terminal by six p.m., heads are going to roll!\"", "illustrator": "Dmitry Prosvirnin, Atha Kanaani", "keywords": "Security", "pack_code": "core2", "position": 125, "quantity": 2, "side_code": "corp", "stripped_text": "When you score Priority Requisition, you may rez a piece of ice ignoring all costs.", "stripped_title": "Priority Requisition", "text": "When you score Priority Requisition, you may rez a piece of ice ignoring all costs.", "title": "Priority Requisition", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_private_security_force_20126(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "20126", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Expensive? Not when you're protecting a fortune as large as ours.\"", "illustrator": "Adam Schumpert", "keywords": "Security", "pack_code": "core2", "position": 126, "quantity": 2, "side_code": "corp", "stripped_text": "If the Runner is tagged, Private Security Force gains: \"click: Do 1 meat damage.\"", "stripped_title": "Private Security Force", "text": "If the Runner is tagged, Private Security Force gains: \"[click]: Do 1 meat damage.\"", "title": "Private Security Force", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_ikawah_project_21010(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "21010", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"The average citizen of Nairobi speaks six languages. Every culture, language, ethnicity of the east of Africa collides here, collapses together. What happens slowly by nature can happen quickly in our lab. We will bring peace.\" - Dr. Muchina, Project Lead", "illustrator": "Micha\u0142 Mi\u0142kowski", "keywords": "Security", "pack_code": "ss", "position": 10, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to steal Ikawah Project, the Runner must spend click and 2 credits.", "stripped_title": "Ikawah Project", "text": "As an additional cost to steal Ikawah Project, the Runner must spend [click] and 2[credit].", "title": "Ikawah Project", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_bacterial_programming_21033(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "21033", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Pavel Kolomeyets", "keywords": "Research", "pack_code": "dtwn", "position": 33, "quantity": 3, "side_code": "corp", "stripped_text": "When Bacterial Programming is scored or stolen, you may look at the top 7 cards of R&D, add any number of them to HQ, trash any number of them, and arrange the rest in any order.", "stripped_title": "Bacterial Programming", "text": "When Bacterial Programming is scored or stolen, you may look at the top 7 cards of R&D, add any number of them to HQ, trash any number of them, and arrange the rest in any order.", "title": "Bacterial Programming", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_ssl_endorsement_21038(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "21038", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Caravan Studio", "keywords": "Initiative", "pack_code": "dtwn", "position": 38, "quantity": 3, "side_code": "corp", "stripped_text": "When this agenda is scored or stolen, place 9 credits on it. When the Corp's turn begins, they may take 3 credits from this agenda. This ability is active even while this agenda is in the Runner's score area.", "stripped_title": "SSL Endorsement", "text": "When this agenda is scored or stolen, place 9[credit] on it.\nWhen the Corp's turn begins, they may take 3[credit] from this agenda. This ability is active even while this agenda is in the Runner's score area.", "title": "SSL Endorsement", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_degree_mill_21055(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "21055", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "Master any subject in 30 minutes or less!*\n*Azmari EdTech is not responsible for altered memories or reduced temporal lobe functionality. Level of mastery may vary.", "illustrator": "Juan Novelletto", "keywords": "Initiative", "pack_code": "cotc", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to steal Degree Mill, the Runner must shuffle 2 installed Runner cards into the stack.", "stripped_title": "Degree Mill", "text": "As an additional cost to steal Degree Mill, the Runner must shuffle 2 installed Runner cards into the stack.", "title": "Degree Mill", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_armed_intimidation_21057(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "21057", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"The way I see it, you've got two options: die here or die running. I'll enjoy both.\"", "illustrator": "Le Vuong", "keywords": "Security", "pack_code": "cotc", "position": 57, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Armed Intimidation, the Runner must either suffer 5 meat damage or take 2 tags.", "stripped_title": "Armed Intimidation", "text": "When you score Armed Intimidation, the Runner must either suffer 5 meat damage or take 2 tags.", "title": "Armed Intimidation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_city_works_project_21078(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "21078", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Nasrul Hakim", "keywords": "Public", "pack_code": "tdatd", "position": 78, "quantity": 3, "side_code": "corp", "stripped_text": "Install City Works Project faceup. When the Runner accesses City Works Project while it is installed, do 2 meat damage and 1 additional meat damage for each advancement token on it.", "stripped_title": "City Works Project", "text": "Install City Works Project faceup.\nWhen the Runner accesses City Works Project while it is installed, do 2 meat damage and 1 additional meat damage for each advancement token on it.", "title": "City Works Project", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_remote_enforcement_21091(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "21091", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Nasrul Hakim", "keywords": "Security", "pack_code": "win", "position": 91, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Remote Enforcement, you may search R&D for a piece of ice, install it protecting a remote server (paying its install cost), and rez it, ignoring its rez cost, then shuffle R&D.", "stripped_title": "Remote Enforcement", "text": "When you score Remote Enforcement, you may search R&D for a piece of ice, install it protecting a remote server (paying its install cost), and rez it, ignoring its rez cost, then shuffle R&D.", "title": "Remote Enforcement", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_viral_weaponization_21094(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "21094", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "Quicker and deadlier than ever imagined, the trial was an outstanding success.", "illustrator": "Micha\u0142 Mi\u0142kowski", "keywords": "Research - Security", "pack_code": "win", "position": 94, "quantity": 3, "side_code": "corp", "stripped_text": "When the turn on which you scored Viral Weaponization ends, do 1 net damage for each card in the grip.", "stripped_title": "Viral Weaponization", "text": "When the turn on which you scored Viral Weaponization ends, do 1 net damage for each card in the grip.", "title": "Viral Weaponization", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_better_citizen_program_21116(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "21116", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"Deep down, everyone wants to be good. We ensure that desire is met.\" - Taavi Gyula", "illustrator": "BalanceSheet", "keywords": "Initiative", "pack_code": "ka", "position": 116, "quantity": 3, "side_code": "corp", "stripped_text": "The first time the Runner plays a run event or installs an icebreaker program each turn, you may give the Runner 1 tag.", "stripped_title": "Better Citizen Program", "text": "The first time the Runner plays a <strong>run</strong> event or installs an <strong>icebreaker</strong> program each turn, you may give the Runner 1 tag.", "title": "Better Citizen Program", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_hyperloop_extension_22027(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "22027", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"Our analysis shows significant support from both the public and private sectors.\"", "illustrator": "Angga Satriohadi", "keywords": "Expansion", "pack_code": "rar", "position": 27, "quantity": 3, "side_code": "corp", "stripped_text": "When Hyperloop Extension is scored or stolen, the Corp gains 3 credits.", "stripped_title": "Hyperloop Extension", "text": "When Hyperloop Extension is scored or stolen, the Corp gains 3[credit].", "title": "Hyperloop Extension", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_jumon_22035(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 6, "agenda_points": 2, "code": "22035", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"Jumon, all too Jumon...\"", "illustrator": "Mariusz Siergiejew", "keywords": "Research", "pack_code": "rar", "position": 35, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn ends, place 2 advancement counters on 1 card in the root of a remote server.", "stripped_title": "Jumon", "text": "When your turn ends, place 2 advancement counters on 1 card in the root of a remote server.", "title": "Jumon", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_fly_on_the_wall_22043(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "22043", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "Only half as annoying as the real thing.", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Initiative", "pack_code": "rar", "position": 43, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Fly on the Wall, give the Runner 1 tag.", "stripped_title": "Fly on the Wall", "text": "When you score Fly on the Wall, give the Runner 1 tag.", "title": "Fly on the Wall", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_broad_daylight_22051(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "22051", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Steve Hamilton", "keywords": "Security", "pack_code": "rar", "position": 51, "quantity": 3, "side_code": "corp", "stripped_text": "When you score Broad Daylight, you may take 1 bad publicity. Place 1 agenda counter on Broad Daylight for each bad publicity you have. click, hosted agenda counter: Do 2 meat damage. Use this ability only once per turn.", "stripped_title": "Broad Daylight", "text": "When you score Broad Daylight, you may take 1 bad publicity. Place 1 agenda counter on Broad Daylight for each bad publicity you have.\n[click], <strong>hosted agenda counter</strong>: Do 2 meat damage. Use this ability only once per turn.", "title": "Broad Daylight", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_timely_public_release_23027(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "23027", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "<strong>Designed by 2015 World Champion Dan D'Argenio</strong>", "illustrator": "Matt Zeilinger", "keywords": "Initiative", "pack_code": "mo", "position": 5, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: Install 1 piece of ice from HQ or Archives in any position protecting a server, ignoring all costs.", "stripped_title": "Timely Public Release", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter</strong>: Install 1 piece of ice from HQ or Archives in any position protecting a server, ignoring all costs.", "title": "Timely Public Release", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_vitruvius_25068(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "25068", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "keywords": "Research", "pack_code": "sc19", "position": 68, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Add 1 card from Archives to HQ.", "stripped_title": "Project Vitruvius", "text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3.\n<strong>Hosted agenda counter:</strong> Add 1 card from Archives to HQ.", "title": "Project Vitruvius", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_successful_field_test_25069(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "25069", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Clark Huggins", "keywords": "Research", "pack_code": "sc19", "position": 69, "quantity": 2, "side_code": "corp", "stripped_text": "When you score Successful Field Test, install any number of cards from HQ, ignoring all costs.", "stripped_title": "Successful Field Test", "text": "When you score Successful Field Test, install any number of cards from HQ, ignoring all costs.", "title": "Successful Field Test", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_fetal_ai_25086(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 2, "code": "25086", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Eko Puteh", "keywords": "Ambush", "pack_code": "sc19", "position": 86, "quantity": 2, "side_code": "corp", "stripped_text": "While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda anywhere except in Archives, do 2 net damage. As an additional cost to steal this agenda, the Runner must pay 2 credits.", "stripped_title": "Fetal AI", "text": "While the Runner is accessing this agenda in R&D, they must reveal it.\nWhen the Runner accesses this agenda anywhere except in Archives, do 2 net damage.\nAs an additional cost to steal this agenda, the Runner must pay 2[credit].", "title": "Fetal AI", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_nisei_mk_ii_25087(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "25087", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Alexandra Douglass", "keywords": "Initiative", "pack_code": "sc19", "position": 87, "quantity": 2, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: End the run.", "stripped_title": "Nisei MK II", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter:</strong> End the run.", "title": "Nisei MK II", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_philotic_entanglement_25088(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "25088", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Ed Mattinian", "keywords": "Security", "pack_code": "sc19", "position": 88, "quantity": 1, "side_code": "corp", "stripped_text": "When you score Philotic Entanglement, do 1 net damage for each agenda in the Runner's score area. Limit 1 Philotic Entanglement per deck.", "stripped_title": "Philotic Entanglement", "text": "When you score Philotic Entanglement, do 1 net damage for each agenda in the Runner's score area.\nLimit 1 Philotic Entanglement per deck.", "title": "Philotic Entanglement", "type_code": "agenda", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_explodeapalooza_25106(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "25106", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "It's like Lethal Action 3, only with more explosions.", "illustrator": "Mike Nesbitt", "keywords": "Sensie", "pack_code": "sc19", "position": 106, "quantity": 2, "side_code": "corp", "stripped_text": "While the Runner is accessing this agenda in R&D, they must reveal it. When the Runner accesses this agenda, you may gain 5 credits.", "stripped_title": "Explode-a-palooza", "text": "While the Runner is accessing this agenda in R&D, they must reveal it.\nWhen the Runner accesses this agenda, you may gain 5[credit].", "title": "Explode-a-palooza", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_beale_25107(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "25107", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "illustrator": "Matt Zeilinger", "keywords": "Research", "pack_code": "sc19", "position": 107, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3. This agenda is worth 1 more agenda point for each hosted agenda counter.", "stripped_title": "Project Beale", "text": "When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3.\nThis agenda is worth 1 more agenda point for each hosted agenda counter.", "title": "Project Beale", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_hostile_takeover_25124(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "25124", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "There are going to be some changes around here.", "illustrator": "Antonio De Luca", "keywords": "Expansion", "pack_code": "sc19", "position": 124, "quantity": 2, "side_code": "corp", "stripped_text": "When you score this agenda, gain 7 credits and take 1 bad publicity.", "stripped_title": "Hostile Takeover", "text": "When you score this agenda, gain 7[credit] and take 1 bad publicity.", "title": "Hostile Takeover", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_oaktown_renovation_25125(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "25125", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Maciej Rebisz", "keywords": "Public - Initiative", "pack_code": "sc19", "position": 125, "quantity": 1, "side_code": "corp", "stripped_text": "Install only faceup. (This agenda is neither rezzed nor unrezzed.) Whenever you advance this agenda, gain 2 credits. If there are 5 or more hosted advancement counters (including the counter just placed), gain 3 credits instead.", "stripped_title": "Oaktown Renovation", "text": "Install only faceup. <em>(This agenda is neither rezzed nor unrezzed.)</em>\nWhenever you advance this agenda, gain 2[credit]. If there are 5 or more hosted advancement counters <em>(including the counter just placed)</em>, gain 3[credit] instead.", "title": "Oaktown Renovation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_atlas_25126(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "25126", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "illustrator": "Emilio Rodriguez", "keywords": "Research", "pack_code": "sc19", "position": 126, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Search R&D for 1 card and reveal it. Add it to HQ.", "stripped_title": "Project Atlas", "text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3.\n<strong>Hosted agenda counter:</strong> Search R&D for 1 card and reveal it. Add it to HQ.", "title": "Project Atlas", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_paper_trail_25140(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "25140", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Liiga Smilshkalne", "keywords": "Security", "pack_code": "sc19", "position": 140, "quantity": 2, "side_code": "corp", "stripped_text": "When you score Paper Trail, Trace[6]. If successful, trash all connection and job resources.", "stripped_title": "Paper Trail", "text": "When you score Paper Trail, Trace[6]. If successful, trash all <strong>connection</strong> and <strong>job</strong> resources.", "title": "Paper Trail", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_priority_requisition_25141(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "25141", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"If it isn't in my terminal by six p.m., heads are going to roll!\"", "illustrator": "Dmitry Prosvirnin, Atha Kanaani", "keywords": "Security", "pack_code": "sc19", "position": 141, "quantity": 2, "side_code": "corp", "stripped_text": "When you score Priority Requisition, you may rez a piece of ice ignoring all costs.", "stripped_title": "Priority Requisition", "text": "When you score Priority Requisition, you may rez a piece of ice ignoring all costs.", "title": "Priority Requisition", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_architect_deployment_test_26032(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "26032", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"Early success should be rewarded, as it will encourage a culture of drive and competition.\"\n-Corporate Leadership for Dummies", "illustrator": "Krembler", "keywords": "Research", "pack_code": "df", "position": 32, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, look at the top 5 cards of R&D. You may install and rez 1 of those cards, ignoring all costs.", "stripped_title": "Architect Deployment Test", "text": "When you score this agenda, look at the top 5 cards of R&D. You may install and rez 1 of those cards, ignoring all costs.", "title": "Architect Deployment Test", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_yagiuda_26040(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "26040", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "illustrator": "Krembler", "keywords": "Research", "pack_code": "df", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Swap 1 card from HQ with 1 card in the root of or protecting the attacked server. The Runner may jack out. Use this ability only during a run.", "stripped_title": "Project Yagi-Uda", "text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3.\n<strong>Hosted agenda counter:</strong> Swap 1 card from HQ with 1 card in the root of or protecting the attacked server. The Runner may jack out. Use this ability only during a run.", "title": "Project Yagi-Uda", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_sting_26041(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "26041", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"'It is my nature,' said the scorpion.\"\n-Conceptual Frameworks in Bio-Ethics and Synthetic Morality, Moser University Press", "illustrator": "Krembler", "keywords": "Ambush", "pack_code": "df", "position": 41, "quantity": 3, "side_code": "corp", "stripped_text": "When a player scores or steals this agenda, do X net damage. X is equal to the number of copies of Sting! in the other player's score area plus 1.", "stripped_title": "Sting!", "text": "When a player scores or steals this agenda, do X net damage. X is equal to the number of copies of Sting! in the other player's score area plus 1.", "title": "Sting!", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_remastered_edition_26047(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "26047", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "Scrub-loving devs nerfed cannon rushes cause whiny bronzers complained. Left me four wins down in finals.\nAnyway I won.", "illustrator": "Deivis Goetten", "keywords": "Expansion", "pack_code": "df", "position": 47, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: Place 1 advancement token on an installed card.", "stripped_title": "Remastered Edition", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter:</strong> Place 1 advancement token on an installed card.", "title": "Remastered Edition", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_divested_trust_26055(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "26055", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "As the documents show, for eight months they have operated as an entirely independent fiscal entity. We are as appalled at the carelessness as you are, and fully support City Hall's investigation.", "illustrator": "Krembler", "pack_code": "df", "position": 55, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner steals another agenda, you may forfeit this agenda to gain 5 credits and add the stolen agenda to HQ.", "stripped_title": "Divested Trust", "text": "Whenever the Runner steals another agenda, you may forfeit this agenda to gain 5[credit] and add the stolen agenda to HQ.", "title": "Divested Trust", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_sds_drone_deployment_26056(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "26056", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"Drones are precision instruments. Collateral damage is merely an undisclosed target.\" -Chief \"Pinchy\" Wilson", "illustrator": "Olie Boldador", "keywords": "Security", "pack_code": "df", "position": 56, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to steal this agenda, the Runner must trash an installed program. When you score this agenda, trash an installed program.", "stripped_title": "SDS Drone Deployment", "text": "As an additional cost to steal this agenda, the Runner must trash an installed program.\nWhen you score this agenda, trash an installed program.", "title": "SDS Drone Deployment", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_vulnerability_audit_26063(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 3, "code": "26063", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 1, "flavor": "The Fracture was no different from any other crisis. As always, Management's first instinct was to find someone to blame. Getting food up to Midway or He3 down to power Earthside hospitals are trivialities compared to the important work of salving Executive ego and keeping one's job.", "illustrator": "Iain Fairclough", "keywords": "Research", "pack_code": "df", "position": 63, "quantity": 3, "side_code": "corp", "stripped_text": "You cannot score this agenda if you installed it this turn.", "stripped_title": "Vulnerability Audit", "text": "You cannot score this agenda if you installed it this turn.", "title": "Vulnerability Audit", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_megaprix_qualifier_26096(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "26096", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"Win Hard or Lose Hard. All that matters is they're talking about you and not the competition.\"\n-Tan \"Nitro\" Nyugen, Toretto-Extreme Team Manager", "illustrator": "Krembler", "pack_code": "ur", "position": 96, "quantity": 3, "side_code": "corp", "stripped_text": "If there is another copy of Megaprix Qualifier in either player's score area when you score this agenda, place 1 agenda counter on this agenda. This agenda is worth 1 more agenda point while it has a hosted agenda counter.", "stripped_title": "Megaprix Qualifier", "text": "If there is another copy of Megaprix Qualifier in either player's score area when you score this agenda, place 1 agenda counter on this agenda.\nThis agenda is worth 1 more agenda point while it has a hosted agenda counter.", "title": "Megaprix Qualifier", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_vacheron_26097(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "26097", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "illustrator": "Patrick Burk", "keywords": "Research", "pack_code": "ur", "position": 97, "quantity": 3, "side_code": "corp", "stripped_text": "Interrupt -> When this agenda would be added to the Runner's score area from anywhere except Archives, instead it is added to their score area with 4 hosted agenda counters. While this agenda is in the Runner's score area with 1 or more hosted agenda counters, it is worth 0 agenda points and gains \"When the Runner's turn begins, remove 1 hosted agenda counter.\"", "stripped_title": "Project Vacheron", "text": "[interrupt] \u2192 When this agenda would be added to the Runner's score area from anywhere except Archives, instead it is added to their score area with 4 hosted agenda counters.\nWhile this agenda is in the Runner's score area with 1 or more hosted agenda counters, it is worth 0 agenda points and gains \"When the Runner's turn begins, remove 1 hosted agenda counter.\"", "title": "Project Vacheron", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_flower_sermon_26106(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "26106", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"Voice is a sledgehammer. Text, a blunt saw. Truth requires subtler instruments.\"\n-Dr. Tang, Address to the Hyoubu Steering Committee", "illustrator": "N. Hopkins", "pack_code": "ur", "position": 106, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 5 agenda counters on it. Hosted agenda counter: Reveal the top card of R&D. Draw 2 cards. Add 1 card from HQ to the top of R&D. Use this ability only once per turn.", "stripped_title": "Flower Sermon", "text": "When you score this agenda, place 5 agenda counters on it.\n<strong>Hosted agenda counter:</strong> Reveal the top card of R&D. Draw 2 cards. Add 1 card from HQ to the top of R&D. Use this ability only once per turn.", "title": "Flower Sermon", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_bellona_26114(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "26114", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "Mars' tiny population made rich multiplayer experiences a big challenge. We cracked it by live-beaming the gestalt of our <em>Earth</em> playerbase second-by-second. Bellona weaves these \"lag-ghosts\" into compelling interactables\u2014more responsive than the real thing!", "illustrator": "N. Hopkins, Iain Fairclough", "keywords": "Expansion", "pack_code": "ur", "position": 114, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to steal this agenda, the Runner must pay 5 credits. When you score this agenda, gain 5 credits.", "stripped_title": "Bellona", "text": "As an additional cost to steal this agenda, the Runner must pay 5[credit].\nWhen you score this agenda, gain 5[credit].", "title": "Bellona", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_transport_monopoly_26121(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "26121", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Once you're on the Space Elevator Authority's blacklist, you aren't going anywhere.", "illustrator": "Zoe Cohen", "keywords": "Initiative", "pack_code": "ur", "position": 121, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 2 agenda counters on it. Hosted agenda counter: This run cannot be declared successful. (This effect does not cause the run to become unsuccessful.) Use this ability only once per turn.", "stripped_title": "Transport Monopoly", "text": "When you score this agenda, place 2 agenda counters on it.\n<strong>Hosted agenda counter:</strong> This run cannot be declared successful. <em>(This effect does not cause the run to become unsuccessful.)</em> Use this ability only once per turn.", "title": "Transport Monopoly", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_cyberdex_sandbox_26128(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "26128", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"All <em><strong>Dragon</strong></em>-rated threats should only be stored in a single clean-start air-gapped server, in a shielded room, under at least 200 metres of bedrock[...]\"\n-Section 5.18.4, Cyberdex Employee Handbook", "illustrator": "Krembler", "keywords": "Security", "pack_code": "ur", "position": 128, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn you purge virus counters, gain 4 credits. When you score this agenda, you may purge virus counters.", "stripped_title": "Cyberdex Sandbox", "text": "The first time each turn you purge virus counters, gain 4[credit].\nWhen you score this agenda, you may purge virus counters.", "title": "Cyberdex Sandbox", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_false_lead_26129(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "26129", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"Begin a voice message to Steve: I'm in some random city staring at yet another empty room. This hot insider scoop of yours feels distinctly chilly.\"", "illustrator": "NtscapeNavigator", "keywords": "Security", "pack_code": "ur", "position": 129, "quantity": 3, "side_code": "corp", "stripped_text": "Forfeit this agenda: If the Runner has 2 or more click remaining, they lose click click.", "stripped_title": "False Lead", "text": "<strong>Forfeit this agenda:</strong> If the Runner has 2 or more [click] remaining, they lose [click][click].", "title": "False Lead", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_megaprix_qualifier_27004(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "27004", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"Win Hard or Lose Hard. All that matters is they're talking about you and not the competition.\"\n- Tan \"Nitro\" Nyugen, Toretto-Extreme Team Manager", "illustrator": "Krembler", "pack_code": "urbp", "position": 4, "quantity": 3, "side_code": "corp", "stripped_text": "If there is another copy of Megaprix Qualifier in either player's score area when you score this agenda, place 1 agenda counter on this agenda. This agenda is worth 1 more agenda point while it has a hosted agenda counter.", "stripped_title": "Megaprix Qualifier", "text": "If there is another copy of Megaprix Qualifier in either player's score area when you score this agenda, place 1 agenda counter on this agenda.\nThis agenda is worth 1 more agenda point while it has a hosted agenda counter.", "title": "Megaprix Qualifier", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_timely_public_release_28006(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "28006", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "<strong>Designed by 2015 World Champion Dan D'Argenio</strong>", "illustrator": "NtscapeNavigator", "keywords": "Initiative", "pack_code": "mor", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: Install 1 piece of ice from HQ or Archives in any position protecting a server, ignoring all costs.", "stripped_title": "Timely Public Release", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter</strong>: Install 1 piece of ice from HQ or Archives in any position protecting a server, ignoring all costs.", "title": "Timely Public Release", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_luminal_transubstantiation_30036(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "30036", "deck_limit": 1, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "We are the light of tomorrow.", "illustrator": "Zoe Cohen", "keywords": "Research", "pack_code": "sg", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, gain click click click. You cannot score agendas for the remainder of the turn. Limit 1 per deck.", "stripped_title": "Luminal Transubstantiation", "text": "When you score this agenda, gain [click][click][click]. You cannot score agendas for the remainder of the turn.\nLimit 1 per deck.", "title": "Luminal Transubstantiation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_longevity_serum_30044(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "30044", "deck_limit": 1, "faction_code": "jinteki", "faction_cost": 0, "flavor": "We make you anew.", "illustrator": "N. Hopkins", "keywords": "Research", "pack_code": "sg", "position": 44, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, trash any number of cards from HQ. Shuffle up to 3 cards from Archives into R&D. Limit 1 per deck.", "stripped_title": "Longevity Serum", "text": "When you score this agenda, trash any number of cards from HQ. Shuffle up to 3 cards from Archives into R&D.\nLimit 1 per deck.", "title": "Longevity Serum", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_tomorrows_headline_30052(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "30052", "deck_limit": 1, "faction_code": "nbn", "faction_cost": 0, "flavor": "We don't find news. We make it.", "illustrator": "NtscapeNavigator", "keywords": "Ambush", "pack_code": "sg", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "When this agenda is scored or stolen, give the Runner 1 tag. Limit 1 per deck.", "stripped_title": "Tomorrow's Headline", "text": "When this agenda is scored or stolen, give the Runner 1 tag.\nLimit 1 per deck.", "title": "Tomorrow's Headline", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_above_the_law_30060(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "30060", "deck_limit": 1, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "We are judge, jury, and executioner.", "illustrator": "Seojun Park", "keywords": "Security", "pack_code": "sg", "position": 60, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may trash 1 installed resource. Limit 1 per deck.", "stripped_title": "Above the Law", "text": "When you score this agenda, you may trash 1 installed resource.\nLimit 1 per deck.", "title": "Above the Law", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_offworld_office_30067(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "30067", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "As the first lunar city, Heinlein was built on the dreams of a new frontier and boundless opportunity, but He3 mining is too lucrative for the corps to ever relinquish control.", "illustrator": "Benjamin Giletti", "keywords": "Expansion", "pack_code": "sg", "position": 67, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, gain 7 credits.", "stripped_title": "Offworld Office", "text": "When you score this agenda, gain 7[credit].", "title": "Offworld Office", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_orbital_superiority_30068(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "30068", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Mobsters bribe police, megacorps acquire militaries.", "illustrator": "Krembler", "keywords": "Security", "pack_code": "sg", "position": 68, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, if the Runner is tagged, do 4 meat damage; otherwise, give the Runner 1 tag.", "stripped_title": "Orbital Superiority", "text": "When you score this agenda, if the Runner is tagged, do 4 meat damage; otherwise, give the Runner 1 tag.", "title": "Orbital Superiority", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_send_a_message_30069(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 5, "agenda_points": 3, "code": "30069", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "It might be over, but we <strong>will</strong> get them next time.", "illustrator": "David Lei", "keywords": "Security", "pack_code": "sg", "position": 69, "quantity": 3, "side_code": "corp", "stripped_text": "When this agenda is scored or stolen, you may rez 1 installed piece of ice, ignoring all costs.", "stripped_title": "Send a Message", "text": "When this agenda is scored or stolen, you may rez 1 installed piece of ice, ignoring all costs.", "title": "Send a Message", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_superconducting_hub_30070(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "30070", "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "With Earth-Luna communications, saving microseconds returns megacredits.", "illustrator": "Scott Uminga", "keywords": "Expansion", "pack_code": "sg", "position": 70, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may draw 2 cards. You get +2 maximum hand size.", "stripped_title": "Superconducting Hub", "text": "When you score this agenda, you may draw 2 cards.\nYou get +2 maximum hand size.", "title": "Superconducting Hub", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_vitruvius_31041(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "31041", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Perfection of form.", "illustrator": "Krembler", "keywords": "Research", "pack_code": "su21", "position": 41, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Add 1 card from Archives to HQ.", "stripped_title": "Project Vitruvius", "text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3.\n<strong>Hosted agenda counter:</strong> Add 1 card from Archives to HQ.", "title": "Project Vitruvius", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_house_of_knives_31051(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "31051", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "The payment for entry is a mere drop of blood.", "illustrator": "Zoe Cohen", "keywords": "Security", "pack_code": "su21", "position": 51, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 3 agenda counters on it. Hosted agenda counter: Do 1 net damage. Use this ability only during a run and only once per run.", "stripped_title": "House of Knives", "text": "When you score this agenda, place 3 agenda counters on it.\n<strong>Hosted agenda counter:</strong> Do 1 net damage. Use this ability only during a run and only once per run.", "title": "House of Knives", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_nisei_mk_ii_31052(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "31052", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "We could stop disasters before they happen, murderers before they act. Surely that's worth an android's sanity?", "illustrator": "Dimik", "keywords": "Initiative", "pack_code": "su21", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it. Hosted agenda counter: End the run.", "stripped_title": "Nisei MK II", "text": "When you score this agenda, place 1 agenda counter on it.\n<strong>Hosted agenda counter:</strong> End the run.", "title": "Nisei MK II", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_license_acquisition_31061(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "31061", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "Alright everyone! The rights go live in exactly fourteen days. I want merch, I want tie-ins, I want sequels! Let's go!", "illustrator": "Zoe Cohen", "keywords": "Expansion", "pack_code": "su21", "position": 61, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may reveal 1 asset or upgrade in HQ or Archives. Install and rez that card, ignoring all costs.", "stripped_title": "License Acquisition", "text": "When you score this agenda, you may reveal 1 asset or upgrade in HQ or Archives. Install and rez that card, ignoring all costs.", "title": "License Acquisition", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_beale_31062(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "31062", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "Everything is data.", "illustrator": "Zoe Cohen", "keywords": "Research", "pack_code": "su21", "position": 62, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3. This agenda is worth 1 more agenda point for each hosted agenda counter.", "stripped_title": "Project Beale", "text": "When you score this agenda, place 1 agenda counter on it for every 2 hosted advancement counters past 3.\nThis agenda is worth 1 more agenda point for each hosted agenda counter.", "title": "Project Beale", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_hostile_takeover_31071(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "31071", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Sometimes the small fry need a little convincing to put profit over principle.", "illustrator": "NtscapeNavigator, Matt Burton", "keywords": "Expansion", "pack_code": "su21", "position": 71, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, gain 7 credits and take 1 bad publicity.", "stripped_title": "Hostile Takeover", "text": "When you score this agenda, gain 7[credit] and take 1 bad publicity.", "title": "Hostile Takeover", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_oaktown_renovation_31072(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "31072", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "There's only one season in Oaktown: construction.", "illustrator": "Kira L. Nguyen", "keywords": "Public - Initiative", "pack_code": "su21", "position": 72, "quantity": 3, "side_code": "corp", "stripped_text": "Install only faceup. (This agenda is neither rezzed nor unrezzed.) Whenever you advance this agenda, gain 2 credits. If there are 5 or more hosted advancement counters (including the counter just placed), gain 3 credits instead.", "stripped_title": "Oaktown Renovation", "text": "Install only faceup. <em>(This agenda is neither rezzed nor unrezzed.)</em>\nWhenever you advance this agenda, gain 2[credit]. If there are 5 or more hosted advancement counters <em>(including the counter just placed)</em>, gain 3[credit] instead.", "title": "Oaktown Renovation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_project_atlas_31073(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "31073", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Next stop: infinity.", "illustrator": "Zoe Cohen", "keywords": "Research", "pack_code": "su21", "position": 73, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3. Hosted agenda counter: Search R&D for 1 card and reveal it. Add it to HQ.", "stripped_title": "Project Atlas", "text": "When you score this agenda, place 1 agenda counter on it for each hosted advancement counter past 3.\n<strong>Hosted agenda counter:</strong> Search R&D for 1 card and reveal it. Add it to HQ.", "title": "Project Atlas", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_azef_protocol_32007(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "32007", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "Argus Security is always willing to send agents over to assist with radical asset reassignment.", "illustrator": "Benjamin Giletti", "keywords": "Security", "pack_code": "msbp", "position": 7, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to score this agenda, trash 1 of your other installed cards. When you score this agenda, do 2 meat damage.", "stripped_title": "Azef Protocol", "text": "As an additional cost to score this agenda, trash 1 of your other installed cards.\nWhen you score this agenda, do 2 meat damage.", "title": "Azef Protocol", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_elivagar_bifurcation_33031(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "33031", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Ancient paradoxes are children's stories to the greatest minds ever designed.", "illustrator": "Scott Uminga", "keywords": "Security", "pack_code": "ms", "position": 31, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may derez 1 installed card.", "stripped_title": "Elivagar Bifurcation", "text": "When you score this agenda, you may derez 1 installed card.", "title": "\u00c9liv\u00e1gar Bifurcation", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_midnight3_arcology_33032(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "33032", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "\"The Midnight-3 glows with an inviting warmth that belies the broken promise within. All that awaits you there is a life of indentured servitude.\"\n\u2013Sundog", "illustrator": "Emilio Rodriguez", "keywords": "Expansion", "pack_code": "ms", "position": 32, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, draw 3 cards. Skip your discard step this turn.", "stripped_title": "Midnight-3 Arcology", "text": "When you score this agenda, draw 3 cards. Skip your discard step this turn.", "title": "Midnight-3 Arcology", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_blood_in_the_water_33039(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": null, "agenda_points": 2, "code": "33039", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "Some tests require <strong>specific</strong> conditions.", "illustrator": "Scott Uminga", "keywords": "Research", "pack_code": "ms", "position": 39, "quantity": 3, "side_code": "corp", "stripped_text": "X is equal to the number of cards in the Runner's grip.", "stripped_title": "Blood in the Water", "text": "X is equal to the number of cards in the Runner's grip.", "title": "Blood in the Water", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_regenesis_33040(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 1, "code": "33040", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"Esteemed guests, by the end of this demonstration you will see that extinction is now only a temporary state of affairs.\"\n\u2013Vientiane Keeling", "illustrator": "Anthony Hutchings", "keywords": "Research", "pack_code": "ms", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, if no Corp cards have been added to Archives this turn, you may reveal 1 facedown agenda in Archives and add it to your score area.", "stripped_title": "Regenesis", "text": "When you score this agenda, if no Corp cards have been added to Archives this turn, you may reveal 1 facedown agenda in Archives and add it to your score area.", "title": "Regenesis", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_artificial_cryptocrash_33049(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "33049", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "The line goes up... until we don't need it to anymore.", "illustrator": "Wyn Lacabra", "keywords": "Initiative", "pack_code": "ms", "position": 49, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, the Runner loses 7 credits.", "stripped_title": "Artificial Cryptocrash", "text": "When you score this agenda, the Runner loses 7[credit].", "title": "Artificial Cryptocrash", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_azef_protocol_33058(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 3, "agenda_points": 2, "code": "33058", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"Don't worry, directors, security is always willing to send agents to assist with radical asset reassignment.\"\n\u2013Yakov Avdakov", "illustrator": "Benjamin Giletti", "keywords": "Security", "pack_code": "ms", "position": 58, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to score this agenda, trash 1 of your other installed cards. When you score this agenda, do 2 meat damage.", "stripped_title": "Azef Protocol", "text": "As an additional cost to score this agenda, trash 1 of your other installed cards.\nWhen you score this agenda, do 2 meat damage.", "title": "Azef Protocol", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_ontological_dependence_33096(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "33096", "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 0, "flavor": "Bend the minds of those below you such that they will always need you, and loyalty is assured forever.", "illustrator": "Oliver Morit", "keywords": "Research", "pack_code": "ph", "position": 96, "quantity": 3, "side_code": "corp", "stripped_text": "This agenda gets -1 advancement requirement for each core damage the Runner has taken this game.", "stripped_title": "Ontological Dependence", "text": "This agenda gets -1 advancement requirement for each core damage the Runner has taken this game.", "title": "Ontological Dependence", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_hybrid_release_33105(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "33105", "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 0, "flavor": "\"By disabling their bodies\u02bc ability to create a variety of necessary enzymes, we\u02bcve ensured their loyalty to us. If they don\u02bct return for supplements every month, they die; simple as that.\"\n\u2014Dr. Vientiane Keeling", "illustrator": "Marlon Ruiz", "keywords": "Expansion", "pack_code": "ph", "position": 105, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may install 1 facedown card from Archives.", "stripped_title": "Hybrid Release", "text": "When you score this agenda, you may install 1 facedown card from Archives.", "title": "Hybrid Release", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_freedom_of_information_33112(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "33112", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"An FOI request? No problem! Please fill out all details. You\u02bcd like to make an anonymous request? I\u02bcm sorry: absolutely not.\"", "illustrator": "Zefanya Langkan Maega", "keywords": "Research", "pack_code": "ph", "position": 112, "quantity": 3, "side_code": "corp", "stripped_text": "This agenda gets -1 advancement requirement for each tag the Runner has.", "stripped_title": "Freedom of Information", "text": "This agenda gets -1 advancement requirement for each tag the Runner has.", "title": "Freedom of Information", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_posttruth_dividend_33113(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 2, "agenda_points": 1, "code": "33113", "deck_limit": 3, "faction_code": "nbn", "faction_cost": 0, "flavor": "\"Hey kiddo, remember what Daddy says about lying?\"\n\"\u02bcOnly when you can get away with it!\u02bc\"", "illustrator": "Wyn Lacabra", "keywords": "Initiative", "pack_code": "ph", "position": 113, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may draw 1 card.", "stripped_title": "Post-Truth Dividend", "text": "When you score this agenda, you may draw 1 card.", "title": "Post-Truth Dividend", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_regulatory_capture_33120(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 6, "agenda_points": 2, "code": "33120", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "This was a criminal offense. Now it\u02bcs an option for business.", "illustrator": "Wyn Lacabra", "keywords": "Research", "pack_code": "ph", "position": 120, "quantity": 3, "side_code": "corp", "stripped_text": "For each bad publicity you have up to 4, this agenda gets -1 advancement requirement.", "stripped_title": "Regulatory Capture", "text": "For each bad publicity you have up to 4, this agenda gets -1 advancement requirement.", "title": "Regulatory Capture", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class agenda_kimberlite_field_33121(Agenda):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"advancement_cost": 4, "agenda_points": 2, "code": "33121", "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 0, "flavor": "\"Weyland\u02bcs synthetic diamonds cost less than naturals... so what are they really digging for here?\"\n\u2014Captain Padma Isbister", "illustrator": "Vitalii Ostaschenko", "keywords": "Expansion", "pack_code": "ph", "position": 121, "quantity": 3, "side_code": "corp", "stripped_text": "When you score this agenda, you may trash 1 of your rezzed cards. If you do, trash 1 installed Runner card with a printed install cost equal to or less than the printed rez cost of the Corp card you trashed.", "stripped_title": "Kimberlite Field", "text": "When you score this agenda, you may trash 1 of your rezzed cards. If you do, trash 1 installed Runner card with a printed install cost equal to or less than the printed rez cost of the Corp card you trashed.", "title": "Kimberlite Field", "type_code": "agenda", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                