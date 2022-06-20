import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2
newPart.addTag('oompID','BUTA-06-X-PI02-01')
newPart.addTag('name','6 mm 2 Pin Pushbutton (Tactile)')
newPart.addTag('hexID','BT62')
newPart.addTag('oompSort','')
newPart.addTag('oompClass','Through Hole')
newPart.addTag('oompClassCode','THTH')
newPart.addTag('oompType','BUTA')
newPart.addTag('oompSize','06')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','PI02')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','40')
newPart.addTag('ooWidth','6 mm')
newPart.addTag('ooHeight','3.5 mm')
newPart.addTag('ooDepth','3.5 mm')
newPart.addTag('ooNumPins','2')
newPart.addTag('ooLifetime','50 000 cycles')
newPart.addTag('oompAbout','A simple tactile pushbutton with two pins. This button is not commonly used. However it is imcluded in OOMP due to it being a part in the SEEED OPL. For a more commonly used through hole button we recommend (BUTA-06-X-STAN-01)')
newPart.addTag('oompSchem','template;BUTA-XXXX-X-PI02-XX-schem')
newPart.addTag('ooDesignator','S')
newPart.addTag('oompSymbol','twoSidedPackage;##ooNumPins@@/2')
newPart.addTag('ooPin1','.')
newPart.addTag('ooPin2','.')
newPart = OOMPtags.addTags(newPart,"BUTA-06-X-PI02-01",pins = 2)
OOMP.parts.append(newPart)
