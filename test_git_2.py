import pandas as pd 

df = pd.read_csv('dataset.csv')

print(df)

df2 = df[df['x1']<0]

print(df2)

