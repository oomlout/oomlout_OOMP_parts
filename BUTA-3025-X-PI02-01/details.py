import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2
newPart.addTag('oompID','BUTA-3025-X-PI02-01')
newPart.addTag('name','SMD (3025) 2 Pin Pushbutton (Tactile)')
newPart.addTag('hexID','BT3025')
newPart.addTag('oompSort','BUTA302502PI')
newPart.addTag('oompType','BUTA')
newPart.addTag('oompSize','3025')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','PI02')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','98')
newPart.addTag('ooNumPins','2')
newPart.addTag('oompSchem','template;BUTA-XXXX-X-PI02-XX-schem')
newPart.addTag('ooDesignator','S')
newPart.addTag('oompSymbol','twoSidedPackage;##ooNumPins@@/2')
newPart.addTag('ooPin1','.')
newPart.addTag('ooPin2','.')
newPart = OOMPtags.addTags(newPart,"BUTA-3025-X-PI02-01",pins = 2)
OOMP.parts.append(newPart)
