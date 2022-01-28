import pandas as pd

df_bakery = pd.read_csv('bakery.csv', sep=",")

df_bakery['Date'] =  pd.to_datetime(df_bakery['Date'])

df_bakery['Day'] = df_bakery['Date'].dt.day_name() 


df_bakery['quantity'] = 1

df_bakery['productid'] = df_bakery['Product'].map(hash)


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


df_transactions = df_bakery.groupby('Transaction').agg(Products= ('Product',  ', '.join), Total_items= ('quantity', 'sum'))
print(df_transactions)

df_transactions = df_bakery.groupby('Transaction')
print(df_transactions.get_group(2))

#katigories 

# prwi mesimeri klp

##score sinoliko kai ana product


print(products.unique())



