import numpy as np
import matplotlib.pyplot as plt

data = [99.1, 99.2, 99.6, 98.1]

eSC = 2

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
plt.savefig("C:\Users\Nipun\Desktop\WeightTimeSeries.png")