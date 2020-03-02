"""
    Two major parsers used in BeautifulSoup is lxml and html5lib
"""

from bs4 import BeautifulSoup
import requests
import csv

with open('simple.html') as html:
    soup = BeautifulSoup(html, 'lxml')

# pprint.pprint(soup)
"""pprint causes results to display same as just print so use prettify"""
# print(soup.prettify())
title = soup.title
# print(title.text)

"""When you dot notation to find a field it always uses the first element"""
first_div = soup.div
# print(first_div)

"""So it is better to use find method"""
other_divs = soup.find('div', class_="footer")
# print(other_divs)

"""Find all article which is nested inside a tag"""
articles = soup.findAll('div', class_="article")  # the findAll method returns a list
for article in articles:
    pass
    # print(article.h2.a.text)
    # print(article.p.text)
    # print()

"""scraping from a website using requests"""
import requests

response = requests.get("https://coreyms.com/")
# print(response.text)

"""
    It is always better to save the data one time
"""
# with open("coreyms.html", "w") as html:
#     html.write(response.text)

with open("coreyms.html") as html:
    corey_soup = BeautifulSoup(html, "lxml")

# print(soup.prettify())
corey_articles = corey_soup.find_all('article')
with open('coreyms.csv', 'w', newline='') as csv_file:  # to stop having empty row between two rows we use newline=''
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Description", "Link"])
    for article in corey_articles:
        title = article.header.h2.a.text
        # print(article.find("div", class_="entry-content").p.text)
        description = article.div.p.text
        try:
            video_src = article.div.span.iframe["src"]
            # video_src = article.find('iframe', class_="youtube-player")['src']
            id = video_src.split("/")[-1].split("?")[0]
            youtube = f"https://www.youtube.com/watch?v={id}"
        except Exception:
            youtube = "None"
        writer.writerow([title, description, youtube])
