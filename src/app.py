from dotenv import load_dotenv
from flask import Flask, request
from flask_redis import FlaskRedis
from config.swaggerConfig import swagger_blueprint

from controllers import TranslationController
from utils import populateDatabase
from adapters import RedisAdapter

load_dotenv()

app = Flask(__name__)

redis_client = FlaskRedis(app, decode_responses=True)
database_client = RedisAdapter(redis_client)

populateDatabase(database_client)
app.register_blueprint(swagger_blueprint)


@app.route("/")
def index():
    return "<h3>Hello, go to /docs to see the API documentation!</h3>"


@app.route("/decrypt", methods=['POST'])
def decrypt():
    morse = request.json["message"]

    return TranslationController.decrypt(morse)


@app.route("/encrypt", methods=['POST'])
def encrypt():
    text = request.json["message"]

    return TranslationController.encrypt(text)
