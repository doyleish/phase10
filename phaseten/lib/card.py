

class Card(object):
    # colors
    # 0=black, 1=red, 2=blue, 3=yellow, 4=green
    wild = False
    skip = False
    number = 0
    color = 0
    value = 0
    sprite = "sprite/card/"

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
            prefix = "{}".format(self.number)
            self.value = 5
        
        self.sprite.append("{}-{}".format(prefix, color))
        
            
