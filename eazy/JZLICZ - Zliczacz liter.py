from curses.ascii import isupper, islower
from typing import Counter
lista=[]

for z in range(int(input())):
  lista+=list(input())
x=Counter(lista)
y = sorted(x)
sort = [l for l in y if islower(l)] + [l for l in y if isupper(l)]
for letter in sort:
  print(letter, x[letter])
