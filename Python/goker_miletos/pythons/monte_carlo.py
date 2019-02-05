#Goker Guner
import random
from math import *
import time

power=int(input("power:"))
rep=int(input("repetition:"))

def mc(power,rep):
    r=5
    number_of_samples=10**power
    final = 0

    for i in range(rep):
        circle_point=0
        square_point=0

        for i in range(number_of_samples):
            x=random.uniform(0,10)
            y=random.uniform(0,10)
            new_x=abs(x-5)
            new_y=abs(y-5)

            if sqrt((new_x**2)+(new_y**2))<=5:
                circle_point+=1
            else:
                square_point+=1
        final += circle_point / (circle_point+square_point)*4

    return final/rep
start=time.time()
print(mc(power,rep))
stop=time.time()-start
print(stop)
