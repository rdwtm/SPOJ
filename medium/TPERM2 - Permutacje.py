from itertools import permutations
import string


for a in range(int(input())) :
    letters=string.ascii_lowercase[0:int(input())]
    perm = permutations(letters)
    for i in list(perm):
        print (*i)