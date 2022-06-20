import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 8
newPart.addTag('oompID','ICIC-DI08-X-K555-01')
newPart.addTag('name','8 Pin DIP 555 Timer')
newPart.addTag('hexID','IC555')
newPart.addTag('oompSort','ICICDI08K555')
newPart.addTag('oompType','ICIC')
newPart.addTag('oompSize','DI08')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','K555')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','98')
newPart.addTag('ooNumPins','8')
newPart.addTag('ooFootprint','OOMP-ICIC-DI08-X-XXXX-01')
newPart.addTag('ooPin1','GND')
newPart.addTag('ooPin2','TRIGGER')
newPart.addTag('ooPin3','OUTPUT')
newPart.addTag('ooPin4','RESET')
newPart.addTag('ooPin5','CONTROL-VOLTAGE')
newPart.addTag('ooPin6','THRESHOLD')
newPart.addTag('ooPin7','DISCHARGE')
newPart.addTag('ooPin8','Vcc')
newPart.addTag('oompDiag','template;ICIC-DI08-X-XXXX-01-diag')
newPart.addTag('ooPackageMarking','ISDP1820P')
newPart.addTag('ooDesignator','U')
newPart = OOMPtags.addTags(newPart,"ICIC-DI08-X-K555-01",pins = 8)
OOMP.parts.append(newPart)
