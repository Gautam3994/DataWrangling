import time
import requests
import json
import pprint

url = "https://formulae.brew.sh/api/formula.json"
response = requests.get(url)
structure = response.json()
softwares = [structure[i]['name']for i in range(len(structure)) if structure[i]['name']]
results = []
t1 = time.perf_counter()
for software in softwares:
    new_url = f'https://formulae.brew.sh/api/formula/{software}.json'
    reponse_software = requests.get(new_url)
    software_data = reponse_software.json()
    final_data = {
        'name': software_data['name'],
        'description': software_data['desc'],
        'analytics': {
            'installed_on_request': {
                '30 days': software_data['analytics']['install_on_request']['30d'][software],
                '90 days': software_data['analytics']['install_on_request']['90d'][software],
                '365 days': software_data['analytics']['install_on_request']['365d'][software]
            }
        }
    }
    results.append(final_data)
    time.sleep(response.elapsed.total_seconds())
    print(f'Got the software {software} in {response.elapsed.total_seconds()}')
t2 = time.perf_counter()
print(t2 - t1)
with open("software_info.json", "w") as software_file:
    json.dump(results, software_file, indent=2)

