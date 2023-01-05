#This project will read or write to 3 commonly used file types
#No copying function yet
import pandas as pd
import json
from json import dump

def main():
    pathToFile = str(input("What is the path to the file?\n"))
    if pathToFile.endswith(".xlsx"):
        excel(pathToFile)
    if pathToFile.endswith(".txt"):
        txt(pathToFile)
    if pathToFile.endswith(".csv"):
        csv(pathToFile)
    if pathToFile.endswith(".json"):
        json(pathToFile)
    
def excel(path):
    operation = str(input("You have selected an Excel file\nAre you \n1)\tReading\n2)\tWriting\n"))
    if operation == "1":
        excelRead(path)
    if operation == "2":
        excelWrite(path)
        
def excelRead(path):
    output = pd.read_excel(path)
    print(output.head())        

def excelWrite(path):
    dataToExcel = ['',]
    while True:
        header = str(input("What would you like the header to be?\n"))
        dataToExcel.append(header)
        while True:
            dataList = ['',]
            data = str(input("What would you like the data to be?\n"))
            dataList[0] = data
            while True:
                cont = str(input("Are there any more data entries? \npress enter to continue\n press n to leave\n"))
                if cont == 'n':
                    dataToExcel.append(dataList)
                    print(dataToExcel)
                    break
                else:
                    data = str(input("What would you like the data to be?\n"))
                    dataList.append(data)
            break
        cont = str(input("Are there more headers? \npress enter to continue\n press n to leave\n"))
        if cont == 'n':
            break
    
    dataToExcel.pop(0)
    
    dictToExcel={}
    
    def pad_dict_list(dict_list, padel):
        lmax = 0
        for lname in dict_list.keys():
            lmax = max(lmax, len(dict_list[lname]))
        for lname in dict_list.keys():
            ll = len(dict_list[lname])
            if  ll < lmax:
                dict_list[lname] += ("",) * (lmax - ll)
        return dict_list
    
    for i in range(len(dataToExcel)-2):
        if i==0:
            dictToExcel[str(dataToExcel[i])] = tuple(dataToExcel[i + 1])
        else:
            i+=1
            dictToExcel[str(dataToExcel[i])] = tuple(dataToExcel[i + 1])

    pad_dict_list(dictToExcel," ")
        
    print(dictToExcel)
    
    output = pd.DataFrame(dictToExcel)
    output.to_excel(path, index=False)
    
def txt(path):
    while True:
        operation = str(input("You have selected a text file\nAre you \n1)\tReading\n2)\tWriting\n"))
        if operation == "1":
            txtRead(path)
        if operation == "2":
            txtWrite(path)
            
def txtRead(path):
    output = open(path,"r")
    print(output.read())
    output.close

def txtWrite(path):
    output = open(path,"w")
    output.writelines(input("What would you like to write?\n"))
    output.close
        
def csv(path):
    while True:
        operation = str(input("You have selected a csv file\nAre you \n1)\tReading\n2)\tWriting\n"))
        if operation == "1":
            csvRead(path)
        if operation == "2":
            csvWrite(path)
        
def csvRead(path):
    output = pd.read_csv(path)
    print(output.head())

def csvWrite(path):
    columnNames = []
    dataList =[]
    while True:
        x = input("What is the name of the column you want to add?\n")
        columnNames.append(x)
        cont = input("Press n to exit or enter to add more\n")
        if cont == 'n':
            break

    while True:
        temp =[]
        while True:
            data = input("What piece of data would you like to add?\n")
            temp.append(data)
            cont = input("Press n to exit or enter to add more\n")
            if cont == 'n':
                break
        dataList.append(temp)
        cont = input("Press n to exit or enter to add another line\n")
        if cont == 'n':
            break
        
    output = pd.DataFrame(dataList,columns=columnNames)
    output.to_csv(path)
    #Add padding if you want
    
def json(path):
    while True:
        operation = str(input("You have selected a JSON file\nAre you \n1)\tReading\n2)\tWriting\n"))
        if operation == "1":
            jsonRead(path)
        if operation == "2":
            jsonWrite(path)
            
def jsonRead(path):
    output = pd.read_json(path)
    print(output.head())
def jsonWrite(path):
    output = {}
    while True:
        x = input("What would you like a key to be?\n")
        y = input("What would you like the value of " + x + " to be\n")
        output[str(x)] = y
        cont = input("Press n to exit or enter to add another line\n")
        if cont == 'n':
            break
    with open(path,"w") as outfile:
        dump(output, outfile)
        
        
main()

