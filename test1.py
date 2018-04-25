# from Stackoverflow
#https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset

import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris")

ratio = iris["petal_length"]/iris["petal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()
