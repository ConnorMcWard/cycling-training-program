import requests
from flask import session

BASE_URL = "https://api.wahooligan.com/v1"


def get_headers():
    access_token = session.get("wahoo_access_token")

    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }


def get_workouts():
    response = requests.get(
        f"{BASE_URL}/workouts",
        headers=get_headers()
    )

    return response.json()


def get_completed_workouts():
    response = requests.get(
        f"{BASE_URL}/workouts?status=completed",
        headers=get_headers()
    )

    return response.json()



