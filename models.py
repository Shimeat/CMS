from app import db

class User(db.Model):
    _tablename_ = 'platform_users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String, nullable=False)
    platforms = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.id

class Platforms(db.Model):
    _tablename_ = "platforms"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    id_head = db.Column(db.Integer)
    id_group = db.Column(db.Integer)


class GroupsPlatforms(db.Model):
    _tablename_ = "group_platforms"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
