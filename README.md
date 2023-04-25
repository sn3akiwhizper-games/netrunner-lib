# netrunner-lib

Python library implementing the basics of the Netrunner Card Game. The goal is to use this lib to create other python-based toys for playing the game.

This project is early stages as of 04/13/2023. I'm working on filling everything out and getting good [documentation](wiki/Home.md) for how to use, contribute, etc.

This project builds off the amazing work of the folks at NetrunnerDB, ProxyNexus, and Jinteki so give them some love anyway you can.

## Getting Started

1. Download Repo
2. From repo root: `pip install --editable ./netrunner_lib/`
3. Copy `netrunner_lib/.env-template` to `netrunner_lib/.env` and update values

Many of the commands I run during dev are stored in the run.sh file, use the function name in the script as the cli arg when running. (i.e. `./run.sh tests all`)

## TODO

This is a gross collection of dev notes to keep track of what I need to do

- test_illegal_moves
  - [ ] add action enforcement & validation to game state (prevent illegal moves)
- test_deck_load1
  - [ ] load deck from json file
  - [ ] check saving deck with card code(if card code not saved then class wont load correct version of card)
  - [ ] convert 'assert' to self.assert for pyunittest
- game_state
  - [ ] run_manager
- test base card classes
- test player classes
- test deck class
- [ ] convert gameplay tests into pyunittests
- test_game_play1
  - [x] corpo playing ice
- test_game_play_all_types
  - [X] ~~*agenda*~~ [2023-04-03]
  - [X] ~~*asset*~~ [2023-04-03]
  - [X] ~~*event*~~ [2023-04-02]
  - [X] ~~*hardware*~~ [2023-04-03]
  - [X] ~~*ice*~~ [2023-04-02]
  - [X] ~~*identity*~~ [2023-04-02]
  - [X] ~~*operation*~~ [2023-04-02]
  - [X] ~~*program (kinda)*~~ [2023-04-03]
  - [X] ~~*resource*~~ [2023-04-03]
  - [X] ~~*upgrade*~~ [2023-04-03]

## NOTES

- play() is first function used to play a card, other functions to follow
  - first checks in each inheritance should be for whether the card is playable (sufficient resources)
- need to know other possible sources for play_card turn action
- each card should be responsible for it's movement throughout the board
- whenever a card is moved to a new location, it's new location needs to be recorded in it's state variable
- when playing a card, it should be **popped from the hand** here:
  - agenda _base_card_classes:Agenda.play()
  - asset _base_card_classes:Assets.play()
  - event individual cards (call self.trash(player))
  - hardware _base_card_classes:Hardware.play()
  - ice _base_card_classes:Ice.play()
  - operation individual cards (call self.trash(player))
  - program _base_card_classes:Program.play()
  - resource _base_card_classes:Resource.play()
  - upgrade _base_card_classes:Upgrade.play()
