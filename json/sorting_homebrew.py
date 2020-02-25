import json
import pprint

with open('software_info.json') as file:
    data = json.load(file)  # dump converting python data to file


def sort_key(package):
    return package['analytics']['installed_on_request'][
        '30 days']  # no need to mention list index as sorted takes care of it
    # this returns the value of the no of downloads in past 30 days
    # to change the selection criteria to some other no of days changes the '30 days'


sorted_list = sorted(data, key=sort_key, reverse=True)
pprint.pprint(sorted_list[0:5])  # to display the top ten value.
print("------------------------------------------------------------------------")
"""to sort data without creating new variable"""
# data.sort(key=sort_key, reverse=True)
# pprint.pprint(data[0:5])
print("------------------------------------------------------------------------")
"""to sort data with video in description"""
data = [item for item in data if 'video' in item['description']]
data.sort(key=sort_key)
pprint.pprint(data[0:5])

