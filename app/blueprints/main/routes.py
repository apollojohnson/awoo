from . import bp as main
from flask import render_template
from app.blueprints.blog.models import Post

@main.route('/')
def index():
    context = {
       'title': 'HOME',
       'posts': Post.query.all()
    }
    return render_template('index.html', **context)

@main.route('/catalog')
def catalog():
    return render_template('catalog.html')

@main.route('/owl')
def owl():
    return render_template('owl.html')

@main.route('/patchnotes')
def patchnotes():
    return render_template('patchnotes.html')