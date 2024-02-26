# ===== gen 9999 best solution ====
# (1537.6918913687825, (3.0699584752630353, 3.061837341328556, 3.0282868905074865))

import random
import matplotlib.pyplot as plt
import numpy as np

def problem(x,y,z):
    return 9*x+6 + 6*y+9 + z//12**8+8 - 69


def fitness(x,y,z):
    ans = problem(x,y,z)
    if ans == 0:
        return 9999999
    else:
        return abs(1/ans)



solutions = []


for s in range(10):
    solutions.append((random.uniform(0,100),random.uniform(0,100),random.uniform(0,100)))



print(solutions[1])

for i in range(100):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0],s[1],s[2]),s))
        rankedsolutions.sort()
        rankedsolutions.reverse()
        print(f"===== gen {i} best solution ====")
        print(rankedsolutions[0])

        if rankedsolutions[0][0] > 1:
            break
        bestsolutions = rankedsolutions[:100]


        elements = []
    for s in bestsolutions: 
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])
    
    newGen = []

    for _ in range(10):
        e1 = random.choice(elements) * random.uniform(0.99,1.01)
        e2 = random.choice(elements) * random.uniform(0.99,1.01)
        e3 = random.choice(elements) * random.uniform(0.99,1.01)

        newGen.append((e1,e2,e3))

    solutions = newGen


data = np.array(elements)
plt.plot(elements)
plt.show()



data = np.array(solutions)
plt.plot(solutions)
plt.show()