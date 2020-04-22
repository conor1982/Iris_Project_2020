# Iris_Project_2020
Programming and Scripting Module Final Project

## Objectives of Project
1.	Research the Dataset: Background information on the dataset with a summary.
2.	Download Data and upload into Github
3.	Summary of Programming Language used and libraries utlised.
4.	Summarise statistics of the Data
5.	Histogram of each variable
6.	Scatter plots of each variable
7.	Learning outcomes
8.	References

## Background information on the Data
(what is the data, who collected it, how it was collected, uses today?)

### Overview of Irish Data Set
The Iris data set  is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. [1]

![Iris Flower](https://github.com/conor1982/Iris_Project_2020/blob/master/iris.png)

It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”. [1] [4]

Multivariate (Data analysis) refers to any statistical technique used to analyze data which arises from more than one variable. 

Multivariate data analysis is a set of statistical models that examine patterns in multidimensional data by considering, at once, several data variables. It is an expansion of bivariate data analysis, which considers only two variables in its models. As multivariate models consider more variables, they can examine more complex phenomena and find data patterns that more accurately represent the real world. [2]

### Summary of Data
The data classifies three variants of the Iris flower based on certain attributes. The three variants of Iris flower found in the dataset are: [3]
    
    1 Iris Setosa
    2 Iris Versicolour
    3 Irish Virginica

![Iris Variants](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/variants.png)

For each variant, data was gathered based on four different attributes: [2]

    1 Sepal Length (in cm)
    2 Sepal Width (in cm)
    3 Petal Length (in cm)
    4 Petal Width (in cm)

The dataset contains a set of 150 records. Each row in the table represents one Iris flower with a measurement of each attribute above and its relative variant.

There are 50 different data points for each variant of Iris. With the complete dataset containing only 150 observations, it is a very popular dataset in teaching and study. It contains real data of good quality which is viewed more favourably than using test data for instance.

Previous studies on the data set show that Iris Setosa is easily seperable from the other two linearly. There is some overlap between the other two making it more difficult to distinguish from each other. [3] This will be demonstrated in this project through the use of various Visualisation techniques. We will aslo show using the Cumulative Distribution Fucntion (CDF) how an initial simple model with fairly high accuracy can be created through initial Exploratory Data Analysis [5] [6]. 

## How to Run and Python Libaries used

### Instructions: How to Run
* software used
* how to run
* python version

### Pandas
* note on pandas

### matplotlib
* note on matplotlib

### Numpy
* note on numpy

### Seaborn
* note on seanborn 

## Importing the Irish Data Set 

### Source of Data

The dataset used in this project was downloaded from the UCI Machine Learning Repository website [3]. Once downloaded it was added to my Github Repsository. Using the Pandas libary in Python a number of checks were conducted to sense check the version of the imported iris data. [7]

#### Fig 1
![Pic of Raw Data](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/iris_raw_data.png)

We can see from Fig 1 that heading needed to be added to this data source. The columns were given the names : sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'.

```python
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
```
### Overview of Data

In researching the dataset, it is undertood that their is 150 rows of data. The variable measurements are in CM and there is three variants (species) of Iris in the dataset. 

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
#### Fig 2
! [Dataset Overview](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/iris_dataset_overview.png)

Through this overview, a good understanding of the actual dataset can be obtained. The first and last 5 rows, will gve a useful look of what a row contains. The shape of the dataset being 150 ros and 5 columns matches what was gathered during researching the data. 

The datatypes are also an important element of the dataset to understand. Here we see the four different variables as float numbers and the species a string value. There was also no null values in this dataset.

Understanding each element of this gave me confidence that the dataset downloaded for the project was of good integrity.

One further check was running the pandas.describe function. The results from this were compared with other summarries found online. There were no discrepencies found in any of the datasets used in the comparison [8] [9].

#### Fig 3
![Summary Stats](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/Iris_summary.png)

## Summary Statistics

https://www.tablesgenerator.com/markdown_tables

### Overall Summary Stats

Overall Summary Stats      	|              	|             	|              	|             	|
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

* comment 1
* comment 2

### Summary of each Variable by Species Type

#### Sepal Length

| Sepal Length Summary Stats    |              	             
|----------------------------	|--------------	|-------------	|--------------	|
| Stats Type                 	| Setosa       	| Versicolor  	| Virginica    	|             	
| count                      	| 50.0         	| 50.0        	| 50.0         	|             	
| mean                       	| 5.01         	| 5.94        	| 6.59         	|             	
| std                        	| 0.35         	| 0.52        	| 0.64         	|             	
| min                        	| 4.3          	| 4.9         	| 4.9          	|             	
| 25%                        	| 4.8          	| 5.6         	| 6.22         	|             	
| 50%                        	| 5.0          	| 5.9         	| 6.5          	|             	
| 75%                        	| 5.2          	| 6.3         	| 6.9          	|             	
| max                        	| 5.8          	| 7.0         	| 7.9          	|             	

#### Range 
| Range                      	|            	         	
|----------------------------	|--------------	|
| Sepal Length               	|              	|
| Iris-setosa                	| 1.5          	|             	
| Iris-versicolor            	| 2.1          	|             	
| Iris-virginica             	| 3.0          	|

* comment 1
* comment 2

#### Sepal Width

 Sepal Width Summary Stats  	|              	
|----------------------------	|--------------	|-------------	|--------------	|
| Stats Type                 	| Setosa       	| Versicolor  	| Virginica    	|             	
| count                      	| 50.0         	| 50.0        	| 50.0         	|             	
| mean                       	| 3.42         	| 2.77        	| 2.97         	|             	
| std                        	| 0.38         	| 0.31        	| 0.32         	|             	
| min                        	| 2.3          	| 2.0         	| 2.2          	|             	
| 25%                        	| 3.12         	| 2.52        	| 2.8          	|             	
| 50%                        	| 3.4          	| 2.8         	| 3.0          	|             	
| 75%                        	| 3.68         	| 3.0         	| 3.18         	|             	
| max                        	| 4.4          	| 3.4         	| 3.8          	|             	

* comment 1
* comment 2

#### Range

| Range                      	|              
|----------------------------	|--------------	|
| Sepal Width                	|              	|             	
| Iris-setosa                	| 2.1          	|             	
| Iris-versicolor            	| 1.4          	|             
| Iris-virginica             	| 1.6          	|             	
 
* comment 1
* comment 2

#### Petal Length

| Petal Length Summary Stats 	|              
|----------------------------	|--------------	|-------------	|--------------	|
| Stats Type                 	| Setosa       	| Versicolor  	| Virginica    	|             
| count                      	| 50.0         	| 50.0        	| 50.0         	|             	
| mean                       	| 1.46         	| 4.26        	| 5.55         	|             	
| std                        	| 0.17         	| 0.47        	| 0.55         	|             	
| min                        	| 1.0          	| 3.0         	| 4.5          	|             	
| 25%                        	| 1.4          	| 4.0         	| 5.1          	|             	
| 50%                        	| 1.5          	| 4.35        	| 5.55         	|             	
| 75%                        	| 1.58         	| 4.6         	| 5.88         	|             	
| max                        	| 1.9          	| 5.1         	| 6.9          	|             	

* comment 1
* comment 2

#### Range

| Range                      	|              	           	              	             	
|----------------------------	|--------------	|
| Petal Length               	|              	|             	          	
| Iris-setosa                	| 0.9          	|                     	
| Iris-versicolor            	| 2.1          	|             	        	
| Iris-virginica             	| 2.4          	|             	        	

* comment 1
* comment 2

#### Petal Width

| Petal Width Summary Stats  	|                         	
| Stats Type                 	| Setosa       	| Versicolor  	| Virginica    	|             	
|----------------------------	|--------------	|-------------	|--------------	|
| count                      	| 50.0         	| 50.0        	| 50.0         	|             	
| mean                       	| 0.24         	| 1.33        	| 2.03         	|             	
| std                        	| 0.11         	| 0.2         	| 0.27         	|             	
| min                        	| 0.1          	| 1.0         	| 1.4          	|             	
| 25%                        	| 0.2          	| 1.2         	| 1.8          	|             	
| 50%                        	| 0.2          	| 1.3         	| 2.0          	|             	
| 75%                        	| 0.3          	| 1.5         	| 2.3          	|             	
| max                        	| 0.6          	| 1.8         	| 2.5          	|             	

* comment 1
* comment 2

#### Range
| Range                      	|              	             	
|----------------------------	|--------------	|
| Petal Width                	|              	|             	              	             	
| Iris-setosa                	| 0.5          	|             	              	             	
| Iris-versicolor            	| 0.8          	|             	              	             	
| Iris-virginica             	| 1.1          	|

* comment
* comment

#### Correlation
|Correlation                	|              	  
|----------------------------	|--------------	|
| Variable                   	| Sepal Length 	| Sepal Width 	| Petal Length 	| Petal Width 	|
| sepal_length               	| 1.0          	| -0.11       	| 0.87         	| 0.82        	|
| sepal_width                	| -0.11        	| 1.0         	| -0.42        	| -0.36       	|
| petal_length               	| 0.87         	| -0.42       	| 1.0          	| 0.96        	|
| petal_width                	| 0.82         	| -0.36       	| 0.96         	| 1.0         	|

PAIRPLOT
* comments

HEATMAP
* comments

SEPAL WIDTH SEPLAL LENGTH SCATTTER
* comments

PETAL WIDTH LENGTH SCATTER
* comments

HISTOGRAMS
* comments

CDF PDF GRAPHS
* comments

### References

1. https://en.wikipedia.org/wiki/Iris_flower_data_set
2. https://towardsdatascience.com/an-introduction-to-multivariate-data-analysis-ece93ceb1ed3
3. https://archive.ics.uci.edu/ml/datasets/iris
4. https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
5. https://towardsdatascience.com/what-why-and-how-to-read-empirical-cdf-123e2b922480
6. https://www.kaggle.com/playingmyway/eda-of-iris-dataset
7. https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
8. https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e
9. https://www.researchgate.net/figure/Example-summary-statistics-for-the-Iris-data_fig4_26387272



### Figures

1. Raw Data
2. Dataset overiew

