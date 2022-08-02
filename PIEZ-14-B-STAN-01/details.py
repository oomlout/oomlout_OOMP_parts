import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PIEZ"
oSize = "14"
oColor = "B"
oDesc = "STAN"
oIndex = "01"
hexId = "PZ14"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 


######  Specs
manufacturersPartNumber = 'TDK,PS1420P02CT'
newPart.addTag('manufacturersPartNumber',manufacturersPartNumber)
manufacturersPartNumber = 'Sweet Sound,PSE1470+4005PA'
newPart.addTag('manufacturersPartNumber',manufacturersPartNumber)


pitch = 5 
newPart.addTag('ooPitch',str(pitch))

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
#newPart.addTag('oompBbls','template;BREB-P400-C-STAN-01-bbls')



######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
