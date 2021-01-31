import os
from datetime import datetime
from flask import Flask, render_template, url_for, redirect, flash
from git import Repo
import twython
from website.forms import PostForm

TWITTER_MAX_SIZE = 280

app = Flask(__name__)
repo = Repo('TIL/')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def index():
    filename = 'TIL/test.md'
    with open(filename, 'r') as f:
        text = f.read()
    posts = [
        {
            'author': 'Sion Gontran',
            'title': 'test',
            'body': text,
            'created': 'Janviary 20, 2021'
        }
    ]
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def send_post():
    form = PostForm()
    if form.validate_on_submit():
        message =  f'''# {form.title.data}
'''
        message += f'''### By Gontran Sion, the {datetime.utcnow().strftime("%Y-%m-%d")}.

'''
        message += f'{form.content.data}'
        f = open(f'TIL/{form.title.data}.md', "a")
        f.write(message)
        f.close()
        message = f'[NEW] - {form.title.data} : {form.content.data}'
        message = message[:TWITTER_MAX_SIZE-4]
        message += f' ...'
        make_tweet(message)
        repo.index.add([f'{form.title.data}.md'])
        repo.index.commit(f'Add/Update {form.title.data}.md')
        origin = repo.remote(name='origin')
        origin.pull()
        origin.push()
        flash('Your post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('create.html',
                           title='New Post',
                           form=form,
                           legend='New Post')

def make_api():
    api = twython.Twython(app_key=os.environ.get('TWITTER_APP_KEY'),
                          app_secret=os.environ.get('TWITTER_APP_KEY_SECRET'),
                          oauth_token=os.environ.get('TWITTER_OAUTH_TOKEN'),
                          oauth_token_secret=os.environ.get('TWITTER_OAUTH_TOKEN_SECRET'))
    return api

def make_tweet(message):
    api = make_api()
    api.update_status(status=message)

if __name__ == '__main__':
    app.run()
