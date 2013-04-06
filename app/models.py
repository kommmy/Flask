from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(120),unique=True)
    # role = db.Column(db.SmallInteger, default = ROLE_USER)
    # posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    def __init__(self, username, email,password):
        self.username = username
        self.email = email
        self.password = password
    def __repr__(self):
        return '<User %r>' % (self.username)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)


class Weibo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(60))
    datetime = db.Column(db.DateTime)
    body = db.Column(db.String(140))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Weibo %r>' % (self.body)

