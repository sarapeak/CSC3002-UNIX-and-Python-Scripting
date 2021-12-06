# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:55:59 2021

@author: sarap
"""

import pandas as pd
import random

def monthlyBonus(mon):
    if mon=='Nov' or mon=='Dec':
        choiceList=[100,100,100,100,200,200,200,200,100,50]
    elif mon=='Jan' or mon=='Feb':
        choiceList=[0,0,0,0,0,0,50,50,100,100]
    else:
        choiceList=[0,0,0,50,50,100,100,100,200,200]
    monthlist=[]
    #get data for each of 8 employees
    for i in range(8):
        monthlist.append(random.choice(choiceList))
    return monthlist

#build a dictionary containing 10 weeks of commission data
bonusDict={}
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for month in months:
    bonusDict[month]=monthlyBonus(month)

#create the DataFrame of data
SalesPeople = ['Jose','Yi','Jon','Oscar','Amanda','Bill','Alexa','Kim']
bonusData=pd.DataFrame(bonusDict, index=SalesPeople)

#add the calculated columns
bonusData['Total Bonus']=bonusData.sum(axis=1)
bonusData['Ave per Week']=bonusData['Total Bonus']/10.0

pd.set_option('display.max_columns', None)#this just forces all columns to print
print (bonusData)

#Prints out the total amount of bonuses using the sum method
print ('For 12 months of bonuses for next year you would need to budget %.1f'
       %(bonusData['Total Bonus'].sum()))
#Prints out the min and max of April bonuses using the min and max methods
print ('In April, the minimum and maximum bonuses are projected to be %.1f'
       %(bonusData['Apr'].min()),
       'and %.1f' %(bonusData['Apr'].max()))
#Prints out the sum of April and December using the sum method
print ('In April, the total bonuses should be %.1f' %(bonusData['Apr'].sum()),
       'and in December they should be %.1f' %(bonusData['Dec'].sum()))

#Creates a line graph
bonusData.plot(kind='line',color=['green','purple'],
               y=['Dec','Jan'],figsize=(10,5))
#Creates a bar graph
bonusData.plot(title='Projected Bonuses for December, January, and April',
               kind='bar',colormap='winter',y=['Dec','Jan','Apr'],figsize=(10,5))