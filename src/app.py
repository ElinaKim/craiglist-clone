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


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run()