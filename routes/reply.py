from flask import (
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.reply import Reply


main = Blueprint('reply', __name__)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    u = current_user()
    # print('DEBUG', form)
    m = Reply.new(form, user_id=u.id)
    # print('reply_m**', m)
    return redirect(url_for('topic.detail', id=m.topic_id))

