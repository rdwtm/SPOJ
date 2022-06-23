a=[float(x) for x in input().split()]
if a[0]==0.00 and a[2]-a[1]==0:
    print('NWR')
elif a[0]==0.00 :
    print('BR')
else:
    print(round((a[2]-a[1])/a[0],2))