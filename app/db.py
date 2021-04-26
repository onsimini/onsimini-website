from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def dbinit():
    db.create_all()
