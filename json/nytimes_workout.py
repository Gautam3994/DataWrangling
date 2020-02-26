import requests
import pprint

main_url = 'https://api.nytimes.com/svc/'
mostpopular_url = main_url + 'mostpopular/v2/'
params = {
    "api-key": "",
       }
# response = requests.get(f'https://api.nytimes.com/svc/mostpopular/v2/{type}/{period}.json', params=key)
# print(response.url)


def query_site(url, offset, required_type, days):
    if params['api-key'] == "":
        print("You require an API Key to access this page")
        return False
    if required_type not in ["viewed", "shared", "emailed"]:
        print("Please check the type")
        return False
    if days not in [1, 7, 30]:
        print("Day value can only be 1,7 or 30")
        return False
    query_url = url+f'{required_type}/{days}.json'
    params['offset'] = offset
    response = requests.get(query_url, params=params)
    print("We are requesting to the url", response.url)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        response.raise_for_status()


result = query_site(mostpopular_url, 0, 'viewed', 30)
pprint.pprint(result['results'][0]['views'])
