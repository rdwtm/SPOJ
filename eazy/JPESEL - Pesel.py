tab=[1,3,7,9,1,3,7,9,1,3,1]
for z in range(int(input())):
    inp=list(input())
    pesel=[int(x) for x in inp]
    test=[a*b for a,b in zip(tab, pesel)]
    test=sum(test)
    if test>0 and str(test)[-1]=='0':
        print("D")
    else:
        print("N")