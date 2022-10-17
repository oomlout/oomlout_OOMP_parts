
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "MOSN"
oSize = "T252"
oColor = "X"
oDesc = "K4184"
oIndex = "01"
hexId = "MN2524184A"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('footprintKicad','FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-TO-252-3_TabPin2')
newPart.addTag('symbolKicad','SYMBOL-kicad-kicad-symbols-Device-Q_NMOS_GDS')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
