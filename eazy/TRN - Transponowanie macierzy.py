#!/usr/bin/python3.8
import numpy as np 
i=[int(x) for x in input().split()]
b=np.zeros((i[0],i[1]),int)

for z in range(i[0]):
    b[z]=[int(x) for x in input().split()]
print(*[str(row)[1:-1] for row in (np.transpose(b))], sep='\n')

