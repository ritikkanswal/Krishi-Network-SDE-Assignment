from flask import Flask


def create_app():
    app=Flask(__name__)

    from .routs import site
    
    app.register_blueprint(site)
    
    return app