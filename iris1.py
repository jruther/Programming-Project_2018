# Justin Rutherford 10.4.18
# running some investigations on the Iris data set

import numpy

# Read data file into array
data = numpy.genfromtxt('data/Iris.csv', delimiter=',')

firstcol = data[:, 0]
seccol = data[:,1]

print(firstcol)
print(numpy.min(firstcol))
import matplotlib.pyplot as mp
mp.hist(firstcol)
mp.show()

sepallengthsetosa = data[:51,0]
print(sepallengthsetosa)

slv = data[51:101,0]







