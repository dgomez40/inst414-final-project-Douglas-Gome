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