from database import db
from datetime import datetime
from flask_login import UserMixin

class Admin(UserMixin, db.Model):
    """ Admin model """
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Admin {self.name}> - {self.email}>"

class Artist(db.Model):
    """ Artist model """
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    tel = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # relationship One-to-Many (Artist to Artwork) : "One artist can have many artworks"
    artworks = db.relationship('Artwork', backref='artists', lazy=True)
    def __repr__(self):
        return f"<Artist {self.firstname} {self.lastname} - {self.email}>"

class Category(db.Model):
    """ Category model """
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # relationship One-to-Many (Category to Artwork) : "One category can have many artworks"
    artworks = db.relationship('Artwork', backref='categories', lazy=True)
    def __repr__(self):
        return f"<Category {self.label}>"


class Artwork(db.Model):
    """ Artwork model """
    __tablename__ = 'artworks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Artwork {self.name} {self.categories.label}>"