i=int(input())
for z in range(i):
    list = []
    a=[int(x) for x in input().split()]
    sr=sum(a[1::])/a[0]
    b=[abs(x-sr) for x in a[1::]]
    ind=b.index(min(b))
    print(a[ind+1])
