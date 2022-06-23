

while True:
    try:
        a=input()
        N_a=''
        for char in a:
            if char=='<':
                st=True
            elif char=='>':
                st=False
            if st==True:
                N_char=char.capitalize()
                N_a+=N_char
            else:
                N_a+=char
        print(N_a)



    except Exception as e:
        exit()





# import re
# while True:
#     try:
#         c=[]
#         d=[]
#         a=input()
#         b = re.split('>', a)
#         for l in b:
#             if l!='':
#                 if l[0]=='<':
#                     c.append(l.upper()+'>')
#                 else:
#                     c.append(l)
#         b = [re.split('<', x) for x in c]
#         for l in b:
#             if l!='':
#                 if l[-1]=='<':
#                     d.append('<'+l.upper())
#                 else:
#                     d.append(l)

#         #c = [l.upper()+'>'  if l[0]=='<' else l for l in b]        
#         print(*d)
#     except Exception as e:
#         print(e)
#         exit()


# #         import re
# # while True:
# #     try:
# #         a=input()
# #         b = re.split('|>', a)
# #         c = [l.upper()+'>'  if l[0]=='<' else l for l in b]
# #         print(c)
# #     except Exception as e:
# #         print(e)
# #         exit()