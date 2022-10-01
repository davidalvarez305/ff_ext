from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from flask import request
from bot import execute

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=["POST"])
def main():
    load_dotenv()
    if request.method == "POST":
        body = request.get_json(force=True)
        execute(body['data'])
        return jsonify({"data": "OK!"})
