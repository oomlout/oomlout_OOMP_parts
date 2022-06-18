import os
svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
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
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,fill='#FFFFFF',stroke='#FFFFFF',stroke_width=0.0)

pins = 18    #  variable;pins;18
# TEMPLATE  template;XXXX-XX-X-XX-01-PINS-EVEN-schem
linewidth = 1    #  linewidth;1
######  rectangle;0;5;13;10*pins;Square
x = 0
y = (5)* -1
width = 13
height = 10*pins
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

for b in range(pins):    # repeat;pins;hLine;7.5;(pins*10/2)-(&&i&&-1)*10;5;0;pin &&i&&
    i = b + 1
    ######  hLine;7.5;(pins*10/2)-(&&i&&-1)*10;5;0;pin &&i&&;
    x = 7.5
    y = ((pins*10/2)-(i-1)*10)* -1
    width = 5
    height = 0
    x1 = x - width/2 
    y1 = y - height/2 
    x2 = x + width/2 
    y2 = y + height/2 
    shape = polyline([((x1+shiftX/2)*mm,(y1+shiftY/2)*mm),((x2+shiftX/2)*mm,(y2+shiftY/2)*mm)],fill='#000000',stroke_width=1)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25)
    
######  oompURL;0;-(%%pins%%*10/2)+2;20;3.5;3;##hexID@@
x = 0
y = (-(pins*10/2)+2)* -1
width = 20
height = 3.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H18',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)

######  oompName;0;(%%pins%%*10/2)+8;20;5;5;##name@@
x = 0
y = ((pins*10/2)+8)* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 18 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')