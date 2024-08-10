from flask import Flask, request

app = Flask(__name__)

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