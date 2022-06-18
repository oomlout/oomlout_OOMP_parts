import OOMP
import OOMPtags

pitch=2.54
pins = 4

newPart = OOMP.oompItem()

newPart = OOMPtags.addTags(newPart,"HEAD-I01-X-X-X",pins=pins)




OOMP.parts.append(newPart)
