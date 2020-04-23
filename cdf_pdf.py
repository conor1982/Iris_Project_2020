#Conor O'Riordan
#Overalp to see how many varibales ovrlap into another
#petal width petal length
#% table
#post histogrm and scatter analysis
#basic model


#Pandas libary import
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#command line prompt??
#header = None added to not have first row as heading
df = pd.read_csv('irisdata.csv', header=None)

#setosa petal_length
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# ref https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
# ref https://medium.com/@rishav.jnit/exploratory-data-analysis-eda-on-iris-dataset-using-python-cadd850c1fc6
# ref https://docs.scipy.org/doc/numpy/reference/generated/numpy.count_nonzero.html


def overlap(variant,variable):
    x=df[df['species']==variant]
    y = np.array(x[variable])
    return y

#petal lengths
versi_pl = overlap('Iris-versicolor','petal_length')
set_pl =overlap('Iris-setosa','petal_length')
vir_pl = overlap('Iris-virginica','petal_length')

#parameters based on Histogram Analysis
#model parameters to return % accuracy
print('Univariate Analysis of Petal Length based on Histograms Observations')

max_set_pl = 2.1
max_versi_pl = 4.8
max_vir_pl = 4.8



setosa_pred = np.count_nonzero(set_pl[:]<max_set_pl)
print("Applying {} as the maximum petal length to identify a Setosa Flower predicts {} Setosas".format(max_set_pl,setosa_pred))

versicolor_pred = np.count_nonzero(versi_pl[:]<max_versi_pl)
print("Applying {} as the maximum petal length to identify a Versicolor Flower predicts {} Versicolors".format(max_versi_pl,versicolor_pred))

virginica_pred = np.count_nonzero(vir_pl[:]>=max_vir_pl)
print("Applying {} as the minimum petal length to identify a Viriginica Flower would predicts {} Virginicas".format(max_vir_pl,virginica_pred))

set_pl_pdf = set_pl/sum(set_pl) 
set_pl_cdf = np.cumsum(set_pl_pdf)

versi_pl_pdf = versi_pl/sum(versi_pl) 
versi_pl_cdf = np.cumsum(versi_pl_pdf)

vir_pl_pdf = vir_pl/sum(vir_pl) 
vir_pl_cdf = np.cumsum(vir_pl_pdf)

#ref https://www.kaggle.com/playingmyway/eda-of-iris-dataset


def cdf_pdf(variant,variable):
    x=df[df['species']==variant]
    graph = counts, bin_edges= np.histogram(x[variable],bins=10, density= True)
    pdf=counts/(sum(counts))
    cdf=np.cumsum(pdf)
    plt.plot(bin_edges[1:],pdf, label='{} PDF'.format(variant))
    plt.plot(bin_edges[1:],cdf, label=' {} CDF'.format(variant))
    plt.grid()
    plt.legend(loc =0)
    plt.savefig('CDF and PDF')
    return graph
    
#set_pl_cdf_pdf = cdf_pdf('Iris-setosa','petal_length')
#ver_pl_cdf_pdf = cdf_pdf('Iris-versicolor','petal_length')
#vir_pl_cdf_pdf = cdf_pdf('Iris-virginica','petal_length')


print('\nModel of Petal Length based on PDF and CDF Observations')

cdf_set_pred = 1.9
cdf_vir_versi_sep = 5

Pred = []


for row in df['petal_length']:
    
    if row <= cdf_set_pred:
       Pred.append("Predicted Setosa")
    elif row>cdf_set_pred and row <cdf_vir_versi_sep:
        Pred.append('Predicted Versicolor')
    elif row>=cdf_vir_versi_sep:
        Pred.append('Predicted Virginica')

set_pred =Pred.count('Predicted Setosa')
ver_pred =Pred.count('Predicted Versicolor')
vir_pred =Pred.count('Predicted Virginica')

set_acc = (set_pred-50)/50
ver_acc = (ver_pred-50)/50
vir_acc= (vir_pred-50)/50



print("\nApplying {} as the maximum petal length to identify a Setosa Flower predicts {} Setosas".format(cdf_set_pred,set_pred))
print("Applying {} as the maximum petal length to identify a Versicolor Flower predicts {} Versicolors".format(cdf_vir_versi_sep,ver_pred))
print("Applying {} as the minimum petal length to identify a Viriginca Flower predicts {} Virginicas".format(cdf_vir_versi_sep,vir_pred))

print(set_acc, 'error rate for Setosa')
print(ver_acc, 'error rate for Versicolor')
print(vir_acc, 'error rate for Virginica')


#https://chrisalbon.com/python/data_wrangling/pandas_create_column_with_loop/
