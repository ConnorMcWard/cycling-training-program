"""This file contains the configuration and API keys for google, openai, and wahoo."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """This class contains the configuration for the app."""
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Wahoo

    WAHOO_CLIENT_ID = os.getenv("WAHOO_CLIENT_ID")
    WAHOO_CLIENT_SECRET_KEY = os.getenv("WAHOO_CLIENT_SECRET_KEY")
    WAHOO_REDIRECT_URI = os.getenv("WAHOO_REDIRECT_URI")
    WAHOO_SCOPES = os.getenv("WAHOO_SCOPES")

    # OpenAI

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Google

    GOOGLE_CAL_API_KEY = ""

    # Flask

    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")

