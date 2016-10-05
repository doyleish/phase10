from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer, String

Base = declarative_base()

color_map = ['Black', 'Red', 'Blue', 'Yellow', 'Green']

class Card(Base):
    __table__ = "card"

    """ 
    colors
    0=black, 1=red, 2=blue, 3=yellow, 4=green
    
    location (2 players)
    -2 = discard
    -1 = main pile
    0 = player 0 hand (player)
    1 = player 1 hand (player)
    2 = player 0 phase pile0 (pile+1)*numplayers + player
    3 = player 1 phase pile0
    4 = player 0 phase pile1
    5 = player 1 phase pile1
    """

    game_id = Column(Integer, primary_key=True) # game id that the card belongs to
    location = Column(Integer) # location of the card
    pos = Column(Integer) # position of the card in its location
    
    wild = Column(Boolean)
    skip = Column(Boolean)
    number = Column(Integer)
    color = Column(Integer)
    value = Column(Integer)
    sprite = Column(String(30))
    
    DEFAULTS = {
        'wild': False,
        'skip': False,
        'game_id': 0,
        'card_id': 0,
        'number': 0,
        'color': 0,
        'value': 0,
        'sprite': "sprite/card/none.png"
    }

    def __init__(self, **kwargs):
        self.__dict__.update(DEFAULTS)
        self.__dict__.update(kwargs)
        
        prefix = ""
        if self.wild:
            prefix = "w"
            self.value = 25
        elif self.skip:
            prefix = "s"
            self.value = 15
        else:
            prefix = self.number
            if self.number >= 10:
                self.value = 10
            else:
                self.value = 5
        
        self.sprite = "/sprite/card/{}-{}.png".format(prefix, self.color)

    def __str__(self):
        if self.wild:
            return "Wild"
        elif self.skip:
            return "Skip"
        else:
            return "{} {}".format(color_map[self.color], self.number)

    def __repr__(self):
        return self.__str__()
        
