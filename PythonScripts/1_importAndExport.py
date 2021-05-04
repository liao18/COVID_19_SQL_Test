
## author @ Jonathan Liao
## version @ 4.3.2021
## 
## reads CDC raw data and creates output csv file that is used by subsequent scripts


import codecs
import csv
import sys
import os
import ctypes  # An included library with Python install.   

#create a custom exception class/name (stupid that I have to do declare this..)

def main():
    #first see if can open file
    here = os.getcwd()
    filepath=os.path.join(here,"CDC.csv")
    if not os.path.exists(filepath):
        message = " ".join(("CDC.csv file not detected in",here))
        ctypes.windll.user32.MessageBoxW(0, message, "FileNotFoundError", 1)
        ctypes.windll.user32.MessageBoxW(0, "1) Please redownload https://data.cdc.gov/NCHS/Deaths-involving-coronavirus-disease-2019-COVID-19/ks3g-spdg \n2) Save as CDC.csv", "FileNotFoundError", 1)
        raise FileNotFoundError
    else:
        print("CDC.csv file detected")
    #now read the csv file
    col_ct = 0
    row_ct = 0
    data = []
    output = []
    with open("CDC.csv", encoding = 'utf8') as csvFile:
        csvFileReader = csv.reader(csvFile, delimiter=',')
        csvFileReader = csv.reader(csvFile, delimiter=',')
        col_ct = len(next(csvFileReader))
        csvFile.seek(0) # next() moved the csvFileReader so this puts the reader back to top for reading
        row_ct = len(list(csvFileReader))
        csvFile.seek(0) # list() exhausts the csvFileReader so this puts the reader back to top for reading
        for row in csvFileReader:
            data.append(row)
            
    #fill blanks with NULLS
    for x in range(0, row_ct):
        for y in range(0, col_ct):
            if data[x][y] == '':
                data[x][y] = "NULL"
    print("CDC.csv file succesfully read")
    
    #process data
    ID = 1 #start at 1 for ID number then keep going up
    state = None
    age = None
    race = None
    death = None
    totalDeathCT = None
    for h in range(0,col_ct):
        if data[0][h].lower() == "state":
            state = h
        if data[0][h].lower() == "age group":
            age = h
        if data[0][h].lower() == "race and hispanic origin group":
            race = h
        if data[0][h].lower() == "COVID-19 Deaths".lower():
            death = h

    #check that state, age, race, and death headers were found. If just one is null, the program errors
    if state is None:
        ctypes.windll.user32.MessageBoxW(0, "State data not found. Check that there is a header for state", "State data not found", 1)
        raise DataTypeError
    if age is None:
        ctypes.windll.user32.MessageBoxW(0, "Age data not found. Check that there is a header for age", "Age data not found", 1)
        raise DataTypeError
    if race is None:
        ctypes.windll.user32.MessageBoxW(0, "Race data not found. Check that there is a header for race", "Race data not found", 1)
        raise DataTypeError
    if death is None:
        ctypes.windll.user32.MessageBoxW(0, "Death data not found. Check that there is a header for death", "Death data not found", 1)
        raise DataTypeError

    #extract total deaths to use for % calculation
    for j in range(0,row_ct):
        if data[j][race].lower() == "Total Deaths".lower():
            totalDeathCT = data[j][death]
            break
    if totalDeathCT is None:
        ctypes.windll.user32.MessageBoxW(0, "Total death count not found. Check that there is a row for TOTAL US deaths", "Death data not found", 1)
        raise DataTypeError

    #write to output
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Age_Group", "Race_and_Hispanic_Origin_Group", "State", "COVID_19_Deaths", "Percent_of_Total_COVID-19_Deaths"]) #write the header first
        for i in range(1, row_ct):
            #ignore data about New York City and The United States
            if data[i][state].lower() == "new york city":
                continue
            if data[i][state].lower() == "united states":
                continue
            if data[i][death].lower() == "NULL".lower():
                writer.writerow([ID, data[i][age], data[i][race], data[i][state], "NULL", "NULL"])
            else:
                writer.writerow([ID, data[i][age], data[i][race], data[i][state], data[i][death], (int(data[i][death])/int(totalDeathCT))*100 ])  
            ID = ID + 1


    
if __name__ == "__main__":
    main()
    
class DataTypeError(Exception):
    pass

class FileNotFoundError(Exception):
    pass




