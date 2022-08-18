import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()
newPart.addTag('oompID','MOSN-T252-X-A50-01')
newPart.addTag('hexID','MNAOD4184A')

newPart.addTag('oompSort','')
newPart.addTag('oompClass','Surface Mount')
newPart.addTag('oompClassCode','SMDS')
newPart.addTag('oompType','MOSN')
newPart.addTag('oompSize','T252')
newPart.addTag('oompColor','X')
newPart.addTag('oompDesc','K4184')
newPart.addTag('oompIndex','01')
newPart.addTag('oompVersion','40')
newPart.addTag('ooPin1','Q')
newPart.addTag('ooPin2','D')
newPart.addTag('ooPin3','S')
newPart.addTag('ooDesignator','Q1')

######  EDA
newPart.addTag("footprintKicad","FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-TO-252-3_TabPin2")  
#newPart.addTag("symbolKicad","")  

newPart.addTag('manufacturerPartNumber','AOD4184A')

newPart = OOMPtags.addTags(newPart,'MOSN-T252-X-A50-01')
OOMP.parts.append(newPart)
