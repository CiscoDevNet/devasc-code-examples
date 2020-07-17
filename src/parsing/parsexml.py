# Fill in this file with the code from parsing XML exercise

import xml.etree.ElementTree as ET
import re

xml = ET.parse("myfile.xml")
root = xml.getroot()

ns = re.match(r'{.*}', root.tag).group(0)
editconf = root.find(f"{ns}edit-config")
defop = editconf.find(f"{ns}default-operation")
testop = editconf.find(f"{ns}test-option")

print("The default-operation contains: %s" % defop.text)
print("The test-option contains: %s" % testop.text)
