import os
import sys
import shutil
from flask import current_app, Blueprint, render_template, request, make_response, redirect, url_for#, Markup
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from website.models import db, Post
from website.forms import PostForm, SubmitForm
from git import Repo
import markdown

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')

@admin.route('/', methods=['GET', 'POST'])
def index():
    form = SubmitForm()
    if form.validate_on_submit():
        #
        if os.path.isdir('./repo'):
            shutil.rmtree('./repo', ignore_errors=True)
        if os.path.isfile('./website/test3.db'):
            os.remove('./website/test3.db')
        #
        repo = Repo.clone_from('git@github.com:onsimini/today-i-learned.git', './repo')
        db.create_all()
        #
        posts = list_files('./repo')
        for post in posts:
            new_post = Post(
                title = post['title'].replace('.md','').replace('-',' '),
                content = markdown.markdown(post['body']),
                author = post['author'],
                date = post['created']
            )
            db.session.add(new_post)
        db.session.commit()
        # remove repo
        shutil.rmtree('./repo', ignore_errors=True)

    return render_template('admin/index.html', form=form)


def list_files(walk_dir):
    posts = []
    for root, subdirs, files in os.walk(walk_dir):
        # Do not go in .git folder
        subdirs[:] = [d for d in subdirs if not '.git' in d]
        # Do not list the root README.md file
        if root == walk_dir:
            files[:] =[f for f in files if not 'README' in f]
        for f in files:
            f_path = f'{root}/{f}'
            with open(f_path) as reader:
                lines = reader.readlines()
                lines = lines[3:]
            new_line = ''
            for line in lines:
                new_line += line
            post = {}
            post['author'] = 'Gontran Sion'
            post['title'] = f
            post['body'] = markdown.markdown(new_line)
            post['created'] = 'Janviary 20, 2021'
            posts.append(post)
    return posts
