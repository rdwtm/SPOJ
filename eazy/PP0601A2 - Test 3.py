try:
    a=0
    b=0
    arg=0
    c=input()
    if (a!=b or b!=c) and b=='42':
        arg+=1  
    b=a
    print(b)
    if arg==3:
        exit 
except:
    exit  
