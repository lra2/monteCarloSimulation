from parameters import Parameters
from variable import Variable

def setParametersBasedOnDistributionType(variable = Variable, distributionType="", minValue=0.0, mostLikelyValue=0.0, maxValue=0.0):
    _distributionType = distributionType

    variable.setVariableDistributionType(_distributionType)
    parameters = Parameters()
    if variable.getVariableDistributionType() == "Uniform":
        return variable.setUniformParameters(parameters, minValue, maxValue)

    elif variable.getVariableDistributionType() == "Triangular":
        return variable.setTriangularParameters(parameters, minValue, mostLikelyValue, maxValue)

    elif variable.getVariableDistributionType() == "Simple":
        return variable.setFixedParameters(parameters, mostLikelyValue)
    
def isUniformParametersIncorrect(variable):
    if variable.getVariableParameters().Minimum > variable.getVariableParameters().Maximum:
        print("Minimum value cannot be greater than maximum value.")
        return True
    
def isTriangularParametersIncorrect(variable):
    if variable.getVariableParameters().Minimum > variable.getVariableParameters().MostLikely:
        print("Minimum value cannot be greater than most likely value.")
        return True
        
    elif variable.getVariableParameters().Minimum > variable.getVariableParameters().Maximum:
        print("Minimum value cannot be greater than maximum value.")
        return True