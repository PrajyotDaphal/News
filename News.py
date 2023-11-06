import requests

def reportage():
   print("choose category")
   print("Business , Science , Technology , Health , Entertainment , Sports")
   branch = input()
   apikey = "b7c98fb3391e484eb7719186558589ff"

   if 'business' in branch:
     mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=business&apikey=" + str(apikey)
     news = requests.get(mainurl).json()
     article = news['articles']
     newsarticle = []
     for arti in article:
        newsarticle.append(arti['title'])   

     for i in range(10):
        print(newsarticle[i]) 
        print("Want another news")
        branch = input()  
     else:
      print("OK")  

   if 'science' in branch :
     mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=science&apikey=" + str(apikey)
     news = requests.get(mainurl).json()
     article = news['articles']
     newsarticle = []
     for arti in article:
        newsarticle.append(arti['title'])

     for i in range(10):
        print(newsarticle[i])
      
     else:
      print("OK")  

   if 'technology' in branch :
     mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apikey=" + str(apikey)
     news = requests.get(mainurl).json()
     article = news['articles']
     newsarticle = []
     for arti in article:
        newsarticle.append(arti['title'])

     for i in range(10):
        print(newsarticle[i]) 
        print("Want another news")
        branch = input() 

     else:
      print("OK")  

   if 'entertainment' in branch :
     mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apikey=" + str(apikey)
     news = requests.get(mainurl).json()
     article = news['articles']
     newsarticle = []
     for arti in article:
        newsarticle.append(arti['title'])

     for i in range(10):
        print(newsarticle[i]) 
        print("Want another news")
        branch = input()

     else:
      print("OK")       

   if 'health' in branch:
     mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=health&apikey=" + str(apikey)
     news = requests.get(mainurl).json()
     article = news['articles']
     newsarticle = []
     for arti in article:
        newsarticle.append(arti['title'])

     for i in range(10):
        print(newsarticle[i])
        print("Want another news")
        branch = input() 
     else:
      print("OK")        

   if 'sports' in branch :
     mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apikey=" + str(apikey)
     news = requests.get(mainurl).json()
     article = news['articles']
     newsarticle = []
     for arti in article:
        newsarticle.append(arti['title'])

     for i in range(10):
        print(newsarticle[i])     

   else:
      print("No Another Catagery News")

reportage()      

  