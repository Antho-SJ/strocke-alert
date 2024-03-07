import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


alpha = 0.05

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
  '#FF6F61', 
  '#6B5B95', 
  '#88B04B', 
  '#F7CAC9', 
  '#92A8D1', 
  '#955251', 
  '#B565A7', 
  '#009B77'
                      ]