import pandas
import matplotlib.pyplot as plt

# pandas
iris = pandas.read_csv('iris.csv')
x = iris.loc[:,'petal.length']
y = iris.loc[:,'petal.width']
lab = iris.loc[:,'variety']

# matplotlib
plt.scatter(x[lab == 'Setosa'], y[lab == 'Setosa'], color = 'g', label = 'Setosa')
plt.scatter(x[lab == 'Virginica'], y[lab == 'Virginica'], color = 'r', label = 'Virginica')
plt.scatter(x[lab == 'Versicolor'], y[lab == 'Versicolor'], color = 'b', label = 'Versicolor')


plt.legend()
plt.show()



