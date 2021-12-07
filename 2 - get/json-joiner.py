import json

"""
Meetup API is not free anymore. It caps the free REST calls to 500 objects. This script
is appends the data together otherwise they will be overwritten.
"""

write = {}

# Read the entire first JSON
with open('meetup-1.json', 'r') as json_file:
    write = json.load(json_file)

# Appends the second JSON starting with a new object ID
id = 500
with open('meetup-2.json', 'r') as json_file:
    data = json.load(json_file)
    for v in data.values():
        write[str(id)] = v
        id = id + 1

# Output final combined JSON
with open('meetup.json', 'w') as outfile:
    json.dump(write, outfile)