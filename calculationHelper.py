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
    return random.uniform(parameters.Minimum, parameters.Maximum)

def getTriangularProbability(parameters):
    return random.triangular(low=parameters.Minimum, high=parameters.Maximum, mode=parameters.MostLikely)

def getSingleProbability(parameters):
    return parameters.FixedValue

def calculateReserve(unitSystem = "", area = 0.0, thickness = 0.0, porosity = 0.0, waterSaturation = 0.0, recoveryFactor = 0.0, formationVolume = 0.0):
    recoverableOil = 0.0 #Np
    reserveConst = 7758.0000

    numerator = area*thickness*porosity*(1 - waterSaturation)
    denominator = formationVolume

    if unitSystem == "USCS":
        numerator *= reserveConst
    
    if denominator != 0:
        recoverableOil = (numerator/denominator)*recoveryFactor
    return recoverableOil