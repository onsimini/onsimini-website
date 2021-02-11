from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

db = SQLAlchemy()
r = FlaskRedis()

def create_app(config_filename):

    app = Flask(__name__)
    app.config.from_object("website.config.DevelopmentConfig")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test3.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    # r.init_app(app)

    with app.app_context():

        from website.admin.view import admin
        from website.blog.view import blog
        app.register_blueprint(admin)
        app.register_blueprint(blog)

        return app
