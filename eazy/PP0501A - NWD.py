
def nwd(a, b): return nwd(b, a%b) if b else a
list = [ ]
n = int(input())
x=2


for z in range(n):
    a=[int(x) for x in input().split()]
    print(nwd(a[0],a[1]))





