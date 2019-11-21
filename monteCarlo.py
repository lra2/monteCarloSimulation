import matplotlib.pyplot as plt
import numpy as np
import random
from parameters import Parameters
from variable import Variable
import variableHelper
import calculationHelper

numberOfSamples = 10000

porosity = Variable()
porosity.setVariableName("Porosity")
variableHelper.setParametersBasedOnDistributionType(porosity)
porosityProbability = calculationHelper.getProbabilityBasedOnDistributionType(porosity)

area = Variable()
area.setVariableName("Area")
variableHelper.setParametersBasedOnDistributionType(area)
areaProbability = calculationHelper.getProbabilityBasedOnDistributionType(area)

payZone = Variable()
payZone.setVariableName("Pay Zone")
variableHelper.setParametersBasedOnDistributionType(payZone)
payZoneProbability = calculationHelper.getProbabilityBasedOnDistributionType(payZone)

waterSaturation = Variable()
waterSaturation.setVariableName("Water Saturation")
variableHelper.setParametersBasedOnDistributionType(waterSaturation)
waterSaturationProbability = calculationHelper.getProbabilityBasedOnDistributionType(waterSaturation)

formationVolumeFactor = Variable()
formationVolumeFactor.setVariableName("Formation Volume Factor")
variableHelper.setParametersBasedOnDistributionType(formationVolumeFactor)
formationVolumeFactorProbability = calculationHelper.getProbabilityBasedOnDistributionType(formationVolumeFactor)

recoveryFactor = Variable()
recoveryFactor.setVariableName("Recovery Factor")
variableHelper.setParametersBasedOnDistributionType(recoveryFactor)
recoveryFactorProbability = calculationHelper.getProbabilityBasedOnDistributionType(recoveryFactor)

npValues = []
for i in range(numberOfSamples):
    #create and calculate variables
    #Check chosen unit system, and if necessary perform value conversion
    npValue = calculationHelper.calculateReserve("SI", area=areaProbability, payZone=payZoneProbability, porosity=porosityProbability, waterSaturation=waterSaturationProbability, recoveryFactor=recoveryFactorProbability, formationVolume=formationVolumeFactorProbability)
    npValues.append(npValue)

npValuesAverage = np.mean(npValues)