
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "CAPC"
oSize = "0402"
oColor = "X"
oDesc = "UF10"
oIndex = "V63D"
hexId = "C4U1063D"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('oplPartNumber',{'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C15525', 'desc': '6.3V 10uF X5R ??20% 0402  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
newPart.addTag('distributorPartNumber',{'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C15525'})
newPart.addTag('manufacturerPartNumber',{'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL05A106MQ5NUNC'})


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
