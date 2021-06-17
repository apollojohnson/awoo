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

# SHOP pages

@main.route('/shop')
def shop():
    context = {
        'title': 'SHOP',
    }
    return render_template('2shop.html', **context)

@main.route('/cart')
def cart():
    context = {
        'title': 'CART',
    }
    return render_template('2cart.html', **context)

@main.route('/checkout')
def checkout():
    context = {
        'title': 'CHECKOUT',
    }
    return render_template('2checkout.html', **context)

@main.route('/wigs')
def wigs():
    context = {
        'title': 'WIGS',
    }
    return render_template('allwigs.html', **context)

@main.route('/fabric')
def fabric():
    context = {
        'title': 'FABRIC',
    }
    return render_template('allfabric.html', **context)

@main.route('/other')
def other():
    context = {
        'title': 'OTHER'
    }
    return render_template('allother.html', **context)

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

@main.route('/mccreeinfo')
def mccreeinfo():
    context = {
        'title': 'MCCREE INFO'
    }
    return render_template('1mccree.html', **context)

@main.route('/sigmainfo')
def sigmainfo():
    context = {
        'title': 'SIGMA INFO'
    }
    return render_template('1sigma.html', **context)

@main.route('/CaptainAmari')
def CaptainAmari():
    context = {
        'title': 'CAPTAIN AMARI'
    }
    return render_template('CaptainAmari.html', **context)

@main.route('/SigmaCarbonFiber')
def SigmaCarbonFiber():
    context = {
        'title': 'CARBON FIBER'
    }
    return render_template('SigmaCarbonFiber.html', **context)

@main.route('/McCreeClassic')
def McCreeClassic():
    context = {
        'title': 'CLASSIC'
    }
    return render_template('McCreeClassic.html', **context)




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



# PRODUCT pages

@main.route('/longwig')
def longwig():
    context = {
        'title': 'LONG WIG'
    }
    return render_template('3longwig.html', **context)

    
@main.route('/mediumwig')
def mediumwig():
    context = {
        'title': 'MEDIUM WIG'
    }
    return render_template('3mediumwig.html', **context)

    
@main.route('/shortwig')
def shortwig():
    context = {
        'title': 'SHORT WIG'
    }
    return render_template('3shortwig.html', **context)

    
@main.route('/cotton')
def cotton():
    context = {
        'title': 'COTTON'
    }
    return render_template('4cotton.html', **context)

    
@main.route('/fur')
def fur():
    context = {
        'title': 'FUR'
    }
    return render_template('4fur.html', **context)

    
@main.route('/satin')
def satin():
    context = {
        'title': 'SATIN'
    }
    return render_template('4satin.html', **context)


@main.route('/eva')
def eva():
    context = {
        'title': 'EVA FOAM'
    }
    return render_template('5eva.html', **context)

@main.route('/heatgun')
def heatgun():
    context = {
        'title': 'HEAT GUN'
    }
    return render_template('heatgun.html', **context)

@main.route('/hatacc')
def hatacc():
    context = {
        'title': 'HAT ACCESSORIES'
    }
    return render_template('hatacc.html', **context)
