import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "TRNN"
oSize = "SO23"
oColor = "X"
oDesc = "KS8050"
oIndex = "01"
hexId = "TN98050"

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


######  EDA
newPart.addTag("footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23")  
#newPart.addTag("symbolKicad","") 

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
