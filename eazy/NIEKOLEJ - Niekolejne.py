
i=int(input())
tab=[]
if i<=2:
    print("NIE")
elif i==3:
    print(1, 3, 0, 2)
else:
    while i!=-1:
        tab.append(i)
        i-=1
    out=tab[0 : None : 2]+tab[1 : None : 2]
    print(*out)
    
