#Conor O'Riordan
#Upload iris data
#Data Sense Checks
#Explore Pandas functions

#START OF ANALYSIS.PY

#Pandas libary import
import pandas as pd
import sys

#ref https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#ref https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
#ref https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/

#iris data downloaded from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/

#import irisdata
#es.py weekly task
#command line argument
#df = pd.read_csv(f'{sys.argv[1]}', header=None)
df = pd.read_csv('irisdata.csv', header=None)

#Adding column names
print("\nColumns added to Dataset")
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#\n to insert line bewteen print spaces

#first 5 lines of dataset
print("\nFirst 5 lines of Dataset")
print(df.head(5))

#last 5 lines of data set
print("\nLast 5 lines of Dataset")
print(df.tail(5))

#shape of data
print("\nShape of dataset Rows:Columns")
print(df.shape)

#dimension of data
print("\nDataset Dimensions")
print(df.ndim)

#data types float string etc
print("\nData Types")
print(df.dtypes)

#Count of variants
print("\nCount of Iris Variants")
print(df['species'].value_counts())

#check for null values
#ref https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-a-column-in-pandas-dataframe
print("\nCount of Null values")
print(df.isnull().sum())

