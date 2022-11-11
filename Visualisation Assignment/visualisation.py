# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 19:52:28 2022

@author: lr22aak
DataSource: https://databank.worldbank.org
dataset: https://databank.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG/1ff4a498/Popular-Indicators
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Downloaded the data from the dataSource url and stored in the same path where python file is present and extracting the csv file using pandas
dataBank = pd.read_csv('814798f0-646e-4480-b98e-82b95ddd3dcf_Data.csv')

# Re-Naming the columns for the extracted data
dataBank.columns = ['Series Name','Series Code','Country Name','Country Code',
                    '2000','2001','2002','2003','2004','2005','2006','2007','2008',
                    '2009','2010','2011','2012','2013','2014','2015']

# dropping the columns which are not going to be used
dataBank = dataBank.drop(['Series Code','Country Code'], axis=1)

dataBank = dataBank.replace('..', np.NaN) # replacing the mising content with NaN


# =============================================================================
#  function "setData" is declared to filter data using the 'Series Name' and 'Country Name'
# =============================================================================
def setData(series_name, countryName):
    '''
    this function is used to filter data set from the whole data available

    Parameters
    ----------
    series_name : string
        Series Name is a group of activity.
        ex:Start-up procedures to register a business, Population growth, Forest area.... for different Countries
    countryName : string
        Country name is the name of the country to be used to filter the data based on the country name.

    Returns
    -------
    countryData : DataFrame
        Country data is filtered dataFrame which contains years and values respective to the Series Name .

    '''
    # Assigning the values belonging to Series Name to a new variable for iteration
    dataToIterate = dataBank.loc[dataBank['Series Name'] == series_name]
    
    # dropping the Series column, after sorting all the values in the column willl be same
    dataToIterate = dataToIterate.drop('Series Name', axis=1)
    
    countryData = []
    
    # for loop is used of iteration and check the country name which was passed as arguments
    for row_index, row in dataToIterate.iterrows():
        # if conditon is used to check for country Name and assing the particular value
        if(row['Country Name'] == countryName):
            countryData = row
                 
    # dropping the Country Name as the data is filtering based on the same
    countryData = countryData.drop('Country Name')
    
    countryData = pd.to_numeric(countryData) # converting the values to numeric data
    # resetting the index as the years are stored as index and will be used for the axes representation
    countryData = countryData.reset_index()
    
    # setting the column names
    countryData.columns =  ['year', series_name]
    
    countryData[series_name] = countryData[series_name].replace(np.NaN, 0)
    
    return countryData # return the simplified data form the common function


# =============================================================================
# line plot function
# =============================================================================
def linePlot(series_name):
    '''
    This function is used to produce line plots.

    Parameters
    ----------
    series_name : string
        Series Name is a group of activity.

    Returns
    -------
    None.

    '''
    # invoking the setData function to fetch data for different countries
    data1 = setData(series_name, 'Guyana')
    data2 = setData(series_name, 'United Kingdom')
    data3 = setData(series_name, 'Uganda')
    data4 = setData(series_name, 'Serbia')
    
    # initialising the plots
    plt.figure()
    
    # creating visualisation plots for multpile Countries
    # x-axis will be assigned to the periodic years available
    # y-axis will be assigned to the Series Names values
    plt.plot(data1['year'], data1[series_name], label = 'Guyana')
    plt.plot(data2['year'], data2[series_name], label = 'United Kingdom')
    plt.plot(data3['year'], data3[series_name], label = 'Uganda')
    plt.plot(data4['year'], data4[series_name], label = 'Serbia')
    
    plt.xlim('2006', '2014') # setting x-axis limits
    
    # x-axis and y-axis labels
    plt.xlabel('Years', fontsize = 20)
    plt.ylabel('No of Procedures', fontsize = 20)
    
    
    plt.title(series_name + " Line Plot", fontsize = 30) # Title of the Series Name
    plt.rcParams["figure.figsize"] = (18,10.5) # to make visulisation of clear plot
    
    plt.legend() # to display the labels
    
    plt.savefig(series_name + ' line_Plot.png') # to save the plots
    
    plt.show() # to display the plots


# =============================================================================
# Sub plots function
# =============================================================================
def subPlots(series_name):
    '''
    This function is used to produce subplots.

    Parameters
    ----------
    series_name : String
        Series Name is a group of activity.

    Returns
    -------
    None.

    '''
    # invoking the setData function to fetch data for different countries
    data1 = setData(series_name, 'Guyana')
    data2 = setData(series_name, 'United Kingdom')
    data3 = setData(series_name, 'Uganda')
    data4 = setData(series_name, 'Serbia')
    
    # initialising the plots
    plt.figure()
    
    plt.suptitle(series_name + " Sub Plots", fontsize = 30) # Title for the all subplots
    
    # sub plot 1
    plt.subplot(2, 2, 1)
    plt.bar(data1['year'], data1[series_name], label= 'Guyana')
    plt.xlim('2006', '2014')
    plt.xlabel('Years', fontsize = 15)
    plt.ylabel('No of Procedures', fontsize = 15)
    plt.legend()
    
    # sub plot 2
    plt.subplot(2, 2, 2)
    plt.bar(data2['year'], data2[series_name], label= 'United Kingdom', color='orange')
    plt.xlim('2006', '2014')
    plt.xlabel('Years', fontsize = 15)
    plt.ylabel('No of Procedures', fontsize = 15)
    plt.legend()
    
    # sub plot 3
    plt.subplot(2, 2, 3)
    plt.bar(data3['year'], data3[series_name], label= 'Uganda', color='green')
    plt.xlim('2006', '2014')
    plt.xlabel('Years', fontsize = 15)
    plt.ylabel('No of Procedures', fontsize = 15)
    plt.legend()
    
    # sub plot 4
    plt.subplot(2, 2, 4)
    plt.bar(data4['year'], data4[series_name], label= 'Serbia', color='pink')
    plt.xlim('2006', '2014')
    plt.xlabel('Years', fontsize = 15)
    plt.ylabel('No of Procedures', fontsize = 15)
    plt.legend()
    
    plt.savefig(series_name + ' Sub_Plot.png') # to save the plots
     
    plt.show() # to display the plots
    

# =============================================================================
# violin plot function
# =============================================================================
def violinPlots(series_name):
    '''
    This function is used to produce violin plots 

    Parameters
    ----------
    series_name : string
        Series Name is a group of activity.

    Returns
    -------
    None.

    '''
    # invoking the setData function to fetch data for different countries
    data1 = setData(series_name, 'Guyana')
    data2 = setData(series_name, 'United Kingdom')
    data3 = setData(series_name, 'Uganda')
    data4 = setData(series_name, 'Serbia')
    
    # initialising the plots
    plt.figure()
    
    plt.title(series_name + " Violin Plot", fontsize = 30) # Title of the Series Name
    
    # setting the data for violin plots
    data = [data1[series_name], data2[series_name], data3[series_name], data4[series_name]]
    
    plt.violinplot(data, showmedians=True)
    
    # x-axis and y-axis labels
    plt.xlabel('Country Names', fontsize = 20)
    plt.ylabel('No of Procedures', fontsize = 20)
    
    plt.xticks([1,2,3,4], ['Guyana','United Kingdom','Uganda','Serbia']) # to change the x-axis values
    
    plt.savefig(series_name + ' Violin_Plot.png') # to save the plots
    
    plt.show() # to display the plots
    

# =============================================================================
# invoking or calling the line plot fucntion
# =============================================================================

# creating a new variable to stor the series name which is used commnly
series_name = 'Start-up procedures to register a business (number)'
# invoking linePlot function
linePlot(series_name)
# invoking Sub Plots function
subPlots(series_name)
# invoking comparision plots function
violinPlots(series_name)

