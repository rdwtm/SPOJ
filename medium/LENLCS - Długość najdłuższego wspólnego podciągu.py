


for i in range(int(input())):
    len1 = input()
    word1 = input()
    len2 = input()
    word2 = input()
    count=0
    for lett in word2:
        if word1.find(lett)!=-1:
            count+=1
            word1 = word1.replace(lett,"",1)
    print(count)
            

 