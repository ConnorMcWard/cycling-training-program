""" This file authenticates the app user to the Wahoo API"""

import requests
from flask import Blueprint, redirect, request, session, current_app

wahoo_auth = Blueprint("wahoo_auth", __name__, url_prefix="/api/")

AUTH_URL = "https://api.wahooligan.com/oauth/authorize"
TOKEN_URL = "https://api.wahooligan.com/oauth/token"



@wahoo_auth.route("/auth/wahoo/login")
def wahoo_login():
    config = current_app.config

    auth_redirect = (
        f"{AUTH_URL}"
        f"?client_id={config['WAHOO_CLIENT_ID']}"
        f"&redirect_uri={config['WAHOO_REDIRECT_URI']}"
        f"&response_type=code"
        f"&scope={config['WAHOO_SCOPES']}"
    )

    return redirect(auth_redirect)


@wahoo_auth.route("/auth/wahoo/callback")
def wahoo_callback():
    config = current_app.config
    code = request.args.get("code")

    token_response = requests.post(
        TOKEN_URL,
        data={
            "client_id": config["WAHOO_CLIENT_ID"],
            "client_secret": config["WAHOO_CLIENT_SECRET_KEY"],
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": config["WAHOO_REDIRECT_URI"]
        }
    )

    token_json = token_response.json()

    session["wahoo_access_token"] = token_json["access_token"]
    session["wahoo_refresh_token"] = token_json["refresh_token"]
    session["wahoo_expires_at"] = token_json["expires_at"]


    return {
        "message": "Wahoo authentication successful",
        "token_recieved": session["wahoo_access_token"] is not None
    }