#wzor gaussa
from re import I


bl_eff=10
gr_eff=6
for i in range(int(input())):
    bl=[int(x) for x in input().split()]
    if not bl:
        bl=[int(x) for x in input().split()]

    bl_x=bl[0:None:2]
    bl_y=bl[1:None:2]
    bl_y.append(bl_y[0])
    gr=[int(x) for x in input().split()]
    gr_x=gr[0:None:2]
    gr_y=gr[1:None:2]
    gr_y.append(gr_y[0])
    P_bl=sum([bl_x[j]*(bl_y[j+1]-bl_y[j-1]) for j in range(int(len(bl_x)))])/2
    P_gr=(sum([gr_x[j]*(gr_y[j+1]-gr_y[j-1]) for j in range(int(len(gr_x)))])/2)-P_bl
    print(int(P_bl*bl_eff+P_gr*gr_eff))




    # P_bl=sum([bl[j*2]*(bl[j*2+3]-bl[j*2-3]) for j in range(int(len(bl)/2))])
    # P_gr=sum([gr[j*2]*(gr[j*2+3]-gr[j*2-3]) for j in range(len(gr))])-P_bl