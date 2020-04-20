# Iris_Project_2020
Programming and Scripting Module Final Project

### Objectives of Project
1.	Research background information about the data and write a summary
2.	Download Data and import into Github
3.	Programming Language used and libraries to be used in project
4.	Summarise the Data
5.	Histogram of each variable
6.	Scatter plot of each variable
7.	Summary of overall analysis
8.	References


## 1.	Research the Data
*	Who did research, where it was done, when etc. 
*   Type of dataset -  multi variable
*	What is in the data – variables, measurments in cm, size of data set
*	Write summary about dataset
*	References
*   REVIEW AND ADD MORE INFO ON LINEAR LDA

## 2.	Iris Dataset
*	Download into github
*	Data checks Rows, Data types, empty values ,count of variables etc. –script
*	References
*   COMPLETED - CLEAN UP CODE AND REFERENCES
*   README SECTION TO BE ADDED

## 3.	Python Libaries
*	List of libraries to be used
*	Software used 
*	Summary (why they were used features)
*	Data Check –script
*	References

## 4.	Summarise Data
*	Descriptive summary of data (Pandas) –script (function with argument)?
*	Max mean min range for data, outliers boxplot?
*	Summarise all 
*	Summarise each variable – variable for each group script
*	Append to text file summary – out put redirection script
*   COMPLETE - FOR REVIEW AND FURTHER CLEAN UP, REFERENCES ETC.
*   README SECTION TO BE ADDED

## 5.	Histograms
*	Save Histogram of each variable to png – script
*	Overlap Histograms to show frequency of each variable – script
*	References
*   SAMPLE CODE CREATED - ONGOING


## 6.	Scatter plots
*	Scatter plots for each variable – script
*	Sepal Width v sepal length
*	Petal width v petal length
*	Pair plot? Might use as part of summary
*	References
*   SAME CODE CREATED - ONGOING

## 7.   CDF
*   Graph CDF of each variable by secies
*   Example of model
*   CDF smmary table Petal Width v Petal Length
*   CDF explanation


## 8.	References
*	Appendix of each ref with num
*   Links to references

### Background information on the Data
(what is the data, who collected it, how it was collected, uses today?)

## Overview of Irish Data Set
The Iris data set  is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. [1]

![Iris Flower](https://github.com/conor1982/Iris_Project_2020/blob/master/iris.png)

It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”. [1] [4]

Multivariate (Data analysis) refers to any statistical technique used to analyze data which arises from more than one variable. 

Multivariate data analysis is a set of statistical models that examine patterns in multidimensional data by considering, at once, several data variables. It is an expansion of bivariate data analysis, which considers only two variables in its models. As multivariate models consider more variables, they can examine more complex phenomena and find data patterns that more accurately represent the real world. [2]

## Summary of Data
The data classifies three variants of the Iris flower based on certain attributes. The three variants of Iris flower found in the dataset are: [3]
    
    1 Iris Setosa
    2 Iris Versicolour
    3 Irish Virginica

![Iris Variants](https://github.com/conor1982/Iris_Project_2020/blob/master/variants.png)

For each variant, data was gathered based on four different attributes: [2]

    1 Sepal Length (in cm)
    2 Sepal Width (in cm)
    3 Petal Length (in cm)
    4 Petal Width (in cm)

The dataset contains a set of 150 records. Each row in the table represents one Iris flower with a measurement of each attribute above and its relative variant.

There are 50 different data points for each variant of Iris. With the complete dataset containing only 150 observations, it is a very popular dataset in teaching and study. It contains real data of good quality which is viewed more favourably than using test data for instance.

Previous studies on the data set show that Iris Setosa is easily seperable from the other two linearly. There is some overlap between the other two making it more difficult to distinguish from each other. [3] This will be demonstrated in this project through the use of various Visualisation techniques. We will aslo show using the Cumulative Distribution Fucntion (CDF) how an initial simple model with fairly high accuracy can be created through initial Exploratory Data Analysis [5] [6]. 


### Importing the Irish Data Set 

## Source of Data

The dataset used in this project was downloaded from the UCI Machine Learning Repository website [3]. Once downloaded it was added to my Github Repsository. Using the Pandas libary in Python a number of checks were conducted to sense check the version of the imported iris data. [7]

# Fig 1
![Pic of Raw Data](https://github.com/conor1982/Iris_Project_2020/blob/master/Screenshots/iris_raw_data.png)

We can see from Fig 1 that heading needed to be added to this data source. The columns were given the names : sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'.

```python
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']




### References

1. https://en.wikipedia.org/wiki/Iris_flower_data_set
2. https://towardsdatascience.com/an-introduction-to-multivariate-data-analysis-ece93ceb1ed3
3. https://archive.ics.uci.edu/ml/datasets/iris
4. https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
5. https://towardsdatascience.com/what-why-and-how-to-read-empirical-cdf-123e2b922480
6. https://www.kaggle.com/playingmyway/eda-of-iris-dataset
7. https://pandas.pydata.org/pandas-docs/stable/reference/frame.html


### Figures

1. Raw Data 