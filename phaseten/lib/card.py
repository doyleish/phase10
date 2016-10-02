
color_map = ['Black', 'Red', 'Blue', 'Yellow', 'Green']

class Card(object):
    # colors
    # 0=black, 1=red, 2=blue, 3=yellow, 4=green
    wild = False
    skip = False
    number = 0
    color = 0
    value = 0
    sprite = "sprite/card/none.png"

    def __init__(self, **kwargs):
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

    def toString(self):
        if self.wild:
            return "Wild"
        elif self.skip:
            return "Skip"
        else:
            return "{} {}".format(color_map[self.color], self.number)
        
