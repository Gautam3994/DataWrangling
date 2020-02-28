import xml.etree.ElementTree as ET

_parser = ET.XMLParser(encoding='utf-8')
_tree = ET.parse('modified_datacamp.xml', parser=_parser)
_root = _tree.getroot()


for _format1 in _root.findall("./genre/decade/movie/format"):
    print(_format1.attrib, _format1.text)