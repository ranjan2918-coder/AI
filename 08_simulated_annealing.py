# 8. Simulated Annealing

import random, math

x = random.randint(-10, 10)
T = 100

while T > 0.1:
    new = x + random.choice([-1, 1])
    if (new-3)**2 < (x-3)**2 or random.random() < math.exp(
        ((x-3)**2 - (new-3)**2) / T
    ):
        x = new
    T *= 0.95

print("Best solution:", x)
print("Minimum value:", (x-3)**2)
