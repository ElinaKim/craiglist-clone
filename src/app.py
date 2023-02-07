from flask import Flask
import psycopg2
from flask_sqlalchemy import SQLAlchemy
import os 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgrespw@localhost:55000/craigslist"
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db = SQLAlchemy(app)

#conn_str = os.getenv("CONN_STR")

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.VARCHAR(80), unique = True, nullable = False)
    email = db.Column(db.VARCHAR(120), unique = True, nullable = False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def __repr__(self):
        return '<User %r>' %self.username

@app.route('/')
def index():
    return 'Hello World'

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()