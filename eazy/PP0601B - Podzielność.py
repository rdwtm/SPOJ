i=int(input())
for z in range(i):
    a=[None]*3
    a=[int(x) for x in input().split()]
    x=a[1]
    text=''
    while (x<a[0]):
        if x%a[2]!=0:
            text+=str(x)+' '
        x+=a[1]
    print(text)