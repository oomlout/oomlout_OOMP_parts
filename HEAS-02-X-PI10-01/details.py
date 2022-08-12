import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 10
newPart.addTag('oompID','HEAS-02-X-PI10-01')
newPart.addTag('hexID','HS210')
newPart.addTag('oompSort','HEAS0210PI')
newPart.addTag('oompType','HEAS')
newPart.addTag('oompSize','02')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','PI10')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','98')
newPart.addTag('ooNumPins','10')
newPart.addTag('ooFootprint','OOMP-HEAD-I01-X-PI10-01')
newPart.addTag('ooDesignator','J1')
newPart = OOMPtags.addTags(newPart,"HEAS-02-X-PI10-01",pins = 10)
OOMP.parts.append(newPart)
