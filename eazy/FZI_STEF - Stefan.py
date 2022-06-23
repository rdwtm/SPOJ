tab=[]
for s in range(int(input())):
    x = int(input())
    tab.append(x)
    su=sum(tab[0:len(tab)-1])
    if x<=0 and su-x>=0:
        st=tab.index(x)
ntab=tab[st+1:]
if ntab==[]:
    print(0)
else:
    for x in reversed(range(len(ntab))):
        su=sum(ntab[x:])
        if ntab[x]<=0 and su-ntab[x]>=0:
            en=x
    print(sum(ntab[:en]))
    


