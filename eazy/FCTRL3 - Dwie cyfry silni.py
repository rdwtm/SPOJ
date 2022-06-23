#!/usr/bin/python3

from math import factorial


list = [ ]
n = int(input())
x=2
for z in range(n):
    list.append(int(input()))
for x in range(n):
    if list[x] <10:
        a=str(factorial(list[x]))
        if len(a)>1:
            print(int(a[-2]),int(a[-1]) )
        else:
            print(0,int(a[-1]) )

    else:
        print(0,0)