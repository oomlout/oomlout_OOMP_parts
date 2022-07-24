import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pitch = 2.54 
newPart.addTag('index','4128')
newPart.addTag('oompID','BREB-P170-X-STAN-01')
newPart.addTag('hexID','BB1')
newPart.addTag('oompSort','P170')
newPart.addTag('oompType','BREB')
newPart.addTag('oompSize','P170')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','STAN')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','99')
newPart.addTag('ooPitch','2.54 mm')
newPart.addTag('ooWidth','35 mm')
newPart.addTag('ooHeight','47 mm')
newPart.addTag('ooDepth','10 mm')
newPart.addTag('useTitle','Prototyping')
newPart.addTag('useDescription','a base for prototyping new circuits.')
newPart.addTag('oompAbout','The start of any project. Great for quickly prototyping a new ciruit. Compatible with most 2.54 mm (0.1") components.')
newPart.addTag('oompClass','Wiring')
newPart.addTag('oompClassCode','WIRE')
#newPart.addTag('oompBbls','template;BREB-P400-C-STAN-01-bbls')
newPart = OOMPtags.addTags(newPart,"BREB-P170-X-STAN-01",pitch = 2.54 )
OOMP.parts.append(newPart)
