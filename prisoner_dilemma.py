import numpy as np
import matplotlib.pyplot as plt

# We start with a payoff matrix
# Payoff matrix for prisoner's dilemma
payoff_matrix = np.array([[2, 0], [3, 1]])
print(f"Payoff matrix for prisoner's dilemma:\n"
      "If both Cooperate, they get 2 each.\n"
      "If both Defect, they get 1 each.\n"
      "If one Cooperates and the other Defects,\n"
      "the one who Defects gets 3\n"
      "and the one who Cooperates gets 0.")

# Now let's define a population
def population(Defectors, Cooperators):
    return np.array([Defectors, Cooperators])

def print_population(population):
    print(f"Population has {population[0]} Defectors and {population[1]} Cooperators.")

def starting_population():
    print("How many Defectors in starting population?")
    Defectors = int(input())
    print("How many Cooperators in starting population?")
    Cooperators = int(input())
    return population(Defectors, Cooperators)

population = starting_population()
print_population(population)

# Now let's define a fitness function
def fitness(population, payoff_matrix):
    return np.dot(population, payoff_matrix)

# Choose a random individual
def random_individual(population):
    return np.random.randint(0, sum(population))

# Identify the strategy of an individual
def strategy(individual):
    return 0 if individual < population[0] else 1

# We enact a death of an individual
def remove_individual(population, individual):
    strat = strategy(individual)
    if strat == 0 and population[0] > 0:
        return population - np.array([1, 0])
    elif strat == 1 and population[1] > 0:
        return population - np.array([0, 1])
    return population - np.array([0, 1])

# We enact a birth of an individual of a given strategy
def add_individual(population, strat):
    return population + np.array([1, 0]) if strat == 0 else population + np.array([0, 1])

# Now we enact a replacement starting with random death then fitness weighted birth.
def replacement(population, payoff_matrix):
    individual = random_individual(population)
    population = remove_individual(population, individual)
    fit = fitness(population, payoff_matrix)
    # Calculate the probability of a Cooperator being born
    prob = fit[1] / sum(fit)
    # Choose a strategy for the new individual
    strat = 1 if np.random.rand() < prob else 0
    return add_individual(population, strat)

# Let's run a few generations in text
def generations_text(population, payoff_matrix, n):
    for _ in range(n):
        population = replacement(population, payoff_matrix)
        print_population(population)

# Let's run a few generations in a plot
def generations_plot(population, payoff_matrix, n):
    data = [population]
    for _ in range(n):
        population = replacement(population, payoff_matrix)
        data.append(population)
    data = np.array(data)
    plt.plot(data)
    plt.xlabel("Generation")
    plt.ylabel("Population")
    plt.title("Prisoner's Dilemma")
    plt.legend(["Defectors", "Cooperators"])
    plt.show()

generations_plot(population, payoff_matrix, 1000)