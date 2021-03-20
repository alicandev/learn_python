import xml.dom.minidom

# load and parse an xml file
doc = xml.dom.minidom.parse("sample.xml")

# print the document node and the name of the first child tag
print(f"doc.nodeName: {doc.nodeName}")
print(f"doc.firstChild.tagName: {doc.firstChild.tagName}")

# get XML tags by name and print each one
skills = doc.getElementsByTagName("skill")
print(f"{skills.length} skills:")
for skill in skills:
  print(f"name: {skill.getAttribute('name')}")

# create a new xml tag and add it to the document
newSkill = doc.createElement("skill")
newSkill.setAttribute("name", "HTML & CSS")
doc.firstChild.appendChild(newSkill)