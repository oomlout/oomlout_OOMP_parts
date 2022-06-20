import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2
newPart.addTag('oompID','DIOS-S123-X-A01-01')
newPart.addTag('name','SMD (SOD-123) 1 Amp Diode (Schottky)')
newPart.addTag('hexID','DS35D1')
newPart.addTag('oompSort','DIOSS123A01')
newPart.addTag('oompType','DIOS')
newPart.addTag('oompSize','S123')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','A01')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','98')
newPart.addTag('ooNumPins','2')
newPart.addTag('ooPackageMarking','SF')
newPart.addTag('ooDesignator','D1')
newPart = OOMPtags.addTags(newPart,"DIOS-S123-X-A01-01",pins = 2)
OOMP.parts.append(newPart)
