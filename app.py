from flask import Flask, request, render_template, Response
import mysql.connector
import json
from mysql.connector import Error

app = Flask(__name__)

def getAllDecks():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="vanguard"
        )
        
    if not mydb.is_connected():
        raise Exception('Failed to connect to database!')
    

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM deck") 

    decks = []
    for (deckid, deck_name, deck_desc) in cursor:
        decks.append({
            "DeckId": deckid,
            "DeckName": deck_name,
            "DeckDescription": deck_desc
        })
    return decks

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


@app.route("/decks")
def getDecks():
    try:
        decks  = getAllDecks()
        return render_template('base.html', decks = decks)
    except Error as e:
        return Response(e.msg, 500)
    
@app.route("/")
def hello_world():
    decks = getAllDecks()
    return render_template("base.html");    

temporary_deck = {
    "name": "Prison",
    "desc": "Control",
    "cards": ["card1", "card2", "card3"]
}
@app.route("/<deckName>/card/<cardName>", methods = ["DELETE"])
def delCard(deckName,cardName):
    temporary_deck["cards"].remove(cardName)
    return temporary_deck

@app.route("/<deckName>")
def deck(deckName):
    return temporary_deck

@app.route("/deck", methods = ['POST'])
def makeDeck():
    deck = request.form 
    addDeck(deck)
    return getDecks(); 

@app.route("/<deckName>/card", methods = ['POST'])
def addCard(deckName):
    card = request.json
    temporary_deck["cards"].append(card["data"])
    return temporary_deck

if __name__ == "__main__":
    app.run()

