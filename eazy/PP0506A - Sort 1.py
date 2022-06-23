import math

n = int(input())


for z in range(n):
    m = int(input())
    list1=[]
    list2={}
    for c in range(m+1):
        a=[x for x in input().split()]
        if c!=m:
            list1.append(a)
            list2[a[0]]=math.sqrt(abs(int(a[1]))+abs(int(a[2])))
    sorted_dict = dict( sorted(list2.items(),
                           key=lambda item: item[1],
                           reverse=False))
    sorted_list=[] 
    for key in sorted_dict:
        sorted_list.append([x for x in list1 if key in x][0])
    text=""
    for col in sorted_list:
        for el in col:
            text=text+el+" "
    print(text)
    if z !=n-1:
        print("\n")



