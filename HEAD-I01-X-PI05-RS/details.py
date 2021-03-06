import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 5
newPart.addTag('oompID','HEAD-I01-X-PI05-RS')
newPart.addTag('name','2.54 mm 5 Pin Header Right Angle (SMD)')
newPart.addTag('oompType','HEAD')
newPart.addTag('oompSize','I01')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','PI05')
newPart.addTag('oompIndex','RS')
newPart.addTag('oompVersion','999')
newPart.addTag('ooNumPins','5')
newPart.addTag('oompBbls','variable;clear')
newPart.addTag('oompBbls','variable;pins;5')
newPart.addTag('oompBbls','template;HEAD-I01-X-XX-RS-bbls')
newPart.addTag('oompDiag','variable;clear')
newPart.addTag('oompDiag','variable;pins;5')
newPart.addTag('oompDiag','template;HEAD-I01-X-XX-RS-diag')
newPart.addTag('oompIden','variable;clear')
newPart.addTag('oompIden','variable;pins;5')
newPart.addTag('oompIden','template;HEAD-I01-X-XX-RS-iden')
newPart.addTag('oompSimp','variable;clear')
newPart.addTag('oompSimp','variable;pins;5')
newPart.addTag('oompSimp','template;HEAD-I01-X-XX-RS-simp')
newPart.addTag('oompSchem','variable;clear')
newPart.addTag('oompSchem','variable;pins;5')
newPart.addTag('oompSchem','template;XXXX-XX-X-XX-01-PINS-ODD-schem')
newPart.addTag('ooDesignator','J1')
newPart.addTag('schematicSymbol','HEAD-XX-X-PI05-XX')
newPart.addTag('pcbFootprint','HEAD-I01-X-PI05-RS')
newPart = OOMPtags.addTags(newPart,"HEAD-I01-X-PI05-RS",pins = 5)
OOMP.parts.append(newPart)
