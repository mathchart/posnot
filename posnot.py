import pygame as pg
import sys
from random import randint
from math import sqrt, cos, sin, radians, log, ceil
from myfuncs import *
 
pg.init()
w, h = 800,800
fenster = pg.display.set_mode((w, h))
pg.display.set_caption("Grouping for Positional Notation")
clock = pg.time.Clock()
FPS = 40

qty_dinge =  215
base = 2 
group_color  = []
dinge = [] 
dinged = []
groups = []
circle_points = []
newnumb = []
radius = 50
pos_width = w // ceil(log(qty_dinge,base))
print("position width: ",pos_width)





def newdinge(n):
    dinge = []
    for i in range(n):
        x = randint(radius,w-radius)
        y = randint(radius,h-210-radius)
        dinge.append((x,y))
    return dinge


def distfrom1(dinge):
    dinged = []
    for ding in dinge:
       dinged.append(((ding),dist(dinge[0],ding)))
    dinged = sorted(dinged,key=lambda x: x[1])
    return dinged


def grouptop(dd,base):
    hold = []
    for g in range(base):
        hold.append(dd[g][0])
    groups.append(hold)
    group_color.append(randcol())
    del dd[0:base]
    return groups,dd

def groupcenter(group):
    xs,ys = 0,0
    for p in group:
        xs += p[0]
        ys += p[1]
    cx = xs // len(group)
    cy = ys // len(group)
    return (cx,cy)

def encircle(group,cx,cy,r):
    ding_angle = 360 // len(group)
    circle_pts = []
    for n,pt in enumerate(group):
        x = int(cx + r*cos(n*radians(ding_angle)))
        y = int(cy + r*sin(n*radians(ding_angle)))
        circle_pts.append((x,y))
    return circle_pts

def group_pow(qty,base):
    newnumb = []
    power_of_base = 0
    groups = qty
    strnumb = ""
    while groups > 0:
        groups, rem = divmod(groups,base)
        newnumb.append(rem)
        strnumb = str(rem)+strnumb
        power_of_base +=1
    return newnumb
 

        
for i in range(qty_dinge//base):
    r = (50*i) % 255
    g = (50*i) % 255
    b = (50*i) % 255
    group_color.append((r,g,b))
dinge = newdinge(qty_dinge)
dinged = distfrom1(dinge)
while len(dinged) >= base:   
    groups,dinged = grouptop(dinged,base)
    #dinged = distfrom1(dinged)
   
hold = []
if len(dinged) > 0:
    for g in dinged:
        hold.append(g[0])
    groups.insert(0,hold)
for d in dinged:
    print(d)


col = randcol()
while True:
    clock.tick(FPS)
    for ereignis in pg.event.get():
        if ereignis.type == pg.QUIT: 
            pg.display.quit()       
            sys.exit()
        if ereignis.type == pg.MOUSEBUTTONDOWN:
            dinge = newdinge(qty_dinge)  
    
    fenster.fill((255,255,0))
    for i,g in enumerate(groups):
        if len(g)> 1:
            #pg.draw.lines(fenster,group_color[i],True,g,5)
            cx, cy = groupcenter(g)
            pg.draw.circle(fenster,group_color[i],(cx,cy),10)
            circle_points = encircle(g,cx,cy,50)
            pg.draw.circle(fenster,(0,255,0),(cx,cy),radius,2)
            for i in circle_points:
                pg.draw.circle(fenster,(0,0,0),i,3)

    for ding in dinge:
        pg.draw.circle(fenster,(0,0,255),ding,5)
    bar_y = int(h*0.75)
    pg.draw.line(fenster,(0,0,0),(0,bar_y),(w,bar_y), 5)
    for i in range(pos_width,w,pos_width):
        pg.draw.line(fenster,(0,0,0),(i,bar_y),(i,h),5)
    newnumb = group_pow(qty_dinge,base)
    #print("nn",newnumb)
    dot_radius = 5
    newnumb.reverse()
    for exp,dots in enumerate(newnumb):
        x, y = pos_width*exp+50, h- 4*dot_radius
        for j in range(dots):
            pg.draw.circle(fenster,(255,0,0),(x , y),dot_radius)
            x += dot_radius* 4
        y = h - i * dot_radius * 4
        #x = exp * pos_width
        
        
    
    pg.display.flip()

pg.quit()

