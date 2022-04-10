from enum import unique
from market import db

class User(db.model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.column(db.String(length=30), nullable=False, unique=True)
    email_address = db.column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.column(db.String(length=60), nullable=False)
    budget = db.column(db.Integer, nullable=False, default=1000)
    items = db.relationship('Items', backref='owener_used', lazy=True)
    
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=False)
    description = db.Column(db.String(length=1000), nullable=False, unique=False)
    owner = db.Column(db.Integer(), db.ForeignKey())
    
    def __repr__(self):
        return f'Item {self.name}'