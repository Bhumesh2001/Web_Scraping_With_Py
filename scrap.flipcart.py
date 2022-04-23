
# import json,requests,pprint
# from bs4 import BeautifulSoup

# url = "https://www.flipkart.com/search?q=camera&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_3_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_3_na_na_na&as-pos=3&as-type=RECENT&suggestionId=camera&requestId=7ba619eb-aeda-4c10-9a25-8ff909bc233a&as-searchtext=cam"
# url1 = requests.get(url)
# content1 = url1.content
# soup = BeautifulSoup(content1,"html.parser")

# def flipkart_data():
#     dict = {}
#     l2 = []
#     div = soup.find("div",class_="_1YokD2 _3Mn1Gg")
#     div1 = div.find_all("div",class_="_1AtVbE col-12-12")
#     count = 0
#     for j in div1:
#         count += 1
#         div1 = j.find("div",class_="col col-7-12")
#         te = div1.find("div",class_="_4rR01T").get_text()
#         dict["camera_name"]=te

#         cl = j.find("div",class_="col col-5-12 nlI3QM")
#         bh = cl.find("div",class_="_25b18c")
#         di = bh.find("div",class_="_30jeq3 _1_WHN1").get_text()
#         dict["camera_price"]=di

#         img = j.find("div",class_="MIXNux").div.img["src"]
#         dict["image_url"]=img

#         details=j.find("ul",class_="_1xgFaf")
#         if details:
#             l1=[]
#             for i in details:
#                 pr = (i.text)
#                 l1.append(pr)
#             dict["details"]=l1
#         data = (dict)
#         l2.append(dict.copy())
#         if count == 24:
#             break
#     with open("flipkart.json","w") as obj:
#         json.dump(l2,obj,indent=4)
# flipkart_data()



# def pattern(number):
#     if number == 0:
#         return 1
#     else:
#         pattern(number-1)
#         print(number,end=" ")
# number = int(input("enter your range: "))
# for j in range(number+1):
#     print()
#     pattern(j)