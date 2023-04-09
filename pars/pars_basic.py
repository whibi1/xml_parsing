import xml.etree.ElementTree as ET

tree= ET.parse("book.xml")
root= tree.getroot()


for a in root:
    print(f"{a.tag}:,{a.text}")
    for b in a:
        print (f"{b.tag}:,{b.text}")
        for c in b:
             print(f"{c.tag}:,{c.text}")





