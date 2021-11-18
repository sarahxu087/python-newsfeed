from flask import Blueprint, render_template

bp = Blueprint('content', __name__, url_prefix='/content')

@bp.route('/')
def dash():
  return render_template('content.html')

@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')