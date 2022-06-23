
class Stack:

    def __init__(self,size):
        self.items = []
        self.size=size

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  # nigdy nie jest pełny
        return self.size==len(self.items)

    def push(self, item):
        self.items.append(item)         # dodajemy na koniec

    def pop(self):                      # zwraca element
        return self.items.pop()         # zabieram od końca
stos=Stack(10)
a=0
while True:
    try:
        a=(input())
        if a=="+" and not Stack.is_full(stos):
            Stack.push(stos,input())
            print(":)")
        elif a=="-"and not Stack.is_empty(stos):
            print(Stack.pop(stos))
        elif Stack.is_full(stos): 
            a=(input())
            print(":(")
            
        elif Stack.is_empty(stos):
            print(":(")

        


    except Exception as e: 
        print(e)

        exit()
    