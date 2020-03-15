print("Hello world")

import re

dataSet = "data_small.txt"
dataList = []
collectedText = []
names = []
strain = []
percent = []
terp1 = []
terp2 = []
terp3 = []
price = []


def openFile():
    global dataList
    global dataSet
    print("Open File!")
    file = open(dataSet, "r")
    #    print(file.read())

    for line in file:
        print(line)
        dataList.append(line)


def returnSpaceIndex(dataList, lineSpace, newData, phase):
    currentLetter = ""
    currentSpace = 0
    if phase == 1:
        for line in range(0, len(dataList)):
            for letter in range(0, len(dataList[line])):
                currentLetter = dataList[line][letter]
                if currentLetter == " ":
                    # currentSpace = letter
                    lineSpace.append(letter)
                    break
    elif phase == 2:
        print("RE Line space function phase 3!")
        global strain
        for line in range(0, len(newData)):
            newText = newData[line]
            print(newData[line])
            returnedText = re.search("\d\d[.]\d\d[%]", newText)
            returnedIter = re.split(r"\d\d[.]\d\d[%]", newText)
            # print(returnedText)
            print(returnedText.group(0))
            print(returnedIter)
            strain.append(returnedIter[0])
            # for letter in range(0,len(dataList[line])):
            # currentLetter = dataList[line][letter]
            # if currentLetter == " ":
            ##currentSpace = letter
            # lineSpace.append(letter)
            # break
    else:
        for line in range(0, len(newData)):
            for letter in range(0, len(newData[line])):
                currentLetter = newData[line][letter]
                if currentLetter == " ":
                    # currentSpace = letter
                    lineSpace.append(letter)
                    break


def appendToList(dataList, lineSpace, newData, phase):
    global collectedText
    tempList = []
    for line in range(0, len(newData)):
        tempList.append(newData[line][(lineSpace[line]):])
    if phase == 1:
        for line in range(0, len(dataList)):
            print("Collected text function: ", dataList[line][:(lineSpace[line] + 2)])
            collectedText.append(dataList[line][0:(lineSpace[line]) + 2])
            print("Collected new data function: ", (dataList[line][(lineSpace[line] + 2):]))
            newData.append(dataList[line][(lineSpace[line] + 2):])
    else:
        for line in range(0, len(newData)):
            print("Collected text function: ", newData[line][:(lineSpace[line])])
            collectedText.append(newData[line][0:(lineSpace[line])])

            print("Collected new data function: ", (tempList[line][(lineSpace[line]):]))
            newData.append(tempList[line][(lineSpace[line]):])


def appendToNewList(dataList, lineSpace, newData):
    print("Append to new list")
    for line in range(0, len(dataList)):
        print("Collected text function: ", dataList[line][:(lineSpace[line])])
        collectedText.append(dataList[line][:(lineSpace[line])])


def deleteData(dataList, tempData, lineSpace, phase):
    global names, strain, percent, terp1, terp2, terp3, price, collectedText
    print("Delete Phase: ", phase)  # Current Phase print
    # Everything else besides the " - " so " -" and " "
    for line in range(0, len(collectedText)):
        print("First CollectedText to be Deleted: ", collectedText[line])
        # del newData[:]
        if phase == 1:
            # append name to
            names.append(collectedText[line])
        if phase == 3:
            # add new data to newData list
            # print("")
            strain.append(collectedText[line])
    del collectedText[:]
    del lineSpace[:]
    # collectedText.append(collectedText[line][lineSpace[line]:])

    # Transfer new data to temp, then delete collectedText for use again
    # if line == len(collectedText)-1:
    #    for line in range(0, len(collectedText)):
    #        tempData.append(collectedText[line])
    #        print("Temp data: " + tempData[line])

    #    for line in range(0, len(collectedText)):
    #        collectedText.append(tempData[line][lineSpace[line]:])


def cleanData():
    global dataList
    global names
    lineSpace = []
    tempData = []
    newData = []
    phase = 0

    print("Start data cleaning...")

    print("Phase 1")
    returnSpaceIndex(dataList, lineSpace, newData, 1)
    appendToList(dataList, lineSpace, newData, 1)
    deleteData(dataList, tempData, lineSpace, 1)

    print("Phase 2")
    returnSpaceIndex(dataList, lineSpace, newData, 2)
    # appendToList(dataList, lineSpace, newData, 2)
    # deleteData(dataList, tempData, lineSpace, 2)

    # del collectedText[:]


#    print(currentLetter)
#    print(currentSpace)


def testFunction():
    print("START TEST FUNCTION:")

    dataDictionary = {"Company": "test", "Strain": "GG", "THC": "69.42%", "Terp1": "C", "Terp2": "H", "Terp3": "M",
                      "Price": "$55"}
    # print(dataDictionary)


openFile()
cleanData()
testFunction()