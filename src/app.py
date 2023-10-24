from flask import Flask, session
from database import db
from routes.public import public_routes
from routes.admin import admin_routes
from models import Admin
from flask_login import LoginManager
from flask_session import Session
from datetime import timedelta
from config import SECRET_KEY
from flask_migrate import Migrate

app = Flask(__name__)

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/artsvert_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# session configuration
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=22)

Session(app)
migrate = Migrate(app, db)

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

app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)
