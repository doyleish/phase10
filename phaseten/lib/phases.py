
def _set(num, cards):
    if len(cards) != num:
        return False
    for i in range(num):
        if not (cards[i]==cards[i-1]):
            return False

def _run(num, cards):
    if len(cards) != num:
        return False

    for i in range(num)[1:]:
        if not (cards[i-1]<cards[i]):
            return False

    return True

def _colors(num, cards):
    if len(cards) != num:
        return False
    
    for i in range(num):
        if not (cards[i].color(cards[i-1])):
            return False

    return True


def one(cards):
    if len(cards) != 2:
        return False
    
    if not _set(3,cards[0]):
        return False
    if not _set(3,cards[1]):
        return False
    
    return True

def two(cards):
    if len(cards) != 2:
        return False
    
    if not _set(3,cards[0]):
        return False
    if not _run(4,cards[1]):
        return False

    return True
    
def three(cards):
    if len(cards) != 2:
        return False
    
    if not _set(4,cards[0]):
        return False
    if not _run(4,cards[1]):
        return False

    return True
    
def four(cards):
    if len(cards) != 1:
        return False
    
    if not _run(7,cards[0]):
        return False

    return True

def five(cards):
    if len(cards) != 1:
        return False
    
    if not _run(8,cards[0]):
        return False

    return True

def six(cards):
    if len(cards) != 1:
        return False
    
    if not _run(9,cards[0]):
        return False

    return True

def seven(cards):
    if len(cards) != 2:
        return False
    
    if not _set(4,cards[0]):
        return False
    if not _set(4,cards[1]):
        return False

    return True

def eight(cards):
    if len(cards) != 1:
        return False
    
    if not _color(7,cards[0]):
        return False

    return True

def nine(cards):
    if len(cards) != 2:
        return False
    
    if not _set(5,cards[0]):
        return False
    if not _set(2,cards[1]):
        return False

    return True

def ten(cards):
    if len(cards) != 2:
        return False
    
    if not _set(5,cards[0]):
        return False
    if not _set(3,cards[1]):
        return False

    return True

PHASECHECKS = [
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    ten
]
