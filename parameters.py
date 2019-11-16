class Parameters:
    def __init__(self, minimum = 0.0, maximum = 0.0, mostLikely = 0.0, fixedValue = 0.0):
        self.Minimum = minimum
        self.Maximum = maximum
        self.MostLikely = mostLikely
        self.FixedValue = fixedValue
    
    def setMinimum(self, minimum):
        self.Minimum = minimum

    def setMaximum(self, maximum):
        self.Maximum = maximum
    
    def setMostLikely(self, mostLikely):
        self.MostLikely = mostLikely
    
    def setFixedValue(self, fixedValue):
        self.FixedValue = fixedValue
    
    def getMinimum(self):
        return self.Minimum
    
    def getMaximum(self):
        return self.Maximum

    def getMostLikely(self):
        return self.MostLikely
    
    def getFixedValue(self):
        return self.FixedValue