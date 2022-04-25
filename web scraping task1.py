#  webscraping.
# task 1 webscraing.

import requests,json,pprint
from bs4 import BeautifulSoup

url = "https://www.imdb.com/india/top-rated-indian-movies/"
r = requests.get(url)
bh = r.content
soup = BeautifulSoup(bh,"html.parser")
def scrap_top_list():
    main_div = soup.find("div",class_="lister")
    tbody = main_div.find("tbody",class_="lister-list")
    trs = tbody.find_all("tr")
    movie_rank =[]
    movie_name =[]
    year_of_release =[]
    movie_urls = []
    movie_ratings = []
    for tr in trs:
        position = tr.find("td",class_= "titleColumn").get_text().strip()
        rank = ''
        for i in position:
            if "." not in i:
                rank = rank + i
            else:
                break
        movie_rank.append(rank)
        title = tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)

        year = tr.find("td",class_="titleColumn").span.get_text()
        year_of_release.append(year)

        imdb_rating = tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)
        
        link = tr.find("td",class_="titleColumn").a["href"]
        movie_link = "https://www.imdb.com"+link
        movie_urls.append(movie_link)
    Top_Movies = []
    details = {"name":"","year":"","rating":"","url":""}
    for i in range(0,len(movie_rank)):
        details["postion"] = int(movie_rank[i])
        details["name"] = str(movie_name[i])
        year_of_release[i] = year_of_release[i][1:5]
        details["year"] = int(year_of_release[i])
        details["rating"] = float(movie_ratings[i])
        details["url"] = movie_urls[i]
        Top_Movies.append(details)
        details = {"name":"","year":"","rating":"","url":""}
    return Top_Movies
p = (scrap_top_list())
print(p)
print("successfully run")
with open("task1.json","w") as top:
    json.dump(p,top,indent=6)
    
