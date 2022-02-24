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
from aquacrop.classes_Guar import *
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
#import WINDSfunctionsandclasses13.py

#exec(open("WINDSfunctionsandclasses_July25.py").read())
pathprefix='/home/ecoslacker/Documents/WINDS_Data/'
# sys.path.append(pathprefix)

db=create_engine('mysql://UofABEWINDS:WINDSAWSPort2020@windsdatabase-1.cdzagwevzppe.us-west-1.rds.amazonaws.com:3306/winds_test')
Guar_data = pd.read_sql('SELECT * from Aquacrop_crop_table',con=db)  #Reads all data from mysql db
Field_data = pd.read_sql('SELECT * from Aquacrop_field_table',con=db)  #Reads all data from mysql db
Soil_data = pd.read_sql('SELECT * from Aquacrop_soil_layers',con=db)  #Reads all data from mysql db

#test
class plant_data:
    def __init__(self, Guar_data):
        self.Crop_name = Guar_data['Crop Name']
        self.Crop_type = int(Guar_data['Crop Type'])                             
        self.Plant_method= int(Guar_data['Plant Method'])                             
        self.Calendar_type = int(Guar_data['Calendar Type'])                           
        self.SwitchGDD = int(Guar_data['SwitchGDD'])                             
        self.Planting_date = Guar_data['Planting Date']                             
        self.Harvest_date = Guar_data['Harvest Date']                             
        self.Emergence = float(Guar_data['Emergence'])                             
        self.MaxRooting = float(Guar_data['Max Rooting'])                             
        self.Senescence = float(Guar_data['Senescence'])                             
        self.Maturity = float(Guar_data['Maturity'])                             
        self.HIstart = float(Guar_data['HIstart'])                             
        self.Flowering = float(Guar_data['Flowering'])                             
        self.YldForm = float(Guar_data['Yld Form'])                             
        self.GDDmethod = int(Guar_data['GDD Method'])                             
        self.Tbase = float(Guar_data['Tbase']); 
        self.Tupp =float(Guar_data['Tupp']); 
        self.PolHeatStress = int(Guar_data['PolHeatStress']); 
        self.Tmax_up = int(Guar_data['Tmax_up']); 
        self.Tmax_lo = int(Guar_data['Tmax_lo']); 
        self.PolColdStress = int(Guar_data['PolColdStress']); 
        self.Tmin_up = int(Guar_data['Tmin_up']); 
        self.Tmin_lo = int(Guar_data['Tmin_lo']); 
        self.TrColdStress = int(Guar_data['TrColdStress']);
        self.GDD_up = float(Guar_data['GDD_up']);
        self.GDD_lo = float(Guar_data['GDD_lo']);
        self.Zmin = float(Guar_data['Zmin']); 
        self.Zmax = float(Guar_data['Zmax']);
        self.fshape_r = float(Guar_data['fshape_r']); 
        self.SxTopQ = float(Guar_data['SxTopQ']);
        self.SxBotQ = float(Guar_data['SxBotQ']);
        self.SeedSize = float(Guar_data['SeedSize']); 
        self.PlantPop = float(Guar_data['PlantPop']); 
        self.CCx = float(Guar_data['CCx']);
        self.CDC = float(Guar_data['CDC']); 
        self.CGC = float(Guar_data['CGC']); 
        self.Kcb = float(Guar_data['Kcb']);
        self.fage = float(Guar_data['fage']); 
        self.WP = float(Guar_data['WP']); 
        self.WPy = float(Guar_data['Wpy']);
        self.fsink = float(Guar_data['fsink']);
        self.HI0 = float(Guar_data['HI0']);
        self.dHI_pre = float(Guar_data['dHI_pre']);
        self.a_HI = float(Guar_data['a_HI']); 
        self.b_HI = float(Guar_data['b_HI']); 
        self.dHI0 = float(Guar_data['dHI0']);
        self.Determinant = float(Guar_data['Determinant']); 
        self.exc = float(Guar_data['exc']); 
        self.p_up1 = float(Guar_data['p_up1']); 
        self.p_up2 = float(Guar_data['p_up2']); 
        self.p_up3 = float(Guar_data['p_up3']); 
        self.p_up4 = float(Guar_data['p_up4']);
        self.p_lo1 = float(Guar_data['p_lo1']); 
        self.p_lo2 = float(Guar_data['p_lo2']); 
        self.p_lo3 = float(Guar_data['p_lo3']); 
        self.p_lo4 = float(Guar_data['p_lo4']); 
        self.fshape_w1 = float(Guar_data['fshape_w1']);
        self.fshape_w2 = float(Guar_data['fshape_w2']);
        self.fshape_w3 = float(Guar_data['fshape_w3']);
        self.fshape_w4 = float(Guar_data['fshape_w4']);
        self.CC0 = float(Guar_data['CC0']);
        self.HIGC = float(Guar_data['HIGC']);
        self.tLinSwitch = float(Guar_data['tLinSwitch']);
        self.dHILinear = float(Guar_data['dHILinear']);
        self.fCO2 = float(Guar_data['fCO2']);
        self.FloweringCD = float(Guar_data['FloweringCD']);
        self.FloweringEnd = float(Guar_data['FloweringEnd']);
        self.fshape_b = float(Guar_data['fshape_b']); # Shape factor describing the reduction in biomass production for insufficient growing degree days
        self.PctZmin = int(Guar_data['PctZmin']); # Initial percentage of minimum effective rooting depth
        self.fshape_ex = int(Guar_data['fshape_ex']); # Shape factor describing the effects of water stress on root expansion
        self.ETadj = int(Guar_data['ETadj']); # Adjustment to water stress thresholds depending on daily ET0 (0 = No, 1 = Yes)
        self.Aer = int(Guar_data['Aer']); # Vol (%) below saturation at which stress begins to occur due to deficient aeration
        self.LagAer = int(Guar_data['LagAer']); # Number of days lag before aeration stress affects crop growth
        self.beta = int(Guar_data['beta']); # Reduction (%) to p_lo3 when early canopy senescence is triggered
        self.a_Tr = int(Guar_data['a_Tr']); # Exponent parameter for adjustment of Kcx once senescence is triggered
        self.GermThr = int(Guar_data['GermThr']); # Proportion of total water storage needed for crop to germinate
        self.CCmin = float(Guar_data['CCmin']); # Minimum canopy size below which yield formation cannot occur
        self.MaxFlowPct = str(Guar_data['MaxFlowPct']); # Proportion of total flowering time (%) at which peak flowering occurs
        self.HIini = float(Guar_data['HIini']); # Initial harvest index
        self.bsted = float(Guar_data['bsted']); # WP co2 adjustment parameter given by Steduto et al. 2007
        self.bface = float(Guar_data['bface']); # WP co2 adjustment parameter given by FACE experiments

class field_data:
    def __init__(self, Field_data):
        self.Field_Name = Field_data['Field_name']
        self.Field_Number = Field_data['Field_number']
        self.Soil_Type = Field_data['soilType']                             
        self.CN = int(Field_data['CN'])                             
        self.CalcCN = int(Field_data['CalcCN'])                           
        self.REW = float(Field_data['REW'])                             
        self.dz = float(Field_data['dz'])                             
        self.Number_of_Layers = int(Field_data['Number of Layers'])                             

class soil_data:
    def __init__(self, Soil_data):
        self.Field_Name = Soil_data['FieldName']
        self.Field_Number = Soil_data['Field_number']
        self.Layer_Number = int(Soil_data['LayerNumber'])                             
        self.Layer_Thickness= float(Soil_data['LayerThickness'])                             
        self.Wilting_Point = float(Soil_data['Wilting Point'])                           
        self.Field_Capacity = float(Soil_data['Field Capacity'])                             
        self.Saturation = float(Soil_data['Saturation'])                             
        self.Hydraulic_Conductivity = float(Soil_data['Hydraulic Conductivity'])                             
        self.Soil_Penetrability = float(Soil_data['Soil Penetrability'])                             
     
    
Guar_data_in = Guar_data.loc[(Guar_data['User']=='Wanyu') & (Guar_data['Crop Name']== 'Guayule')]
Field_data_in = Field_data.loc[(Field_data['User']=='Wanyu') & (Field_data['Field_name'] == 'Guayule2018')]
Soil_data_in = Soil_data.loc[(Soil_data['User']=='Pete') & (Soil_data['FieldName'] == 'Guar1') & (Soil_data['LayerNumber'] == 1)]
P = plant_data(Guar_data_in)
F = field_data(Field_data_in)
S = soil_data(Soil_data_in)

print('Crop type', P.Crop_type)
# Reads in the weather data
weather = pd.read_csv('GuayuleWeather_2018_csv.csv') 
# Prepares the weather data that is in the csv to the format that the aquacrop code needs it in (ten spaces between each value)
with open('GuayuleWeather_2018_csv.txt', 'w') as f: weather.to_string(f, col_space = 10, index=False, justify = 'left') 
# Uses the function prepare weather to convert weather data
wdf = prepare_weather('GuayuleWeather_2018_csv.txt') 
# Grabs the soil class from the classes.py file
soil = SoilClass('SandyLoam2018', F, S) 
# Prepares the crop class with the name of the crop, planting date, and harvest date
crop = CropClass('GuarGDD', P, PlantingDate='01/01',HarvestDate='12/31')
# Initialize water content to be field capacity 
InitWC = InitWCClass(value=['FC']) 
# The model is run using SimStartTime, SimEndTime, weather data, soil, crop, initial water content
model = AquaCropModel('2018/01/01','2018/12/31', wdf,soil,crop, InitWC) 
model.initialize() 
model.step(till_termination=True)

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


# The following are print statements to see different outputs
# Final summary (season total)
print('\n Final Summary = \n', FinalHead) 
# Daily water flux
print('\n Daily Water Flux = \n', FluxHead) 
 # Soil water content in each soil compartment
print('\n Soil Water Content = \n', WaterHead)
# Crop growth
print('\n Crop Growth = \n', GrowthHead) 

# Plotting canopy coverage over time (days after planting)
GrowthHead = GrowthHead[(GrowthHead.T != 0).any()]
plt1 = GrowthHead.plot(x ='DAP', y='CC', kind='line', label = 'With stress', title = 'Canopy Coverage over Time')
GrowthHead.plot(x ='DAP', y='CC_NS', kind='line', color = 'y', label = 'Without stress', ax=plt1)
plt1.set_ylabel("Canopy Coverage")
plt1.set_xlabel("Days After Planting (DAP)")

# Plotting biomass with no stress and stress conditions over time (days after planting) on the same graph
plt2 = GrowthHead.plot(x ='DAP', y='B_NS', kind='line', color = "k", label = 'Without stress', title = 'Biomass over Time')
GrowthHead.plot(x ='DAP', y='B', kind='line', color = "r", label='With stress', ax=plt2)
plt2.set_ylabel("Biomass (kg/ha)")
plt2.set_xlabel("Days After Planting (DAP)")
#Plot one less point 

