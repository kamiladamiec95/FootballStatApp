import json

CONFIG_FILE = "../config.json"

def add_leagues_from_file():
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)

    leagues_to_add = config_data["leagues_to_add"]
    current_leagues = config_data["leagues"]

    for league in leagues_to_add:
        db.add_leagues(league)

    current_leagues.extend(leagues_to_add)

    config_data["leagues_to_add"] = []
    config_data["leagues"] = current_leagues

    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f)