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
    
    def setUniformParameters(self, parameters, minimumValue=0.0, maximumValue=0.0):
        parameters.setMinimum(minimumValue)
        parameters.setMaximum(maximumValue)
        self.setVariableParameters(parameters)
    
    def setTriangularParameters(self, parameters, minimumValue=0.0, mostLikelyValue=0.0, maximumValue=0.0):
        parameters.setMinimum(minimumValue)
        parameters.setMostLikely(mostLikelyValue)
        parameters.setMaximum(maximumValue)
        self.setVariableParameters(parameters)
    
    def setFixedParameters(self, parameters, mostLikelyValue=0.0):
        parameters.setFixedValue(mostLikelyValue)
        self.setVariableParameters(parameters)