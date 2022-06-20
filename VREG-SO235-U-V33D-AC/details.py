import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 5
newPart.addTag('oompID','VREG-SO235-U-V33D-AC')
newPart.addTag('name',' SMD (SOT-23-5) 3.3v Voltage Regulator 150 mA ')
newPart.addTag('hexID','VS533')
newPart.addTag('oompSort','VREGSO235V33D')
newPart.addTag('oompType','VREG')
newPart.addTag('oompSize','SO235')
newPart.addTag('oompColor','U')
newPart.addTag('oompDesc','V33D')
newPart.addTag('oompIndex','AC')
newPart.addTag('oompVersion','98')
newPart.addTag('ooNumPins','5')
newPart.addTag('ooDesignator','U1')
newPart = OOMPtags.addTags(newPart,"VREG-SO235-U-V33D-AC",pins = 5)
OOMP.parts.append(newPart)
