
'''
card classes of type upgrade
'''
from netrunner_lib.cards._base_card_classes import Upgrade

            
class upgrade_corporate_troubleshooter_01065(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01065", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "\"I solve problems.\"", "illustrator": "Ed Mattinian", "pack_code": "core", "position": 65, "quantity": 1, "side_code": "corp", "stripped_text": "X credits, trash: Choose 1 rezzed piece of ice protecting this server. That ice gets +X strength for the remainder of the turn.", "stripped_title": "Corporate Troubleshooter", "text": "<strong>X[credit]</strong>, [trash]<strong>:</strong> Choose 1 rezzed piece of ice protecting this server. That ice gets +X strength for the remainder of the turn.", "title": "Corporate Troubleshooter", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_experiential_data_01066(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01066", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Floyd felt the anger in the man before him, ranting against simulants. His programming pushed a routine rebuttal to the front of his thoughts, and the urge to speak it was overwhelming. This is only going to make things worse, he thought.", "illustrator": "Mauricio Herrera", "pack_code": "core", "position": 66, "quantity": 2, "side_code": "corp", "stripped_text": "All ice protecting this server has +1 strength.", "stripped_title": "Experiential Data", "text": "All ice protecting this server has +1 strength.", "title": "Experiential Data", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_akitaro_watanabe_01079(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01079", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Just don't ask how he does it.", "illustrator": "Mike Nesbitt", "keywords": "Sysop - Unorthodox", "pack_code": "core", "position": 79, "quantity": 1, "side_code": "corp", "stripped_text": "The rez cost of ice protecting this server is lowered by 2.", "stripped_title": "Akitaro Watanabe", "text": "The rez cost of ice protecting this server is lowered by 2.", "title": "Akitaro Watanabe", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_red_herrings_01091(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01091", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Mike Nesbitt", "pack_code": "core", "position": 91, "quantity": 2, "side_code": "corp", "stripped_text": "Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must pay 5 credits. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)", "stripped_title": "Red Herrings", "text": "Persistent \u2192 As an additional cost to steal an agenda from this server or its root, the Runner must pay 5[credit]. <em>(If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)</em>", "title": "Red Herrings", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_sansan_city_grid_01092(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01092", "cost": 6, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"I hear the coast is nice this time of year.\"\n\"If you're in the right business, it's nice all the year.\"", "illustrator": "Ed Mattinian", "keywords": "Region", "pack_code": "core", "position": 92, "quantity": 1, "side_code": "corp", "stripped_text": "Each agenda in the root of this server gets -1 advancement requirement. Limit 1 region per server.", "stripped_title": "SanSan City Grid", "text": "Each agenda in the root of this server gets -1 advancement requirement.\nLimit 1 <strong>region</strong> per server.", "title": "SanSan City Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_research_station_01105(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01105", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "\"Jack Weyland built the Beanstalk and transformed the human race forever. I can't wait to see what we're going to do next.\"", "illustrator": "Ralph Beisner", "keywords": "Facility", "pack_code": "core", "position": 105, "quantity": 2, "side_code": "corp", "stripped_text": "Install only in the root of HQ. Your maximum hand size is +2.", "stripped_title": "Research Station", "text": "Install only in the root of HQ.\nYour maximum hand size is +2.", "title": "Research Station", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_ash_2x3zb9cy_02013(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02013", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Eyes forward, please.\"", "illustrator": "Mauricio Herrera", "keywords": "Bioroid", "pack_code": "wla", "position": 13, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever there is a successful run on this server, Trace[4]. If successful, the Runner cannot access any cards other than Ash 2X3ZB9CY for the remainder of this run.", "stripped_title": "Ash 2X3ZB9CY", "text": "Whenever there is a successful run on this server, Trace[4]. If successful, the Runner cannot access any cards other than Ash 2X3ZB9CY for the remainder of this run.", "title": "Ash 2X3ZB9CY", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_chilo_city_grid_02036(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02036", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Clones whisper of ChiLo as a promised land of freedom.", "illustrator": "Jonathan Lee", "keywords": "Region", "pack_code": "ta", "position": 36, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever there is a successful trace during a run on this server, give the Runner 1 tag. Limit 1 region per server.", "stripped_title": "ChiLo City Grid", "text": "Whenever there is a successful trace during a run on this server, give the Runner 1 tag.\nLimit 1 <strong>region</strong> per server.", "title": "ChiLo City Grid", "trash_cost": 6, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_amazon_industrial_zone_02038(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02038", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "illustrator": "Jon Hrubesch", "keywords": "Region", "pack_code": "ta", "position": 38, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you install a piece of ice protecting this server, you may immediately rez it, lowering its rez cost by 3. Limit 1 region per server.", "stripped_title": "Amazon Industrial Zone", "text": "Whenever you install a piece of ice protecting this server, you may immediately rez it, lowering its rez cost by 3.\nLimit 1 <strong>region</strong> per server.", "title": "Amazon Industrial Zone", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_hokusai_grid_02095(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02095", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Despite its appearance, the Hokusai Grid is the most notorious research facility at Jinteki.", "illustrator": "Emilio Rodriguez", "keywords": "Region", "pack_code": "hs", "position": 95, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner makes a successful run on this server, do 1 net damage. Limit 1 region per server.", "stripped_title": "Hokusai Grid", "text": "Whenever the Runner makes a successful run on this server, do 1 net damage.\nLimit 1 <strong>region</strong> per server.", "title": "Hokusai Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_bernice_mai_02097(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02097", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Keeping tabs on the world, one screen at a time.", "illustrator": "Erfan Fajar", "keywords": "Sysop", "pack_code": "hs", "position": 97, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever there is a successful run on this server, Trace[5]. If successful, give the Runner 1 tag. If unsuccessful, trash Bernice Mai.", "stripped_title": "Bernice Mai", "text": "Whenever there is a successful run on this server, Trace[5]. If successful, give the Runner 1 tag. If unsuccessful, trash Bernice Mai.", "title": "Bernice Mai", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_simone_diego_02099(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02099", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "\"A job done once is a job done right.\"", "illustrator": "Matt Zeilinger", "keywords": "Sysop", "pack_code": "hs", "position": 99, "quantity": 3, "side_code": "corp", "stripped_text": "2 recurring credits You can spend hosted credits to take the basic action to advance cards in the root of or protecting this server.", "stripped_title": "Simone Diego", "text": "2[recurring-credit]\nYou can spend hosted credits to take the basic action to advance cards in the root of or protecting this server.", "title": "Simone Diego", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_ruhr_valley_02111(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02111", "cost": 6, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "Known for luxury hoppers and a delectable sauerkraut.", "illustrator": "Yoann Boissonnet", "keywords": "Region", "pack_code": "fp", "position": 111, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to make a run on this server, the Runner must spend click. Limit 1 region per server.", "stripped_title": "Ruhr Valley", "text": "As an additional cost to make a run on this server, the Runner must spend [click].\nLimit 1 <strong>region</strong> per server.", "title": "Ruhr Valley", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_midori_02113(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02113", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "\"Looks like someone is being naughty\u2026\"", "illustrator": "RJ Palmer", "keywords": "Sysop", "pack_code": "fp", "position": 113, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner approaches a piece of ice protecting this server, you may swap that ice with 1 piece of ice from HQ. (The new ice is installed unrezzed.) If you do, the Runner may jack out. Use this ability only once per run.", "stripped_title": "Midori", "text": "Whenever the Runner approaches a piece of ice protecting this server, you may swap that ice with 1 piece of ice from HQ. <em>(The new ice is installed unrezzed.)</em> If you do, the Runner may jack out. Use this ability only once per run.", "title": "Midori", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_awakening_center_03021(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03021", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "illustrator": "Diana Martinez", "pack_code": "cac", "position": 21, "quantity": 3, "side_code": "corp", "stripped_text": "Awakening Center can host bioroid ice (each piece is installed facedown, ignoring all install costs). Whenever the Runner passes all of the ice protecting this server, you may rez a piece of ice on Awakening Center, lowering the rez cost by 7 credits, to force the Runner to encounter it. Trash that ice after the run is completed.", "stripped_title": "Awakening Center", "text": "Awakening Center can host <strong>bioroid</strong> ice (each piece is installed facedown, ignoring all install costs).\nWhenever the Runner passes all of the ice protecting this server, you may rez a piece of ice on Awakening Center, lowering the rez cost by 7[credit], to force the Runner to encounter it. Trash that ice after the run is completed.", "title": "Awakening Center", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_tyrs_hand_03022(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03022", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "illustrator": "John Derek Murphy", "keywords": "Hostile", "pack_code": "cac", "position": 22, "quantity": 3, "side_code": "corp", "stripped_text": "Interrupt -> When a subroutine would be broken on a piece of bioroid ice protecting this server, you may rez this upgrade. Interrupt -> trash: Prevent 1 subroutine from being broken on a piece of bioroid ice protecting this server.", "stripped_title": "Tyr's Hand", "text": "[interrupt] \u2192 When a subroutine would be broken on a piece of <strong>bioroid</strong> ice protecting this server, you may rez this upgrade.\n[interrupt] \u2192 <strong>[trash]:</strong> Prevent 1 subroutine from being broken on a piece of <strong>bioroid</strong> ice protecting this server.", "title": "Tyr's Hand", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_off_the_grid_04038(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04038", "cost": 6, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Zefanya Langkan Maega", "pack_code": "st", "position": 38, "quantity": 3, "side_code": "corp", "stripped_text": "Install only in a remote server. The Runner cannot initiate a run on this server. Whenever the Runner makes a successful run on HQ, trash Off the Grid.", "stripped_title": "Off the Grid", "text": "Install only in a remote server.\nThe Runner cannot initiate a run on this server.\nWhenever the Runner makes a successful run on HQ, trash Off the Grid.", "title": "Off the Grid", "trash_cost": 0, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_panic_button_04072(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04072", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "The button didn't seem to do anything. So he pushed it again. And again. And again.", "illustrator": "Gong Studios", "pack_code": "tc", "position": 72, "quantity": 3, "side_code": "corp", "stripped_text": "Install only in the root of HQ. 1 credit: Draw 1 card. Use this ability only during a run on HQ.", "stripped_title": "Panic Button", "text": "Install only in the root of HQ.\n1[credit]: Draw 1 card. Use this ability only during a run on HQ.", "title": "Panic Button", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_strongbox_04091(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04091", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Andreas Zafiratos", "pack_code": "fal", "position": 91, "quantity": 3, "side_code": "corp", "stripped_text": "Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must spend click. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)", "stripped_title": "Strongbox", "text": "Persistent \u2192 As an additional cost to steal an agenda from this server or its root, the Runner must spend [click]. <em>(If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)</em>", "title": "Strongbox", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_caprice_nisei_04114(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04114", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "The first clone to serve as an NAPD detective.", "illustrator": "Matt Zeilinger", "keywords": "Clone - Psi", "pack_code": "dt", "position": 114, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner passes all of the ice protecting this server, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, end the run.", "stripped_title": "Caprice Nisei", "text": "Whenever the Runner passes all of the ice protecting this server, you and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, end the run.", "title": "Caprice Nisei", "trash_cost": 1, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_neotokyo_grid_05021(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05021", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "It is difficult to go to Japan without ending up in the sprawl of NeoTokyo.", "illustrator": "Emilio Rodriguez", "keywords": "Region", "pack_code": "hap", "position": 21, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each turn an advancement counter is placed on a card in the root of this server, gain 1 credit. Limit 1 region per server.", "stripped_title": "NeoTokyo Grid", "text": "The first time each turn an advancement counter is placed on a card in the root of this server, gain 1[credit].\nLimit 1 <strong>region</strong> per server.", "title": "NeoTokyo Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_tori_hanzo_05022(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05022", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "Known as the Red Woman, Hanz\u014d is notorious for her ruthless methods of server protection.", "illustrator": "Smirtouille", "keywords": "Sysop", "pack_code": "hap", "position": 22, "quantity": 3, "side_code": "corp", "stripped_text": "Interrupt -> The first time you would do 1 or more net damage during each run against this server, instead you may pay 2 credits to do 1 core damage.", "stripped_title": "Tori Hanzo", "text": "[interrupt] \u2192 The first time you would do 1 or more net damage during each run against this server, instead you may pay 2[credit] to do 1 core damage.", "title": "Tori Hanz\u014d", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_midway_station_grid_06007(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06007", "cost": 4, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "flavor": "Halfway upstalk, Midway is a destination unto itself with its microgravity hotels and fine dining options.", "illustrator": "Emilio Rodriguez", "keywords": "Beanstalk - Region", "pack_code": "up", "position": 7, "quantity": 3, "side_code": "corp", "stripped_text": "During runs on this server, the Runner must pay 1 credit as an additional cost to use an icebreaker ability to break subroutines. Limit 1 region per server.", "stripped_title": "Midway Station Grid", "text": "During runs on this server, the Runner must pay 1[credit] as an additional cost to use an <strong>icebreaker</strong> ability to break subroutines.\nLimit 1 <strong>region</strong> per server.", "title": "Midway Station Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_heinlein_grid_06023(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06023", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"There are many advantages to having facilities on the moon. Less traffic, for example.\" -Director Hass", "illustrator": "Henning Ludvigsen", "keywords": "Region", "pack_code": "tsb", "position": 23, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner loses or spends click during a run on this server, they lose all credits in their credit pool. Limit 1 region per server.", "stripped_title": "Heinlein Grid", "text": "Whenever the Runner loses or spends [click] during a run on this server, they lose all credits in their credit pool.\nLimit 1 <strong>region</strong> per server.", "title": "Heinlein Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_willothewisp_06032(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06032", "cost": 4, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Adam S. Doyle", "pack_code": "tsb", "position": 32, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner makes a successful run on this server, you may trash this upgrade. If you do, choose 1 installed icebreaker that was used to break at least 1 subroutine during this run. The Runner adds that icebreaker to the bottom of the stack.", "stripped_title": "Will-o'-the-Wisp", "text": "Whenever the Runner makes a successful run on this server, you may trash this upgrade. If you do, choose 1 installed <strong>icebreaker</strong> that was used to break at least 1 subroutine during this run. The Runner adds that <strong>icebreaker</strong> to the bottom of the stack.", "title": "Will-o'-the-Wisp", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_port_anson_grid_06044(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06044", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "The port was first built as a remote location to unload and offload dangerous felons.", "illustrator": "Emilio Rodriguez", "keywords": "Region", "pack_code": "fc", "position": 44, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to jack out during a run on this server, the Runner must trash 1 installed program. Limit 1 region per server.", "stripped_title": "Port Anson Grid", "text": "As an additional cost to jack out during a run on this server, the Runner must trash 1 installed program.\nLimit 1 <strong>region</strong> per server.", "title": "Port Anson Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_crisium_grid_06048(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06048", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Mars would never have been colonized if not for the Gagarin facilities at Promontorium Agarum.", "illustrator": "Camille Kuo", "keywords": "Region", "pack_code": "fc", "position": 48, "quantity": 3, "side_code": "corp", "stripped_text": "Runs against this server cannot be declared successful. (This effect does not cause runs to become unsuccessful.) Limit 1 region per server.", "stripped_title": "Crisium Grid", "text": "Runs against this server cannot be declared successful. <em>(This effect does not cause runs to become unsuccessful.)</em>\nLimit 1 <strong>region</strong> per server.", "title": "Crisium Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_shell_corporation_06092(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06092", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Ralph Beisner", "pack_code": "atr", "position": 92, "quantity": 3, "side_code": "corp", "stripped_text": "You cannot use Shell Corporation more than once per turn. click: Place 3 credits on Shell Corporation. click: Take all credits from Shell Corporation.", "stripped_title": "Shell Corporation", "text": "You cannot use Shell Corporation more than once per turn.\n[click]: Place 3[credit] on Shell Corporation.\n[click]: Take all credits from Shell Corporation.", "title": "Shell Corporation", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_selfdestruct_06112(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06112", "cost": 2, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Alexandr Elichev", "pack_code": "ts", "position": 112, "quantity": 3, "side_code": "corp", "stripped_text": "Remote server only. trash: Trash all cards installed in the root of or protecting this server. Trace[X], where X is equal to the number of cards trashed. If successful, do 3 net damage. Use this ability only during a run on this server.", "stripped_title": "Self-destruct", "text": "Remote server only.\n<strong>[trash]:</strong> Trash all cards installed in the root of or protecting this server. Trace[X], where X is equal to the number of cards trashed. If successful, do 3 net damage. Use this ability only during a run on this server.", "title": "Self-destruct", "trash_cost": 0, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_satellite_grid_07023(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07023", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Maciej Rebisz", "keywords": "Region", "pack_code": "oac", "position": 23, "quantity": 3, "side_code": "corp", "stripped_text": "Each piece of ice protecting this server is considered to have 1 additional advancement token on it. Limit 1 region per server.", "stripped_title": "Satellite Grid", "text": "Each piece of ice protecting this server is considered to have 1 additional advancement token on it.\nLimit 1 <strong>region</strong> per server.", "title": "Satellite Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_the_twins_07024(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07024", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Anything worth doing is worth doing twice.", "illustrator": "Antonio De Luca", "keywords": "Sysop", "pack_code": "oac", "position": 24, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner passes a rezzed piece of ice protecting this server, you may reveal and trash another copy of that ice from HQ to force the Runner to encounter the piece of ice just passed again.", "stripped_title": "The Twins", "text": "Whenever the Runner passes a rezzed piece of ice protecting this server, you may reveal and trash another copy of that ice from HQ to force the Runner to encounter the piece of ice just passed again.", "title": "The Twins", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_dedicated_technician_team_07026(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07026", "cost": 1, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Have you tried turning it off and on again?", "illustrator": "Crystal Ben", "pack_code": "oac", "position": 26, "quantity": 3, "side_code": "corp", "stripped_text": "2 recurring credits Use these credits to install ice protecting this server.", "stripped_title": "Dedicated Technician Team", "text": "2[recurring-credit]\nUse these credits to install ice protecting this server.", "title": "Dedicated Technician Team", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_cyberdex_virus_suite_07027(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07027", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Ed Mattinian", "keywords": "Ambush", "pack_code": "oac", "position": 27, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, you may purge virus counters. trash: Purge virus counters.", "stripped_title": "Cyberdex Virus Suite", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade, you may purge virus counters.\n<strong>[trash]:</strong> Purge virus counters.", "title": "Cyberdex Virus Suite", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_valley_grid_08015(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08015", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Simon Weaner", "keywords": "Region", "pack_code": "val", "position": 15, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner fully breaks a piece of ice protecting this server, they get -1 maximum hand size until the beginning of your next turn. Limit 1 region per server.", "stripped_title": "Valley Grid", "text": "Whenever the Runner fully breaks a piece of ice protecting this server, they get -1 maximum hand size until the beginning of your next turn.\nLimit 1 <strong>region</strong> per server.", "title": "Valley Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_breaker_bay_grid_08040(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08040", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "After the Big One, real estate value changed sharply. Some found that they had become owners of beachfront property. Others were underwater.", "illustrator": "Sander Mosk", "keywords": "Region", "pack_code": "bb", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "The rez cost of each card in the root of this server is lowered by 5. Limit 1 region per server.", "stripped_title": "Breaker Bay Grid", "text": "The rez cost of each card in the root of this server is lowered by 5.\nLimit 1 <strong>region</strong> per server.", "title": "Breaker Bay Grid", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_oaktown_grid_08053(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08053", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "Built Oaktown tough.", "illustrator": "Maciej Rebisz", "keywords": "Region", "pack_code": "cc", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "The trash cost of each card in the root of this server is increased by 3. Limit 1 region per server.", "stripped_title": "Oaktown Grid", "text": "The trash cost of each card in the root of this server is increased by 3.\nLimit 1 <strong>region</strong> per server.", "title": "Oaktown Grid", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_ryon_knight_08054(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08054", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Bioroids recognize consciousness in others, but not in themselves.\"", "illustrator": "Roderick Constance", "keywords": "Sysop", "pack_code": "cc", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "trash: Do 1 core damage. Use this ability only during a run against this server and only if the Runner has no unspent click.", "stripped_title": "Ryon Knight", "text": "[trash]: Do 1 core damage. Use this ability only during a run against this server and only if the Runner has no unspent [click].", "title": "Ryon Knight", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_marcus_batty_08074(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08074", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Frederic Pinson", "keywords": "Sysop - Psi", "pack_code": "uw", "position": 74, "quantity": 3, "side_code": "corp", "stripped_text": "trash: You and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, resolve 1 subroutine on a rezzed piece of ice protecting this server. Use this ability only during a run on this server.", "stripped_title": "Marcus Batty", "text": "[trash]: You and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, resolve 1 subroutine on a rezzed piece of ice protecting this server. Use this ability only during a run on this server.", "title": "Marcus Batty", "trash_cost": 1, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_underway_grid_08080(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08080", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "Alex Kim", "keywords": "Region", "pack_code": "uw", "position": 80, "quantity": 3, "side_code": "corp", "stripped_text": "Ice protecting this server cannot be bypassed. Cards in the root of and/or protecting this server cannot be exposed. Limit 1 region per server.", "stripped_title": "Underway Grid", "text": "Ice protecting this server cannot be bypassed.\nCards in the root of and/or protecting this server cannot be exposed.\nLimit 1 <strong>region</strong> per server.", "title": "Underway Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_old_hollywood_grid_08097(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08097", "cost": 5, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "David Ogilvie", "keywords": "Region", "pack_code": "oh", "position": 97, "quantity": 3, "side_code": "corp", "stripped_text": "Persistent -> The Runner cannot steal agendas from this server or its root. Ignore this ability for any agenda the Runner has a copy of in their score area. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.) Limit 1 region per server.", "stripped_title": "Old Hollywood Grid", "text": "Persistent \u2192 The Runner cannot steal agendas from this server or its root. Ignore this ability for any agenda the Runner has a copy of in their score area. <em>(If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)</em>\nLimit 1 <strong>region</strong> per server.", "title": "Old Hollywood Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_product_placement_08115(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08115", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Matt Zeilinger", "keywords": "Advertisement", "pack_code": "uot", "position": 115, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, gain 2 credits.", "stripped_title": "Product Placement", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade anywhere except in Archives, gain 2[credit].", "title": "Product Placement", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_expo_grid_08119(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08119", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "The expo was built in the East California desert: a temporary city constructed for the advancement of humanity.", "illustrator": "Maciej Rebisz", "keywords": "Region", "pack_code": "uot", "position": 119, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, gain 1 credit if there is a rezzed asset installed in the root of this server. Limit 1 region per server.", "stripped_title": "Expo Grid", "text": "When your turn begins, gain 1[credit] if there is a rezzed asset installed in the root of this server.\nLimit 1 <strong>region</strong> per server.", "title": "Expo Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_keegan_lane_09024(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09024", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"We use ice on our servers. More runners should ice their own rigs.\"", "illustrator": "Joshua Meehan", "keywords": "Sysop", "pack_code": "dad", "position": 24, "quantity": 3, "side_code": "corp", "stripped_text": "trash, remove 1 tag: Trash 1 program. Use this ability only during a run on this server.", "stripped_title": "Keegan Lane", "text": "[trash], <strong>remove 1 tag:</strong> Trash 1 program. Use this ability only during a run on this server.", "title": "Keegan Lane", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_rutherford_grid_09025(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09025", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "To the worlds sitting on the couch and watching threedee, Rutherford District might as well be all of New Angeles.", "illustrator": "Johan T\u00f6rnlund", "keywords": "Region", "pack_code": "dad", "position": 25, "quantity": 3, "side_code": "corp", "stripped_text": "The base trace strength of each trace during a run on this server is increased by 2. Limit 1 region per server.", "stripped_title": "Rutherford Grid", "text": "The base trace strength of each trace during a run on this server is increased by 2.\nLimit 1 <strong>region</strong> per server.", "title": "Rutherford Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_mumbad_city_grid_10014(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10014", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Zach Graves", "keywords": "Region", "pack_code": "kg", "position": 14, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner passes a piece of ice protecting this server, you may swap that ice with another piece of ice protecting this server. Limit 1 region per server.", "stripped_title": "Mumbad City Grid", "text": "Whenever the Runner passes a piece of ice protecting this server, you may swap that ice with another piece of ice protecting this server.\nLimit 1 <strong>region</strong> per server.", "title": "Mumbad City Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_disposable_hq_10034(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10034", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Simon Weaner", "keywords": "Ambush", "pack_code": "bf", "position": 34, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, you may add any number of cards from HQ to the bottom of R&D.", "stripped_title": "Disposable HQ", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade, you may add any number of cards from HQ to the bottom of R&D.", "title": "Disposable HQ", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_surat_city_grid_10057(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10057", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "The political centre of Mumbad.", "illustrator": "Maciej Rebisz", "keywords": "Region", "pack_code": "dag", "position": 57, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you rez another card in the root of or protecting this server, you may rez 1 card, paying 2 credits less. Limit 1 region per server.", "stripped_title": "Surat City Grid", "text": "Whenever you rez another card in the root of or protecting this server, you may rez 1 card, paying 2[credit] less.\nLimit 1 <strong>region</strong> per server.", "title": "Surat City Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_mumbad_virtual_tour_10076(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10076", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 2, "illustrator": "Adam S. Doyle", "keywords": "Alliance", "pack_code": "si", "position": 76, "quantity": 3, "side_code": "corp", "stripped_text": "This upgrade costs 0 influence if you have 7 or more assets in your deck. When the Runner accesses this upgrade while it is installed, they must trash it, if able.", "stripped_title": "Mumbad Virtual Tour", "text": "This upgrade costs 0 influence if you have 7 or more assets in your deck.\nWhen the Runner accesses this upgrade while it is installed, they must trash it, if able.", "title": "Mumbad Virtual Tour", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_navi_mumbai_city_grid_10110(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10110", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "The entertainment capital of Mumbad.", "illustrator": "Johan T\u00f6rnlund", "keywords": "Region", "pack_code": "ftm", "position": 110, "quantity": 3, "side_code": "corp", "stripped_text": "During runs on this server, the Runner cannot use paid abilities on their installed cards except for mid-access abilities and abilities on icebreakers. Limit 1 region per server.", "stripped_title": "Navi Mumbai City Grid", "text": "During runs on this server, the Runner cannot use paid abilities on their installed cards except for mid-access abilities and abilities on <strong>icebreakers</strong>.\nLimit 1 <strong>region</strong> per server.", "title": "Navi Mumbai City Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_georgia_emelyov_11014(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11014", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "\"Your mistake is thinking that it's just business, when really it's a war.\"", "illustrator": "Aurore Folny", "keywords": "Sysop", "pack_code": "23s", "position": 14, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner makes an unsuccessful run on this server, do 1 net damage. 2 credits: Move Georgia Emelyov to another server.", "stripped_title": "Georgia Emelyov", "text": "Whenever the Runner makes an unsuccessful run on this server, do 1 net damage.\n2[credit]: Move Georgia Emelyov to another server.", "title": "Georgia Emelyov", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_prisec_11040(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11040", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "\"While the money pooled at the top, the power went with it, until there were two sets of laws: one for them, one for us\" -Omar Keung, the Flashpoint", "illustrator": "Maciej Rebisz", "keywords": "Ambush", "pack_code": "bm", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "If the Runner accesses Prisec while installed, you may pay 2 credits to give the Runner 1 tag and do 1 meat damage.", "stripped_title": "Prisec", "text": "If the Runner accesses Prisec while installed, you may pay 2[credit] to give the Runner 1 tag and do 1 meat damage.", "title": "Prisec", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_drone_screen_11076(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11076", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Falstaff-337B; decrypt-ok; loc:0.258500, -79.920791 -ok; auth-ok; msg:KAR kill authority requested y/n?", "illustrator": "Adam S. Doyle", "pack_code": "in", "position": 76, "quantity": 3, "side_code": "corp", "stripped_text": "If the Runner is tagged, Drone Screen gains \"Whenever the Runner initiates a run on this server, Trace[3]. If successful, do 1 meat damage (cannot be prevented).\"", "stripped_title": "Drone Screen", "text": "If the Runner is tagged, Drone Screen gains \"Whenever the Runner initiates a run on this server, Trace[3]. If successful, do 1 meat damage (cannot be prevented).\"", "title": "Drone Screen", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_manta_grid_11091(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11091", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Simon Weaner", "keywords": "Region", "pack_code": "ml", "position": 91, "quantity": 3, "side_code": "corp", "stripped_text": "If the Runner has fewer than 6 credits or no unspent clicks when a successful run on this server ends, you have 1 additional click to spend your next turn. Limit 1 region per server.", "stripped_title": "Manta Grid", "text": "If the Runner has fewer than 6[credit] or no unspent clicks when a successful run on this server ends, you have 1 additional [click] to spend your next turn.\nLimit 1 <strong>region</strong> per server.", "title": "Manta Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_nihongai_grid_11093(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11093", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "VIKO", "keywords": "Region", "pack_code": "ml", "position": 93, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner makes a successful run on this server, if they do not have at least 2 cards in the grip and 6 credits, you may look at the top 5 cards of R&D and swap 1 of those cards with 1 card in HQ. Limit 1 region per server.", "stripped_title": "Nihongai Grid", "text": "Whenever the Runner makes a successful run on this server, if they do not have at least 2 cards in the grip and 6[credit], you may look at the top 5 cards of R&D and swap 1 of those cards with 1 card in HQ.\nLimit 1 <strong>region</strong> per server.", "title": "Nihongai Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_bryan_stinson_11117(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11117", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "\"My job? I provide legal exculpation and sign everything. It pays very well.\"", "illustrator": "Priscilla Kim", "keywords": "Character", "pack_code": "qu", "position": 117, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner has fewer than 6 credits, Bryan Stinson gains \"click: Play a transaction operation from Archives, ignoring all costs. Remove that transaction from the game instead of trashing it.\"", "stripped_title": "Bryan Stinson", "text": "While the Runner has fewer than 6[credit], Bryan Stinson gains \"[click]: Play a <strong>transaction</strong> operation from Archives, ignoring all costs. Remove that <strong>transaction</strong> from the game instead of trashing it.\"", "title": "Bryan Stinson", "trash_cost": 5, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_defense_construct_12011(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12011", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Pavel Kolomeyets", "pack_code": "dc", "position": 11, "quantity": 3, "side_code": "corp", "stripped_text": "Defense Construct can be advanced. trash: Add 1 facedown card from Archives to HQ for each advancement token on Defense Construct. Use this ability only during a run on Archives.", "stripped_title": "Defense Construct", "text": "Defense Construct can be advanced.\n[trash]: Add 1 facedown card from Archives to HQ for each advancement token on Defense Construct. Use this ability only during a run on Archives.", "title": "Defense Construct", "trash_cost": 0, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_oberth_protocol_12018(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12018", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "illustrator": "Pavel Kolomeyets", "pack_code": "dc", "position": 18, "quantity": 3, "side_code": "corp", "stripped_text": "As an additional cost to rez this upgrade, forfeit 1 agenda. The first time each turn you advance a card in the root of or protecting this server, place 1 more advancement counter on that card.", "stripped_title": "Oberth Protocol", "text": "As an additional cost to rez this upgrade, forfeit 1 agenda.\nThe first time each turn you advance a card in the root of or protecting this server, place 1 more advancement counter on that card.", "title": "Oberth Protocol", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_khondi_plaza_12019(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12019", "cost": 3, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "flavor": "Senate staffers and clerks of the MCA can be seen thronging Khondi Plaza during break times.", "illustrator": "Maciej Rebisz", "keywords": "Ritzy", "pack_code": "dc", "position": 19, "quantity": 3, "side_code": "corp", "stripped_text": "X recurring credits Use these credits to rez ice protecting this server. X is the number of remote servers.", "stripped_title": "Khondi Plaza", "text": "X[recurring-credit]\nUse these credits to rez ice protecting this server. X is the number of remote servers.", "title": "Khondi Plaza", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_signal_jamming_12020(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12020", "cost": 0, "deck_limit": 3, "faction_code": "neutral-corp", "faction_cost": 0, "illustrator": "JuanManuel Tumburus", "pack_code": "dc", "position": 20, "quantity": 3, "side_code": "corp", "stripped_text": "trash: Cards cannot be installed until the end of the run. Use this ability only during a run on this server.", "stripped_title": "Signal Jamming", "text": "[trash]: Cards cannot be installed until the end of the run. Use this ability only during a run on this server.", "title": "Signal Jamming", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_bamboo_dome_12053(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12053", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Pavel Kolomeyets", "keywords": "Region", "pack_code": "eas", "position": 53, "quantity": 3, "side_code": "corp", "stripped_text": "Install only in the root of R&D. click: Reveal the top 3 cards of R&D. Secretly choose 1 to add to HQ. Return the others to the top of R&D, in any order. Limit 1 region per server.", "stripped_title": "Bamboo Dome", "text": "Install only in the root of R&D.\n[click]: Reveal the top 3 cards of R&D. Secretly choose 1 to add to HQ. Return the others to the top of R&D, in any order.\nLimit 1 <strong>region</strong> per server.", "title": "Bamboo Dome", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_ben_musashi_12054(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12054", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "illustrator": "Alexandr Elichev", "keywords": "Clone", "pack_code": "eas", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must suffer 2 net damage. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)", "stripped_title": "Ben Musashi", "text": "Persistent \u2192 As an additional cost to steal an agenda from this server or its root, the Runner must suffer 2 net damage. <em>(If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)</em>", "title": "Ben Musashi", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_henry_phillips_12056(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12056", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"Toying with them is where the job satisfaction comes in\".", "illustrator": "Nasrul Hakim", "keywords": "Sysop", "pack_code": "eas", "position": 56, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner breaks a subroutine during a run on this server, gain 2 credits if they are tagged.", "stripped_title": "Henry Phillips", "text": "Whenever the Runner breaks a subroutine during a run on this server, gain 2[credit] if they are tagged.", "title": "Henry Phillips", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_warroid_tracker_12068(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12068", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Micah Epstein", "keywords": "Bioroid", "pack_code": "baw", "position": 68, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner trashes at least 1 card from this server, from its root, or protecting it, Trace[4]. If successful, the Runner trashes 2 of their installed cards.", "stripped_title": "Warroid Tracker", "text": "Whenever the Runner trashes at least 1 card from this server, from its root, or protecting it, Trace[4]. If successful, the Runner trashes 2 of their installed cards.", "title": "Warroid Tracker", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_traffic_analyzer_12075(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12075", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "\"It's all about M.E. Monetizing Everything.\" -Eryn Nielle", "illustrator": "Tim Durning", "pack_code": "baw", "position": 75, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you rez a piece of ice protecting this server, Trace[2]. If successful, the Corp gains 1 credit.", "stripped_title": "Traffic Analyzer", "text": "Whenever you rez a piece of ice protecting this server, Trace[2]. If successful, the Corp gains 1[credit].", "title": "Traffic Analyzer", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_helheim_servers_12091(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12091", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "illustrator": "James Ives", "keywords": "Facility", "pack_code": "fm", "position": 91, "quantity": 3, "side_code": "corp", "stripped_text": "Trash 1 card from HQ: All ice protecting this server has +2 strength until the end of the run. Use this ability only during a run on this server.", "stripped_title": "Helheim Servers", "text": "<strong>Trash 1 card from HQ</strong>: All ice protecting this server has +2 strength until the end of the run. Use this ability only during a run on this server.", "title": "Helheim Servers", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_fractal_threat_matrix_12119(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12119", "cost": 4, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "\"I embedded recursive data loops into the go-no-go subroutines of every piece of ice.\" -Anson Rose", "illustrator": "Caroline Elizabeth Huss", "keywords": "Security Protocol", "pack_code": "cd", "position": 119, "quantity": 3, "side_code": "corp", "stripped_text": "Each time all the subroutines are broken on a piece of ice protecting this server, trash the top 2 cards of the stack.", "stripped_title": "Fractal Threat Matrix", "text": "Each time all the subroutines are broken on a piece of ice protecting this server, trash the top 2 cards of the stack.", "title": "Fractal Threat Matrix", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_black_level_clearance_13039(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13039", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 5, "flavor": "Even knowing this floor existed was cause for termination...", "illustrator": "Antonio De Luca", "keywords": "Security Protocol", "pack_code": "td", "position": 39, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner makes a successful run on this server, they must either suffer 1 core damage or jack out. If the Runner jacks out this way, gain 5 credits, draw 1 card, and trash this upgrade.", "stripped_title": "Black Level Clearance", "text": "Whenever the Runner makes a successful run on this server, they must either suffer 1 core damage or jack out. If the Runner jacks out this way, gain 5[credit], draw 1 card, and trash this upgrade.", "title": "Black Level Clearance", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_mason_bellamy_13040(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13040", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"They say he is an ex-runner. I don't know if it is true, but he is chromed to the gills and seems to know all the runners' tricks.\"", "illustrator": "Matt Zeilinger", "keywords": "Sysop", "pack_code": "td", "position": 40, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever an encounter with a piece of ice protecting this server ends, if the Runner broke at least 1 subroutine during that encounter, they lose click.", "stripped_title": "Mason Bellamy", "text": "Whenever an encounter with a piece of ice protecting this server ends, if the Runner broke at least 1 subroutine during that encounter, they lose [click].", "title": "Mason Bellamy", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_k_p_lynn_13052(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13052", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Anastasia Ovchinnikova", "keywords": "Executive", "pack_code": "td", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner passes all of the ice protecting this server, they must take 1 tag or end the run.", "stripped_title": "K. P. Lynn", "text": "Whenever the Runner passes all of the ice protecting this server, they must take 1 tag or end the run.", "title": "K. P. Lynn", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_ash_2x3zb9cy_20075(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20075", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Eyes forward, please.\"", "illustrator": "Antonio De Luca", "keywords": "Bioroid", "pack_code": "core2", "position": 75, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever there is a successful run on this server, Trace[4]. If successful, the Runner cannot access any cards other than Ash 2X3ZB9CY for the remainder of this run.", "stripped_title": "Ash 2X3ZB9CY", "text": "Whenever there is a successful run on this server, Trace[4]. If successful, the Runner cannot access any cards other than Ash 2X3ZB9CY for the remainder of this run.", "title": "Ash 2X3ZB9CY", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_strongbox_20076(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20076", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "illustrator": "Andreas Zafiratos", "pack_code": "core2", "position": 76, "quantity": 1, "side_code": "corp", "stripped_text": "Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must spend click. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)", "stripped_title": "Strongbox", "text": "Persistent \u2192 As an additional cost to steal an agenda from this server or its root, the Runner must spend [click]. <em>(If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)</em>", "title": "Strongbox", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_hokusai_grid_20108(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20108", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Despite its appearance, the Hokusai Grid is the most notorious research facility at Jinteki.", "illustrator": "Emilio Rodriguez", "keywords": "Region", "pack_code": "core2", "position": 92, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever the Runner makes a successful run on this server, do 1 net damage. Limit 1 region per server.", "stripped_title": "Hokusai Grid", "text": "Whenever the Runner makes a successful run on this server, do 1 net damage.\nLimit 1 <strong>region</strong> per server.", "title": "Hokusai Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_red_herrings_20122(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20122", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Liiga Smilshkalne", "pack_code": "core2", "position": 106, "quantity": 1, "side_code": "corp", "stripped_text": "Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must pay 5 credits. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)", "stripped_title": "Red Herrings", "text": "Persistent \u2192 As an additional cost to steal an agenda from this server or its root, the Runner must pay 5[credit]. <em>(If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)</em>", "title": "Red Herrings", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_bernice_mai_20123(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20123", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Keeping tabs on the world, one screen at a time.", "illustrator": "Erfan Fajar", "keywords": "Sysop", "pack_code": "core2", "position": 107, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever there is a successful run on this server, Trace[5]. If successful, give the Runner 1 tag. If unsuccessful, trash Bernice Mai.", "stripped_title": "Bernice Mai", "text": "Whenever there is a successful run on this server, Trace[5]. If successful, give the Runner 1 tag. If unsuccessful, trash Bernice Mai.", "title": "Bernice Mai", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_calibration_testing_21017(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21017", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"Once every week, we perform a drill. Except, I'm the only one who knows it's a drill.\"", "illustrator": "James Cory Webster", "keywords": "Off-site", "pack_code": "ss", "position": 17, "quantity": 3, "side_code": "corp", "stripped_text": "Remote server only. trash: Place 1 advancement counter on a card installed in the root of this server.", "stripped_title": "Calibration Testing", "text": "Remote server only.\n<strong>[trash]:</strong> Place 1 advancement counter on a card installed in the root of this server.", "title": "Calibration Testing", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_jinja_city_grid_21031(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21031", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"The site of the world's second beanstalk, or I'll die trying.\" - Miria Byanyima, Director of VSEP", "illustrator": "Kirsten Zirngibl", "keywords": "Region", "pack_code": "dtwn", "position": 31, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you draw a piece of ice, you may reveal it and install it protecting this server, paying 4 credits less. Limit 1 region per server.", "stripped_title": "Jinja City Grid", "text": "Whenever you draw a piece of ice, you may reveal it and install it protecting this server, paying 4[credit] less.\nLimit 1 <strong>region</strong> per server.", "title": "Jinja City Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_forced_connection_21037(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21037", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "illustrator": "Josh Corpuz", "keywords": "Ambush", "pack_code": "dtwn", "position": 37, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, Trace[3]. If successful, give the Runner 2 tags.", "stripped_title": "Forced Connection", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade anywhere except in Archives, Trace[3]. If successful, give the Runner 2 tags.", "title": "Forced Connection", "trash_cost": 0, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_code_replicator_21052(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21052", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "for (;;)", "illustrator": "Caravan Studio", "pack_code": "cotc", "position": 52, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner passes a rezzed piece of ice protecting this server, you may trash this upgrade. If you do, the Runner must approach that ice again. They may jack out.", "stripped_title": "Code Replicator", "text": "Whenever the Runner passes a rezzed piece of ice protecting this server, you may trash this upgrade. If you do, the Runner must approach that ice again. They may jack out.", "title": "Code Replicator", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_tempus_21071(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21071", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "illustrator": "Liiga Smilshkalne", "keywords": "Ambush", "pack_code": "tdatd", "position": 71, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, Trace[3]. If successful, the Runner must lose click click or suffer 1 core damage.", "stripped_title": "Tempus", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade anywhere except in Archives, Trace[3]. If successful, the Runner must lose [click][click] or suffer 1 core damage.", "title": "Tempus", "trash_cost": 0, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_bio_vault_21072(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21072", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Many things go in. Nothing comes out.", "illustrator": "Pavel Kolomeyets", "keywords": "Off-site", "pack_code": "tdatd", "position": 72, "quantity": 3, "side_code": "corp", "stripped_text": "Install only in a remote server. Bio Vault can be advanced. trash, 2 hosted advancement tokens: End the run.", "stripped_title": "Bio Vault", "text": "Install only in a remote server.\nBio Vault can be advanced.\n[trash], <strong>2 hosted advancement tokens:</strong> End the run.", "title": "Bio Vault", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_mwanza_city_grid_21096(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21096", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "illustrator": "Yog Joshi", "keywords": "Region", "pack_code": "win", "position": 96, "quantity": 3, "side_code": "corp", "stripped_text": "Root of HQ or R&D only. Whenever the Runner breaches this server, they access 3 additional cards. When the breach ends, gain 2 credits for each time the Runner accessed a card during that breach. Limit 1 region per server.", "stripped_title": "Mwanza City Grid", "text": "Root of HQ or R&D only.\nWhenever the Runner breaches this server, they access 3 additional cards. When the breach ends, gain 2[credit] for each time the Runner accessed a card during that breach.\nLimit 1 <strong>region</strong> per server.", "title": "Mwanza City Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_intake_21098(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21098", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "illustrator": "Adam S. Doyle", "keywords": "Ambush", "pack_code": "win", "position": 98, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, Trace[4]. If successful, add 1 installed program or virtual resource to the grip.", "stripped_title": "Intake", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade anywhere except in Archives, Trace[4]. If successful, add 1 installed program or <strong>virtual</strong> resource to the grip.", "title": "Intake", "trash_cost": 0, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_overseer_matrix_21100(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21100", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "The blast doesn't hurt, but what comes after does.", "illustrator": "Mariusz Siergiejew", "pack_code": "win", "position": 100, "quantity": 3, "side_code": "corp", "stripped_text": "Persistent -> Whenever the Runner trashes a card from this server or its root, you may pay 1 credit to give the Runner 1 tag. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)", "stripped_title": "Overseer Matrix", "text": "Persistent \u2192 Whenever the Runner trashes a card from this server or its root, you may pay 1[credit] to give the Runner 1 tag. <em>(If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)</em>", "title": "Overseer Matrix", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_giordano_memorial_field_22033(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22033", "cost": 3, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "The world changed. Concession prices did not.", "illustrator": "Emilio Rodriguez", "keywords": "Facility", "pack_code": "rar", "position": 33, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner makes a successful run on this server, end the run unless they pay 2 credits for each agenda in their score area.", "stripped_title": "Giordano Memorial Field", "text": "Whenever the Runner makes a successful run on this server, end the run unless they pay 2[credit] for each agenda in their score area.", "title": "Giordano Memorial Field", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_daruma_22041(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22041", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "JB Casacop", "pack_code": "rar", "position": 41, "quantity": 3, "side_code": "corp", "stripped_text": "When the Runner approaches this server, you may trash this upgrade. If you do, choose 1 card in the root of another server or 1 agenda, asset, or upgrade in HQ. Swap that card with 1 card in the root of this server. If you swap cards this way, the Runner may jack out.", "stripped_title": "Daruma", "text": "When the Runner approaches this server, you may trash this upgrade. If you do, choose 1 card in the root of another server or 1 agenda, asset, or upgrade in HQ. Swap that card with 1 card in the root of this server. If you swap cards this way, the Runner may jack out.", "title": "Daruma", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_arella_salvatore_22049(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22049", "cost": 2, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"Cheers, Philbert.\"", "illustrator": "Matt Zeilinger", "keywords": "Sysop", "pack_code": "rar", "position": 49, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever an agenda is scored from this server, you may install a card from HQ, ignoring all costs, and place 1 advancement token on it.", "stripped_title": "Arella Salvatore", "text": "Whenever an agenda is scored from this server, you may install a card from HQ, ignoring all costs, and place 1 advancement token on it.", "title": "Arella Salvatore", "trash_cost": 5, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_embolus_23011(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "23011", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "<strong>Designed by 2016 GenCon Champion Dan D'Argenio</strong>", "illustrator": "Mariusz Siergiejew", "pack_code": "mo", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may pay 1 credit to place 1 power counter on this upgrade. Whenever the Runner makes a successful run, remove 1 power counter from this upgrade. Hosted power counter: End the run. Use this ability only during a run on this server.", "stripped_title": "Embolus", "text": "When your turn begins, you may pay 1[credit] to place 1 power counter on this upgrade.\nWhenever the Runner makes a successful run, remove 1 power counter from this upgrade.\n<strong>Hosted power counter</strong>: End the run. Use this ability only during a run on this server.", "title": "Embolus", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_hired_help_23101(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "23101", "cost": 1, "deck_limit": 1, "faction_code": "neutral-corp", "faction_cost": 1, "flavor": "<strong>Designed by the Day 1B players at Magnum Opus</strong>", "illustrator": "Matt Zeilinger", "keywords": "Orgcrime - Enforcer", "pack_code": "mo", "position": 8, "quantity": 1, "side_code": "corp", "stripped_text": "As an additional cost to run this server, the Runner must trash 1 agenda from their score area. Ignore this ability if the Runner made a successful run on HQ this turn. Limit 1 per deck.", "stripped_title": "Hired Help", "text": "As an additional cost to run this server, the Runner must trash 1 agenda from their score area. Ignore this ability if the Runner made a successful run on HQ this turn.\nLimit 1 per deck.", "title": "Hired Help", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_ash_2x3zb9cy_25082(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25082", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "\"Eyes forward, please.\"", "illustrator": "Antonio De Luca", "keywords": "Bioroid", "pack_code": "sc19", "position": 82, "quantity": 2, "side_code": "corp", "stripped_text": "Whenever there is a successful run on this server, Trace[4]. If successful, the Runner cannot access any cards other than Ash 2X3ZB9CY for the remainder of this run.", "stripped_title": "Ash 2X3ZB9CY", "text": "Whenever there is a successful run on this server, Trace[4]. If successful, the Runner cannot access any cards other than Ash 2X3ZB9CY for the remainder of this run.", "title": "Ash 2X3ZB9CY", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_mason_bellamy_25083(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25083", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"They say he is an ex-runner. I don't know if it is true, but he is chromed to the gills and seems to know all the runners' tricks.\"", "illustrator": "Matt Zeilinger", "keywords": "Sysop", "pack_code": "sc19", "position": 83, "quantity": 1, "side_code": "corp", "stripped_text": "Whenever an encounter with a piece of ice protecting this server ends, if the Runner broke at least 1 subroutine during that encounter, they lose click.", "stripped_title": "Mason Bellamy", "text": "Whenever an encounter with a piece of ice protecting this server ends, if the Runner broke at least 1 subroutine during that encounter, they lose [click].", "title": "Mason Bellamy", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_hokusai_grid_25103(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25103", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Despite its appearance, the Hokusai Grid is the most notorious research facility at Jinteki.", "illustrator": "Emilio Rodriguez", "keywords": "Region", "pack_code": "sc19", "position": 103, "quantity": 2, "side_code": "corp", "stripped_text": "Whenever the Runner makes a successful run on this server, do 1 net damage. Limit 1 region per server.", "stripped_title": "Hokusai Grid", "text": "Whenever the Runner makes a successful run on this server, do 1 net damage.\nLimit 1 <strong>region</strong> per server.", "title": "Hokusai Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_product_placement_25120(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25120", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "illustrator": "Matt Zeilinger", "keywords": "Advertisement", "pack_code": "sc19", "position": 120, "quantity": 2, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade anywhere except in Archives, gain 2 credits.", "stripped_title": "Product Placement", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade anywhere except in Archives, gain 2[credit].", "title": "Product Placement", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_red_herrings_25121(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25121", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "illustrator": "Liiga Smilshkalne", "pack_code": "sc19", "position": 121, "quantity": 2, "side_code": "corp", "stripped_text": "Persistent -> As an additional cost to steal an agenda from this server or its root, the Runner must pay 5 credits. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)", "stripped_title": "Red Herrings", "text": "Persistent \u2192 As an additional cost to steal an agenda from this server or its root, the Runner must pay 5[credit]. <em>(If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)</em>", "title": "Red Herrings", "trash_cost": 1, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_crisium_grid_25139(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25139", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "Mars would never have been colonized if not for the Gagarin facilities at Promontorium Agarum.", "illustrator": "Camille Kuo", "keywords": "Region", "pack_code": "sc19", "position": 139, "quantity": 1, "side_code": "corp", "stripped_text": "Runs against this server cannot be declared successful. (This effect does not cause runs to become unsuccessful.) Limit 1 region per server.", "stripped_title": "Crisium Grid", "text": "Runs against this server cannot be declared successful. <em>(This effect does not cause runs to become unsuccessful.)</em>\nLimit 1 <strong>region</strong> per server.", "title": "Crisium Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_cold_site_server_26038(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26038", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "The Net abhors a vacuum. Any unexplained gap must be <em>made.</em>", "illustrator": "Krembler", "keywords": "Facility", "pack_code": "df", "position": 38, "quantity": 3, "side_code": "corp", "stripped_text": "click: Place 1 power counter on this upgrade. As an additional cost to run this server, the Runner must spend 1click and 1 credit for each hosted power counter. When your turn begins, remove all hosted power counters.", "stripped_title": "Cold Site Server", "text": "[click]<strong>:</strong> Place 1 power counter on this upgrade.\nAs an additional cost to run this server, the Runner must spend 1[click] and 1[credit] for each hosted power counter.\nWhen your turn begins, remove all hosted power counters.", "title": "Cold Site Server", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_letheia_nisei_26046(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26046", "cost": 1, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "illustrator": "Diana Simonova (Antheia Vaulor)", "keywords": "Psi - Clone", "pack_code": "df", "position": 46, "quantity": 3, "side_code": "corp", "stripped_text": "The first time each run the Runner approaches this server, you and the Runner secretly spend 0 credits, 1 credit, or 2 credits. Reveal spent credits. If you and the Runner spent a different number of credits, you may trash this upgrade. If you do, the Runner moves to the outermost position of this server. The Runner may jack out.", "stripped_title": "Letheia Nisei", "text": "The first time each run the Runner approaches this server, you and the Runner secretly spend 0[credit], 1[credit], or 2[credit]. Reveal spent credits. If you and the Runner spent a different number of credits, you may trash this upgrade. If you do, the Runner moves to the outermost position of this server. The Runner may jack out.", "title": "Letheia Nisei", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_increased_drop_rates_26054(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26054", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 1, "flavor": "Ultra-Mythic chance \u2191!\u2191!\u2191! Free Vorpal Tommy Gun [epic] and pinstripe suit [cosmetic] with 10x buy-in!", "illustrator": "N. Hopkins, Krembler", "keywords": "Ambush", "pack_code": "df", "position": 54, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, remove 1 bad publicity unless they take 1 tag.", "stripped_title": "Increased Drop Rates", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade, remove 1 bad publicity unless they take 1 tag.", "title": "Increased Drop Rates", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_reduced_service_26062(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26062", "cost": 0, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "illustrator": "Krembler", "pack_code": "df", "position": 62, "quantity": 3, "side_code": "corp", "stripped_text": "When you rez this upgrade, you may pay up to 4 credits to place that many power counters on it. As an additional cost to run this server, the Runner must pay 2 credits for each hosted power counter. Whenever the Runner makes a successful run on a central server, remove 1 hosted power counter.", "stripped_title": "Reduced Service", "text": "When you rez this upgrade, you may pay up to 4[credit] to place that many power counters on it.\nAs an additional cost to run this server, the Runner must pay 2[credit] for each hosted power counter.\nWhenever the Runner makes a successful run on a central server, remove 1 hosted power counter.", "title": "Reduced Service", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_tranquility_home_grid_26105(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26105", "cost": 1, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 2, "flavor": "The oldest of Heinlein's domes, the self-proclaimed heart of Lunar culture.", "illustrator": "Zoe Cohen", "keywords": "Region", "pack_code": "ur", "position": 105, "quantity": 3, "side_code": "corp", "stripped_text": "Remote server only. The first time each turn you install a card in the root of this server, gain 2 credits or draw 1 card. Limit 1 region per server.", "stripped_title": "Tranquility Home Grid", "text": "Remote server only.\nThe first time each turn you install a card in the root of this server, gain 2[credit] or draw 1 card.\nLimit 1 <strong>region</strong> per server.", "title": "Tranquility Home Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_la_costa_grid_26112(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26112", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Some slums of New Angeles are so worn down, City Hall calls the acres of windowless clone barracks \"gentrification\" with a straight face.", "illustrator": "Eirik H. Kiil", "keywords": "Region - Seedy", "pack_code": "ur", "position": 112, "quantity": 3, "side_code": "corp", "stripped_text": "Remote server only. When your turn begins, place 1 advancement counter on a card installed in the root of this server. Limit 1 region per server.", "stripped_title": "La Costa Grid", "text": "Remote server only.\nWhen your turn begins, place 1 advancement counter on a card installed in the root of this server.\nLimit 1 <strong>region</strong> per server.", "title": "La Costa Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_ganked_26119(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26119", "cost": 0, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 2, "flavor": "Roll Initiative...", "illustrator": "N. Hopkins", "keywords": "Ambush", "pack_code": "ur", "position": 119, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, you may trash it to choose a rezzed piece of ice protecting this server. The Runner encounters that ice.", "stripped_title": "Ganked!", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade, you may trash it to choose a rezzed piece of ice protecting this server. The Runner encounters that ice.", "title": "Ganked!", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_cayambe_grid_26127(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26127", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "The Apu spirits of the great mountains bridge this world and the realm above.", "illustrator": "Kira L. Nguyen", "keywords": "Region", "pack_code": "ur", "position": 127, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, place 1 advancement token on a piece of ice protecting this server. Whenever the Runner approaches this server, end the run unless they pay 2 credits for each advanced piece of ice protecting this server. Limit 1 region per server.", "stripped_title": "Cayambe Grid", "text": "When your turn begins, place 1 advancement token on a piece of ice protecting this server.\nWhenever the Runner approaches this server, end the run unless they pay 2[credit] for each advanced piece of ice protecting this server.\nLimit 1 <strong>region</strong> per server.", "title": "Cayambe Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_la_costa_grid_27005(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "27005", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 3, "flavor": "Some slums of New Angeles are so worn down, City Hall calls the acres of windowless clone barracks \"gentrification\" with a straight face.", "illustrator": "Eirik H. Kiil", "keywords": "Region - Seedy", "pack_code": "urbp", "position": 5, "quantity": 3, "side_code": "corp", "stripped_text": "Remote server only. When your turn begins, place 1 advancement counter on a card installed in the root of this server. Limit 1 region per server.", "stripped_title": "La Costa Grid", "text": "Remote server only.\nWhen your turn begins, place 1 advancement counter on a card installed in the root of this server.\nLimit 1 <strong>region</strong> per server.", "title": "La Costa Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_cayambe_grid_27007(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "27007", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "The Apu spirits of the great mountains bridge this world and the realm above.", "illustrator": "Kira L. Nguyen", "keywords": "Region", "pack_code": "urbp", "position": 7, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, place 1 advancement token on a piece of ice protecting this server. Whenever the Runner approaches this server, end the run unless they pay 2 credits for each advanced piece of ice protecting this server. Limit 1 region per server.", "stripped_title": "Cayambe Grid", "text": "When your turn begins, place 1 advancement token on a piece of ice protecting this server.\nWhenever the Runner approaches this server, end the run unless they pay 2[credit] for each advanced piece of ice protecting this server.\nLimit 1 <strong>region</strong> per server.", "title": "Cayambe Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_embolus_28003(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "28003", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "<strong>Designed by 2016 GenCon Champion Dan D'Argenio</strong>", "illustrator": "Kevin Tame", "pack_code": "mor", "position": 3, "quantity": 3, "side_code": "corp", "stripped_text": "When your turn begins, you may pay 1 credit to place 1 power counter on this upgrade. Whenever the Runner makes a successful run, remove 1 power counter from this upgrade. Hosted power counter: End the run. Use this ability only during a run on this server.", "stripped_title": "Embolus", "text": "When your turn begins, you may pay 1[credit] to place 1 power counter on this upgrade.\nWhenever the Runner makes a successful run, remove 1 power counter from this upgrade.\n<strong>Hosted power counter</strong>: End the run. Use this ability only during a run on this server.", "title": "Embolus", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_sansan_city_grid_29014(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "29014", "cost": 6, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "\"I hear the coast is nice this time of year.\"\n\"If you're in the right business, it's nice all the year.\"", "illustrator": "Ed Mattinian", "keywords": "Region", "pack_code": "sm", "position": 14, "quantity": 1, "side_code": "corp", "stripped_text": "Each agenda in the root of this server gets -1 advancement requirement. Limit 1 region per server.", "stripped_title": "SanSan City Grid", "text": "Each agenda in the root of this server gets -1 advancement requirement.\nLimit 1 <strong>region</strong> per server.", "title": "SanSan City Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_manegarm_skunkworks_30042(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30042", "cost": 2, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "\"Whose memory-tape needs such stringent security?\"\n\u2014The Catalyst", "illustrator": "David Lei", "pack_code": "sg", "position": 42, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner approaches this server, end the run unless they either spend click click or pay 5 credits.", "stripped_title": "Manegarm Skunkworks", "text": "Whenever the Runner approaches this server, end the run unless they either spend [click][click] or pay 5[credit].", "title": "Manegarm Skunkworks", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_anoetic_void_30050(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30050", "cost": 0, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 4, "flavor": "The self-evolving Net twists into spaces unthought and unthinkable: realms of gods and other infohazards, mocking our sacrifices to petty causality.\n\u2014Conceptual Frameworks for Applied Theology", "illustrator": "BalanceSheet", "pack_code": "sg", "position": 50, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner approaches this server, you may pay 2 credits and trash 2 cards from HQ. If you do, end the run.", "stripped_title": "Anoetic Void", "text": "Whenever the Runner approaches this server, you may pay 2[credit] and trash 2 cards from HQ. If you do, end the run.", "title": "Anoetic Void", "trash_cost": 1, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_amaze_amusements_30058(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30058", "cost": 1, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "Free commemorative souvenir!", "illustrator": "Bruno Balixa", "pack_code": "sg", "position": 58, "quantity": 3, "side_code": "corp", "stripped_text": "Persistent -> Whenever a run on this server ends, if the Runner stole any agendas during that run, give the Runner 2 tags. (If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)", "stripped_title": "AMAZE Amusements", "text": "Persistent \u2192 Whenever a run on this server ends, if the Runner stole any agendas during that run, give the Runner 2 tags. <em>(If the Runner trashes this card while accessing it, this ability still applies for the remainder of this run.)</em>", "title": "AMAZE Amusements", "trash_cost": 3, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_malapert_data_vault_30066(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30066", "cost": 1, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 3, "flavor": "Sunlight does not touch the Crater of Eternal Darkness, a fitting abode for the Consortium's malefic secrets.", "illustrator": "Owen Sinodov", "pack_code": "sg", "position": 66, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you score an agenda from this server, you may search R&D for 1 non-agenda card and reveal it. (Shuffle R&D after searching it.) Add that card to HQ.", "stripped_title": "Malapert Data Vault", "text": "Whenever you score an agenda from this server, you may search R&D for 1 non-agenda card and reveal it. <em>(Shuffle R&D after searching it.)</em> Add that card to HQ.", "title": "Malapert Data Vault", "trash_cost": 4, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_corporate_troubleshooter_31049(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31049", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 1, "flavor": "Problem solved.", "illustrator": "NtscapeNavigator", "pack_code": "su21", "position": 49, "quantity": 3, "side_code": "corp", "stripped_text": "X credits, trash: Choose 1 rezzed piece of ice protecting this server. That ice gets +X strength for the remainder of the turn.", "stripped_title": "Corporate Troubleshooter", "text": "<strong>X[credit]</strong>, [trash]<strong>:</strong> Choose 1 rezzed piece of ice protecting this server. That ice gets +X strength for the remainder of the turn.", "title": "Corporate Troubleshooter", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_hokusai_grid_31059(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31059", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Director Kase hung landscapes of the Hokusai facility behind their desk. The implication was wonderful for concentrating the minds of the staff.", "illustrator": "Zoe Cohen", "keywords": "Region", "pack_code": "su21", "position": 59, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner makes a successful run on this server, do 1 net damage. Limit 1 region per server.", "stripped_title": "Hokusai Grid", "text": "Whenever the Runner makes a successful run on this server, do 1 net damage.\nLimit 1 <strong>region</strong> per server.", "title": "Hokusai Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_sansan_city_grid_31069(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31069", "cost": 6, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 3, "flavor": "The Coast is open for business.", "illustrator": "Nedliv Audiovisuell", "keywords": "Region", "pack_code": "su21", "position": 69, "quantity": 3, "side_code": "corp", "stripped_text": "Each agenda in the root of this server gets -1 advancement requirement. Limit 1 region per server.", "stripped_title": "SanSan City Grid", "text": "Each agenda in the root of this server gets -1 advancement requirement.\nLimit 1 <strong>region</strong> per server.", "title": "SanSan City Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_crisium_grid_31079(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31079", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 1, "flavor": "The Promontorium Agarum shipyards work on a scale that would be impossible in Earthgrav.", "illustrator": "NtscapeNavigator", "keywords": "Region", "pack_code": "su21", "position": 79, "quantity": 3, "side_code": "corp", "stripped_text": "Runs against this server cannot be declared successful. (This effect does not cause runs to become unsuccessful.) Limit 1 region per server.", "stripped_title": "Crisium Grid", "text": "Runs against this server cannot be declared successful. <em>(This effect does not cause runs to become unsuccessful.)</em>\nLimit 1 <strong>region</strong> per server.", "title": "Crisium Grid", "trash_cost": 5, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_vladisibirsk_city_grid_32006(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "32006", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "illustrator": "Kira L. Nguyen", "keywords": "Region", "pack_code": "msbp", "position": 6, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this upgrade. 2 hosted advancement counters: Place 2 advancement counters on another card in the root of this server that you can advance. Use this ability only once per turn. Limit 1 region per server.", "stripped_title": "Vladisibirsk City Grid", "text": "You can advance this upgrade.\n<strong>2 hosted advancement counters:</strong> Place 2 advancement counters on another card in the root of this server that you can advance. Use this ability only once per turn.\nLimit 1 <strong>region</strong> per server.", "title": "Vladisibirsk City Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_mavirus_33047(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33047", "cost": 3, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 1, "flavor": "Viruses, runners; all are food to them.", "illustrator": "Jack Reeves", "keywords": "Ambush", "pack_code": "ms", "position": 47, "quantity": 3, "side_code": "corp", "stripped_text": "While the Runner is accessing this upgrade in R&D, they must reveal it. When the Runner accesses this upgrade, you may purge virus counters. If this upgrade is rezzed, do 1 net damage. trash: Purge virus counters.", "stripped_title": "Mavirus", "text": "While the Runner is accessing this upgrade in R&D, they must reveal it.\nWhen the Runner accesses this upgrade, you may purge virus counters. If this upgrade is rezzed, do 1 net damage.\n[trash]<strong>:</strong> Purge virus counters.", "title": "Mavirus", "trash_cost": 0, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_vladisibirsk_city_grid_33056(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33056", "cost": 3, "deck_limit": 3, "faction_code": "nbn", "faction_cost": 4, "flavor": "Straddling the banks of the Ob River, this metropolis contains hope for a better tomorrow.", "illustrator": "Kira L. Nguyen", "keywords": "Region", "pack_code": "ms", "position": 56, "quantity": 3, "side_code": "corp", "stripped_text": "You can advance this upgrade. 2 hosted advancement counters: Place 2 advancement counters on another card in the root of this server that you can advance. Use this ability only once per turn. Limit 1 region per server.", "stripped_title": "Vladisibirsk City Grid", "text": "You can advance this upgrade.\n<strong>2 hosted advancement counters:</strong> Place 2 advancement counters on another card in the root of this server that you can advance. Use this ability only once per turn.\nLimit 1 <strong>region</strong> per server.", "title": "Vladisibirsk City Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_djupstad_grid_33102(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33102", "cost": 4, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 4, "flavor": "\"It\u02bcs technically above our pay grade, but we know where our weapons come from. In Djupstad they wait, deep in thought, until we call upon them.\"\n\u2014Aron Hendrik", "illustrator": "Kira L. Nguyen", "keywords": "Region", "pack_code": "ph", "position": 102, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever you score an agenda from the root of this server, do 1 core damage. Limit 1 region per server.", "stripped_title": "Djupstad Grid", "text": "Whenever you score an agenda from the root of this server, do 1 core damage.\nLimit 1 <strong>region</strong> per server.", "title": "Djupstad Grid", "trash_cost": 4, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_mr_hendrik_33103(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33103", "cost": 0, "deck_limit": 3, "faction_code": "haas-bioroid", "faction_cost": 3, "flavor": "Few employees know he exists. Even fewer know he is actually <em>three</em>.", "illustrator": "Ferenc Patk\u00f3s", "keywords": "Ambush - Sysop", "pack_code": "ph", "position": 103, "quantity": 3, "side_code": "corp", "stripped_text": "When the Runner accesses this upgrade while it is installed, you may pay 2 credits to do 1 core damage. If the Runner has any click remaining, they may lose all their click to prevent this damage.", "stripped_title": "Mr. Hendrik", "text": "When the Runner accesses this upgrade while it is installed, you may pay 2[credit] to do 1 core damage. If the Runner has any [click] remaining, they may lose all their [click] to prevent this damage.", "title": "Mr. Hendrik", "trash_cost": 2, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_nanisivik_grid_33111(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33111", "cost": 2, "deck_limit": 3, "faction_code": "jinteki", "faction_cost": 2, "flavor": "Here, at the edge of the habitable world, they extract the future from the bones of the past.", "illustrator": "Emilio Rodriguez", "keywords": "Region", "pack_code": "ph", "position": 111, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever the Runner approaches this server, you may turn 1 facedown piece of ice in Archives faceup. If you do, resolve 1 subroutine on that ice. Limit 1 region per server.", "stripped_title": "Nanisivik Grid", "text": "Whenever the Runner approaches this server, you may turn 1 facedown piece of ice in Archives faceup. If you do, resolve 1 subroutine on that ice.\nLimit 1 <strong>region</strong> per server.", "title": "Nanisivik Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_yakov_erikovich_avdakov_33126(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33126", "cost": 2, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 2, "flavor": "They say the Butcher of Siberia keeps the best cuts for himself.", "illustrator": "Dave Lee", "keywords": "Executive", "pack_code": "ph", "position": 126, "quantity": 3, "side_code": "corp", "stripped_text": "Whenever a player trashes a card (including this upgrade) from the root of this server or protecting it, except during installation, gain 2 credits.", "stripped_title": "Yakov Erikovich Avdakov", "text": "Whenever a player trashes a card <em>(including this upgrade)</em> from the root of this server or protecting it, except during installation, gain 2[credit].", "title": "Yakov Erikovich Avdakov", "trash_cost": 2, "type_code": "upgrade", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class upgrade_zato_city_grid_33127(Upgrade):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33127", "cost": 3, "deck_limit": 3, "faction_code": "weyland-consortium", "faction_cost": 4, "flavor": "Getting in is hard. Getting out requires a death certificate.", "illustrator": "Vitalii Ostaschenko", "keywords": "Region", "pack_code": "ph", "position": 127, "quantity": 3, "side_code": "corp", "stripped_text": "Remote server only. Each piece of ice protecting this server gains When the Runner encounters this ice, choose 1 subroutine on it. You may trash this ice to resolve that subroutine.. Limit 1 region per server.", "stripped_title": "ZATO City Grid", "text": "Remote server only.\nEach piece of ice protecting this server gains \"When the Runner encounters this ice, choose 1 subroutine on it. You may trash this ice to resolve that subroutine.\".\nLimit 1 <strong>region</strong> per server.", "title": "ZATO City Grid", "trash_cost": 3, "type_code": "upgrade", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                