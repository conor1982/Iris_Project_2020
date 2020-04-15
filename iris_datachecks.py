#Conor O'Riordan
#Past2 project plan
#Upload iris data
#Data Checks
#Explore Python

#Pandas libary import
import pandas as pd



#ref https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/

#iris data downloaded from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/

#import irisdata
#command line prompt??
#header = None added to not have first row as heading
df = pd.read_csv('irisdata.csv', header=None)

#print first 5 lines check for headings
print(df.head(5))

#Adding column names
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Species']

# \n to insert line bewteen print spaces

#first 5 lines of dataset
print("\nFirst 5 lines")
print(df.head(5))

#last 5 lines of data set
print("\nLast 5 lines")
print(df.tail(5))

#shape of data
print("\nShape of dataset Rows:Columns")
print(df.shape)

#dimension of data
print("\nDatset dimensions")
print(df.ndim)

#data types float string etc
print("\nData types")
print(df.dtypes)

#Summary Stats of Dataset
print("\nStats Summary")
print(df.describe())

print("Iris variant count")
print(df['Species'].value_counts())

