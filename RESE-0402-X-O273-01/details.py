
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "RESE"
oSize = "0402"
oColor = "X"
oDesc = "O273"
oIndex = "01"
hexId = "R4O273"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('oplPartNumber',{'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C25771', 'desc': '62.5mW Thick Film Resistors 50V ??100ppm/?? ??1% -55??~+155?? 27k?? 0402  Chip Resistor - Surface Mount ROHS'})
newPart.addTag('distributorPartNumber',{'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C25771'})
newPart.addTag('manufacturerPartNumber',{'code': 'C-XXXX', 'name': 'UNI-ROYAL(Uniroyal Elec)', 'partID': '0402WGF2702TCE'})


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
