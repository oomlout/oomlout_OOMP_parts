import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 3
newPart.addTag('oompID','VREG-SO23-X-ADJU-AE')
newPart.addTag('name','SMD (SOT-23) Adjustable Voltage Regulator 200 mA')
newPart.addTag('hexID','VS3A2D')
newPart.addTag('oompSort','VREGSO23ADJU')
newPart.addTag('oompType','VREG')
newPart.addTag('oompSize','SO23')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','ADJU')
newPart.addTag('oompIndex','AE')
newPart.addTag('oompVersion','98')
newPart.addTag('ooNumPins','3')
newPart.addTag('ooPin1','REF')
newPart.addTag('ooPin2','CATH')
newPart.addTag('ooPin3','ANODE')
newPart.addTag('oompBbls','template;XXXX-SO23-X-XXXX-01-bbls')
newPart.addTag('oompDiag','template;XXXX-SO23-X-XXXX-01-diag')
newPart.addTag('oompIden','template;XXXX-SO23-X-XXXX-01-iden')
newPart.addTag('oompSimp','template;XXXX-SO23-X-XXXX-01-simp')
newPart.addTag('ooPackageMarking','432')
newPart.addTag('ooDesignator','U1')
newPart = OOMPtags.addTags(newPart,"VREG-SO23-X-ADJU-AE",pins = 3)
OOMP.parts.append(newPart)
