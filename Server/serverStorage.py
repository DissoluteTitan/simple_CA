import csv

def writeRegistry(reg_info):
    with open('regisrty.csv', 'a+') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(reg_info)

def readRegistry():
    with open('registry.csv','r+') as regFile:
        regFileReader = csv.reader(regFile)
        name_column = [row[0] for row in regFileReader]
    return name_column