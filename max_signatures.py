import pandas as pd

filename = input("Please enter a file name: ")

data = pd.read_csv(filename, low_memory=False, encoding="ISO-8859-1")

# find max number of signatures on a petition
index = data['signatureCount'].idxmax()
signature_count = data.loc[index, 'signatureCount']
title = data.loc[index, 'title']
body = data.loc[index, 'body']
print('\nThe petition with the most signatures has %s signatures. The title is \"%s\" and the text is as follows:\n\n%s\n' % (signature_count, title, body))