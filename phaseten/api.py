from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import lib.db as db
import lib.templating as templating

from lib.card import Card
from lib.player import Player
from lib.game import Game

import json

app = Flask(__name__)
engine = create_engine('sqlite:///:memory:', echo=True)
Card.metadata.create_all(engine)
Player.metadata.create_all(engine)
Game.metadata.create_all(engine)

s = sessionmaker(bind=engine)

def jsonify(val):
    if isinstance(val,dict):
        return json.dumps(val)
    else:
        return json.dumps({"return":val})

@app.route('/p10/api/new_game')
def new_game():
    # returns game_id
    return jsonify(db.create_game(s()))

@app.route('/p10/api/deal/<game_id>')
def deal_round(game_id):
    # returns player_id for first turn
    return jsonify(db.deal_round(s(), game_id))

@app.route('/p10/api/join/<game_id>')
def join_game(game_id):
    # returns player_id of new player
    return jsonify(db.new_player(s(), game_id))

@app.route('/p10/api/top_discard/<game_id>')
def top_discard(game_id):
    # returns the card json
    return db.top_discard(s(), game_id).jsonify()

@app.route('/p10/api/top_main/<game_id>')
def top_main(game_id):
    # returns the card json
    return jsonify({'card_id':-1, 'sprite':'/static/back.png'})

@app.route('/p10/api/draw_discard/<game_id>')
def draw_discard(game_id):
    # returns card
    return db.draw_discard(s(), game_id).jsonify()

@app.route('/p10/api/draw_main/<game_id>')
def draw_main(game_id):
    return db.draw_deck(s(), game_id).jsonify()

@app.route('/p10/api/discard/<game_id>/<card_id>')
def discard(game_id, card_id):
    "GOOD if success"
    return jsonify(db.discard(s(), game_id, card_id))

@app.route('/p10/api/down/<game_id>')
def lay_down(game_id):
    if db.check_phase(s(), game_id):
        pass

@app.route('/p10/api/ac/<game_id>')
def get_ac(game_id):
    # return action_counter
    return jsonify(db.get_game(s(), game_id).ac)

@app.route('/p10/api/game_info/<game_id>')
def game_info(game_id):
    # return action_counter
    return db.get_game(s(), game_id).jsonify()

@app.route('/p10/api/sprite/card/<value>-<color>')
def card_sprite(value, color):
    # return action_counter
    return templating.format_card(value, color)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10101)
