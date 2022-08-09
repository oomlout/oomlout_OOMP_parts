import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "TRNP"
oSize = "T92"
oColor = "X"
oDesc = "K2N3906"
oIndex = "01"
hexId = "TP92N36"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 


######  Specs
#pitch = 2.54 

######  Common
newPart.addTag('hexID',hexId)
#newPart.addTag('oompSort','')
#newPart.addTag('oompVersion','99')

######  About
#newPart.addTag('useDescription','')
#newPart.addTag('oompAbout','')



######  Dimensions
#newPart.addTag('ooPitch',str(pitch))
#newPart.addTag('ooWidth','')
#newPart.addTag('ooHeight','')
#newPart.addTag('ooDepth','')
#newPart.addTag('oompBbls','template;BREB-P400-C-STAN-01-bbls')



######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
