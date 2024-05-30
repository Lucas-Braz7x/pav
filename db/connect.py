from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_connect_db(app):
    db.init_app(app)



