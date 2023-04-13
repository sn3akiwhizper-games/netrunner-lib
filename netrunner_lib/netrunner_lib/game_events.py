
# from netrunner_lib.game_state import NetrunnerGame #cant import this for its type b/c of circular imports

def prompt_server_selection(game) -> int:
    '''
    prompt to select a corpo owned server
    returns index of selected server, zero-based for immediate use
    [HQ, R&D, Archives, Remote1,...]
    '''
    raise Exception('DEPRECATED')
    print('1) HQ\t2) R&D\t3) Archives')
    print('\t'.join([f"{idx+1}) Remote {idx}" for x, idx in enumerate(game.corpo.remote_servers)]))
    selection = input('Choose a server: (idx number)')
    return int(selection)-1

def generic_player_prompt(player, message) -> str:
    '''
    generic prompt to player using provided message, return the value as a string
    created as a placeholder to allow for easy upgrading to different prompts
    '''
    raise Exception("DEPRECATED")
    return input(message)
