import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2
newPart.addTag('index','')
newPart.addTag('hexID','CTS60U047')
newPart.addTag('oompType','CAPT')
newPart.addTag('oompSize','6032')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','UF47')
newPart.addTag('oompIndex','V16')
newPart.addTag('oompVersion','99')
newPart.addTag('oompClass','Surface Mount')
newPart.addTag('oompClassCode','SMDS')
newPart.addTag('ooWidth','0.8 mm')
newPart.addTag('ooLength','1.6 mm')
newPart.addTag('ooNumPins','2')
newPart.addTag('oompSchem','template;CAPT-XXXX-X-XXXX-XX-schem')
newPart.addTag('ooDesignator','C1')
newPart = OOMPtags.addTags(newPart,"CAPT-6032-X-UF47-V16",pins = 2)
OOMP.parts.append(newPart)
