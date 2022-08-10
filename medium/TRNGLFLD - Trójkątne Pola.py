
# pobranie wartości wejść
for i in range(int(input())):
    Num_tip=int(input())
    # jeśli jeden trójkąt to nie trzeba sprawdzać
    if Num_tip==3:
        for j in range(Num_tip):
           input()
        print('1 2 3')
    else:
        x=[]
        y=[]
        for j in range(Num_tip):
            tip=([int(x) for x in input().split()])
            x.append(tip[0])
            y.append(tip[1])
        for k in range(int(Num_tip/3)):
            tips=[]
            tips.append(x.index(min(z for z in x if z is not None)))
            tips.append(x.index(max(z for z in x if z is not None)))
            tips.append(y.index(min(z for z in y if z is not None)))
            if tips[2] == tips[0] or tips[2] == tips[1]:
                tips[2] = y.index(max(z for z in y if z is not None))   
            tips.sort()
            for tip in tips:
                x[tip]=None
                y[tip]=None
            for ind in range(len(tips)):
                tips[ind]=int(tips[ind])+1
            print(*tips)
        print("")




