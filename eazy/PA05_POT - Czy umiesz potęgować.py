#!/usr/bin/python3



list = [ ]
n = int(input())
x=2
for z in range(n):
    a=[int(x) for x in input().split()]
    list.append(a)
for x in range(n):
    if list[x][1] == 0:
        print (1)
    else:

        arg = int(list[x][1]%4)
        if arg == 0:
            a = str(list[x][0]**4)
            print (int(a[-1]))
        elif arg == 1:
            a = str(list[x][0])
            print (int(a[-1]))
        elif arg == 2:
            a = str(list[x][0]**2)
            print (int(a[-1]))
        elif arg == 3:
            a = str(list[x][0]**3)
            print (int(a[-1]))
        # match arg:
        #     case 0:
        #         a = str(list[x][0]**4)
        #         print (int(a[-1]))

        #     case 1:
        #         a = str(list[x][0])
        #         print (int(a[-1]))

        #     case 2:
        #         a = str(list[x][0]**2)
        #         print (int(a[-1]))

        #     case 3:
        #         a = str(list[x][0]**3)
        #         print (int(a[-1]))

