from card import Card

import random

random.seed()
class Deck(object):
    main_pile = []
    discard_pile = []

    def __init__(self):
        
        ## Bootstrap the cards.  12 numbers * 4 colors * 2 of each color/number combination
        for color in (1,1,2,2,3,3,4,4):
            for number in (1,2,3,4,5,6,7,8,9,10,11,12):
                self.main_pile.append(Card(color=color, number=number))

        for x in range(4):
            self.main_pile.append(Card(skip=True))

        for x in range(8):
            self.main_pile.append(Card(wild=True))

        self.shuffle()
    
    def top_main(self):
        if len(self.main_pile) == 0:
            return False
        return self.main_pile[-1]

    def top_discard(self):
        if len(self.discard_pile) == 0:
            return False
        return self.discard_pile[-1]
    
    def _state_check(self):
        if len(self.main_pile) == 1:
            topcard = self.main_pile.pop(0)
            for x in range(len(self.discard_pile)):
                self.main_pile.append(self.discard_pile.pop(0))
            self.main_pile.append(topcard)
            self.shuffle(preserve_top=True)
        return

    def pull_main(self):
        self._state_check()
        return self.main_pile.pop(-1)
        
    def pull_discard(self):
        if len(self.discard_pile) == 0:
            # The client should be checking that there is a discard pile
            return False
        return self.discard_pile.pop(-1)

    def shuffle(self, preserve_top=False):
        end = len(self.main_pile)-1
        if preserve_top:
            end = end-1

        for x in range(5000):
            a = random.randint(0, end)
            b = random.randint(0, end)
            self.main_pile[a], self.main_pile[b] = self.main_pile[b], self.main_pile[a]
        
        return

#    def __str__(self):
#        pass
#
#    def __repr__(self):
#        pass

    def toStr(self):
        out = []
        for card in self.main_pile:
            out.append(card.toString())

        return '\n'.join(out)
