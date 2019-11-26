import numpy as np
import random
import math
from parameters import Parameters
from variable import Variable

def getProbabilityBasedOnDistributionType(variable = Variable):
    distributionType = variable.getVariableDistributionType()
    variableParameters = variable.getVariableParameters()

    if distributionType == "Uniform":
        return getUniformProbability(variableParameters)
    elif distributionType == "Triangular":
        return getTriangularProbability(variableParameters)
    else:
        return getSingleProbability(variableParameters)

def getUniformProbability(parameters):
    return np.random.uniform(low=parameters.Minimum, high=parameters.Maximum)

def getTriangularProbability(parameters):
    return np.random.triangular(left=parameters.Minimum, mode=parameters.MostLikely, right=parameters.Maximum)

def getSingleProbability(parameters):
    return parameters.FixedValue

def calculateReserve(unitSystem = "", area = 0.0, thickness = 0.0, porosity = 0.0, waterSaturation = 0.0, recoveryFactor = 0.0, formationVolume = 0.0):
    recoverableOil = 0.0 #Np
    reserveConst = 7758

    numerator = area*thickness*porosity*(1 - waterSaturation)
    denominator = formationVolume

    if unitSystem == "USCS":
        numerator *= reserveConst
    
    recoverableOil = (numerator/denominator)*recoveryFactor
    return recoverableOil