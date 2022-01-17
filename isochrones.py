import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# MIST isochrones
mist = np.loadtxt('MIST_v1.2_feh_p0.00_afe_p0.0_vvcrit0.4_basic.iso')
amist = mist[:,1]
pmist = mist[:,7]

rmist = 10**mist[:,11]
tmist = mist[:,10]
for logage in [9, 10]:
    j = abs(amist - logage) < 1e-6
    label = f'MIST, {10**(logage-9)} Gyr'
    plt.plot( tmist[j],pmist[j], c='darkgreen',ls='--', label=label)

# Dartmouth isochrones
for age in [1, 10]:
    iso = np.loadtxt(f'a{age*1e3:05.0f}fehp00afep0.Gaia')
    miso = iso[:,1]
    tiso = iso[:,2]
    Liso=iso[:,4]
    riso = np.sqrt(miso/10**(iso[:,3]-4.438))
    label = f'DSEB, {age} Gyr'
    plt.plot(tiso, Liso, c='navy', label=label)

plt.plot(3.843, 0.000688 ,marker='o',color='red')
plt.errorbar(3.843,0.000688 ,xerr=0.015, yerr=0.007,color='red',label='EBLM J0642-60')
plt.xlim(4,3.5)
plt.ylim(3,-3)
plt.xlabel('log Teff $[K]$', fontsize=12)
plt.ylabel('log L $[L_{\odot}]$', fontsize=12)
plt.legend()
plt.show(block=True)

