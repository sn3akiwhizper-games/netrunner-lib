
import requests

API_URL = 'https://netrunnerdb.com/api/v3/public'

# endpoints = document.getElementsByClassName('endpoint')
# for (let index = 0; index < endpoints.length; index++) {
#     console.log(endpoints[index].children[1].innerText);
# }
#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/card_cycles
# GET /api/v3/public/card_cycles/:id
# GET /api/v3/public/card_cycles/:id/relationships/cards
# GET /api/v3/public/card_cycles/:id/relationships/card_sets
# GET /api/v3/public/card_cycles/:id/card_sets
# GET /api/v3/public/card_cycles/:id/cards
# GET /api/v3/public/card_cycles/:id/relationships/printings
# GET /api/v3/public/card_cycles/:id/printings

#####################################################
# GET /api/v3/public/card_cycles
def get_card_cycles():
    response = requests.get("{API_URL}/card_cycles")
    return response.json()

# GET /api/v3/public/card_cycles/:id
def get_card_cycle_by_id(id):
    response = requests.get(f"{API_URL}/card_cycles/{id}")
    return response.json()

# GET /api/v3/public/card_cycles/:id/relationships/cards
def get_card_cycle_relationship_cards(id):
    response = requests.get(f"{API_URL}/card_cycles/{id}/relationships/cards")
    return response.json()

# GET /api/v3/public/card_cycles/:id/relationships/card_sets
def get_card_cycle_relationship_card_sets(id):
    response = requests.get(f"{API_URL}/card_cycles/{id}/relationships/card_sets")
    return response.json()

# GET /api/v3/public/card_cycles/:id/card_sets
def get_card_cycle_card_sets(id):
    response = requests.get(f"{API_URL}/card_cycles/{id}/card_sets")
    return response.json()

# GET /api/v3/public/card_cycles/:id/cards
def get_card_cycle_cards(id):
    response = requests.get(f"{API_URL}/card_cycles/{id}/cards")
    return response.json()

# GET /api/v3/public/card_cycles/:id/relationships/printings
def get_card_cycle_relationship_printings(id):
    response = requests.get(f"{API_URL}/card_cycles/{id}/relationships/printings")
    return response.json()

# GET /api/v3/public/card_cycles/:id/printings
def get_card_cycle_printings(id):
    response = requests.get(f"{API_URL}/card_cycles/{id}/printings")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/card_pools
# GET /api/v3/public/card_pools/:id
# GET /api/v3/public/card_pools/:id/relationships/card_cycles
# GET /api/v3/public/card_pools/:id/card_cycles
# GET /api/v3/public/card_pools/:id/relationships/cards
# GET /api/v3/public/card_pools/:id/relationships/card_sets
# GET /api/v3/public/card_pools/:id/card_sets
# GET /api/v3/public/card_pools/:id/cards

#####################################################

def get_card_pools():
    response = requests.get(f'{API_URL}/card_pools')
    return response.json()

def get_card_pool(card_pool_id):
    response = requests.get(f'{API_URL}/card_pools/{card_pool_id}')
    return response.json()

def get_card_pool_card_cycles(card_pool_id):
    response = requests.get(f'{API_URL}/card_pools/{card_pool_id}/relationships/card_cycles')
    return response.json()

def get_card_pool_card_cycles_list(card_pool_id):
    response = requests.get(f'{API_URL}/card_pools/{card_pool_id}/card_cycles')
    return response.json()

def get_card_pool_cards(card_pool_id):
    response = requests.get(f'{API_URL}/card_pools/{card_pool_id}/relationships/cards')
    return response.json()

def get_card_pool_card_sets(card_pool_id):
    response = requests.get(f'{API_URL}/card_pools/{card_pool_id}/relationships/card_sets')
    return response.json()

def get_card_pool_card_sets_list(card_pool_id):
    response = requests.get(f'{API_URL}/card_pools/{card_pool_id}/card_sets')
    return response.json()

def get_card_pool_cards_list(card_pool_id):
    response = requests.get(f'{API_URL}/card_pools/{card_pool_id}/cards')
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/card_pools/:id/relationships/format
# GET /api/v3/public/card_pools/:id/format
# GET /api/v3/public/card_pools/:id/relationships/snapshots
# GET /api/v3/public/card_pools/:id/snapshots
# GET /api/v3/public/card_set_types
# GET /api/v3/public/card_set_types/:id
# GET /api/v3/public/card_set_types/:id/relationships/card_sets
# GET /api/v3/public/card_set_types/:id/card_sets
# GET /api/v3/public/card_sets
#####################################################

# GET /api/v3/public/card_pools/:id/relationships/format
def get_card_pool_format_relationships(card_pool_id):
    response = requests.get(f"{API_URL}/card_pools/{card_pool_id}/relationships/format")
    return response.json()

# GET /api/v3/public/card_pools/:id/format
def get_card_pool_format(card_pool_id):
    response = requests.get(f"{API_URL}/card_pools/{card_pool_id}/format")
    return response.json()

# GET /api/v3/public/card_pools/:id/relationships/snapshots
def get_card_pool_snapshots_relationships(card_pool_id):
    response = requests.get(f"{API_URL}/card_pools/{card_pool_id}/relationships/snapshots")
    return response.json()

# GET /api/v3/public/card_pools/:id/snapshots
def get_card_pool_snapshots(card_pool_id):
    response = requests.get(f"{API_URL}/card_pools/{card_pool_id}/snapshots")
    return response.json()

# GET /api/v3/public/card_set_types
def get_card_set_types():
    response = requests.get("{API_URL}/card_set_types")
    return response.json()

# GET /api/v3/public/card_set_types/:id
def get_card_set_type(card_set_type_id):
    response = requests.get(f"{API_URL}/card_set_types/{card_set_type_id}")
    return response.json()

# GET /api/v3/public/card_set_types/:id/relationships/card_sets
def get_card_set_type_relationships(card_set_type_id):
    response = requests.get(f"{API_URL}/card_set_types/{card_set_type_id}/relationships/card_sets")
    return response.json()

# GET /api/v3/public/card_set_types/:id/card_sets
def get_card_sets_for_card_set_type(card_set_type_id):
    response = requests.get(f"{API_URL}/card_set_types/{card_set_type_id}/card_sets")
    return response.json()

# GET /api/v3/public/card_sets
def get_card_sets():
    response = requests.get("{API_URL}/card_sets")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/card_sets?filter[card_cycle_id]=:card_cycle_id
# GET /api/v3/public/card_sets?filter[card_set_type_id]=:card_set_type_id
# GET /api/v3/public/card_sets/:id
# GET /api/v3/public/card_sets/:id/relationships/card_cycle
# GET /api/v3/public/card_sets/:id/card_cycle
# GET /api/v3/public/card_sets/:id/relationships/cards
# GET /api/v3/public/card_sets/:id/relationships/card_set_type
# GET /api/v3/public/card_sets/:id/card_set_type
# GET /api/v3/public/card_sets/:id/cards

#####################################################

# GET /api/v3/public/card_sets?filter[card_cycle_id]=:card_cycle_id
def get_card_sets_by_card_cycle_id(card_cycle_id):
    response = requests.get(f"{API_URL}/card_sets?filter[card_cycle_id]={card_cycle_id}")
    return response.json()

# GET /api/v3/public/card_sets?filter[card_set_type_id]=:card_set_type_id
def get_card_sets_by_card_set_type_id(card_set_type_id):
    response = requests.get(f"{API_URL}/card_sets?filter[card_set_type_id]={card_set_type_id}")
    return response.json()

# GET /api/v3/public/card_sets/:id
def get_card_set(card_set_id):
    response = requests.get(f"{API_URL}/card_sets/{card_set_id}")
    return response.json()

# GET /api/v3/public/card_sets/:id/relationships/card_cycle
def get_card_set_card_cycle_relationships(card_set_id):
    response = requests.get(f"{API_URL}/card_sets/{card_set_id}/relationships/card_cycle")
    return response.json()

# GET /api/v3/public/card_sets/:id/card_cycle
def get_card_set_card_cycle(card_set_id):
    response = requests.get(f"{API_URL}/card_sets/{card_set_id}/card_cycle")
    return response.json()

# GET /api/v3/public/card_sets/:id/relationships/cards
def get_card_set_cards_relationships(card_set_id):
    response = requests.get(f"{API_URL}/card_sets/{card_set_id}/relationships/cards")
    return response.json()

# GET /api/v3/public/card_sets/:id/relationships/card_set_type
def get_card_set_card_set_type_relationships(card_set_id):
    response = requests.get(f"{API_URL}/card_sets/{card_set_id}/relationships/card_set_type")
    return response.json()

# GET /api/v3/public/card_sets/:id/card_set_type
def get_card_set_card_set_type(card_set_id):
    response = requests.get(f"{API_URL}/card_sets/{card_set_id}/card_set_type")
    return response.json()

# GET /api/v3/public/card_sets/:id/cards
def get_cards_for_card_set(card_set_id):
    response = requests.get(f"{API_URL}/card_sets/{card_set_id}/cards")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/card_sets/:id/relationships/printings
# GET /api/v3/public/card_sets/:id/printings
# GET /api/v3/public/card_subtypes
# GET /api/v3/public/card_subtypes/:id
# GET /api/v3/public/card_subtypes/:id/relationships/cards
# GET /api/v3/public/card_subtypes/:id/cards
# GET /api/v3/public/card_subtypes/:id/relationships/printings
# GET /api/v3/public/card_subtypes/:id/printings
# GET /api/v3/public/card_types
# GET /api/v3/public/card_types?filter[side_id]=:side_id
# GET /api/v3/public/card_types/:id

#####################################################

# GET /api/v3/public/card_sets/:id/relationships/printings
def get_card_set_printings_relationships(card_set_id):
    response = requests.get(f"{API_URL}/card_sets/{card_set_id}/relationships/printings")
    return response.json()

# GET /api/v3/public/card_sets/:id/printings
def get_card_set_printings(card_set_id):
    response = requests.get(f"{API_URL}/card_sets/{card_set_id}/printings")
    return response.json()

# GET /api/v3/public/card_subtypes
def get_card_subtypes():
    response = requests.get("{API_URL}/card_subtypes")
    return response.json()

# GET /api/v3/public/card_subtypes/:id
def get_card_subtype(card_subtype_id):
    response = requests.get(f"{API_URL}/card_subtypes/{card_subtype_id}")
    return response.json()

# GET /api/v3/public/card_subtypes/:id/relationships/cards
def get_card_subtype_relationships(card_subtype_id):
    response = requests.get(f"{API_URL}/card_subtypes/{card_subtype_id}/relationships/cards")
    return response.json()

# GET /api/v3/public/card_subtypes/:id/cards
def get_cards_for_card_subtype(card_subtype_id):
    response = requests.get(f"{API_URL}/card_subtypes/{card_subtype_id}/cards")
    return response.json()

# GET /api/v3/public/card_subtypes/:id/relationships/printings
def get_card_subtype_printings_relationships(card_subtype_id):
    response = requests.get(f"{API_URL}/card_subtypes/{card_subtype_id}/relationships/printings")
    return response.json()

# GET /api/v3/public/card_subtypes/:id/printings
def get_printings_for_card_subtype(card_subtype_id):
    response = requests.get(f"{API_URL}/card_subtypes/{card_subtype_id}/printings")
    return response.json()

# GET /api/v3/public/card_types
def get_card_types():
    response = requests.get("{API_URL}/card_types")
    return response.json()

# GET /api/v3/public/card_types?filter[side_id]=:side_id
def get_card_types_by_side_id(side_id):
    response = requests.get(f"{API_URL}/card_types?filter[side_id]={side_id}")
    return response.json()

# GET /api/v3/public/card_types/:id
def get_card_type(card_type_id):
    response = requests.get(f"{API_URL}/card_types/{card_type_id}")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/card_types/:id/relationships/cards
# GET /api/v3/public/card_types/:id/cards
# GET /api/v3/public/card_types/:id/relationships/side
# GET /api/v3/public/card_types/:id/side
# GET /api/v3/public/cards
# GET /api/v3/public/cards?filter[search]=:query
# GET /api/v3/public/cards/:id

#####################################################

# GET /api/v3/public/card_types/:id/relationships/cards
def get_card_type_cards_relationships(card_type_id):
    response = requests.get(f"{API_URL}/card_types/{card_type_id}/relationships/cards")
    return response.json()

# GET /api/v3/public/card_types/:id/cards
def get_cards_for_card_type(card_type_id):
    response = requests.get(f"{API_URL}/card_types/{card_type_id}/cards")
    return response.json()

# GET /api/v3/public/card_types/:id/relationships/side
def get_card_type_side_relationships(card_type_id):
    response = requests.get(f"{API_URL}/card_types/{card_type_id}/relationships/side")
    return response.json()

# GET /api/v3/public/card_types/:id/side
def get_card_type_side(card_type_id):
    response = requests.get(f"{API_URL}/card_types/{card_type_id}/side")
    return response.json()

# GET /api/v3/public/cards
def get_all_cards():
    response = requests.get("{API_URL}/cards")
    return response.json()

# GET /api/v3/public/cards?filter[search]=:query
def search_cards(query):
    response = requests.get(f"{API_URL}/cards?filter[search]={query}")
    return response.json()

# GET /api/v3/public/cards/:id
def get_card(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/cards/:id/relationships/card_subtypes
# GET /api/v3/public/cards/:id/card_subtypes
# GET /api/v3/public/cards/:id/relationships/card_type
# GET /api/v3/public/cards/:id/card_type
# GET /api/v3/public/cards/:id/relationships/faction

#####################################################

# GET /api/v3/public/cards/:id/relationships/card_subtypes
def get_card_card_subtypes_relationships(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/relationships/card_subtypes")
    return response.json()

# GET /api/v3/public/cards/:id/card_subtypes
def get_card_card_subtypes(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/card_subtypes")
    return response.json()

# GET /api/v3/public/cards/:id/relationships/card_type
def get_card_card_type_relationships(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/relationships/card_type")
    return response.json()

# GET /api/v3/public/cards/:id/card_type
def get_card_card_type(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/card_type")
    return response.json()

# GET /api/v3/public/cards/:id/relationships/faction
def get_card_faction_relationships(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/relationships/faction")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/cards/:id/faction
# GET /api/v3/public/cards/:id/relationships/printings
# GET /api/v3/public/cards/:id/printings
# GET /api/v3/public/cards/:id/relationships/side
# GET /api/v3/public/cards/:id/side

#####################################################

# GET /api/v3/public/cards/:id/faction
def get_card_faction(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/faction")
    return response.json()

# GET /api/v3/public/cards/:id/relationships/printings
def get_card_printings_relationships(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/relationships/printings")
    return response.json()

# GET /api/v3/public/cards/:id/printings
def get_card_printings(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/printings")
    return response.json()

# GET /api/v3/public/cards/:id/relationships/side
def get_card_side_relationships(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/relationships/side")
    return response.json()

# GET /api/v3/public/cards/:id/side
def get_card_side(card_id):
    response = requests.get(f"{API_URL}/cards/{card_id}/side")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/factions
# GET /api/v3/public/factions?filter[side_id]=:side_id
# GET /api/v3/public/factions?filter[is_mini]=:is_mini
# GET /api/v3/public/factions/:id
# GET /api/v3/public/factions/:id/relationships/cards

#####################################################

# GET /api/v3/public/factions
def get_factions():
    response = requests.get("{API_URL}/factions")
    return response.json()

# GET /api/v3/public/factions?filter[side_id]=:side_id
def get_factions_by_side_id(side_id):
    response = requests.get(f"{API_URL}/factions?filter[side_id]={side_id}")
    return response.json()

# GET /api/v3/public/factions?filter[is_mini]=:is_mini
def get_mini_factions(is_mini):
    response = requests.get(f"{API_URL}/factions?filter[is_mini]={is_mini}")
    return response.json()

# GET /api/v3/public/factions/:id
def get_faction(faction_id):
    response = requests.get(f"{API_URL}/factions/{faction_id}")
    return response.json()

# GET /api/v3/public/factions/:id/relationships/cards
def get_faction_cards_relationships(faction_id):
    response = requests.get(f"{API_URL}/factions/{faction_id}/relationships/cards")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/factions/:id/cards
# GET /api/v3/public/factions/:id/relationships/printings
# GET /api/v3/public/factions/:id/printings

#####################################################

# GET /api/v3/public/factions/:id/cards
def get_faction_cards(faction_id):
    response = requests.get(f"{API_URL}/factions/{faction_id}/cards")
    return response.json()

# GET /api/v3/public/factions/:id/relationships/printings
def get_faction_printings_relationships(faction_id):
    response = requests.get(f"{API_URL}/factions/{faction_id}/relationships/printings")
    return response.json()

# GET /api/v3/public/factions/:id/printings
def get_faction_printings(faction_id):
    response = requests.get(f"{API_URL}/factions/{faction_id}/printings")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/factions/:id/relationships/side
# GET /api/v3/public/factions/:id/side
# GET /api/v3/public/formats
# GET /api/v3/public/formats/:id
# GET /api/v3/public/formats/:id/relationships/card_pools
# GET /api/v3/public/formats/:id/card_pools

#####################################################

# GET /api/v3/public/factions/:id/relationships/side
def get_faction_side_relationships(faction_id):
    response = requests.get(f"{API_URL}/factions/{faction_id}/relationships/side")
    return response.json()

# GET /api/v3/public/factions/:id/side
def get_faction_side(faction_id):
    response = requests.get(f"{API_URL}/factions/{faction_id}/side")
    return response.json()

# GET /api/v3/public/formats
def get_formats():
    response = requests.get("{API_URL}/formats")
    return response.json()

# GET /api/v3/public/formats/:id
def get_format(format_id):
    response = requests.get(f"{API_URL}/formats/{format_id}")
    return response.json()

# GET /api/v3/public/formats/:id/relationships/card_pools
def get_format_card_pools_relationships(format_id):
    response = requests.get(f"{API_URL}/formats/{format_id}/relationships/card_pools")
    return response.json()

# GET /api/v3/public/formats/:id/card_pools
def get_format_card_pools(format_id):
    response = requests.get(f"{API_URL}/formats/{format_id}/card_pools")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/formats/:id/relationships/restrictions
# GET /api/v3/public/formats/:id/restrictions
# GET /api/v3/public/formats/:id/relationships/restrictions
# GET /api/v3/public/formats/:id/snapshots

#####################################################

# GET /api/v3/public/formats/:id/relationships/restrictions
def get_format_restrictions_relationships(format_id):
    response = requests.get(f"{API_URL}/formats/{format_id}/relationships/restrictions")
    return response.json()

# GET /api/v3/public/formats/:id/restrictions
def get_format_restrictions(format_id):
    response = requests.get(f"{API_URL}/formats/{format_id}/restrictions")
    return response.json()

# GET /api/v3/public/formats/:id/relationships/restrictions
def get_format_restrictions_relationships(format_id):
    response = requests.get(f"{API_URL}/formats/{format_id}/relationships/restrictions")
    return response.json()

# GET /api/v3/public/formats/:id/snapshots
def get_format_snapshots(format_id):
    response = requests.get(f"{API_URL}/formats/{format_id}/snapshots")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/illustrators
# GET /api/v3/public/illustrators/:id
# GET /api/v3/public/illustrators/:id/relationships/printings
# GET /api/v3/public/illustrators/:id/printings
# GET /api/v3/public/printings
# GET /api/v3/public/printings?filter[distinct_cards]

#####################################################

# GET /api/v3/public/illustrators
def get_illustrators():
    response = requests.get("{API_URL}/illustrators")
    return response.json()

# GET /api/v3/public/illustrators/:id
def get_illustrator(illustrator_id):
    response = requests.get(f"{API_URL}/illustrators/{illustrator_id}")
    return response.json()

# GET /api/v3/public/illustrators/:id/relationships/printings
def get_illustrator_printings_relationships(illustrator_id):
    response = requests.get(f"{API_URL}/illustrators/{illustrator_id}/relationships/printings")
    return response.json()

# GET /api/v3/public/illustrators/:id/printings
def get_illustrator_printings(illustrator_id):
    response = requests.get(f"{API_URL}/illustrators/{illustrator_id}/printings")
    return response.json()

# GET /api/v3/public/printings
def get_printings():
    response = requests.get("{API_URL}/printings")
    return response.json()

# GET /api/v3/public/printings?filter[distinct_cards]
def get_distinct_card_printings():
    response = requests.get("{API_URL}/printings?filter[distinct_cards]")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/printings?filter[search]=:query
# GET /api/v3/public/printings/:id
# GET /api/v3/public/printings/:id/relationships/card_cycle
# GET /api/v3/public/printings/:id/card_cycle
# GET /api/v3/public/printings/:id/relationships/card
# GET /api/v3/public/printings/:id/relationships/card_set

#####################################################

# GET /api/v3/public/printings?filter[search]=:query
def search_printings(query):
    response = requests.get(f"{API_URL}/printings?filter[search]={query}")
    return response.json()

# GET /api/v3/public/printings/:id
def get_printing(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}")
    return response.json()

# GET /api/v3/public/printings/:id/relationships/card_cycle
def get_printing_card_cycle_relationships(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/relationships/card_cycle")
    return response.json()

# GET /api/v3/public/printings/:id/card_cycle
def get_printing_card_cycle(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/card_cycle")
    return response.json()

# GET /api/v3/public/printings/:id/relationships/card
def get_printing_card_relationships(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/relationships/card")
    return response.json()

# GET /api/v3/public/printings/:id/relationships/card_set
def get_printing_card_set_relationships(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/relationships/card_set")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/printings/:id/card_set
# GET /api/v3/public/printings/:id/card
# GET /api/v3/public/printings/:id/relationships/faction
# GET /api/v3/public/printings/:id/faction
# GET /api/v3/public/printings/:id/relationships/illustrators

#####################################################

# GET /api/v3/public/printings/:id/card_set
def get_printing_card_set(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/card_set")
    return response.json()

# GET /api/v3/public/printings/:id/card
def get_printing_card(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/card")
    return response.json()

# GET /api/v3/public/printings/:id/relationships/faction
def get_printing_faction_relationships(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/relationships/faction")
    return response.json()

# GET /api/v3/public/printings/:id/faction
def get_printing_faction(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/faction")
    return response.json()

# GET /api/v3/public/printings/:id/relationships/illustrators
def get_printing_illustrators_relationships(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/relationships/illustrators")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/printings/:id/illustrators
# GET /api/v3/public/printings/:id/relationships/side
# GET /api/v3/public/printings/:id/side
# GET /api/v3/public/restrictions
# GET /api/v3/public/restrictions/:id

#####################################################

# GET /api/v3/public/printings/:id/illustrators
def get_printing_illustrators(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/illustrators")
    return response.json()

# GET /api/v3/public/printings/:id/relationships/side
def get_printing_side_relationships(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/relationships/side")
    return response.json()

# GET /api/v3/public/printings/:id/side
def get_printing_side(printing_id):
    response = requests.get(f"{API_URL}/printings/{printing_id}/side")
    return response.json()

# GET /api/v3/public/restrictions
def get_restrictions():
    response = requests.get("{API_URL}/restrictions")
    return response.json()

# GET /api/v3/public/restrictions/:id
def get_restriction(restriction_id):
    response = requests.get(f"{API_URL}/restrictions/{restriction_id}")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/sides
# GET /api/v3/public/sides/:id
# GET /api/v3/public/sides/:id/relationships/cards
# GET /api/v3/public/sides/:id/relationships/card_types

#####################################################

# GET /api/v3/public/sides
def get_sides():
    response = requests.get("{API_URL}/sides")
    return response.json()

# GET /api/v3/public/sides/:id
def get_side(side_id):
    response = requests.get(f"{API_URL}/sides/{side_id}")
    return response.json()

# GET /api/v3/public/sides/:id/relationships/cards
def get_side_cards_relationships(side_id):
    response = requests.get(f"{API_URL}/sides/{side_id}/relationships/cards")
    return response.json()

# GET /api/v3/public/sides/:id/relationships/card_types
def get_side_card_types_relationships(side_id):
    response = requests.get(f"{API_URL}/sides/{side_id}/relationships/card_types")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/sides/:id/card_types
# GET /api/v3/public/sides/:id/cards
# GET /api/v3/public/sides/:id/relationships/factions
# GET /api/v3/public/sides/:id/factions
# GET /api/v3/public/sides/:id/relationships/printings

#####################################################

# GET /api/v3/public/sides/:id/card_types
def get_side_card_types(side_id):
    response = requests.get(f"{API_URL}/sides/{side_id}/card_types")
    return response.json()

# GET /api/v3/public/sides/:id/cards
def get_side_cards(side_id):
    response = requests.get(f"{API_URL}/sides/{side_id}/cards")
    return response.json()

# GET /api/v3/public/sides/:id/relationships/factions
def get_side_factions_relationships(side_id):
    response = requests.get(f"{API_URL}/sides/{side_id}/relationships/factions")
    return response.json()

# GET /api/v3/public/sides/:id/factions
def get_side_factions(side_id):
    response = requests.get(f"{API_URL}/sides/{side_id}/factions")
    return response.json()

# GET /api/v3/public/sides/:id/relationships/printings
def get_side_printings_relationships(side_id):
    response = requests.get(f"{API_URL}/sides/{side_id}/relationships/printings")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/sides/:id/printings
# GET /api/v3/public/snapshots
# GET /api/v3/public/snapshots?filter[active]=:active
# GET /api/v3/public/snapshots?filter[format_id]=:format_id
# GET /api/v3/public/snapshots/:id
# GET /api/v3/public/snapshots/:id/relationships/card_pool

#####################################################

# GET /api/v3/public/sides/:id/printings
def get_side_printings(side_id):
    response = requests.get(f"{API_URL}/sides/{side_id}/printings")
    return response.json()

# GET /api/v3/public/snapshots
def get_snapshots():
    response = requests.get("{API_URL}/snapshots")
    return response.json()

# GET /api/v3/public/snapshots?filter[active]=:active
def get_active_snapshots(active):
    response = requests.get(f"{API_URL}/snapshots?filter[active]={active}")
    return response.json()

# GET /api/v3/public/snapshots?filter[format_id]=:format_id
def get_snapshots_by_format(format_id):
    response = requests.get(f"{API_URL}/snapshots?filter[format_id]={format_id}")
    return response.json()

# GET /api/v3/public/snapshots/:id
def get_snapshot(snapshot_id):
    response = requests.get(f"{API_URL}/snapshots/{snapshot_id}")
    return response.json()

# GET /api/v3/public/snapshots/:id/relationships/card_pool
def get_snapshot_card_pool_relationships(snapshot_id):
    response = requests.get(f"{API_URL}/snapshots/{snapshot_id}/relationships/card_pool")
    return response.json()

#####################################################
#####################################################
#generate python functions to interact with these API endpoints. do not include examples.
# GET /api/v3/public/snapshots/:id/card_pool
# GET /api/v3/public/snapshots/:id/relationships/format
# GET /api/v3/public/snapshots/:id/format
# GET /api/v3/public/snapshots/:id/relationships/restriction
# GET /api/v3/public/snapshots/:id/restriction

#####################################################

# GET /api/v3/public/snapshots/:id/card_pool
def get_snapshot_card_pool(snapshot_id):
    response = requests.get(f"{API_URL}/snapshots/{snapshot_id}/card_pool")
    return response.json()

# GET /api/v3/public/snapshots/:id/relationships/format
def get_snapshot_format_relationships(snapshot_id):
    response = requests.get(f"{API_URL}/snapshots/{snapshot_id}/relationships/format")
    return response.json()

# GET /api/v3/public/snapshots/:id/format
def get_snapshot_format(snapshot_id):
    response = requests.get(f"{API_URL}/snapshots/{snapshot_id}/format")
    return response.json()

# GET /api/v3/public/snapshots/:id/relationships/restriction
def get_snapshot_restriction_relationships(snapshot_id):
    response = requests.get(f"{API_URL}/snapshots/{snapshot_id}/relationships/restriction")
    return response.json()

# GET /api/v3/public/snapshots/:id/restriction
def get_snapshot_restriction(snapshot_id):
    response = requests.get(f"{API_URL}/snapshots/{snapshot_id}/restriction")
    return response.json()

#####################################################
#####################################################
