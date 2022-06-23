from numpy import sort
i=int(input())
for z in range(i):
    j=int(input())
    out=[]
    a=[x for x in input().split()]
    First=max(a)
    pos_first=[i for i,x in enumerate(a) if x==First]
    a_sort=[int(x) for x in sort(a)]
    for el in pos_first:
        out.append(int(a[el]))
    out+=a_sort[0 : (j-len(pos_first))]
    print(*out)
        
    