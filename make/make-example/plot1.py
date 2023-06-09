import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.txt", unpack=True)

fig, ax = plt.subplots(1, 1, constrained_layout=True)
ax.plot(data)
fig.savefig("plot1.pdf")
# fig.savefig('build/plot1.pdf')
