import pandas as pd

df_bakery = pd.read_csv('bakery.csv', sep=",")

df_bakery['Date'] =  pd.to_datetime(df_bakery['Date'])

df_bakery['Day'] = df_bakery['Date'].dt.day_name() 


print(df_bakery)

products = df_bakery.Product


###             ΠΩΛΗΣΕΙΣ ΓΙΑ ΚΑΘΕ ΠΡΟΙΟΝ              ###
Products_count = products.value_counts()

print(Products_count)
###

###             ΠΩΛΗΣΕΙΣ ΓΙΑ ΚΑΘΕ ΠΡΟΙΟΝ  ΠΟΣΟΣΤΟ            ###

Products_percent = products.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'

print(Products_percent)

###


a = df_bakery.groupby('Transaction')

print(a.first())

print(a.get_group(2))

b = df_bakery.groupby(['Product', 'Transaction']).agg('sum')

print(b)

