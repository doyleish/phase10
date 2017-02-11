from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import lib.db as db

from lib.card import Card
from lib.player import Player
from lib.game import Game

import json

app = Flask(__name__)
engine = create_engine('sqlite:////tmp/p10.db')
url_base = '/apps/phase10'
Card.metadata.create_all(engine)
Player.metadata.create_all(engine)
Game.metadata.create_all(engine)

s = sessionmaker(bind=engine)

def jsonify(val):
    if isinstance(val,dict):
        return json.dumps(val)
    else:
        return json.dumps({"return":val})

@app.route(url_base+'/api/new_game')
def new_game():
    # returns game_id
    return jsonify(db.create_game(s()))

@app.route(url_base+'/api/deal/<game_id>')
def deal_round(game_id):
    # returns player_id for first turn
    return jsonify(db.deal_round(s(), game_id))

@app.route(url_base+'/api/join/<game_id>')
def join_game(game_id):
    # returns player_id of new player
    return jsonify(db.new_player(s(), game_id))

@app.route(url_base+'/api/top_discard/<game_id>')
def top_discard(game_id):
    # returns the card json
    return jsonify(db.top_discard(s(), game_id))

@app.route(url_base+'/api/top_main/<game_id>')
def top_main(game_id):
    # returns the card json
    return jsonify({'card_id':-1, 'sprite':'/static/back.png'})

@app.route(url_base+'/api/draw_discard/<game_id>')
def draw_discard(game_id):
    # returns card
    return jsonify(db.draw_discard(s(), game_id))

@app.route(url_base+'/api/draw_main/<game_id>')
def draw_main(game_id):
    return jsonify(db.draw_main(s(), game_id))

@app.route(url_base+'/api/discard/<game_id>/<card_id>')
def discard(game_id, card_id):
    "GOOD if success"
    return jsonify(db.discard(s(), game_id, card_id))

@app.route(url_base+'/api/skip/<game_id>/<player_id>')
def skip(game_id, player_id):
    return jsonify(db.skip(s(), game_id, player_id))

@app.route(url_base+'/api/down/<game_id>/<cardset>')
def lay_down(game_id, cardset):
    return jsonify(db.lay_down(s(), game_id, cardset))

@app.route(url_base+'/api/hit/<game_id>/<card_id>/<pile_id>/<side>')
def hit(game_id, card_id, pile_id, side):
    return jsonify(db.hit(s(), game_id, card_id, int(pile_id), int(side)))

@app.route(url_base+'/api/ac/<game_id>')
def get_ac(game_id):
    return jsonify(db.get_game(s(), game_id).ac)

@app.route(url_base+'/api/game_info/<game_id>')
def game_info(game_id):
    return db.get_game(s(), game_id).jsonify()

@app.route(url_base+'/api/hand/<game_id>/<player_id>')
def hand(game_id, player_id):
    return jsonify(db.hand(s(), game_id, player_id))

@app.route(url_base+'/api/rearrange/<game_id>/<player_id>/<cardset>')
def rearrange(game_id, player_id, cardset):
    return jsonify(db.rearrange_hand(s(), game_id, player_id, cardset))

@app.route(url_base+'/api/players/<game_id>')
def players(game_id):
    return jsonify(db.get_dict_players(s(), game_id))

@app.route(url_base+'/api/phases/<game_id>')
def phases(game_id):
    return jsonify(db.get_phases(s(), game_id))

if __name__ == "__main__":
    app.run(host='localhost', port=10101)
