"""
    file that contains all the public routes
"""

from flask import render_template, request, redirect, url_for, Blueprint, abort
from database import db
from models import Artwork
import uuid
import random
from flask_login import login_user, login_required, logout_user, current_user

# blueprint for the public routes
public_routes = Blueprint('public', __name__, url_prefix='/')


@public_routes.route('/')
def index():
    """ route for the home page """
    # random artworks for home page
    random_artworks = [random.choice(Artwork.query.filter_by(category_id=1).all()), random.choice(Artwork.query.filter_by(category_id=2).all()), random.choice(Artwork.query.filter_by(category_id=3).all())]
    print(random_artworks)
    current_page = 'home'
    return render_template('index.html', current_page=current_page, cache_id=uuid.uuid4(), random_artworks=random_artworks)


@public_routes.route('<category>/')
def each(category):
    """ route for each category """
    if category == 'painting':
        current_page = 'painting'
        paintings = Artwork.query.filter_by(category_id=1).all()
        rNum = random.choice([4])
        return render_template('painting.html', current_page=current_page, cache_id=uuid.uuid4(), paintings=paintings, rNum=str(rNum))
    elif category == 'print':
        current_page = 'print'
        rNum = random.choice([6])
        prints = Artwork.query.filter_by(category_id=2).all()
        return render_template('prints.html', current_page=current_page, cache_id=uuid.uuid4(), prints=prints, rNum=str(rNum))
    elif category == 'sculpture':
        current_page = 'sculpture'
        rNum = random.choice([6])
        sculptures = Artwork.query.filter_by(category_id=3).all()
        return render_template('sculpture.html', current_page=current_page, cache_id=uuid.uuid4(), sculptures=sculptures, rNum=str(rNum))
    else:
        abort(404)

@public_routes.route('<category>/<int:id>/details')
def details(category, id):
    """ route for each artwork details """
    current_page = category
    artwork = Artwork.query.filter_by(id=id).first()
    similar_artworks = Artwork.query.filter_by(category_id=artwork.categories.id).limit(4).all()
    similar_artworks.remove(artwork)
    print(similar_artworks)
    return render_template('artwork_details.html', current_page=current_page, cache_id=uuid.uuid4(), artwork=artwork, similar_artworks=similar_artworks)