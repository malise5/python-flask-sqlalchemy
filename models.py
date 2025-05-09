from email.mime import image
from operator import ge
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Production(db.Model):
    __tablename__ = 'production'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    imageUrl = db.Column(db.String(200), nullable=True)
    director = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Production {self.title}, {self.genre}, {self.budget}, {self.imageUrl}, {self.director}, {self.description}>'