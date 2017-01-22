from lib.card import Card
from lib.player import Player
from lib.game import Game

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json

engine = create_engine('sqlite:////tmp/p10.db')

s = sessionmaker(bind=engine)()

s.query(Player).filter((Player.player_id == 2)&(Player.game_id == 5)).delete()
s.commit()


