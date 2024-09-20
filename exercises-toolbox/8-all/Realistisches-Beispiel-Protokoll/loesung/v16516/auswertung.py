import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import scipy.constants


import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties.unumpy import (
    nominal_values as noms,
    std_devs as stds,
)

from curve_fit import ucurve_fit
from latex_formatting import make_qty


# Load all data files
camera = np.genfromtxt("data/Messwerte_Kamera.txt",  names=True, delimiter=",")
track = np.genfromtxt("data/Messwerte_Bahn.txt",  names=True, delimiter=",")
ball = np.genfromtxt("data/Messwerte_Kugel.txt",  names=True, delimiter=",")
cylinder = np.genfromtxt("data/Messwerte_Zylinder.txt",  names=True, delimiter=",")
measurements_ball = np.genfromtxt("data/Messwerte_Frames_Kugel.txt",  names=True, delimiter=",")
measurements_cylinder = np.genfromtxt("data/Messwerte_Frames_Zylinder.txt",  names=True, delimiter=",")


# overview of raw data
print("Übersicht der (rohen) Messwerte")
print("Kamera Einstellungen")
print(camera.dtype.names)
print(camera)
print("Bahn Eigenschaften")
print(track.dtype.names)
print(track)
print("Ball Eigenschaften")
print(ball.dtype.names)
print(ball)
print("Zylinder Eigenschaften")
print(cylinder.dtype.names)
print(cylinder)
print("Messreihe: Ball")
print(measurements_ball.dtype.names)
print(measurements_ball)
print("Messreihe: Zylinder")
print(measurements_cylinder.dtype.names)
print(measurements_cylinder)
print("-"*70,end="\n\n")


# create data with uncertainties and SI-Units

framerate = camera["fps"] # frame/s
L = track_length = unc.ufloat(track["l"],track["sigma_l"])/100 # m

m_B = ball_mass = unc.ufloat(ball["m"],ball["sigma_m"])/1000 # kg
U_B = ball_perimeter = unc.ufloat(ball["U"],ball["sigma_U"])/100 #m
R_B = ball_radius = ball_perimeter / (2 * np.pi)
I_B = ball_momentinertia = 2/5 * m_B * (R_B**2)


h_B = heights_ball = unp.uarray(measurements_ball["h"], measurements_ball["sigma_h"])/100 # m
fi_B = initalframes_ball = unp.uarray(measurements_ball["Fi"], measurements_ball["sigma_Fi"]) # 1  
ff_B = finalframes_ball = unp.uarray(measurements_ball["Ff"], measurements_ball["sigma_Ff"]) # 1

t_B = durations_ball = (ff_B - fi_B) / framerate #s


# each height was measured 3 times => calculating the mean of these measurments 
# selecting each height once 
h_B = h_B.reshape(-1, 3)[:,0]
t_B = t_B.reshape(-1, 3).mean(axis=1)



m_C = cylinder_mass = unc.ufloat(cylinder["m"],cylinder["sigma_m"])/1000 # kg
U_C = cylinder_perimeter = unc.ufloat(cylinder["U"],cylinder["sigma_U"])/100 #m
d_C = cylinder_thickness = unc.ufloat(cylinder["d"],cylinder["sigma_d"])/1000 #m
Ri_C = cylinder_radius_inner = cylinder_perimeter / (2 * np.pi)
Ro_C = cylinder_radius_outer = cylinder_radius_inner + cylinder_thickness
I_C = ball_momentinertia = 1/2 * m_C * (Ro_C**2 + Ri_C**2)

h_C = heights_cylinder = unp.uarray(measurements_cylinder["h"], measurements_cylinder["sigma_h"])/100 # m
fi_C = initalframes_cylinder = unp.uarray(measurements_cylinder["Fi"], measurements_cylinder["sigma_Fi"]) # 1  
ff_C = finalframes_cylinder = unp.uarray(measurements_cylinder["Ff"], measurements_cylinder["sigma_Ff"]) # 1

t_C = durations_cylinder = (ff_C - fi_C) / framerate #s

# each height was measured 3 times => calculating the mean of these measurments 
# selecting each height once 
h_C = h_C.reshape(-1, 3)[:,0]
t_C = t_C.reshape(-1, 3).mean(axis=1)

# Part 1: determination of the gravitational constant g


# fitting theoretical curve to data
def fit_g_ball(h, g, t0):
     return np.sqrt(7/5 * 1/h * 2* noms(L)**2/g) + t0

params = ucurve_fit(fit_g_ball, noms(h_B), t_B, p0=[10, 0])


print("Fit Parameter (Kugel):")
print(params)


# plotting data an fit
h_plot = np.linspace(0.01,0.35, 1000) 
fig, ax = plt.subplots(1, 1, layout="constrained")

ax.errorbar(
     noms(h_B),
     noms(t_B),
     yerr=stds(t_B),
     fmt="k_",
    label="Daten: Kugel",
)
ax.plot(h_plot, fit_g_ball(h_plot, *noms(params)), "-", label="Fit")
ax.set_xlim(h_plot[0], h_plot[-1])
ax.set_xlabel(r"$h \mathbin{/} \unit{\meter}$")
ax.set_ylabel(r"$t \mathbin{/} \unit{\second}$")
ax.legend(loc="best")
fig.savefig("build/plot-g_ball.pdf")

# exporting fit parameters
parameter_g, parameter_t0 = params

with open("build/parameter-g_ball.tex", "w") as f:
    f.write(make_qty(parameter_g, r"\meter\per\second\squared"))

with open("build/parameter-t0-g_ball.tex", "w") as f:
    f.write(make_qty(parameter_t0, r"\second"))


# fitting theoretical curve to data
def fit_g_cylinder(h, g, t0):
    return np.sqrt((3 + noms(Ri_C**2/Ro_C**2)) * noms(L)**2/(g*h)) + t0

params = ucurve_fit(fit_g_cylinder, noms(h_C), t_C, p0=[10, 0])

print("Fit Parameter (Zylinder):")
print(params)


# plotting data an fit
h_plot = np.linspace(0.01,0.35, 1000) 
fig, ax = plt.subplots(1, 1, layout="constrained")

ax.errorbar(
     noms(h_C),
     noms(t_C),
     yerr=stds(t_C),
     fmt="k_",
    label="Daten: Zylinder",
)
ax.plot(h_plot, fit_g_cylinder(h_plot, *noms(params)), "-", label="Fit")
ax.set_xlim(h_plot[0], h_plot[-1])
ax.set_xlabel(r"$h \mathbin{/} \unit{\meter}$")
ax.set_ylabel(r"$t \mathbin{/} \unit{\second}$")
ax.legend(loc="best")
fig.savefig("build/plot-g_cylinder.pdf")

# exporting fit parameters
parameter_g, parameter_t0 = params

with open("build/parameter-g_cylinder.tex", "w") as f:
    f.write(make_qty(parameter_g, r"\meter\per\second\squared"))

with open("build/parameter-t0-g_cylinder.tex", "w") as f:
    f.write(make_qty(parameter_t0, r"\second"))



# Part 2: determination of the Moment of inertia if g is assumed to be known
g = scipy.constants.g # m/s²



# fitting theoretical curve to data
def fit_I_ball(h, I, t0):
     return np.sqrt(2/g * 1/h * noms(L)**2 * (1 + I/(noms(m_B) * noms(R_B)**2) )) + t0

params = ucurve_fit(fit_I_ball, noms(h_B), t_B, p0=[0.001, -1])


print("Fit Parameter (Kugel):")
print(params)

# plotting data an fit
h_plot = np.linspace(0.01,0.35, 1000) 
fig, ax = plt.subplots(1, 1, layout="constrained")

ax.errorbar(
     noms(h_B),
     noms(t_B),
     yerr=stds(t_B),
     fmt="k_",
    label="Daten: Kugel",
)
ax.plot(h_plot, fit_I_ball(h_plot, *noms(params)), "-", label="Fit")
ax.set_xlim(h_plot[0], h_plot[-1])
ax.set_xlabel(r"$h \mathbin{/} \unit{\meter}$")
ax.set_ylabel(r"$t \mathbin{/} \unit{\second}$")
ax.legend(loc="best")
fig.savefig("build/plot-I_ball.pdf")

# exporting fit parameters
parameter_I, parameter_t0 = params

with open("build/parameter-I_ball.tex", "w") as f:
    f.write(make_qty(parameter_I*10000, r"\kilo\gram\centi\meter\squared"))# change units: kg cm²

with open("build/parameter-t0-I_ball.tex", "w") as f:
    f.write(make_qty(parameter_t0, r"\second"))


# fitting theoretical curve to data
def fit_I_cylinder(h, I, t0):
     return np.sqrt(2/g * 1/h * noms(L)**2 * (1 + I/(noms(m_C) * noms(Ro_C)**2) )) + t0

params = ucurve_fit(fit_I_cylinder, noms(h_C), t_C, p0=[0.001, -1])


print("Fit Parameter (Zylinder):")
print(params)


# plotting data an fit
h_plot = np.linspace(0.01,0.35, 1000) 
fig, ax = plt.subplots(1, 1, layout="constrained")

ax.errorbar(
     noms(h_C),
     noms(t_C),
     yerr=stds(t_C),
     fmt="k_",
    label="Daten: Zylinder",
)
ax.plot(h_plot, fit_I_cylinder(h_plot, *noms(params)), "-", label="Fit")
ax.set_xlim(h_plot[0], h_plot[-1])
ax.set_xlabel(r"$h \mathbin{/} \unit{\meter}$")
ax.set_ylabel(r"$t \mathbin{/} \unit{\second}$")
ax.legend(loc="best")

fig.savefig("build/plot-I_cylinder.pdf")

# exporting fit parameters
parameter_I, parameter_t0 = params

with open("build/parameter-I_cylinder.tex", "w") as f:
    f.write(make_qty(parameter_I*10000, r"\kilo\gram\centi\meter\squared"))# change units: kg cm²

with open("build/parameter-t0-I_cylinder.tex", "w") as f:
    f.write(make_qty(parameter_t0, r"\second"))


# exporting non tabular data

with open("build/theoretical-g.tex", "w") as f:
    f.write(make_qty(g,r"\meter\per\second\squared", figures=2, formatting="per-mode=reciprocal"))

with open("build/framerate.tex", "w") as f:
    f.write(make_qty(framerate, r"\per\second", figures=0, formatting="per-mode=reciprocal"))

with open("build/theoretical-I_ball.tex", "w") as f:
    f.write(make_qty(I_B*10000,r"\kilo\gram\centi\meter\squared")) # change units: kg cm²

with open("build/theoretical-I_cylinder.tex", "w") as f:
    f.write(make_qty(I_C*10000,r"\kilo\gram\centi\meter\squared"))# change units: kg cm²

with open("build/tracklength.tex", "w") as f:
    f.write(make_qty(L,r"\meter"))

with open("build/mass_ball.tex", "w") as f:
    f.write(make_qty(m_B,r"\kilo\gram"))

with open("build/mass_cylinder.tex", "w") as f:
    f.write(make_qty(m_B,r"\kilo\gram"))

with open("build/radius_ball.tex", "w") as f:
    f.write(make_qty(R_B, r"\meter"))

with open("build/radius-inner_cylinder.tex", "w") as f:
    f.write(make_qty(Ri_C,r"\meter"))

with open("build/radius-outer_cylinder.tex", "w") as f:
    f.write(make_qty(Ro_C,r"\meter"))

# writing latex tables
# first: writing all measured values not just the averages
# heights_ball, durations_ball, durations_cylinder
# have not been reduced to 6 values each
# Columns:
# %h          
# %F_i        
# %F_i_sigma  
# %F_f        
# %F_f_sigma  
# %t          
# %t_sigma    
# %F_i        
# %F_i_sigma  
# %F_f        
# %F_f_sigma  
# %t          
# %t_sigma    



table_header_all = r"""
  \begin{tblr}{
    colspec = {
        S[table-format=1.3]
        S[table-format=4.0]
        S[table-format=1.0]
        S[table-format=4.0]
        S[table-format=1.0]
        S[table-format=1.3]
        S[table-format=1.3]
        S[table-format=4.0]
        S[table-format=1.0]
        S[table-format=4.0]
        S[table-format=1.0]
        S[table-format=1.3]
        S[table-format=1.3]
    },
    row{1} = {guard},
    row{2} = {guard, mode=math},
    vline{3,5,7,9,11,13} = {2}{-}{text=\clap{\pm}},
  }
    \toprule                                                  
    &                                                        
    \SetCell[c=6]{c} Messung: Kugel & & & & & &
    \SetCell[c=6]{c} Messung: Zylinder & & & & & \\ 
    \cmidrule[lr]{2-7}\cmidrule[lr]{8-14}
    h \mathbin{/} \unit{\meter} &%
    \SetCell[c=2]{c} F_\text{i} \mathbin{/} 1 & &%
    \SetCell[c=2]{c} F_\text{f} \mathbin{/} 1 & &%
    \SetCell[c=2]{c} t \mathbin{/} \unit{\second} & &% 
    \SetCell[c=2]{c} F_\text{i} & &%
    \SetCell[c=2]{c} F_\text{f} & &%
    \SetCell[c=2]{c} t \mathbin{/} \unit{\second}& \\
    \midrule
"""

    
table_footer = r"""    \bottomrule
  \end{tblr}
"""


row_template = (
    r"{0.n:1.3f} & {1.n:0.0f} & {1.s:0.0f} &  {2.n:0.0f} & {2.s:0.0f}&  {3.n:1.3f} & {3.s:1.3f}  &  {4.n:0.0f} & {4.s:0.0f}&  {5.n:0.0f} & {5.s:0.0f}&  {6.n:1.3f} & {6.s:1.3f}   \\"
)



with open("build/table_all-measurements.tex", "w") as f:
    f.write(table_header_all)
    for row in zip(heights_ball, initalframes_ball, finalframes_ball, durations_ball, initalframes_cylinder, finalframes_cylinder, durations_cylinder):
        f.write(row_template.format(*row))
        f.write("\n")
    f.write(table_footer)


# second: writing the averaged values and leaving out the frames
# heights_ball, durations_ball, durations_cylinder
# have not been reduced to 6 values each


table_header_averaged = r"""
  \begin{tblr}{
    colspec = {
        S[table-format=1.3]
        S[table-format=2.3]
        S[table-format=1.4]
        S[table-format=3.3]
        S[table-format=1.5]
    },
    row{1} = {guard},
    row{2} = {guard, mode=math},
    vline{3,5,7,9} = {2}{-}{text=\clap{\pm}},
  }
    \toprule                                                  
    &                                                        
    \SetCell[c=2]{c} Messung: Kugel & &
    \SetCell[c=2]{c} Messung: Zylinder &\\ 
    \cmidrule[lr]{2-3}\cmidrule[lr]{4-5}
    h \mathbin{/} \unit{\meter} &%
    \SetCell[c=2]{c} t \mathbin{/} \unit{\second} & &% 
    \SetCell[c=2]{c} t \mathbin{/} \unit{\second}& \\
    \midrule
"""

    
table_footer = r"""    \bottomrule
  \end{tblr}
"""


row_template = (
    r"{0.n:1.3f} & {1.n:1.3f} & {1.s:1.3f} &  {2.n:1.3f} & {2.s:1.3f}   \\"
)


with open("build/table_averaged-measurements.tex", "w") as f:
    f.write(table_header_averaged)
    for row in zip(h_B, t_B, t_C):
        f.write(row_template.format(*row))
        f.write("\n")
    f.write(table_footer)





