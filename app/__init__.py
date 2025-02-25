from flask import Flask
from app.config.settings import Config
from app.api.routes import bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Register blueprints
    app.register_blueprint(bp)
    
    return app 