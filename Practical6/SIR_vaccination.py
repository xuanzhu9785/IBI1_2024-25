#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#define initial variables
N = 10000 #total population
vaccinated_percentage = 0.1
V = int(vaccinated_percentage * N)
infected = 1
recovered = 0
vaccinated = V
beta = 0.3 # infection rate
gamma = 0.05 # recovery rate
vaccination_levels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.figure( figsize=(6,4),dpi=150)
for v_percent in vaccination_levels:
    V = int(v_percent /100*N)
    susceptible = N - infected - recovered - V
    S, I, R = [susceptible], [infected], [recovered]
    for t in range(1, 1000): #time course
        new_infected = np.random.binomial(max(S[-1], 0), beta * I[-1] / N)
        new_recovered = np.random.binomial(I[-1], gamma)

        S.append(S[-1] - new_infected)
        I.append(I[-1] + new_infected - new_recovered)
        R.append(R[-1] + new_recovered)
    plt.plot(I, label=f"Vaccination: {v_percent}%")
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model with different vaccination rates')
plt.legend()
plt.savefig("SIR_vaccination_plot.png")
plt.show()