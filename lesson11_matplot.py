# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)

xpoints = np.array([0, 18])
ypoints = np.array([50, 90])

plt.plot(xpoints, ypoints)

plt.show()

