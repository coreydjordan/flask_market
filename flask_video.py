from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from numpy import true_divide
from sqlalchemy import create_engine

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
# engine = create_engine('sqlite:///market.db')

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=False)
    description = db.Column(db.String(length=1000), nullable=False, unique=False)
    
    def __repr__(self):
        return f'Item {self.name}'
db.create_all()
db.session.commit()


def add_items():
    #!users being created in the form of instances
    item1 = Item(name='iPhone 10', price= 500, barcode= 123456789, description= 'desc')
    item2 = Item(name='Laptop', price= 600, description= 'describe', barcode=987654321)
    # item3 = Item(first_name='Dave', last_name='Smith', balance=889)
    # item4 = Item(first_name='Deon', last_name='Criss', balance=908345)
    # item5 = Item(first_name='Danielle', last_name='White', balance=23999)
    # db.session.add(item1)
    # db.session.add(item2)
    db.session.commit()
    return True
add_items()

#!iterate over the items to get all of them
# for item in Item.query.all():
#     print(item.name, item.price)

#!iterate over the items and set a parameter to filter by  
# for item in Item.query.filter_by(price=500):
#     print(item.name)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items = items)


if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)
    