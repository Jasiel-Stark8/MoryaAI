"""Application entry point"""
from flask import Flask
from flask_cors import CORS
import pymongo
import sys
from users import db

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://morya:9jj7nsxBsoOT43nL@morya.kxt9fkg.mongodb.net/"
db.init_app(app)

@app.route('/')
def hello():
    return "I am Morya"


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
