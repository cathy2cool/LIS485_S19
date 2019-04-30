from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='352d121a08fd4f9d991291ef97a5b857')

# /v2/top-headlines
#top_headlines = newsapi.get_top_headlines(q='strawberries',
                                          #sources='fox-news',
                                          #category='technology',
                                          #language='en',
                                          #country='us')

# /v2/everything
#all_articles = newsapi.get_everything(q='japan',
                                      #sources='fox-news',
                                      #domains='fox.com',
                                      #from_param='2019-04-01',
                                      #to='2019-04-30',
                                      #language='en',
                                      #sort_by='relevancy',
                                      #page=2)

# /v2/sources
#sources = newsapi.get_sources()

import json 
with open('japan_data.json', 'r') as outfile:
    
    parsed = json.load(outfile)

    new_jppython = json.dumps(parsed,indent=2, sort_keys=True, separators=(". ", "="))

    authors = new_jppython.find("author")
    
    for item in parsed:
            author_names = item["author"]
        

print("Number of authors: ", authors)
print("List of authors: ", author_names) 



    
    

