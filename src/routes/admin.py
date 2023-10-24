"""
    file that contains all the routes for the admin panel
"""

from flask import render_template, request, redirect, url_for, Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from models import Admin, Category, Artwork, Artist, Client
import uuid
import os
from flask_login import login_user, login_required, logout_user, current_user

admin_routes = Blueprint('admin', __name__, url_prefix='/admin')

#----------------------------------------------
# fucntion to check if the file is allowed, have extensions jpg, png or jpeg
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# ---------------------------------------------

# -------------------  auth routes -------------------

# signup route
@admin_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    """ route for the admin signup page """
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if request.method == 'POST':
        print(email, password)
        if len(password) < 8:
            return render_template('admin/signup.html', error='Your password must be at least 8 characters long.')
        admin = Admin.query.filter_by(email=email).first()
        if admin:
            return render_template('admin/signup.html', error='Email address already exists')
        new_admin = Admin(name=name, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_admin)
        db.session.commit()

        return redirect(url_for('admin.login'))
    else : #request.method == 'GET':
        return render_template('admin/signup.html')

# login route
@admin_routes.route('/login', methods=['GET','POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if request.method == 'POST':
        admin = Admin.query.filter_by(email=email).first()
        print(admin,check_password_hash(admin.password, password))
        if not admin or not check_password_hash(admin.password, password) :
            return render_template('admin/login.html', error='Email or password incorrect. Please check your login details and try again.')

        login_user(admin)
        return redirect(url_for('admin.main'))
    else :
        return render_template('admin/login.html')

# logout route
@admin_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))

# ------------------- end auth routes -------------------


# -------------------- main routes --------------------
@admin_routes.route('/')
@login_required
def main():
    current_page = 'home'
    cache_id = uuid.uuid4()
    print(cache_id)
    print(f"Current admin name : {current_user.name}")
    artists = Artist.query.all()
    artworks = Artwork.query.all()
    clients = Client.query.all()
    return render_template('admin/index.html', cache_id=cache_id, current_page=current_page, current_admin_name=current_user.name, artists=artists, artworks=artworks, clients=clients)

# ------------------- end main routes -------------------

# -------------------  artwork routes -------------------
@admin_routes.route('/artworks')
@login_required
def view_artworks():
    current_page = 'artworks'
    all_artworks = Artwork.query.all()
    paintings = Artwork.query.filter_by(category_id=1).all()
    prints = Artwork.query.filter_by(category_id=2).all()
    sculptures = Artwork.query.filter_by(category_id=3).all()

    print(paintings,prints,sculptures)
    return render_template('admin/artworks.html', current_page=current_page,paintings=paintings, prints=prints, sculptures=sculptures, all_artworks=all_artworks)

@admin_routes.route('/artworks/add', methods=['GET', 'POST'])
@login_required
def add_artwork():
    current_page = 'artworks'
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    category_id = request.form.get('category')
    artist_id = request.form.get('artist')
    category = Category.query.filter_by(id=category_id).first()

    if request.method == 'POST':
        print(request.files)
        if 'image' not in request.files:
            return render_template('admin/add_artwork_1.html', error='No file part')
        
        file = request.files['image']
        if file.filename == '':
            return render_template('admin/add_artwork_1.html', error='No selected file')
        
        print(file)
        if file and allowed_file(file.filename):
            filename = file.filename
            image_url = 'static/images/' + category.label + '/' + filename
            file.save(image_url)
            print(filename)
        new_artwork = Artwork(name=name.capitalize(), description=description, price=price, category_id=category_id, artist_id=artist_id, image_url=image_url)
        db.session.add(new_artwork)
        db.session.commit()
        return redirect(url_for('admin.view_artworks'))
    return render_template('admin/add_artwork_1.html', cache_id=uuid.uuid4(), current_page=current_page, categories=Category.query.all(), artists=Artist.query.all())

@admin_routes.route('/artworks/<int:id>/details', methods=['GET', 'POST'])
@login_required
def view_artwork_details(id):
    return f"Artwork { id }" 


# ------------------- end artwork routes -------------------


# -------------------  artist routes -------------------
@admin_routes.route('/artists')
@login_required
def view_artists():
    current_page = 'artists'
    return render_template('admin/artists.html', current_page=current_page, artists=Artist.query.all())


@admin_routes.route('/artists/add', methods=['GET', 'POST'])
@login_required
def add_artist():
    current_page = 'artists'
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')   
    email = request.form.get('email')
    tel = request.form.get('tel')
    country = request.form.get('country')
    city = request.form.get('city')
    password = request.form.get('password')

    if request.method == 'POST':
        if len(password) < 8:
            return render_template('admin/add_artist.html', error='The password must be at least 8 characters long.')
        artist = Artist.query.filter_by(email=email).first()
        if artist:
            return render_template('admin/add_artist.html', error='Email address already exists')
        
        picture = request.files['picture']
        if picture.filename == '':
            return render_template('admin/add_artist.html', error='No selected profile picture')
        
        if picture and allowed_file(picture.filename):
            picture_url = 'static/images/profile_pictures/' + picture.filename
            picture.save(picture_url)
            print(picture.filename)
            new_artist = Artist(firstname=firstname.upper(), lastname=lastname.capitalize(), email=email, tel=tel, country=country, city=city, picture_url=picture_url, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_artist)
            db.session.commit()
            return redirect(url_for('admin.view_artists'))
    return render_template('admin/add_artist.html', cache_id=uuid.uuid4(), current_page=current_page)

@admin_routes.route('/artists/<int:id>/details')
@login_required
def view_artist_details(id):
    """ route for the artist details"""
    artist = Artist.query.filter_by(id=id).first()
    return jsonify({
            'firstname': artist.firstname,
            'lastname': artist.lastname,
            'email': artist.email,
            'tel': artist.tel,
            'country': artist.country,
            'city': artist.city,
            'picture_url': url_for('static', filename='images/profile_pictures/' + artist.picture_url.split('/')[-1]),
            'count': len(artist.artworks)
        }
)
# ------------------- end artist routes -------------------


# -------------------  client routes -------------------
@admin_routes.route('/clients')
@login_required
def view_clients():
    current_page = 'clients'
    clients = Client.query.all()
    print(clients)
    return render_template('admin/clients.html', current_page=current_page, clients=clients)

# ------------------- end client routes -------------------