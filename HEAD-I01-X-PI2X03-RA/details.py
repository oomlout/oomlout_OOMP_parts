import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
pins = 6
newPart.addTag('hexID','HR2X03')
newPart.addTag('oompSort','')
newPart.addTag('oompType','HEAD')
newPart.addTag('oompSize','I01')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','PI2X03')
newPart.addTag('oompIndex','RA')
newPart.addTag('oompVersion','98')
newPart.addTag('ooNumRows','2')
newPart.addTag('ooNumPins','6')
newPart.addTag('ooFootprint','OOMP-HEAD-I01-X-PI2X03-01')
newPart = OOMPtags.addTags(newPart,"HEAD-I01-X-PI2X03-RA",pins = 6)
OOMP.parts.append(newPart)
