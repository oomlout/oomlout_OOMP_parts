
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "RESE"
oSize = "0603"
oColor = "X"
oDesc = "O402"
oIndex = "01"
hexId = "RESE-6O402-01"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('oplPartNumber',{'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C22940', 'desc': '100mW Thick Film Resistors 75V ??100ppm/?? ??1% -55??~+155?? 2.4k?? 0603  Chip Resistor - Surface Mount ROHS'})
newPart.addTag('distributorPartNumber',{'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C22940'})
newPart.addTag('manufacturerPartNumber',{'code': 'C-XXXX', 'name': 'UNI-ROYAL(Uniroyal Elec)', 'partID': '0603WAF2401T5E'})


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
