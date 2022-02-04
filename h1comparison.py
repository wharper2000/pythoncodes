import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Teff_paper=(6297,5647,5993,6213,5947,5595,5595,5750,6041,5520,5750,5972,5560,5170,5634,5850)
Teff_err_p=(60,50,50,150,100,120,120,100,143,60,90,84,80,70,114,50)
h1_p_obs=(0.788,0.731,0.762,0.772,0.757,0.721,0.770,0.726,0.750,0.718,0.738,0.741,0.735,0.697,0.710,0.756)
h1_err_p_obs=(0.002,0.01,0.002,0.004,0.001,0.004,0.001,0.006,0.003,0.003,0.010,0.002,0.002,0.005,0.004,0.011)
h1_p_calc=(0.763,0.718,0.747,0.759,0.743,0.714,0.714,0.726,0.741,0.712,0.726,0.737,0.722,0.689,0.713,0.738)
h1_err_p_calc=(0.002,0.004,0.002,0.008,0.005,0.009,0.007,0.006,0.009,0.004,0.006,0.006,0.005,0.004,0.007,0.003)

h1_observed=(0.814,0.7848,0.8143,0.7731,0.780,0.789,0.863,0.734,0.793,0.8060,0.836,0.733)
h1_observed_err=(0.010,0.0038,0.0024,0.0060,0.0066,0.018,0.047,0.056,0.014,0.074,0.012,0.058)
h1_calc=(0.757, 0.740,0.754,0.732,0.763,0.736,0.757,0.754,0.769,0.786,0.772,0.761)
h1_calc_err=(0.003,0.003,0.004,0.005,0.006,0.005,0.008,0.006,0.007,0.004,0.006,0.007)
effT_calculated=(6505,5898,6230,5800,6443,5723,6210,6216,6484,6967,6638,6062)
effT_calculated_err=(131.467,125.295,80,100,139.838,110.295,137.136,138.219,135.427,108.01,128.749,125.855)

plt.figure(0)
plt.scatter(Teff_paper,h1_p_obs,marker="x",color="black",label="data from \nreferance paper")
plt.scatter(effT_calculated,h1_observed,marker="x",color="red",label="data from \nTIC analysis")
plt.errorbar(effT_calculated,h1_observed,xerr=effT_calculated_err,yerr=h1_observed_err,ecolor="red",fmt="none")
plt.errorbar(Teff_paper,h1_p_obs,xerr=Teff_err_p,yerr=h1_err_p_obs,ecolor="black",fmt="none")
plt.title("Graph comparing observed values of h1 \n to reference paper values")
plt.xlabel("effective temperature K")
plt.ylabel("observed h1")
plt.legend()
plt.show(block=False)

h1_p_obs_a = np.array(h1_p_obs)
h1_p_calc_a= np.array(h1_p_calc)
subtracted_array0 = np.subtract(h1_p_obs_a, h1_p_calc_a)
delta_h1_p = list(subtracted_array0)

h1_observed_a = np.array(h1_observed)
h1_calc_a= np.array(h1_calc)
subtracted_array1 = np.subtract(h1_observed_a, h1_calc_a)
delta_h1 = list(subtracted_array1)

#square errors, add them, then sqrt total to get delta uncertainty.

h1_p_obs_a_err = np.array(h1_err_p_obs)
h1_p_calc_a_err= np.array(h1_err_p_calc)
h1_p_obs_a_err=np.array(h1_p_obs_a_err**2)
h1_p_calc_a_err= np.array(h1_p_calc_a_err**2)
addedarray = np.array(h1_p_obs_a_err+ h1_p_calc_a_err)
delta_h1_p_err = np.sqrt(addedarray)

h1_observed_a_err = np.array(h1_observed_err)
h1_observed_a_err = np.array(h1_observed_a_err**2)
h1_calc_a_err= np.array(h1_calc_err)
h1_calc_a_err= np.array(h1_calc_a_err**2)

addedarray2 = np.array(h1_calc_a_err+ h1_observed_a_err)
delta_h1_err = np.sqrt(addedarray2)




plt.figure(1)
plt.title("Graph showing delta h1 and comparing with \nreference paper")
plt.scatter(Teff_paper,delta_h1_p,marker="x",color="black",label="data from \nreferance paper")
plt.scatter(effT_calculated,delta_h1,marker="x",color="red",label="data from \nTIC analysis")
plt.errorbar(effT_calculated,delta_h1,xerr=effT_calculated_err,yerr=delta_h1_err,ecolor="red",fmt="none")
plt.errorbar(Teff_paper,delta_h1_p,xerr=Teff_err_p,yerr=delta_h1_p_err,ecolor="black",fmt="none")
plt.axhline(y=0,color="green")

plt.xlabel("effective temperature K")
plt.ylabel("observed h1-calculated h1")
plt.legend()
plt.show(block=True)
