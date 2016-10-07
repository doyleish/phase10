from card import Card
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer

Base = declarative_base()

class Player(Base):
    __table__ = 'player'
    
    game_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, primary_key=True, auto_increment=True)
    current_phase = Column(Integer)
    score = Column(Integer)
    
    DEFAULTS = {
        'game_id': -1,
        'current_phase': 1,
        'score': 0
    }

    def __init__(self, **kwargs):
        self.__dict__.update(DEFAULTS)
        self.__dict__.update(kwargs)

    def __str__(self):
        return "Game:{} Player:{} Score:{} Phase{}".format(self.game_id,
                                                           self.player_id,
                                                           self.current_phase,
                                                           self.score)

    def __repr__(self):
        return self.__str__()
