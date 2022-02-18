import numpy as np
import matplotlib.pyplot as plt
from scipy import stats



Teff_paper=(6297,5647,5993,6213,5947,5595,5595,5750,6041,5520,5750,5972,5560,5170,5634,5850)
Teff_err_p=(60,50,50,150,100,120,120,100,143,60,90,84,80,70,114,50)
h1_p_obs=(0.788,0.731,0.762,0.772,0.757,0.721,0.770,0.726,0.750,0.718,0.738,0.741,0.735,0.697,0.710,0.756)
h1_err_p_obs=(0.002,0.01,0.002,0.004,0.001,0.004,0.001,0.006,0.003,0.003,0.010,0.002,0.002,0.005,0.004,0.011)
h1_p_calc=(0.763,0.718,0.747,0.759,0.743,0.714,0.714,0.726,0.741,0.712,0.726,0.737,0.722,0.689,0.713,0.738)
h1_err_p_calc=(0.002,0.004,0.002,0.008,0.005,0.009,0.007,0.006,0.009,0.004,0.006,0.006,0.005,0.004,0.007,0.003)


effT_calculated,effT_calculated_err,h1_observed,h1_observed_err,h1_calc,h1_calc_err=np.loadtxt("EBLM_values.csv",unpack=True)
HJ_effT_calculated,HJ_effT_calculated_err,HJ_h1_observed,HJ_h1_observed_err,HJ_h1_calc,HJ_h1_calc_err=np.loadtxt("HJ_values.csv",unpack=True)

effT_calculated_r,effT_calculated_err_r,h1_observed_r,h1_observed_err_r,h1_calc_r,h1_calc_err_r=np.loadtxt("EBLM_removed.csv",unpack=True)
HJ_effT_calculated_r,HJ_effT_calculated_err_r,HJ_h1_observed_r,HJ_h1_observed_err_r,HJ_h1_calc_r,HJ_h1_calc_err_r=np.loadtxt("HJ_removed.csv",unpack=True)

"""
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
"""

#reference paper
h1_p_obs_a = np.array(h1_p_obs)
h1_p_calc_a= np.array(h1_p_calc)
subtracted_array0 = np.subtract(h1_p_obs_a, h1_p_calc_a)
delta_h1_p = list(subtracted_array0)

#analysed values from jupyter EBLM
h1_observed_a = np.array(h1_observed)
h1_calc_a= np.array(h1_calc)
subtracted_array1 = np.subtract(h1_observed_a, h1_calc_a)
delta_h1 = list(subtracted_array1)

#analysed values from jupyter HJ
HJ_h1_observed_a = np.array(HJ_h1_observed)
HJ_h1_calc_a= np.array(HJ_h1_calc)
subtracted_array2 = np.subtract(HJ_h1_observed_a, HJ_h1_calc_a)
HJ_delta_h1 = list(subtracted_array2)

#analysed values from jupyter EBLM with large uncertainties removed
h1_observed_a_r = np.array(h1_observed_r)
h1_calc_a_r= np.array(h1_calc_r)
subtracted_arrayr = np.subtract(h1_observed_a_r, h1_calc_a_r)
delta_h1_r = list(subtracted_arrayr)

#analysed values from jupyter HJ with large uncertainties removed
HJ_h1_observed_a_r = np.array(HJ_h1_observed_r)
HJ_h1_calc_a_r= np.array(HJ_h1_calc_r)
subtracted_arrayr2 = np.subtract(HJ_h1_observed_a_r, HJ_h1_calc_a_r)
HJ_delta_h1_r = list(subtracted_arrayr2)

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

#HJ errors
HJ_h1_observed_a_err = np.array(HJ_h1_observed_err)
HJ_h1_observed_a_err = np.array(HJ_h1_observed_a_err**2)
HJ_h1_calc_a_err= np.array(HJ_h1_calc_err)
HJ_h1_calc_a_err= np.array(HJ_h1_calc_a_err**2)
addedarray3 = np.array(HJ_h1_calc_a_err+ HJ_h1_observed_a_err)
HJ_delta_h1_err = np.sqrt(addedarray3)

#EBLM error propogation, removed uncertainties
h1_observed_a_err_r= np.array(h1_observed_err_r)
h1_observed_a_err_r = np.array(h1_observed_a_err_r**2)
h1_calc_a_err_r= np.array(h1_calc_err_r)
h1_calc_a_err_r= np.array(h1_calc_a_err_r**2)
addedarrayr2 = np.array(h1_calc_a_err_r+ h1_observed_a_err_r)
delta_h1_err_r = np.sqrt(addedarrayr2)

#HJ errors with removed uncertainties
HJ_h1_observed_a_err_r = np.array(HJ_h1_observed_err_r)
HJ_h1_observed_a_err_r = np.array(HJ_h1_observed_a_err_r**2)
HJ_h1_calc_a_err_r= np.array(HJ_h1_calc_err_r)
HJ_h1_calc_a_err_r= np.array(HJ_h1_calc_a_err_r**2)
addedarrayr3 = np.array(HJ_h1_calc_a_err_r+ HJ_h1_observed_a_err_r)
HJ_delta_h1_err_r = np.sqrt(addedarrayr3)


print(len(effT_calculated_r))
print(len(delta_h1_r))

plt.figure(1)
#plt.title("Graph showing delta h1 and comparing with \nreference paper")

plt.rc('axes', labelsize=8)    # fontsize of the x and y labels
plt.rc('font', size=8) #changes default font size
plt.subplot(2, 1, 1)
plt.scatter(Teff_paper,delta_h1_p,marker="x",color="black",label="Data from \nreferance paper")
plt.scatter(effT_calculated,delta_h1,marker="x",color="red",label="EBLM data from \nTIC analysis")
plt.scatter(HJ_effT_calculated,HJ_delta_h1,marker="x",color="blue",label="Hot Jupiter data\nfrom TIC analysis")

plt.errorbar(effT_calculated,delta_h1,xerr=effT_calculated_err,yerr=delta_h1_err,ecolor="red",fmt="none")
plt.errorbar(Teff_paper,delta_h1_p,xerr=Teff_err_p,yerr=delta_h1_p_err,ecolor="black",fmt="none")
plt.errorbar(HJ_effT_calculated,HJ_delta_h1,xerr=HJ_effT_calculated_err,yerr=HJ_delta_h1_err,ecolor="blue",fmt="none")
plt.axhline(y=0,color="green")

plt.ylabel("observed h$_1$-calculated h$_1$")


plt.subplot(2, 1, 2)
plt.scatter(Teff_paper,delta_h1_p,marker="x",color="black",label="Data from \nreferance paper")
plt.scatter(effT_calculated_r,delta_h1_r,marker="x",color="red",label="EBLM data from \nTIC analysis")
plt.scatter(HJ_effT_calculated_r,HJ_delta_h1_r,marker="x",color="blue",label="Hot Jupiter data\nfrom TIC analysis")

plt.errorbar(effT_calculated_r,delta_h1_r,xerr=effT_calculated_err_r,yerr=delta_h1_err_r,ecolor="red",fmt="none")
plt.errorbar(Teff_paper,delta_h1_p,xerr=Teff_err_p,yerr=delta_h1_p_err,ecolor="black",fmt="none")
plt.errorbar(HJ_effT_calculated_r,HJ_delta_h1_r,xerr=HJ_effT_calculated_err_r,yerr=HJ_delta_h1_err_r,ecolor="blue",fmt="none")
plt.axhline(y=0,color="green")

plt.xlabel("effective temperature K")
plt.ylabel("observed h$_1$-calculated h$_1$")
#plt.legend()
plt.savefig("h1_split.png")
plt.show(block=True)
