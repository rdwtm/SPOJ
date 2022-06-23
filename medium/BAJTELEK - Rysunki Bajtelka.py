#wzor gaussa
bl_eff=10
gr_eff=6
for i in range(int(input())):
    bl=[int(x) for x in input().split()]
    gr=[int(x) for x in input().split()]
    P_bl=sum([bl[j*2]*(bl[j*2+3]-bl[j*2-3]) for j in range(len(bl)/2)])
    P_gr=sum([gr[j*2]*(gr[j*2+3]-gr[j*2-3]) for j in range(len(gr))])-P_bl
    print(P_bl*bl_eff+P_gr*gr_eff)
