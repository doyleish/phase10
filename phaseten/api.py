from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('sqlite:///:memory:', echo=True)

def newgame():
    return game_id

def deal(game_id):
    return True

def joingame(game_id):
    return player

def top_discard(game_id):
    return card

def top_deck(game_id):
    return card

def verify_hand(game_id, player, hand):
    return True

def pull_from_discard(game_id, player):
    return newcard

def pull_from_deck(game_id, player):
    return newcard

def discard(game_id, player, card):
    return topdiscard

def lay_down(game_id, player):
    if good:
        set won on obj

def wait_for_turn(game_id):
    time.sleep(2)
    return game_id.current_turn

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=101010)
