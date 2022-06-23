a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
out=b[a[1] : None]+ b[None : a[1]]
print(*out)