import string
import random as rand
import matplotlib.pyplot as plt
import numpy as np

def orderCheck(data):
    return True if len(list(set(data))) != len(data) else False

letter = [i for i in string.ascii_uppercase]
number = ['1','2','3','4','5','6','7','8','9','0']

orderProbabilities = 0
allProbabilities = 0

repeater = 1000
chance = []

while(repeater):
    outcomes = [rand.choice(letter) for _ in range(3)] + [rand.choice(number) for _ in range(3)]
    if orderCheck(outcomes):
        orderProbabilities += 1
    allProbabilities += 1

    chance.append(1 - (orderProbabilities / allProbabilities))

    repeater -= 1

npChance = np.array(chance)
plt.plot(npChance)
plt.show()