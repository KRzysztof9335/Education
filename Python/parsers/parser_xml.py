import xml.etree.ElementTree as ET

tree = ET.parse("/home/krzysztof/Projects/Education/Python/example1.xml")

content = tree.getroot()
# menu = content.find("breakfast_menu")

for item in content.iter(): # type:ignore
    name = item.attrib["name"] if "name" in item.attrib else None
    print(name)