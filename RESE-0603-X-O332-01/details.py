
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "RESE"
oSize = "0603"
oColor = "X"
oDesc = "O332"
oIndex = "01"
hexId = "RESE-6O332-01"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('oplPartNumber',{'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C22978', 'desc': '100mW Thick Film Resistors 75V ??100ppm/?? ??1% -55??~+155?? 3.3k?? 0603  Chip Resistor - Surface Mount ROHS'})
newPart.addTag('distributorPartNumber',{'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C22978'})
newPart.addTag('manufacturerPartNumber',{'code': 'C-XXXX', 'name': 'UNI-ROYAL(Uniroyal Elec)', 'partID': '0603WAF3301T5E'})


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
