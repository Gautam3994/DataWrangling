import requests
import pprint

response = requests.get("http://musicbrainz.org/ws/2/artist/?query=artist%3ANirvana&fmt=json")
data = response.json()
pprint.pprint(data)