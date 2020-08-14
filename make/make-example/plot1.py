import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.txt', unpack=True)
plt.plot(data)
plt.savefig('plot1.pdf')
#plt.savefig('build/plot1.pdf')
