import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2
newPart.addTag('oompID','SENS-92D-X-PIRS-01')
newPart.addTag('name','9.2 mm PIRS Sensor')
newPart.addTag('hexID','SEPI')
newPart.addTag('oompSort','SENS92DPIRS')
newPart.addTag('oompType','SENS')
newPart.addTag('oompSize','92D')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','PIRS')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','98')
newPart.addTag('ooDiameter','9.2 mm')
newPart.addTag('ooNumPins','2')
newPart.addTag('ooDesignator','0')
newPart = OOMPtags.addTags(newPart,"SENS-92D-X-PIRS-01",pins = 2)
OOMP.parts.append(newPart)
