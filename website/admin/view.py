from flask import current_app, Blueprint, render_template, request, make_response, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from website.models import db, Post
from website.forms import PostForm

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')

@admin.route('/')
def index():
    posts = Post.query.all()
    return render_template('admin/index.html', posts=posts)
