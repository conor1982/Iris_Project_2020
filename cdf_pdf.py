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

#petal widths
versi_pw = overlap('Iris-versicolor','petal_width')
set_pw =overlap('Iris-setosa','petal_width')
vir_pw = overlap('Iris-virginica','petal_width')

max_set_pw = set_pw.max()
min_set_pw = set_pw.min()

max_versi_pw = versi_pw.max()
min_versi_pw = versi_pw.min()

max_vir_pw = vir_pw.max()
min_vir_pw = vir_pw.min()

set_pw_IN_versi_pw = np.count_nonzero(set_pw[:]>min_versi_pw)/np.count_nonzero(set_pw)
print("The percentage of Setosa Flower Petal Widths overlapping into Versicolor is {:.2%}".format(set_pw_IN_versi_pw))

set_pw_IN_vir_pw = np.count_nonzero(set_pw[:]>min_vir_pw)/np.count_nonzero(set_pw)
print("The percentage of Setosa Flower Petal Widths overlapping into Virginica is {:.2%}".format(set_pw_IN_versi_pw))

ver_pw_IN_vir_pw = np.count_nonzero(versi_pw[:]>min_vir_pw)/np.count_nonzero(versi_pw)
print("The percentage of Versicolor Flower Petal Widths overlapping into Virginica is {:.2%}".format(ver_pw_IN_vir_pw))

vir_pw_IN_ver_pw = np.count_nonzero(vir_pw[:]<max_versi_pw)/np.count_nonzero(vir_pw)
print("The percentage of Virginica Flower Petal Widths overlapping into Versicolor is {:.2%}".format(vir_pw_IN_ver_pw))

set_pw_pdf = set_pw/sum(set_pw) 
set_pw_cdf = np.cumsum(set_pw_pdf)

versi_pw_pdf = versi_pw/sum(versi_pw) 
versi_pw_cdf = np.cumsum(versi_pw_pdf)

vir_pw_pdf = vir_pw/sum(vir_pw) 
vir_pw_cdf = np.cumsum(vir_pw_pdf)


#petal lengthss
versi_pl = overlap('Iris-versicolor','petal_length')
set_pl =overlap('Iris-setosa','petal_length')
vir_pl = overlap('Iris-virginica','petal_length')

max_set_pl = set_pl.max()
min_set_pl = set_pl.min()

max_versi_pl = versi_pl.max()
min_versi_pl = versi_pl.min()

max_vir_pl = vir_pl.max()
min_vir_pl = vir_pl.min()

set_pl_IN_versi_pl = np.count_nonzero(set_pl[:]>min_versi_pl)/np.count_nonzero(set_pl)
print("\nThe percentage of Setosa Flower Petal Lengths overlapping into Versicolor is {:.2%}".format(set_pl_IN_versi_pl))

set_pl_IN_vir_pl = np.count_nonzero(set_pl[:]>min_vir_pl)/np.count_nonzero(set_pl)
print("The percentage of Setosa Flower Petal Lengths overlapping into Virginica is {:.2%}".format(set_pl_IN_versi_pl))

ver_pl_IN_vir_pl = np.count_nonzero(versi_pl[:]>min_vir_pl)/np.count_nonzero(versi_pl)
print("The percentage of Versicolor Flower Petal Lengths overlapping into Virginica is {:.2%}".format(ver_pl_IN_vir_pl))

vir_pl_IN_ver_pl = np.count_nonzero(vir_pl[:]<max_versi_pl)/np.count_nonzero(vir_pl)
print("The percentage of Virginica Flower Petal Widths overlapping into Versicolor is {:.2%}".format(vir_pl_IN_ver_pl))

set_pl_pdf = set_pl/sum(set_pl) 
set_pl_cdf = np.cumsum(set_pl_pdf)

versi_pl_pdf = versi_pl/sum(versi_pl) 
versi_pl_cdf = np.cumsum(versi_pl_pdf)

vir_pl_pdf = vir_pl/sum(vir_pl) 
vir_pl_cdf = np.cumsum(vir_pl_pdf)

#ref https://www.kaggle.com/playingmyway/eda-of-iris-dataset


def cdf_pdf(variant,variable):
    x=df[df['species']==variant]
    counts, bin_edges= np.histogram(x[variable],bins=10, density= True)
    pdf=counts/(sum(counts))
    cdf=np.cumsum(pdf)
    plt.plot(bin_edges[1:],pdf)
    plt.plot(bin_edges[1:],cdf)
    plt.grid()
    
    
set_pl_cdf_pdf = cdf_pdf('Iris-setosa','petal_length')
ver_pl_cdf_pdf = cdf_pdf('Iris-versicolor','petal_length')
vir_pl_cdf_pdf = cdf_pdf('Iris-virginica','petal_length')
plt.show()






