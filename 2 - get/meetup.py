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
        event_time = data[event]['local_time']
        rsvp_count = data[event]['yes_rsvp_count']
        waitlist_count = data[event]['waitlist_count']
        duration = data[event]['duration'] if "duration" in data[event] else 0
        link = data[event]['link']
        c.execute(
            "INSERT INTO event (event_id, status, event_date, event_time, waitlist_count, duration, rsvp_count,link) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (event_id, status, event_date, event_time, waitlist_count, duration, rsvp_count, link))
        if "venue" in data[event] and "lat" in data[event]['venue']:
            venue = data[event]['venue']
            venue_lat = venue['lat']
            venue_lon = venue['lon']
            venue_city = venue['city']
            c.execute("UPDATE event set venue_lat = ?, venue_lon = ?, venue_city = ? where event_id = ?",
                      (venue_lat, venue_lon, venue_city, event_id))
    connection.commit()


db_file_name = 'meetup.db'
json_file_name = 'meetup.json'
createdb(db_file_name, json_file_name)
