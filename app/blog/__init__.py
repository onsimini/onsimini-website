from flask import Blueprint, render_template

bp = Blueprint('blog',
               __name__,
               template_folder='templates',
               static_folder='static'
               )


@bp.route('/')
def index():
    return render_template('blog-index.html')

@bp.route('/post/<id>')
def blogPost(id):
    return "<h1>post {}</h1>".format(id)
