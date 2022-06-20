import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2
newPart.addTag('oompID','BAHO-CR1220-X-SMDS-01')
newPart.addTag('name','CR1220 SMD Battery Holder')
newPart.addTag('hexID','BHS1220')
newPart.addTag('oompSort','')
newPart.addTag('oompClass','Surface Mount')
newPart.addTag('oompClassCode','SMDS')
newPart.addTag('oompType','BAHO')
newPart.addTag('oompSize','CR1220')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','SMDS')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','40')
newPart.addTag('ooWidth','15.06 mm')
newPart.addTag('ooHeight','4.10 mm')
newPart.addTag('ooLength','15 mm')
newPart.addTag('ooNumPins','2')
newPart.addTag('oompAbout','A surface mount battery holder for a CR1220 lithium ion button cell. Commonly used as a battery backup for on board clocks.')
newPart.addTag('oompSchem','template;BAHO-XXXX-X-XXXX-XX-schem')
newPart.addTag('ooDesignator','BT1')
newPart = OOMPtags.addTags(newPart,"BAHO-CR1220-X-SMDS-01",pins = 2)
OOMP.parts.append(newPart)
