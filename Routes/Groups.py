from flask.blueprints import Blueprint
from flask import render_template
from models.lecturer import Lecturer
from models.subject import Subject
from models.group import Group

groups = Blueprint('groups', __name__,
                   template_folder='templates',
                   static_folder='static')


@groups.route('/groups')
def index():
    return render_template('groups.html', groups=Group.query.all(), lecturers=Lecturer.query.all(),
                           subjects=Subject.query.all())
