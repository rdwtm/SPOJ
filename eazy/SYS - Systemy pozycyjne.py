def konw(x, y):
    tab="0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J"
    t=tab.split()
    c=[]
    b=''
    while x/y>0:
        c.append(t[x%y])
        x=x//y
    for v in reversed(c):
        b+=str(v)
    return b

i=int(input())
for z in range(i):
    a=int(input())
    text = konw(a,16)+' '+konw(a,11)
    print(text)