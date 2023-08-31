#!/usr/bin/env python
import pygedm
import numpy as np
import matplotlib.pyplot as plt

def delayToDM(delay, nu1, nu2):
    return abs(delay / (4.15 * ((nu1**-2) - (nu2**-2))))

def DMToDelay(DM, nu1, nu2):
    return 1.0e-3 * abs(4.15 * DM * ((nu1**-2) - (nu2**-2)))

dms = np.arange(10, 2000, 10)
delays = np.zeros(len(dms))
scatters = np.zeros(len(dms))

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
LOFAR = False
if LOFAR is True:
    for i in range(0, len(dms)):
        dm = dms[i]
        delays[i] = DMToDelay(dm, 0.12, 0.18)
        scatters[i] = pygedm.pygedm.dm_to_dist(60, 0, dm, "ymw16", mode="Gal", nu=0.15)[1].value
    ax.plot(dms, delays, label="LOFAR delay", color='blue')
    ax.plot(dms, 1.e-1*scatters, label="LOFAR scattering / 10", color='blue', ls="--")
    ax.plot(dms, scatters, label="LOFAR scattering", color='blue', ls=":")
    ax.axhline(1, label="LOFAR time resolution", color='darkblue')
    outprefix = "LOFAR"
else:
    for i in range(0, len(dms)):
        dm = dms[i]
        delays[i] = DMToDelay(dm, 0.185, 0.215)
        scatters[i] = pygedm.pygedm.dm_to_dist(0, 0, dm, "ymw16", mode="Gal", nu=0.2)[1].value
    ax.plot(dms, delays, label="MWA delay", color='orange')
    ax.plot(dms, 1.e-1*scatters, label="MWA scattering / 10", color='orange', ls="--")
    ax.plot(dms, scatters, label="MWA scattering", color='orange', ls=":")
    ax.axhline(0.5, label="Old MWA time resolution", color='darkorange')
    outprefix = "MWA"
#ax.axhline(1, color='black', lw=2)
ax.set_ylim(1.e-3, 3.e3)
ax.axhline(10, color='black')
ax.axhline(30, color='black', alpha=0.5)
ax.axhline(100, color='black', alpha=0.1)
ax.legend(fontsize=8)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("DM / pc cm$^{-3}$")
ax.set_ylabel("time / s")
fig.savefig(f"{outprefix}_delay_scattering.png", bbox_inches="tight")
