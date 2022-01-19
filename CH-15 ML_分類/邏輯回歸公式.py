
import numpy as np
import matplotlib.pyplot as mt

t = np.arange(-6, 6, 0.1)
S = 1/(1+(np.e**(-t)))

mt.plot(t,S)
mt.show()