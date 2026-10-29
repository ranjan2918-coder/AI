# 7. Genetic Algorithm

import random

population = [random.randint(1, 20) for _ in range(6)]

for _ in range(20):
    population.sort(key=lambda x: abs(x-10))
    a, b = population[:2]
    child = (a+b)//2
    if random.random() < 0.3:
        child += random.choice([-1, 1])
    population[-1] = child

print("Best solution:", min(population, key=lambda x: abs(x-10)))
