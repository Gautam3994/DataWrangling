import xml.etree.ElementTree as ET


tree = ET.parse('modified_sample.xml')
root = tree.getroot()

for book in root.findall('./book'):
    print(book.find('Review').tag)
