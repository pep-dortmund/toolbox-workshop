import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("data.txt", unpack=True)

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(data)
fig.savefig("plot1.pdf")
# fig.savefig('build/plot1.pdf')
