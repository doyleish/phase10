from lib.card import Card

_card_template = '\
  <div class="card">\
    <b><font style="font-size: 25pt; background-color: {0}; color: white;">&nbsp{1}&nbsp</font></b>\
  </div>\
'

def format_card(value, color):
    return _card_template.format(Card.COLOR_MAP[color], value)
