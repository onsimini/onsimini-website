from flask import Blueprint, render_template

bp = Blueprint('admin',
               __name__,
               template_folder='templates',
               static_folder='static',
               url_prefix='/admin'
               )


@bp.route('/')
def admin():
    return render_template('admin-index.html')
