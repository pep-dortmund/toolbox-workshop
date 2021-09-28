import matplotlib as mpl
mpl.rcdefaults()
import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams.update({
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'pgf.texsystem': 'lualatex',
    'pgf.preamble': r'\input{header-matplotlib.tex}',
})

x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)
plt.figure(figsize=(4.76, 2.94))
plt.plot(x, y)
plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/figures/mattex4.pdf')
