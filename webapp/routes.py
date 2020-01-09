from webapp import app
from flask import render_template, url_for, jsonify

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/price', methods=['GET', 'POST'])
def price():
    return 'Yay'
