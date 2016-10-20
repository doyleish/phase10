from lib.card import Card
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer

import json

Base = declarative_base()

class Player(Base):
    __tablename__ = 'player'
    
    game_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, primary_key=True)
    phase = Column(Integer)
    score = Column(Integer)
    
    DEFAULTS = {
        'game_id': -1,
        'phase': 1,
        'score': 0
    }

    def __init__(self, **kwargs):
        self.__dict__.update(self.DEFAULTS)
        self.__dict__.update(kwargs)

    def __str__(self):
        return "Game:{} Player:{} Score:{} Phase{}".format(self.game_id,
                                                           self.player_id,
                                                           self.phase,
                                                           self.score)

    def __repr__(self):
        return self.__str__()
    
    def dictify(self):
        return {'id': self.player_id,
                'phase': self.phase,
                'score': self.score}

    def jsonify(self):
        return json.dumps(self.dictify())
