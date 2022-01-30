from app import db

class User(db.Model):
    _tablename_ = 'platform_users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String, nullable=False)
    platforms = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.id

