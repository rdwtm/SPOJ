#!/usr/bin/python3

def nwd(a, b): return nwd(b, a%b) if b else a
def nww(a, b): return a*b//nwd(a, b)

list = [ ]
n = int(input())

for z in range(n):
    a=[int(x) for x in input().split()]
    print(nww(a[0],a[1]))



