import csv

def writeInfo(infoList):
    with open('user.csv','w+') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(infoList)