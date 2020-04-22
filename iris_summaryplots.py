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

#APPEND FROM HERE FOR ANALYSIS.PY

#ref https://seaborn.pydata.org/tutorial/axis_grids.html
#ref https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e
#ref https://www.kaggle.com/rakesh6184/seaborn-plot-to-visualize-iris-data


#PAIRPLOTS
#ref https://seaborn.pydata.org/generated/seaborn.pairplot.html
#pairplot of all

#setting tickmarks and color palatte
sns.set(style = 'ticks', color_codes=True)
#colors for each species type
sns.pairplot(df,hue = 'species')
#save plot name
plt.savefig("Pairplot of Iris Data")

#pairplot petal width and petal length
sns.set(style = 'ticks', color_codes=True)
#plot just returning a pairplot for petal width and petal length
sns.pairplot(df,hue = 'species',vars=['petal_width','petal_length'] )
plt.savefig("Pairplot of Petal Width and Petal Length")

#heatmap
#ref https://seaborn.pydata.org/generated/seaborn.heatmap.html
plt.figure(figsize=(10,11))
#ref https://seaborn.pydata.org/tutorial/color_palettes.html
#heatmap for the df, labels on, line widths adjusted and color palette chosen
sns.heatmap(df.corr(),annot=True, linewidths=.5, cmap='Blues')
#save map as heatmap.png
plt.savefig('Heat Map')
plt.close()

#Hist Function
def makehist(x):
    hist = sns.FacetGrid(df,hue="species",height=6) \
        .map(sns.distplot,x) \
        .add_legend()
    #plt.title(x)
    plt.savefig("Histogram of {}".format(x))
    plt.close()
    return hist

#Scatterplot function
def makeplot(x,y):
    scatter = sns.FacetGrid(df,hue='species', height=4)\
        .map(plt.scatter,x,y)\
        .add_legend()
    plt.savefig("Scatterplot of {} and {}".format(x,y))
    plt.close()
    return scatter


#histogram function calls
sep_len_hist = makehist('sepal_length')
sep_width_hist = makehist('sepal_width')
pet_len_hist = makehist('petal_length')
pet_width_hist =makehist('petal_width')

#scaterplot function calls
scatter_sl_sw = makeplot('sepal_length','sepal_width')
scatter_pl_pw = makeplot('sepal_length','petal_length')
scatter_sl_pw = makeplot('sepal_length','petal_width')
scatter_pl_sw = makeplot('sepal_width','petal_length')
scatter_pl_sw = makeplot('sepal_width','petal_width')
scatter_pl_sw = makeplot('petal_length','petal_width')
