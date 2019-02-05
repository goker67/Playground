#Goker Guner
import math
num=int(input("Bir sayi girin:"))

def isprime(num):
    count=0
    if num<0:
        print("{} sayısı negatiftir".format(num))
        return 0
    elif num == 1:
        print("1 sayısı asal veya değildir denemez.")
        return 0
    for i in range(2,math.floor(math.sqrt(num))+1):

        if num%i == 0:
            count+=1
            break

    if(count!=0):
        print("{} sayısı asal değildir".format(num))
    else:
        print("{} sayısı asaldır".format(num))
    return 0

isprime(num)

"""
import argparse konut satırından değer girmek için kulllanılır.
arguments=sys.argv liste olarak döner.
"""
