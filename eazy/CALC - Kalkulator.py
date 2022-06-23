while True:
    try:
        b=input()
        a=b.split()
        print(int(eval(a[1]+a[0]+a[2]))) # uzycie eval jest skrajnie niebezpieczne, gdyz urzytkownik moze wpisac niebezpieczny kod
    except Exception as e: 
        print(e)
        exit()