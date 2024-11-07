from flask import Flask, request, render_template, Response
import mysql.connector
import json
from mysql.connector import Error
class cardDB:
    def getAllCards():
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="vanguard"
            )
            
        if not mydb.is_connected():
            raise Exception('Failed to connect to database!')
        

        cursor = mydb.cursor(dictionary = True)
        cursor.execute("select * FROM vanguard.card") 
        records = cursor.fetchall()
        try:
        
            cards = []
            for record in records:
                cards.append({
                    "CardName": record["cardName"],
                    "CardText": record["cardText"],
                    "ImagePath": "../static/" + record["imageName"]

                })
            
            return cards
        except Error as e:
            return Response(e.msg, 500)
