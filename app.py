from flask import Flask, request, render_template, Response
import mysql.connector
import json
from mysql.connector import Error
from Database.deck_database import deckDB
from Database.card_database import cardDB
from Controllers.deckController import deckBP
from Controllers.cardController import cardBP
app = Flask(__name__)
app.register_blueprint(deckBP)
app.register_blueprint(cardBP)
@app.route("/home")
def getHome():
    try:
        return render_template('home.html', decks = [])
    except Error as e:
        return Response(e.msg, 500)
if __name__ == "__main__":
    app.run()

