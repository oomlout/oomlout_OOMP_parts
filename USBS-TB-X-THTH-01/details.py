import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 4
newPart.addTag('index','9876')
newPart.addTag('oompID','USBS-TB-X-THTH-01')
newPart.addTag('name','Type B Through Hole USB Socket')
newPart.addTag('hexID','UTB')
newPart.addTag('oompSort','THTHTB')
newPart.addTag('oompType','USBS')
newPart.addTag('oompSize','TB')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','THTH')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','99')
newPart.addTag('oompSkip','true')
newPart.addTag('ooWidth','16 mm')
newPart.addTag('ooHeight','10.3 mm')
newPart.addTag('ooLength','12.2 mm')
newPart.addTag('ooNumPins','4')
newPart.addTag('oompClass','Through Hole Component')
newPart.addTag('oompClassCode','THTH')
newPart.addTag('oompSchem','template;USBS-XXXX-X-XXXX-XX-schem')
newPart.addTag('ooDesignator','J1')
newPart = OOMPtags.addTags(newPart,"USBS-TB-X-THTH-01",pins = 4)
OOMP.parts.append(newPart)
