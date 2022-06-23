n = int(input())

for z in range(n):
     a=[x for x in input().split()]
     a=a[1:len(a)]
     new_a=[]
     text=""
     for cnt in reversed(range(len(a))):
         if cnt==0:
             text=text+a[0]
         else:
             text=text+a[len(a)-cnt]+' '
     print(text)

     