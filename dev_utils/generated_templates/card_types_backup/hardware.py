
'''
card classes of type hardware
'''
from netrunner_lib.cards._base_card_classes import Hardware

            
class hardware_cyberfeeder_01005(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01005", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "I feel almost naked without it.", "illustrator": "Gong Studios", "keywords": "Chip", "pack_code": "core", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to pay for using icebreakers or for installing virus programs.", "stripped_title": "Cyberfeeder", "text": "1[recurring-credit]\nUse this credit to pay for using <strong>icebreakers</strong> or for installing <strong>virus</strong> programs.", "title": "Cyberfeeder", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_grimoire_01006(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01006", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"My little book of magic spells.\" -The Whizzard", "illustrator": "Jonathan Lee", "keywords": "Console", "pack_code": "core", "position": 6, "quantity": 1, "side_code": "runner", "stripped_text": "+2 mu Whenever you install a virus program, place 1 virus counter on that program. Limit 1 console per player.", "stripped_title": "Grimoire", "text": "+2[mu]\nWhenever you install a <strong>virus</strong> program, place 1 virus counter on that program.\nLimit 1 <strong>console</strong> per player.", "title": "Grimoire", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_lemuria_codecracker_01023(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01023", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "\"A little preparation goes a long way.\" -Gabriel Santiago", "illustrator": "Emerson Tung", "pack_code": "core", "position": 23, "quantity": 2, "side_code": "runner", "stripped_text": "click, 1 credit: Expose 1 card. Use this ability only if you have made a successful run on HQ this turn.", "stripped_title": "Lemuria Codecracker", "text": "[click], 1[credit]: Expose 1 card. Use this ability only if you have made a successful run on HQ this turn.", "title": "Lemuria Codecracker", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_desperado_01024(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01024", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "illustrator": "Outland Entertainment LLC", "keywords": "Console", "pack_code": "core", "position": 24, "quantity": 1, "side_code": "runner", "stripped_text": "+1 mu Gain 1 credit whenever you make a successful run. Limit 1 console per player.", "stripped_title": "Desperado", "text": "+1[mu]\nGain 1[credit] whenever you make a successful run.\nLimit 1 <strong>console</strong> per player.", "title": "Desperado", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_akamatsu_mem_chip_01038(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01038", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "The Akamatsu company was founded on three principles: first, to make the fastest mem chips on the market, second, to turn a profit, and third, to serve as a front for the manufacture of illegal neural-stimulants. It is the last principle that perhaps explains their rabid brand loyalty.", "illustrator": "Outland Entertainment LLC", "keywords": "Chip", "pack_code": "core", "position": 38, "quantity": 2, "side_code": "runner", "stripped_text": "+1 mu", "stripped_title": "Akamatsu Mem Chip", "text": "+1[mu]", "title": "Akamatsu Mem Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_rabbit_hole_01039(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01039", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "It's not endless, it just feels that way.", "illustrator": "Mark Anthony Taduran", "keywords": "Link", "pack_code": "core", "position": 39, "quantity": 2, "side_code": "runner", "stripped_text": "+1 link When Rabbit Hole is installed, you may search your stack for another copy of Rabbit Hole and install it by paying its install cost. Shuffle your stack.", "stripped_title": "Rabbit Hole", "text": "+1[link]\nWhen Rabbit Hole is installed, you may search your stack for another copy of Rabbit Hole and install it by paying its install cost. Shuffle your stack.", "title": "Rabbit Hole", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_the_personal_touch_01040(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01040", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "A z-loop here, a cortical wave there\u2026", "illustrator": "Bruno Balixa", "keywords": "Mod", "pack_code": "core", "position": 40, "quantity": 2, "side_code": "runner", "stripped_text": "Install The Personal Touch only on an icebreaker. Host icebreaker has +1 strength.", "stripped_title": "The Personal Touch", "text": "Install The Personal Touch only on an <strong>icebreaker.</strong>\nHost <strong>icebreaker</strong> has +1 strength.", "title": "The Personal Touch", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_the_toolbox_01041(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "01041", "cost": 9, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Michael Hamlett", "keywords": "Console", "pack_code": "core", "position": 41, "quantity": 1, "side_code": "runner", "stripped_text": "+2 mu +2 link 2 recurring credits Use these credits to pay for using icebreakers. Limit 1 console per player.", "stripped_title": "The Toolbox", "text": "+2[mu] +2[link]\n2[recurring-credit]\nUse these credits to pay for using <strong>icebreakers</strong>.\nLimit 1 <strong>console</strong> per player.", "title": "The Toolbox", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_spinal_modem_02002(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02002", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Gong Studios", "keywords": "Console", "pack_code": "wla", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu, 2 recurring credits You can spend hosted credits to use icebreakers. Whenever there is a successful trace during a run, suffer 1 core damage. Limit 1 console per player.", "stripped_title": "Spinal Modem", "text": "+1[mu], 2[recurring-credit]\nYou can spend hosted credits to use <strong>icebreakers</strong>.\nWhenever there is a successful trace during a run, suffer 1 core damage.\nLimit 1 <strong>console</strong> per player.", "title": "Spinal Modem", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_cortez_chip_02005(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02005", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Named after Hernando Cortez, a former Weyland technician convicted of smuggling company tech. He still collected his pension while in prison, the last beneficiary of a loophole in Weyland's standard employment contract.", "illustrator": "Mauricio Herrera", "keywords": "Chip", "pack_code": "wla", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Choose a piece of ice. The Corp must pay 2 credits as an additional cost to rez that ice until the end of the turn.", "stripped_title": "Cortez Chip", "text": "[trash]: Choose a piece of ice. The Corp must pay 2[credit] as an additional cost to rez that ice until the end of the turn.", "title": "Cortez Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_plascrete_carapace_02009(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02009", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Ralph Beisner", "keywords": "Gear", "pack_code": "wla", "position": 9, "quantity": 3, "side_code": "runner", "stripped_text": "Place 4 power counters on Plascrete Carapace when it is installed. When there are no power counters left on Plascrete Carapace, trash it. Hosted power counter: Prevent 1 meat damage.", "stripped_title": "Plascrete Carapace", "text": "Place 4 power counters on Plascrete Carapace when it is installed. When there are no power counters left on Plascrete Carapace, trash it.\n<strong>Hosted power counter:</strong> Prevent 1 meat damage.", "title": "Plascrete Carapace", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_e3_feedback_implants_02024(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02024", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "CyberSolutions' e3 line of implants trade strictly in muscle memory and autonomic responses, freeing the brain to focus entirely on cerebral tasks.", "illustrator": "Mauricio Herrera", "keywords": "Mod", "pack_code": "ta", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you break a subroutine on a piece of ice, you may pay 1 credit to break 1 subroutine on that ice.", "stripped_title": "e3 Feedback Implants", "text": "Whenever you break a subroutine on a piece of ice, you may pay 1[credit] to break 1 subroutine on that ice.", "title": "e3 Feedback Implants", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_dyson_mem_chip_02028(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02028", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Archaic but reliable.", "illustrator": "JB Casacop", "keywords": "Chip - Link", "pack_code": "ta", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu, +1 link", "stripped_title": "Dyson Mem Chip", "text": "+1[mu], +1[link]", "title": "Dyson Mem Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_muresh_bodysuit_02044(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02044", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "Light and form-fitting, its like bulletproof skin.", "illustrator": "Gong Studios", "keywords": "Gear", "pack_code": "ce", "position": 44, "quantity": 3, "side_code": "runner", "stripped_text": "Interrupt -> The first time each turn you would suffer meat damage, prevent 1 meat damage.", "stripped_title": "Muresh Bodysuit", "text": "[interrupt] \u2192 The first time each turn you would suffer meat damage, prevent 1 meat damage.", "title": "Muresh Bodysuit", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_dinosaurus_02048(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02048", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Matt Zeilinger", "keywords": "Console", "pack_code": "ce", "position": 48, "quantity": 3, "side_code": "runner", "stripped_text": "Dinosaurus can host a single non-AI icebreaker. The memory cost of the hosted icebreaker does not count against your memory limit. Hosted icebreaker has +2 strength. Limit 1 console per player.", "stripped_title": "Dinosaurus", "text": "Dinosaurus can host a single non-<strong>AI icebreaker</strong>. The memory cost of the hosted <strong>icebreaker</strong> does not count against your memory limit.\nHosted <strong>icebreaker</strong> has +2 strength.\nLimit 1 <strong>console</strong> per player.", "title": "Dinosaurus", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_doppelganger_02064(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02064", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Twice the fun.", "illustrator": "Howard Schechlman", "keywords": "Console", "pack_code": "asis", "position": 64, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Once per turn, you may immediately make another run when a successful run ends. Limit 1 console per player.", "stripped_title": "Doppelganger", "text": "+1[mu]\nOnce per turn, you may immediately make another run when a successful run ends.\nLimit 1 <strong>console</strong> per player.", "title": "Doppelg\u00e4nger", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_hq_interface_02085(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02085", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "If you don't have someone on the inside, find someone on the inside who's fond of desk ornaments.", "illustrator": "Robert Chew", "pack_code": "hs", "position": 85, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you breach HQ, access 1 additional card.", "stripped_title": "HQ Interface", "text": "Whenever you breach HQ, access 1 additional card.", "title": "HQ Interface", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_replicator_02088(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02088", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Do you really need another one?", "illustrator": "Mike Nesbitt", "pack_code": "hs", "position": 88, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you install a piece of hardware (including Replicator), you may search your stack for another copy of that hardware, reveal it, and add it your grip. Shuffle your stack.", "stripped_title": "Replicator", "text": "Whenever you install a piece of hardware (including Replicator), you may search your stack for another copy of that hardware, reveal it, and add it your grip. Shuffle your stack.", "title": "Replicator", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_rd_interface_02107(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "02107", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Works best at your own desk.", "illustrator": "Reza Ilyasa", "pack_code": "fp", "position": 107, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you breach R&D, access 1 additional card.", "stripped_title": "R&D Interface", "text": "Whenever you breach R&D, access 1 additional card.", "title": "R&D Interface", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_monolith_03036(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03036", "cost": 18, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Emilio Rodriguez", "keywords": "Console", "pack_code": "cac", "position": 36, "quantity": 3, "side_code": "runner", "stripped_text": "+3 mu When you install this hardware, install up to 3 programs from your grip, paying 4 credits less for each. Interrupt -> Trash 1 program from your grip: Prevent 1 core damage or 1 net damage. Limit 1 console per player.", "stripped_title": "Monolith", "text": "+3[mu]\nWhen you install this hardware, install up to 3 programs from your grip, paying 4[credit] less for each.\n[interrupt] \u2192 <strong>Trash 1 program from your grip:</strong> Prevent 1 core damage or 1 net damage.\nLimit 1 <strong>console</strong> per player.", "title": "Monolith", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_feedback_filter_03037(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03037", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "It still hurts, a bit, the first time. The second time, you feel nothing at all. But don't push your luck.", "illustrator": "Lili Ibrahim", "keywords": "Gear", "pack_code": "cac", "position": 37, "quantity": 3, "side_code": "runner", "stripped_text": "Interrupt -> 3 credits: Prevent 1 net damage. Interrupt -> trash: Prevent up to 2 core damage.", "stripped_title": "Feedback Filter", "text": "[interrupt] \u2192 <strong>3[credit]:</strong> Prevent 1 net damage.\n[interrupt] \u2192 <strong>[trash]:</strong> Prevent up to 2 core damage.", "title": "Feedback Filter", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_clone_chip_03038(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03038", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "It is good practice to backup the backup.", "illustrator": "Christina Davis", "keywords": "Chip", "pack_code": "cac", "position": 38, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Install a program from your heap (paying the install cost).", "stripped_title": "Clone Chip", "text": "[trash]: Install a program from your heap (paying the install cost).", "title": "Clone Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_omnidrive_03039(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "03039", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Bruno Balixa", "keywords": "Gear", "pack_code": "cac", "position": 39, "quantity": 3, "side_code": "runner", "stripped_text": "Omni-drive can host a single program of 1 mu or less. The memory cost of the hosted program does not count against your memory limit. 1 recurring credit Use this credit to pay for using the hosted program.", "stripped_title": "Omni-drive", "text": "Omni-drive can host a single program of 1[mu] or less. The memory cost of the hosted program does not count against your memory limit.\n1[recurring-credit]\nUse this credit to pay for using the hosted program.", "title": "Omni-drive", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_lockpick_04006(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04006", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"I originally designed it for someone else, but it was so useful I decided to keep it for myself.\" -Kate \"Mac\" McCaffrey", "illustrator": "Gong Studios", "keywords": "Chip - Stealth", "pack_code": "om", "position": 6, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to pay for using decoders.", "stripped_title": "Lockpick", "text": "1[recurring-credit]\nUse this credit to pay for using <strong>decoders</strong>.", "title": "Lockpick", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_record_reconstructor_04028(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04028", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"Why is data deleted? Maybe they don't want it to be found. Or maybe it's just useless. The useless data is the kind you want.\" -The Professor", "illustrator": "Lucas Durham", "pack_code": "st", "position": 28, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on Archives, instead of breaching Archives, you may add 1 faceup card from Archives to the top of R&D.", "stripped_title": "Record Reconstructor", "text": "Whenever you make a successful run on Archives, instead of breaching Archives, you may add 1 faceup card from Archives to the top of R&D.", "title": "Record Reconstructor", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_prepaid_voicepad_04029(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04029", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "A VoicePAD is a personal access device with most of its functions ripped out. Just about all it's good for is making voice-calls and managing your contacts. The only reason to even have one is for its anonymity, which for a certain kind of person is all the reason one needs.", "illustrator": "Mike Nesbitt", "keywords": "Gear", "pack_code": "st", "position": 29, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit (When you install this card and before your turn begins, refill to 1 hosted credit.) You can spend hosted credits to play events.", "stripped_title": "Prepaid VoicePAD", "text": "1[recurring-credit] <em>(When you install this card and before your turn begins, refill to 1 hosted credit.)</em>\nYou can spend hosted credits to play events.", "title": "Prepaid VoicePAD", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_deep_red_04042(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04042", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Christina Davis", "keywords": "Console", "pack_code": "mt", "position": 42, "quantity": 3, "side_code": "runner", "stripped_text": "+3 mu Use the MU on Deep Red only for Caissa programs. Whenever you install a Caissa program, you may trigger its click ability without spending click. Limit 1 console per player.", "stripped_title": "Deep Red", "text": "+3[mu]\nUse the MU on Deep Red only for <strong>Ca\u00efssa</strong> programs.\nWhenever you install a <strong>Ca\u00efssa</strong> program, you may trigger its [click] ability without spending [click].\nLimit 1 <strong>console</strong> per player.", "title": "Deep Red", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_llds_processor_04066(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04066", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "LLDS Unlimited was born the day two designers answered the question \"Why doesn't anyone make Diesel for computers?\"", "illustrator": "Gong Studios", "keywords": "Chip", "pack_code": "tc", "position": 66, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you install an icebreaker, that icebreaker has +1 strength until the end of the turn.", "stripped_title": "LLDS Processor", "text": "Whenever you install an <strong>icebreaker</strong>, that <strong>icebreaker</strong> has +1 strength until the end of the turn.", "title": "LLDS Processor", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_capstone_04068(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04068", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"Once you have achieved perfection, what's next?\" -The Professor", "illustrator": "Jason Rumpff", "pack_code": "tc", "position": 68, "quantity": 3, "side_code": "runner", "stripped_text": "click: Trash any number of cards from your grip. For each trashed card of which you have another copy installed, draw 1 card.", "stripped_title": "Capstone", "text": "[click]: Trash any number of cards from your grip. For each trashed card of which you have another copy installed, draw 1 card.", "title": "Capstone", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_blackguard_04085(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04085", "cost": 11, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "The power of the focused mind is a power beyond comprehension.", "illustrator": "Smirtouille", "keywords": "Console", "pack_code": "fal", "position": 85, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu Whenever you expose a card, the Corp must rez it by paying its rez cost, if able. Limit 1 console per player.", "stripped_title": "Blackguard", "text": "+2[mu]\nWhenever you expose a card, the Corp must rez it by paying its rez cost, if able.\nLimit 1 <strong>console</strong> per player.", "title": "Blackguard", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_cybersolutions_mem_chip_04086(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04086", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"CyberSolutions is a boring name for a company that makes pretty exciting products. Their memory chips have some pretty tricky stuff going on inside and I keep hearing good things about their M/MI implants. I even heard they were on the path to their own androids about a year ago. I wonder whatever happened with that?\" -Kate \"Mac\" McCaffrey", "illustrator": "Gong Studios", "keywords": "Chip", "pack_code": "fal", "position": 86, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu", "stripped_title": "CyberSolutions Mem Chip", "text": "+2[mu]", "title": "CyberSolutions Mem Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_dyson_fractal_generator_04103(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04103", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "The Dyson Fractal Generator is a useless lump of silicon; all it does is produce truly random results. What kind of madman slaps that in his rig? What's the use of a totally random number? -John Masanori", "illustrator": "Gong Studios", "keywords": "Chip - Stealth", "pack_code": "dt", "position": 103, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to pay for using fracters.", "stripped_title": "Dyson Fractal Generator", "text": "1[recurring-credit]\nUse this credit to pay for using <strong>fracters</strong>.", "title": "Dyson Fractal Generator", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_silencer_04104(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "04104", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Take Moore's Law, iterate it over a century or two, and mix in quantum computing. You get to the point where you're developing the software on a hardware platform that you design at the same time. Tailor-made for each other. Exciting time to be alive! -William Knuth, The Tower of Babbage", "illustrator": "Gong Studios", "keywords": "Chip - Stealth", "pack_code": "dt", "position": 104, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to pay for using killers.", "stripped_title": "Silencer", "text": "1[recurring-credit]\nUse this credit to pay for using <strong>killers</strong>.", "title": "Silencer", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_logos_05037(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05037", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Agri Karuniawan", "keywords": "Console", "pack_code": "hap", "position": 37, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Your maximum hand size is increased by 1. Whenever the Corp scores an agenda, you may search your stack for a card and add it to your grip. Shuffle your stack. Limit 1 console per player.", "stripped_title": "Logos", "text": "+1[mu]\nYour maximum hand size is increased by 1.\nWhenever the Corp scores an agenda, you may search your stack for a card and add it to your grip. Shuffle your stack.\nLimit 1 <strong>console</strong> per player.", "title": "Logos", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_public_terminal_05038(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05038", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Express loved libraries. The consoles were weak, but the security even weaker. He wirelessly loaded up his personal blend of code and started cloning the drive. In just a few minutes, another zombie would claw its way to the surface of cyberspace.", "illustrator": "Emilio Rodriguez", "pack_code": "hap", "position": 38, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to play run events.", "stripped_title": "Public Terminal", "text": "1[recurring-credit]\nUse this credit to play <strong>run</strong> events.", "title": "Public Terminal", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_unregistered_sw_35_05039(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05039", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "illustrator": "Gong Studios", "keywords": "Weapon", "pack_code": "hap", "position": 39, "quantity": 3, "side_code": "runner", "stripped_text": "Use this hardware only if you have made a successful run on HQ this turn. click click: Trash 1 rezzed bioroid, clone, executive, or sysop in the root of a remote server.", "stripped_title": "Unregistered S&W '35", "text": "Use this hardware only if you have made a successful run on HQ this turn.\n<strong>[click][click]:</strong> Trash 1 rezzed <strong>bioroid</strong>, <strong>clone</strong>, <strong>executive</strong>, or <strong>sysop</strong> in the root of a remote server.", "title": "Unregistered S&W '35", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_window_05040(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05040", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "The grass looked greener on the other side of the tear. But it always did, and there was always another tear.", "illustrator": "Seage", "pack_code": "hap", "position": 40, "quantity": 3, "side_code": "runner", "stripped_text": "click: Draw 1 card from the bottom of your stack.", "stripped_title": "Window", "text": "[click]: Draw 1 card from the bottom of your stack.", "title": "Window", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_qcoherence_chip_05052(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "05052", "cost": 0, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "One of the core problems of quantum computing is isolating the system from external factors to prevent decoherence. The Q-Coherence Chip is one, imperfect, solution.", "illustrator": "Gong Studios", "keywords": "Chip", "pack_code": "hap", "position": 52, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu When an installed program is trashed, trash this hardware.", "stripped_title": "Q-Coherence Chip", "text": "+1[mu]\nWhen an installed program is trashed, trash this hardware.", "title": "Q-Coherence Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_boxe_06055(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06055", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Aaron Agregado", "keywords": "Console", "pack_code": "fc", "position": 55, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu Your maximum hand size is increased by 2. Limit 1 console per player.", "stripped_title": "Box-E", "text": "+2[mu]\nYour maximum hand size is increased by 2.\nLimit 1 <strong>console</strong> per player.", "title": "Box-E", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_autoscripter_06076(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06076", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "It practically runs itself, unless you're in a pinch.", "illustrator": "Lucas Durham", "pack_code": "uao", "position": 76, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you install a program from your grip during your turn, gain click. Trash Autoscripter if you make an unsuccessful run.", "stripped_title": "Autoscripter", "text": "The first time you install a program from your grip during your turn, gain [click].\nTrash Autoscripter if you make an unsuccessful run.", "title": "Autoscripter", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_astrolabe_06079(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06079", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"There is no better tool for charting the empty spaces of the net.\" -Nasir Meidan", "illustrator": "Gong Studios", "keywords": "Console", "pack_code": "uao", "position": 79, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Draw 1 card whenever the Corp creates a server. Limit 1 console per player.", "stripped_title": "Astrolabe", "text": "+1[mu]\nDraw 1 card whenever the Corp creates a server.\nLimit 1 <strong>console</strong> per player.", "title": "Astrolabe", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_ekomind_06093(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06093", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"Sometimes you just need a brain in a jar.\" -g00ru", "illustrator": "Lorraine Schleter", "keywords": "Console", "pack_code": "atr", "position": 93, "quantity": 3, "side_code": "runner", "stripped_text": "Your memory limit is equal to the number of cards in your grip. Limit 1 console per player.", "stripped_title": "Ekomind", "text": "Your memory limit is equal to the number of cards in your grip.\nLimit 1 <strong>console</strong> per player.", "title": "Ekomind", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_cybsoft_macrodrive_06098(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "06098", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "Cybsoft started by designing games. Eventually they just redesigned the same game each year, and to combat piracy created a dedicated machine to play it. Profits grew ten-fold.", "illustrator": "Gong Studios", "pack_code": "atr", "position": 98, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to install programs.", "stripped_title": "Cybsoft MacroDrive", "text": "1[recurring-credit]\nUse this credit to install programs.", "title": "Cybsoft MacroDrive", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_archives_interface_07044(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07044", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "A black box that makes data disappear forever.", "illustrator": "Maciej Rebisz", "pack_code": "oac", "position": 44, "quantity": 3, "side_code": "runner", "stripped_text": "Interrupt -> Whenever you would access a card in Archives, you may instead remove it from the game. Use this ability only once each time you breach Archives.", "stripped_title": "Archives Interface", "text": "[interrupt] \u2192 Whenever you would access a card in Archives, you may instead remove it from the game. Use this ability only once each time you breach Archives.", "title": "Archives Interface", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_chop_bot_3000_07045(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07045", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "There was a sickly smell coming from his closet. He hoped it was only a mouse this time.", "illustrator": "Maciej Rebisz", "pack_code": "oac", "position": 45, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may trash another of your installed cards. If you do, draw 1 card or remove 1 tag.", "stripped_title": "Chop Bot 3000", "text": "When your turn begins, you may trash another of your installed cards. If you do, draw 1 card or remove 1 tag.", "title": "Chop Bot 3000", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_memstrips_07046(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07046", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"The trick is remembering which virus you loaded onto which strip. That's why I draw emoji on 'em. Then I just have to remember which emoji stands for which virus.\" -Princess Space Kitten", "illustrator": "Maciej Rebisz", "keywords": "Chip", "pack_code": "oac", "position": 46, "quantity": 3, "side_code": "runner", "stripped_text": "+3 mu Use the MU on MemStrips only for virus programs.", "stripped_title": "MemStrips", "text": "+3[mu]\nUse the MU on MemStrips only for <strong>virus</strong> programs.", "title": "MemStrips", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_vigil_07047(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07047", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"Show me your faith without deeds, if you can.\"", "illustrator": "Lili Ibrahim", "keywords": "Console", "pack_code": "oac", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu When your turn begins, if the Corp has cards in HQ equal to their maximum hand size, draw 1 card. Limit 1 console per player.", "stripped_title": "Vigil", "text": "+1[mu]\nWhen your turn begins, if the Corp has cards in HQ equal to their maximum hand size, draw 1 card.\nLimit 1 <strong>console</strong> per player.", "title": "Vigil", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_qianju_pt_07054(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "07054", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"By the time you add in all of the options, you've spent about three times the base price. Of course, a lot of the systems are supposed to make you safer - if you can keep track of them.\"", "illustrator": "Carolina Eade", "keywords": "Vehicle", "pack_code": "oac", "position": 54, "quantity": 3, "side_code": "runner", "stripped_text": "When your turn begins, you may lose click. If you do, prevent the first tag you would take until your next turn begins.", "stripped_title": "Qianju PT", "text": "When your turn begins, you may lose [click]. If you do, prevent the first tag you would take until your next turn begins.", "title": "Qianju PT", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_dorm_computer_08024(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08024", "cost": 0, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Lucas Durham", "pack_code": "bb", "position": 24, "quantity": 3, "side_code": "runner", "stripped_text": "Place 4 power counters on Dorm Computer when you install it. click, hosted power counter: Make a run. Avoid all tags for the remainder of the run.", "stripped_title": "Dorm Computer", "text": "Place 4 power counters on Dorm Computer when you install it.\n[click], <strong>hosted power counter:</strong> Make a run. Avoid all tags for the remainder of the run.", "title": "Dorm Computer", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_comet_08027(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08027", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Del Borovic", "keywords": "Console", "pack_code": "bb", "position": 27, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu The first time you play an event each turn, you may play another event (without spending a click) after the first one resolves. Limit 1 console per player.", "stripped_title": "Comet", "text": "+1[mu]\nThe first time you play an event each turn, you may play another event (without spending a click) after the first one resolves.\nLimit 1 <strong>console</strong> per player.", "title": "Comet", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_skulljack_08042(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08042", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "The implanted brain-machine interface, or \"skulljack,\" is the single most common cybernetic enhancement that isn't a medical necessity.", "illustrator": "Aaron Agregado", "keywords": "Cybernetic", "pack_code": "cc", "position": 42, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, suffer 1 core damage. The trash cost of each Corp card is lowered by 1.", "stripped_title": "Skulljack", "text": "When you install this hardware, suffer 1 core damage.\nThe trash cost of each Corp card is lowered by 1.", "title": "Skulljack", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_turntable_08043(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08043", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Sara K. Diesel", "keywords": "Console", "pack_code": "cc", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Whenever you steal an agenda, you may swap that agenda with an agenda in the Corp's score area. Limit 1 console per player.", "stripped_title": "Turntable", "text": "+1[mu]\nWhenever you steal an agenda, you may swap that agenda with an agenda in the Corp's score area.\nLimit 1 <strong>console</strong> per player.", "title": "Turntable", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_titanium_ribs_08045(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08045", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Matt Zeilinger", "keywords": "Cybernetic", "pack_code": "cc", "position": 45, "quantity": 3, "side_code": "runner", "stripped_text": "When you install Titanium Ribs, suffer 2 meat damage. You choose the card(s) from your grip to trash whenever you take damage (including the damage taken by installing Titanium Ribs).", "stripped_title": "Titanium Ribs", "text": "When you install Titanium Ribs, suffer 2 meat damage.\nYou choose the card(s) from your grip to trash whenever you take damage (including the damage taken by installing Titanium Ribs).", "title": "Titanium Ribs", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_netready_eyes_08047(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08047", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Ethan Patrick Harris", "keywords": "Cybernetic", "pack_code": "cc", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "When you install Net-Ready Eyes, suffer 2 meat damage. Whenever you initiate a run, choose an icebreaker. That icebreaker has +1 strength for the remainder of the run.", "stripped_title": "Net-Ready Eyes", "text": "When you install Net-Ready Eyes, suffer 2 meat damage.\nWhenever you initiate a run, choose an <strong>icebreaker</strong>. That <strong>icebreaker</strong> has +1 strength for the remainder of the run.", "title": "Net-Ready Eyes", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_brain_cage_08049(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08049", "cost": 1, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "The skull is not one bone, but 22. The surgery is even more complex than it sounds.", "illustrator": "Mike Nesbitt", "keywords": "Cybernetic", "pack_code": "cc", "position": 49, "quantity": 3, "side_code": "runner", "stripped_text": "You get +3 maximum hand size. When you install this hardware, suffer 1 core damage.", "stripped_title": "Brain Cage", "text": "You get +3 maximum hand size.\nWhen you install this hardware, suffer 1 core damage.", "title": "Brain Cage", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_forger_08065(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08065", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "Using the exact same rig as a million other people is just another form of security through anonymity.", "illustrator": "Lili Ibrahim", "keywords": "Console", "pack_code": "uw", "position": 65, "quantity": 3, "side_code": "runner", "stripped_text": "+1 link Interrupt -> trash: Prevent 1 tag. trash: Remove 1 tag. Limit 1 console per player.", "stripped_title": "Forger", "text": "+1[link]\n[interrupt] \u2192 <strong>[trash]:</strong> Prevent 1 tag.\n<strong>[trash]:</strong> Remove 1 tag.\nLimit 1 <strong>console</strong> per player.", "title": "Forger", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_bookmark_08106(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "08106", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Bruno Balixa", "pack_code": "uot", "position": 106, "quantity": 3, "side_code": "runner", "stripped_text": "click: Host up to 3 cards from your grip facedown on this hardware (you may look at these cards at any time). click: Add all hosted cards to your grip. trash: Add all hosted cards to your grip.", "stripped_title": "Bookmark", "text": "<strong>[click]:</strong> Host up to 3 cards from your grip facedown on this hardware <em>(you may look at these cards at any time)</em>.\n<strong>[click]:</strong> Add all hosted cards to your grip.\n<strong>[trash]:</strong> Add all hosted cards to your grip.", "title": "Bookmark", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_heartbeat_09032(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09032", "cost": 2, "deck_limit": 3, "faction_code": "apex", "faction_cost": 3, "flavor": "\"Meantime the hellish tattoo of the heart increased. It grew quicker and quicker, and louder and louder every instant.\" -Edgar Allan Poe", "illustrator": "Thomas Williams", "keywords": "Console", "pack_code": "dad", "position": 32, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Trash an installed card: Prevent 1 damage. Limit 1 console per player.", "stripped_title": "Heartbeat", "text": "+1[mu]\n<strong>Trash an installed card:</strong> Prevent 1 damage.\nLimit 1 <strong>console</strong> per player.", "title": "Heartbeat", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_brain_chip_09039(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09039", "cost": 2, "deck_limit": 3, "faction_code": "adam", "faction_cost": 3, "illustrator": "Jessada Sutthi", "keywords": "Console", "pack_code": "dad", "position": 39, "quantity": 3, "side_code": "runner", "stripped_text": "+X mu Your maximum hand size is increased by X. X is equal to the number of agenda points you have. Limit 1 console per player.", "stripped_title": "Brain Chip", "text": "+X[mu]\nYour maximum hand size is increased by X.\nX is equal to the number of agenda points you have.\nLimit 1 <strong>console</strong> per player.", "title": "Brain Chip", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_security_chip_09046(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09046", "cost": 0, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 1, "flavor": "Fortunately, Globalsec buys them by the case.", "illustrator": "Lucas Durham", "keywords": "Chip", "pack_code": "dad", "position": 46, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Choose an icebreaker (or any number of cloud icebreakers). Each chosen icebreaker has +1 strength for each link you have for the remainder of this run. Use this ability only during a run.", "stripped_title": "Security Chip", "text": "[trash]: Choose an <strong>icebreaker</strong> (or any number of <strong>cloud icebreakers</strong>). Each chosen <strong>icebreaker</strong> has +1 strength for each [link] you have for the remainder of this run. Use this ability only during a run.", "title": "Security Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_security_nexus_09047(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "09047", "cost": 8, "deck_limit": 3, "faction_code": "sunny-lebeau", "faction_cost": 3, "illustrator": "Lili Ibrahim", "keywords": "Console", "pack_code": "dad", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu +1 link Once per turn, when you encounter a piece of ice, you may force the Corp to \"Trace[5]. If successful, give the Runner 1 tag and end the run. If unsuccessful, the Runner bypasses the currently encountered ice.\" Limit 1 console per player.", "stripped_title": "Security Nexus", "text": "+1[mu] +1[link]\nOnce per turn, when you encounter a piece of ice, you may force the Corp to \"Trace[5]. If successful, give the Runner 1 tag and end the run. If unsuccessful, the Runner bypasses the currently encountered ice.\"\nLimit 1 <strong>console</strong> per player.", "title": "Security Nexus", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_ramujanreliant_550_bmi_10002(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10002", "cost": 1, "deck_limit": 6, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Kate Laird", "keywords": "Consumer-grade", "pack_code": "kg", "position": 2, "quantity": 6, "side_code": "runner", "stripped_text": "Interrupt -> trash: Prevent up to X core damage or net damage. Trash cards from the top of your stack equal to the amount of damage prevented. X is equal to the number of other installed copies of Ramujan-reliant 550 BMI plus 1. Limit 6 per deck.", "stripped_title": "Ramujan-reliant 550 BMI", "text": "[interrupt] \u2192 [trash]<strong>:</strong> Prevent up to X core damage or net damage. Trash cards from the top of your stack equal to the amount of damage prevented. X is equal to the number of other installed copies of Ramujan-reliant 550 BMI plus 1.\nLimit 6 per deck.", "title": "Ramujan-reliant 550 BMI", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_maya_10007(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10007", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Adam Schumpert", "keywords": "Console", "pack_code": "kg", "position": 7, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu Once per turn, immediately after you access a card from R&D, you may add that card to the bottom of R&D. If you do, take 1 tag. Limit 1 console per player.", "stripped_title": "Maya", "text": " +2[mu]\nOnce per turn, immediately after you access a card from R&D, you may add that card to the bottom of R&D. If you do, take 1 tag.\nLimit 1 <strong>console</strong> per player.", "title": "Maya", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_emp_device_10020(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10020", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "\"No! Don't set that off HERE!\"", "illustrator": "Maciej Rebisz", "keywords": "Weapon", "pack_code": "bf", "position": 20, "quantity": 3, "side_code": "runner", "stripped_text": "trash: The Corp cannot rez more than 1 piece of ice for the remainder of this run. Use this ability only during a run.", "stripped_title": "EMP Device", "text": "[trash]: The Corp cannot rez more than 1 piece of ice for the remainder of this run. Use this ability only during a run.", "title": "EMP Device", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_netchip_10024(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10024", "cost": 1, "deck_limit": 6, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Mike Nesbitt", "keywords": "Consumer-grade - Chip", "pack_code": "bf", "position": 24, "quantity": 6, "side_code": "runner", "stripped_text": "NetChip can host a program with a memory cost less than or equal to the number of copies of NetChip installed. The memory cost of the hosted program does not count against your memory limit. Limit 6 per deck.", "stripped_title": "NetChip", "text": "NetChip can host a program with a memory cost less than or equal to the number of copies of NetChip installed. The memory cost of the hosted program does not count against your memory limit.\nLimit 6 per deck.", "title": "NetChip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_reflection_10041(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10041", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"I'm on a need-to-know basis. I need to know everything.\" -Nero Severn", "illustrator": "Maciej Rebisz", "keywords": "Console", "pack_code": "dag", "position": 41, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu +1 link Whenever you jack out, the Corp reveals 1 card from HQ at random. Limit 1 console per player.", "stripped_title": "Reflection", "text": " +1[mu] +1[link]\nWhenever you jack out, the Corp reveals 1 card from HQ at random.\nLimit 1 <strong>console</strong> per player.", "title": "Reflection", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_spy_camera_10042(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10042", "cost": 0, "deck_limit": 6, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Lucas Durham", "keywords": "Consumer-grade", "pack_code": "dag", "position": 42, "quantity": 6, "side_code": "runner", "stripped_text": "click: Look at the top X cards of your stack and arrange them in any order. X is the number of copies of Spy Camera installed. trash: Look at the top card of R&D. Limit 6 per deck.", "stripped_title": "Spy Camera", "text": "[click]: Look at the top X cards of your stack and arrange them in any order. X is the number of copies of Spy Camera installed.\n[trash]: Look at the top card of R&D.\nLimit 6 per deck.", "title": "Spy Camera", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_sports_hopper_10064(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "10064", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "\"Check out my new ride.\" -2xTiger", "illustrator": "BalanceSheet", "keywords": "Vehicle", "pack_code": "si", "position": 64, "quantity": 3, "side_code": "runner", "stripped_text": "+1 link trash: Draw 3 cards.", "stripped_title": "Sports Hopper", "text": " +1[link]\n[trash]: Draw 3 cards.", "title": "Sports Hopper", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_gpi_net_tap_11003(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11003", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Sometimes the itsy-bitsy data is most important.", "illustrator": "Alexandr Elichev", "pack_code": "23s", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you approach a piece of ice, you may expose it. You may then trash GPI Net Tap to jack out.", "stripped_title": "GPI Net Tap", "text": "Whenever you approach a piece of ice, you may expose it. You may then trash GPI Net Tap to jack out.", "title": "GPI Net Tap", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_mirror_11005(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11005", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Kathryn Steele", "keywords": "Console", "pack_code": "23s", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu Whenever you make a successful run on R&D, you may replace 1 spent recurring credit. Limit 1 console per player.", "stripped_title": "Mirror", "text": "+2[mu]\nWhenever you make a successful run on R&D, you may replace 1 spent recurring credit.\nLimit 1 <strong>console</strong> per player.", "title": "Mirror", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_obelus_11041(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11041", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Jenn Tran", "keywords": "Console", "pack_code": "es", "position": 41, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu You get +1 maximum hand size for each tag you have. The first time each turn a successful run on HQ or R&D ends, draw 1 card for each time you accessed a card during that run. Limit 1 console per player.", "stripped_title": "Obelus", "text": "+1[mu]\nYou get +1 maximum hand size for each tag you have.\nThe first time each turn a successful run on HQ or R&D ends, draw 1 card for each time you accessed a card during that run.\nLimit 1 <strong>console</strong> per player.", "title": "Obelus", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_the_gauntlet_11063(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11063", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "illustrator": "Del Borovic", "keywords": "Console", "pack_code": "in", "position": 63, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu Whenever you breach HQ during a run, access 1 additional card for each piece of ice protecting HQ that you fully broke during that run. Limit 1 console per player.", "stripped_title": "The Gauntlet", "text": "+2[mu]\nWhenever you breach HQ during a run, access 1 additional card for each piece of ice protecting HQ that you fully broke during that run.\nLimit 1 <strong>console</strong> per player.", "title": "The Gauntlet", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_top_hat_11067(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11067", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"I usually find something interesting in there. Just not what I was looking for.\"", "illustrator": "John Ariosa", "pack_code": "in", "position": 67, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you make a successful run on R&D, instead of breaching R&D, you may choose 1 of the top 5 cards in R&D and access it.", "stripped_title": "Top Hat", "text": "Whenever you make a successful run on R&D, instead of breaching R&D, you may choose 1 of the top 5 cards in R&D and access it.", "title": "Top Hat", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_sifr_11101(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11101", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "illustrator": "Yog Joshi", "keywords": "Console", "pack_code": "qu", "position": 101, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu Once per turn, when you encounter a piece of ice, you may reduce your maximum hand size by 1 until the beginning of your next turn. If you do, the strength of that ice is lowered to 0 for the remainder of the encounter. Limit 1 console per player.", "stripped_title": "Sifr", "text": "+2[mu]\nOnce per turn, when you encounter a piece of ice, you may reduce your maximum hand size by 1 until the beginning of your next turn. If you do, the strength of that ice is lowered to 0 for the remainder of the encounter.\nLimit 1 <strong>console</strong> per player.", "title": "\u015eifr", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_recon_drone_11103(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "11103", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"A little birdie told me...\" -Khan", "illustrator": "Matt Zeilinger", "pack_code": "qu", "position": 103, "quantity": 3, "side_code": "runner", "stripped_text": "X credits,trash: Prevent X damage from a card currently being accessed.", "stripped_title": "Recon Drone", "text": "X[credit],[trash]: Prevent X damage from a card currently being accessed.", "title": "Recon Drone", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_maw_12002(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12002", "cost": 6, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Console", "pack_code": "dc", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu The first time each turn you access a card not in Archives and do not steal or trash it, the Corp must trash 1 card from HQ at random. Limit 1 console per player.", "stripped_title": "Maw", "text": "+2[mu]\nThe first time each turn you access a card not in Archives and do not steal or trash it, the Corp must trash 1 card from HQ at random.\nLimit 1 <strong>console</strong> per player.", "title": "Maw", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_severnius_stim_implant_12021(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12021", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 4, "flavor": "\"Sure, the implantation was fine, but it pumps Burn. Did you think it wouldn't hurt?\"", "illustrator": "Marius Bota", "keywords": "Cybernetic", "pack_code": "so", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "click: Trash 2 or more cards from your grip. Run HQ or R&D. Whenever you breach that server during this run, access 1 additional card for every 2 cards you trashed.", "stripped_title": "Severnius Stim Implant", "text": "<strong>[click]:</strong> Trash 2 or more cards from your grip. Run HQ or R&D. Whenever you breach that server during this run, access 1 additional card for every 2 cards you trashed.", "title": "Severnius Stim Implant", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_rubicon_switch_12043(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12043", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Even I don't know how or why this one works. I just copied the schematics from a burst broadcast from someplace north of Paxton's Node, where nothing is supposed to be.\" -Los", "illustrator": "Kathryn Steele", "pack_code": "eas", "position": 43, "quantity": 3, "side_code": "runner", "stripped_text": "click, X credits: Derez 1 piece of ice with printed rez cost X credits that was rezzed this turn. Use this ability only once per turn.", "stripped_title": "Rubicon Switch", "text": "<strong>[click]</strong>, <strong>X[credit]:</strong> Derez 1 piece of ice with printed rez cost X[credit] that was rezzed this turn. Use this ability only once per turn.", "title": "Rubicon Switch", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_adjusted_matrix_12046(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12046", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"Who said you can't teach an old breaker new tricks?\" -g00ru", "illustrator": "Kathryn Steele", "keywords": "Mod", "pack_code": "eas", "position": 46, "quantity": 3, "side_code": "runner", "stripped_text": "Install only on an icebreaker. Host icebreaker gains AI and \"Interface -> Lose click: Break 1 subroutine.\"", "stripped_title": "Adjusted Matrix", "text": "Install only on an <strong>icebreaker</strong>.\nHost <strong>icebreaker</strong> gains <strong>AI</strong> and \"Interface \u2192 <strong>Lose [click]:</strong> Break 1 subroutine.\"", "title": "Adjusted Matrix", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_dedicated_processor_12047(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12047", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Better, Faster, Stronger", "illustrator": "Jason Juta", "keywords": "Mod", "pack_code": "eas", "position": 47, "quantity": 3, "side_code": "runner", "stripped_text": "Install Dedicated Processor on a non-AI icebreaker. Host icebreaker gains \"2 credits: +4 strength.\"", "stripped_title": "Dedicated Processor", "text": "Install Dedicated Processor on a non-<strong>AI icebreaker</strong>.\nHost <strong>icebreaker</strong> gains \"2[credit]: +4 strength.\"", "title": "Dedicated Processor", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_maui_12063(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12063", "cost": 5, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Matt Bradbury", "keywords": "Console", "pack_code": "baw", "position": 63, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu X recurring credits Use these credits during runs on HQ. X is the number of pieces of ice protecting HQ. Limit 1 console per player.", "stripped_title": "Maui", "text": "+2[mu]\nX[recurring-credit]\nUse these credits during runs on HQ. X is the number of pieces of ice protecting HQ.\nLimit 1 <strong>console</strong> per player.", "title": "M\u0101ui", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_daredevil_12066(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12066", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "\"Taking risks is what makes it fun!\" -Kabonesa Wu", "illustrator": "Ed Mattinian", "keywords": "Console", "pack_code": "baw", "position": 66, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu The first time you initiate a run on a server protected by 2 or more pieces of ice each turn, draw 2 cards. Limit 1 console per player.", "stripped_title": "Daredevil", "text": "+2[mu]\nThe first time you initiate a run on a server protected by 2 or more pieces of ice each turn, draw 2 cards.\nLimit 1 <strong>console</strong> per player.", "title": "Daredevil", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_respirocytes_12102(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "12102", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Alexandr Elichev", "keywords": "Cybernetic", "pack_code": "cd", "position": 102, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, suffer 1 meat damage. The first time each turn you have no cards in your grip, draw 1 card and place 1 power counter on this hardware. When this hardware has 3 or more hosted power counters, trash it.", "stripped_title": "Respirocytes", "text": "When you install this hardware, suffer 1 meat damage.\nThe first time each turn you have no cards in your grip, draw 1 card and place 1 power counter on this hardware.\nWhen this hardware has 3 or more hosted power counters, trash it.", "title": "Respirocytes", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_polyhistor_13005(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13005", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "illustrator": "BalanceSheet", "keywords": "Console", "pack_code": "td", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu, +1 link The first time each turn you pass all of the ice protecting HQ, you may draw 1 card to force the Corp to draw 1 card. Limit 1 console per player.", "stripped_title": "Polyhistor", "text": "+1[mu], +1[link]\nThe first time each turn you pass all of the ice protecting HQ, you may draw 1 card to force the Corp to draw 1 card.\nLimit 1 <strong>console</strong> per player.", "title": "Polyhistor", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_llds_memory_diamond_13015(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13015", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "It is not literally made of diamonds, but it is worth several times its weight in them.", "illustrator": "Wenjuinn Png", "keywords": "Mod", "pack_code": "td", "position": 15, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu, +1 link Your maximum hand size is increased by 1.", "stripped_title": "LLDS Memory Diamond", "text": "+1[mu], +1[link]\nYour maximum hand size is increased by 1.", "title": "LLDS Memory Diamond", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_ubax_13016(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "13016", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"It is more than just a 'pretty nanite plant'. It's a complex synthetic intelligent distributed network, and a VERY pretty nanite plant.\" - Bios", "illustrator": "Andreas Zafiratos", "keywords": "Console", "pack_code": "td", "position": 16, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu When your turn begins, draw 1 card. Limit 1 console per player.", "stripped_title": "Ubax", "text": "+1[mu]\nWhen your turn begins, draw 1 card.\nLimit 1 <strong>console</strong> per player.", "title": "Ubax", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_bmi_buffer_14020(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "14020", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Timur Shevtsov", "pack_code": "tdc", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever a program is trashed from your grip, host it on BMI Buffer instead of adding it to your heap. click click: Install 1 hosted program (paying all costs).", "stripped_title": "BMI Buffer", "text": "Whenever a program is trashed from your grip, host it on BMI Buffer instead of adding it to your heap.\n[click][click]: Install 1 hosted program (paying all costs).", "title": "BMI Buffer", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_bmi_buffer_2_14021(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "14021", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "illustrator": "Timur Shevtsov", "pack_code": "tdc", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever a program is trashed from your grip, host it on BMI Buffer instead of adding it to your heap. click click: Install 1 hosted program, ignoring all costs.", "stripped_title": "BMI Buffer 2", "text": "Whenever a program is trashed from your grip, host it on BMI Buffer instead of adding it to your heap.\n[click][click]: Install 1 hosted program, ignoring all costs.", "title": "BMI Buffer 2", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_cyberfeeder_20006(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20006", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "I feel almost naked without it.", "illustrator": "Gong Studios", "keywords": "Chip", "pack_code": "core2", "position": 6, "quantity": 2, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to pay for using icebreakers or for installing virus programs.", "stripped_title": "Cyberfeeder", "text": "1[recurring-credit]\nUse this credit to pay for using <strong>icebreakers</strong> or for installing <strong>virus</strong> programs.", "title": "Cyberfeeder", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_spinal_modem_20007(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20007", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Gong Studios", "keywords": "Console", "pack_code": "core2", "position": 7, "quantity": 2, "side_code": "runner", "stripped_text": "+1 mu, 2 recurring credits You can spend hosted credits to use icebreakers. Whenever there is a successful trace during a run, suffer 1 core damage. Limit 1 console per player.", "stripped_title": "Spinal Modem", "text": "+1[mu], 2[recurring-credit]\nYou can spend hosted credits to use <strong>icebreakers</strong>.\nWhenever there is a successful trace during a run, suffer 1 core damage.\nLimit 1 <strong>console</strong> per player.", "title": "Spinal Modem", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_doppelganger_20025(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20025", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Twice the fun.", "illustrator": "Steve Hamilton", "keywords": "Console", "pack_code": "core2", "position": 25, "quantity": 2, "side_code": "runner", "stripped_text": "+1 mu Once per turn, you may immediately make another run when a successful run ends. Limit 1 console per player.", "stripped_title": "Doppelganger", "text": "+1[mu]\nOnce per turn, you may immediately make another run when a successful run ends.\nLimit 1 <strong>console</strong> per player.", "title": "Doppelg\u00e4nger", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_hq_interface_20026(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20026", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "If you don't have someone on the inside, find someone on the inside who's fond of desk ornaments.", "illustrator": "Robert Chew", "pack_code": "core2", "position": 26, "quantity": 1, "side_code": "runner", "stripped_text": "Whenever you breach HQ, access 1 additional card.", "stripped_title": "HQ Interface", "text": "Whenever you breach HQ, access 1 additional card.", "title": "HQ Interface", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_dinosaurus_20045(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20045", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Matt Zeilinger", "keywords": "Console", "pack_code": "core2", "position": 45, "quantity": 2, "side_code": "runner", "stripped_text": "Dinosaurus can host a single non-AI icebreaker. The memory cost of the hosted icebreaker does not count against your memory limit. Hosted icebreaker has +2 strength. Limit 1 console per player.", "stripped_title": "Dinosaurus", "text": "Dinosaurus can host a single non-<strong>AI icebreaker</strong>. The memory cost of the hosted <strong>icebreaker</strong> does not count against your memory limit.\nHosted <strong>icebreaker</strong> has +2 strength.\nLimit 1 <strong>console</strong> per player.", "title": "Dinosaurus", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_rabbit_hole_20046(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20046", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "It's not endless, it just feels that way.", "illustrator": "Mark Anthony Taduran", "keywords": "Link", "pack_code": "core2", "position": 46, "quantity": 2, "side_code": "runner", "stripped_text": "+1 link When Rabbit Hole is installed, you may search your stack for another copy of Rabbit Hole and install it by paying its install cost. Shuffle your stack.", "stripped_title": "Rabbit Hole", "text": "+1[link]\nWhen Rabbit Hole is installed, you may search your stack for another copy of Rabbit Hole and install it by paying its install cost. Shuffle your stack.", "title": "Rabbit Hole", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_the_personal_touch_20047(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20047", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "A z-loop here, a cortical wave there\u2026", "illustrator": "Aurore Folny", "keywords": "Mod", "pack_code": "core2", "position": 47, "quantity": 1, "side_code": "runner", "stripped_text": "Install The Personal Touch only on an icebreaker. Host icebreaker has +1 strength.", "stripped_title": "The Personal Touch", "text": "Install The Personal Touch only on an <strong>icebreaker.</strong>\nHost <strong>icebreaker</strong> has +1 strength.", "title": "The Personal Touch", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_dyson_mem_chip_20057(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "20057", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "Archaic but reliable.", "illustrator": "JB Casacop", "keywords": "Chip - Link", "pack_code": "core2", "position": 57, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu, +1 link", "stripped_title": "Dyson Mem Chip", "text": "+1[mu], +1[link]", "title": "Dyson Mem Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_zamba_21003(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21003", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "Mounted holistic lenses download, recompile, and broadcast data faster than a corporate cover-up.", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Console", "pack_code": "ss", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu Whenever a Corp card is exposed, you may gain 1 credit. Limit 1 console per player.", "stripped_title": "Zamba", "text": "+2[mu]\nWhenever a Corp card is exposed, you may gain 1[credit].\nLimit 1 <strong>console</strong> per player.", "title": "Zamba", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_cyberdelia_21006(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21006", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Optical computing still has its uses. But it's hard to explain them to people whose eyes glaze over when you bring up the double-slit experiment.", "illustrator": "Nasrul Hakim", "keywords": "Chip", "pack_code": "ss", "position": 6, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu The first time each turn you fully break a piece of ice, gain 1 credit.", "stripped_title": "Cyberdelia", "text": "+1[mu]\nThe first time each turn you fully break a piece of ice, gain 1[credit].", "title": "Cyberdelia", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_acacia_21021(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21021", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "The system is so deeply rooted, who knows how far the cables run?", "illustrator": "Alexandr Elichev", "pack_code": "dtwn", "position": 21, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp purges virus counters, you may gain 1 credit for each virus counter removed and trash Acacia.", "stripped_title": "Acacia", "text": "Whenever the Corp purges virus counters, you may gain 1[credit] for each virus counter removed and trash Acacia.", "title": "Acacia", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_friday_chip_21042(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21042", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "\"It makes every bad thing that you do so much better.\"\n- g00ru", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Chip", "pack_code": "cotc", "position": 42, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you trash a Corp card, you may place 1 virus counter on Friday Chip. When your turn begins, you may move 1 hosted virus counter to a virus program.", "stripped_title": "Friday Chip", "text": "Whenever you trash a Corp card, you may place 1 virus counter on Friday Chip.\nWhen your turn begins, you may move 1 hosted virus counter to a <strong>virus</strong> program.", "title": "Friday Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_knobkierie_21062(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21062", "cost": 5, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Console", "pack_code": "tdatd", "position": 62, "quantity": 3, "side_code": "runner", "stripped_text": "+3 mu Use the MU on Knobkierie only for virus programs. The first time you make a successful run each turn, you may place 1 virus counter on an installed virus program. Limit 1 console per player.", "stripped_title": "Knobkierie", "text": "+3[mu]\nUse the MU on Knobkierie only for <strong>virus</strong> programs.\nThe first time you make a successful run each turn, you may place 1 virus counter on an installed <strong>virus</strong> program.\nLimit 1 <strong>console</strong> per player.", "title": "Knobkierie", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_gebrselassie_21087(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21087", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 4, "flavor": "Go for distance.", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Mod", "pack_code": "win", "position": 87, "quantity": 3, "side_code": "runner", "stripped_text": "click: Host this hardware on an installed non-AI icebreaker. Abilities that increase host icebreaker's strength last for the remainder of the turn (instead of any shorter duration).", "stripped_title": "Gebrselassie", "text": "[click]: Host this hardware on an installed non-AI <strong>icebreaker</strong>.\nAbilities that increase host icebreaker's strength last for the remainder of the turn <em>(instead of any shorter duration)</em>.", "title": "Gebrselassie", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_zer0_21101(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21101", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Eat. Code. Sleep. Eat. Code. Sleep. Eat. Code. Eat. Code. Sleep. Eat. Code. Code. Sleep. Code. Code. Code. Eat. Code. Code. Code. Code. Code. Code.", "illustrator": "Martin de Diego S\u00e1daba", "pack_code": "ka", "position": 101, "quantity": 3, "side_code": "runner", "stripped_text": "click, suffer 1 net damage: Gain 1 credit and draw 2 cards. Use this ability only once per turn.", "stripped_title": "Zer0", "text": "[click], <strong>suffer 1 net damage</strong>: Gain 1[credit] and draw 2 cards. Use this ability only once per turn.", "title": "Zer0", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_hippo_21103(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21103", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 5, "flavor": "Getting it up the stairs was enough for him to know that if he ever moved, it was staying.", "illustrator": "Juan Novelletto", "pack_code": "ka", "position": 103, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you fully break the outermost piece of ice protecting the attacked server during a run, you may remove this hardware from the game to trash that ice.", "stripped_title": "Hippo", "text": "The first time each turn you fully break the outermost piece of ice protecting the attacked server during a run, you may remove this hardware from the game to trash that ice.", "title": "Hippo", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_flameout_21109(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "21109", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "Caravan Studio", "keywords": "Mod", "pack_code": "ka", "position": 109, "quantity": 3, "side_code": "runner", "stripped_text": "Flame-out can host a single program. When you install Flame-out, place 9 credits on it. Use these credits to pay for using hosted program. When a turn ends in which you used credits on Flame-out, trash hosted program.", "stripped_title": "Flame-out", "text": "Flame-out can host a single program.\nWhen you install Flame-out, place 9[credit] on it. Use these credits to pay for using hosted program.\nWhen a turn ends in which you used credits on Flame-out, trash hosted program.", "title": "Flame-out", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_patchwork_22004(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22004", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Simon Boxer", "keywords": "Console", "pack_code": "rar", "position": 4, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Interrupt -> Whenever you would play or install a card, you may trash 1 card from your grip. If you do, instead play or install that card paying 2 credits less. Use this ability only once per turn. Limit 1 console per player.", "stripped_title": "Patchwork", "text": "+1[mu]\n[interrupt] \u2192 Whenever you would play or install a card, you may trash 1 card from your grip. If you do, instead play or install that card paying 2[credit] less. Use this ability only once per turn.\nLimit 1 <strong>console</strong> per player.", "title": "Patchwork", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_hijacked_router_22005(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22005", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Angga Satriohadi", "pack_code": "rar", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever the Corp creates a server, they lose 1 credit. Whenever you make a successful run on Archives, you may trash this hardware. If you do, the Corp loses 3 credits.", "stripped_title": "Hijacked Router", "text": "Whenever the Corp creates a server, they lose 1[credit].\nWhenever you make a successful run on Archives, you may trash this hardware. If you do, the Corp loses 3[credit].", "title": "Hijacked Router", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_paragon_22010(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22010", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Console", "pack_code": "rar", "position": 10, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu The first time you make a successful run each turn, you may gain 1 credit and look at the top card of your stack. If you do, you may add that card to the bottom of your stack. Limit 1 console per player.", "stripped_title": "Paragon", "text": "+1[mu]\nThe first time you make a successful run each turn, you may gain 1[credit] and look at the top card of your stack. If you do, you may add that card to the bottom of your stack.\nLimit 1 <strong>console</strong> per player.", "title": "Paragon", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_minds_eye_22017(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22017", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "illustrator": "JB Casacop", "keywords": "Console", "pack_code": "rar", "position": 17, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Whenever you make a successful run on R&D, you may place 1 power counter on this hardware. click, 3 hosted power counters: Breach R&D. You cannot access cards in the root of R&D during this breach. Limit 1 console per player.", "stripped_title": "Mind's Eye", "text": "+1[mu]\nWhenever you make a successful run on R&D, you may place 1 power counter on this hardware.\n<strong>[click]</strong>, <strong>3 hosted power counters:</strong> Breach R&D. You cannot access cards in the root of R&D during this breach.\nLimit 1 <strong>console</strong> per player.", "title": "Mind's Eye", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_mache_22018(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "22018", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"What are you making?\"\n\"What <em>aren't</em> I making?\"", "illustrator": "Martin de Diego S\u00e1daba", "pack_code": "rar", "position": 18, "quantity": 3, "side_code": "runner", "stripped_text": "The first time you trash an accessed card each turn, you may place power counters on Mache equal to that card's trash cost. 3 hosted power counters: Draw 1 card.", "stripped_title": "Mache", "text": "The first time you trash an accessed card each turn, you may place power counters on M\u00e2ch\u00e9 equal to that card's trash cost.\n<strong>3 hosted power counters</strong>: Draw 1 card.", "title": "M\u00e2ch\u00e9", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_cyberfeeder_25008(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25008", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 1, "flavor": "I feel almost naked without it.", "illustrator": "Gong Studios", "keywords": "Chip", "pack_code": "sc19", "position": 8, "quantity": 2, "side_code": "runner", "stripped_text": "1 recurring credit Use this credit to pay for using icebreakers or for installing virus programs.", "stripped_title": "Cyberfeeder", "text": "1[recurring-credit]\nUse this credit to pay for using <strong>icebreakers</strong> or for installing <strong>virus</strong> programs.", "title": "Cyberfeeder", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_patchwork_25009(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25009", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Simon Boxer", "keywords": "Console", "pack_code": "sc19", "position": 9, "quantity": 2, "side_code": "runner", "stripped_text": "+1 mu Interrupt -> Whenever you would play or install a card, you may trash 1 card from your grip. If you do, instead play or install that card paying 2 credits less. Use this ability only once per turn. Limit 1 console per player.", "stripped_title": "Patchwork", "text": "+1[mu]\n[interrupt] \u2192 Whenever you would play or install a card, you may trash 1 card from your grip. If you do, instead play or install that card paying 2[credit] less. Use this ability only once per turn.\nLimit 1 <strong>console</strong> per player.", "title": "Patchwork", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_hq_interface_25031(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25031", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "If you don't have someone on the inside, find someone on the inside who's fond of desk ornaments.", "illustrator": "Robert Chew", "pack_code": "sc19", "position": 31, "quantity": 1, "side_code": "runner", "stripped_text": "Whenever you breach HQ, access 1 additional card.", "stripped_title": "HQ Interface", "text": "Whenever you breach HQ, access 1 additional card.", "title": "HQ Interface", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_paragon_25032(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25032", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Console", "pack_code": "sc19", "position": 32, "quantity": 2, "side_code": "runner", "stripped_text": "+1 mu The first time you make a successful run each turn, you may gain 1 credit and look at the top card of your stack. If you do, you may add that card to the bottom of your stack. Limit 1 console per player.", "stripped_title": "Paragon", "text": "+1[mu]\nThe first time you make a successful run each turn, you may gain 1[credit] and look at the top card of your stack. If you do, you may add that card to the bottom of your stack.\nLimit 1 <strong>console</strong> per player.", "title": "Paragon", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_akamatsu_mem_chip_25048(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25048", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 1, "flavor": "The Akamatsu company was founded on three principles: first, to make the fastest mem chips on the market, second, to turn a profit, and third, to serve as a front for the manufacture of illegal neural-stimulants. It is the last principle that perhaps explains their rabid brand loyalty.", "illustrator": "Outland Entertainment LLC", "keywords": "Chip", "pack_code": "sc19", "position": 48, "quantity": 1, "side_code": "runner", "stripped_text": "+1 mu", "stripped_title": "Akamatsu Mem Chip", "text": "+1[mu]", "title": "Akamatsu Mem Chip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_dinosaurus_25049(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25049", "cost": 5, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "illustrator": "Matt Zeilinger", "keywords": "Console", "pack_code": "sc19", "position": 49, "quantity": 2, "side_code": "runner", "stripped_text": "Dinosaurus can host a single non-AI icebreaker. The memory cost of the hosted icebreaker does not count against your memory limit. Hosted icebreaker has +2 strength. Limit 1 console per player.", "stripped_title": "Dinosaurus", "text": "Dinosaurus can host a single non-<strong>AI icebreaker</strong>. The memory cost of the hosted <strong>icebreaker</strong> does not count against your memory limit.\nHosted <strong>icebreaker</strong> has +2 strength.\nLimit 1 <strong>console</strong> per player.", "title": "Dinosaurus", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_rd_interface_25050(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "25050", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "Works best at your own desk.", "illustrator": "Reza Ilyasa", "pack_code": "sc19", "position": 50, "quantity": 1, "side_code": "runner", "stripped_text": "Whenever you breach R&D, access 1 additional card.", "stripped_title": "R&D Interface", "text": "Whenever you breach R&D, access 1 additional card.", "title": "R&D Interface", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_demolisher_26002(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26002", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Step 1: Apply to Problem.\nStep 2: No more Problem!", "illustrator": "Olie Boldador", "keywords": "Console", "pack_code": "df", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu The trash cost of each Corp card is lowered by 1. The first time each turn you trash a Corp card, gain 1 credit. Limit 1 console per player.", "stripped_title": "Demolisher", "text": "+1[mu]\nThe trash cost of each Corp card is lowered by 1.\nThe first time each turn you trash a Corp card, gain 1[credit].\nLimit 1 <strong>console</strong> per player.", "title": "Demolisher", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_flip_switch_26013(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26013", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 1, "flavor": "BMI switches let runners surface without a true disconnect. Handy for a break... immediately.", "illustrator": "Krembler", "pack_code": "df", "position": 13, "quantity": 3, "side_code": "runner", "stripped_text": "You cannot use this hardware during the Corp's turn. trash: Jack out. trash: Remove 1 tag. Interrupt -> trash: Reduce the base trace strength of a trace to 0.", "stripped_title": "Flip Switch", "text": "You cannot use this hardware during the Corp's turn.\n[trash]<strong>:</strong> Jack out.\n[trash]<strong>:</strong> Remove 1 tag.\n[interrupt] \u2192 [trash]<strong>:</strong> Reduce the base trace strength of a trace to 0.", "title": "Flip Switch", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_lucky_charm_26014(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26014", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Want to win a coinflip? Use a coin with two heads.", "illustrator": "Elizaveta Sokolova", "pack_code": "df", "position": 14, "quantity": 3, "side_code": "runner", "stripped_text": "Remove this hardware from the game: Prevent a Corp card ability from ending the run. Use this ability only if you made a successful run on HQ this turn.", "stripped_title": "Lucky Charm", "text": "<strong>Remove this hardware from the game:</strong> Prevent a Corp card ability from ending the run. Use this ability only if you made a successful run on HQ this turn.", "title": "Lucky Charm", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_masterwork_v37_26015(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26015", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "flavor": "v35: Springs to the mount ejectors (new feature)\nv36: Reduced power to springs (x5)", "illustrator": "Olie Boldador", "keywords": "Console", "pack_code": "df", "position": 15, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu. The first time each turn you install a piece of hardware, draw 1 card. Whenever a run begins, you may install a piece of hardware, paying 1 credit more. Limit 1 console per player.", "stripped_title": "Masterwork (v37)", "text": "+1[mu].\nThe first time each turn you install a piece of hardware, draw 1 card.\nWhenever a run begins, you may install a piece of hardware, paying 1[credit] more.\nLimit 1 <strong>console</strong> per player.", "title": "Masterwork (v37)", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_supercorridor_26023(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26023", "cost": 4, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "The Net is boundless, but the right access port is worth a road trip.", "illustrator": "Elizaveta Sokolova", "keywords": "Console", "pack_code": "df", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu You have +1 maximum hand size. When your turn ends, if you and the Corp have the same number of credits, you may gain 2 credits. Limit 1 console per player.", "stripped_title": "Supercorridor", "text": "+2[mu]\nYou have +1 maximum hand size.\nWhen your turn ends, if you and the Corp have the same number of credits, you may gain 2[credit].\nLimit 1 <strong>console</strong> per player.", "title": "Supercorridor", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_devil_charm_26068(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26068", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "A simple little box, brimming with temptation.", "illustrator": "Elizaveta Sokolova", "keywords": "Chip", "pack_code": "ur", "position": 68, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you encounter a piece of ice, you may remove this hardware from the game. If you do, that ice gets -6 strength for the remainder of the run.", "stripped_title": "Devil Charm", "text": "Whenever you encounter a piece of ice, you may remove this hardware from the game. If you do, that ice gets -6 strength for the remainder of the run.", "title": "Devil Charm", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_gachapon_26069(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26069", "cost": 0, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "flavor": "Win a new friend today!", "illustrator": "Elizaveta Sokolova", "keywords": "Chip", "pack_code": "ur", "position": 69, "quantity": 3, "side_code": "runner", "stripped_text": "trash: Set aside the top 6 cards of your stack. You may install 1 program or virtual resource from among the set aside cards, paying 2 credits less. Shuffle 3 of the remaining cards into your stack, then remove the rest from the game.", "stripped_title": "Gachapon", "text": "[trash]<strong>:</strong> Set aside the top 6 cards of your stack. You may install 1 program or <strong>virtual</strong> resource from among the set aside cards, paying 2[credit] less. Shuffle 3 of the remaining cards into your stack, then remove the rest from the game.", "title": "Gachapon", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_keiko_26070(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26070", "cost": 3, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"...and friends hold you close. I vow never to let go of my princess.\"", "illustrator": "Olie Boldador", "keywords": "Console - Companion", "pack_code": "ur", "position": 70, "quantity": 3, "side_code": "runner", "stripped_text": "+2 mu The first time each turn you spend credits from or install a companion, gain 1 credit. Limit 1 console per player.", "stripped_title": "Keiko", "text": "+2[mu]\nThe first time each turn you spend credits from or install a <strong>companion</strong>, gain 1[credit].\nLimit 1 <strong>console</strong> per player.", "title": "Keiko", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_boomerang_26075(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26075", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Return to sender.", "illustrator": "Elizaveta Sokolova", "pack_code": "ur", "position": 75, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, choose an installed piece of ice. Use this hardware only during encounters with that ice. trash: Break up to 2 subroutines. When this run ends, if it is successful, you may shuffle a copy of Boomerang from your heap into your stack.", "stripped_title": "Boomerang", "text": "When you install this hardware, choose an installed piece of ice. Use this hardware only during encounters with that ice.\n[trash]<strong>:</strong> Break up to 2 subroutines. When this run ends, if it is successful, you may shuffle a copy of Boomerang from your heap into your stack.", "title": "Boomerang", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_mu_safecracker_26076(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26076", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "illustrator": "Zoe Cohen", "pack_code": "ur", "position": 76, "quantity": 3, "side_code": "runner", "stripped_text": "Use this hardware only by spending credits from stealth cards. Whenever you make a successful run on HQ, you may pay 1 credit to access 1 additional card when you breach HQ. Whenever you make a successful run on R&D, you may pay 2 credits to access 1 additional card when you breach R&D.", "stripped_title": "Mu Safecracker", "text": "Use this hardware only by spending credits from <strong>stealth</strong> cards.\nWhenever you make a successful run on HQ, you may pay 1[credit] to access 1 additional card when you breach HQ.\nWhenever you make a successful run on R&D, you may pay 2[credit] to access 1 additional card when you breach R&D.", "title": "Mu Safecracker", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_prognostic_qloop_26077(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26077", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Overinflate a superposition-stack and optimal code forms the negentropy traverse.\"\n\"Aha, like putting too much air into a balloon?!\"", "illustrator": "N. Hopkins", "keywords": "Chip", "pack_code": "ur", "position": 77, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn a run begins, you may look at the top 2 cards of your stack. 1 credit: Reveal the top card of your stack. You may install that card if it is a program or piece of hardware. Use this ability only once per turn.", "stripped_title": "Prognostic Q-Loop", "text": "The first time each turn a run begins, you may look at the top 2 cards of your stack.\n<strong>1[credit]:</strong> Reveal the top card of your stack. You may install that card if it is a program or piece of hardware. Use this ability only once per turn.", "title": "Prognostic Q-Loop", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_swift_26078(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26078", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Red ones go faster.\" - Ken \"Express\" Tenma", "illustrator": "Kira L. Nguyen", "keywords": "Console - Vehicle", "pack_code": "ur", "position": 78, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu The first time each turn you play a run event, gain click. Limit 1 console per player.", "stripped_title": "Swift", "text": "+1[mu]\nThe first time each turn you play a <strong>run</strong> event, gain [click].\nLimit 1 <strong>console</strong> per player.", "title": "Swift", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_aniccam_26084(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26084", "cost": 3, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "Objects are but modulations in a continuous cycle of energy\u2014illusory and impermanent echoes of the Self.", "illustrator": "Olie Boldador", "keywords": "Console", "pack_code": "ur", "position": 84, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu The first time each turn an event is trashed (from any location), draw 1 card. Limit 1 console per player.", "stripped_title": "Aniccam", "text": "+1[mu]\nThe first time each turn an event is trashed <em>(from any location)</em>, draw 1 card.\nLimit 1 <strong>console</strong> per player.", "title": "Aniccam", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_simulchip_26085(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26085", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "\"I <em>could</em> let my code evolve something new, but sometimes I just want to remember yesterday's solution.\"\n-Lane", "illustrator": "Elizaveta Sokolova", "keywords": "Chip", "pack_code": "ur", "position": 85, "quantity": 3, "side_code": "runner", "stripped_text": "If no installed programs have been trashed this turn, you must trash 1 installed program as an additional cost to use this hardware. trash: Install 1 program from your heap, paying 3 credits less.", "stripped_title": "Simulchip", "text": "If no installed programs have been trashed this turn, you must trash 1 installed program as an additional cost to use this hardware.\n[trash]<strong>:</strong> Install 1 program from your heap, paying 3[credit] less.", "title": "Simulchip", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_buffer_drive_26093(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "26093", "cost": 3, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 1, "flavor": "\"Future me <em>needs</em> those 60 petabytes of cat vids.\"\n-Princess Space Kitten", "illustrator": "Elizaveta Sokolova", "pack_code": "ur", "position": 93, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn 1 or more cards are trashed from your grip or stack, you may add 1 of those cards to the bottom of your stack. Remove this hardware from the game: Add 1 card from your heap to the top of your stack.", "stripped_title": "Buffer Drive", "text": "The first time each turn 1 or more cards are trashed from your grip or stack, you may add 1 of those cards to the bottom of your stack.\n<strong>Remove this hardware from the game:</strong> Add 1 card from your heap to the top of your stack.", "title": "Buffer Drive", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_swift_27002(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "27002", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Red ones go faster.\" - Ken \"Express\" Tenma", "illustrator": "Kira L. Nguyen", "keywords": "Console - Vehicle", "pack_code": "urbp", "position": 2, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu The first time each turn you play a run event, gain click. Limit 1 console per player.", "stripped_title": "Swift", "text": "+1[mu]\nThe first time each turn you play a <strong>run</strong> event, gain [click].\nLimit 1 <strong>console</strong> per player.", "title": "Swift", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_e3_feedback_implants_29003(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "29003", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "CyberSolutions' e3 line of implants trade strictly in muscle memory and autonomic responses, freeing the brain to focus entirely on cerebral tasks.", "illustrator": "Mauricio Herrera", "keywords": "Mod", "pack_code": "sm", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "Whenever you break a subroutine on a piece of ice, you may pay 1 credit to break 1 subroutine on that ice.", "stripped_title": "e3 Feedback Implants", "text": "Whenever you break a subroutine on a piece of ice, you may pay 1[credit] to break 1 subroutine on that ice.", "title": "e3 Feedback Implants", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_prepaid_voicepad_29008(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "29008", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "A VoicePAD is a personal access device with most of its functions ripped out. Just about all it's good for is making voice-calls and managing your contacts. The only reason to even have one is for its anonymity, which for a certain kind of person is all the reason one needs.", "illustrator": "Mike Nesbitt", "keywords": "Gear", "pack_code": "sm", "position": 8, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit (When you install this card and before your turn begins, refill to 1 hosted credit.) You can spend hosted credits to play events.", "stripped_title": "Prepaid VoicePAD", "text": "1[recurring-credit] <em>(When you install this card and before your turn begins, refill to 1 hosted credit.)</em>\nYou can spend hosted credits to play events.", "title": "Prepaid VoicePAD", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_carnivore_30003(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30003", "cost": 4, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "\"It hungers to sink teeth into problems.\"\n\u2014Loup", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Console", "pack_code": "sg", "position": 3, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Access -> Trash 2 cards from your grip: Trash the card you are accessing. Use this ability only once per turn. Limit 1 console per player.", "stripped_title": "Carnivore", "text": "+1[mu]\nAccess \u2192 <strong>Trash 2 cards from your grip:</strong> Trash the card you are accessing. Use this ability only once per turn.\nLimit 1 <strong>console</strong> per player.", "title": "Carnivore", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_docklands_pass_30013(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30013", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "Zahya knows the keeper of every door between the Docklands and the Domes. More importantly, she knows their price.", "illustrator": "David Lei", "pack_code": "sg", "position": 13, "quantity": 3, "side_code": "runner", "stripped_text": "The first time each turn you breach HQ, access 1 additional card.", "stripped_title": "Docklands Pass", "text": "The first time each turn you breach HQ, access 1 additional card.", "title": "Docklands Pass", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_pennyshaver_30014(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30014", "cost": 3, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "flavor": "\"Braggarts chase big heists. Patience enriches skimming fractions of a credit at a time.\" \u2014Zahya", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Console", "pack_code": "sg", "position": 14, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Whenever you make a successful run, place 1 credit on this hardware. click: Place 1 credit on this hardware, then take all credits from it. Limit 1 console per player.", "stripped_title": "Pennyshaver", "text": "+1[mu]\nWhenever you make a successful run, place 1[credit] on this hardware.\n[click]<strong>:</strong> Place 1[credit] on this hardware, then take all credits from it.\nLimit 1 <strong>console</strong> per player.", "title": "Pennyshaver", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_dzmz_optimizer_30022(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30022", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "T\u0101o exhaled, the med-exoskeleton faithfully stabilizing him. In that absent breath, he reached through layers of waldos and optimizers and plucked the errant molecule from the chip.", "illustrator": "David Lei", "pack_code": "sg", "position": 22, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu The first program you install each turn costs 1 credit less to install.", "stripped_title": "DZMZ Optimizer", "text": "+1[mu]\nThe first program you install each turn costs 1[credit] less to install.", "title": "DZMZ Optimizer", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_pantograph_30023(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30023", "cost": 2, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "\"With this beautiful baby I can juggle simultaneous runs by haptic feedback alone!\"\n\u2014T\u0101o", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Console", "pack_code": "sg", "position": 23, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu Whenever an agenda is scored or stolen, gain 1 credit. Then, you may install 1 card from your grip. Limit 1 console per player.", "stripped_title": "Pantograph", "text": "+1[mu]\nWhenever an agenda is scored or stolen, gain 1[credit]. Then, you may install 1 card from your grip.\nLimit 1 <strong>console</strong> per player.", "title": "Pantograph", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_t400_memory_diamond_30031(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "30031", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "LLDS still holds the patent, but good tech attracts knockoffs.", "illustrator": "Elizaveta Sokolova", "keywords": "Chip", "pack_code": "sg", "position": 31, "quantity": 3, "side_code": "runner", "stripped_text": "+1 mu You get +1 maximum hand size.", "stripped_title": "T400 Memory Diamond", "text": "+1[mu]\nYou get +1 maximum hand size.", "title": "T400 Memory Diamond", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_prepaid_voicepad_31038(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "31038", "cost": 2, "deck_limit": 3, "faction_code": "neutral-runner", "faction_cost": 0, "flavor": "They were off the market for years, till the Beanstalk Crisis made redundancy fashionable again.", "illustrator": "Zoe Cohen, Alexis Spicer", "keywords": "Gear", "pack_code": "su21", "position": 38, "quantity": 3, "side_code": "runner", "stripped_text": "1 recurring credit (When you install this card and before your turn begins, refill to 1 hosted credit.) You can spend hosted credits to play events.", "stripped_title": "Prepaid VoicePAD", "text": "1[recurring-credit] <em>(When you install this card and before your turn begins, refill to 1 hosted credit.)</em>\nYou can spend hosted credits to play events.", "title": "Prepaid VoicePAD", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_ghosttongue_33005(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33005", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "flavor": "Arming the resistance with disarming charm.", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Cybernetic", "pack_code": "ms", "position": 5, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, suffer 1 core damage. The play cost of each event is lowered by 1 credit.", "stripped_title": "Ghosttongue", "text": "When you install this hardware, suffer 1 core damage.\nThe play cost of each event is lowered by 1[credit].", "title": "Ghosttongue", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_marrow_33006(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33006", "cost": 2, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 2, "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Console - Cybernetic", "pack_code": "ms", "position": 6, "quantity": 3, "side_code": "runner", "stripped_text": "+1mu You get +3 maximum hand size. When you install this hardware, suffer 1 core damage. Whenever the Corp scores an agenda, sabotage 1. (The Corp trashes 1 card of their choice from HQ or the top of R&D.) Limit 1 console per player.", "stripped_title": "Marrow", "text": "+1[mu]\nYou get +3 maximum hand size.\nWhen you install this hardware, suffer 1 core damage.\nWhenever the Corp scores an agenda, sabotage 1. <em>(The Corp trashes 1 card of their choice from HQ or the top of R&D.)</em>\nLimit 1 <strong>console</strong> per player.", "title": "Marrow", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_panweave_33014(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33014", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "flavor": "Skimming credits with the slightest touch.", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Cybernetic", "pack_code": "ms", "position": 14, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, suffer 1 meat damage. The first time each turn you make a successful run on HQ, the Corp loses 1 credit. If they do, gain 1 credit.", "stripped_title": "PAN-Weave", "text": "When you install this hardware, suffer 1 meat damage.\nThe first time each turn you make a successful run on HQ, the Corp loses 1[credit]. If they do, gain 1[credit].", "title": "PAN-Weave", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_virtuoso_33015(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33015", "cost": 4, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 4, "illustrator": "Zoe Cohen", "keywords": "Console", "pack_code": "ms", "position": 15, "quantity": 3, "side_code": "runner", "stripped_text": "+1mu When your turn begins, identify your mark. (If you dont have a mark, a random central server becomes your mark for this turn.) The first time each turn you make a successful run on your mark, if that server is HQ, access 1 additional card when you breach HQ. Otherwise, breach HQ when the run ends. Limit 1 console per player.", "stripped_title": "Virtuoso", "text": "+1[mu]\nWhen your turn begins, identify your mark. <em>(If you don\u2019t have a mark, a random central server becomes your mark for this turn.)</em>\nThe first time each turn you make a successful run on your mark, if that server is HQ, access 1 additional card when you breach HQ. Otherwise, breach HQ when the run ends.\nLimit 1 <strong>console</strong> per player.", "title": "Virtuoso", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_endurance_33025(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33025", "cost": 8, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 5, "illustrator": "Anna Butova", "keywords": "Console - Vehicle", "pack_code": "ms", "position": 25, "quantity": 3, "side_code": "runner", "stripped_text": "+2mu When you install this hardware, place 3 power counters on it. The first time each turn you make a successful run, place 1 power counter on this hardware. 2 hosted power counters: Break up to 2 subroutines. Limit 1 console per player.", "stripped_title": "Endurance", "text": "+2[mu]\nWhen you install this hardware, place 3 power counters on it.\nThe first time each turn you make a successful run, place 1 power counter on this hardware.\n<strong>2 hosted power counters:</strong> Break up to 2 subroutines.\nLimit 1 <strong>console</strong> per player.", "title": "Endurance", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_time_bomb_33069(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33069", "cost": 1, "deck_limit": 3, "faction_code": "anarch", "faction_cost": 3, "illustrator": "Anna Butova", "keywords": "Weapon", "pack_code": "ph", "position": 69, "quantity": 3, "side_code": "runner", "stripped_text": "Install only if you made a successful run on a central server this turn. When you install this hardware, place 1 power counter on it. When your turn begins, if there are 3 or more hosted power counters, trash this hardware and sabotage 3. (The Corp trashes 3 cards of their choice from HQ and/or the top of R&D.) Otherwise, place 1 power counter on this hardware.", "stripped_title": "Time Bomb", "text": "Install only if you made a successful run on a central server this turn. When you install this hardware, place 1 power counter on it.\nWhen your turn begins, if there are 3 or more hosted power counters, trash this hardware and sabotage 3. <em>(The Corp trashes 3 cards of their choice from HQ and/or the top of R&D.)</em> Otherwise, place 1 power counter on this hardware.", "title": "Time Bomb", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_poison_vial_33077(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33077", "cost": 2, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "The poison cuts deeper than the blade.", "illustrator": "Ed Mattinian", "keywords": "Weapon", "pack_code": "ph", "position": 77, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, load 3 power counters onto it. When it is empty, trash it. Hosted power counter: Break up to 2 subroutines. Use this ability only if you have already broken a subroutine during this encounter.", "stripped_title": "Poison Vial", "text": "When you install this hardware, load 3 power counters onto it. When it is empty, trash it.\n<strong>Hosted power counter:</strong> Break up to 2 subroutines. Use this ability only if you have already broken a subroutine during this encounter.", "title": "Poison Vial", "type_code": "hardware", "uniqueness": false}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_wake_implant_v2ajrj_33078(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33078", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 3, "illustrator": "Zefanya Langkan Maega", "keywords": "Cybernetic", "pack_code": "ph", "position": 78, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, suffer 1 meat damage. Whenever you make a successful run on HQ, place 1 power counter on this hardware. Whenever you breach R&D, you may remove up to 3 hosted power counters to access that many additional cards.", "stripped_title": "WAKE Implant v2A-JRJ", "text": "When you install this hardware, suffer 1 meat damage.\nWhenever you make a successful run on HQ, place 1 power counter on this hardware.\nWhenever you breach R&D, you may remove up to 3 hosted power counters to access that many additional cards.", "title": "WAKE Implant v2A-JRJ", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_zenit_chip_jz2mj_33079(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33079", "cost": 1, "deck_limit": 3, "faction_code": "criminal", "faction_cost": 2, "flavor": "\"Zenit implants help you focus on the important things.\"\n\u2014Amp\u00e8re holo-billboard", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Cybernetic - Chip", "pack_code": "ph", "position": 79, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, suffer 1 core damage. The first time each turn you make a successful run on a central server, draw 1 card.", "stripped_title": "Zenit Chip JZ-2MJ", "text": "When you install this hardware, suffer 1 core damage.\nThe first time each turn you make a successful run on a central server, draw 1 card.", "title": "Zenit Chip JZ-2MJ", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_hippocampic_mechanocytes_33085(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33085", "cost": 0, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 2, "flavor": "To outsiders, it is ironic that no one in Amp\u00e8re can remember who invented these little fellows. Within the company, this is considered normal.", "illustrator": "Ed Mattinian", "keywords": "Cybernetic", "pack_code": "ph", "position": 85, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, place 2 power counters on it and suffer 1 meat damage. You get +1 maximum hand size for each hosted power counter.", "stripped_title": "Hippocampic Mechanocytes", "text": "When you install this hardware, place 2 power counters on it and suffer 1 meat damage.\nYou get +1 maximum hand size for each hosted power counter.", "title": "Hippocampic Mechanocytes", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                
class hardware_basilar_synthgland_2kvj_33086(Hardware):
    '''

    '''
    def __init__(self):
        super().__init__(r'''{"code": "33086", "cost": 1, "deck_limit": 3, "faction_code": "shaper", "faction_cost": 3, "flavor": "It isn\u02bct as enjoyable as coffee, but the effects are magnitudes stronger.", "illustrator": "Martin de Diego S\u00e1daba", "keywords": "Cybernetic", "pack_code": "ph", "position": 86, "quantity": 3, "side_code": "runner", "stripped_text": "When you install this hardware, suffer 2 core damage. You get +1 allotted click for each of your turns.", "stripped_title": "Basilar Synthgland 2KVJ", "text": "When you install this hardware, suffer 2 core damage.\nYou get +1 allotted [click] for each of your turns.", "title": "Basilar Synthgland 2KVJ", "type_code": "hardware", "uniqueness": true}''')

    def play(self, player, game):
        '''
        do play actions?
        '''
        super().play(player,game)
        print(f'playing card: {self.title} || TOIMPLEMENT!')
                