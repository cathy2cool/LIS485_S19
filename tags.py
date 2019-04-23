import pandas as pd
import re
# c\(.*c\((.*)\)

filename = input("Please enter a file name: ")
# filename = "civil_rights150.csv"

#open csv file
data = pd.read_csv(filename, low_memory=False, encoding="ISO-8859-1")

tag_count = {}

# find all tags and add them to dictionary
for i in data['issues']:
    all_tags = re.findall(r'c\(.*c\((.*)\)', i)
    if len(all_tags) > 0:
        for i in all_tags:
            tags = i.split(', ')
            for i in tags:
                tag_count[i] = tag_count.get(i,0) + 1

sorted_tags = []
for key, val in tag_count.items():
    sorted_tags.append( (val, key) )

sorted_tags.sort(reverse=True)


#print tags counts
for value, tag in sorted_tags:
    print(tag, "was tagged", value, "times.")
