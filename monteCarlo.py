import matplotlib.pyplot as plt
import numpy as np
import random
import statistics
from parameters import Parameters
from variable import Variable
import variableHelper
import calculationHelper

NUMBER_OF_SAMPLES = 10000

area = Variable()
area.setVariableName("Area")
variableHelper.setParametersBasedOnDistributionType(area)

thickness = Variable()
thickness.setVariableName("Thickness")
variableHelper.setParametersBasedOnDistributionType(thickness)

porosity = Variable()
porosity.setVariableName("Porosity")
variableHelper.setParametersBasedOnDistributionType(porosity)

waterSaturation = Variable()
waterSaturation.setVariableName("Water Saturation")
variableHelper.setParametersBasedOnDistributionType(waterSaturation)

recoveryFactor = Variable()
recoveryFactor.setVariableName("Recovery Factor")
variableHelper.setParametersBasedOnDistributionType(recoveryFactor)

formationVolumeFactor = Variable()
formationVolumeFactor.setVariableName("Formation Volume Factor")
variableHelper.setParametersBasedOnDistributionType(formationVolumeFactor)

unitySystem = input("Choose the unity system (SI or USCS): ")

npValues = []
for i in range(NUMBER_OF_SAMPLES):
    areaProbability = 0.0
    thicknessProbability = 0.0
    porosityProbability = 0.0
    waterSaturationProbability = 0.0
    recoveryFactorProbability = 0.0
    formationVolumeFactorProbability = 0.0

    areaProbability = calculationHelper.getProbabilityBasedOnDistributionType(area)
    thicknessProbability = calculationHelper.getProbabilityBasedOnDistributionType(thickness)
    porosityProbability = calculationHelper.getProbabilityBasedOnDistributionType(porosity)
    waterSaturationProbability = calculationHelper.getProbabilityBasedOnDistributionType(waterSaturation)
    recoveryFactorProbability = calculationHelper.getProbabilityBasedOnDistributionType(recoveryFactor)
    formationVolumeFactorProbability = calculationHelper.getProbabilityBasedOnDistributionType(formationVolumeFactor)

    npValue = calculationHelper.calculateReserve(unitSystem=unitySystem, 
                                area=areaProbability,
                                thickness=thicknessProbability,
                                porosity=porosityProbability,
                                waterSaturation=waterSaturationProbability,
                                recoveryFactor=recoveryFactorProbability,
                                formationVolume=formationVolumeFactorProbability)
    npValues.append(npValue)

npValuesAverage = np.mean(npValues, dtype=np.float64)
standardDeviation = statistics.pstdev(npValues, mu=None)
num_bins = NUMBER_OF_SAMPLES

fig, ax = plt.subplots()

n, bins, patches = ax.hist(npValues, num_bins, density=1)

y = ((1 / (np.sqrt(2 * np.pi) * standardDeviation)) *
     np.exp(-0.5 * (1 / standardDeviation * (bins - npValuesAverage))**2))

ax.plot(bins, y, '--')
ax.set_xlabel('Np')
ax.set_ylabel('Y')

fig.tight_layout()
plt.show()