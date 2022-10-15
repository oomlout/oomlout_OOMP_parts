
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "CAPC"
oSize = "0805"
oColor = "X"
oDesc = "UF7"
oIndex = "V63D"
hexId = "C8U763D"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('oplPartNumber',{'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C16780', 'desc': '6.3V 47uF X5R ??20% 0805  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
newPart.addTag('distributorPartNumber',{'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C16780'})
newPart.addTag('manufacturerPartNumber',{'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL21A476MQYNNNE'})


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
