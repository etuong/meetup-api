#!/usr/bin/python

import json
import sqlite3


def createdb(db_file_name, json_file_name):
    connection = sqlite3.connect(db_file_name)
    c = connection.cursor()

    with open(json_file_name, "r") as f:
        data = json.load(f)

    for event in data:
        event_id = data[event]['id']
        status = data[event]['status']
        event_date = data[event]['local_date']
        rsvp_count = data[event]['yes_rsvp_count']
        link = data[event]['link']
        c.execute("INSERT INTO event (event_id, status, event_date, rsvp_count,link) VALUES (?,?,?,?,?)",
                  (event_id, status, event_date, rsvp_count, link))

    connection.commit()


db_file_name = 'meetup.db'
json_file_name = 'meetup.json'
createdb(db_file_name, json_file_name)
