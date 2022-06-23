import math
pi=3.141592654

a=[int(x) for x in input().split()]
r=math.sqrt(a[0]**2-(a[1]/2)**2) # a[0]->r, a[1]->d
print(pi*r**2)
