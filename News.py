import requests
import json
from Extention.Speak import speak

def get_urls():
    with open('## Contents.json File Location ##', 'r') as file:
        return json.load(file)

def News(category):
    urls = get_urls()
    if category in urls.get('news_URL', {}):
        url = urls['news_URL'][category]
        response = requests.get(url)
        
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get('articles', [])
            
            for i in range(min(10, len(articles))):
                article = articles[i]
                speak("Title:", article.get('title', 'N/A'))
                speak("Description:", article.get('description', 'N/A'))
                print()
        else:
            speak(f"Failed to fetch news. Status Code: {response.status_code}")
    else:
        speak("Invalid news category")

def extract_category(command):
    category_keywords = ['jarvis news on', 'news in']
    for keyword in category_keywords:
        if keyword in command:
            return command.split(keyword, 1)[-1].strip()
    return None


    while True:
    # if 1:
     query = Listen().lower()    

     if "news" in query:
          category = extract_category(query)
          if category:
           News(category)
          else:
              speak("Sorry, I couldn't determine the news category.")
