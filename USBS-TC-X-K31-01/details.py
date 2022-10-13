
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "USBS"
oSize = "TC"
oColor = "X"
oDesc = "K31"
oIndex = "01"
hexId = "USCK31"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('distributorPartNumber',{'companyName': 'LCSC', 'companyCode': 'C-LCSC', 'partNumber': 'C165948'})
newPart.addTag('manufacturerPartNumber',{'companyName': 'Korean Hroparts Elec', 'companyCode': 'C-KHRO', 'partNumber': 'TYPE-C-31-M-12'})


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
