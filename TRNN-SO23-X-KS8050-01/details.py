
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "TRNN"
oSize = "SO23"
oColor = "X"
oDesc = "KS8050"
oIndex = "01"
hexId = "TNS248050"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('footprintKicad','FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23')
newPart.addTag('symbolKicad','SYMBOL-kicad-kicad-symbols-Device-Q_NPN_BEC')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
