from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routers import main
    app.register_blueprint(main)

    return app