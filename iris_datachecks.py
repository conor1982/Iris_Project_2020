#Upload iris data
#checks on data
#Heading needed


import pandas as pd


raw = pd.read_csv('irisdata.csv')

#data = raw.round(2)
#print(raw)
#summarystats = data.describe().round(2)
#print(summarystats)

print(raw.isnull().sum())
