#!/usr/bin/python3
i=int(input())
b="0"
for z in range(i):
    a=int(input())
    while a!=int(b):
        a=a+int(b)
        b=""
        c = 0
        for x in reversed(str(a)):
            b+=str(x)
            c+=1
    print (b,c)
    b=0   
