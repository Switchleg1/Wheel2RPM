import sys
import csv
from cfgfile import cfgfile

#load config file
cfgInfo = cfgfile("config.yaml", True)

#settings
minRPM = 8160
maxRPM = 0
lineList = []

def processLine(line, minRPM, maxRPM):
    gear = int(float(line[cfgInfo.gear]))
    if gear < 1:
        gear = 0
    elif gear > 6:
        gear = 6
    else:
        gear = gear - 1

    wheelSpeed = float(line[cfgInfo.wheelSpeed])
    multiplier = cfgInfo.multipliers[gear]
    newRPM = wheelSpeed * multiplier

    if minRPM > newRPM:
        minRPM = newRPM

    if maxRPM < newRPM:
        maxRPM = newRPM

    line[cfgInfo.engineRPM] = newRPM
    
    return minRPM, maxRPM
        

with open(sys.argv[1], "r", encoding="utf-8-sig", errors="surrogateescape") as inputFile:
    inputList = csv.DictReader(inputFile)
    for line in inputList:
        minRPM,maxRPM = processLine(line, minRPM, maxRPM)
        lineList.append(line)

with open(sys.argv[2], "w", newline='') as outputFile:
    outputCSV = csv.DictWriter(outputFile, fieldnames=inputList.fieldnames)
    outputCSV.writeheader()
    for line in lineList:
        outputCSV.writerow(line)

print("[Stats]")
print("  minRPM: " + str(minRPM))
print("  maxRPM: " + str(maxRPM))
print("")
              
            
            
