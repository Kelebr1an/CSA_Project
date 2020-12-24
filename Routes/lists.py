from flask.blueprints import Blueprint
from flask import render_template
from models.lecturer import Lecturer

lists = Blueprint('lists', __name__,
                  template_folder='templates',
                  static_folder='static')


@lists.route('/lists')
def index():
    return render_template('lists.html', lecturers=Lecturer.query.all())
