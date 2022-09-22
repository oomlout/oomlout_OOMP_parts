import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2
newPart.addTag('index','4280')
newPart.addTag('hexID','CTS35U010F')
newPart.addTag('oompType','CAPT')
newPart.addTag('oompSize','3528')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','UF10')
newPart.addTag('oompIndex','V16')
newPart.addTag('oompVersion','99')
newPart.addTag('ooNumPins','2')
newPart.addTag('oompClass','Surface Mount')
newPart.addTag('oompClassCode','SMDS')
newPart.addTag('oompSchem','template;CAPT-XXXX-X-XXXX-XX-schem')
newPart.addTag('ooDesignator','C1')
newPart = OOMPtags.addTags(newPart,"CAPT-3528-X-UF10-V16",pins = 2)
OOMP.parts.append(newPart)
