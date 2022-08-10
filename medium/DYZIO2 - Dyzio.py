#sito Eratostenesa

for i in range(int(input())):
    Num=([int(x) for x in input().split()])
    n = Num[1]
    if n < 2:
        print(0)
    else:
        skr = [False] * (n + 1)
        i = 2
        while i * i <= n:
            if  not skr[i]:
                j = i * i            
                while j <= n:
                    j += i
            i += 1
        cnt=0
        for i in range(Num[0], n+1):
            if not skr[i]:
                cnt+=1
        print(cnt)