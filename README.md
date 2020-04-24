# Iris_Project_2020
Programming and Scripting Module Final Project

***
## Objectives of Project
1.	Research the Dataset: Background information on the dataset with a summary.
2.	Download Data and upload into Github
3.	Summary of Programming Language used and libraries utlised.
4.	Summarise statistics of the Data
5.	Histogram of each variable
6.	Scatter plots of each variable
7.	Learning outcomes
8.	References

***
## Background information on the Data

### Overview of Irish Data Set
The Iris data set  is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. [1]

##### Fig 1
![Iris Flower](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/iris.png)

It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula *“all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”*. [1] [4]

Multivariate (Data analysis) refers to any statistical technique used to analyze data which arises from more than one variable. 

*Multivariate data analysis is a set of statistical models that examine patterns in multidimensional data by considering, at once, several data variables. It is an expansion of bivariate data analysis, which considers only two variables in its models. As multivariate models consider more variables, they can examine more complex phenomena and find data patterns that more accurately represent the real world.* [2]

### Summary of Data
The data classifies three variants of the Iris flower based on certain attributes. The three variants of Iris flower found in the dataset are: [3]
    
    1 Iris Setosa
    2 Iris Versicolour
    3 Irish Virginica

##### Fig 2
![Iris Variants](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/variants.png)

For each variant, data was gathered based on four different attributes: [2]

    1 Sepal Length (in cm)
    2 Sepal Width (in cm)
    3 Petal Length (in cm)
    4 Petal Width (in cm)

The dataset contains a set of 150 records. Each row in the table represents one Iris flower with a measurement of each attribute above and its relative variant.

There are 50 different data points for each variant of Iris. With the complete dataset containing only 150 observations, it is a very popular dataset in teaching and study. It contains real data of good quality which is viewed more favourably than using test data for instance.

Previous studies on the data set show that Iris Setosa is easily seperable from the other two linearly. There is some overlap between the other two making it more difficult to distinguish from each other. [3] This will be demonstrated in this project through the use of various Visualisation techniques. We will aslo show using the Cumulative Distribution Fucntion (CDF) how an initial simple model with fairly high accuracy can be created through initial Exploratory Data Analysis [5] [6]. 

***
## How to Run and Python Libaries used

### Instructions: How to Run

* Analysis.py can be run from the command line. 
* The Irisdata set must be entered as an argument on the command line also.
* The Iris Data set must be in the same folder you are running the command from.
* All graphical outputs and summary tables will appear in the same folder where program is run.
* If the incorrect file name is entered or the file does not exisit within the relevant folder, the user will recieve an error message i.e. *'File not Found'*

### Programming Language
* Python was used in this project
* Python version used *Python3.7.6*
* Program developed in Microsoft Visual Studio

### Python Libaries

#### Pandas
* imported alias *Pandas as pd*
* extensively used in this project
* popular libary for data analysis and data manipulation

#### Numpy
* imported alias *Numpy as np*
* allows to create extensive arrays and matrices

#### matplotlib
* imported alias *Matplotlib.pyplot as plt*
* numerical extension to Numpy
* Extensive plotting tools

#### Seaborn
* imported alias *Seaborn as sns*
* Seaborn is a Python visualization library based on matplotlib
* Provides excellent graphical visualisations
* Provides a higher level of visualisation than Matplotlib

#### Sys
* imported to allow program to be run from a command line argument

***
## Importing the Irish Data Set 

### Source of Data

The dataset used in this project was downloaded from the UCI Machine Learning Repository website [3]. Once downloaded it was added to my Github Repsository. Using the Pandas libary in Python a number of checks were conducted to sense check the version of the imported iris data. [7]

##### Fig 3
![Pic of Raw Data](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/iris_raw_data.png)

We can see from Fig 1 that heading needed to be added to this data source. The columns were given the names : sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'.

```python
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
```
### Overview of Data

In researching the dataset, it is undertood that their are 150 rows of data. The variable measurements are in CM and there are three variants (species) of Iris in the dataset. 

I felt it useful to create an overview of the dataset in Python. This included:
   
    1 First 5 and last 5 rows of the Dataset
    2 Shape of the Dataset
    3 Dimensions of Dataset
    4 Data Types
    5 Count of Species variants
    6 Count of null values

```python
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
print("\nCount of Null values")
print(df.isnull().sum())

#print summary stats
print('summary')
print(df.describe())
```
##### Fig 4
![Dataset Overview](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/iris_dataset_overview.png)

Through this overview, a good understanding of the actual dataset can be obtained. The first and last 5 rows, will gve a useful look of what a row contains. The shape of the dataset being 150 rows and 5 columns matches what was gathered during researching the data. 

The datatypes are also an important element of the dataset to understand. Here we see the four different variables as float numbers and the species a string value. There was also no null values in this dataset.

Understanding each element of this gave me confidence that the dataset downloaded for the project was of good integrity.

One further check was running the *pandas.describe* function. The results from this were compared with other summarries found online. There were no discrepencies found in any of the datasets used in the comparison [8] [9].

***
## Summary Statistics

Again utilising the Pandas libary, summary statistics tables were created. One for the overall data set and one for each variable by species type. The range was also calculate for each variable by species type. Finally a correlation matrix was created for each variable. All summaries were rounded to two decimel places.

To create a summary by variable the *.pivot* function was used in pandas. Although it does not support aggregation, I felt it worked well to use with the *.describe()* [7].

### Table 1 - Overall Summary Stats

|Overall Summary Stats      	|              	|             	|              	|             	|
|----------------------------	|--------------	|-------------	|--------------	|-------------	|
| Stats Type                 	| Sepal Length 	| Sepal Width 	| Petal Length 	| Petal Width 	|
| count                      	| 150.0        	| 150.0       	| 150.0        	| 150.0       	|
| mean                       	| 5.84         	| 3.05        	| 3.76         	| 1.2         	|
| std                        	| 0.83         	| 0.43        	| 1.76         	| 0.76        	|
| min                        	| 4.3          	| 2.0         	| 1.0          	| 0.1         	|
| 25%                        	| 5.1          	| 2.8         	| 1.6          	| 0.3         	|
| 50%                        	| 5.8          	| 3.0         	| 4.35         	| 1.3         	|
| 75%                        	| 6.4          	| 3.3         	| 5.1          	| 1.8         	|
| max                        	| 7.9          	| 4.4         	| 6.9          	| 2.5         	|

### Summary of each Variable by Species Type

#### Table 2 - Sepal Length

| Sepal Length Summary Stats 	|        	|            	|           	|
|----------------------------	|--------	|------------	|-----------	|
| Stats Type                 	| Setosa 	| Versicolor 	| Virginica 	|
| count                      	| 50.0   	| 50.0       	| 50.0      	|
| mean                       	| 5.01   	| 5.94       	| 6.59      	|
| std                        	| 0.35   	| 0.52       	| 0.64      	|
| min                        	| 4.3    	| 4.9        	| 4.9       	|
| 25%                        	| 4.8    	| 5.6        	| 6.22      	|
| 50%                        	| 5.0    	| 5.9        	| 6.5       	|
| 75%                        	| 5.2    	| 6.3        	| 6.9       	|
| max                        	| 5.8    	| 7.0        	| 7.9       	|

#### Table 3 - Range of Sepal Length

| Range           	|     	|
|-----------------	|-----	|
| Sepal Length    	|     	|
| Iris-setosa     	| 1.5 	|
| Iris-versicolor 	| 2.1 	|
| Iris-virginica  	| 3.0 	|

#### Table 4 - Sepal Width

| Sepal Width Summary Stats  	|        	|            	|           	|
|----------------------------	|--------	|------------	|-----------	|
| Stats Type                 	| Setosa 	| Versicolor 	| Virginica 	|
| count                      	| 50.0   	| 50.0       	| 50.0      	|
| mean                       	| 3.42   	| 2.77       	| 2.97      	|
| std                        	| 0.38   	| 0.31       	| 0.32      	|
| min                        	| 2.3    	| 2.0        	| 2.2       	|
| 25%                        	| 3.12   	| 2.52       	| 2.8       	|
| 50%                        	| 3.4    	| 2.8        	| 3.0       	|
| 75%                        	| 3.68   	| 3.0        	| 3.18      	|
| max                        	| 4.4    	| 3.4        	| 3.8       	|            	

#### Table 5 - Range of Sepal Width

| Range           	|     	|
|-----------------	|-----	|
| Sepal Width     	|     	|
| Iris-setosa     	| 2.1 	|
| Iris-versicolor 	| 1.4 	|
| Iris-virginica  	| 1.6 	|    	

#### Table 6 - Petal Length

| Petal Length Summary Stats 	|        	|            	|           	|
|----------------------------	|--------	|------------	|-----------	|
| Stats Type                 	| Setosa 	| Versicolor 	| Virginica 	|
| count                      	| 50.0   	| 50.0       	| 50.0      	|
| mean                       	| 1.46   	| 4.26       	| 5.55      	|
| std                        	| 0.17   	| 0.47       	| 0.55      	|
| min                        	| 1.0    	| 3.0        	| 4.5       	|
| 25%                        	| 1.4    	| 4.0        	| 5.1       	|
| 50%                        	| 1.5    	| 4.35       	| 5.55      	|
| 75%                        	| 1.58   	| 4.6        	| 5.88      	|
| max                        	| 1.9    	| 5.1        	| 6.9       	|            	

#### Table 7 - Range of Petal Length

| Range           	|     	|
|-----------------	|-----	|
| Petal Length    	|     	|
| Iris-setosa     	| 0.9 	|
| Iris-versicolor 	| 2.1 	|
| Iris-virginica  	| 2.4 	|

#### Table 8 - Petal Width

 | Petal Width Summary Stats  	|        	|            	|           	|
|----------------------------	|--------	|------------	|-----------	|
| Stats Type                 	| Setosa 	| Versicolor 	| Virginica 	|
| count                      	| 50.0   	| 50.0       	| 50.0      	|
| mean                       	| 0.24   	| 1.33       	| 2.03      	|
| std                        	| 0.11   	| 0.2        	| 0.27      	|
| min                        	| 0.1    	| 1.0        	| 1.4       	|
| 25%                        	| 0.2    	| 1.2        	| 1.8       	|
| 50%                        	| 0.2    	| 1.3        	| 2.0       	|
| 75%                        	| 0.3    	| 1.5        	| 2.3       	|
| max                        	| 0.6    	| 1.8        	| 2.5       	|       	

#### Table 9 - Range of Petal Width

| Range           	|     	|
|-----------------	|-----	|
| Petal Width     	|     	|
| Iris-setosa     	| 0.5 	|
| Iris-versicolor 	| 0.8 	|
| Iris-virginica  	| 1.1 	|

#### Table 10 - Correlation

| Correlation  	|              	|             	|              	|             	|
|--------------	|--------------	|-------------	|--------------	|-------------	|
| Variable     	| Sepal Length 	| Sepal Width 	| Petal Length 	| Petal Width 	|
| sepal_length 	| 1.0          	| -0.11       	| 0.87         	| 0.82        	|
| sepal_width  	| -0.11        	| 1.0         	| -0.42        	| -0.36       	|
| petal_length 	| 0.87         	| -0.42       	| 1.0          	| 0.96        	|
| petal_width  	| 0.82         	| -0.36       	| 0.96         	| 1.0         	|


#### Example of code for Summary Tables

```python
#Summary Stats of Dataset
summary = df.describe().round(2)

#create Sepal Length (sl) dataframe from filtering from main dataframe (df)
sl =df[['sepal_length', 'species']]
sw =df[['sepal_width', 'species']]
pl =df[['petal_length', 'species']]
pw =df[['petal_width', 'species']]

#summary rounded to two places
sepal_length =  sl.pivot(columns='species',values='sepal_length').describe().round(2)
sepal_width =  sw.pivot(columns='species',values='sepal_width').describe().round(2)
petal_length =  pl.pivot(columns='species',values='petal_length').describe().round(2)
petal_width =  pw.pivot(columns='species',values='petal_width').describe().round(2)

#correlation
correlation = df.corr().round(2)
```
### Summary Text File creation

Each summary is outputted to a single *.txt* file. A function was created for this task with the funtion parameters including: [11] [12] [13]

* mode type: either writing or appending to *.txt* file
* heading: slice a list for what summary heading to use
* heading type: selecte a different header for either overall summary or by variable
* irisvar: what summary to write/append to the *.txt* file

#### Example of Code for Summary file creation

```python
#overall headers for text file sections
overall_header = "Stats Type, Sepal Length, Sepal Width, Petal Length,Petal Width"

#correlation header for text file sections
corr_header = "Variable, Sepal Length, Sepal Width, Petal Length,Petal Width"

#lists to slice to give text file section headings
L = ['Overall Summary Stats','Sepal Length Summary Stats', 'Sepal Width Summary Stats','Petal Length Summary Stats', 'Petal Width Summary Stats', 'Correlation','Range','Covariance']
VL = ['Sepal Length', 'Sepal Width','Petal Length','Petal Width']

#header for diff species for text file output
species_header = "Stats Type, Setosa, Versicolor, Virginica"

#function to create and append summary to text file
def createtxtfile(mode,heading,headertype,irisvar):
     with open('Summary.txt', mode, newline='') as f:
         #header list for summary file
         f.write(L[heading]+"\n")
         #header type for summary stats or correlation
         f.write(headertype+'\n')
         #to convert df to string in order to work for 'with open' function
         irisvar.astype(str).to_csv(f, header=False, sep =',')
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
```
***
## Exploratory Data Analysis and Supporting Graphics

### Pairplot

##### Fig 5
![Pairplot](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/Pairplot%20of%20Iris%20Data.png)

Beacuse of the multivariate nature of the data set, a pairplot is a useful way to view the bivarariate relation between all variables in one place. 

From the pairplot, petal width and petal length look like the best features to use to identify species type. Setosa is very separate while Versicolor and Viriginica have some overlap.

Sepal width and sepal length are not easily seperable from each other and contains quite alot of overlap of features.

### Heatmap

##### Fig 6
![Heatmap](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/Heat%20Map.png)

This Heatmap is an excellent graphical representaion of Table 10 as seen earlier. This correaltion matrix again shows a very positive correlation of 0.96 between petal width and length. There also appears to be a strong correaltion between sepal length and petal length also 0.87.

*The range of correlation coeffiecent values run from -1.0 to 1.0 where -1.0 indicates a perfect negative correaltion and 1.0 indicates a perfrect positive correaltion [14] The closer to these figures indicates a strong correlation.* With a value of 0.96, petal length and petal width have a very strong positive correlation.

The strength of association according to guidleines intrepreting Pearsons's correlation would be *Large* [14] 

### Scatterplots

*A scatterplot is a type of data display that shows the relationship between two numerical variables. Each member of the dataset gets plotted as a point whose (x, y)(x,y)left parenthesis, x, comma, y, right parenthesis coordinates relates to its values for the two variables.* [16]

Scatterplots are a 2d representaion of each variable together. We can use these to attempt to draw a line between each Iris species. Those that look separable more linearly will be more useful in identifying what pair of variables are most useful together.

A scatterplot was created for each pair of variables. A function was created with the function parameter being the variable x and variable y i.e. sepal width, petal length. This allowed for more efficent coding when creating scatter plots for each variable.

#### Code example

```python
#Scatterplot function
def makeplot(x,y):
    scatter = sns.FacetGrid(df,hue='species', height=4)\
        .map(plt.scatter,x,y)\
        .add_legend()
    plt.savefig("Scatterplot of {} and {}".format(x,y))
    plt.close()
    return scatter

#scaterplot function calls
scatter_sl_sw = makeplot('sepal_length','sepal_width')
scatter_pl_pw = makeplot('sepal_length','petal_length')
scatter_sl_pw = makeplot('sepal_length','petal_width')
scatter_pl_sw = makeplot('sepal_width','petal_length')
scatter_pl_sw = makeplot('sepal_width','petal_width')
scatter_pl_sw = makeplot('petal_length','petal_width')
```

#### Sepal Width and Sepal Length Scatter Plot

##### Fig 7 
![Sepal Width Sepal Length Scatter](https://github.com/conor1982/Iris_Project_2020/blob/master/Scatterplots/Scatterplot%20of%20sepal_length%20and%20sepal_width.png)

This scatter plot shows that Setosa is distinguisable from the other two species of Iris. However a lot of ovelap can be seen between Veriscolor and Virginica. Looking back to the correaltion table we see that there is a *Small* negative correaltion of -0.11 between the two species. 

#### Petal Width and Petal Length Scatter Plot

##### Fig 8
![Petal Width Petal Length Scatter](https://github.com/conor1982/Iris_Project_2020/blob/master/Scatterplots/Scatterplot%20of%20petal_length%20and%20petal_width.png)

This scatter plot shows that Setosa is distinguisable from the other two species of Iris. There is some minor ovelap can be seen between Veriscolor and Virginica. Looking back to the correaltion table we see that these variables have the strongest positive correaltion and would be the most useful when trying to predict a species type based  on petal width and petal length.

There is also *Strong* correlations between sepal length:petal length and sepal length:petal width but the overlap between Versicolor and Virginica is more prevelant than can be seen when analysing petal width:petal length.

##### Fig 9
![Sepal Length Petal Length Scatter](https://github.com/conor1982/Iris_Project_2020/blob/master/Scatterplots/Scatterplot%20of%20sepal_length%20and%20petal_length.png)

##### Fig 10
![Sepal Length Petal Width Scatter](https://github.com/conor1982/Iris_Project_2020/blob/master/Scatterplots/Scatterplot%20of%20sepal_length%20and%20petal_width.png)

### Histograms

A histogram is a plot that lets you discover, and show, the underlying frequency distribution (shape) of a set of continuous data. This allows the inspection of the data for its underlying distribution (e.g., normal distribution), outliers, skewness, etc. [15]. A Histogram is a univariate plot. These Histograms plots each species of Iris individually.

To construct a histogram from a continuous variable you first need to split the data into intervals, called bins [15]

A histogram was created for each variable The data for each was split into 5 bins. A function was created with the function parameter being the variable i.e. sepal width, petal length etc. This allowed for more effiecnt code when creating a Histogram for each variable. These Histograms also display the PDF (probability density function) which will be looked at in more detail later on.

#### Code example

```python
#Hist Function
def makehist(x):
    hist = sns.FacetGrid(df,hue="species",height=6) \
        .map(sns.distplot,x, bins=5) \
        .add_legend()
    #plt.title(x)
    plt.savefig("Histogram of {}".format(x))
    plt.close()
    return hist

#histogram function calls
sep_len_hist = makehist('sepal_length')
sep_width_hist = makehist('sepal_width')
pet_len_hist = makehist('petal_length')
pet_width_hist =makehist('petal_width')
```
#### Sepal Length

##### Fig 11
![Sepal Length Histogram](https://github.com/conor1982/Iris_Project_2020/blob/master/Histograms/Histogram%20of%20sepal_length.png)

We can observe from the Histogram there is considerable overlap between the three species

#### Sepal Width

##### Fig 12
![Sepal Width Histogram](https://github.com/conor1982/Iris_Project_2020/blob/master/Histograms/Histogram%20of%20sepal_width.png)

We can observe from this Histogram that all species are fully overlapped

#### Petal Length

##### Fig 13
![Petal Length Histogram](https://github.com/conor1982/Iris_Project_2020/blob/master/Histograms/Histogram%20of%20petal_length.png)

We can obseve from the Histogram that Setosa is easily seperable while there is some overlap between Versicolor and Virginica.

Creating a basic model: [20]

* if petal length < 2.1 then Setosa - this would have 100% accuracy
* if petal length >2.1 and <= 4.8 the Versilcolor - this would be accuarate for 92%
* if petal length > 4.8 then Virginica - this would be accurate for 94% 

The above shows how using Histograms can be very useful when creating an initial high level model for identifying species type in this dataset.

##### Code Example

```python
#function for overlap
def overlap(variant,variable):
    x=df[df['species']==variant]
    y = np.array(x[variable])
    return y

#petal lengths
versi_pl = overlap('Iris-versicolor','petal_length')
set_pl =overlap('Iris-setosa','petal_length')
vir_pl = overlap('Iris-virginica','petal_length')

#parameters based on Histogram Analysis
#basic model parameters to return % accuracy
max_set_pl = 2.1

max_versi_pl = 4.8

max_vir_pl = 4.8

print('Univariate Analysis of Petal Length based on Histograms Observations')

setosa_accuracy = np.count_nonzero(set_pl[:]<max_set_pl)/np.count_nonzero(set_pl)
print("Applying {} as the maximum petal length to identify a Setosa Flower would have an accuaracy of {:.2%}".format(max_set_pl,setosa_accuracy))

versicolor_accuracy = np.count_nonzero(versi_pl[:]<=max_versi_pl)/np.count_nonzero(versi_pl)
print("Applying {} as the maximum petal length to identify a Versilcolor Flower would have an accuaracy of {:.2%}".format(max_versi_pl,versicolor_accuracy))

virginica_accuracy = np.count_nonzero(vir_pl[:]>max_vir_pl)/np.count_nonzero(vir_pl)
print("Applying {} as the maximum petal length to identify a Virginica Flower would have an accuaracy of {:.2%}".format(max_vir_pl,virginica_accuracy))
```

#### Petal Width

##### Fig 14
![Petal Width Length Histogram](https://github.com/conor1982/Iris_Project_2020/blob/master/Histograms/Histogram%20of%20petal_width.png)

We can obseve from the Histogram that Setosa is easily seperable while there is a wider overlap between Versicolor and Virginica in compared to the petal length Histogram.

### PDF (Probability Density Function) and CDF (Cumulative Distribution Frequency)

*Probability density function (PDF) is a statistical expression that defines a probability distribution (the likelihood of an outcome) for a discrete random variable (e.g., a stock or ETF) as opposed to a continuous random variable. The difference between a discrete random variable is that you can identify an exact value of the variable.* [17]

*DF(X) generates a probability mass function or density function according to whether it thinks «X» is discrete or continuous. CDF(x) does the same, generating a cumulative mass or cumulative probability function. If «X» contains text values it knows «X» must be discrete. If «X» contains numbers with few or no identical values, it guesses continuous. If «X» contains numbers with many identical values, it guesses discrete.*

The PDF and CDF are very common techniques in exploratory data analysis. The CDF is cumulative sum of the PDF over a defined interval. After observing the Histograms above, the petal length histogram will be used in the PDF and CDF analysis.

#### Code example


```python
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
```
#### Setosa

##### Fig 15
![Setosa PDF CDF](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/CDF%20and%20PDF%20for%20Iris-setosa.png)

#### Versicolor

##### Fig 16
![Versicolor PDF CDF](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/CDF%20and%20PDF%20for%20Iris-versicolor.png)

#### Virginica

##### Fig 17
![Virginica PDF CDF](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/CDF%20and%20PDF%20for%20Iris-virginica.png)

#### Combined

##### Fig 18
![Combined PDF CDF](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/CDF%20and%20PDF.png)

We can observe from this Graph that: [19]

* 100% of Setosa's have a petal length <2
* approx 95% of Versicolor  have a petal length of <= 5
* approx 90% of Virigina have a petal length >5

***
## Summary and Conclusion

### Learning Outcomes

#### Python

This project was an excellet learning curve into programming particulary Python. Having never used Pyhon before January 2020, this project offered the opportunity in particular to utilise the key Python libaries used for Data Analysis.

Getting to research and adopt some functions of the Pandas libary for this project was very interesting. Although still a bit to learn and making my code more streamlined, I feel I have the confidence now to apply some techniques leanred from Pandas in my current role.

Also, using Matplotlib and especially Seaborn opened up the incredible graphical and visualisation options on offer. This project was a great opportunity to discover and some of these functions.

#### Github

Prior to starting this course I was unaware of Github. Having the opportunity to work with it is something I will continue to use and will begin to implement in my current role. While doing the *README* file, learning about Markdown language was extremely beneficial

Also, as advised in the project documentation, breaking up this project into smaller parts was very important. Github allowed me to keep track of an initial project plan. Breaking it up into smaller sections definitely helped with the programming side rather than try and do it all together.

### Iris data

#### Analysis

As stated before and noted during research, the iris data set is a very popular dataset particularly in the teaching of data analyis and machine learning. Utilising the power of Python to create an exploratory analysis of the dataset was a the biggest learning outcome. 

The next step will be learning and applying more statistical machine learning based approach to develop and apply more robust models for predicting and forecsating.

In this project, observations from histograms, scatterplots and density plots allowed me to create some basic control flow arguments that identify an Iris species based on a particular value. 

From the observations and research, petal length was the best variable to create some models. While these might be somewhat useful as a basic predictor, as I move further along this course, I will develop more skills to adopt more mathematical and statistical functions and techniques.



##### Code example

```python
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
print("Applying {} as the minimum petal length to identify a Viriginica Flower would predicts {} Virginicas".format(max_vir_pl,virginica_pred))


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
```

***
### References

1. https://en.wikipedia.org/wiki/Iris_flower_data_set
2. https://towardsdatascience.com/an-introduction-to-multivariate-data-analysis-ece93ceb1ed3
3. https://archive.ics.uci.edu/ml/datasets/iris
4. https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
5. https://towardsdatascience.com/what-why-and-how-to-read-empirical-cdf-123e2b922480
6. https://www.kaggle.com/playingmyway/eda-of-iris-dataset
7. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html
8. https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e
9. https://www.researchgate.net/figure/Example-summary-statistics-for-the-Iris-data_fig4_26387272
10. https://www.tablesgenerator.com/markdown_tables
11. https://www.w3schools.com/python/python_functions.asp
12. https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
13. https://stackoverflow.com/questions/23231605/convert-pandas-dataframe-to-csv-string
14. https://statistics.laerd.com/statistical-guides/pearson-correlation-coefficient-statistical-guide.php
15. https://statistics.laerd.com/statistical-guides/understanding-histograms.php
16. https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/introduction-to-scatterplots/a/scatterplots-and-correlation-review
17. https://www.investopedia.com/terms/p/pdf.asp
18. https://wiki.analytica.com/Cdf_and_Pdf_Functions
19. https://www.youtube.com/watch?v=hCBr43Wv_Es
20. https://www.youtube.com/watch?v=11BFX7Ygtyo

***
### References in Code

* [A] https://stackoverflow.com/questions/29645153/remove-name-dtype-from-pandas-output
* [B]https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-a-column-in-pandas-dataframe
* [C] https://pandas.pydata.org/pandas-docs/version/0.17.1/generated/pandas.DataFrame.describe.html
* [D] https://www.dataquest.io/blog/pandas-cheat-sheet
* [E] https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
* [F] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html
* [G] https://www.python-course.eu/pandas_data_files.php
* [H] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.round.html
* [I] https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
* [J] https://www.w3schools.com/python/python_functions.asp
* [K] https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
* [L] https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
* [M] https://stackoverflow.com/questions/23231605/convert-pandas-dataframe-to-csv-string/
* [N] https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
* [O] https://stackoverflow.com/questions/29645153/remove-name-dtype-from-pandas-output
* [P] https://seaborn.pydata.org/generated/seaborn.pairplot.html
* [Q] https://seaborn.pydata.org/generated/seaborn.heatmap.html
* [R] https://seaborn.pydata.org/tutorial/color_palettes.html
* [S] https://stackoverflow.com/questions/49039581/matplotlib-savefig-will-not-overwrite-old-files
* [T] https://seaborn.pydata.org/generated/seaborn.distplot.html
* [U] https://seaborn.pydata.org/generated/seaborn.scatterplot.html
* [V] https://www.w3schools.com/python/numpy_creating_arrays.asp
* [W] https://www.programcreek.com/python/example/102210/numpy.count_nonzero
* [X] https://medium.com/@rishav.jnit/exploratory-data-analysis-eda-on-iris-dataset-using-python-cadd850c1fc6
* [Y] https://www.kaggle.com/playingmyway/eda-of-iris-dataset
* [Z] https://chrisalbon.com/python/data_wrangling/pandas_create_column_with_loop/

***
### Figures

1. Iris Flower
2. Iris Variants
3. Raw Data
4. Dataset Overview
5. Pairplot
6. Heatmap
7. Sepal width:sepal length Scatterplot
8. Petal width: petal length Scatterplot
9. Sepal length: petal length Scatterplot
10. Sepal Length petal width Scatterplot
11. Sepal length Histogram
12. Sepal width Histogram
13. Petal length Histogram
14. Petal width Histogram
15. Setosa PDF CDF Graph
16. Versicolor PDF CDF Graph
17. Virginica PDF CDF Graph
18. Overall PDF CDF Graph

