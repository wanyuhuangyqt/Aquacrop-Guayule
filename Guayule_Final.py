# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:01:04 2020

@author: carol
"""

import sys
import csv
_=[sys.path.append(i) for i in ['.', '..']] # finds 'AquaCrop' file
import matplotlib.pyplot as plt
import matplotlib
# Visualization tool used for high-level interface for drawing attractive and informative stastical graphics
import seaborn as sns 
import numpy as np
import pandas as pd
from aquacrop.core import *
from aquacrop.classes_Guayule_Current import *

# Reads in the weather data
weather = pd.read_csv('GuayuleWeather_2018_csv.csv') 
# Prepares the weather data that is in the csv to the format that the aquacrop code needs it in (ten spaces between each value)
with open('GuayuleWeather_2018_csv.txt', 'w') as f: weather.to_string(f, col_space = 10, index=False, justify = 'left') 
# Uses the function prepare weather to convert weather data
wdf = prepare_weather('GuayuleWeather_2018_csv.txt') 
# Grabs the soil class from the classes.py file
soil = SoilClass('SandyLoam2018') 
# Prepares the crop class with the name of the crop, planting date, and harvest date
crop = CropClass('Wheat', PlantingDate='01/01',HarvestDate='12/31') 
# Initialize water content to be field capacity 
InitWC = InitWCClass(value=['FC']) 
# The model is run using SimStartTime, SimEndTime, weather data, soil, crop, initial water content
irrmngt = IrrMngtClass(IrrMethod=1,SMT=[50]*4) # 4 growth stages / thresholds have 50% of total water. They irrigate as soon as the soil moisture gets down to 50% 
model = AquaCropModel('2018/01/01','2018/12/31', wdf,soil,crop, InitWC, IrrMngt=irrmngt) 
model.initialize() 
model.step(till_termination=True)

#model = AquaCropModel(SimStartTime=f'{2018}/01/01',
                      #SimEndTime=f'{2018}/12/31',
                      #wdf=prepare_weather,
                      #Soil=SoilClass,
                      #Crop=CropClass,
                      #InitWC=InitWClass
                      #irrmngt=IrrMngtClass)


# Allows for the outputs below to show all columns when printed
pd.set_option('max_columns', None) 
 # Daily Water Flux dataframe. The 'none' removes the limit from the output so all the data can be shown
FluxHead = model.Outputs.Flux.head(None)
# Soil-water content in each soil compartment dataframe
WaterHead = model.Outputs.Water.head(None) 
# Crop growth dataframe
GrowthHead = model.Outputs.Growth.head(None) 
# Final summary (seasonal total) dataframe
FinalHead = model.Outputs.Final.head(None) 


# Plotting canopy coverage over time (days after planting)
plt1 = GrowthHead.plot(x ='DAP', y='CC', kind='scatter', title = 'Canopy Coverage over Time')
plt1.set_ylabel("Canopy Coverage")
plt1.set_xlabel("Days After Planting (DAP)")

# Plotting biomass over time (days after planting)
plt2 = GrowthHead.plot(x ='DAP', y='B', kind='scatter', title = 'Biomass with Stress over Time')
plt2.set_ylabel("Biomass (kg/ha)")
plt2.set_xlabel("Days After Planting (DAP)")

# Plotting biomass with no stress conditions over time (days after planting)
plt3 = GrowthHead.plot(x ='DAP', y='B_NS', kind='scatter', title = 'Biomass without Stress over Time')
plt3.set_ylabel("Biomass (kg/ha)")
plt3.set_xlabel("Days After Planting (DAP)")

# The following are print statements to see different outputs
# Final summary (season total)
print('\n Final Summary = \n', FinalHead) 
# Daily water flux
print('\n Daily Water Flux = \n', FluxHead) 
 # Soil water content in each soil compartment
print('\n Soil Water Content = \n', WaterHead)
# Crop growth
print('\n Crop Growth = \n', GrowthHead) 

