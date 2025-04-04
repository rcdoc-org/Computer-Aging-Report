import intune
import os
import csv
import pandas

def Access_BreakDown_CSV(filename:str):
    currentDir = os.getcwd()
    #parentDir = os.path.dirname(currentDir)
    
    breakdownFile = os.path.join(currentDir, filename)
    return breakdownFile

def Create_Reports_Directory():
    currentDir = os.getcwd()
    #parentDir = os.path.dirname(currentDir)
    reportsDir = os.path.join(currentDir, "reports")
    
    if not os.path.exists(reportsDir):
        os.mkdir(reportsDir)
    return reportsDir

def Read_BreakDowns(filename:str,dataframe):
    reportsDir = Create_Reports_Directory()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            #location,prefixes,domains
            dataframe_filtered = intune.Filter_Devices(dataframe=dataframe,devicePrefixes=row["prefixes"],emailDomains=row["domains"])
            prefixes = row["prefixes"]
            domains = row["domains"]
            intune.Export_Devices(dataframe=dataframe_filtered, reportsDir=reportsDir,devicePrefixes=prefixes, emailDomains=domains)
            
            
    