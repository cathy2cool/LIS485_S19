data = pd.read_csv("white_genocide.csv", low_memory=False, encoding="ISO-8859-1")


status= data[data.status == "open"]
print("How many are open: {0}".format(
    len(status)))
