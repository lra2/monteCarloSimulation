import numpy as np
import random
import math
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

def g_of_x(x, A, lamda):
    return A*math.pow(e, -1*lamda*x)

def inverse_G_of_r(r, lamda):
    return (-1 * math.log(float(r)))/lamda

def getImportanceSamplingVariance(probability, lamda, numSamples):
    A = lamda
    int_max = 5 #mudar
    
    runnigTotal = 0
    for i in range(numSamples):
        runnigTotal += (f_of_x(probability) / g_of_x(probability, A, lamda))**2
    sumOfSquares = runnigTotal / numSamples

    runnigTotal = 0
    for i in range(numSamples):
        runnigTotal += f_of_x(probability) / g_of_x(probability, A, lamda)
    squareOfAverage = (runnigTotal / numSamples)**2

    return sumOfSquares - squareOfAverage

def getOptimalLambda(probability, lambdaSamples, numSamples):
    testLambdas = [i*0.05 for i in range(lambdaSamples)]
    variances = []

    for i, lamda in enumerate(testLambdas):
        variances.append(getImportanceSamplingVariance(probability, lamda, numSamples))
    
    return testLambdas[np.argmin(np.asarray(variances))]

def getOptimalVariance(probability, lambdaSamples, numSamples):
    testLambdas = [i*0.05 for i in range(lambdaSamples)]
    variances = []

    for i, lamda in enumerate(testLambdas):
        variances.append(getImportanceSamplingVariance(probability, lamda, numSamples))
    
    return variances[np.argmin(np.asarray(variances))]

def importanteSamplingMonteCarlo(probability, lamda, numSamples):
    A = lamda

    runningTotal = 0
    for i in range(numSamples):
        runningTotal += f_of_x(inverse_G_of_r(probability, lamda=lamda))/g_of_x(inverse_G_of_r(probability, lamda=lamda), A, lamda)
    approximation = float(runningTotal/numSamples)
    return approximation

def calculateReserve(unitSystem = "", area = 0.0, payZone = 0.0, porosity = 0.0, waterSaturation = 0.0, recoveryFactor = 0.0, formationVolume = 0.0):
    recoverableOil = 0.0 #Np
    reserveConst = 7758

    numerator = area*payZone*porosity*(1 - waterSaturation)
    denominator = formationVolume

    if unitSystem == "UA":
        numerator *= reserveConst
    
    recoverableOil = (numerator/denominator)*recoveryFactor
    return recoverableOil