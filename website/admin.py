from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from website.db import get_db


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/', methods=('GET', 'POST'))
def admin():
    db = get_db()
    error = None

    users = db.execute(
        'SELECT username '
        'FROM user'
    ).fetchall()

    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username '
        'FROM post p JOIN user u ON p.author_id = u.id',
    ).fetchall()

    var_site = db.execute(
        'SELECT * '
        'FROM var_site'
    ).fetchall()

    if request.method == 'POST':
        if request.form['logout']:
            session.clear()
            return redirect(url_for('admin.admin'))

    if error:
        flash(error)

    return render_template('admin/index.html',
                           posts=posts,
                           users=users,
                           var_site=var_site)


@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('admin.admin'))

        flash(error)

    return render_template('admin/index.html')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('admin.admin'))

        flash(error)

    return render_template('admin/index.html')


@bp.route('/delete_user', methods=('GET', 'POST'))
def delete_user():
    if request.method == 'POST':
        usr = request.form['user']
        db = get_db()
        db.execute('DELETE FROM user WHERE username = ?', (str(usr),))
        db.commit()
    return redirect(url_for('admin.admin'))


@bp.route('/add_post', methods=('GET', 'POST'))
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['editordata']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id) '
                'VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('admin.admin'))

    return render_template('admin/index.html')
