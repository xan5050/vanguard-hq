from flask import Flask, request, render_template, Response, Blueprint
import mysql.connector
import json
from mysql.connector import Error
from Database.card_database import cardDB
cardBP = Blueprint('card', __name__, url_prefix='/card', static_folder='../static', static_url_path='/static')
@cardBP.route("/")
def showAllCards():
    try: 
        cards  = cardDB.getAllCards()
        return render_template('card.html',  cards = cards)
    except Error as e:
        return Response(e.msg, 500)