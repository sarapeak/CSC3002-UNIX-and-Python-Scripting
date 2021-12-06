# -*- coding: utf-8 -*-
"""
Created on Thu May 20 10:06:26 2021

@author: sarap
"""

import pandas as pd
students = {'Name':['Jones','Garcia','Chen','Smith','Solo','Adams','Dreydel'],
            'Year':[1,1,1,2,3,4,3],
            'GPA':[2.40,3.50,4.00,2.75,3.70,2.60,3.90]}
stuData = pd.DataFrame(students)
print (stuData.head(7))
print ('The mean of the gpas is', stuData['GPA'].mean())
stuData.plot(kind='bar',x='Name',y='GPA')
stuData.plot(kind='scatter',x='Year',y='GPA')
