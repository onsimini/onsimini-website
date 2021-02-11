from website import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text())
    author = db.Column(db.String(100))
    date = db.Column(db.String(100))

    def __repr__(self):
        return '<Post {} {}>'.format(self.title,self.content)
