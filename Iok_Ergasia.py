import pandas as pd

df_bake = pd.read_csv('bakery.csv', sep=",")

df_score = pd.read_excel('Bakery_score.xlsx',sheet_name= 1, usecols= (0,5,6,7),header=0)  
print(df_score)

df_bake = df_bake[df_bake.Product != 'NONE']

df_bakery = df_bake.merge(df_score, on='Record_id')

print(df_bakery)

df_bakery['Date'] =  pd.to_datetime(df_bakery['Date'])

df_bakery['Time'] =  pd.to_datetime(df_bakery['Time'])

df_bakery['Day'] = df_bakery['Date'].dt.day_name() 

df_bakery['Month'] = df_bakery['Date'].dt.month_name()

s = {7 : 'Morning',
    8 :'Morning', 
    9 :'Morning',
    10:'Morning',
    11:'Morning',
    12:'Morning',
    13:'Afternoon',
    14:'Afternoon',
    15:'Afternoon',
    16:'Afternoon',
    17:'Afternoon',
    18:'Afternoon',
    19:'Evening',
    20:'Evening',
    21:'Evening',
    22:'Evening',
    23:'Evening'}

df_bakery['Session'] = (df_bakery['Time'].dt.hour).map(s)


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


df_transactions = df_bakery.groupby('Transaction').agg(Products= ('Product',  ', '.join), Total_items= ('quantity', 'sum'), Total_score= ('Value_Score', 'sum'))
print(df_transactions)




#katigories 

# prwi mesimeri klp

##score sinoliko kai ana product


#print(products.unique())



