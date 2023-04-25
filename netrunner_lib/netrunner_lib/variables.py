"""Global variables for the netrunner_lib package
This file should always be included as `from netrunner_lib import variables as vars`, so it is easier to track where the variables are being used (i.e. vars.BASE_REPO_PATH).

Loads additional variables from the .env 
"""

import os
from dotenv import load_dotenv

from os.path import join as pjo

# load_dotenv('.env')
load_dotenv()

BASE_REPO_PATH = os.getenv('PROJECT_REPO_PATH')
BASE_PROJECT_PATH = pjo(BASE_REPO_PATH,'netrunner_lib','netrunner_lib')

ASSETS_PATH = pjo(BASE_PROJECT_PATH,'assets')

CARD_DB_JSON_PATH = pjo(ASSETS_PATH,'netrunnerDB','netrunnberdb-cards-v2-03-31-2021.json')

DECKLIST_PATH = pjo(ASSETS_PATH,'netrunnerDB','deck_lists')
CUSTOM_DECK_SAVE_PATH = DECKLIST_PATH

CARD_IMAGES_PATH = pjo(ASSETS_PATH,'card_images')

VERBOSITY=int(os.getenv('VERBOSITY',0))

def debug_print(msg:str,level:int=3):
    '''
    print debugging info based on the current verbosity level
    INPUT:
        - msg:str message to print
        - level:int verbosity level to meet in order to print (0=silent,3=everything)
    '''
    if level<=VERBOSITY:
        print(f'DEBUG[{level}]:',msg)
