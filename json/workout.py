import requests
import pprint
"""
25

"""

# response = requests.get("http://musicbrainz.org/ws/2/artist/?query=artist%3ANirvana&fmt=json")
# data = response.json()
# for i in range(len(data['artists'])):
#     pprint.pprint(data['artists'][i]['name'])
#     print('----------------------------------------------------------------------------------------------')

artist_url = "http://musicbrainz.org/ws/2/artist/"

params = {
    "query": "artist:" + "One Direction",
    "fmt": "json"
}
response = requests.get(artist_url, params=params)
print(response.url)
data = response.json()
num =0
for i in range(len(data['artists'])):
    if data['artists'][i]['name'] == "One Direction":
        pprint.pprint(data['artists'][i])
print(num)
# print(data['artists'][0]['disambiguation'])
# for i in range(len(data['artists'][0]['aliases'])):
#     if data['artists'][0]["aliases"][i]["locale"] == 'es':
#         pprint.pprint(data['artists'][0]["aliases"][i])
# pprint.pprint(data['artists'][0]['begin-area']['name'])
# req_id = data["artists"][3]['id']


"""required format for release"""
# http://musicbrainz.org/ws/2/artist/c49d69dc-e008-47cf-b5ff-160fafb1fe1f?inc=releases&fmt=json
# new_url = artist_url+req_id
# release_params = {
#     "inc": "releases",
#     "fmt": "json"
# }
# release_response = requests.get(new_url, params=release_params)
# release_data = release_response.json()
# print(release_data['releases'])



