from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.transaction import transaction
    from app.routes.user import user
    from app.routes.user import user
    from app.routes.auth import auth

    app.register_blueprint(transaction)
    app.register_blueprint(user)
    app.register_blueprint(user)
    app.register_blueprint(auth)

    return app