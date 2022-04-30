from dotenv import load_dotenv
from flask import Flask, request
from flask_redis import FlaskRedis

from controllers.TranslationController import TranslationController
from utils.populateDatabase import populateDatabase

load_dotenv()

app = Flask(__name__)
redis_client = FlaskRedis(app, decode_responses=True)
populateDatabase(redis_client)


@app.route("/")
def index():
    return "<p>Hello, go to /docs to see the API documentation!</p>"


@app.route("/decrypt", methods=['GET'])
def decrypt():
    morse = request.json["message"]

    return TranslationController.decrypt(morse)


@app.route("/encrypt", methods=['GET'])
def encrypt():
    text = request.json["message"]

    return TranslationController.encrypt(text)
