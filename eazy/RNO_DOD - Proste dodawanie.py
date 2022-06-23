#!/usr/bin/python3


list = [ ]
n = int(input())

for z in range(n):
    x=input()
    a=[int(x) for x in input().split()]
    print(sum(a))

    