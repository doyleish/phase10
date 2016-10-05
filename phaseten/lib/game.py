from card import Card
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer

Base = declarative_base()

class Game(Base):
    __table__ = "game"

    game_id = Column(Integer, primary_key=0, auto_increment=True)
    dealer = Column(Integer)
    game_round = Column(Integer)
    player_turn = Column(Integer)
    
    DEFAULTS = {
        'dealer': 0,
        'game_round': 0,
        'player_turn': 0
    }

    def __init__(self):
        self.__dict__.update(DEFAULTS)

        #TODO
        # bootstrap cards
        # shuffle cards
        # 

    def new_player(self):
        index = len(self.players)
        self.players.append(Player())
        return index
    
    def next_turn(self):
        self.player_turn = (self.player_turn + 1) % num_players

    def deal(self):
        
        tmp_players = []
        #TODO load all players with game id from db

        num_players = len()
        for x in range(num_players*10)
            index = (x + self.player_turn) % num_players

    def draw_main(self):
        self.players[index].add_card(self.deck.draw_main())
        return

    def draw_discard(self, player):
        self.players[index].add_card(self.deck.draw_discard())
        return

