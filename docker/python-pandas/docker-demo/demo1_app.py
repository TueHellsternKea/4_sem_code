import pandas as pd
df = pd.read_csv('customers.csv', sep=';')
print(df.head(10))