#!/usr/bin/python

def TaxTable(filename):
    fread = open(filename,'r')
    Kingdom = []
    phylum = []
    Class = []
    Order = []
    Family = []
    genus = []
    Sp = []
    Tax = []
    ID = []
    for line in fread:
        tempLine = line.split(';')
        tempTax = []
        tempKingdom = ""
        tempPhylum = ""
        tempClass = ""
        tempOrder = ""
        tempFamily = ""
        tempGenus = ""
        tempSp = ""
        tempID = ""
        for i in range(len(tempLine)):
            tempcol = tempLine[i].split('__')
            if (tempcol[0][-1:]=="k"):
                incase = tempcol[1].split('\t')
                fortempID = tempcol[0].split('\t')
                if(len(incase)==1):
                    Kingdom.append(tempcol[1])
                    tempKingdom = tempcol[1]
                    tempID = fortempID[0]
            elif (tempcol[0]==" p"):
                incase = tempcol[1].split('\t')
                if(len(incase)==1):
                    phylum.append(tempcol[1])
                    tempPhylum = tempcol[1]
            elif (tempcol[0]==" c"):
                incase = tempcol[1].split('\t')
                if(len(incase)==1):
                    Class.append(tempcol[1])
                    tempClass = tempcol[1]
            elif (tempcol[0]==" o"):
                incase = tempcol[1].split('\t')
                if(len(incase)==1):
                    Order.append(tempcol[1])
                    tempOrder = tempcol[1]
            elif (tempcol[0]==" f"):
                incase = tempcol[1].split('\t')
                if(len(incase)==1):
                    Family.append(tempcol[1])
                    tempFamily = tempcol[1]
            elif (tempcol[0]==" g"):
                incase = tempcol[1].split('\t')
                if(len(incase)==1):
                    genus.append(tempcol[1])
                    tempGenus = tempcol[1]
            elif (tempcol[0]==" s"):
                incase = tempcol[1].split('\t')
                if(len(incase)==3):
                    Sp.append(incase[0])
                    tempSp = incase[0]
        tempTax = [tempKingdom,tempPhylum,tempClass,tempOrder,tempFamily,tempGenus,tempSp,tempID]
        Tax.append(tempTax)
    return Tax

def AssignColor(Tax):
    phylum = []
    Family = []
    Class = []
    genus = []
    for i in range(len(Tax)):
        phylum.append(Tax[i][1])
        Family.append(Tax[i][4])
        Class.append(Tax[i][2])
        genus.append(Tax[i][5])
    uniqPhylum = list(set(phylum))
    uniqFamily = list(set(Family))
    uniqClass = list(set(Class))
    uniqGenus = list(set(genus))

    color = ['r','g','b','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DEEEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125','r','g','b','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DE\
EEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125','r','g','b','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DE\
EEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125','r','g','b','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DE\
EEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125']

    classColor = []
    for i in range(len(uniqPhylum)):
        tempClassColor = [uniqPhylum[i],color[i]]
        classColor.append(tempClassColor)
    return classColor

def AssignColor2(Tax):
    phylum = []
    Family = []
    Class = []
    genus = []
    for i in range(len(Tax)):
        phylum.append(Tax[i][2])
        Family.append(Tax[i][3])
        Class.append(Tax[i][3])
        genus.append(Tax[i][6])
    uniqPhylum = list(set(phylum))
    uniqFamily = list(set(Family))
    uniqClass = list(set(Class))
    uniqGenus = list(set(genus))

    color = ['r','g','b','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DEEEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125','r','g','b','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DEEEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125','r','g','b','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DEEEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125','r','g','b','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DEEEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125']

    classColor = []
    for i in range(len(uniqPhylum)):
        tempClassColor = [uniqPhylum[i],color[i]]
        classColor.append(tempClassColor)
    return classColor

def MakeAbunTable(AbunRead):
    AbunTable = []
    for line in AbunRead:
        tempcol =  line.split('\t')
        tempAbunTable = [tempcol[0],tempcol[1],tempcol[2]]
        AbunTable.append(tempAbunTable)
    bignumber = 0
    amp = 1
    for i in range(len(AbunTable)):
        if (float(AbunTable[i][2])>bignumber):
            bignumber = float(AbunTable[i][2])
    for i in range(len(AbunTable)):
        AbunTable[i][2] = str(format(float(AbunTable[i][2])*amp/bignumber,'f'))
    return AbunTable

def TaxToGuide(Tax):
    guide = []
    for i in range(len(Tax)):
        tempName = ""
        for j in range(len(Tax[i])-1):
            if (Tax[i][j] != ""):
                tempName = tempName+"."+Tax[i][j]
        TempGuide = [Tax[i][7],tempName[1:]]
        guide.append(TempGuide)
    return guide

def ReadSummaryAbun(AbunRead):
    AbunTable = []
    for line in AbunRead:
        tempcol =  line.split('\t')
        tempAbunTable = [tempcol[0],tempcol[1]]
        AbunTable.append(tempAbunTable)
        bignumber = 0
    amp = 1
    for i in range(len(AbunTable)):
        if (float(AbunTable[i][1])>bignumber):
            bignumber = float(AbunTable[i][1])
    for i in range(len(AbunTable)):
        AbunTable[i][1] = str(format(float(AbunTable[i][1])*amp/bignumber,'f'))
    return AbunTable

def ReadTableSep(filename,Sep):
    fread = open(filename,'r')
    Table = []
    for line in fread:
        tempcol = line.strip().split(Sep)
        tempTable = []
        for i in range(len(tempcol)):
            tempTable.append(tempcol[i])
        Table.append(tempTable)
    return Table


def ReadRefSoilTax(filename):
    fread = open(filename,'r')
    Table = []
    for line in fread:
        tempcol = line.strip().split('\t')
        tempTax = tempcol[2].split(';')
        tempTable = []
        tempTable.append(tempcol[0])
        for i in range(len(tempTax)):
            tempTable.append(tempTax[i])
        Table.append(tempTable)
    return Table
