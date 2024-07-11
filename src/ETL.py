import json
import database.db as db
import re
import os
import pandas as pd

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

def read_and_archive_raw_data_json():
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)

    leagues = config_data["leagues"]
    files_path = config_data["event_files_path"]
    pattern = re.compile(r"^(" + '|'.join(leagues) + r")\d+.json$")

    for file in os.listdir(files_path):
        if pattern.match(file):
                with open(f"{files_path}/{file}", encoding="utf-8") as data_file:
                    events = json.load(data_file)
                df = pd.json_normalize(events, "events", ["home_team", "away_team", "league", "external_match_id"],
                            record_prefix="events_")
                df_matches = pd.DataFrame(df.where(df["events_event"] == "match_start"))
                df_matches = df_matches.dropna(how='all')
                df_matches["is_finished"] = 0 
                league = re.sub(r"(\d|.json)", "", file)
                db.add_match(df_matches, league)
                db.add_event(df, league)
                os.rename(f"{files_path}/{file}", f"Archive/{file}")        