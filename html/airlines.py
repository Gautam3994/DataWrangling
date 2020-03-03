"""
1-A) Get the list of carriers
1-B) Get the list of airports
2) Make HTTP request to download data - Make you dont have to unneccesary download data multiple time
                                        i.e old data mostly wont change so save it.
                                        It will make parsing easier
3) Parsing the files
"""
from bs4 import BeautifulSoup
import requests

# response = requests.get("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
# with open('airlines.html', 'w') as html:
#     html.writelines(response.text)
#


def find(soup, _id):
    results = soup.find('select', id=_id)
    list_of_values = []
    for result in results.find_all('option'):
        list_of_values.append(result['value'])
    return list_of_values


def print_list(label, list_):
    print(f"\n{label}:")
    for value in list_:
        print(value)


def main():
    with open('airlines.html') as html:
        soup = BeautifulSoup(html, 'lxml')
        # print(soup.prettify())
    carriers = find(soup, 'CarrierList')
    airlines = find(soup, 'AirportList')
    # print_list("Carriers", carriers)
    # print_list("Airlines", airlines)
    # form1 = soup.find('form', id="form1")
    # print(form1)
    make_request(soup)

"""
    Next we have to look at the form section for the method(POST, PUT, ETC ) and then we have to look for the url
    In this case <form action="./Data_Elements.aspx?Data=2" id="form1" method="post">
    Then we have to send to a sample request and check what parameters are being sent in the form data section of the 
    Network tab
    __viewstategenerator field will be visible only in linux.
    Now we have to find where the remaining fields other than carriers and airlines come from
"""


def make_request(soup):
    eventtarget = soup.find('input', id="__VIEWSTATE")
    eventargument = soup.find('input', id="__EVENTARGUMENT")

    print(eventtarget)


main()