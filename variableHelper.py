from parameters import Parameters
from variable import Variable

def setParametersBasedOnDistributionType(variable = Variable):
    _distributionType = input("Enter distribution type for " + variable.getVariableName() + ":")

    variable.setVariableDistributionType(_distributionType)
    parameters = Parameters()
    if variable.getVariableDistributionType() == "Uniform":
        return variable.setUniformParameters(parameters)

        if isUniformParametersIncorrect(variable):
            setParametersBasedOnDistributionType(variable)
            return variable.setUniformParameters(parameters)

    elif variable.getVariableDistributionType() == "Triangular":
        return variable.setTriangularParameters(parameters)

        if isTriangularParametersIncorrect(variable):
            setParametersBasedOnDistributionType(variable)
            return variable.setTriangularParameters(parameters)

    elif variable.getVariableDistributionType() == "Single":
        return variable.setFixedParameters(parameters)
            
    else:
        print("Invalid Distribution Type. Please try again!")
        setParametersBasedOnDistributionType(variable)
    
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