from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from src.routes.index import initialize_routes
from db.connect import create_connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

create_connect_db(app)

api = Api(app)

initialize_routes(api)



