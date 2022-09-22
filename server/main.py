from flask import Flask
from dotenv import load_dotenv
from flask import request
from bot import execute

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    load_dotenv()
    data = request.get_json(force=True)
    print(data)
    execute()
    return request.args