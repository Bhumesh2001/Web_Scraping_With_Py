# task 2 webscraping.


# type 1

# import json
# with open("task1.json","r") as im:
#     m2 = json.load(im)
# def group_by_year():
#     dict1 = {}
#     for j in m2:
#         year = j["year"]
#         movie_year = []
#         for i in range(len(m2)):
#             if year == m2[i]["year"]:
#                 movie_year.append(m2[i])
#         dict1[year] = movie_year
#     return dict1
# y = group_by_year()
# with open("task2.json","w") as mr:
#     json.dump(y,mr,indent=6)


# type2
 
# with open("task1.json","r") as rt:
#     pm = json.load(rt)
# def group_by_year(movies):
#     years = []
#     for i in movies:
#         year = i["year"]
#         if year not in years:
#             years.append(year)
#     movie_dict = {i:[]for i in years}
#     for j in movies:
#         year = j["year"]
#         for y in movie_dict:
#             if str(y) == str(year):
#                 movie_dict[y].append(j)
#     return movie_dict
# pl = (group_by_year(pm))

# with open("task2.json","w") as fh:
#     json.dump(pl,fh,indent=6)
