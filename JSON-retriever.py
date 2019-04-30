# Simone and Brandon
# This file uses the NewsAPI to find articles including the search terms 'facebook' and 'privacy' and outputs a JSON file

from newsapi import NewsApiClient
import json 

# Init
newsapi = NewsApiClient(api_key='745cf0c9a8cb471a89aafa1f24a27f8a')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='trump',language='en',country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='facebook AND privacy',domains='wired.com,techcrunch.com,cnn.com,nytimes.com,foxnews.com',from_param='2019-04-01',to='2019-04-30',language='en',sort_by='relevancy',page=1)
data = all_articles["articles"]
with open('data.json', 'w') as outfile: 
    json.dump(data, outfile)
