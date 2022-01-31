import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Teff_paper=(6297,5647,5993,6213,5947,5595,5595,5750,6041,5520,5750,5972,5560,5170,5634,5850)
Teff_err_p=(60,50,50,150,100,120,120,100,143,60,90,84,80,70,114,50)
h1_p_obs=(0.788,0.731,0.762,0.772,0.757,0.721,0.770,0.726,0.750,0.718,0.738,0.741,0.735,0.697,0.710,0.756)
h1_err_p_obs=(0.002,0.01,0.002,0.004,0.001,0.004,0.001,0.006,0.003,0.003,0.010,0.002,0.002,0.005,0.004,0.011)

h1_calculated=(0.8198 ,0.766,0.824,0.814,0.7848,0.08310,0.82,0.789,0.863,0.734,0.793,0.8060,0.836,0.733)
h1_calculated_err=(0.0096,0.069,0.012,0.010,0.0038,0.0067,0.12,0.018,0.047,0.056,0.014,0.0074,0.012,0.058)
effT_calculated=(6532.23,5592,6671,6505,5898,6733,6443,5723,6210,6216,6484,6967,6638,6062)
effT_calculated_err=(109.214,125.216,130.578,131.467,125.295,131.587,139.838,110.295,137.136,138.219,135.427,108.01,128.749,125.855)

plt.scatter(Teff_paper,h1_p_obs,marker="x",color="black",label="data from \nreferance paper")
plt.scatter(effT_calculated,h1_calculated,marker="x",color="red",label="data from \nTIC analysis")
plt.errorbar(effT_calculated,h1_calculated,xerr=effT_calculated_err,yerr=h1_calculated_err,ecolor="red",fmt="none")
plt.errorbar(Teff_paper,h1_p_obs,xerr=Teff_err_p,yerr=h1_err_p_obs,ecolor="blue",fmt="none")
plt.xlabel("effective temperature K")
plt.ylabel("observed h1")
plt.legend()
plt.show(block=True)