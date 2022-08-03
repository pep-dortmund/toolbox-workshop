import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.txt", unpack=True)
data2 = np.genfromtxt("data2.txt", unpack=True)
plt.plot(data, data2)
plt.savefig("plot2.pdf")
# plt.savefig('build/plot2.pdf')
