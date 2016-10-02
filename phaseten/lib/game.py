

class game(object):
    joinable = True
    dealer = 0
    turn = 1
    
    players = []
    
    deck = None

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def new_player(self):
        index = len(self.players)
        self.players.append(Player())
        return index

    def deal(self):
        self.joinable = False
        num_players = len(self.players)
        for x in range(num_players*10)
            index = x % num_players
            self.players[index].hand.append(self.deck.draw_main())

    def draw_main(self, player):
        self.players[index].hand.append(self.deck.draw_main())
        return

    def draw_discard(self, player):
        self.players[index].hand.append(self.deck.draw_discard())
        return

