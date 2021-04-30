from flask import Blueprint, render_template

error_pages = Blueprint('error_pages',
                        __name__,
                        template_folder='templates',
                        static_folder='static')


@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_404.html'), 404
