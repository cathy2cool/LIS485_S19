import json


with open('all_articles.json') as jsonfile:
    parsed = json.load(jsonfile)

print (json.dumps(parsed, indent=2, ))

# this file makes the json file more readable for to a human 
