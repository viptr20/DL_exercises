import numpy as np
import matplotlib.pyplot as plt

from data_task04 import gdp_cap, life_exp, pop

gdp_cap = np.array(gdp_cap)
life_exp = np.array(life_exp)
pop = np.array(pop)
sizes = pop * 2

plt.figure()
plt.scatter(gdp_cap, life_exp, s=sizes)
plt.xscale("log")
plt.xlabel("GDP per Capita [in USD]")
plt.ylabel("Life Expectancy [in years]")
plt.title("World Development in 2007")

plt.show()