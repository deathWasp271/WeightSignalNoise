import os
import numpy as np
import matplotlib.pyplot as plt

data = [99.1, 99.2, 99.6, 98.1, 99.7, 98.5, 97.6, 97.9, 98.1, 98.0, 98.7, 98.2, 97.7, 98.4, 97.9, 98.1, 98.3, 99.2, 99.1, 97.4, 97.7, 97.9, 97.6, 97.5, 97.5, 97.7, 97.4, 97.1]

eSC = 1.111

def weightedAvg(randomV, weights): # len(randomV) = len(weights)
    tupleArray = [(randomV[i], weights[i]) for i in range(len(randomV))]
    return (sum(map(lambda (x,y) : x*y, tupleArray))*1.0)/sum(weights)

weights = [eSC**i for i in range(len(data))]
result = map(lambda x: weightedAvg(data[:x], weights[:x]), range(1, len(data)+1))

days = range(1, len(data)+1)
openingWeight = result

plt.plot(days, data, 'bo')
plt.plot(days, result, 'ro')
plt.plot(days, data, 'b', label="Actual Weight")
plt.plot(days, result, 'r', label="ESMAed Weight")
plt.legend(loc="upper left")
plt.show()
plt.savefig('../WeightTimeSeries.png')
