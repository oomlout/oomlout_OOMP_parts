import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pitch = 3.5
pins = 8
newPart.addTag('oompID','TERS-35D-L-PI08-01')
newPart.addTag('name','3.5 mm 8 Pin Blue Screw Terminal')
newPart.addTag('hexID','ST308L')
newPart.addTag('oompSort','TERS35D08PI')
newPart.addTag('oompClass','Through Hole')
newPart.addTag('oompClassCode','THTH')
newPart.addTag('oompType','TERS')
newPart.addTag('oompSize','35D')
newPart.addTag('oompColor','L')
newPart.addTag('oompDesc','PI08')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','98')
newPart.addTag('ooPitch','3.5mm')
newPart.addTag('ooNumPins','8')
newPart.addTag('ooFootprint','OOMP-TERS-35D-X-PI08-01')
newPart.addTag('ooDesignator','J1')
newPart = OOMPtags.addTags(newPart,"TERS-35D-L-PI08-01",pitch = 3.5,pins = 8)
OOMP.parts.append(newPart)
