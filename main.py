from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__, template_folder='templates')

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)