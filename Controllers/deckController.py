from flask import Flask, request, render_template, Response, Blueprint
import mysql.connector
import json
from mysql.connector import Error
deckBP = Blueprint('deck', __name__, url_prefix='/deck', static_folder='static', static_url_path='/static')
@deckBP.route("/", methods = ['POST'])
def getDecks():
    try:
        return render_template('home.html', decks = [])
    except Error as e:
        return Response(e.msg, 500)
