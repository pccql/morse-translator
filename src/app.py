from dotenv import load_dotenv
from flask import Flask
from controllers.TranslationController import TranslationController

load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello, go to /docs to see the API documentation!</p>"


@app.route("/translate/morseToText/<string:morse>", methods=['GET'])
def morseToText(morse):
    return TranslationController.morseToText(morse)


@app.route("/translate/textToMorse/<string:text>", methods=['GET'])
def textToMorse(text):
    return TranslationController.textToMorse(text)
