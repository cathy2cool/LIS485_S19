import pandas as pd
data = pd.read_csv("civil_rights150.csv", low_memory = False, encoding="ISO-8859-1")
status = data[data.status == "responded"]
print("Petitions that were responded to: {0}".format(
    len(status)))
