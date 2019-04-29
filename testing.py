data = pd.read_csv("pokemon.csv", low_memory=False, encoding="ISO-8859-1")


file= data[data.percent-male == 0.5]
print("pokemon that have a equal chance to be male or female : {0}".format(
    len(file)))
