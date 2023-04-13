

import requests

BASE_URL = "https://netrunnerdb.com/api/2.0"

# Set authentication credentials
# auth_key = "your_auth_key_here"
# auth_secret = "your_auth_secret_here"

# Account API endpoint functions

def get_account_info(api_key):
    url = f"{BASE_URL}/private/account/info"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    return response.json()

# Card API endpoint functions

def get_card(card_code):
    url = f"{BASE_URL}/public/card/{card_code}"
    # headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url)
    return response.json()

def get_all_cards():
    url = f"{BASE_URL}/public/cards"
    # headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url)
    return response.json()

# Cycle API endpoint functions

def get_cycle(api_key, cycle_code):
    url = f"{BASE_URL}/public/cycle/{cycle_code}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_all_cycles(api_key):
    url = f"{BASE_URL}/public/cycles"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_account_info(api_key):
    url = f"{BASE_URL}/private/account/info"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_card_by_code(card_code):
    url = f"{BASE_URL}/public/card/{card_code}"
    response = requests.get(url)
    return response.json()

def get_all_cards():
    url = f"{BASE_URL}/public/cards"
    response = requests.get(url)
    return response.json()

def get_cycle_by_code(cycle_code):
    url = f"{BASE_URL}/public/cycle/{cycle_code}"
    response = requests.get(url)
    return response.json()

def get_all_cycles():
    url = f"{BASE_URL}/public/cycles"
    response = requests.get(url)
    return response.json()

def publish_deck(api_key, deck_data):
    url = f"{BASE_URL}/private/deck/publish"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.post(url, headers=headers, json=deck_data)
    return response.json()

def save_deck(api_key, deck_data):
    url = f"{BASE_URL}/private/deck/save"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.post(url, headers=headers, json=deck_data)
    return response.json()

def get_private_deck_by_id(api_key, deck_id):
    url = f"{BASE_URL}/private/deck/{deck_id}"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_private_deck_by_uuid(api_key, deck_uuid):
    url = f"{BASE_URL}/private/deck/{deck_uuid}"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_all_private_decks(api_key):
    url = f"{BASE_URL}/private/decks"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_public_deck_by_id(deck_id):
    url = f"{BASE_URL}/public/deck/{deck_id}"
    response = requests.get(url)
    return response.json()

def get_public_deck_by_uuid(deck_uuid):
    url = f"{BASE_URL}/public/deck/{deck_uuid}"
    response = requests.get(url)
    return response.json()

# Decklist endpoints
def get_private_decklists(api_key):
    """Get all (published) decklists created by authenticated user"""
    url = f"{BASE_URL}/private/decklists"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_public_decklist(decklist_id):
    """Get one (published) decklist by ID"""
    url = f"{BASE_URL}/public/decklist/{decklist_id}"
    response = requests.get(url)
    return response.json()

def get_public_decklist_by_uuid(decklist_uuid):
    """Get one (published) decklist by UUID"""
    url = f"{BASE_URL}/public/decklist/{decklist_uuid}"
    response = requests.get(url)
    return response.json()

def get_public_decklists_by_date(date):
    """Get all (published) decklists for a date"""
    url = f"{BASE_URL}/public/decklists/by_date/{date}"
    response = requests.get(url)
    return response.json()

# Faction endpoints
def get_faction(faction_code):
    """Get one faction by code"""
    url = f"{BASE_URL}/public/faction/{faction_code}"
    response = requests.get(url)
    return response.json()

def get_all_factions():
    """Get all factions"""
    url = f"{BASE_URL}/public/factions"
    response = requests.get(url)
    return response.json()

def get_mwl_data():
    """"""
    url = f"{BASE_URL}/public/mwl"
    response = requests.get(url)
    return response.json()

def get_pack_by_code(pack_code):
    """"""
    url = f"{BASE_URL}/public/pack/{pack_code}"
    response = requests.get(url)
    return response.json()

def get_all_packs():
    """"""
    url = f"{BASE_URL}/public/packs"
    response = requests.get(url)
    return response.json()

def get_all_prebuilts():
    """"""
    url = f"{BASE_URL}/public/prebuilts"
    response = requests.get(url)
    return response.json()

def get_side_by_code(side_code):
    """"""
    url = f"{BASE_URL}/public/side/{side_code}"
    response = requests.get(url)
    return response.json()

def get_all_sides():
    """"""
    url = f"{BASE_URL}/public/sides"
    response = requests.get(url)
    return response.json()

def get_type_by_code(type_code):
    """"""
    url = f"{BASE_URL}/public/type/{type_code}"
    response = requests.get(url)
    return response.json()

def get_all_types():
    """"""
    url = f"{BASE_URL}/public/types"
    response = requests.get(url)
    return response.json()
