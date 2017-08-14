from models.mongua import Mongua
from models.user import User
from models.reply import Reply
from models.board import Board


class Topic(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('views', int, 0),
        ('title', str, ''),
        ('content', str, ''),
        ('user_id', int, 0),
        ('board_id', int, 0),
    ]

    @classmethod
    def get(cls, id):
        # print('id', id)
        m = cls.find_by(id=id)
        # print('topic_m', m)
        m.views += 1
        m.save()
        return m

    def replies(self):
        ms = Reply.find_all(topic_id=self.id)
        return ms

    def board(self):
        m = Board.find(self.board_id)
        return m

    def user(self):
        u = User.find(id=self.user_id)
        return u

