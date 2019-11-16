import matplotlib.pyplot as plt
import numpy as np
import random
from parameters import Parameters
from variable import Variable
import variableHelper
import calculationHelper

porosity = Variable()
porosity.setVariableName("Porosity")
variableHelper.setParametersBasedOnDistributionType(porosity)
porosityProbability = calculationHelper.getProbabilityBasedOnDistributionType(porosity)
#print(porosityProbability)

area = Variable()
area.setVariableName("Area")
variableHelper.setParametersBasedOnDistributionType(area)
areaProbability = calculationHelper.getProbabilityBasedOnDistributionType(area)
#print(areaProbability)

payZone = Variable()
payZone.setVariableName("Pay Zone")
variableHelper.setParametersBasedOnDistributionType(payZone)
payZoneProbability = calculationHelper.getProbabilityBasedOnDistributionType(payZone)
#print(payZoneProbability)

saturation = Variable()
saturation.setVariableName("Water Saturation")
variableHelper.setParametersBasedOnDistributionType(saturation)
saturationProbability = calculationHelper.getProbabilityBasedOnDistributionType(saturation)
#print(saturationProbability)

bo = Variable()
bo.setVariableName("B0")
variableHelper.setParametersBasedOnDistributionType(bo)
boProbability = calculationHelper.getProbabilityBasedOnDistributionType(bo)
#print(boProbability)

factor = Variable()
factor.setVariableName("Factor Rec.")
variableHelper.setParametersBasedOnDistributionType(factor)
factorProbability = calculationHelper.getProbabilityBasedOnDistributionType(factor)
#print(factorProbability)