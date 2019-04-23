def nulls():
  import csv
  import pandas as pd

  frame = pd.read_csv("pb1uniquetweets.csv")
  original = len(frame.location)
  frame.dropna(inplace=True)
  new = len(frame.location)

  print("The total number of empty fields in location is:", original - new)





  #locs = frame[frame.location]
  #frame['num_nulls'] = locs.isnull().sum(axis=1)
  #print("{0}".format(len(locs)))
  #with open ("pb1uniquetweets.csv") as csv_file:
      #csv_reader = csv.reader(csv_file,delimiter=",")
