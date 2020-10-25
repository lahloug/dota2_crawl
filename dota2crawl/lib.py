#!/usr/bin/env python

from datetime import datetime
import json
import requests
from pathlib import Path

API_URL = "https://api.pandascore.co/dota2"


def get_auth_token(token_file=".pandascore_token.txt"):
    """
    token file is the relative path to home directory
    """
    token_file = str(Path.home()) + "/" + token_file
    with open(token_file, "r") as f:
        tok = f.read()
    return tok.strip()


def get_tournaments():
    url = f"{API_URL}/tournaments"
    headers = {"Authorization": get_auth_token() }
    res = requests.get(url, headers=headers)
    return res.json()


def save_json(name, data):
    now = datetime.now()
    name = name + "_" + now + ".json"
    with open(name, 'w') as f:
        json.dum(data, f)


if __name__ == "__main__":
    res = get_tournaments()
    print(res)
