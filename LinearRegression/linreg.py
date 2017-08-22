from statistics import mean
import numpy as np

def best_fit_parameters(x,y):
		m = ((mean(x)*mean(y)) - mean(x*y)) / ((mean(x)*mean(x)) - mean(x*x))
		b = mean(y) - m*mean(x)
		return m,b


