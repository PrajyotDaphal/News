import requests
from Listen import Listen
from Speak import Say

apikey = "***PAST YOUR API KEY***"

def business():
      mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=business&apikey=" + str(apikey)
      news = requests.get(mainurl).json()
      article = news['articles']
      newsarticle = []
      for arti in article:
        newsarticle.append(arti['title'])   

      for i in range(10):
        Say(newsarticle[i]) 

def science():
      mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=science&apikey=" + str(apikey)
      news = requests.get(mainurl).json()
      article = news['articles']
      newsarticle = []
      for arti in article:
        newsarticle.append(arti['title'])

      for i in range(10):
        Say(newsarticle[i])        

def entertainment():
      mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apikey=" + str(apikey)
      news = requests.get(mainurl).json()
      article = news['articles']
      newsarticle = []
      for arti in article:
        newsarticle.append(arti['title'])

      for i in range(10):
        Say(newsarticle[i]) 

def sports():
      mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apikey=" + str(apikey)
      news = requests.get(mainurl).json()
      article = news['articles']
      newsarticle = []
      for arti in article:
        newsarticle.append(arti['title'])

      for i in range(10):
        Say(newsarticle[i])  

def health():
      mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=health&apikey=" + str(apikey)
      news = requests.get(mainurl).json()
      article = news['articles']
      newsarticle = []
      for arti in article:
        newsarticle.append(arti['title'])

      for i in range(10):
        Say(newsarticle[i])

def technology():
      mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apikey=" + str(apikey)
      news = requests.get(mainurl).json()
      article = news['articles']
      newsarticle = []
      for arti in article:
        newsarticle.append(arti['title'])

      for i in range(10):
        Say(newsarticle[i])

while True:
   try:

    branch = Listen()

    if "business" in branch:
     business()
     Say("wan another news")
     

    elif "science" in branch:
     science()
     Say("wan another news")

    elif "technology" in branch:
      technology()
      Say("wan another news")

    elif "entertainment" in branch:
     entertainment() 
     Say("wan another news")

    elif "sports" in branch:
     sports()
     Say("wan another news")

    else:
       Say("Unknown Category")
       break

   except:
    Say("Unknown Category")
    continue                               
