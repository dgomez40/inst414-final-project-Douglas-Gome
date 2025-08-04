import pandas as pd
import seaborn as sns
import matplotlib as plt
import numpy as np


def air_pollutant():

    pm25_raw = pd.read_csv('data/pm25.csv')
    print(pm25_raw)

def weather():

    temperature_raw = pd.read_csv('data/temperature.csv')
    print(temperature_raw)

#my next steps would be to get access to proper temperature csv file, current one wouldn't work that well right now
#then I could merge the two databases off a common key, date, I have to find temp file that does not go through the entire day
#but the data provider is down at the moment https://www.ncei.noaa.gov/access/search/index
#if this dataset doesn't come up I have been looking into other resources.

#sort the data from oldest data to newest perferrably just 2025 data would be fine, plenty of rows,
#this will be my training data

def merge():
    #merge two datasets



return pollutant_merge;