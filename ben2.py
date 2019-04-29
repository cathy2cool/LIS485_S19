data = pd.read_csv("white_genocide.csv", low_memory=False, encoding="ISO-8859-1")


file= data[data.signatureCount == 1]
print("How many are have solo signatures : {0}".format(
    len(file)))
