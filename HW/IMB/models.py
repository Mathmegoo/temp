from datetime import date

from app import db

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.String(5000), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)

class Comments (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(
        db.Integer,
        db.ForeignKey('articles.id'),
        nullable=False,
        index=True
    )
    article = db.relationship(Articles, foreign_keys=[article_id,])
    content = db.Column(db.String(400), nullable=False)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)
    def __str__(self):
        content = self.content
        return f'Comment is {content}'    
