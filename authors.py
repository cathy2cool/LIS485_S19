#This will create an output listing by the key, in this case it is by the key 'author'
import json
with open('data.json') as jsonfile:
    parsed = json.load(jsonfile)
# print(type(parsed))
for item in parsed:
# articles = parsed['articles'][0]
    print(item["author"])
# for item in articles.items():
#     print(item['author'])

# # print (json.dumps(parsed, indent=2, sort_keys=True))
