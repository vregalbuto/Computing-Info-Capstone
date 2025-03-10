from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class NBAStats(db.Model):
    __tablename__ = 'nbastats'
    TEAM_NAME = db.Column(db.String(120), primary_key=True)
    GAME_ID = db.Column(db.String(64))
    GAME_DATE = db.Column(db.DateTime())
    MATCH_UP = db.Column(db.String(120))
    WIN_LOSS = db.Column(db.String(64))
    PTS = db.Column(db.Float())
    FG_PCT = db.Column(db.Float())
    FG3_PCT = db.Column(db.Float())
    FT_PCT = db.Column(db.Float())
    REB = db.Column(db.Float())
    AST = db.Column(db.Float())
    STL = db.Column(db.Float())
    BLK = db.Column(db.Float())
    TOV = db.Column(db.Float())
    PLUS_MINUS = db.Column(db.Float())
    #avg_price = db.Column(db.Float())


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
#   posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# class Post(db.Model):
#     __tablename__ = 'posts'
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     def __repr__(self):
#         return '<Post {}'.format(self.body)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



