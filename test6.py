# The file does not contain a naming scheme so we identify the columns as follows; 
names = ('sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class')

import numpy #NumPy is the fundamental package for scientific computing with Python. 

# Read data file into array (source = Stackoverflow adopted from Lecture 10)
data = numpy.genfromtxt('data/Iris.csv', delimiter=',')

print(names)
print(data) 


