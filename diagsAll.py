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

# TEMPLATE  template;BUTA-06-X-STAN-01
linewidth = 0.5    #  linewidth;0.5
######  rectangle;0;0;6.2;6.2;main bounding box
x = 0
y = (0)* -1
width = 6.2
height = 6.2
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

#  circle;0;0;3;3;button circle
######  rectangle;-3.25;2.25;1;1;pins
x = -3.25
y = (2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;3.25;2.25;1;1;pins
x = 3.25
y = (2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;3.25;-2.25;1;1;pins
x = 3.25
y = (-2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-3.25;-2.25;1;1;pins
x = -3.25
y = (-2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))


# MISSING TEMPLATE # TEMPLATE  template;XXXX-XXXX-X-XXXX-XX-bbls-words

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

# TEMPLATE  template;BUTA-06-X-STAN-01
linewidth = 0.5    #  linewidth;0.5
######  rectangle;0;0;6.2;6.2;main bounding box
x = 0
y = (0)* -1
width = 6.2
height = 6.2
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

#  circle;0;0;3;3;button circle
######  rectangle;-3.25;2.25;1;1;pins
x = -3.25
y = (2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;3.25;2.25;1;1;pins
x = 3.25
y = (2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;3.25;-2.25;1;1;pins
x = 3.25
y = (-2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-3.25;-2.25;1;1;pins
x = -3.25
y = (-2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

# TEMPLATE  template;BUTA-06-X-STAN-01
linewidth = 0.5    #  linewidth;0.5
######  rectangle;0;0;6.2;6.2;main bounding box
x = 0
y = (0)* -1
width = 6.2
height = 6.2
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

#  circle;0;0;3;3;button circle
######  rectangle;-3.25;2.25;1;1;pins
x = -3.25
y = (2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;3.25;2.25;1;1;pins
x = 3.25
y = (2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;3.25;-2.25;1;1;pins
x = 3.25
y = (-2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-3.25;-2.25;1;1;pins
x = -3.25
y = (-2.25)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;BUTA-XXXX-X-XXXX-XX-schem

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-06-X-STAN-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

# TEMPLATE  template;BUTA-12-X-STAN-01
linewidth = 0.5    #  linewidth;0.5
######  rectangle;0;0;12.5;12.5;main bounding box
x = 0
y = (0)* -1
width = 12.5
height = 12.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

#  circle;0;0;8;8;button circle
######  rectangle;0;0;3;3;central square
x = 0
y = (0)* -1
width = 3
height = 3
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-6.75;2.5;1;1;pins
x = -6.75
y = (2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;6.75;2.5;1;1;pins
x = 6.75
y = (2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;6.75;-2.5;1;1;pins
x = 6.75
y = (-2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-6.75;-2.5;1;1;pins
x = -6.75
y = (-2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))


# MISSING TEMPLATE # TEMPLATE  template;XXXX-XXXX-X-XXXX-XX-bbls-words

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

# TEMPLATE  template;BUTA-12-X-STAN-01
linewidth = 0.5    #  linewidth;0.5
######  rectangle;0;0;12.5;12.5;main bounding box
x = 0
y = (0)* -1
width = 12.5
height = 12.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

#  circle;0;0;8;8;button circle
######  rectangle;0;0;3;3;central square
x = 0
y = (0)* -1
width = 3
height = 3
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-6.75;2.5;1;1;pins
x = -6.75
y = (2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;6.75;2.5;1;1;pins
x = 6.75
y = (2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;6.75;-2.5;1;1;pins
x = 6.75
y = (-2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-6.75;-2.5;1;1;pins
x = -6.75
y = (-2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))


# MISSING TEMPLATE # TEMPLATE  template;XXXX-XXXX-X-XXXX-XX-diag-words

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

# TEMPLATE  template;BUTA-12-X-STAN-01
linewidth = 0.5    #  linewidth;0.5
######  rectangle;0;0;12.5;12.5;main bounding box
x = 0
y = (0)* -1
width = 12.5
height = 12.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

#  circle;0;0;8;8;button circle
######  rectangle;0;0;3;3;central square
x = 0
y = (0)* -1
width = 3
height = 3
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-6.75;2.5;1;1;pins
x = -6.75
y = (2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;6.75;2.5;1;1;pins
x = 6.75
y = (2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;6.75;-2.5;1;1;pins
x = 6.75
y = (-2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-6.75;-2.5;1;1;pins
x = -6.75
y = (-2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))


# MISSING TEMPLATE # TEMPLATE  template;XXXX-XXXX-X-XXXX-XX-iden-words

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;BUTA-XXXX-X-XXXX-XX-schem

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

# TEMPLATE  template;BUTA-12-X-STAN-01
linewidth = 0.5    #  linewidth;0.5
######  rectangle;0;0;12.5;12.5;main bounding box
x = 0
y = (0)* -1
width = 12.5
height = 12.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

#  circle;0;0;8;8;button circle
######  rectangle;0;0;3;3;central square
x = 0
y = (0)* -1
width = 3
height = 3
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-6.75;2.5;1;1;pins
x = -6.75
y = (2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;6.75;2.5;1;1;pins
x = 6.75
y = (2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;6.75;-2.5;1;1;pins
x = 6.75
y = (-2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  rectangle;-6.75;-2.5;1;1;pins
x = -6.75
y = (-2.5)* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))


# MISSING TEMPLATE # TEMPLATE  template;XXXX-XXXX-X-XXXX-XX-simp-words

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/BUTA-12-X-STAN-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 2    #  variable;pins;2
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
shape = text('2.54 mm 2 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H02',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 2    #  variable;pins;2
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 2    #  variable;pins;2
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 2    #  variable;pins;2
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
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

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
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
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
shapes.append(shape)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H02',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

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
shapes.append(shape)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 2 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 2    #  variable;pins;2
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H02',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI02-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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
shape = text('2.54 mm 3 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H03',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 3    #  variable;pins;3
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 3    #  variable;pins;3
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 3    #  variable;pins;3
# TEMPLATE  template;XXXX-XX-X-XX-01-PINS-ODD-schem
linewidth = 1    #  linewidth;1
######  rectangle;0;0;13;10*pins;Square
x = 0
y = (0)* -1
width = 13
height = 10*pins
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

for b in range(pins):    # repeat;pins;hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&
    i = b + 1
    ######  hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&;
    x = 9
    y = ((pins*10/2)-(i-1)*10-5)* -1
    width = 5
    height = 0
    x1 = x - width/2 
    y1 = y - height/2 
    x2 = x + width/2 
    y2 = y + height/2 
    shape = polyline([((x1+shiftX/2)*mm,(y1+shiftY/2)*mm),((x2+shiftX/2)*mm,(y2+shiftY/2)*mm)],fill='#000000',stroke_width=1)
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;4;(pins*10/2)-(&&i&&-1)*10-5;3.5;PIN &&i&&
    i = b + 1
    x = 4
    y = ((pins*10/2)-(i-1)*10-5)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
######  oompURL;0;-(%%pins%%*10/2)-3.5;20;3.5;3;##hexID@@
x = 0
y = (-(pins*10/2)-3.5)* -1
width = 20
height = 3.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (-(pins*10/2)-3.5)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H03',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

######  oompName;0;(%%pins%%*10/2)+3;20;5;5;##name@@
x = 0
y = ((pins*10/2)+3)* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = ((pins*10/2)+3)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 3 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 3    #  variable;pins;3
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H03',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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
# MISSING TEMPLATE # TEMPLATE  template;XXXX-I01-X-XX-OOEB-bbls

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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
os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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
# TEMPLATE  template;XXXX-XX-X-XX-01-PINS-ODD-schem
linewidth = 1    #  linewidth;1
######  rectangle;0;0;13;10*pins;Square
x = 0
y = (0)* -1
width = 13
height = 10*pins
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

for b in range(pins):    # repeat;pins;hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&
    i = b + 1
    ######  hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&;
    x = 9
    y = ((pins*10/2)-(i-1)*10-5)* -1
    width = 5
    height = 0
    x1 = x - width/2 
    y1 = y - height/2 
    x2 = x + width/2 
    y2 = y + height/2 
    shape = polyline([((x1+shiftX/2)*mm,(y1+shiftY/2)*mm),((x2+shiftX/2)*mm,(y2+shiftY/2)*mm)],fill='#000000',stroke_width=1)
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;4;(pins*10/2)-(&&i&&-1)*10-5;3.5;PIN &&i&&
    i = b + 1
    x = 4
    y = ((pins*10/2)-(i-1)*10-5)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
######  oompURL;0;-(%%pins%%*10/2)-3.5;20;3.5;3;##hexID@@
x = 0
y = (-(pins*10/2)-3.5)* -1
width = 20
height = 3.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (-(pins*10/2)-3.5)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H03OOEB',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

######  oompName;0;(%%pins%%*10/2)+3;20;5;5;##name@@
x = 0
y = ((pins*10/2)+3)* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = ((pins*10/2)+3)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 3 Pin Header (OOEB)',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H03OOEB',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-RA/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 4    #  variable;pins;4
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
shape = text('2.54 mm 4 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H04',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 4    #  variable;pins;4
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 4    #  variable;pins;4
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 4    #  variable;pins;4
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
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

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
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
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
shapes.append(shape)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H04',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

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
shapes.append(shape)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 4 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 4    #  variable;pins;4
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H04',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI04-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 5    #  variable;pins;5
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
shape = text('2.54 mm 5 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H05',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 5    #  variable;pins;5
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 5    #  variable;pins;5
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 5    #  variable;pins;5
# TEMPLATE  template;XXXX-XX-X-XX-01-PINS-ODD-schem
linewidth = 1    #  linewidth;1
######  rectangle;0;0;13;10*pins;Square
x = 0
y = (0)* -1
width = 13
height = 10*pins
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

for b in range(pins):    # repeat;pins;hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&
    i = b + 1
    ######  hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&;
    x = 9
    y = ((pins*10/2)-(i-1)*10-5)* -1
    width = 5
    height = 0
    x1 = x - width/2 
    y1 = y - height/2 
    x2 = x + width/2 
    y2 = y + height/2 
    shape = polyline([((x1+shiftX/2)*mm,(y1+shiftY/2)*mm),((x2+shiftX/2)*mm,(y2+shiftY/2)*mm)],fill='#000000',stroke_width=1)
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;4;(pins*10/2)-(&&i&&-1)*10-5;3.5;PIN &&i&&
    i = b + 1
    x = 4
    y = ((pins*10/2)-(i-1)*10-5)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
######  oompURL;0;-(%%pins%%*10/2)-3.5;20;3.5;3;##hexID@@
x = 0
y = (-(pins*10/2)-3.5)* -1
width = 20
height = 3.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (-(pins*10/2)-3.5)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H05',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

######  oompName;0;(%%pins%%*10/2)+3;20;5;5;##name@@
x = 0
y = ((pins*10/2)+3)* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = ((pins*10/2)+3)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 5 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 5    #  variable;pins;5
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H05',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI05-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 6    #  variable;pins;6
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
shape = text('2.54 mm 6 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H06',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 6    #  variable;pins;6
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 6    #  variable;pins;6
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 6    #  variable;pins;6
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
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

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
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
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
shapes.append(shape)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H06',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

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
shapes.append(shape)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 6 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 6    #  variable;pins;6
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H06',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI06-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 7    #  variable;pins;7
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
shape = text('2.54 mm 7 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H07',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 7    #  variable;pins;7
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 7    #  variable;pins;7
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 7    #  variable;pins;7
# TEMPLATE  template;XXXX-XX-X-XX-01-PINS-ODD-schem
linewidth = 1    #  linewidth;1
######  rectangle;0;0;13;10*pins;Square
x = 0
y = (0)* -1
width = 13
height = 10*pins
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

for b in range(pins):    # repeat;pins;hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&
    i = b + 1
    ######  hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&;
    x = 9
    y = ((pins*10/2)-(i-1)*10-5)* -1
    width = 5
    height = 0
    x1 = x - width/2 
    y1 = y - height/2 
    x2 = x + width/2 
    y2 = y + height/2 
    shape = polyline([((x1+shiftX/2)*mm,(y1+shiftY/2)*mm),((x2+shiftX/2)*mm,(y2+shiftY/2)*mm)],fill='#000000',stroke_width=1)
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;4;(pins*10/2)-(&&i&&-1)*10-5;3.5;PIN &&i&&
    i = b + 1
    x = 4
    y = ((pins*10/2)-(i-1)*10-5)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
######  oompURL;0;-(%%pins%%*10/2)-3.5;20;3.5;3;##hexID@@
x = 0
y = (-(pins*10/2)-3.5)* -1
width = 20
height = 3.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (-(pins*10/2)-3.5)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H07',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

######  oompName;0;(%%pins%%*10/2)+3;20;5;5;##name@@
x = 0
y = ((pins*10/2)+3)* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = ((pins*10/2)+3)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 7 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 7    #  variable;pins;7
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H07',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI07-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 8    #  variable;pins;8
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
shape = text('2.54 mm 8 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H08',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 8    #  variable;pins;8
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 8    #  variable;pins;8
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 8    #  variable;pins;8
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
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

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
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
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
shapes.append(shape)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H08',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

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
shapes.append(shape)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 8 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 8    #  variable;pins;8
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H08',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI08-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 9    #  variable;pins;9
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
shape = text('2.54 mm 9 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H09',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 9    #  variable;pins;9
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 9    #  variable;pins;9
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 9    #  variable;pins;9
# TEMPLATE  template;XXXX-XX-X-XX-01-PINS-ODD-schem
linewidth = 1    #  linewidth;1
######  rectangle;0;0;13;10*pins;Square
x = 0
y = (0)* -1
width = 13
height = 10*pins
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

for b in range(pins):    # repeat;pins;hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&
    i = b + 1
    ######  hLine;9;(pins*10/2)-(&&i&&-1)*10-5;5;0;pin &&i&&;
    x = 9
    y = ((pins*10/2)-(i-1)*10-5)* -1
    width = 5
    height = 0
    x1 = x - width/2 
    y1 = y - height/2 
    x2 = x + width/2 
    y2 = y + height/2 
    shape = polyline([((x1+shiftX/2)*mm,(y1+shiftY/2)*mm),((x2+shiftX/2)*mm,(y2+shiftY/2)*mm)],fill='#000000',stroke_width=1)
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;4;(pins*10/2)-(&&i&&-1)*10-5;3.5;PIN &&i&&
    i = b + 1
    x = 4
    y = ((pins*10/2)-(i-1)*10-5)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
######  oompURL;0;-(%%pins%%*10/2)-3.5;20;3.5;3;##hexID@@
x = 0
y = (-(pins*10/2)-3.5)* -1
width = 20
height = 3.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (-(pins*10/2)-3.5)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H09',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

######  oompName;0;(%%pins%%*10/2)+3;20;5;5;##name@@
x = 0
y = ((pins*10/2)+3)* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = ((pins*10/2)+3)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 9 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 9    #  variable;pins;9
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H09',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI09-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 10    #  variable;pins;10
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
shape = text('2.54 mm 10 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H10',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 10    #  variable;pins;10
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 10    #  variable;pins;10
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 10    #  variable;pins;10
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
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

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
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
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
shapes.append(shape)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H10',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

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
shapes.append(shape)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 10 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 10    #  variable;pins;10
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H10',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI10-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 12    #  variable;pins;12
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
shape = text('2.54 mm 12 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H12',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 12    #  variable;pins;12
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 12    #  variable;pins;12
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 12    #  variable;pins;12
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
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

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
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
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
shapes.append(shape)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H12',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

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
shapes.append(shape)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 12 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 12    #  variable;pins;12
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H12',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI12-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 14    #  variable;pins;14
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
shape = text('2.54 mm 14 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H14',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 14    #  variable;pins;14
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 14    #  variable;pins;14
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 14    #  variable;pins;14
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
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

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
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
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
shapes.append(shape)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H14',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

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
shapes.append(shape)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 14 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 14    #  variable;pins;14
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H14',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI14-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 16    #  variable;pins;16
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
shape = text('2.54 mm 16 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H16',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 16    #  variable;pins;16
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 16    #  variable;pins;16
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

pins = 16    #  variable;pins;16
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
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

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
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
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
shapes.append(shape)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H16',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

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
shapes.append(shape)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 16 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 16    #  variable;pins;16
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H16',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI16-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

pins = 18    #  variable;pins;18
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
shape = text('2.54 mm 18 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
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
shape = text('http://oom.lt/H18',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

pins = 18    #  variable;pins;18
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

pins = 18    #  variable;pins;18
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

x = 0
y = (0)* -1
fontShift = (4)* 0.3527 * .5
shapes.append(text('"J1"',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='4pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

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
    shapes.append(shape)
    
for b in range(pins):    # repeat;pins;textB;2;(pins*10/2)-(&&i&&-1)*10;3.5;PIN &&i&&
    i = b + 1
    x = 2
    y = ((pins*10/2)-(i-1)*10)* -1
    fontShift = (3.5)* 0.3527 * .5
    shapes.append(text('PIN ' + str(i) + '',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke='#000000',font_size='3.5pt',font_family='Relief Single Line Outline',text_anchor='middle',stroke_width=0.25))
    
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
shapes.append(shape)
x = 0
y = (-(pins*10/2)+2)* -1
fontShift = (3)* 0.3527 * .5
shape = text('http://oom.lt/H18',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='3pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)

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
shapes.append(shape)
x = 0
y = ((pins*10/2)+8)* -1
fontShift = (5)* 0.3527 * .5
shape = text('2.54 mm 18 Pin Header',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.4,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

pins = 18    #  variable;pins;18
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shapes.append(rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth))

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shapes.append(shape)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H18',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
shapes.append(shape)


os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI18-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;LEDS-10-X-XXXX-01-bbls

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;LEDS-10-X-XXXX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;LEDS-10-X-XXXX-01-iden

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;LEDS-XXXX-X-XXXX-XX-schem

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;LEDS-10-X-XXXX-01-simp

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/LEDS-10-R-FROS-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/PHTR-05-I9-STAN-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/POTE-95D-L-O103-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;RESE-W04-X-XXXX-XX-bbls

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;RESE-W04-X-XXXX-XX-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;RESE-W04-X-XXXX-XX-iden

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;RESE-XXXX-X-XXXX-XX-schem

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;RESE-W04-X-XXXX-XX-simp

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/RESE-W04-X-O561-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;XXXX-T220-X-XXXX-01-bbls

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;XXXX-T220-X-XXXX-01-diag

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;XXXX-T220-X-XXXX-01-iden

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/diagIDEN.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagIDEN.svg')

for shape in shapes:
    shape.remove()
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

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/diagSCHEM.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')

for shape in shapes:
    shape.remove()
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

# MISSING TEMPLATE # TEMPLATE  template;XXXX-T220-X-XXXX-01-simp

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/TRNN-T220-BCE-A05-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')

for shape in shapes:
    shape.remove()
