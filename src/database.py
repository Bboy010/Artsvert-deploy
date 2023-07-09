from flask_sqlalchemy import SQLAlchemy

# Configuration de la connexion à la base de données

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/flask'
db = SQLAlchemy()

# # Création de l'objet

# def init_app(app):
#     db.init_app(app)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/flask'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     from models import Artwork, Artist
#     db.create_all()