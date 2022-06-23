n = int(input())


for z in range(n):
    a=[int(x) for x in input().split()]
    nap=""
    for c in reversed(a[1:len(a)]):
        nap=nap+str(c)+" "
    print(nap)