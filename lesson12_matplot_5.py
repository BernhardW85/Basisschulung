import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(100, 15, 200)

print(x)

plt.hist(x)
plt.show()