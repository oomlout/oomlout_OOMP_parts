

import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "VREG"
oSize = "SO235"
oColor = "X"
oDesc = "KAP2112K"
oIndex = "V33D"
hexId = "V235AP2112K33"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 


######  Specs
#manufacturersPartNumber = ''
#newPart.addTag('manufacturersPartNumber',manufacturersPartNumber)
#pitch = 2.54 
#newPart.addTag('ooPitch',str(pitch))

######  Common
newPart.addTag('hexID',hexId)
#newPart.addTag('oompSort','')
#newPart.addTag('oompVersion','99')

######  About
#newPart.addTag('useDescription','')
#newPart.addTag('oompAbout','')



######  Dimensions

#newPart.addTag('ooWidth','')
#newPart.addTag('ooHeight','')
#newPart.addTag('ooDepth','')
#newPart.addTag('oompBbls','')

######  EDA
#newPart.addTag("footprintKicad","")  
#newPart.addTag("symbolKicad","")  

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
