import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([10, 5, 9, 10])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([12, 6, 10, 9])

x3 = np.array(['A', 'B', 'C', 'D'])
y3 = np.array([10, 5, 9, 10])

x4 = np.array([0, 1, 2, 3])
y4 = np.array([12, 6, 10, 9])
labels = ['Kunde A', 'Kunde B', 'Kunde C', 'Kunde D']
special = [0.1, 0, 0, 0]
customer_color = ['c', 'black', '#4ACF50', 'lime']


plt.subplot(2, 2, 1)
plt.plot(x1, y1)

plt.subplot(2, 2, 2)
plt.plot(x2, y2)

plt.subplot(2, 2, 3)
plt.bar(x3, y3, width=0.5) #barh

plt.subplot(2, 2, 4)
#plt.plot(x4, y4)
plt.pie(y4, labels=labels, explode=special, shadow=True, colors=customer_color)

plt.show()
