from flask import Flask, session
from config import Config
from auth.wahoo_auth import wahoo_auth


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(wahoo_auth)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, ssl_context="adhoc")