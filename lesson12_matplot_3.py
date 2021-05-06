import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([1, 2, 7, 9])


y2 = np.array([3, 8, 1, 10])

design = {'colour': 'green', 'linewidth': 1.8, 'linestyle': '--'}
plt.plot(y1, linewidth=10.5)
plt.plot(y2)

font1 = {'family': 'serif', 'color': 'blue', 'size': 16}
font2 = {'family': 'serif', 'color': 'brown', 'size': 12}

plt.title('Beispiel für kWh', fontdict=font1)
plt.xlabel('kWh', fontdict=font2)
plt.ylabel('Preis', fontdict=font2)

#plt.grid()
#plt.grid(axis='y', color='green', linewidth=1.8)

plt.grid(axis='y', **design)

plt.show()
