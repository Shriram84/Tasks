from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

@app.route("/testfunc")
def test():
    return "This is my first GET function"

if __name__ == '__main__':
    app.run(port = 5002)
