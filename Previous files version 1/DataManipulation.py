#ApoER2 with and without exon 19 data manipulation

import csv

GOs = {}
PathList = []

#GoBP Table
def GoBPTable():
    file = open("ApoER2WithAndWithoutExon19.csv")
    csv_reader = csv.reader(file)
    newfile = open("GOBPTable.txt", "w")
    for line in csv_reader:
        affyid = line[0]
        goData = line[12]
        if "///" in goData:
            theGos = goData.split("///")
            for go in theGos:
                data = go.split("//")
                goId = data[0].strip()
                goTitle = data[1].strip()
                inference = data[2].strip()
                if goId not in GOs.keys():
                    GOs[goId] = goTitle
                newfile.write(affyid + "," + goId + "," + inference + "\n")
        elif "//" in goData:
            data = goData.split("//")
            goId = data[0].strip()
            goTitle = data[1].strip()
            inference = data[2].strip()
            if goId not in GOs.keys():
                GOs[goId] = goTitle
            newfile.write(affyid + "," + goId + "," + inference + "\n")
        else:
            pass        
    newfile.close()
    file.close()

def GoCCTable():
    file = open("ApoER2WithAndWithoutExon19.csv")
    csv_reader = csv.reader(file)
    newfile = open("GOCCTable.txt", "w")
    for line in csv_reader:
        affyid = line[0]
        goData = line[13]
        if "///" in goData:
            theGos = goData.split("///")
            for go in theGos:
                data = go.split("//")
                goId = data[0].strip()
                goTitle = data[1].strip()
                inference = data[2].strip()
                if goId not in GOs.keys():
                    GOs[goId] = goTitle
                newfile.write(affyid + "," + goId + "," + inference + "\n")
        elif "//" in goData:
            data = goData.split("//")
            goId = data[0].strip()
            goTitle = data[1].strip()
            inference = data[2].strip()
            if goId not in GOs.keys():
                GOs[goId] = goTitle
            newfile.write(affyid + "," + goId + "," + inference + "\n")
        else:
            pass
    file.close()      
    newfile.close()

def GoMFTable():
    file = open("ApoER2WithAndWithoutExon19.csv")
    csv_reader = csv.reader(file)
    newfile = open("GoMFTable.txt", "w")
    for line in csv_reader:
        affyid = line[0]
        goData = line[14]
        if "///" in goData:
            theGos = goData.split("///")
            for go in theGos:
                data = go.split("//")
                goId = data[0].strip()
                goTitle = data[1].strip()
                inference = data[2].strip()
                if goId not in GOs.keys():
                    GOs[goId] = goTitle
                newfile.write(affyid + "," + goId + "," + inference + "\n")
        elif "//" in goData:
            data = goData.split("//")
            goId = data[0].strip()
            goTitle = data[1].strip()
            inference = data[2].strip()
            if goId not in GOs.keys():
                GOs[goId] = goTitle
            newfile.write(affyid + "," + goId + "," + inference + "\n")
        else:
            pass
    newfile.close()
    file.close()

def GoTable():
    newfile = open("GoTable.txt", "w")
    for key in GOs.keys():
        newfile.write(key + "\t" + GOs[key] + "\n")
    newfile.close()

def PathwayTable():
    file = open("ApoER2WithAndWithoutExon19.csv")
    csv_reader = csv.reader(file)
    newfile = open("PathwayTable.txt", "w")
    for line in csv_reader:
        affyid = line[0]
        pathwayData = line[15]
        if "///" in pathwayData:
            thePaths = pathwayData.split("///")
            for path in thePaths:
                data = path.split("//")
                pathTitle = data[0].strip()
                if pathTitle not in PathList:
                    PathList.append(pathTitle)
                newfile.write(affyid + "\t" + pathTitle + "\n")
        elif "//" in pathwayData:
            data = pathwayData.split("//")
            pathTitle = data[0].strip()
            if pathTitle not in PathList:
                PathList.append(pathTitle)
            newfile.write(affyid + "\t" + pathTitle + "\n")
        else:
            pass
    newfile.close()
    file.close()

def AllPaths():
    newfile = open("AllPathsTable.txt", "w")
    for item in PathList:
        newfile.write(item + "\n")
    newfile.close()

def ProteinFamilyTable():
    file = open("ApoER2WithAndWithoutExon19.csv")
    csv_reader = csv.reader(file)
    newfile = open("PFamTable.txt", "w")
    for line in csv_reader:
        affyid = line[0]
        proteinData = line[16]
        if "///" in proteinData:
            theProteins = proteinData.split("///")
            for protein in theProteins:
                data = protein.split("//")
                proteinTitle = data[1].strip()
                newfile.write(affyid + "\t" + proteinTitle + "\n")
        elif "//" in proteinData:
            data = proteinData.split("//")
            proteinTitle = data[1].strip()
            newfile.write(affyid + "\t" + proteinTitle + "\n")
        else:
            pass
    newfile.close()
    file.close()

def ProteinDomainTable():
    file = open("ApoER2WithAndWithoutExon19.csv")
    csv_reader = csv.reader(file)
    newfile = open("PDomainTable.txt", "w")
    for line in csv_reader:
        affyid = line[0]
        proteinData = line[16]
        if "///" in proteinData:
            theProteins = proteinData.split("///")
            for protein in theProteins:
                data = protein.split("//")
                proteinTitle = data[1].strip()
                newfile.write(affyid + "\t" + proteinTitle + "\n")
        elif "//" in proteinData:
            data = proteinData.split("//")
            proteinTitle = data[1].strip()
            newfile.write(affyid + "\t" + proteinTitle + "\n")
        else:
            pass
    newfile.close()
    file.close()

def AffyTable():
    file = open("ApoER2WithAndWithoutExon19.csv")
    csv_reader = csv.reader(file)
    newfile = open("AffyTable.txt", "w")
    for line in csv_reader:
        affyid = line[0]
        negSignal = line[1]
        negDetection = line[2]
        vsSignal = line[3]
        vsDetection = line[4]
        logRatio = line[5]
        foldChange = line[6]
        change = line[7]
        symbol = line[8].strip()
        publicId = line[10]
        uniGeneId = line[11]
        newfile.write(affyid + "\t" + negSignal + "\t" + negDetection + "\t" + vsSignal + "\t" + vsDetection + "\t" + logRatio + "\t" + foldChange +"\t" + change + "\t" + symbol + "\t" + publicId + "\t" + uniGeneId + "\n")
    newfile.close()
    file.close()

def GeneTable():
    file = open("ApoER2WithAndWithoutExon19.csv")
    csv_reader = csv.reader(file)
    newfile = open("GeneTable.txt", "w")
    geneDict = {}
    for line in csv_reader:
        symbol = line[8].strip()
        title = line[9].strip()
        geneDict[symbol] = title
    del geneDict['---']
    for key in geneDict.keys():
        newfile.write(key + "\t" + geneDict[key] + "\n")
    newfile.close()
    file.close()

GoBPTable()
GoCCTable()
GoMFTable()
GoTable()
PathwayTable()
AllPaths()
ProteinFamilyTable()
ProteinDomainTable()
AffyTable()
GeneTable()










        


        
    
