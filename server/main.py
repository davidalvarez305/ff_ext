from flask import Flask, make_response, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from flask import request
from bot import execute

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=["POST", "OPTIONS"])
def main():
    load_dotenv()
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    elif request.method == "POST":
        body = request.get_json(force=True)
        print(body['data'])
        execute(body['data'])
        return jsonify({"data": "OK!"})


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
