# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 21:28:44 2022

@author: jonrb
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

cars = pd.read_csv('cars.csv')

headers = list(cars.columns)

print(cars)

number = LabelEncoder()

for i, heading in enumerate(list(cars.columns)):
  if i == 4 or i == 5 or i == 9 or i == 14 or i == 17 or i == 18 or i == 29:
    continue
  else:
    cars[heading] = number.fit_transform(
      cars[heading].astype('str'))

print(cars)