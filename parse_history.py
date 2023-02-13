import json
import sqlite3
from datetime import datetime

def json_to_db(file_path : str, db_con : sqlite3.Connection):
    # python json docs: https://docs.python.org/3/library/json.html
    # open json file
    print(f"opening file at '{file_path}'...")
    with open(file_path, "r") as f:
        json_file = f.read()
    print("opened!")

    # parse json file to python object
    print("parsing file json...")
    locations : list = json.loads(json_file)['locations']
    print("parsed!")

    # python sqlite3 docs: https://docs.python.org/3/library/sqlite3.html
    # create a sqlite3 database to store this huge list of locations
    # con = sqlite3.connect("locations.db")
    # create cursor from provided database connection
    cur = db_con.cursor()

    # delete table if it already exists
    cur.execute("DROP TABLE IF EXISTS locations;")
    # create the table
    print("creating locations table...")
    cur.execute("CREATE TABLE locations(timestamp INT, latitude INT , longitude INT);")

    # populate the locations table
    # each "location" item has a lot of data, including activity, device, and more.
    # for now, i'm going to only take latitude, longitude, and timestamp
    print("populating locations table...")
    for loc in locations:
        # convert timestamp string into unix time integer
        datetime_str = loc["timestamp"].split("Z")[0].split(".")[0]
        # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        naive_dt = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
        timestamp = int(naive_dt.timestamp())
        cur.execute("INSERT INTO locations (timestamp, latitude, longitude) VALUES(?, ?, ?)", (timestamp, int(loc["latitudeE7"]), int(loc["longitudeE7"])))
    db_con.commit()
    print("database populated!")

    result = cur.execute("SELECT COUNT(*) FROM locations")
    print(f"count of locations: {result.fetchone()}")
    return 0