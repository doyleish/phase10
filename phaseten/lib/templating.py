from lib.card import Card

_card_template = '
  <div style="position: absolute;
             display: inline-block;
             width: 120px;
             height: 200px;
             border-style: solid;
             border-color: black;
             border-width: 1px;
             border-radius: 3px;
             padding: 5px;
             background-color: white;
             ">
    <b><font style="font-size: 25pt; background-color: {0}; color: white;">&nbsp{1}&nbsp</font></b>
  </div>
'

def format_card(value, color):
    return _card_template.format(Card.COLOR_MAP[color], value)
