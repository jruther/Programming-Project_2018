# Justin Rutherford 25.4.18
# running some investigations on the Iris data set
# adapted from https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

import numpy

# Read data file into array (source = Stackoverflow adopted from Lecture 10)
data = numpy.genfromtxt('data/Iris.csv', delimiter=',')

# what are the dimensions of the dataset (instances and attributes?)
print(data.shape)

# What is the size of the datset?
print(data.size)


