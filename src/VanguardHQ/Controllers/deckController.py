from flask import Flask, request, render_template, Response, Blueprint
import mysql.connector
import os
import json
from mysql.connector import Error
from Database.deck_database import deckDB
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
db = deckDB(api_key,api_secret)
deckBP = Blueprint('deck', __name__, url_prefix='/deck', static_folder='../static', static_url_path='/static')

@deckBP.route("/")
def getDecks():
    try:
        decks = db.getAllDecks()
        return render_template('deck.html', decks = decks)
    except Error as e:
        return Response(e.msg, 500)
    
@deckBP.route("/test", methods = ['POST'])
def makeDeck():
    deck = request.form 
    db.addDeck(deck)
    try:
        decks = db.getAllDecks()
        return render_template('deck.html', decks = decks)
    except Error as e:
        return Response(e.msg, 500)
