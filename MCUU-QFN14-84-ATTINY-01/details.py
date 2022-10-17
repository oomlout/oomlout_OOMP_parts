
import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "MCUU"
oSize = "QFN14"
oColor = "84"
oDesc = "ATTINY"
oIndex = "01"
hexId = "MCAT84SC14"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('footprintKicad','FOOTPRINT-kicad-kicad-footprints-Package_DFN_QFN-QFN-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm')
newPart.addTag('symbolKicad','SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny84-20M')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
#newPart = OOMPtags.addTags(newPart,oompId),pitch = pitch)
OOMP.parts.append(newPart)
