def fun(a):
    return a/2 if a%2==0  else (3*a)+1

n = int(input())

for z in range(n):
    x=int(input())
    cnt=0
    while x!=1:
        cnt+=1
        x=fun(x)
    print(cnt)