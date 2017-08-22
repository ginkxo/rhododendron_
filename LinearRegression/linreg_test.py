from statistics import mean
from sys import argv
import numpy as np
import matplotlib.pyplot as pt 
from linreg import *

xs, ys = np.loadtxt(argv[1], delimiter=',', unpack=True)
m,b = best_fit_parameters(xs, ys)

regline = [(m*x)+b for x in xs]

pt.scatter(xs,ys)
pt.plot(xs, regline)
pt.show()


