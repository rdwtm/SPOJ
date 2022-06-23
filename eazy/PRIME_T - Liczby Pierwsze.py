import math 
list = [ ]
n = int(input())



def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

for z in range(n):
    if czy_pierwsza(int(input())):
        print("TAK")
    else:
        print("NIE")










        # def prime(a):
#     r = math.sqrt(a)
#     i = 2
#     while (i<=r):
#         if((a%i)!=0):
#             i+=1
#         else:
#             return 0    
#     return 1


# for z in range(n):
#     arg = prime(int(input()))
#     if arg==1:
#             print("NIE")
#     else:
#         if arg:
#             print("TAK")
#         else:
#             print("NIE")