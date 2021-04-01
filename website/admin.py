from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
    )
from werkzeug.security import generate_password_hash
from website.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/', methods=('GET', 'POST'))
def admin():
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
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('admin/index.html')
