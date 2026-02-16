from flask import Flask, session
from config import Config
from auth.wahoo_auth import wahoo_auth
from clients.wahoo_client import get_workouts




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(wahoo_auth)

    @app.route("/test-wahoo")
    def test_wahoo():
        workouts = get_workouts()
        return workouts

    return app

app = create_app()

if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True,
        ssl_context="adhoc"
    )