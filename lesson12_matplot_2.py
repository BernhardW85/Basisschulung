import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 3, 6, 9, 14, 24])
ypoints = np.array([3, 8, 1, 10, 5, 8])

#plt.plot(xpoints, ypoints)
#plt.plot(xpoints, ypoints, '+-.g') # '*-y'  'o:m' 'o-.g'
#plt.plot(ypoints)

plt.plot(xpoints, ypoints, 'D', ms=20, mec='g', mfc='#4CAF50')

plt.style

plt.show()

