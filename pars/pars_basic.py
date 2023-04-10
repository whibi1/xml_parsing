import xml.etree.ElementTree as ET

tree= ET.parse("book.xml")
root= tree.getroot()

list=[]
for a in root:
    
    list.append(a.tag)
    list.append(a.text)
    for b in a:
        
        list.append(b.tag)
        list.append(b.text)
        for c in b:
             list.append(c.tag)
             list.append(c.text)

with open("aa.txt","w") as f:
    for line in list:
        f.write(line+"\n")








