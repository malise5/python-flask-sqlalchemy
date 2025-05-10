from email.mime import image
from operator import ge
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin



db = SQLAlchemy()

class Production(db.Model, SerializerMixin):
    __tablename__ = 'productions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    imageUrl = db.Column(db.String(200), nullable=True)
    director = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    crew_members = db.relationship('CrewMember', backref='production', lazy=True)

    #create a serialize rule that will help add our 'crew_members' to the production
    serialize_rules = ('-crew_members.production_id', )


    def __repr__(self):
        return f'<Production Title: {self.title}, Genre: {self.genre}, Budget: {self.budget}, Director: {self.director}, Description: {self.description}, Image URL: {self.imageUrl}, crew_members: {self.crew_members}>'


class CrewMember(db.Model, SerializerMixin):
    __tablename__ = 'crew_members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    #create a serialize rule that will help add our 'production' to the crew_member
    serialize_rules = ('-production.crew_memberS',)

    def __repr__(self):
        return f'<CrewMember Name: {self.name}, Role: {self.role}, Production ID: {self.production_id}>'