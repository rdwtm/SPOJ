while True:
    out=''
    b=['']
    try:
        a=[x for x in input().split()]
        b[0]=a[0]
        for x in a[1:None]:
            b.append(x.capitalize())
        for l in b:
            out+=l
        print(out)
    except Exception as e:
        exit()