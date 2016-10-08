from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import lib.db as db
from lib.card import Card
from lib.player import Player
from lib.game import Game

app = Flask(__name__)
engine = create_engine('sqlite:///:memory:', echo=True)
Card.metadata.create_all(engine)
Player.metadata.create_all(engine)
Game.metadata.create_all(engine)

s = sessionmaker(bind=engine)

def newgame():
    # returns game_id
    return db.create_game(s())

def deal(game_id):
    # returns player_id for first turn
    return db.deal_round(s(), game_id)

def joingame(game_id):
    # returns player_id of new player
    return db.new_player(s(), game_id)

def top_discard(game_id):
    # returns the card json
    return db.top_discard(s(), game_id).jsonify()

def top_main(game_id):
    # returns the card json
    return db.top_main(s(), game_id).jsonify()

def draw_discard(game_id, player):
    # returns card
    return db.draw_discard(s(), game_id, player)

def draw_deck(game_id, player):
    return db.draw_deck(s(), game_id, player)

def discard(game_id, card):
    return db.discard(s(), game_id, card)

def lay_down(game_id, player):
    if db.check_phase(s(), game_id, player):
        pass

def get_ac(game_id):
    # return action_counter
    return db.get_game(s(), game_id).ac

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=101010)
