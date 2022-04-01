from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/homee')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': 123456789, 'price': 500},
        {'id': 2, 'name': 'MacBook', 'barcode': 987654321, 'price': 700},
        {'id': 3, 'name': 'Keyboard', 'barcode': 2468101214, 'price': 100},
        {'id': 4, 'name': 'Keyboard', 'barcode': 2468101215, 'price': 100}
        ]
    return render_template('market.html', items = items)


if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)
    