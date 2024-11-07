from flask import Flask, request, render_template, Response
import mysql.connector
import json
from mysql.connector import Error
class deckDB:
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

    def getMyDeck():
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="vanguard"
            )
            
        if not mydb.is_connected():
            raise Exception('Failed to connect to database!')
        

        cursor = mydb.cursor(dictionary = True)
        cursor.execute("SELECT * FROM vanguard.cardassignment ca inner join vanguard.card c on c.cardid = ca.cardid inner join vanguard.deck d on d.deckid = ca.deckid where ca.deckid = 1;") 
        records = cursor.fetchall()
        try:
            firstRecord = records[0]
            deck = {}
            deck["name"] = firstRecord["Name"]
            deck["description"] = firstRecord["Des"]
            cards = []
            for record in records:
                cards.append({
                    "CardName": record["cardName"],
                    "CardText": record["cardText"],
                    "ImagePath": "./static/" + record["imageName"]

                })
            deck["cards"] = cards
            return deck
        except Error as e:
            return Response(e.msg, 500)
