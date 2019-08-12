import json
import os.path

locations_path = 'locations.json'

if os.path.isfile(locations_path):
    with open(locations_path, 'r') as f:
        thing_locations = json.loads(f.read())
else:
    thing_locations = {}
