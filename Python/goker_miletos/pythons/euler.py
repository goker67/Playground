#Goker Guners
from math import *

def f(y,t):
    return y + t

def f2(y,t):
    if t == 0:
        t += 10e-9
    return sin(t)-(y/t)

def Euler(f,t0,y0,n,tf):


    for i in range(n):
        h = (tf - t0)/n
        y1 = y0 + h*f(y0,t0)
        t1 = t0 + h

        t0=t1
        y0=y1


    return y0

print(Euler(f,0,0,10,10))
analytic=exp(10)-10-1
print(analytic)
relative=abs(Euler(f,0,0,10,10)-analytic)/analytic
print(relative)
print(Euler(f2,0,0,10,10))
analytic2=(sin(10)/10)-cos(10)
print(analytic2)
relative2 = abs(Euler(f2,0,0,10,10)-analytic2)/analytic2
print(relative2)
