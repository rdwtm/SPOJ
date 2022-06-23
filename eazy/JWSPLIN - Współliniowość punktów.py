i=int(input())
for z in range(i):
    p=[int(x) for x in input().split()]
    if p[2]==p[0]==p[4]:
        print("TAK")
    else:
        a=(p[3]-p[1])/(p[2]-p[0])
        b=p[1]-a
        if a*p[4]+b==p[5]:
            print("TAK")
        else:
            print("NIE")