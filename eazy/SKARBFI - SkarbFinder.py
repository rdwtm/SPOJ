n = int(input())
list = []
for z in range(n):
    m = int(input())
    x=0
    y=0
    for c in range(m):
        a=[x for x in input().split()]
        if a[0] == '0':
            x=x+int(a[1])
        elif a[0] == '1':
            x=x-int(a[1])
        elif a[0] == '2':
            y=y+int(a[1])
        elif a[0] == '3':
            y=y-int(a[1])
    text=""
    if x>0:
        text="0 "+str(x)
    elif x<0:
        text="1 "+str(-x)
    if y>0:
        text=text+"\n2 "+str(y)
    elif y<0:
        text=text+"\n3 "+str(-y)
    elif x==0 and y==0:
        text="studnia"
    print(text)
    