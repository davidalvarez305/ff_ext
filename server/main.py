from flask import Flask

app = Flask(__name__)

@app.route("/", method='POST')
def main():
    return "<p>Hello, World!</p>"