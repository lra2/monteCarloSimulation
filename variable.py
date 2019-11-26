from parameters import Parameters

class Variable(Parameters):
    def __init__(self, parameters = Parameters, name = "", distributionType = ""):
        self.Name = name
        self.Parameters = parameters
        self.DistributionType = distributionType
    
    def setVariableName(self, name):
        self.Name = name
    
    def setVariableDistributionType(self, distributionType):
        self.DistributionType = distributionType
    
    def setVariableParameters(self, parameters):
        self.Parameters = parameters
    
    def getVariableName(self):
        return self.Name
    
    def getVariableDistributionType(self):
        return self.DistributionType
    
    def getVariableParameters(self):
        return self.Parameters
    
    def setUniformParameters(self, parameters):
        _minimumValue = float(input("Enter minimum value for " + self.getVariableName() + ": "))
        parameters.setMinimum(_minimumValue)

        _maximumValue = float(input("Enter maximum value for " + self.getVariableName() + ": "))
        parameters.setMaximum(_maximumValue)

        self.setVariableParameters(parameters)
    
    def setTriangularParameters(self, parameters):
        _minimumValue = float(input("Enter minimum value for " + self.getVariableName() + ": "))
        parameters.setMinimum(_minimumValue)

        _mostLikelyValue = float(input("Enter most likely value for " + self.getVariableName() + ": "))
        parameters.setMostLikely(_mostLikelyValue)

        _maximumValue = float(input("Enter maximum value for " + self.getVariableName() + ": "))
        parameters.setMaximum(_maximumValue)

        self.setVariableParameters(parameters)
    
    def setFixedParameters(self, parameters):
        _fixedValue = float(input("Enter value for " + self.getVariableName() + ": "))
        parameters.setFixedValue(_fixedValue)

        self.setVariableParameters(parameters)