import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 2
newPart.addTag('oompID','HEAD-I01-X-PI02-RS')
newPart.addTag('name','2.54 mm 2 Pin Header Right Angle (SMD)')
newPart.addTag('oompType','HEAD')
newPart.addTag('oompSize','I01')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','PI02')
newPart.addTag('oompIndex','RS')
newPart.addTag('oompVersion','999')
newPart.addTag('ooNumPins','2')
newPart.addTag('oompBbls','variable;clear')
newPart.addTag('oompBbls','variable;pins;2')
newPart.addTag('oompBbls','template;HEAD-I01-X-XX-RS-bbls')
newPart.addTag('oompDiag','variable;clear')
newPart.addTag('oompDiag','variable;pins;2')
newPart.addTag('oompDiag','template;HEAD-I01-X-XX-RS-diag')
newPart.addTag('oompIden','variable;clear')
newPart.addTag('oompIden','variable;pins;2')
newPart.addTag('oompIden','template;HEAD-I01-X-XX-RS-iden')
newPart.addTag('oompSimp','variable;clear')
newPart.addTag('oompSimp','variable;pins;2')
newPart.addTag('oompSimp','template;HEAD-I01-X-XX-RS-simp')
newPart.addTag('oompSchem','variable;clear')
newPart.addTag('oompSchem','variable;pins;2')
newPart.addTag('oompSchem','template;XXXX-XX-X-XX-01-PINS-EVEN-schem')
newPart.addTag('ooDesignator','J1')
newPart.addTag('schematicSymbol','HEAD-XX-X-PI02-XX')
newPart.addTag('pcbFootprint','HEAD-I01-X-PI02-RS')
newPart = OOMPtags.addTags(newPart,"HEAD-I01-X-PI02-RS",pins = 2)
OOMP.parts.append(newPart)
