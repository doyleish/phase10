from lib.card import Card
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer

Base = declarative_base()

class Game(Base):
    __tablename__ = "game"

    game_id = Column(Integer, primary_key=True, autoincrement=True)
    dealer = Column(Integer)
    game_round = Column(Integer)
    player_turn = Column(Integer)
    
    DEFAULTS = {
        'dealer': 0,
        'game_round': 0,
        'player_turn': 0
    }

    def __init__(self):
        self.__dict__.update(self.DEFAULTS)

        #TODO
        # bootstrap cards
        # shuffle cards
        # 
