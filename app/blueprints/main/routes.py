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
    context = {
        'title': 'CATALOG',
    }
    return render_template('catalog.html', **context)

@main.route('/patchnotes')
def patchnotes():
    context = {
        'title': 'PATCH NOTES'
    }
    return render_template('patchnotes.html', **context)
   
@main.route('/info')
def info():
    context = {
        'title': 'INFO'
    }
    return render_template('info.html', **context)


# CHARACTERSPAGE pages

@main.route('/allcharacters')
def allcharacters():
    context = {
        'title': 'ALL CHARACTERS'
    }
    return render_template('allcharacters.html', **context)

@main.route('/anainfo')
def anainfo():
    context = {
        'title': 'ANA INFO'
    }
    return render_template('1ana.html', **context)

@main.route('/asheinfo')
def asheinfo():
    context = {
        'title': 'ASHE INFO'
    }
    return render_template('1ashe.html', **context)

@main.route('/dvainfo')
def dvainfo():
    context = {
        'title': 'DVA INFO'
    }
    return render_template('1dva.html', **context)


# OWL pages

@main.route('/owl')
def owl():
    context = {
        'title': 'OWL'
    }
    return render_template('owl.html', **context)

@main.route('/teams')
def teams():
    context = {
        'title': 'TEAMS'
    }
    return render_template('teams.html', **context)