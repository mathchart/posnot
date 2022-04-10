from math import sqrt
from random import randint

 


def randcol():
    return(randint(1,255),randint(1,255),randint(1,255))

def dist(a,b):
    return round(sqrt((a[0]-b[0])**2+(a[1]-b[1])**2),1)
