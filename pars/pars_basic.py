import xml.etree.ElementTree as ET

tree= ET.parse("book.xml")
root= tree.getroot()

liste=[]
for a in root:
    
    liste.append(a.tag)
    liste.append(a.text)
    for b in a:
        
        liste.append(b.tag)
        liste.append(b.text)
        for c in b:
             liste.append(c.tag)
             liste.append(c.text)

print(liste)
with open("aa.txt","r+") as f:
    for line in liste:
        f.write(line+"\n")








