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

summary = df.describe().round(2)


#print("\nCorrealtion")
#print(df.corr().round(2))

#https://thispointer.com/pandas-apply-a-function-to-single-or-selected-columns-or-rows-in-dataframe/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html
#ref https://www.dataquest.io/blog/pandas-cheat-sheet/

#to create summarys for each variable

#creat Sepal Length (sl) dataframe from filtering from main dataframe (df)
sl =df[['sepal_length', 'species']]
sw =df[['sepal_width', 'species']]
pl =df[['petal_length', 'species']]
pw =df[['petal_width', 'species']]

#variable created by pivoting data and applying the describe function the create summary stats
sepal_length =  sl.pivot(columns='species',values='sepal_length').describe().round(2)
sepal_width =  sw.pivot(columns='species',values='sepal_width').describe().round(2)
petal_length =  pl.pivot(columns='species',values='petal_length').describe().round(2)
petal_width =  pw.pivot(columns='species',values='petal_width').describe().round(2)

#overall headers for text file sections
overall_header = "Sepal Length,Sepal Width,Petal Length,Petal Width"

#list to slice to give text file section headings
L = ['Overall Summary Stats','Sepal Length Summary Stats', 'Sepal Width Summary Stats','Petal Length Summary Stats', 'Petal Width Summary Stats']

#header for diff species for text file output
species_header = "Stats Type, Setosa, Versicolor, Virginica"


#ref https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
#ref https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
#ref https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file


#function to create and append summary to text file
def createtxtfile(mode,heading,irisvar):
     with open('Summary.txt', mode, newline='') as f:
         f.write(L[heading]+"\n")
         f.write(overall_header+'\n')
         irisvar.astype(str).to_csv(f, header=False, sep =',')
         f.write("\n")


#function call
createtxtfile('w',0,summary)
createtxtfile('a',1,sepal_length)
createtxtfile('a',2,sepal_width)
createtxtfile('a',3,petal_length)
createtxtfile('a',4,petal_width)



#ref https://www.python-course.eu/pandas_data_files.php



#test = df['sepal_length'] >5

#c = test.groupby(df['sepal_length']>5)




