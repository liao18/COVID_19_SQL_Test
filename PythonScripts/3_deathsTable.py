
## author @ Jonathan Liao
## version @ 4.3.2021
## 
## CSV data class, reads data and sends to GUI launcher

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

    print("output.csv file succesfully read")

    #write to output
    with open('Deaths.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data[0][0], data[0][3], data[0][4], data[0][5]])
        stateID = 1
        for i in range(1, row_ct): 
            writer.writerow([data[i][0], stateID, data[i][4], data[i][5]])
            if (i % 120 == 0):
                stateID = stateID + 1
    print(row_ct)


    
if __name__ == "__main__":
    main()
    
class DataTypeError(Exception):
    pass

class FileNotFoundError(Exception):
    pass



