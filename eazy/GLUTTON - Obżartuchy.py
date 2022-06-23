import math

n = int(input())
l_sek=24*60*60

for z in range(n):
    a=[x for x in input().split()]
    list=[]
    for c in range(int(a[0])):
        l=(int(input()))
        cnt_cookies=l_sek/l
        list.append(int(cnt_cookies)/int(a[1]))
    boxes=sum(list)
    print(math.ceil(boxes))

        