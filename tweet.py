#Dani Emily David
#This checks for tweeters with more than 1000 followers
import pandas as pd
data = pd.read_csv("pb1uniquetweets.csv", low_memory = False, encoding="ISO-8859-1")
status = data[data.followers_count > 1000]
print("Tweeters with more than 1000 followers: {0}".format(
    len(status)))
