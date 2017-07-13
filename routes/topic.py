from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.topic import Topic
from models.board import Board

import uuid

main = Blueprint('topic', __name__)
csrf_tokens = dict()


@main.route("/")
def index():
    # board_id = 2
    board_id = int(request.args.get('board_id', -1))
    if board_id == -1:
        ms = Topic.all()
    else:
        ms = Topic.find_all(board_id=board_id)
    token = str(uuid.uuid4())
    u = current_user()
    csrf_tokens[token] = u.id
    bs = Board.all()
    return render_template("topic/index.html",
                           ms=ms,
                           token=token,
                           bs=bs,
                           u=u,
                           bid=board_id,
                           )


@main.route('/<int:id>')
def detail(id):
    u = current_user()
    t = Topic.get(id)
    # 传递 topic 的所有 reply 到 页面中
    return render_template("topic/detail.html", topic=t, u=u)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    token = request.args.get('token')
    if token in csrf_tokens and csrf_tokens[token] == u.id:
        csrf_tokens.pop(token)
    m = Topic.new(form, user_id=u.id)
    return redirect(url_for('.detail', id=m.id))


@main.route("/delete")
def delete():
    id = int(request.args.get('id'))
    token = request.args.get('token')
    u = current_user()
    topic = Topic.find(id)
    # 判断 token 是否是我们给的
    # print(u.id, token, csrf_tokens)
    if token in csrf_tokens and csrf_tokens[token] == topic.user_id:
        csrf_tokens.pop(token)
        print('删除 topic 用户是', u, id)
        topic.delete()
        return redirect(url_for('.index'))
    else:
        abort(401)


@main.route("/new")
def new():
    board_id = int(request.args.get('board_id', -1))
    token = str(uuid.uuid4())
    u = current_user()
    csrf_tokens[token] = u.id
    bs = Board.all()
    return render_template("topic/new.html", bs=bs, bid=board_id, token=token)
