import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 3
newPart.addTag('oompID','SENS-T92-X-K36-01')
newPart.addTag('name','TO-92 Temperature (TMP36) Sensor')
newPart.addTag('hexID','SE36')
newPart.addTag('oompSort','SENST92K36')
newPart.addTag('oompType','SENS')
newPart.addTag('oompSize','T92')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','K36')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','98')
newPart.addTag('ooNumPins','3')
newPart.addTag('ooPackageMarking','TMP36')
newPart.addTag('ooDesignator','U')
newPart = OOMPtags.addTags(newPart,"SENS-T92-X-K36-01",pins = 3)
OOMP.parts.append(newPart)
