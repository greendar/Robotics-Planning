from methods import *

f = open('Expectations.csv', 'r')

expList = []

for line in f:
    a = line.split(',')
    a[-1] = a[-1][:-1]   #clean a \n from end of each line
    expList.append(Expectation(a[0], a[1], a[2], a[3], a[4], a[5]))

for exp in expList:
    print(exp)
