import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import statistics
from tkinter import *
from tkinter import filedialog
from parameters import Parameters
from variable import Variable
import variableHelper
import calculationHelper

NUMBER_OF_SAMPLES = 10000

class Simulation:
    def __init__(self, master=None):
        master.title('Monte Carlo Simulation')

        self.DefaultFont = ("Calibri", "10")

        self.areaValues = []
        self.thicknessValues = []
        self.porosityValues = []
        self.waterSaturationValues = []
        self.recoveryFactorValues = []
        self.formationVolumeFactorValues = []
        self.npValues = []

        self.parametersDataContainer = Frame(master)
        self.parametersDataContainer["pady"] = 10
        self.parametersDataContainer.pack()

        self.parametersTitle = Label(self.parametersDataContainer, text="Enter parameters for simulation")
        self.parametersTitle["font"] = ("Calibri", "14", "bold")
        self.parametersTitle.pack(side=TOP)

        self.parametersHint = Label(self.parametersDataContainer, text="Parameters order: Min, Likely, Max")
        self.parametersHint["font"] = ("Calibri", "10")
        self.parametersHint.pack(side=BOTTOM)

        #Containers
        self.areaContainer = Frame(master)
        self.areaContainer["padx"] = 20
        self.areaContainer["pady"] = 10
        self.areaContainer.pack()

        self.thicknessContainer = Frame(master)
        self.thicknessContainer["padx"] = 20
        self.thicknessContainer["pady"] = 10
        self.thicknessContainer.pack()

        self.porosityContainer = Frame(master)
        self.porosityContainer["padx"] = 20
        self.porosityContainer["pady"] = 10
        self.porosityContainer.pack()

        self.waterSaturationContainer = Frame(master)
        self.waterSaturationContainer["padx"] = 20
        self.waterSaturationContainer["pady"] = 10
        self.waterSaturationContainer.pack()

        self.recoveryFactorContainer = Frame(master)
        self.recoveryFactorContainer["padx"] = 20
        self.recoveryFactorContainer["pady"] = 10
        self.recoveryFactorContainer.pack()

        self.formationVolumeFactorContainer = Frame(master)
        self.formationVolumeFactorContainer["padx"] = 20
        self.formationVolumeFactorContainer["pady"] = 10
        self.formationVolumeFactorContainer.pack()

        self.unitySystemContainer = Frame(master)
        self.unitySystemContainer["padx"] = 20
        self.unitySystemContainer["pady"] = 10
        self.unitySystemContainer.pack()

        #Labels
        self.areaLabel = Label(self.areaContainer, text="Area", font=self.DefaultFont)
        self.areaLabel.pack(side=LEFT)

        self.thicknessLabel = Label(self.thicknessContainer, text="Thickness", font=self.DefaultFont)
        self.thicknessLabel.pack(side=LEFT)

        self.porosityLabel = Label(self.porosityContainer, text="Porosity", font=self.DefaultFont)
        self.porosityLabel.pack(side=LEFT)

        self.waterSaturationLabel = Label(self.waterSaturationContainer, text="Water Saturation", font=self.DefaultFont)
        self.waterSaturationLabel.pack(side=LEFT)

        self.recoveryFactorLabel = Label(self.recoveryFactorContainer, text="Recovery Factor", font=self.DefaultFont)
        self.recoveryFactorLabel.pack(side=LEFT)

        self.formationVolumeLabel = Label(self.formationVolumeFactorContainer, text="Formation Volume Factor", font=self.DefaultFont)
        self.formationVolumeLabel.pack(side=LEFT)

        self.unitySystemLabel = Label(self.unitySystemContainer, text="Choose the unity system", font=self.DefaultFont)
        self.unitySystemLabel.pack(side=LEFT)

        #Area fields
        self.minAreaEntry = Entry(self.areaContainer)
        self.minAreaEntry["width"] = 10
        self.minAreaEntry["font"] = self.DefaultFont
        self.minAreaEntry["justify"] = "center"
        self.minAreaEntry.config(state=DISABLED)
        self.minAreaEntry.pack(side=LEFT, padx=5)

        self.singleAreaEntry = Entry(self.areaContainer)
        self.singleAreaEntry["width"] = 10
        self.singleAreaEntry["font"] = self.DefaultFont
        self.singleAreaEntry["justify"] = "center"
        self.singleAreaEntry.pack(side=LEFT, padx=5)

        self.maxAreaEntry = Entry(self.areaContainer)
        self.maxAreaEntry["width"] = 10
        self.maxAreaEntry["font"] = self.DefaultFont
        self.maxAreaEntry["justify"] = "center"
        self.maxAreaEntry.config(state=DISABLED)
        self.maxAreaEntry.pack(side=LEFT, padx=5)

        self.areaTriangularDistributionCheckbox = Radiobutton(self.areaContainer)
        self.areaTriangularDistributionCheckbox["text"] = "Triangular Dist."
        self.areaTriangularDistributionCheckbox["value"] = 'Triangular'
        self.areaTriangularDistributionCheckbox["variable"] = areaDistributionTypeChoice
        self.areaTriangularDistributionCheckbox["command"] = self.handleAreaDistributionChoice
        self.areaTriangularDistributionCheckbox.pack(side=RIGHT)

        self.areaUniformDistributionCheckbox = Radiobutton(self.areaContainer)
        self.areaUniformDistributionCheckbox["text"] = "Uniform Dist."
        self.areaUniformDistributionCheckbox["value"] = 'Uniform'
        self.areaUniformDistributionCheckbox["variable"] = areaDistributionTypeChoice
        self.areaUniformDistributionCheckbox["command"] = self.handleAreaDistributionChoice
        self.areaUniformDistributionCheckbox.pack(side=RIGHT)

        self.areaSingleDistributionCheckbox = Radiobutton(self.areaContainer)
        self.areaSingleDistributionCheckbox["text"] = "Single Dist."
        self.areaSingleDistributionCheckbox["value"] = 'Simple'
        self.areaSingleDistributionCheckbox["variable"] = areaDistributionTypeChoice
        self.areaSingleDistributionCheckbox["command"] = self.handleAreaDistributionChoice
        self.areaSingleDistributionCheckbox.pack(side=RIGHT)

        #Thickness Fields
        self.minThicknessEntry = Entry(self.thicknessContainer)
        self.minThicknessEntry["width"] = 10
        self.minThicknessEntry["font"] = self.DefaultFont
        self.minThicknessEntry["justify"] = "center"
        self.minThicknessEntry.config(state=DISABLED)
        self.minThicknessEntry.pack(side=LEFT, padx=5)

        self.singleThicknessEntry = Entry(self.thicknessContainer)
        self.singleThicknessEntry["width"] = 10
        self.singleThicknessEntry["font"] = self.DefaultFont
        self.singleThicknessEntry["justify"] = "center"
        self.singleThicknessEntry.config(state=NORMAL)
        self.singleThicknessEntry.pack(side=LEFT, padx=5)

        self.maxThicknessEntry = Entry(self.thicknessContainer)
        self.maxThicknessEntry["width"] = 10
        self.maxThicknessEntry["font"] = self.DefaultFont
        self.maxThicknessEntry["justify"] = "center"
        self.maxThicknessEntry.config(state=DISABLED)
        self.maxThicknessEntry.pack(side=LEFT, padx=5)

        self.thicknessTriangularDistributionCheckbox = Radiobutton(self.thicknessContainer)
        self.thicknessTriangularDistributionCheckbox["text"] = "Triangular Dist."
        self.thicknessTriangularDistributionCheckbox["value"] = 'Triangular'
        self.thicknessTriangularDistributionCheckbox["variable"] = thicknessDistributionChoice
        self.thicknessTriangularDistributionCheckbox["command"] = self.handleThicknessDistributionChoice
        self.thicknessTriangularDistributionCheckbox.pack(side=RIGHT)

        self.thicknessUniformDistributionCheckbox = Radiobutton(self.thicknessContainer)
        self.thicknessUniformDistributionCheckbox["text"] = "Uniform Dist."
        self.thicknessUniformDistributionCheckbox["value"] = 'Uniform'
        self.thicknessUniformDistributionCheckbox["variable"] = thicknessDistributionChoice
        self.thicknessUniformDistributionCheckbox["command"] = self.handleThicknessDistributionChoice
        self.thicknessUniformDistributionCheckbox.pack(side=RIGHT)

        self.thicknessSingleDistributionCheckbox = Radiobutton(self.thicknessContainer)
        self.thicknessSingleDistributionCheckbox["text"] = "Single Dist."
        self.thicknessSingleDistributionCheckbox["value"] = 'Simple'
        self.thicknessSingleDistributionCheckbox["variable"] = thicknessDistributionChoice
        self.thicknessSingleDistributionCheckbox["command"] = self.handleThicknessDistributionChoice
        self.thicknessSingleDistributionCheckbox.pack(side=RIGHT)

        #Porosity Fields
        self.minPorosityEntry = Entry(self.porosityContainer)
        self.minPorosityEntry["width"] = 10
        self.minPorosityEntry["font"] = self.DefaultFont
        self.minPorosityEntry["justify"] = "center"
        self.minPorosityEntry.config(state=DISABLED)
        self.minPorosityEntry.pack(side=LEFT, padx=5)

        self.singlePorosityEntry = Entry(self.porosityContainer)
        self.singlePorosityEntry["width"] = 10
        self.singlePorosityEntry["font"] = self.DefaultFont
        self.singlePorosityEntry["justify"] = "center"
        self.singlePorosityEntry.config(state=NORMAL)
        self.singlePorosityEntry.pack(side=LEFT, padx=5)

        self.maxPorosityEntry = Entry(self.porosityContainer)
        self.maxPorosityEntry["width"] = 10
        self.maxPorosityEntry["font"] = self.DefaultFont
        self.maxPorosityEntry["justify"] = "center"
        self.maxPorosityEntry.config(state=DISABLED)
        self.maxPorosityEntry.pack(side=LEFT, padx=5)

        self.porosityTriangularDistributionCheckbox = Radiobutton(self.porosityContainer)
        self.porosityTriangularDistributionCheckbox["text"] = "Triangular Dist."
        self.porosityTriangularDistributionCheckbox["value"] = 'Triangular'
        self.porosityTriangularDistributionCheckbox["variable"] = porosityDistributionChoice
        self.porosityTriangularDistributionCheckbox["command"] = self.handlePorosityDistributionChoice
        self.porosityTriangularDistributionCheckbox.pack(side=RIGHT)

        self.porosityUniformDistributionCheckbox = Radiobutton(self.porosityContainer)
        self.porosityUniformDistributionCheckbox["text"] = "Uniform Dist."
        self.porosityUniformDistributionCheckbox["value"] = 'Uniform'
        self.porosityUniformDistributionCheckbox["variable"] = porosityDistributionChoice
        self.porosityUniformDistributionCheckbox["command"] = self.handlePorosityDistributionChoice
        self.porosityUniformDistributionCheckbox.pack(side=RIGHT)

        self.porositySingleDistributionCheckbox = Radiobutton(self.porosityContainer)
        self.porositySingleDistributionCheckbox["text"] = "Single Dist."
        self.porositySingleDistributionCheckbox["value"] = 'Simple'
        self.porositySingleDistributionCheckbox["variable"] = porosityDistributionChoice
        self.porositySingleDistributionCheckbox["command"] = self.handlePorosityDistributionChoice
        self.porositySingleDistributionCheckbox.pack(side=RIGHT)

        #Water Saturation Fields
        self.minWaterSaturationEntry = Entry(self.waterSaturationContainer)
        self.minWaterSaturationEntry["width"] = 10
        self.minWaterSaturationEntry["font"] = self.DefaultFont
        self.minWaterSaturationEntry["justify"] = "center"
        self.minWaterSaturationEntry.config(state=DISABLED)
        self.minWaterSaturationEntry.pack(side=LEFT, padx=5)

        self.singleWaterSaturationEntry = Entry(self.waterSaturationContainer)
        self.singleWaterSaturationEntry["width"] = 10
        self.singleWaterSaturationEntry["font"] = self.DefaultFont
        self.singleWaterSaturationEntry["justify"] = "center"
        self.singleWaterSaturationEntry.config(state=NORMAL)
        self.singleWaterSaturationEntry.pack(side=LEFT, padx=5)

        self.maxWaterSaturationEntry = Entry(self.waterSaturationContainer)
        self.maxWaterSaturationEntry["width"] = 10
        self.maxWaterSaturationEntry["font"] = self.DefaultFont
        self.maxWaterSaturationEntry["justify"] = "center"
        self.maxWaterSaturationEntry.config(state=DISABLED)
        self.maxWaterSaturationEntry.pack(side=LEFT, padx=5)

        self.waterSaturationTriangularDistributionCheckbox = Radiobutton(self.waterSaturationContainer)
        self.waterSaturationTriangularDistributionCheckbox["text"] = "Triangular Dist."
        self.waterSaturationTriangularDistributionCheckbox["value"] = 'Triangular'
        self.waterSaturationTriangularDistributionCheckbox["variable"] = waterSaturationDistributionChoice
        self.waterSaturationTriangularDistributionCheckbox["command"] = self.handleWaterSaturationDistributionChoice
        self.waterSaturationTriangularDistributionCheckbox.pack(side=RIGHT)

        self.waterSaturationUniformDistributionCheckbox = Radiobutton(self.waterSaturationContainer)
        self.waterSaturationUniformDistributionCheckbox["text"] = "Uniform Dist."
        self.waterSaturationUniformDistributionCheckbox["value"] = 'Uniform'
        self.waterSaturationUniformDistributionCheckbox["variable"] = waterSaturationDistributionChoice
        self.waterSaturationUniformDistributionCheckbox["command"] = self.handleWaterSaturationDistributionChoice
        self.waterSaturationUniformDistributionCheckbox.pack(side=RIGHT)

        self.waterSaturationSingleDistributionCheckbox = Radiobutton(self.waterSaturationContainer)
        self.waterSaturationSingleDistributionCheckbox["text"] = "Single Dist."
        self.waterSaturationSingleDistributionCheckbox["value"] = 'Simple'
        self.waterSaturationSingleDistributionCheckbox["variable"] = waterSaturationDistributionChoice
        self.waterSaturationSingleDistributionCheckbox["command"] = self.handleWaterSaturationDistributionChoice
        self.waterSaturationSingleDistributionCheckbox.pack(side=RIGHT)

        #Recovery Factor Fields
        self.minRecoveryFactorEntry = Entry(self.recoveryFactorContainer)
        self.minRecoveryFactorEntry["width"] = 10
        self.minRecoveryFactorEntry["font"] = self.DefaultFont
        self.minRecoveryFactorEntry["justify"] = "center"
        self.minRecoveryFactorEntry.config(state=DISABLED)
        self.minRecoveryFactorEntry.pack(side=LEFT, padx=5)

        self.singleRecoveryFactorEntry = Entry(self.recoveryFactorContainer)
        self.singleRecoveryFactorEntry["width"] = 10
        self.singleRecoveryFactorEntry["font"] = self.DefaultFont
        self.singleRecoveryFactorEntry["justify"] = "center"
        self.singleRecoveryFactorEntry.config(state=NORMAL)
        self.singleRecoveryFactorEntry.pack(side=LEFT, padx=5)

        self.maxRecoveryFactorEntry = Entry(self.recoveryFactorContainer)
        self.maxRecoveryFactorEntry["width"] = 10
        self.maxRecoveryFactorEntry["font"] = self.DefaultFont
        self.maxRecoveryFactorEntry["justify"] = "center"
        self.maxRecoveryFactorEntry.config(state=DISABLED)
        self.maxRecoveryFactorEntry.pack(side=LEFT, padx=5)

        self.recoveryFactorTriangularDistributionCheckbox = Radiobutton(self.recoveryFactorContainer)
        self.recoveryFactorTriangularDistributionCheckbox["text"] = "Triangular Dist."
        self.recoveryFactorTriangularDistributionCheckbox["value"] = 'Triangular'
        self.recoveryFactorTriangularDistributionCheckbox["variable"] = recoveryFactorDistributionChoice
        self.recoveryFactorTriangularDistributionCheckbox["command"] = self.handleRecoveryFactorDistributionChoice
        self.recoveryFactorTriangularDistributionCheckbox.pack(side=RIGHT)

        self.recoveryFactorUniformDistributionCheckbox = Radiobutton(self.recoveryFactorContainer)
        self.recoveryFactorUniformDistributionCheckbox["text"] = "Uniform Dist."
        self.recoveryFactorUniformDistributionCheckbox["value"] = 'Uniform'
        self.recoveryFactorUniformDistributionCheckbox["variable"] = recoveryFactorDistributionChoice
        self.recoveryFactorUniformDistributionCheckbox["command"] = self.handleRecoveryFactorDistributionChoice
        self.recoveryFactorUniformDistributionCheckbox.pack(side=RIGHT)

        self.recoveryFactorSingleDistributionCheckbox = Radiobutton(self.recoveryFactorContainer)
        self.recoveryFactorSingleDistributionCheckbox["text"] = "Single Dist."
        self.recoveryFactorSingleDistributionCheckbox["value"] = 'Simple'
        self.recoveryFactorSingleDistributionCheckbox["variable"] = recoveryFactorDistributionChoice
        self.recoveryFactorSingleDistributionCheckbox["command"] = self.handleRecoveryFactorDistributionChoice
        self.recoveryFactorSingleDistributionCheckbox.pack(side=RIGHT)

        #Formation Volume Factor Fields
        self.minFormationVolumeFactorEntry = Entry(self.formationVolumeFactorContainer)
        self.minFormationVolumeFactorEntry["width"] = 10
        self.minFormationVolumeFactorEntry["font"] = self.DefaultFont
        self.minFormationVolumeFactorEntry["justify"] = "center"
        self.minFormationVolumeFactorEntry.config(state=DISABLED)
        self.minFormationVolumeFactorEntry.pack(side=LEFT, padx=5)

        self.singleFormationVolumeFactorEntry = Entry(self.formationVolumeFactorContainer)
        self.singleFormationVolumeFactorEntry["width"] = 10
        self.singleFormationVolumeFactorEntry["font"] = self.DefaultFont
        self.singleFormationVolumeFactorEntry["justify"] = "center"
        self.singleFormationVolumeFactorEntry.config(state=NORMAL)
        self.singleFormationVolumeFactorEntry.pack(side=LEFT, padx=5)

        self.maxFormationVolumeFactorEntry = Entry(self.formationVolumeFactorContainer)
        self.maxFormationVolumeFactorEntry["width"] = 10
        self.maxFormationVolumeFactorEntry["font"] = self.DefaultFont
        self.maxFormationVolumeFactorEntry["justify"] = "center"
        self.maxFormationVolumeFactorEntry.config(state=DISABLED)
        self.maxFormationVolumeFactorEntry.pack(side=LEFT, padx=5)

        self.formationVolumeFactorTriangularDistributionCheckbox = Radiobutton(self.formationVolumeFactorContainer)
        self.formationVolumeFactorTriangularDistributionCheckbox["text"] = "Triangular Dist."
        self.formationVolumeFactorTriangularDistributionCheckbox["value"] = 'Triangular'
        self.formationVolumeFactorTriangularDistributionCheckbox["variable"] = formationVolumeFactorDistributionChoice
        self.formationVolumeFactorTriangularDistributionCheckbox["command"] = self.handleFormationVolumeFactorDistributionChoice
        self.formationVolumeFactorTriangularDistributionCheckbox.pack(side=RIGHT)

        self.formationVolumeFactorUniformDistributionCheckbox = Radiobutton(self.formationVolumeFactorContainer)
        self.formationVolumeFactorUniformDistributionCheckbox["text"] = "Uniform Dist."
        self.formationVolumeFactorUniformDistributionCheckbox["value"] = 'Uniform'
        self.formationVolumeFactorUniformDistributionCheckbox["variable"] = formationVolumeFactorDistributionChoice
        self.formationVolumeFactorUniformDistributionCheckbox["command"] = self.handleFormationVolumeFactorDistributionChoice
        self.formationVolumeFactorUniformDistributionCheckbox.pack(side=RIGHT)

        self.formationVolumeFactorSingleDistributionCheckbox = Radiobutton(self.formationVolumeFactorContainer)
        self.formationVolumeFactorSingleDistributionCheckbox["text"] = "Single Dist."
        self.formationVolumeFactorSingleDistributionCheckbox["value"] = 'Simple'
        self.formationVolumeFactorSingleDistributionCheckbox["variable"] = formationVolumeFactorDistributionChoice
        self.formationVolumeFactorSingleDistributionCheckbox["command"] = self.handleFormationVolumeFactorDistributionChoice
        self.formationVolumeFactorSingleDistributionCheckbox.pack(side=RIGHT)

        #Unity System Field
        self.unitySystemUSCSCheckbox = Radiobutton(self.unitySystemContainer)
        self.unitySystemUSCSCheckbox["text"] = "USCS"
        self.unitySystemUSCSCheckbox["value"] = 'USCS'
        self.unitySystemUSCSCheckbox["variable"] = unitySystemChoice
        self.unitySystemUSCSCheckbox.pack(side=RIGHT)

        self.unitySystemSICheckbox = Radiobutton(self.unitySystemContainer)
        self.unitySystemSICheckbox["text"] = "SI"
        self.unitySystemSICheckbox["value"] = 'SI'
        self.unitySystemSICheckbox["variable"] = unitySystemChoice
        self.unitySystemSICheckbox.pack(side=RIGHT)

        self.buttonContainer = Frame(master)
        self.buttonContainer["pady"] = 20
        self.buttonContainer.pack()

        self.exportResultsButton = Button(self.buttonContainer)
        self.exportResultsButton["text"] = "Export Data"
        self.exportResultsButton["font"] = ("Calibri", "12")
        self.exportResultsButton["width"] = 15
        self.exportResultsButton["command"] = self.exportData
        self.exportResultsButton.config(state=DISABLED)
        self.exportResultsButton.pack(side=RIGHT)

        self.showHistogramButton = Button(self.buttonContainer)
        self.showHistogramButton["text"] = "Show Histogram"
        self.showHistogramButton["font"] = ("Calibri", "12")
        self.showHistogramButton["width"] = 15
        self.showHistogramButton["command"] = self.showHistogram
        self.showHistogramButton.config(state=DISABLED)
        self.showHistogramButton.pack(side=RIGHT)

        self.calculateButton = Button(self.buttonContainer)
        self.calculateButton["text"] = "Calculate"
        self.calculateButton["font"] = ("Calibri", "12", "bold")
        self.calculateButton["width"] = 12
        self.calculateButton["padx"] = 15
        self.calculateButton["command"] = self.calculate
        self.calculateButton.pack(side=LEFT)

        self.resultContainer = Frame(master)
        self.resultContainer["pady"] = 15
        self.resultContainer.pack()

        self.result = Label(self.resultContainer, text="", font=("Calibri", "12", "bold"))
        self.result.pack()

    def calculate(self):
        #Unity System Choice
        _unitySystemChoice = unitySystemChoice.get()
        self.setAllParameters()
        self.npResults = runSimulation(_unitySystemChoice, area, thickness, porosity, waterSaturation, recoveryFactor, formationVolumeFactor, self)
        self.npAverage = round(np.mean(self.npResults, dtype=np.float64), 2)

        if self.npAverage == 0:
            self.showHistogramButton.config(state=DISABLED)
            self.exportResultsButton.config(state=DISABLED)
        else:
            self.showHistogramButton.config(state=NORMAL)
            self.exportResultsButton.config(state=NORMAL)
        self.result["text"] = "Ev = " + str(self.npAverage)

    def handleAreaDistributionChoice(self):
        choice = areaDistributionTypeChoice.get()
        
        if choice == 'Simple':
            self.singleAreaEntry.config(state=NORMAL)
            self.minAreaEntry.config(state=DISABLED)
            self.maxAreaEntry.config(state=DISABLED)
        elif choice == 'Uniform':
            self.singleAreaEntry.config(state=DISABLED)
            self.minAreaEntry.config(state=NORMAL)
            self.maxAreaEntry.config(state=NORMAL)
        elif choice == 'Triangular':
            self.singleAreaEntry.config(state=NORMAL)
            self.minAreaEntry.config(state=NORMAL)
            self.maxAreaEntry.config(state=NORMAL)
    
    def handleThicknessDistributionChoice(self):
        choice = thicknessDistributionChoice.get()
        
        if choice == 'Simple':
            self.singleThicknessEntry.config(state=NORMAL)
            self.minThicknessEntry.config(state=DISABLED)
            self.maxThicknessEntry.config(state=DISABLED)
        elif choice == 'Uniform':
            self.singleThicknessEntry.config(state=DISABLED)
            self.minThicknessEntry.config(state=NORMAL)
            self.maxThicknessEntry.config(state=NORMAL)
        elif choice == 'Triangular':
            self.singleThicknessEntry.config(state=NORMAL)
            self.minThicknessEntry.config(state=NORMAL)
            self.maxThicknessEntry.config(state=NORMAL)
    
    def handlePorosityDistributionChoice(self):
        choice = porosityDistributionChoice.get()
        
        if choice == 'Simple':
            self.singlePorosityEntry.config(state=NORMAL)
            self.minPorosityEntry.config(state=DISABLED)
            self.maxPorosityEntry.config(state=DISABLED)
        elif choice == 'Uniform':
            self.singlePorosityEntry.config(state=DISABLED)
            self.minPorosityEntry.config(state=NORMAL)
            self.maxPorosityEntry.config(state=NORMAL)
        elif choice == 'Triangular':
            self.singlePorosityEntry.config(state=NORMAL)
            self.minPorosityEntry.config(state=NORMAL)
            self.maxPorosityEntry.config(state=NORMAL)
    
    def handleWaterSaturationDistributionChoice(self):
        choice = waterSaturationDistributionChoice.get()
        
        if choice == 'Simple':
            self.singleWaterSaturationEntry.config(state=NORMAL)
            self.minWaterSaturationEntry.config(state=DISABLED)
            self.maxWaterSaturationEntry.config(state=DISABLED)
        elif choice == 'Uniform':
            self.singleWaterSaturationEntry.config(state=DISABLED)
            self.minWaterSaturationEntry.config(state=NORMAL)
            self.maxWaterSaturationEntry.config(state=NORMAL)
        elif choice == 'Triangular':
            self.singleWaterSaturationEntry.config(state=NORMAL)
            self.minWaterSaturationEntry.config(state=NORMAL)
            self.maxWaterSaturationEntry.config(state=NORMAL)
    
    def handleRecoveryFactorDistributionChoice(self):
        choice = recoveryFactorDistributionChoice.get()
        
        if choice == 'Simple':
            self.singleRecoveryFactorEntry.config(state=NORMAL)
            self.minRecoveryFactorEntry.config(state=DISABLED)
            self.maxRecoveryFactorEntry.config(state=DISABLED)
        elif choice == 'Uniform':
            self.singleRecoveryFactorEntry.config(state=DISABLED)
            self.minRecoveryFactorEntry.config(state=NORMAL)
            self.maxRecoveryFactorEntry.config(state=NORMAL)
        elif choice == 'Triangular':
            self.singleRecoveryFactorEntry.config(state=NORMAL)
            self.minRecoveryFactorEntry.config(state=NORMAL)
            self.maxRecoveryFactorEntry.config(state=NORMAL)
    
    def handleFormationVolumeFactorDistributionChoice(self):
        choice = formationVolumeFactorDistributionChoice.get()
        
        if choice == 'Simple':
            self.singleFormationVolumeFactorEntry.config(state=NORMAL)
            self.minFormationVolumeFactorEntry.config(state=DISABLED)
            self.maxFormationVolumeFactorEntry.config(state=DISABLED)
        elif choice == 'Uniform':
            self.singleFormationVolumeFactorEntry.config(state=DISABLED)
            self.minFormationVolumeFactorEntry.config(state=NORMAL)
            self.maxFormationVolumeFactorEntry.config(state=NORMAL)
        elif choice == 'Triangular':
            self.singleFormationVolumeFactorEntry.config(state=NORMAL)
            self.minFormationVolumeFactorEntry.config(state=NORMAL)
            self.maxFormationVolumeFactorEntry.config(state=NORMAL)
    
    def setAllParameters(self):
        #Area Parameters
        areaDistChoice = areaDistributionTypeChoice.get()
        areaMinValue = getEntryValue(self.minAreaEntry)
        areaMostLikelyValue = getEntryValue(self.singleAreaEntry)
        areaMaxValue = getEntryValue(self.maxAreaEntry)
        variableHelper.setParametersBasedOnDistributionType(area, distributionType=areaDistChoice, minValue=areaMinValue, mostLikelyValue=areaMostLikelyValue, maxValue=areaMaxValue)

        #Thickness Parameters
        thicknessDistChoice = thicknessDistributionChoice.get()
        thicknessMinValue = getEntryValue(self.minThicknessEntry)
        thicknessMostLikelyValue = getEntryValue(self.singleThicknessEntry)
        thicknessMaxValue = getEntryValue(self.maxThicknessEntry)
        variableHelper.setParametersBasedOnDistributionType(thickness, distributionType=thicknessDistChoice, minValue=thicknessMinValue, mostLikelyValue=thicknessMostLikelyValue, maxValue=thicknessMaxValue)

        #Porosity Parameters
        porosityDistChoice = porosityDistributionChoice.get()
        porosityMinValue = getEntryValue(self.minPorosityEntry)
        porosityMostLikelyValue = getEntryValue(self.singlePorosityEntry)
        porosityMaxValue = getEntryValue(self.maxPorosityEntry)
        variableHelper.setParametersBasedOnDistributionType(porosity, distributionType=porosityDistChoice, minValue=porosityMinValue, mostLikelyValue=porosityMostLikelyValue, maxValue=porosityMaxValue)

        #Water Saturation Parameters
        waterSaturationDistChoice = waterSaturationDistributionChoice.get()
        waterMinValue = getEntryValue(self.minWaterSaturationEntry)
        waterMostLikelyValue = getEntryValue(self.singleWaterSaturationEntry)
        waterMaxValue = getEntryValue(self.maxWaterSaturationEntry)
        variableHelper.setParametersBasedOnDistributionType(waterSaturation, distributionType=waterSaturationDistChoice, minValue=waterMinValue, mostLikelyValue=waterMostLikelyValue, maxValue=waterMaxValue)

        #Recovery Factor Parameters
        recoveryDistChoice = recoveryFactorDistributionChoice.get()
        recoveryMinValue = getEntryValue(self.minRecoveryFactorEntry)
        recoveryMostLikelyValue = getEntryValue(self.singleRecoveryFactorEntry)
        recoveryMaxValue = getEntryValue(self.maxRecoveryFactorEntry)
        variableHelper.setParametersBasedOnDistributionType(recoveryFactor, distributionType=recoveryDistChoice, minValue=recoveryMinValue, mostLikelyValue=recoveryMostLikelyValue, maxValue=recoveryMaxValue)

        #Formation Volume Factor
        volumeDistChoice = formationVolumeFactorDistributionChoice.get()
        volumeMinValue = getEntryValue(self.minFormationVolumeFactorEntry)
        volumeMostLikelyValue = getEntryValue(self.singleFormationVolumeFactorEntry)
        volumeMaxValue = getEntryValue(self.maxFormationVolumeFactorEntry)
        variableHelper.setParametersBasedOnDistributionType(formationVolumeFactor, distributionType=volumeDistChoice, minValue=volumeMinValue, mostLikelyValue=volumeMostLikelyValue, maxValue=volumeMaxValue)
    
    def showHistogram(self):
        standardDeviation = statistics.pstdev(self.npResults, mu=None)
        num_bins = NUMBER_OF_SAMPLES

        fig, ax = plt.subplots()

        n, bins, patches = ax.hist(self.npResults, num_bins, density=1)
        
        y = ((1 / (np.sqrt(2 * np.pi) * standardDeviation)) *
            np.exp(-0.5 * (1 / standardDeviation * (bins - self.npAverage))**2))

        ax.plot(bins, y, '--')
        ax.set_xlabel('Np')
        ax.set_ylabel('Y')

        fig.tight_layout()
        plt.show()
    
    def exportData(self):
        tableDictionary = {'Area': self.areaValues,
                        'Thickness': self.thicknessValues,
                        'Porosity': self.porosityValues,
                        'Water Saturation': self.waterSaturationValues,
                        'Recovery Factor': self.recoveryFactorValues,
                        'Formation Volume Factor': self.formationVolumeFactorValues,
                        'Np Value': self.npValues}
        dataFrame = pd.DataFrame(tableDictionary)
        export_file_path = filedialog.asksaveasfilename(initialdir='~/Documents', defaultextension='.csv')
        dataFrame.to_csv(export_file_path, index=None, header=True)

def runSimulation(unitySystem, area, thickness, porosity, waterSaturation, recoveryFactor, formationVolumeFactor, simulation):
    npValues = []
    for i in range(NUMBER_OF_SAMPLES):
        areaProbability = 0.0
        thicknessProbability = 0.0
        porosityProbability = 0.0
        waterSaturationProbability = 0.0
        recoveryFactorProbability = 0.0
        formationVolumeFactorProbability = 0.0

        areaProbability = calculationHelper.getProbabilityBasedOnDistributionType(area)
        simulation.areaValues.append(round(areaProbability, 2))
        thicknessProbability = calculationHelper.getProbabilityBasedOnDistributionType(thickness)
        simulation.thicknessValues.append(round(thicknessProbability, 2))
        porosityProbability = calculationHelper.getProbabilityBasedOnDistributionType(porosity)
        simulation.porosityValues.append(round(porosityProbability, 2))
        waterSaturationProbability = calculationHelper.getProbabilityBasedOnDistributionType(waterSaturation)
        simulation.waterSaturationValues.append(round(waterSaturationProbability, 2))
        recoveryFactorProbability = calculationHelper.getProbabilityBasedOnDistributionType(recoveryFactor)
        simulation.recoveryFactorValues.append(round(recoveryFactorProbability, 2))
        formationVolumeFactorProbability = calculationHelper.getProbabilityBasedOnDistributionType(formationVolumeFactor)
        simulation.formationVolumeFactorValues.append(round(formationVolumeFactorProbability, 2))

        npValue = calculationHelper.calculateReserve(unitSystem=unitySystem, 
                                    area=areaProbability,
                                    thickness=thicknessProbability,
                                    porosity=porosityProbability,
                                    waterSaturation=waterSaturationProbability,
                                    recoveryFactor=recoveryFactorProbability,
                                    formationVolume=formationVolumeFactorProbability)
        simulation.npValues.append(round(npValue, 2))
        npValues.append(npValue)
    return npValues

def getEntryValue(entry=Entry):
    if len(entry.get()) != 0:
        return float(entry.get())
    else:
        return 0.0

root = Tk()

areaDistributionTypeChoice = StringVar()
areaDistributionTypeChoice.set('Simple')
thicknessDistributionChoice = StringVar()
thicknessDistributionChoice.set('Simple')
porosityDistributionChoice = StringVar()
porosityDistributionChoice.set('Simple')
waterSaturationDistributionChoice = StringVar()
waterSaturationDistributionChoice.set('Simple')
recoveryFactorDistributionChoice = StringVar()
recoveryFactorDistributionChoice.set('Simple')
formationVolumeFactorDistributionChoice = StringVar()
formationVolumeFactorDistributionChoice.set('Simple')
unitySystemChoice = StringVar()
unitySystemChoice.set('SI')

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

Simulation(root)
root.mainloop()