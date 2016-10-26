
def _set(num, cards):
    if len(cards) != num:
        return False
    for i in range(num):
        if not (cards[i]==cards[i-1]):
            return False

    return True

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
        if not (cards[i]._color(cards[i-1])):
            return False

    return True


def one(cards):
    #import pdb; pdb.set_trace()
    if len(cards) != 2:
        return False
    if not _set(3,cards[0]):
        return False
    if not _set(3,cards[1]):
        return False
    
    return {'set':[cards[0],cards[1]],
            'run':[],
            'color':[]}

def two(cards):
    if len(cards) != 2:
        return False
    if not _set(3,cards[0]):
        return False
    if not _run(4,cards[1]):
        return False

    return {'set':[cards[0]],
            'run':[cards[1]],
            'color':[]}
    
def three(cards):
    if len(cards) != 2:
        return False
    if not _set(4,cards[0]):
        return False
    if not _run(4,cards[1]):
        return False

    return {'set':[cards[0]],
            'run':[cards[1]],
            'color':[]}
    
def four(cards):
    if len(cards) != 1:
        return False
    if not _run(7,cards[0]):
        return False

    return {'set':[],
            'run':[cards[0]],
            'color':[]}

def five(cards):
    if len(cards) != 1:
        return False
    if not _run(8,cards[0]):
        return False

    return {'set':[],
            'run':[cards[0]],
            'color':[]}

def six(cards):
    if len(cards) != 1:
        return False
    if not _run(9,cards[0]):
        return False

    return {'set':[],
            'run':[cards[0]],
            'color':[]}

def seven(cards):
    if len(cards) != 2:
        return False
    if not _set(4,cards[0]):
        return False
    if not _set(4,cards[1]):
        return False

    return {'set':[cards[0],cards[1]],
            'run':[],
            'color':[]}

def eight(cards):
    if len(cards) != 1:
        return False
    if not _color(7,cards[0]):
        return False

    return {'set':[],
            'run':[],
            'color':[cards[0]]}

def nine(cards):
    if len(cards) != 2:
        return False
    if not _set(5,cards[0]):
        return False
    if not _set(2,cards[1]):
        return False

    return {'set':[cards[0],cards[1]],
            'run':[],
            'color':[]}

def ten(cards):
    if len(cards) != 2:
        return False
    if not _set(5,cards[0]):
        return False
    if not _set(3,cards[1]):
        return False

    return {'set':[cards[0],cards[1]],
            'run':[],
            'color':[]}

PHASECHECKS = [
    None,
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
