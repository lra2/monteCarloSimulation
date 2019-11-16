import numpy as np
import random
from parameters import Parameters
from variable import Variable

e = 2.71828182846
PI = 3.14159265359

def getProbabilityBasedOnDistributionType(variable = Variable):
    distributionType = variable.getVariableDistributionType()
    variableParameters = variable.getVariableParameters()

    if distributionType == "Uniform":
        return getUniformProbability(variableParameters)
    elif distributionType == "Triangular":
        return getTriangularProbability(variableParameters)
    else:
        return getNormalProbability(variableParameters)

def getUniformProbability(parameters):
    range = parameters.Maximum - parameters.Minimum
    choice = random.uniform(parameters.Minimum, parameters.Maximum)
    return parameters.Minimum + range * choice

def getTriangularProbability(parameters):
    return random.triangular(parameters.Minimum, parameters.Maximum, parameters.MostLikely)

def getNormalProbability(parameters):
    return np.random.normal(parameters.FixedValue)

def f_of_x(x):
    return (e**(-1*x))/(1+(x-1)**2)

def getVariance(probability, numSamples):
    runningTotal = 0

    for i in range(numSamples):
        runningTotal += f_of_x(probability)**2
    sumOfSquares = runningTotal * probability / numSamples

    runningTotal = 0

    for i in range(numSamples):
        runningTotal += f_of_x(probability)
    squareAverage = (probability * runningTotal / numSamples)**2

    return sumOfSquares - squareAverage