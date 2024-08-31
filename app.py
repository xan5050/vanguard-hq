from flask import Flask, request
import mysql.connector
import json
from mysql.connector import Error

app = Flask(__name__)

@app.route("/decks")
def getDecks():
    try:
        mydb = mysql.connector.connect(

        )
        
        if mydb.is_connected():
            db_info = mydb.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            cursor = mydb.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"You're connected to database: {record}")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM deck")

        columns = [column[0] for column in mycursor.description]
        data = [dict(zip(columns, row)) for row in mycursor.fetchall()]
        json_data = json.dumps(data, indent=4)
        print(json_data)
        return json_data

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return e.msg
    

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"    

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

@app.route("/<deckName>/card", methods = ['POST'])
def addCard(deckName):
    card = request.json
    temporary_deck["cards"].append(card["data"])
    return temporary_deck




if __name__ == "__main__":
    app.run()