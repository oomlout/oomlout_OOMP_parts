import os
svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shapes=[]
shiftX=50
shiftY=50
x = 0
y = (0)* -1
width = 50
height = 50
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,fill='#FFFFFF',stroke='#FFFFFF',stroke_width=0.0))

######  rectangle;0;0;6.2;6.2;Main Square
x = 0
y = (0)* -1
width = 6.2
height = 6.2
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

#  circle;0;0;3.5;3.5;Main Button
#  circle;2.15;2.15;0.75;0.75;Circle Nub 1
#  circle;-2.15;-2.15;0.75;0.75;Circle Nub 2
#  circle;2.15;-2.15;0.75;0.75;Circle Nub 3
#  circle;-2.15;2.15;0.75;0.75;Circle Nub 4
######  rectangle;3.8;2.25;1.4;0.7;pad 1
x = 3.8
y = (2.25)* -1
width = 1.4
height = 0.7
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-3.8;-2.25;1.4;0.7;pad 2
x = -3.8
y = (-2.25)* -1
width = 1.4
height = 0.7
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-3.8;2.25;1.4;0.7;pad 3
x = -3.8
y = (2.25)* -1
width = 1.4
height = 0.7
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;3.8;-2.25;1.4;0.7;pad 4
x = 3.8
y = (-2.25)* -1
width = 1.4
height = 0.7
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

#  name;0;5;20;5;6 mm SMD Pushbutton (Tactile)
