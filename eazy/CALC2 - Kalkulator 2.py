tab=[None] * 10
while True:
    try:
        b=input()
        a=b.split()
        if a[0]=='z':
            tab[int(a[1])]=a[2]
        else:
            print(int(eval(tab[int(a[1])]+a[0]+tab[int(a[2])]))) # uzycie eval jest skrajnie niebezpieczne, gdyz urzytkownik moze wpisac niebezpieczny kod
    except Exception as e: 
        print(e)
        exit()