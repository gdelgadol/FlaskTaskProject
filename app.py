from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdklfjaklsdjfklajsdhfkjhasdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from routes import *

if __name__ == '__main__':
    app.run(debug=True)