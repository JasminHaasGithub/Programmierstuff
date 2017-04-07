import numpy as np
import matplotlib.pyplot as pl

xs = np.linspace(0, 7, 300)
ys = [ x*x for x in xs]

pl.plot(xs, ys)
pl.show()
