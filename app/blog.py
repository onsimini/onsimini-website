from flask import Blueprint, render_template
from app.models import Post

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    return render_template('index.html', posts=Post.query.all())
