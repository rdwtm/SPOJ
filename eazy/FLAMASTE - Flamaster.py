#!/usr/bin/python3

list = [ ]
n = int(input())

for z in range(n):
    list.append(input()+" ")
for x in list:
    out=""
    arg =""
    cnt=1
    for c in range(len(x)):
        if x[c]==arg:
            cnt+=1
        elif cnt> 2:
            out=out+arg+str(cnt)
            cnt=1
        else:
            out=out+(arg * cnt)
            cnt=1

        arg=x[c]
        if c==(len(x)-1) and cnt> 2:
            out=out+str(cnt)


    print(out)
      



