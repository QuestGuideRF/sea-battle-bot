from app .game_logic import create_empty_board ,place_all_ships
from app .utils import generate_game_id
games ={}
def create_game (player_id ):
    game_id =generate_game_id ()
    board =create_empty_board ()
    place_all_ships (board )
    games [game_id ]={
    "player1":player_id ,
    "player2":None ,
    "boards":{player_id :board },
    "turn":player_id ,
    }
    return game_id
def join_game (game_id ,player_id ):
    game =games .get (game_id )
    if game and game ["player2"]is None :
        board =create_empty_board ()
        place_all_ships (board )
        game ["player2"]=player_id
        game ["boards"][player_id ]=board
        return True
    return False
def get_game (game_id ):
    return games .get (game_id )
def switch_turn (game_id ):
    game =games [game_id ]
    game ["turn"]=game ["player1"]if game ["turn"]==game ["player2"]else game ["player2"]
def get_board (game_id ,player_id ):
    return games [game_id ]["boards"][player_id ]
def get_turn (game_id ):
    return games [game_id ]["turn"]
def delete_game (game_id ):
    if game_id in games :
        del games [game_id ]