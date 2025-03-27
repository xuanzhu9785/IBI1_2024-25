# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define initial parameters
N = 100 * 100  # Total population
beta = 0.3  # Infection probability per contact
gamma = 0.05  # Recovery probability
time_steps = 100  # Number of time steps to simulate

# Define initial population state
# 0 = Susceptible, 1 = Infected, 2 = Recovered
population = np. zeros( (100, 100) )

# Randomly choose one initial infected point
outbreak = np.random.choice(range(100), 2) #outbreak contains two figures
population[outbreak[0], outbreak[1]] = 1 #change the coordinates from susceptible to infected

# Define function to get the data of neighbors of a point
def get_neighbors(x, y, size = 100):
    neighbors = []
    possible_neighbors = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)] #list possible_neighbors
    for nx, ny in possible_neighbors:
            if 0 <= nx < 100 and 0 <= ny < 100:
                neighbors.append((nx, ny))
    return neighbors

# Simulation loop
for t in range(0,100):
    # Find all infected points
    infected_points = np.argwhere(population == 1)
    new_population = population.copy()

    # Loop through infected points and attempt to infect neighbors
    for point in infected_points:
        x, y = point
        neighbors = get_neighbors(x, y, 100)

        # Attempt to infect susceptible neighbors
        for nx, ny in neighbors:
            if population[nx, ny] == 0:  # If the neighbor is susceptible
                if np.random.rand() < beta:  # Infection probability
                    new_population[nx, ny] = 1

        # Recovery step for infected individuals
        if np.random.rand() < gamma:
            new_population[x, y] = 2  # Recovered

    # Update population state
    population = new_population

    # Plot the population state every 10 time steps
    if t % 10 == 0 or t == time_steps - 1:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest') #heat map
        plt.title(f"Time Step: {t}")
        plt.colorbar(label="State (0=Susceptible, 1=Infected, 2=Recovered)")
        plt.show()
