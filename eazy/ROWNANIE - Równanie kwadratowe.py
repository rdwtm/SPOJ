while True:
    try:
        b=input()
        a=b.split()
        delta=(float(a[1])*float(a[1]))-(4*float(a[0])*float(a[2]))
        if delta>0:
            print(2)
        elif delta==0:
            print(1)
        elif delta<0:
            print(0)
    except Exception as e: 
        exit()
    
# while True:
#         b=input()
#         a=b.split()
#         print(a)
#         delt=int(a[2])*int(a[2])-4*int(a[0])*int(a[2])
#         if delt>0:
#             print(2)
#         elif delt==0:
#             print(1)
#         elif delt<0:
#             print(0)
   