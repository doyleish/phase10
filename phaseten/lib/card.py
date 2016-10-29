from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer, String

import json

Base = declarative_base()

COLOR_MAP = ['black', 'red', 'blue', 'gold', 'green']

class Card(Base):
    __tablename__ = "card"

    """ 
    colors
    0=black, 1=red, 2=blue, 3=gold, 4=green
    
    location (2 players)
    -2 = discard
    -1 = main pile
    0 = player 0 hand (player)
    1 = player 1 hand (player)
    2 = phase pile0 (pile+numplayers)
    """

    game_id = Column(Integer, primary_key=True) # game id that the card belongs to
    card_id = Column(Integer, primary_key=True)
    location = Column(Integer) # location of the card
    pos = Column(Integer) # position of the card in its location
    
    wild = Column(Boolean)
    skip = Column(Boolean)
    number = Column(Integer)
    color = Column(Integer)
    value = Column(Integer)
    sprite = Column(String(30))
    
    DEFAULTS = {
        'game_id': -1,
        'location': -1,
        'pos': -1,
        'wild': False,
        'skip': False,
        'number': 0,
        'color': 0,
        'value': 0,
        'sprite': "sprite/card/none.png"
    }

    def __init__(self, **kwargs):
        self.__dict__.update(self.DEFAULTS)
        self.__dict__.update(kwargs)
        
        prefix = ""
        if self.wild:
            prefix = "W"
            self.value = 25
        elif self.skip:
            prefix = "S"
            self.value = 15
        else:
            prefix = self.number
            if self.number >= 10:
                self.value = 10
            else:
                self.value = 5
        
        self.sprite = "/p10/api/sprite/card/{}-{}".format(prefix, self.color)
    
    def __str__(self):
        if self.wild:
            return "Wild"
        elif self.skip:
            return "Skip"
        else:
            return "{} {}".format(COLOR_MAP[self.color], self.number)

    def __repr__(self):
        return self.__str__()
    
    def dictify(self):
        val = ""
        if self.wild:
            val = "W"
        elif self.skip:
            val = "S"
        else:
            val = str(self.number)
        
        return {'card_id': self.card_id,
                'value': val,
                'pos': self.pos,
                'color': COLOR_MAP[self.color]}

    def jsonify(self):
        return json.dumps(self.dictify())

    def __eq__(self, compare):
        if(self.wild or compare.wild):
            return True
        if(self.skip or compare.skip):
            return False
        return (self.number == compare.number)

    def _color(self, compare):
        if(self.wild or compare.wild):
            return True
        if(self.skip or compare.skip):
            return False
        return (self.color == compare.color)

    def __lt__(self, compare):
        if(self.wild or compare.wild):
            return True
        if(self.skip or compare.skip):
            return False
        return (self.number<compare.number)
    
    def __gt__(self, compare):
        if(self.wild or compare.wild):
            return True
        if(self.skip or compare.skip):
            return False
        return (self.number>compare.number)

