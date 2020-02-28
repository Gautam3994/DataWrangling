import re
import xml.etree.ElementTree as ET

"""normal parsing results in error as the file conatins invalid characters"""
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('datacamp.xml', parser=parser)
root = tree.getroot()
# print(root.tag)

for child in root:
    pass
    # print(child.tag, child.attrib)

"""To know all elements in the entire tree even the nested ones"""
all_elements = [element.tag for element in root.iter()]
# pprint.pprint(all_elements)

"""The above method doesnt show the document levels"""
# print(ET.tostring(root, encoding='utf-8').decode("utf-8"))

"""Using iter method i we can loop over all similar tags"""
for movie in root.iter('movie'):
    pass
    # print(movie.attrib)

"""Text"""
for description in root.iter('description'):
    pass
    # print(description.text)

"""XPATH"""
"""Value Match"""
"""Find all movies with the year 1992"""
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    pass
    # print(movie.attrib)

"""Attribute Match"""
"""Find all movies with multiple formata"""
"""... IS IMPORTANT TO GET THE PARENT ELEMENT IN BELOW CODE"""
for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
    pass
    # print(movie.attrib)

"""find a particular element"""
b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
b2tf.attrib["title"] = "Back to the Future"

"""MODIFYING ELEMENTS"""
"""Regex"""
for _format in root.findall("./genre/decade/movie/format"):
    match = re.search(",", _format.text)
    if match:
        _format.set("multiple", "Yes")
    else:
        _format.set("multiple", "No")


"""MOVING ELEMENTS"""
for decade in root.findall("./genre/decade"):
    # print(decade.attrib)
    for year in decade.findall("./movie/year"):
        pass
        """To find in which decade list the movies are"""
        # print(year.text)

for movie in root.findall("./genre/decade/movie/[year='2000']"):
    pass
    # print(movie.attrib)

"""SubElement"""
""" In the details the 2000s options is not available so we creating"""
action = root.find("./genre[@category='Action']")
# print(action.attrib)
new_dec = ET.SubElement(action, 'decade', {"years": "2000s"})
# print(ET.tostring(root, encoding='utf-8').decode("utf-8"))

"""Adding and removing data"""
"""Pop is used to remove attributes"""
xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre/decade[@years='1990s']")
dec1990s.remove(xmen)
print(ET.tostring(root, encoding='utf-8').decode("utf-8"))
tree.write('modified_datacamp.xml')
