import time
import json


import requests
import pprint

main_url = 'https://api.nytimes.com/svc/'
mostpopular_url = main_url + 'mostpopular/v2/'
params = {
    "api-key": "wz9SJgMftlL0C8KVE0ABsWZ0lXnKUXGA",
}


def query_site(url, required_type, days, offset=0):
    if params['api-key'] == "":
        print("You require an API Key to access this page")
        return False
    if required_type not in ["viewed", "shared", "emailed"]:
        print("Please check the type")
        return False
    if days not in [1, 7, 30]:
        print("Day value can only be 1,7 or 30")
        return False
    query_url = url + f'{required_type}/{days}.json'
    params['offset'] = str(offset)
    response = requests.get(query_url, params=params)
    print("We are requesting to the url", response.url)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        response.raise_for_status()


"""You wont get all files so you have to use save it to a locations"""


def save_file(url, offset, req_type, days):
    result = query_site(url, req_type, days)
    # provide offset to get more results[there is a restriction in the values
    # you can provide as offset ]
    num_results = result["num_results"]
    full_data = []
    """Below code to save to local"""
    with open('nytimes_workout.json', 'w', encoding='utf-8') as file:
        for off_set in range(0, num_results, 20):  # it is range(start=0, stop=num_results, step=20):
            data = query_site(url, req_type, days, offset=off_set)
            time.sleep(5)
            full_data += data['results']  # if you use append it will create list of list
        json.dump(full_data, file, indent=2, ensure_ascii=False)  # this gets rid of the /u values


# save_file(mostpopular_url, 0, 'viewed', 30)

def parse_file():
    with open('nytimes_workout.json') as file:
        data = json.load(file)
    titles = []
    urls = []
    for i in range(len(data)):
        dict = {
            data[i]['section']: data[i]['title']
        }
        titles.append(dict)
        for media in data[i]['media']:
            for inner in media['media-metadata']:
                if inner['format'] == 'Standard Thumbnail':
                    urls.append(inner['url'])
    print(titles)


parse_file()
