import os
from dotenv import load_dotenv

from os.path import join as pjo

load_dotenv('.env')

BASE_REPO_PATH = os.getenv('PROJECT_REPO_PATH')
BASE_PROJECT_PATH = pjo(BASE_REPO_PATH,'netrunner_lib','netrunner_lib')

ASSETS_PATH = pjo(BASE_PROJECT_PATH,'assets')

CARD_DB_JSON_PATH = pjo(ASSETS_PATH,'netrunnerDB','netrunnberdb-cards-v2-03-31-2021.json')

DECKLIST_PATH = pjo(ASSETS_PATH,'netrunnerDB','deck_lists')
CUSTOM_DECK_SAVE_PATH = DECKLIST_PATH

CARD_IMAGES_PATH = pjo(ASSETS_PATH,'card_images')
