from flask import render_template, url_for
from app import app


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/404.html')
def four0():
    return render_template('404.html')


@app.route('/faq.html')
def faq():
    return render_template('faq.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')
