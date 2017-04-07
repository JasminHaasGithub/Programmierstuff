import numpy as np
import matplotlib.pyplot as pl

h = 0,1
f(x) = x*x
xs = np.linspace(0, 7, 300)
ys = [ (f(x + h) - f(x)) / h
