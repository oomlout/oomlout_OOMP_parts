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

#  CLEAR variable;clear
pins = 3    #  variable;pins;3
# MISSING TEMPLATE # TEMPLATE  template;XXXX-I01-X-XX-OOEB-bbls

os.chdir("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/")
try:
    os.remove("C:/GH/oomlout_OOMP/oomlout_OOMP_parts/HEAD-I01-X-PI03-OOEB/diagBBLS.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagBBLS.svg')