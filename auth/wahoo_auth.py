"""This file authenticates the app user to the Wahoo API"""

import requests
from flask import Blueprint, redirect, request, session, current_app
from urllib.parse import urlencode


wahoo_auth = Blueprint("wahoo_auth", __name__, url_prefix="/api/auth/wahoo/")

AUTH_URL = "https://api.wahooligan.com/oauth/authorize"
TOKEN_URL = "https://api.wahooligan.com/oauth/token"


@wahoo_auth.route("login")
def wahoo_login():
    config = current_app.config

    print("Redirect URI being sent:", config["WAHOO_REDIRECT_URI"])

    params = {
        "client_id": config["WAHOO_CLIENT_ID"],
        "redirect_uri": config["WAHOO_REDIRECT_URI"],
        "response_type": "code",
        "scope": config["WAHOO_SCOPES"],
    }

    auth_redirect = f"{AUTH_URL}?{urlencode(params)}"

    print("Full redirect URL:", auth_redirect)

    return redirect(auth_redirect)


@wahoo_auth.route("callback")
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
            "redirect_uri": config["WAHOO_REDIRECT_URI"],
        },
    )

    token_json = token_response.json()

    print("Token JSON:", token_json)

    session["wahoo_access_token"] = token_json["access_token"]
    session["wahoo_refresh_token"] = token_json["refresh_token"]
    session["wahoo_expires_at"] = token_json["expires_in"]

    return {
        "message": "Wahoo authentication successful",
        "token_recieved": session["wahoo_access_token"] is not None,
    }
