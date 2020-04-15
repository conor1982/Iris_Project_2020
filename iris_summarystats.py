#Conor O'Riordan
#Past2 project plan
#Upload iris data
#Data Checks
#Explore Python

#Pandas libary import
import pandas as pd

#ref https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
#ref https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/

#iris data downloaded from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/

#import irisdata
#command line prompt??
#header = None added to not have first row as heading
df = pd.read_csv('irisdata.csv', header=None)

#Adding column names
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#Summary Stats of Dataset
print("\nStats Summary")
print(df.describe().round(2))

print("\nSepal Length Summary Stats\n",df.pivot(columns='species',values='sepal_length').describe())
print(df.pivot(columns='species', values='sepal_width').describe(), "\n")
print(df.pivot(columns='species', values='petal_length').describe(), "\n")
print(df.pivot(columns='species', values='petal_width').describe(), "\n")

species = df.groupby('species')
print(species.mean())
print(species.min())
print(species.max())
print(species.median())
print(species.std())

range = species.mean() - species.min()
print(range)

sepal_length = df.pivot(columns='species',values='sepal_length').describe().round(2)

sepal_width =  df.pivot(columns='species',values='sepal_width').describe().round(2)

sepal_length.to_csv("Summary.csv",encoding='utf-8',sep='\t')

sepal_width.to_csv("Summary.csv",sep='\t',encoding='utf-8',mode='a' )


#https://thispointer.com/pandas-apply-a-function-to-single-or-selected-columns-or-rows-in-dataframe/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html
