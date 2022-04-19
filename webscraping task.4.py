# webscraping task 4

# type 1

# import json,pprint,requests
# from bs4 import BeautifulSoup

# def scrap_movie_details(movie_url):
#     page = requests.get(movie_url)

#     soup = BeautifulSoup(page.text,"html.parser")
#     # scrap_movie_name
#     name = soup.find("h1",attrs={"data-testid":"hero-title-block__title"}).get_text()

#     # scrap movie runtime
#     runtime=soup.find("li",attrs={"data-testid":"title-techspec_runtime"}).text.strip("Runtime")
#     w=runtime.split(" ")
#     if len(w)==4:
#         runtime1=int(w[0])*60+int(w[2])
#     else:
#         runtime1=int(runtime1[0])*60
    
#     # scrap_movie gener
#     genre=soup.find("li",attrs={"data-testid":"storyline-genres"})
#     Genre=genre.find_all("a")
#     gener1=[]
#     for i in Genre:
#         l=i.text
#         gener1.append(l)

#     # scrap movie bio
#     bio=soup.find("span",attrs={"data-testid":"plot-xs_to_m"}).text

#     # scrap directer of the movie
#     d_name=[]
#     director_name=soup.find('div', class_="ipc-metadata-list-item__content-container")
#     x=director_name.find_all("li",class_="ipc-inline-list__item")
#     for i in x:
#         d_name.append(i.a.get_text()) 

#     # in this div i get country and laungauge details
#     country=soup.find("li",attrs={"data-testid":"title-details-origin"}).find("a").text
#     language=[]
#     language_name=soup.find("li",attrs={"data-testid":"title-details-languages"})
#     x=language_name.find_all("li",class_="ipc-inline-list__item")
#     for i in x:
#         language.append(i.a.get_text())
#     # scrap poster image
#     poster_image_url=soup.find("img",class_="ipc-image")["src"]

#     # create dictionary for movie details
#     movie_details_dic = {"name":"","directer":"","bio":"","runtime":"","gener":"","langauge":"","country":"",}
#     movie_details_dic["name"] = name
#     movie_details_dic["directer"] = d_name
#     movie_details_dic["bio"] = bio
#     movie_details_dic["runtime"] = runtime1
#     movie_details_dic["gener"] = gener1
#     movie_details_dic["langauge"] = language
#     movie_details_dic["country"] = country
#     movie_details_dic["poster_image-url"] = poster_image_url

#     return movie_details_dic
# p = ((scrap_movie_details("https://www.imdb.com/title/tt0066763/")))
# with open("task4.json","w") as t4:
#     json.dump(p,t4,indent=6)




# type 2

# import json,requests
# from bs4 import BeautifulSoup
# from pprint import pprint

# def scrape_movie_details(url):
#     dict1={}
#     page= requests.get(url)
#     soup=BeautifulSoup(page.text,"html.parser")
#     name=soup.find("h1", attrs={"data-testid":"hero-title-block__title"}).text
#     dict1["name"]=name
#     g=[]
#     director_name=soup.find('div', class_="ipc-metadata-list-item__content-container")
#     x=director_name.find_all("li",class_="ipc-inline-list__item")
#     for i in x:
#         g.append(i.a.get_text()) 
#     dict1["director"]=g
#     country_name=soup.find("li",attrs={"data-testid":"title-details-origin"}).find("a").text
#     dict1["country"]=country_name
#     j=[]
#     language_name=soup.find("li",attrs={"data-testid":"title-details-languages"})
#     x=language_name.find_all("li",class_="ipc-inline-list__item")
#     for i in x:
#         j.append(i.a.get_text())
#     dict1["language"]=j
#     poster_image_url=soup.find("img",class_="ipc-image")["src"]
#     dict1["poster image url"]=poster_image_url
#     bio=soup.find("span",attrs={"data-testid":"plot-xs_to_m"}).text
#     dict1["bio"]=bio
#     genre=soup.find("li",attrs={"data-testid":"storyline-genres"})
#     Genre=genre.find_all("a")
#     h=[]
#     dict1["genre"]=h
#     for i in Genre:
#         l=i.text
#         h.append(l)
#     run_time=soup.find("li",attrs={"data-testid":"title-techspec_runtime"}).text.strip("Runtime")
#     w=run_time.split(" ")
#     if len(w)==4:
#         m=int(w[0])*60+int(w[2])
#     else:
#         m=int(m[0])*60
#     dict1["runtime"]=m
#     return (dict1)

# x=scrape_movie_details("https://www.imdb.com/title/tt0986264/")
# with open("task4.json","w") as p:
#     json.dump(x,p,indent=4)