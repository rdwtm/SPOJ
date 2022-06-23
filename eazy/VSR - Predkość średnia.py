i=int(input())
for z in range(i):
    a=[None]*2
    a=[int(x) for x in input().split()]
    v_sr = (2*a[0]*a[1])/sum(a)
    print(int(v_sr))