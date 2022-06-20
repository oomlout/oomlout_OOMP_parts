import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2
newPart.addTag('oompID','SENS-05-X-LIRE-01')
newPart.addTag('name','5 mm Light (Resistive) Sensor')
newPart.addTag('hexID','SEPR')
newPart.addTag('oompSort','SENS05LIRE')
newPart.addTag('oompType','SENS')
newPart.addTag('oompSize','05')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','LIRE')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','98')
newPart.addTag('ooDiameter','5.0 mm')
newPart.addTag('ooNumPins','2')
newPart.addTag('ooDesignator','0')
newPart = OOMPtags.addTags(newPart,"SENS-05-X-LIRE-01",pins = 2)
OOMP.parts.append(newPart)
