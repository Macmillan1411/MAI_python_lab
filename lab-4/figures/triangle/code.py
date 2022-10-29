from math import sqrt

def_a = 7 
def_b = 2 
def_c = 8
def triangle_perimeter(a = def_a,b = def_b,c = def_c):
    return a + b + c

def triangle_area(a = def_a, b = def_b, c = def_c):
    s = (a + b + c) / 2
    return sqrt((s * (s - a)*(s - b) * (s - c)))

