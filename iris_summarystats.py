#Conor O'Riordan
#Past3 project plan
#Upload iris data
#Summary of Variables


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

print("\nCorrealtion")
print(df.corr().round(2))

#https://thispointer.com/pandas-apply-a-function-to-single-or-selected-columns-or-rows-in-dataframe/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html
#ref https://www.dataquest.io/blog/pandas-cheat-sheet/

#to create summarys for each variable

#creat Sepal Length (sl) dataframe from filtering from main dataframe (df)
sl =df[['sepal_length', 'species']]

#variable created by pivoting data and applying the describe function the create summary stats
sepal_length =  sl.pivot(columns='species',values='sepal_length').describe().round(2)

#exports to csv - COULD NOT APPLY COLUMN HEADINGS
sepal_length.to_csv("sl.csv")

#read in csv created above
Sepal_length_Summary = pd.read_csv('sl.csv')

#Assign column headings here so csv file will get a column heading for summary stat table
Sepal_length_Summary.columns = ['Sepal Length Summary Stats','Setosa','Versicolor', 'Virginica']

#export above to csv, with no index and a comma separtor in place
Sepal_length_Summary.to_csv('Summary.csv',index=False, sep = ',')


#Comments the same as Sepal Length expect for one addition in relation to appending to csv file
sw =df[['sepal_width', 'species']]
sepal_width =  sw.pivot(columns='species',values='sepal_width').describe().round(2)
sepal_width.to_csv("sw.csv")
Sepal_Width_Summary = pd.read_csv('sw.csv')
Sepal_Width_Summary.columns = ['Sepal Width Summary Stats','Setosa','Versicolor', 'Virginica']

#mode = 'a' here to append above to prevuiously created csv
Sepal_Width_Summary.to_csv('Summary.csv',index=False, sep = ',',mode='a')


#Comments the same as Sepal Length comments
pl =df[['petal_length', 'species']]
petal_length =  pl.pivot(columns='species',values='petal_length').describe().round(2)
petal_length.to_csv("pl.csv")
Petal_Length_Summary = pd.read_csv('pl.csv')
Petal_Length_Summary.columns = ['Petal Length Summary Stats','Setosa','Versicolor', 'Virginica']
Petal_Length_Summary.to_csv('Summary.csv',index=False, sep = ',',mode='a')

#Comments the same as Sepal Length comments
pw =df[['petal_width', 'species']]
petal_width =  pw.pivot(columns='species',values='petal_width').describe().round(2)
petal_width.to_csv("pw.csv")
Petal_Width_Summary = pd.read_csv('pw.csv')
Petal_Width_Summary.columns = ['Petal Width Summary Stats','Setosa','Versicolor', 'Virginica']
Petal_Width_Summary.to_csv('Summary.csv',index=False, sep = ',',mode='a')