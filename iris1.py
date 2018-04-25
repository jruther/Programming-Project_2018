# Justin Rutherford 10.4.18
# running some investigations on the Iris data set

import numpy

# Read data file into array (source = Stackoverflow adopted from Lecture 10)
data = numpy.genfromtxt('data/Iris.csv', delimiter=',')

# The 1st column is the sepal lenght measured in cm's for all 3 classes of Iris flower
sepal_lenght = data[:, 0]

print("The minimum sepal lenght in cm is:", numpy.min(sepal_lenght))
print("The maximum sepal lenght in cm is:",numpy.max(sepal_lenght))
print("The mean sepal lenght in cm is:", numpy.mean(sepal_lenght))
print("The median sepal lenght in cm is:", numpy.median(sepal_lenght))

# The 2nd column is the sepal width measured in cm's for all 3 classes of Iris flower
sepal_width = data[:, 1] # This determines the range of data for Sepal Width 

print("The minimum sepal width in cm is:", numpy.min(sepal_width))
print("The maximum sepal width in cm is:", numpy.max(sepal_width))
print("The mean sepal width in cm is:", numpy.mean(sepal_width))
print("The median sepal width in cm is:", numpy.median(sepal_width))

# The 3rd column is the petal lenght measured in cm's for all 3 classes of Iris flower
petal_length = data[:, 2] # This determines the range of data for petal length.

print("The minimum petal length in cm is:", numpy.min(petal_length))
print("The maximum petal length in cm is:", numpy.max(petal_length))
print("The mean petal length in cm is:", numpy.mean(petal_length))
print("The median petal length in cm is:", numpy.median(petal_length))

# The 4th column is the petal width measured in cm's for all 3 classses of Iris flower.
petal_width = data[:, 3]

print("The minimum petal width in cm is:", numpy.min(petal_width))
print("The maximum petal width in cm is:", numpy.max(petal_width))
print("The mean petal width in cm is:", numpy.mean(petal_width))
print("The median petal width in cm is:", numpy.median(petal_width))

# Now we have the comprehensive range of values for the Iris Class, lets look at differenct species. 
# We know from our research (https://en.wikipedia.org/wiki/Iris_flower_data_set) we know that we have 3 species of Iris with 50 samples in each.

# Let's compare the sepal length of the various species 
sepal_length_setosa = data[:50, 0]
sepal_length_versicolor = data[51:100, 0]
sepal_lenght_virginica = data[101:, 0]

print("The minimum setosa sepal lenght in cm is:", numpy.min(sepal_length_setosa))
print("The maximum setosa sepal lenght in cm is:",numpy.max(sepal_length_setosa))
print("The mean setosa sepal lenght in cm is:", numpy.mean(sepal_length_setosa))
print("The median setosa sepal lenght in cm is:", numpy.median(sepal_length_setosa))

print("The minimum versicolor sepal lenght in cm is:", numpy.min(sepal_length_versicolor))
print("The maximum versicolor sepal lenght in cm is:",numpy.max(sepal_length_versicolor))
print("The mean versicolor sepal lenght in cm is:", numpy.mean(sepal_length_versicolor))
print("The median versicolor sepal lenght in cm is:", numpy.median(sepal_length_versicolor))

print("The minimum virginica sepal lenght in cm is:", numpy.min(sepal_lenght_virginica))
print("The maximum virginica sepal lenght in cm is:",numpy.max(sepal_lenght_virginica))
print("The mean virginica sepal lenght in cm is:", numpy.mean(sepal_lenght_virginica))
print("The median virginica sepal lenght in cm is:", numpy.median(sepal_lenght_virginica))


# Let's compare the sepal width of the various species 
sepal_width_setosa = data[:50, 1]
sepal_width_versicolor = data[51:100, 1]
sepal_width_virginica = data[101:, 1]

print("The minimum setosa sepal width in cm is:", numpy.min(sepal_width_setosa))
print("The maximum setosa sepal width in cm is:",numpy.max(sepal_width_setosa))
print("The mean setosa sepal width in cm is:", numpy.mean(sepal_width_setosa))
print("The median setosa sepal width in cm is:", numpy.median(sepal_width_setosa))

print("The minimum versicolor sepal width in cm is:", numpy.min(sepal_width_versicolor))
print("The maximum versicolor sepal width in cm is:",numpy.max(sepal_width_versicolor))
print("The mean versicolor sepal width in cm is:", numpy.mean(sepal_width_versicolor))
print("The median versicolor sepal width in cm is:", numpy.median(sepal_width_versicolor))

print("The minimum virginica sepal width in cm is:", numpy.min(sepal_width_virginica))
print("The maximum virginica sepal width in cm is:",numpy.max(sepal_width_virginica))
print("The mean virginica sepal width in cm is:", numpy.mean(sepal_width_virginica))
print("The median virginica sepal width in cm is:", numpy.median(sepal_width_virginica))

# Let's compare the petal lenght of the various species
petal_length_setosa = data[:50, 2]
petal_length_versicolor = data[51:100,2]
petal_length_virginica = data[101:, 2]

print("The minimum setosa petal lenght in cm is:", numpy.min(petal_length_setosa))
print("The maximum setosa petal lenght in cm is:",numpy.max(petal_length_setosa))
print("The mean setosa petal lenght in cm is:", numpy.mean(petal_length_setosa))
print("The median setosa petal lenght in cm is:", numpy.median(petal_length_setosa))

print("The minimum versicolor petal lenght in cm is:", numpy.min(petal_length_versicolor))
print("The maximum versicolor petal lenght in cm is:",numpy.max(petal_length_versicolor))
print("The mean versicolor petal lenght in cm is:", numpy.mean(petal_length_versicolor))
print("The median versicolor petal lenght in cm is:", numpy.median(petal_length_versicolor))

print("The minimum virginica petal lenght in cm is:", numpy.min(petal_length_virginica))
print("The maximum virginica petal lenght in cm is:",numpy.max(petal_length_virginica))
print("The mean virginica petal lenght in cm is:", numpy.mean(petal_length_virginica))
print("The median virginica petal lenght in cm is:", numpy.median(petal_length_virginica))

# And finally lets compare the petal width of the various species
petal_width_setosa = data[:50, 3]
petal_width_versicolor = data[51:100, 3]
petal_width_virginica = data[101:, 3]

print("The minimum setosa petal width in cm is:", numpy.min(petal_width_setosa))
print("The maximum setosa petal width in cm is:",numpy.max(petal_width_setosa))
print("The mean setosa petal width in cm is:", numpy.mean(petal_width_setosa))
print("The median setosa petal width in cm is:", numpy.median(petal_width_setosa))

print("The minimum versicolor petal width in cm is:", numpy.min(petal_width_versicolor))
print("The maximum versicolor petal width in cm is:",numpy.max(petal_width_versicolor))
print("The mean versicolor petal width in cm is:", numpy.mean(petal_width_versicolor))
print("The median versicolor petal width in cm is:", numpy.median(petal_width_versicolor))

print("The minimum virginica petal width in cm is:", numpy.min(petal_width_virginica))
print("The maximum virginica petal width in cm is:",numpy.max(petal_width_virginica))
print("The mean virginica petal width in cm is:", numpy.mean(petal_width_virginica))
print("The median virginica petal width in cm is:", numpy.median(petal_width_virginica))

import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris")
iris["ID"] = iris.index
iris["ratio"] = iris["sepal_length"]/iris["sepal_width"]

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False)

plt.legend()
plt.show()

