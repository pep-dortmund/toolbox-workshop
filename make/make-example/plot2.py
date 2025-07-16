import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("data.txt", unpack=True)
data2 = np.genfromtxt("data2.txt", unpack=True)
fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(data, data2)
fig.savefig("plot2.pdf")
# plt.savefig('build/plot2.pdf')
