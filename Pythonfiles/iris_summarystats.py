#Conor O'Riordan
#Summary of Variables


#Pandas libary import
import pandas as pd
import numpy as np

#ref https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
#ref https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/

#iris data downloaded from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/

#import irisdata
#command line prompt??
#header = None added to not have first row as heading
df = pd.read_csv('irisdata.csv', header=None)
#print(df)
#Adding column names
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#PART 2 APPEND FROM HERE TO ANALYSIS.PY

#Summary Stats of Dataset
summary = df.describe().round(2)

#https://thispointer.com/pandas-apply-a-function-to-single-or-selected-columns-or-rows-in-dataframe/


#to create summarys for each variable

#ref https://www.dataquest.io/blog/pandas-cheat-sheet
#create Sepal Length (sl) dataframe from filtering from main dataframe (df)
sl =df[['sepal_length', 'species']]
sw =df[['sepal_width', 'species']]
pl =df[['petal_length', 'species']]
pw =df[['petal_width', 'species']]

#variable created by pivoting data and applying the describe function the create summary stats
#ref https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html
#ref #ref https://www.python-course.eu/pandas_data_files.php

#ref https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
#summary rounded to two places
sepal_length =  sl.pivot(columns='species',values='sepal_length').describe().round(2)
sepal_width =  sw.pivot(columns='species',values='sepal_width').describe().round(2)
petal_length =  pl.pivot(columns='species',values='petal_length').describe().round(2)
petal_width =  pw.pivot(columns='species',values='petal_width').describe().round(2)

#ref https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
correlation = df.corr().round(2)
covariance =df.cov().round(2)

#range and variance
#variance function
def species_var(species):
    v = np.var(df[species])
    vr = print(species,'variance =',np.around(v, decimals=2))
    return vr

#sepal_length_range = sl.max() - sl.min()
sl_range = (sl.pivot(columns='species',values='sepal_length').max()-sl.pivot(columns='species',values='sepal_length').min()).round(2)
sw_range = (sw.pivot(columns='species',values='sepal_width').max()-sw.pivot(columns='species',values='sepal_width').min()).round(2)
pl_range = (pl.pivot(columns='species',values='petal_length').max()-pl.pivot(columns='species',values='petal_length').min()).round(2)
pw_range = (pw.pivot(columns='species',values='petal_width').max()-pw.pivot(columns='species',values='petal_width').min()).round(2)


#overall headers for text file sections
overall_header = "Stats Type, Sepal Length, Sepal Width, Petal Length,Petal Width"

#correlation header for text file sections
corr_header = "Variable, Sepal Length, Sepal Width, Petal Length,Petal Width"

#lists to slice to give text file section headings
L = ['Overall Summary Stats','Sepal Length Summary Stats', 'Sepal Width Summary Stats','Petal Length Summary Stats', 'Petal Width Summary Stats', 'Correlation','Range','Covariance']
VL = ['Sepal Length', 'Sepal Width','Petal Length','Petal Width']

#header for diff species for text file output
species_header = "Stats Type, Setosa, Versicolor, Virginica"

#ref https://www.w3schools.com/python/python_functions.asp
#function to create and append summary to text file
def createtxtfile(mode,heading,headertype,irisvar):
     #ref https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
     #ref https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
     with open('Summary.txt', mode, newline='') as f:
         #header list for summary file
         f.write(L[heading]+"\n")
         #header type for summary stats or correlation
         f.write(headertype+'\n')
         #ref https://stackoverflow.com/questions/23231605/convert-pandas-dataframe-to-csv-string
         #to convert df to string in order to work for 'with open' function
         irisvar.astype(str).to_csv(f, header=False, sep =',')
         #ref https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
         f.write("\n")

#function call
#'w' is write mode
#'a' is append mode
#writes to then appends to Summary.txt
createtxtfile('w',0,overall_header,summary)
createtxtfile('a',1,species_header,sepal_length)
createtxtfile('a',6,VL[0],sl_range)
createtxtfile('a',2,species_header,sepal_width)
createtxtfile('a',6,VL[1],sw_range)
createtxtfile('a',3,species_header,petal_length)
createtxtfile('a',6,VL[2],pl_range)
createtxtfile('a',4,species_header,petal_width)
createtxtfile('a',6,VL[3],pw_range)
createtxtfile('a',5,corr_header,correlation)
createtxtfile('a',7,corr_header,covariance)

#print statements for each summary section
print("Overall Summary")
print(summary)

print("\nSepal Length Summary")
print(sepal_length)

#ref https://stackoverflow.com/questions/29645153/remove-name-dtype-from-pandas-output
#convert to string to remove 'dtype: float64
print("\nSepal Length Range")
print(sl_range.to_string())

print("\nSepal Width Summary")
print(sepal_width)

print("\nSepal Width Range")
print(sw_range.to_string())

print("\nPetal Length Summary")
print(petal_length)

print("\nPetal Length Range")
print(pl_range.to_string())

print("\nPetal Width Summary")
print(petal_width)

print("\nPetal Width Range")
print(pw_range.to_string())

print("\n Correlation ")
print(correlation)

print("\n Covariance ")
print(covariance)   