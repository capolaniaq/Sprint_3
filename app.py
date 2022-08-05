from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/experiences/')
def experiences():
    return render_template('experiences.html')


@app.route('/login/')
def login():
    return render_template('login.html')