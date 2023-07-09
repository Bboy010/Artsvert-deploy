from flask import Flask
from database import db
from routes.public import public_routes
from routes.admin import admin_routes
from models import Admin
from flask_login import LoginManager

app = Flask(__name__)

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/artsvert_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# session configuration
app.config['SECRET_KEY'] = 'bboyartsvert'

# image configuration
# app.config['UPLOAD_FOLDER'] = 'static/images'
# app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

# ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Link app to db : il permet de lier l'instance de SQLAlchemy à l app Flask
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))


# save Blueprints 
app.register_blueprint(admin_routes)
app.register_blueprint(public_routes)
# app.register_blueprint(painting_routes)
# app.register_blueprint(print_routes)
# app.register_blueprint(sculpture_routes)

app.app_context().push()


if __name__ == '__main__':
    app.run(debug=True)
