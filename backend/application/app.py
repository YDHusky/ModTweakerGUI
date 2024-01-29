from flask import Flask
from flask_jwt_extended import JWTManager

from flask_cors import CORS
from backend.application.config import DevelopmentConfig
from backend.application.extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    JWTManager(app)
    CORS(app, origins='http://localhost:5173', supports_credentials=True)
    from backend.application.controllers.testConroller import test_bp
    app.register_blueprint(test_bp)
    return app
