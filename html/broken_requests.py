from bs4 import BeautifulSoup
import requests

# source = requests.get("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2", timeout=6)
# print(source.status_code)
with open('airlines.html') as html:
    soup = BeautifulSoup(html, "lxml")
event_validation = soup.find('input', id="__EVENTVALIDATION")['value']
view_state = soup.find('input', id="__VIEWSTATE")['value']
r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                  data={'AirportList': "BOS",
                        'CarrierList': "VX",
                        'Submit': 'Submit',
                        "__EVENTTARGET": "",
                        "__EVENTARGUMENT": "",
                        "__EVENTVALIDATION": event_validation,
                        "__VIEWSTATE": view_state
                        }, timeout=6)
print(r.text)

"""
Some time we get error in this as the page may come cookie information
so use request session
session = requests.session
session.get
"""

