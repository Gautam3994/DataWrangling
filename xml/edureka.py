import xml.etree.ElementTree as ET
import time

tree = ET.parse('sample.xml')
root = tree.getroot()

for i, child in enumerate(root.findall("./book/description")):
    a = str(child.text) + f" Description has added for the {i} element"
    child.text = str(a)  # text to the change
    child.set('updated', 'yes')  # set to add attributes
    # append to add new child

# print(root[0].find('price').text)
# 'this creates an subelement child(child of child)'
ET.SubElement(root[0], 'Review', {'updated': 'yes'})
for x in root.iter('Review'):
    sting = "Sting"
    x.text = str(sting)

ET.SubElement(root, "Review")
tree.write('modified_sample.xml')

# pop, remove, clear

