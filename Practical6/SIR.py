#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#define initial variables
N = 10000 #total population
susceptible = [N-1] #values of variables at the beginning
infected = [1]
recovered = [0]
beta = 0.3 # infection rate
gamma = 0.05 # recovery rate
for t in range(1, 1000): #time course
    S = susceptible[-1] #current values
    I = infected[-1]
    R = recovered[-1]
    infection_probability = beta*(I/N) #calculate current probabilities
    new_infected = np.random.choice([0, 1], #get new infected population
                                    size=S,
                                    p=[1 - infection_probability, infection_probability]).sum()
    new_recovered = np.random.choice([0, 1], #get new recovered population
                                    size=I,
                                    p=[1 - gamma, gamma]).sum() 
    susceptible.append(S - new_infected) #update population
    infected.append(I + new_infected - new_recovered)
    recovered.append(R + new_recovered)
plt.figure( figsize=(6,4),dpi=150) #plot the figure
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.plot(recovered, label='Recovered')
plt.xlabel('Time') #add labels 
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()
plt.savefig("SIR_model.png", format="png")
plt.show()