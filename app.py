from flask import Flask, request, render_template, Response
import mysql.connector
import json
from mysql.connector import Error
from Database.deck_database import deckDB
from Database.card_database import cardDB
app = Flask(__name__)

def addDeck(deck):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="vanguard"
        )  

    cursor = mydb.cursor()
    sql = "INSERT INTO deck (name, des) VALUES (%s, %s)"
    val = (deck["name"], deck["des"])
    cursor.execute(sql, val)
    mydb.commit()


@app.route("/home")
def getHome():
    try:
        #decks  = getAllDecks()
        return render_template('home.html', decks = [])
    except Error as e:
        return Response(e.msg, 500)
    

@app.route("/card")
def showAllCards():
    try: 
        cards  = cardDB.getAllCards()
        return render_template('card.html',  cards = cards)
    except Error as e:
        return Response(e.msg, 500)

@app.route("/deck", methods = ['POST'])
def makeDeck():
    deck = request.form 
    addDeck(deck)
    return getHome(); 
deckDB.getMyDeck()
if __name__ == "__main__":
    app.run()

