import numpy as np
import model as hp
import matplotlib.pyplot as plt

T_REF = 18.333

year = 18

coeffs = hp.get_coeffs_c(1)
heating_coeffs = coeffs[1]

for i in range(5):


	temps = np.loadtxt("house_temp_" + str(year+i) + "_2.csv", delimiter = ',')
	heating_ff_demand = np.loadtxt("house_ff_demand_" + str(year+i) + "_2.csv", delimiter = ',')

	COP = (temps - T_REF) * heating_coeffs[0] + heating_coeffs[1]
	elec_demand = (heating_ff_demand / COP) * 0.000293 * 1000000

	np.savetxt("elec_demand_hourly_" + str(year + i) + "_2.csv", elec_demand)
#	plt.plot(elec_demand, "r*")
#	plt.xlabel("Time")
#	plt.ylabel("Electricity Demand (kWh)")
#	plt.show()
#	plt.savefig("Elec_demand_" + str(year+1) + ".png")
