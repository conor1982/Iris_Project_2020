#Conor O'Riordan
#pands-project 2020
#Iris Dateset

#Libary imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys



#iris data downloaded from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/

#import irisdata
#es.py weekly task
#command line argument
try:
    df = pd.read_csv(f'{sys.argv[1]}', header=None)

except IndexError:
    print('No File entered on command line')
    
    #system exit when an exception or error  occurs
    sys.exit(1)

#both the following needed for readfile and letter variables above
#error handling if incorrect filename with extension entered on command line
except NameError:
    print('File not Found')
    sys.exit(1)

#error handling if incorrect name entered on command line    
except FileNotFoundError:
    print('File not Found')
    sys.exit(1)
    
#df = pd.read_csv('irisdata.csv', header=None)

#Adding column names
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#\n to insert line bewteen print spaces

#first 5 lines of dataset
print("\nOVERVIEW OF DATASET")
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
#[A] https://stackoverflow.com/questions/29645153/remove-name-dtype-from-pandas-output
#convert to string to remove 'dtype: float64 in print output
print(df.dtypes.to_string())

#Count of variants
print("\nCount of Iris Variants")
#convert to string to remove 'dtype: float64 in print output
print(df['species'].value_counts().to_string())

#check for null values IN THE DATASET
#[B]https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-a-column-in-pandas-dataframe
print("\nCount of Null values")
print(df.isnull().sum().to_string())

#-----------------------------------------------------------------------------------

#Summary Stats of Dataset
# .describe() function from Pandas libary
# [C] https://pandas.pydata.org/pandas-docs/version/0.17.1/generated/pandas.DataFrame.describe.html
summary = df.describe().round(2)

#to create summarys for each variable
# [D] https://www.dataquest.io/blog/pandas-cheat-sheet
# [E] https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/

#create Sepal Length (sl) dataframe from filtering from main dataframe (df)
sl =df[['sepal_length', 'species']]
sw =df[['sepal_width', 'species']]
pl =df[['petal_length', 'species']]
pw =df[['petal_width', 'species']]

#variable created by pivoting data and applying the describe function the create summary stats
# [F] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html
# [G] https://www.python-course.eu/pandas_data_files.php
# [H] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.round.html
#summary rounded to two places
sepal_length =  sl.pivot(columns='species',values='sepal_length').describe().round(2)
sepal_width =  sw.pivot(columns='species',values='sepal_width').describe().round(2)
petal_length =  pl.pivot(columns='species',values='petal_length').describe().round(2)
petal_width =  pw.pivot(columns='species',values='petal_width').describe().round(2)

# [I] https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
# create correlation matrix for each variable
correlation = df.corr().round(2)

# range variable creation
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

#Main list
L = ['Overall Summary Stats','Sepal Length Summary Stats', 'Sepal Width Summary Stats','Petal Length Summary Stats', 'Petal Width Summary Stats', 'Correlation','Range']

#list for Range table
VL = ['Sepal Length', 'Sepal Width','Petal Length','Petal Width']

#header for diff species for text file output
species_header = "Stats Type, Setosa, Versicolor, Virginica"

# [J] https://www.w3schools.com/python/python_functions.asp
#function to create and append summary to text file
def createtxtfile(mode,heading,headertype,irisvar):
     #[K] https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
     #[L] https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
     
     # with open function
     #output file name.txt
     # mode is write or append
     with open('Summary.txt', mode, newline='') as f:
         #header list for summary file
         f.write(L[heading]+"\n")
         #header type for summary stats or correlation
         f.write(headertype+'\n')
         #[M] https://stackoverflow.com/questions/23231605/convert-pandas-dataframe-to-csv-string
         #to convert df to string in order to work for 'with open' function
         irisvar.astype(str).to_csv(f, header=False, sep =',')
         #[N] https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
         f.write("\n")

#function calls
#'w' is write mode
#'a' is append mode
# List iteration 
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

#print statements for each summary section
print("\nSUMMARY STATISTCIS")
print("\nOverall Summary")
print(summary)

print("\nSepal Length Summary")
print(sepal_length)

#[O] https://stackoverflow.com/questions/29645153/remove-name-dtype-from-pandas-output
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

#-----------------------------------------------------------------------------------

#Plots and Graphs Section

#Pairplots
#[P] https://seaborn.pydata.org/generated/seaborn.pairplot.html
#pairplot of all

#setting tickmarks and color palatte
sns.set(style = 'ticks', color_codes=True)
#colors for each species type
sns.pairplot(df,hue = 'species')
#save plot name
plt.savefig("Pairplot of Iris Data")
plt.close()

#pairplot petal width and petal length
sns.set(style = 'ticks', color_codes=True)
#plot just returning a pairplot for petal width and petal length
sns.pairplot(df,hue = 'species',vars=['petal_width','petal_length'] )
#save plot name
plt.savefig("Pairplot of Petal Width and Petal Length")
plt.close()

#heatmap
#[Q] https://seaborn.pydata.org/generated/seaborn.heatmap.html
#specifiy width and heigth of a figure
plt.figure(figsize=(10,11))

#[R] https://seaborn.pydata.org/tutorial/color_palettes.html
#heatmap for the df, labels on, line widths adjusted and color palette chosen
sns.heatmap(df.corr(),annot=True, linewidths=.5, cmap='Blues')

#save map as heatmap.png
plt.savefig('Heat Map')

# [S] https://stackoverflow.com/questions/49039581/matplotlib-savefig-will-not-overwrite-old-files
# plt.close so exisiting plot can be overwritten
plt.close()

#Hist Function
#creates histograms
def makehist(x):
    # [T] https://seaborn.pydata.org/generated/seaborn.distplot.html
    #formation of multi grid plot grids
    #hue is iris species
    #height in inches of each facet
    # data broken into bins of 5
    #legend added default location or best fit
    hist = sns.FacetGrid(df,hue="species",height=6).map(sns.distplot,x,bins=5).add_legend()
    
    #save histogram
    #print statement with text and function parameter
    plt.savefig("Histogram of {}".format(x))
    
    #see ref [S]
    #plt.close so exisiting plot can be overwritten
    plt.close()
    return hist

#Scatterplot function
#creates scatterplot
#2 parameters e.g petal_width, sepal length etc.
def makeplot(x,y):
    #[U] https://seaborn.pydata.org/generated/seaborn.scatterplot.html
    #formation of multi grid plot grids
    #hue is iris species
    #height in inches of each facet
    # data broken into bins of 5
    #legend added default location or best fit
    scatter = sns.FacetGrid(df,hue='species', height=4).map(plt.scatter,x,y).add_legend()
    
    #saves plot
    ##print statement with text and function parameter
    plt.savefig("Scatterplot of {} and {}".format(x,y))
    
    #see ref [S]
    #plt.close so exisiting plot can be overwritten
    plt.close()
    return scatter


#histogram function calls
#parameters passed
sep_len_hist = makehist('sepal_length')
sep_width_hist = makehist('sepal_width')
pet_len_hist = makehist('petal_length')
pet_width_hist =makehist('petal_width')

#scaterplot function calls
#parameters passed
scatter_sl_sw = makeplot('sepal_length','sepal_width')
scatter_pl_pw = makeplot('sepal_length','petal_length')
scatter_sl_pw = makeplot('sepal_length','petal_width')
scatter_pl_sw = makeplot('sepal_width','petal_length')
scatter_pl_sw = makeplot('sepal_width','petal_width')
scatter_pl_sw = makeplot('petal_length','petal_width')


# function parameters iris variant and variable
# functin creates a numpy array based on parameters
def overlap(variant,variable):
    #variable for filterimg dataframe
    x=df[df['species']==variant]
    #creating numpy array
    # [V] https://www.w3schools.com/python/numpy_creating_arrays.asp
    y = np.array(x[variable])
    return y

#function call to create petal length numpy arrays by variant type
versi_pl = overlap('Iris-versicolor','petal_length')
set_pl =overlap('Iris-setosa','petal_length')
vir_pl = overlap('Iris-virginica','petal_length')

#-----------------------------------------------------------------------------------

# Section on creating basic models
print('\nUnivariate Analysis of Petal Length based on Histograms Observations')

#values based on Histogram Analysis
#model values to return % accuracy
max_set_pl = 2.1
max_versi_pl = 4.8
max_vir_pl = 4.8

#variable to see how many values in the numpy array meet the values in relative variables directly above
setosa_pred = np.count_nonzero(set_pl[:]<max_set_pl)
#prints message on the number of variants identified applying the values above
#count non_zero used for aggregating numpy array
#[W] https://www.programcreek.com/python/example/102210/numpy.count_nonzero
print("Applying {} as the maximum petal length to identify a Setosa Flower predicts {} Setosas".format(max_set_pl,setosa_pred))

#as above
versicolor_pred = np.count_nonzero(versi_pl[:]<max_versi_pl)
print("Applying {} as the maximum petal length to identify a Versicolor Flower predicts {} Versicolors".format(max_versi_pl,versicolor_pred))

#as above
virginica_pred = np.count_nonzero(vir_pl[:]>=max_vir_pl)
print("Applying {} as the minimum petal length to identify a Viriginica Flower predicts {} Virginicas".format(max_vir_pl,virginica_pred))


#PDF CDF
# [X] https://medium.com/@rishav.jnit/exploratory-data-analysis-eda-on-iris-dataset-using-python-cadd850c1fc6
# [Y] https://www.kaggle.com/playingmyway/eda-of-iris-dataset

#pdf numpy array/sum numpy array
set_pl_pdf = set_pl/sum(set_pl) 
#cdf numpy cumsum function
set_pl_cdf = np.cumsum(set_pl_pdf)

versi_pl_pdf = versi_pl/sum(versi_pl) 
versi_pl_cdf = np.cumsum(versi_pl_pdf)

vir_pl_pdf = vir_pl/sum(vir_pl) 
vir_pl_cdf = np.cumsum(vir_pl_pdf)

#Function to creat PDF CDF graph
# ref [X]
# ref [Y]
def cdf_pdf(variant,variable):
    #filter the dataframe by species
    x=df[df['species']==variant]
    
    #variables to create a count for PDF calc and variable for graph with 10 bins  
    graph = counts, bin_edges= np.histogram(x[variable],bins=10, density= True)
    
    #pdf calc
    pdf=counts/(sum(counts))

    #cdf calc
    cdf=np.cumsum(pdf)

    #plot PDF line
    plt.plot(bin_edges[1:],pdf, label='{} PDF'.format(variant))
    
    #plot CDF line
    plt.plot(bin_edges[1:],cdf, label=' {} CDF'.format(variant))
    
    #apply a grid
    plt.grid()
    
    #apply legend in best fit 'loc = 0'
    plt.legend(loc =0)

    #save plot
    plt.savefig('CDF and PDF')
    return graph

#function calls on each variant and variable
# plots all three functions on one plot
# plt.close() not included in function for this reason  
set_pl_cdf_pdf = cdf_pdf('Iris-setosa','petal_length')
ver_pl_cdf_pdf = cdf_pdf('Iris-versicolor','petal_length')
vir_pl_cdf_pdf = cdf_pdf('Iris-virginica','petal_length')


print('\nModel of Petal Length based on PDF and CDF Observations')

#approx values from PDF CDF graph
# visual of intersect between variants
cdf_set_pred = 1.9
cdf_vir_versi_sep = 5

#list for loop results append
# Andrew beatty Lab 4 control flow - numbers problem
Pred = []

#[Z] https://chrisalbon.com/python/data_wrangling/pandas_create_column_with_loop/

#open of loop to run through petal length data
for row in df['petal_length']:
    
    #control flow if and elif 
    if row <= cdf_set_pred:
       #append condition to the list above
       #condition true apply relative text
       Pred.append("Predicted Setosa")
    elif row>cdf_set_pred and row <cdf_vir_versi_sep:
        Pred.append('Predicted Versicolor')
    elif row>=cdf_vir_versi_sep:
        Pred.append('Predicted Virginica')

# count number of times each condition from foor loop result appears on list
set_pred =Pred.count('Predicted Setosa')
ver_pred =Pred.count('Predicted Versicolor')
vir_pred =Pred.count('Predicted Virginica')

#variables to create % value of prediction
set_acc = (set_pred-50)/50
ver_acc = (ver_pred-50)/50
vir_acc= (vir_pred-50)/50


#prints out message of how any of each variants were identified apply CDF observations
print("Applying {} as the maximum petal length to identify a Setosa Flower predicts {} Setosas".format(cdf_set_pred,set_pred))
print("Applying {} as the maximum petal length to identify a Versicolor Flower predicts {} Versicolors".format(cdf_vir_versi_sep,ver_pred))
print("Applying {} as the minimum petal length to identify a Viriginca Flower predicts {} Virginicas".format(cdf_vir_versi_sep,vir_pred))

#prints error rate of predictions
print("\n",set_acc, 'error rate for Setosa')
print(ver_acc, 'error rate for Versicolor')
print(vir_acc, 'error rate for Virginica')



