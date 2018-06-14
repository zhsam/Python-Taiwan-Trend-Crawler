from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import datetime as dt

# Part 1 - Crawl Hot Video infos from YouTube
response = requests.get('https://movies.yahoo.com.tw/chart.html')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Part 2 - Get movies ranking
movie_name = []

# Get movie for #1
top = soup.find_all(attrs={"class": "rank_list_box"})[0].find_all("h1")[0].get_text()
movie_name.append(top)

# Get movie for #2~20
for link in soup.find_all(attrs={"class": "rank_txt"}):
    movie_name.append(link.get_text())

# Part 3 - Get short videos
# get short video link
link = []
for i in soup.find_all(attrs={"class": "icon_notice"}):
    if i.find_all("a"):
        # print(i.find_all("a")[0].get("href"))
        link.append(i.find_all("a")[0].get("href"))
    else:
        # print("null")
        link.append("null")

# Part 4 - Get scores for each video
score = []
for k in soup.find_all(attrs={"class": "starwithnum"}):
    if k.find_all("h6"):
        score.append(k.find_all("h6")[0].get_text())
    else:
        score.append("null")

# movies
header = ['movie_name']
df = pd.DataFrame(movie_name, columns=header)
df["link"] = link
df["score"] = score

# Part 5 - Get the right file name and Export
# df.to_csv('yt.csv',index=False)
file_name = str(dt.date.today()) + '-YahooMovies.xlsx'
df.to_excel(file_name,index=False)
