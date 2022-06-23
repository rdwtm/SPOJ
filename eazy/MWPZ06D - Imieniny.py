i=int(input())
for z in range(i):
    a=[int(x) for x in input().split()]
    if (a[0]-1)<=a[1] and a[1]%(a[0]-1)==0:
        print("NIE")
    else:
        print("TAK")