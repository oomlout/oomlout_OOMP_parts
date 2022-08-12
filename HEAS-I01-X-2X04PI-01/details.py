import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2*4
newPart.addTag('oompID','HEAS-I01-X-2X04PI-01')
newPart.addTag('hexID','HSX4')
newPart.addTag('oompSort','HEAS012X04PI')
newPart.addTag('oompType','HEAS')
newPart.addTag('oompSize','I01')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','2X04PI')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','98')
newPart.addTag('ooNumPins','2X04')
newPart.addTag('ooFootprint','OOMP-HEAD-I01-X-2X04PI-01')
newPart.addTag('ooDesignator','J1')
newPart = OOMPtags.addTags(newPart,"HEAS-I01-X-2X04PI-01",pins = 2*4)
OOMP.parts.append(newPart)
