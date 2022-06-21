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

#  CLEAR variable;clear
pins = 3    #  variable;pins;3
# TEMPLATE  template;XXXX-I01-X-XX-01-bbls
linewidth = 0.75    #  linewidth;0.75
######  pinHolder;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,fill='#000000',stroke_width=1))

linewidth = 0.75    #  linewidth;0.75
for b in range(pins):    # repeat;pins;pin;(2.54*pins/2-2.54/2)-2.54*(&&i&&-1);0;0.64;0.64;pin &&i&&
    i = b + 1
    ######  pin;(2.54*pins/2-2.54/2)-2.54*(&&i&&-1);0;0.64;0.64;pin &&i&&;
    x = (2.54*pins/2-2.54/2)-2.54*(i-1)
    y = (0)* -1
    width = 0.64
    height = 0.64
    x1 = x - width/2 
    y1 = y + height/2 
    x2 = x + width/2 
    y2 = y - height/2 
    shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,fill='#FFD700',stroke_width=0.5))
    
######  oompName;0;4;20;5;5;##name@@
x = 0
y = (4)* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (4)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 3 Pin Header (Long)',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

######  oompURL;0;-6;20;5;3;##hexID@@
x = 0
y = (-6)* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (-6)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/HL03',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAL-I01-X-PI03-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAL-I01-X-PI03-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()