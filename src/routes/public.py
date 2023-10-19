"""
    file that contains all the public routes
"""

from flask import render_template, request, redirect, url_for, Blueprint, abort
from database import db
from models import Artwork
import uuid
import random
from flask import session

# blueprint for the public routes
public_routes = Blueprint('public', __name__, url_prefix='/')


@public_routes.route('/')
def index():
    """ route for the home page """
    # random artworks for home page
    if 'cart' not in session:
        session['cart'] = []

    random_artworks = [random.choice(Artwork.query.filter_by(category_id=1).all()), random.choice(Artwork.query.filter_by(category_id=2).all()), random.choice(Artwork.query.filter_by(category_id=3).all())]
    print(random_artworks)
    current_page = 'home'
    return render_template('index.html', current_page=current_page, cache_id=uuid.uuid4(), random_artworks=random_artworks, artworks_in_cart=session['cart'])


@public_routes.route('<category>/')
def each(category):
    """ route for each category """
    if 'cart' not in session:
        session['cart'] = []

    if category == 'painting':
        current_page = 'painting'
        paintings = Artwork.query.filter_by(category_id=1).all()
        rNum = random.choice([4])
        return render_template('painting.html', current_page=current_page, cache_id=uuid.uuid4(), paintings=paintings, rNum=str(rNum), artworks_in_cart=session['cart'])
    elif category == 'print':
        current_page = 'print'
        rNum = random.choice([6])
        prints = Artwork.query.filter_by(category_id=2).all()
        return render_template('prints.html', current_page=current_page, cache_id=uuid.uuid4(), prints=prints, rNum=str(rNum), artworks_in_cart=session['cart'])
    elif category == 'sculpture':
        current_page = 'sculpture'
        rNum = random.choice([6])
        sculptures = Artwork.query.filter_by(category_id=3).all()
        return render_template('sculpture.html', current_page=current_page, cache_id=uuid.uuid4(), sculptures=sculptures, rNum=str(rNum), artworks_in_cart=session['cart'])
    else:
        abort(404)

@public_routes.route('<category>/<int:id>/details')
def details(category, id):
    """ route for each artwork details """
    current_page = category
    artwork = Artwork.query.filter_by(id=id).first()
    similar_artworks = Artwork.query.filter_by(category_id=artwork.categories.id).limit(4).all()

    if 'cart' not in session:
        session['cart'] = []

    if artwork in similar_artworks:
        similar_artworks.remove(artwork)
    print(similar_artworks)
    return render_template('artwork_details.html', current_page=current_page, cache_id=uuid.uuid4(), artwork=artwork, similar_artworks=similar_artworks, artworks_in_cart=session['cart'])

# ---- cart routes ----
@public_routes.route('/cart')
def cart():
    """ route for the cart page """
    total = 0
    # ids = [Artwork.query.filter_by(id=id).first().id]
    if 'cart' in session:
        artworks_in_cart = [Artwork.query.filter_by(id=id).first() for id in session['cart']]
        for artwork in artworks_in_cart:
            total += artwork.price
    else:
        artworks_in_cart = []
    print(artworks_in_cart, total)
    return render_template('cart.html', cache_id=uuid.uuid4(), artworks_in_cart=artworks_in_cart, total_of_prices=total)

@public_routes.route('/add/<int:id>/to_cart')
def add_to_cart(id):
    """ route for adding an artwork to the cart """
    if 'cart' not in session:
        session['cart'] = []
    if id not in session['cart']:
        session['cart'].append(id)

    artworks_in_cart = [ Artwork.query.filter_by(id=id).first() for id in session['cart'] ]
    print(session['cart'])
    print(artworks_in_cart)

    return redirect(url_for('public.cart', cache_id=uuid.uuid4()))

@public_routes.route('/remove/<int:id>/from_cart')
def remove_from_cart(id):
    """ route for removing an artwork from the cart """
    if 'cart' not in session:
        session['cart'] = []
    if id in session['cart']:
        session['cart'].remove(id)

    artworks_in_cart = [ Artwork.query.filter_by(id=id).first() for id in session['cart'] ]
    print(session['cart'])
    print(artworks_in_cart)

    return redirect(url_for('public.cart', cache_id=uuid.uuid4()))

# ---- end cart routes ----

# ---- checkout ----
@public_routes.route('/cart/checkout')
def checkout():
    """ route for the checkout page """
    total = 0
    # ids = [Artwork.query.filter_by(id=id).first().id]
    if 'cart' in session:
        artworks_in_cart = [Artwork.query.filter_by(id=id).first() for id in session['cart']]
        for artwork in artworks_in_cart:
            total += artwork.price
    else:
        artworks_in_cart = []
    print(total, artworks_in_cart)
    return render_template('checkout.html', cache_id=uuid.uuid4(), artworks_in_cart=artworks_in_cart, total=total)