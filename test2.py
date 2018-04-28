#https://gist.github.com/jobliz/2903500

import matplotlib
import matplotlib.pyplot as plt

# Iris petal length/width scatterplot (greatest class correlation)
# Dataset: http://archive.ics.uci.edu/ml/datasets/Iris
# Output: https://imgur.com/9TWhn

def data():
    lists = [line.strip().split(",") for line in open('Data/Iris.csv', 'r').readlines()]
    return [map(float, l[:4]) for l in lists], [l[-1] for l in lists]

def listrow(lst, n):
    result = []
    for l in lst:
        result.append(l[n])
    return result

matrix, labels = data()
xcord1 = []; ycord1 = []
xcord2 = []; ycord2 = []
xcord3 = []; ycord3 = []
x = 2 # petal length
y = 3 # petal width

for n, elem in enumerate(matrix):
  if labels[n] == 'Iris-setosa':
    xcord1.append(matrix[n][x])
    ycord1.append(matrix[n][y])
  elif labels[n] == 'Iris-versicolor':
    xcord2.append(matrix[n][x])
    ycord2.append(matrix[n][y])
  elif labels[n] == 'Iris-virginica':
    xcord3.append(matrix[n][x])
    ycord3.append(matrix[n][y])

fig = plt.figure()
ax = fig.add_subplot(111)
type1 = ax.scatter(xcord1, ycord1, s=50, c='red')
type2 = ax.scatter(xcord2, ycord2, s=50, c='green')
type3 = ax.scatter(xcord3, ycord3, s=50, c='blue')

ax.set_title('Petal size from Iris dataset', fontsize=14)
ax.set_xlabel('Petal length (cm)')
ax.set_ylabel('Petal width (cm)')
ax.legend([type1, type2, type3], ["Iris Setosa", "Iris Versicolor", "Iris Virginica"], loc=2)

ax.grid(True,linestyle='-',color='0.75')

plt.show()
