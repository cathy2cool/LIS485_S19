import pandas as pd
#This code checks the number of petitions with less than 500 signatures 
# Read the file
data = pd.read_csv("civil_rights150.csv", low_memory=False, encoding="ISO-8859-1")

petition_num = data[data.signatureCount < 500]
print("Petitions with less that 100 sigs: {0}".format(
    len(petition_num)))
