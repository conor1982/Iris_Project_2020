#Conor O'Riordan
#Past4 project plan
#Plots and Hist
#Plot and Hist options


#Pandas libary import
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#command line prompt??
#header = None added to not have first row as heading
df = pd.read_csv('irisdata.csv', header=None)

#Adding column names
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#pairplot
sns.set_style("whitegrid");
sns.pairplot(df,hue="species",height=4);
plt.savefig("Pairplot")

#Hist Function

def makehist(x):
    sns.FacetGrid(df,hue="species",height=6) \
        .map(sns.distplot,x) \
        .add_legend()
    plt.title(x)
    plt.savefig(x)

#plot function
def makeplot(x,y):
    sns.FacetGrid(df,hue='species', height=4)\
        .map(plt.scatter,x,y)\
        .add_legend()
    plt.show()
#ref https://seaborn.pydata.org/tutorial/axis_grids.html
#ref https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e
#ref https://www.kaggle.com/rakesh6184/seaborn-plot-to-visualize-iris-data

#heatmap
plt.figure(figsize=(10,11))
sns.heatmap(df.corr(),annot=True)
plt.plot()
plt.show()

