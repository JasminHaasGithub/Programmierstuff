import numpy as np
import matplotlib.pyplot as pl

xs = np.linspace(0, 7, 300)
ys = np.sin(xs)

pl.plot(xs, ys)
pl.show()
