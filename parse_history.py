import json
import sqlite3

# https://docs.python.org/3/library/json.html
# open json file
print("opening file...")
with open("Records.json", "r") as f:
    json_file = f.read()
print("opened!")

# parse json file to python object
print("parsing file...")
locations : list = json.loads(json_file)['locations']
print("parsed!")

# print(f"locations length: {len(locations)}")
# for loc in locations:
#     print(loc)

# create a sqlite3 database to store this huge list of locations
# https://docs.python.org/3/library/sqlite3.html
# con = sqlite3.connect("locations.db")
# cur = con.cursor()

# create the table
# cur.execute("CREATE TABLE locations(latitude, longitude, timestamp)")
# each "location" item has a lot of data, including activity, device, and more.
# for now, i'm going to only take latitude, longitude, and timestamp

# populate the locations table
# for loc in locations:
#     cur.execute("INSERT INTO locations values (?, ?, ?)")