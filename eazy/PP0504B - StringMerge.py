
def string_merge(a,b):
    text=""
    if len(a)<len(b):
        for x in range(len(a)):
            text = text+a[x]+b[x]
    else:
        for x in range(len(b)):
            text = text+a[x]+b[x]
    return text


n = int(input())


for z in range(n):
    a=[x for x in input().split()]
    print (string_merge(a[0],a[1]))
    
