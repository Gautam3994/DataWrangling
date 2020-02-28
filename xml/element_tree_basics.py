import xml.etree.ElementTree as ET
import pprint

tree = ET.parse('exampleresearcharticle.xml')
"""To load data from a string use the below method"""
# data = ""
# tree = ET.fromstring(data)
root = tree.getroot()  # this returns a list

"""To find the child"""
print("List of all child tags:")
for child in root:
    print(child.tag)
    # print(child.attrib)

"""To find a nested element"""
title = root.find("./fm/bibl/title")
title_text = ""
for p in title:  # here title is the root and we are iterating over it child elements
    title_text += p.text  # since most of the data is <p>(text) we use text
print("\nTitle: "),
print(title_text)

"""Final all nested elements"""
print("\nList of all emails:")
for a in root.findall("./fm/bibl/aug/au"):
    email = a.find('email')
    if email is not None:
        print(email.text)

"""Full Details of a author"""
full_data = []
for a in root.findall("./fm/bibl/aug/au"):
    email = a.find('email')
    if email is not None:
        email = email.text
    surname = a.find('snm')
    if surname is not None:
        surname = surname.text
    firstname = a.find('fnm')
    if firstname is not None:
        firstname = firstname.text
    data = {
        'email': email,
        'fnm': firstname,
        'snm': surname
    }
    full_data.append(data)
pprint.pprint(full_data)



