
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "CAPC"
oSize = "0402"
oColor = "X"
oDesc = "NF2"
oIndex = "V50"
hexId = "C4N2"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('oplPartNumber',{'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C1532', 'desc': '50V 22nF X7R ??10% 0402  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
newPart.addTag('distributorPartNumber',{'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C1532'})
newPart.addTag('manufacturerPartNumber',{'code': 'C-XXXX', 'name': 'FH (Guangdong Fenghua Advanced Tech)', 'partID': '0402B223K500NT'})


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
