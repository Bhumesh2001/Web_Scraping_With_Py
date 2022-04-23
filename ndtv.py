
# import requests,json,pprint
# from bs4 import BeautifulSoup

# url = "https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation"
# res = requests.get(url)
# r = res.content
# soup = BeautifulSoup(r,"html.parser")

# def scrap_data():
#     d = {}
#     m = []
#     nd = soup.find("div",class_="lisingNews")
#     bh = nd.find_all("div",class_="news_Itm-cont")
#     for j in bh:
#         gh = j.find("h2",class_="newsHdng").get_text()
#         n = j.find("p",class_="newsCont").get_text()
#         d.update({"title":gh,"content":n})
#         m.append(d)
#         print(m)
#         with open("ndtv.json","w") as nm:
#             json.dump(m,nm,indent=6)
# (scrap_data())
