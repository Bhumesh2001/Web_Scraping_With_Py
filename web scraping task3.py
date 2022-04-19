# task 3 webscraping.

# import json
# from pprint import pprint

# with open("imdb2.1.json","r") as p:
#     d=json.load(p)
#     pprint(d)
# def group_by_decade():
#     k={}
#     l=[]
#     b=sorted([x for x in d])
#     g=str(b[0])
#     h=g[0:3]+"0"
#     x=int(h)
#     for z in d:
#         if x<=int(b[-1]):
#             for i in range(x,x+10):
#                 if str(i) in d:
#                     for z in d[str(i)]:
#                         print(z)
#                         l.append(z)
#             k[x]=l
#             l=[]
#             x+=10
#     return k
# p=group_by_decade()
# with open("task3.json","w") as m:
#     json.dump(p,m,indent=4)

