# Justin Rutherford 10.4.18
# running some investigations on the Iris data set

import numpy

# Read data file into array (source = Stackoverflow via lecture)
data = numpy.genfromtxt('data/Iris.csv', delimiter=',')

firstcol = data[:, 0]
seccol = data[:, 1]
thirdcol = data[:, 2]
fourthcol = data[:, 3]


print(firstcol)
print(numpy.min(firstcol))
import matplotlib.pyplot as mp
mp.hist(firstcol)
mp.show()







