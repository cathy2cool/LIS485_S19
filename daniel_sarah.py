import pandas as pd
df = pd.read_csv('civil_rights150.csv',
                     index_col='id',
                     low_memory=False,
                     encoding="ISO-8859-1",
                     header=0
                     )

df.human_time= df.human_time.apply(pd.to_datetime)

df['Day'] = [d.date() for d in df['human_time']]
df['Time'] = [d.time() for d in df['human_time']]

df.to_csv('new_civil_rights.csv')

print(df)
