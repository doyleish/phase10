from lib.card import Card
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer

import json

Base = declarative_base()

class Game(Base):
    __tablename__ = "game"

    game_id = Column(Integer, primary_key=True, autoincrement=True)
    dealer = Column(Integer)
    game_round = Column(Integer)
    player_turn = Column(Integer)
    ac = Column(Integer)
    
    DEFAULTS = {
        'dealer': 0,
        'game_round': 0,
        'player_turn': 0,
        'ac': 0
    }

    def __init__(self):
        self.__dict__.update(self.DEFAULTS)

    def dictify(self):
        return {'title': self.game_id,
                'dealer': self.dealer,
                'round': self.game_round,
                'turn': self.player_turn}
    
    def jsonify(self):
        return json.dumps(self.dictify())

