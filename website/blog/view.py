from flask import Blueprint, render_template
from website.models import Post

blog = Blueprint('blog', __name__, template_folder='templates', static_folder='static')

@blog.route('/')
def index():
    posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)