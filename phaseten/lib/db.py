from lib.card import Card
from lib.player import Player
from lib.game import Game
import lib.phases as phases
import random

def get_game(session, game_id):
    return session.query(Game).filter(Game.game_id == game_id).one()

def get_player(session, game_id, player_id):
    return session.query(Player).filter((Player.player_id == player_id)&(Player.game_id == game_id)).one()

def get_players(session, game_id):
    res = session.query(Player).filter(Player.game_id == game_id).order_by(Player.player_id.asc()).all()
    retval = []
    for x in res:
        retval.append(x)
    return retval

def get_card(session, game_id, card_id):
    retval = session.query(Card).filter((Card.card_id == card_id)&(Card.game_id == game_id)).order_by(Card.pos.asc()).one()
    return retval

def get_cards(session, game_id, location):
    res = session.query(Card).filter((Card.location == location)&(Card.game_id == game_id)).order_by(Card.pos.asc()).all()
    retval = []
    for x in res:
        retval.append(x)
    return retval

def get_all_cards(session, game_id):
    res = session.query(Card).filter((Card.game_id == game_id)).order_by(Card.pos.asc()).all()
    retval = []
    for x in res:
        retval.append(x)
    return retval

def get_dict_players(session, game_id):
    ret = []
    for x in get_players(session, game_id):
        ret.append(x.dictify())
    return ret

def round_over_check(session, game_id):
    players = get_players(session, game_id)
    for player in players:
        hand = get_cards(session, game_id, player.player_id)
        if len(hand) == 0:
            return True

    return False

def set_hand_order(session, game_id):
    game = get_game(session, game_id)
    hand = get_cards(session, game_id, game.player_turn)
    for i in range(len(hand)):
        hand[i].pos = i

    game.ac+=1
    session.flush()


def inc_turn(session, game_id):
    game = get_game(session, game_id)
    players = get_players(session, game_id)
    if round_over_check(session, game_id):
        end_round(session, game_id)
        return
    
    game.player_turn = (game.player_turn+1)%len(players)
    while(True):
        if(players[game.player_turn].skip > 0):
            players[game.player_turn].skip -= 1
            game.player_turn = (game.player_turn+1)%len(players)
        else:
            break
    game.ac+=1
    session.commit()

def end_round(session, game_id):
    game = get_game(session, game_id)
    players = get_players(session, game_id)
    
    # tally scores
    for player in players:
        hand = get_cards(session, game_id, player.player_id)
        player.down = False
        for card in hand:
            player.score+=card.value
    
    cards = get_all_cards(session, game_id)
    for i in range(len(cards)):
        cards[i].location = -1
        cards[i].pos = i
    
    game.piles_set = 0
    game.piles_run = 0
    game.piles_color = 0
    
    game.game_round += 1
    game.dealer = (game.dealer+1)%len(players)
    game.player_turn = game.dealer
    game.ac+=1
    
    session.commit()

def hit(session, game_id, card_id, pile_id, side):
    game = get_game(session, game_id)
    players = get_players(session, game_id)
    card = get_card(session, game_id, card_id)
    pile = get_cards(session, game_id, pile_id)
    
    if side:
        pile.append(card)
    else:
        pile.insert(0,card)
    
    test = None
    
    if pile_id < 200:
        test = phases._set
    elif pile_id < 300:
        test = phases._run
    elif pile_id < 400:
        test = phases._color
    else:
        return

    if test(len(pile), pile):
        for i in range(len(pile)):
            pile[i].location = pile_id
            pile[i].pos = i
        session.flush()
        set_hand_order(session, game_id)
        
        if round_over_check(session, game_id):
            end_round(session, game_id)
            return
        
        game.ac+=1
    
    session.commit()
    

def lay_down(session, game_id, cardset):
    game = get_game(session, game_id)
    player = get_player(session, game_id, game.player_turn)
    hand = get_cards(session, game_id, game.player_turn)
    
    cards = []
    for subset in cardset.strip('_').split("_"):
        sv = []
        for c in subset.strip('-').split('-'):
            sv.append(get_card(session, game_id, c))
        cards.append(sv)

    # import pdb; pdb.set_trace()

    check = phases.PHASECHECKS[player.phase](cards)
    if(check):
        player.down = True
        player.phase+=1
        if(player.phase>10):
            game.player_turn = -1
            game.dealer = -1
        for pile in check['set']:
            i = 0
            for card in pile:
                card.location = 100+game.piles_set
                card.pos = i
                i+=1
            game.piles_set+=1

        for pile in check['run']:
            i = 0
            for card in pile:
                card.location = 200+game.piles_run
                card.pos = i
                i+=1
            game.piles_run+=1

        for pile in check['color']:
            i = 0
            for card in pile:
                card.location = 300+game.piles_color
                card.pos = i
                i+=1
            game.piles_color+=1
        
        game.ac+=1
        session.flush()
        set_hand_order(session, game_id)
        session.commit()
        return "Good"
    else:
        return "Bad"


def get_phases(session, game_id):
    game = get_game(session, game_id)
    players = get_players(session, game_id)
    piles_set = game.piles_set
    piles_run = game.piles_run
    piles_color = game.piles_color
    ret = {}
    for phase in list(range(100,100+piles_set))+list(range(200,200+piles_run))+list(range(300,300+piles_color)):
        ret[phase] = []
        cards = get_cards(session, game_id, phase)
        for card in cards:
            c = card.dictify()
            ret[phase].append(c)
    return ret


def _state_check(main_pile, discard_pile):
    if len(main_pile) == 1:
        topcard = main_pile.pop(0)
        for x in range(len(discard_pile)-1):
            main_pile.append(discard_pile.pop(0))
        main_pile.append(topcard)
        shuffle(main_pile, preserve_top=True)
    
    for x in range(len(discard_pile)):
        discard_pile[x].pos = x
    
    for x in range(len(main_pile)):
        main_pile[x].pos = x

    return

def _card_bootstrap(session, game_id):
        # mfw SQLite doesn't support autoinc on composite primary keys :(
        count = 0
        
        for x in range(4):
            session.add(Card(game_id=game_id, skip=True, pos=count, card_id=count))
            count += 1
        
        for x in range(8):
            session.add(Card(game_id=game_id, wild=True, pos=count, card_id=count))
            count += 1
        
        for color in (1,1,2,2,3,3,4,4):
            for number in (1,2,3,4,5,6,7,8,9,10,11,12):
                session.add(Card(game_id=game_id, number=number, color=color, pos=count, card_id=count))
                count += 1

def create_game(session):
    game = Game()
    session.add(game)
    session.flush()
    game_id = game.game_id
    _card_bootstrap(session, game_id)
    session.commit()
    return game_id

def new_player(session, game_id):
    game = get_game(session, game_id)
    num = len(get_players(session, game_id))
    new_player = Player(game_id=game_id, player_id=num)
    print(new_player.__dict__)
    session.add(new_player)
    session.flush()
    pid = new_player.player_id
    game.ac += 1
    session.commit()
    return pid

def top_main(session, game_id):
    return get_cards(session, game_id, -1)[-1]

def top_discard(session, game_id):
    stack = get_cards(session, game_id, -2)
    if len(stack):
        return stack[-1].dictify()
    else:
        return {'card_id':-1}

def draw_main(session, game_id, player_id=-1):
    game = get_game(session, game_id)
    if player_id<0:
      player_id = game.player_turn
    
    pile = get_cards(session, game_id, -1)
    discard = get_cards(session, game_id, -2)
    hand = get_cards(session, game_id, player_id)

    _state_check(pile, discard)
    
    pile[-1].location = player_id
    pile[-1].pos = len(hand) # append card to end of hand
    
    game.ac += 1
    session.commit()
    return "GOOD"
    
def draw_discard(session, game_id):
    game = get_game(session, game_id)
    player_id = game.player_turn
    
    discard = get_cards(session, game_id, -2)
    hand = get_cards(session, game_id, player_id)

    if (not len(discard)):
        return "BAD"

    discard[-1].location = player_id
    discard[-1].pos = len(hand) # append card to end of hand
    
    game.ac += 1
    session.commit()
    return "GOOD"

def skip(session, game_id, player_id):
    player = get_player(session, game_id, player_id);
    player.skip += 1;
    session.commit()
    return "GOOD"

def discard(session, game_id, card_id):
    game = get_game(session, game_id)
    card = get_card(session, game_id, card_id)
    
    players = get_players(session, game_id)
    
    discard_pile = get_cards(session, game_id, -2)
    card.location = -2
    card.pos = len(discard_pile)
    session.flush
    set_hand_order(session, game_id)
    
    inc_turn(session, game_id)
    return "GOOD"



def hand(session, game_id, player_id):
    cards = get_cards(session, game_id, player_id)
    rv = {'return': []}
    for card in cards:
        tmp = card.dictify()
        rv['return'].append(tmp)

    return rv


def deal_round(session, game_id):
    # set up deck
    cards = get_all_cards(session, game_id)
    for card in cards:
        card.location = -1
    shuffle(cards)

    # deal out cards
    game = get_game(session, game_id)
    players = get_players(session, game_id)
    dealer = game.dealer
    for player in range(dealer+1, (len(players)*10)+dealer+1):
        turn = player%len(players)
        draw_main(session, game_id, player_id=turn)
    
    # update game obj to reflect next round
    game.game_round += 1
    
    inc_turn(session, game_id)

    return "GOOD"

def rearrange_hand(session, game_id, player_id, cardset):
    hand = get_cards(session, game_id, player_id)
    cards = []
    for cid in cardset.split('-'):
        cards.append(get_card(session, game_id, cid))
    for card in range(len(cards)):
        cards[card].pos = card
    
    session.commit()
    return "GOOD"

def shuffle(pile, preserve_top=False):
    end = len(pile)-1
    if preserve_top:
        end = end-1

    for x in range(5000):
        a = random.randint(0, end)
        b = random.randint(0, end)
        pile[a], pile[b] = pile[b], pile[a]
    
    for x in range(len(pile)):
        pile[x].pos = x
    return
