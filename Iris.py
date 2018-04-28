# Justin Rutherford 30.3.18
# code extracted from comment by OILBHE DASZYNSKA - Sunday, 4 March 2018, 9:27 PM
#Re: Wk5 Exercise

names = ('Sepal-Length', 'Sepal-Width', 'Petal-Length', 'Petal-Width', 'Class')
print(names)

with open("data/iris.csv") as f:
  total = 0
  for line in f:
    print('{:10} {:10} {:10} {:10} {:10}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3], line.split(',')[4]))


