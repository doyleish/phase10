from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('sqlite:///:memory:', echo=True)

def index():
    pass

def newgame():
    pass

def joingame():
    pass

def pull_from_discard():
    pass

def pull_from_deck():
    pass

def discard():
    pass

def lay_down():
    pass

def wait_for_turn():
    thread lock
    pass

app.run(host='0.0.0.0', port=101010)
