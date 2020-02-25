import json
from urllib.request import urlopen
import pprint
# https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2

with urlopen("http://musicbrainz.org/ws/2/recording/fcbcdc39-8851-4efc-a02a-ab0e13be224f?inc=artist-credits+isrcs+releases&fmt=json") as response:
    source = response.read()

structure = json.loads(source)
# print(json.dumps(structure, indent=2))
# for alias in structure['aliases']:
#     pprint.pprint(alias['name']),
#     pprint.pprint(alias['type'])

# for i in range(len(structure['artist-credit'])):
#     pprint.pprint(structure['artist-credit'][i]['artist']['sort-name'])

