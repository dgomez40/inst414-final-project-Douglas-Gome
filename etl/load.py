import pandas as pd

def save_transformed_csv(pollutant_merge):
    pollutant_merge.to_csv('pollutant_merge_polished.csv')



