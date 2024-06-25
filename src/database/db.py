import sqlalchemy
import pandas as pd

def connect_to_db():
    engine = sqlalchemy.create_engine("mssql+pymssql://sa:YourStrongPassw0rd@localhost:1401/FootballStatistics")
    return engine

def add_leagues(league):
    query = f"EXEC dbo.AddLeague @LeagueName = '%s'"% (league)
    with connect_to_db().begin() as conn:
        conn.execute(sqlalchemy.text(query))  