import os
from dotenv import load_dotenv

from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate

from db import db
from resources.routes import routes
from models.user import UserModel
from models.seller import SellerModel
from models.admin import AdminModel


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "Development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{config( 'DB_USER' )}:{config( 'DB_PASSWORD' )}"
    f"@localhost:{config( 'DB_PORT' )}/{config( 'DB_NAME' )}"
    )
    SQLALCHEMY_ECHO = True


def create_app(config="config.DevelopmentConfig"):
    app = Flask( __name__ )
    app.config.from_object( config )
    db.init_app( app )
    CORS( app )
    api = Api( app )
    [api.add_resource( *route_data ) for route_data in routes]
    return app

app = create_app()

migrate = Migrate(app, db)