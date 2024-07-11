import json
import database.db as db

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


def read_and_archive_teams_json():
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)

    leagues = config_data["leagues"]
    files_path = config_data["team_files_path"]
    pattern = re.compile(r"^(" + '|'.join(leagues) + r")Teams.json$")

    for file in os.listdir(files_path):
        if pattern.match(file):
                teams = pd.read_json(f"{files_path}/{file}").transpose()
                os.rename(f"{files_path}/{file}", f"Archive/{file}")
                league = file.replace("Teams.json", "")
                db.add_team(teams, league)        