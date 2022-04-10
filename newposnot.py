""" Visual simulation of positional notation """
__author__ = "Joe Speier"
__email__ = "jspeier@xycharts.com"
__creation__ = 'Created 202204'
__maintainer__ = 'jds'
__status__ = '2'



import pygame as pg
import sys
from random import randint
from math import sqrt, cos, sin, radians, log, ceil
from myfuncs import *

"""Functions for here"""
def newdinge(n):
    dinge = []
    for i in range(n):
        x = randint(radius,w - radius)
        y = randint(radius,int(h*.75)-radius)
        dinge.append(Ding(x,y,randcol(),radius,0,0))
    return dinge



"""The class of things"""
class Ding():
    def __init__(self,x,y,col,radius,dx=0,dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.col = col
        self.radius = radius
        self.dist = 0

    def __str__(self):
       msg = f"({self.x},{self.y}) {self.col} {self.radius}"       
       return msg

    def distbetween(self,other):
        other.dist = round(sqrt((self.x-other.x)**2+(self.y - other.y)**2),1)
        return other.dist



"""Store distance from top thing"""
def distfrom1(dinge):
    dinged = []
    for ding in dinge:
       d = dist((ding.x,ding.y),(dinge[0].x,dinge[0].y))
       #d = dinge[0].distbetween(ding)
       dinged.append(((ding),d))
    dinge_sorted = sorted(dinged,key=lambda x: x[1])
    return dinge_sorted

"""Select and hold a base worth of closest items"""
def grouptop(dinge_sorted,base):
    hold = []
    for g in range(base):
        hold.append(dinge_sorted[g][0])
    groups.append(hold)
    group_color.append(randcol())
    del dinge_sorted[0:base]
    return groups,dinge_sorted


"""Initialization for display screen"""
pg.init()
w, h = 1200,1000
big_screen = pg.display.set_mode((w,h))
big_screen.fill((255,255,0))
pg.display.set_caption('Grouping Precedes Positional Notation')
clock = pg.time.Clock()
FPS = 40

"""Initialization for quantity to meaningful number"""
base = 7  #must be >= 2
qty_dinge = 78
dinge_dist = []
groups = []
group_color = []
circle_points = []
newnumb = []
radius = 15
group_circle_radius = 50
dinge = newdinge(qty_dinge)

"""Number position framework parameters"""
frame_scr_h = int(h * .25)
frame_scr = pg.Surface((w,frame_scr_h))
frame_scr.fill((255,255,0))
lw = 10
top_line = int(h*.75)
max_exp = ceil(log(qty_dinge,base))
cell_width = w // max_exp
pg.draw.line(frame_scr,(0,0,0),(0,0),(w,0), lw)
for i in range(cell_width,w-lw,cell_width):
    pg.draw.line(frame_scr,(0,0,0),(i,0),(i,frame_scr_h),lw)

"""Power of base position titles"""
font = pg.font.SysFont('miriam', 36)
for i in range(max_exp,-1,-1):
    if i == 2:
         base_pow_text = f'{base}\u00b2'
    elif i == 1:
        base_pow_text = f'{base}^1'
    elif i == 0:
        base_pow_text = f'{base}\u00b0'
    else:
        base_pow_text = str(base)+"^"+str(i)
        base_pow_text = f'{base}^{i}'

    pos_value = font.render(base_pow_text,1,(0,0,255))
    frame_scr.blit(pos_value,(cell_width//2 +cell_width*(max_exp - i - 1),10))


"""Power of base's orderly representation of things"""
pow_scr = pg.Surface((300,500))
pow_scr.fill((255,255,0))
small_thing_radius = 8
for i in range(base): 
    for j in range(base):
        pg.draw.circle(pow_scr,(255,0,0),(j*32+cell_width//4,(i+1)*20),small_thing_radius)
#frame_scr.blit(pow_scr,(0,frame_scr_h - base*20-15))

""" Collect the groups by nearness"""
# dinge_dist = 


"""Animation Loop"""
while True:
    clock.tick(FPS)
    for ev in pg.event.get():
        if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and pg.K_ESCAPE): 
            pg.display.quit()       
            sys.exit()
    for ding in dinge:
        pg.draw.circle(big_screen,ding.col,(ding.x,ding.y),ding.radius)
    big_screen.blit(frame_scr,(0,top_line))
    pg.display.flip()
