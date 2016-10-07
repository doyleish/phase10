from card import Card
from player import Player
from game import Game

def get_game(session, game_id):
    return session.query(Game).filter(Game.game_id == game_id).one()

def get_player(session, game_id, player_id):
    return session.query(Player).filter((Player.player_id == player_id)&(Game.game_id == game_id)).one()

def get_players(session, game_id):
    res = session.query(Player).filter(Game.game_id == game_id).order_by(Player.player_id.asc()).all()
    retval = []
    for x in res:
        retval.append(x)
    return retval

def get_cards(session, game_id, location):
    res = session.query(Card).filter((Card.location == location)&(Game.game_id == game_id)).order_by(Card.pos.asc()).all()
    retval = []
    for x in res:
        retval.append(x)
    return retval

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
        count = 0
        for color in (1,1,2,2,3,3,4,4):
            for number in (1,2,3,4,5,6,7,8,9,10,11,12):
                session.add(Card(game_id=game_id, number=number, pos=count))
                count += 1

        for x in range(4):
            session.add(Card(game_id=game_id, skip=True, pos=count))
            count += 1

        for x in range(8):
            session.add(Card(game_id=game_id, wild=True, pos=count)
            count += 1


def create_game(session):
    game = Game()
    session.add(game)
    session.flush()
    game_id = game.game_id
    new_player(session, game_id)
    _card_bootstrap(session, game_id)
    session.commit()

def new_player(session, game_id):
    session.add(Player(game_id=game_id))
    return

def top_main(session, game_id):
    return get_cards(session, game_id, -1)[-1]

def top_discard(session, game_id):
    return get_cards(session, game_id, -2)[-1]

def draw_main(session, game_id, player_id):
    pile = get_cards(session, game_id, -1)
    discard = get_cards(session, game_id, -2)
    hand = get_cards(session, game_id, player_id)

    _state_check(pile, discard)
    
    pile[-1].location = player_id
    pile[-1].pos = len(hand) # append card to end of hand
    
    session.commit()
    return
    
def draw_discard(session, game_id, player_id):
    discard = get_cards(session, game_id, -2)
    hand = get_cards(session, game_id, player_id)

    pile[-1].location = player_id
    pile[-1].pos = len(hand) # append card to end of hand
    
    session.commit()
    return

def deal_round(session, game_id):
    game = get_game(session, game_id)
    players = get_players(session, game_id)
    dealer = game.game_round%len(players)
    for player in range(dealer+1, (len(players)*10)+dealer+1):
        turn = player%len(players)
        draw_main(session, game_id, turn)

    game.game_round += 1
    game.player_turn = (dealer+1)%len(players)
    session.commit()
    return

def rearrange_hand(session, game_id, player_id, indices):
    hand = get_cards(session, game_id, player_id)
    for index in range(indices):
        hand[indices[index]].pos = index

    session.commit()

def shuffle(pile, preserve_top=False):
    end = len(pile)-1
    if preserve_top:
        end = end-1

    for x in range(5000):
        a = random.randint(0, end)
        b = random.randint(0, end)
        pile[a], pile[b] = pile[b], pile[a]
    
    return
