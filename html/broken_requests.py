from bs4 import BeautifulSoup
import requests

session = requests.session()
source = session.get("https://www.transtats.bts.gov/Data_Elements_Financial.aspx?Data=6").text
# print(response)

# with open("airlines.html") as html:
soup = BeautifulSoup(source, 'lxml')

event_validation = soup.find('input', id="__EVENTVALIDATION")['value']
view_state = soup.find('input', id="__VIEWSTATE")["value"]
view_state_generator = soup.find('input', id="__VIEWSTATEGENERATOR")["value"]

# carrier_list = soup.find("select", id="CarrierList")
# for carrier in carrier_list.find_all('option'):
#     if not carrier.text == "All U.S. Carriers":
#         print(carrier['value'])
# print()
# region_list = soup.find("select", id="RegionList")
# for region in region_list.find_all('option'):
#     if not region.text == "All regions":
#         print(region['value'])


response = session.post("https://www.transtats.bts.gov/Data_Elements_Financial.aspx?Data=6",
                        data={
                            "Submit": "Submit",
                            "CarrierList": "DL",
                            "RegionList": "D",
                            "__EVENTVALIDATION": event_validation,
                            "__VIEWSTATE": view_state,
                            "__VIEWSTATEGENERATOR": view_state_generator,
                            "__EVENTTARGET": "",
                            "__EVENTARGUMENT": ""
                        })
print(response.text)

with open("result.html", "w") as result:
    result.write(response.text)
"""
Some time we get error in this as the page may come cookie information
so use request session
session = requests.session
session.get
"""
