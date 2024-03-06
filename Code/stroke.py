import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Nomination des variables qualitatives et quantitatives
variables_quantitatives = [
                            'age', 
                            'avg_glucose_level', 
                            'bmi'
                          ]

colors_quantitative = [
                            'midnightblue', 
                            'orange', 
                            'green'
                       ]



variables_qualitatives = [
                            'gender', 
                            'hypertension', 
                            'heart_disease', 
                            'ever_married', 
                            'work_type', 
                            'Residence_type', 
                            'smoking_status', 
                            'stroke'
                         ]


colors_qualitative = [
                            'midnightblue', 
                            'orange', 
                            'green', 
                            'red', 
                            'purple', 
                            'blue', 
                            'pink', 
                            'cyan'
                      ]