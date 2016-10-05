from card import Card
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer

Base = declarative_base()

class Player(Base):
    __table__ = 'player'
    
    game_id = Column(Integer, primary_key=Truea)
    player_id = Column(Integer, primary_key=True)
    current_phase = Column(Integer)
    score = Column(Integer)

    def __init__(self):
        pass

    def rearrange_hand(self, index1, index2):

    def add_card(self, card):
        self.hand.append(card)
        return self.hand

    def drop_card(self, index):
        self.hand.pop(index)

