# Justin Rutherford 10.4.18
# running some investigations on the Iris data set using NumPy


import numpy #NumPy is the fundamental package for scientific computing with Python. 

# Read data file into array (source = Stackoverflow adopted from Lecture 10)
data = numpy.genfromtxt('data/Iris.csv', delimiter=',')

# We initially investigate the parameters/metadata adapting code obtained from the following site;
#https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
print()

# What is the size of the datset?
print("The size of the file is:", data.size)
print()

# what are the dimensions of the dataset (instances and attributes?)
print("The number of rows and columns in the files is:", data.shape)
print()

# Define the column data by name
print("The first column contains the sepal length in cm's")
print("The second column contains the sepal width in cm's")
print("The third column contains the petal length in cm's")
print("The fourth column contains the petal width in cm's")
print("The fifth column contains the species type in cm's")
print()

# Define the rows by reference to the species type
print("Rows 1 to 50 refer to Iris Setosa samples")
print("Rows 51 to 100 refer to Iris Versicolor samples")
print ("Rows 101 to 150 refer to Irish Virginica samples")
print()

# The 1st column is the sepal length measured in cm's for all 3 classes of Iris flower
sepal_length = data[:, 0]

print("The minimum sepal length in cm is:", numpy.min(sepal_length))
print("The maximum sepal length in cm is:",numpy.max(sepal_length))
print("The mean sepal length in cm is:", numpy.mean(sepal_length))
print("The median sepal length in cm is:", numpy.median(sepal_length))
print()

# The 2nd column is the sepal width measured in cm's for all 3 classes of Iris flower
sepal_width = data[:, 1] # This determines the range of data for Sepal Width 

print("The minimum sepal width in cm is:", numpy.min(sepal_width))
print("The maximum sepal width in cm is:", numpy.max(sepal_width))
print("The mean sepal width in cm is:", numpy.mean(sepal_width))
print("The median sepal width in cm is:", numpy.median(sepal_width))
print()

# The 3rd column is the petal length measured in cm's for all 3 classes of Iris flower
petal_length = data[:, 2] # This determines the range of data for petal length.

print("The minimum petal length in cm is:", numpy.min(petal_length))
print("The maximum petal length in cm is:", numpy.max(petal_length))
print("The mean petal length in cm is:", numpy.mean(petal_length))
print("The median petal length in cm is:", numpy.median(petal_length))
print()

# The 4th column is the petal width measured in cm's for all 3 classses of Iris flower.
petal_width = data[:, 3]

print("The minimum petal width in cm is:", numpy.min(petal_width))
print("The maximum petal width in cm is:", numpy.max(petal_width))
print("The mean petal width in cm is:", numpy.mean(petal_width))
print("The median petal width in cm is:", numpy.median(petal_width))
print()

# Now we have the comprehensive range of values for the Iris Class, lets look at differenct species. 
# We know from our research (https://en.wikipedia.org/wiki/Iris_flower_data_set) we know that we have 3 species of Iris with 50 samples in each.

# Let's compare the sepal length of the various species 
sepal_length_setosa = data[:50, 0]
sepal_length_versicolor = data[51:100, 0]
sepal_length_virginica = data[101:, 0]

print("The minimum setosa sepal lenght in cm is:", numpy.min(sepal_length_setosa))
print("The maximum setosa sepal lenght in cm is:",numpy.max(sepal_length_setosa))
print("The mean setosa sepal lenght in cm is:", numpy.mean(sepal_length_setosa))
print("The median setosa sepal lenght in cm is:", numpy.median(sepal_length_setosa))
print()

print("The minimum versicolor sepal length in cm is:", numpy.min(sepal_length_versicolor))
print("The maximum versicolor sepal length in cm is:",numpy.max(sepal_length_versicolor))
print("The mean versicolor sepal length in cm is:", numpy.mean(sepal_length_versicolor))
print("The median versicolor sepal lenght in cm is:", numpy.median(sepal_length_versicolor))
print()

print("The minimum virginica sepal length in cm is:", numpy.min(sepal_length_virginica))
print("The maximum virginica sepal length in cm is:",numpy.max(sepal_length_virginica))
print("The mean virginica sepal length in cm is:", numpy.mean(sepal_length_virginica))
print("The median virginica sepal length in cm is:", numpy.median(sepal_length_virginica))
print()

# Let's compare the sepal width of the various species 
sepal_width_setosa = data[:50, 1]
sepal_width_versicolor = data[51:100, 1]
sepal_width_virginica = data[101:, 1]

print("The minimum setosa sepal width in cm is:", numpy.min(sepal_width_setosa))
print("The maximum setosa sepal width in cm is:",numpy.max(sepal_width_setosa))
print("The mean setosa sepal width in cm is:", numpy.mean(sepal_width_setosa))
print("The median setosa sepal width in cm is:", numpy.median(sepal_width_setosa))
print()

print("The minimum versicolor sepal width in cm is:", numpy.min(sepal_width_versicolor))
print("The maximum versicolor sepal width in cm is:",numpy.max(sepal_width_versicolor))
print("The mean versicolor sepal width in cm is:", numpy.mean(sepal_width_versicolor))
print("The median versicolor sepal width in cm is:", numpy.median(sepal_width_versicolor))
print()

print("The minimum virginica sepal width in cm is:", numpy.min(sepal_width_virginica))
print("The maximum virginica sepal width in cm is:",numpy.max(sepal_width_virginica))
print("The mean virginica sepal width in cm is:", numpy.mean(sepal_width_virginica))
print("The median virginica sepal width in cm is:", numpy.median(sepal_width_virginica))
print()

# Let's compare the petal lenght of the various species
petal_length_setosa = data[:50, 2]
petal_length_versicolor = data[51:100,2]
petal_length_virginica = data[101:, 2]

print("The minimum setosa petal length in cm is:", numpy.min(petal_length_setosa))
print("The maximum setosa petal length in cm is:",numpy.max(petal_length_setosa))
print("The mean setosa petal length in cm is:", numpy.mean(petal_length_setosa))
print("The median setosa petal length in cm is:", numpy.median(petal_length_setosa))
print()

print("The minimum versicolor petal length in cm is:", numpy.min(petal_length_versicolor))
print("The maximum versicolor petal length in cm is:",numpy.max(petal_length_versicolor))
print("The mean versicolor petal length in cm is:", numpy.mean(petal_length_versicolor))
print("The median versicolor petal length in cm is:", numpy.median(petal_length_versicolor))
print()

print("The minimum virginica petal length in cm is:", numpy.min(petal_length_virginica))
print("The maximum virginica petal length in cm is:",numpy.max(petal_length_virginica))
print("The mean virginica petal length in cm is:", numpy.mean(petal_length_virginica))
print("The median virginica petal length in cm is:", numpy.median(petal_length_virginica))
print()

# And finally lets compare the petal width of the various species
petal_width_setosa = data[:50, 3]
petal_width_versicolor = data[51:100, 3]
petal_width_virginica = data[101:, 3]

print("The minimum setosa petal width in cm is:", numpy.min(petal_width_setosa))
print("The maximum setosa petal width in cm is:",numpy.max(petal_width_setosa))
print("The mean setosa petal width in cm is:", numpy.mean(petal_width_setosa))
print("The median setosa petal width in cm is:", numpy.median(petal_width_setosa))
print()

print("The minimum versicolor petal width in cm is:", numpy.min(petal_width_versicolor))
print("The maximum versicolor petal width in cm is:",numpy.max(petal_width_versicolor))
print("The mean versicolor petal width in cm is:", numpy.mean(petal_width_versicolor))
print("The median versicolor petal width in cm is:", numpy.median(petal_width_versicolor))
print()

print("The minimum virginica petal width in cm is:", numpy.min(petal_width_virginica))
print("The maximum virginica petal width in cm is:",numpy.max(petal_width_virginica))
print("The mean virginica petal width in cm is:", numpy.mean(petal_width_virginica))
print("The median virginica petal width in cm is:", numpy.median(petal_width_virginica))
print()
print("I maybe guilty of 'overanalysis' in this report....!")
print()

