i=int(input())
for z in range(i):
    list = []
    a=[int(x) for x in input().split()]
    list = a[2 : : 2] + a[1 : : 2]
    print(*list)
