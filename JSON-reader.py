# Simone and Brandon
# This file reads a JSON file called data.json and finds the titles of articles including the search terms 'facebook' and 'privacy'

import json
# keys: source, author, title, description, url, urlToImage, publishedAt, content

with open('data.json') as jsonfile:
    parsed = json.load(jsonfile)
for item in parsed:
    print(item['title'],'\n')
