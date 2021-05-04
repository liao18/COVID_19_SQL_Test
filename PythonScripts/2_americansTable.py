
## author @ Jonathan Liao
## version @ 4.3.2021
## 


import codecs
import csv
import sys
import os
import ctypes  # An included library with Python install.   

#create a custom exception class/name (stupid that I have to do declare this..)

def main():
    #first see if can open file
    here = os.getcwd()
    filepath=os.path.join(here,"output.csv")
    if not os.path.exists(filepath):
        message = " ".join(("output.csv file not detected in",here))
        ctypes.windll.user32.MessageBoxW(0, message, "FileNotFoundError", 1)
        ctypes.windll.user32.MessageBoxW(0, "1) Please redownload https://data.cdc.gov/NCHS/Deaths-involving-coronavirus-disease-2019-COVID-19/ks3g-spdg \n2) Save as CDC.csv", "FileNotFoundError", 1)
        raise FileNotFoundError
    else:
        print("output.csv file detected")
    #now read the csv file
    col_ct = 0
    row_ct = 0
    data = []
    output = []
    with open("output.csv", encoding = 'utf8') as csvFile:
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
    print("output.csv file succesfully read")
    
    #process data
    ID = None
    age = None
    race = None
    for h in range(0,col_ct):
        if data[0][h].lower() == "id":
            ID = h
        if data[0][h].lower() == "age_group":
            age = h
        if data[0][h].lower() == "race_and_hispanic_origin_group":
            race = h

    #check that state, age, race, and death headers were found. If just one is null, the program errors
    if ID is None:
        ctypes.windll.user32.MessageBoxW(0, "ID data not found. Check that there is a header for ID", "ID data not found", 1)
        raise DataTypeError
    if age is None:
        ctypes.windll.user32.MessageBoxW(0, "Age data not found. Check that there is a header for age", "Age data not found", 1)
        raise DataTypeError
    if race is None:
        ctypes.windll.user32.MessageBoxW(0, "Race data not found. Check that there is a header for race", "Race data not found", 1)
        raise DataTypeError

    #write to output
    with open('americans.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Age_Group", "Race_and_Hispanic_Origin_Group"]) #write the header first
        #age and race counters
        ageID = 1
        raceID = 1
        for i in range(1, row_ct):
            writer.writerow([data[i][ID], ageID, raceID])
            if ageID == 15:
                ageID = 1
                raceID = raceID + 1
            else:
                ageID = ageID + 1
            if raceID == 9:
                raceID = 1


    
if __name__ == "__main__":
    main()
    
class DataTypeError(Exception):
    pass

class FileNotFoundError(Exception):
    pass




