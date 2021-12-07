## Motivation

I am an organizer for a meetup group and wanted to get some statistical data for our events. Meetup has an API that is
not free, but it does provide free requests for the GET method. The data can be obtained
from https://secure.meetup.com/meetup_api/console/

## Data

The console is an interface with fields for the query. I wanted information pertaining on the events like the what and
when and where. I didn't care about the cost and I also wanted to omit the event description to reduce the file size. Below are my input fields.

* urlname: This is the name of the group, 1-5GenAsians 
* no_later_than: Second request requires timestamp from the first, 2018-12-22T00:00:00.000
* type: Include all type of events - past,upcoming
* omit: name,description,date_in_series_pattern,updated,utc_offset,is_online_event,group,visibility,member_pay_fee,how_to_find_us

## Procedure

Since the free tier limits to only 500 objects as the response payload, I had to make two separate requests to get all
my group's events since we have around 800. The following outlines the steps to wrangle and clean the data.

1. Observe the responded and extracted JSONs, meetup-1.json and meetup-2.json
2. Clean data with json-joiner.py to combine both JSONs into one (meetup.json). Keep in mind of the incrementing identifications.
3. Create data definition with meetup.sql
4. Parse with meetup.py