
class Player(object):
    # phase types
    # 0 = set, 1 = run, 2 = color
    hand = [] # list of cards. re-orderable
    current_phase = 0
    score = 0

    
    down_phases = {}

    def __init__(self):
        pass

    def rearrange_hand(self, index1, index2):
        self.hand[index1], self.hand[index2] = self.hand[index2], self.hand[index1]

    def add_card(self, card):
        self.hand.append(card)
        return self.hand

    def drop_card(self, index):
        self.hand.pop(index)

