import pandas as pd
df = pd.read_csv('pb1uniquetweets.csv',
                     low_memory=False,
                     encoding="ISO-8859-1",
                     header=0
                     )

df['Title'] = df['Title'].str.replace('http\S+|www.\S+', '', case=False) 

df['Text'] = df['Text'].str.replace('http\S+|www.\S+', '', case=False)

df.to_csv('new_tweets1.csv')

print(df)
