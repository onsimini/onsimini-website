from flask import Flask


def create_app():

    app = Flask(__name__)

    from . import admin
    app.register_blueprint(admin.bp)

    from app.error_pages.handlers import error_pages
    app.register_blueprint(error_pages)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
