for i in range(int(input())):
    order=[]
    time=0
    Num_files=int(input())
    files_size=([int(x) for x in input().split()])
    smallest=min(files_size)
    N_files_size=files_size[:]
    for i in range(Num_files):
        smallest_ind = N_files_size.index(min(N_files_size))
        x = N_files_size.pop(smallest_ind)
        time=time+x
        order.append(files_size.index(x)+1)
    print(time)
    for i in range(1,Num_files):
        print(smallest, order[i])
