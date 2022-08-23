import csv
import json
from jsonmerge import merge

csvfile = open('C:\\Trabalho\\Arquivos\\i18n - revisado.csv', 'r')

resultPT = []
resultEN = []
resultES = []

resultOfColumn2 = []
lastColumn = ''

objJsonPT = {}
objJsonEN = {}
objJsonES = {}

reader = csv.DictReader(csvfile, delimiter=';')
for row in reader:
    if lastColumn != row['Column1']:
        filename = f'C:\\Trabalho\\Arquivos\\{lastColumn + ".pt"}.json'
        jsonfilePT = open(filename, 'w')
        filename = f'C:\\Trabalho\\Arquivos\\{lastColumn + ".en"}.json'
        jsonfileEN = open(filename, 'w')
        filename = f'C:\\Trabalho\\Arquivos\\{lastColumn + ".es"}.json'
        jsonfileES = open(filename, 'w')

        lastColumn = row['Column1']

        filePT = ""
        fileEN = ""
        fileES = ""

        for i in range(len(resultPT)):
            if(i >= 1):
                filePT = merge(filePT, resultPT[i])
            else:
                filePT = resultPT[i]

        for i in range(len(resultEN)):
            if(i >= 1):
                fileEN = merge(fileEN, resultEN[i])
            else:
                fileEN = resultEN[i]

        for i in range(len(resultES)):
            if(i >= 1):
                fileES = merge(fileES, resultES[i])
            else:
                fileES = resultES[i]


        #stringResult = ",".join(str(x) for x in resultPT)
        json.dump(filePT, jsonfilePT, ensure_ascii=False)
        json.dump(fileEN, jsonfileEN, ensure_ascii=False)
        json.dump(fileES, jsonfileES, ensure_ascii=False)

        resultPT = []
        resultEN = []
        resultES = []
    else:
        splitColumn2 = row['Column2'].split('.')
        backupObj = ''
        for i in reversed(range(len(splitColumn2))):
            if (i == len(splitColumn2) -1):
                objJsonPT = {
                    splitColumn2[i]: row['Column3']
                }
            else:
                objJsonPT = {
                    splitColumn2[i]: objJsonPT
                }

        for i in reversed(range(len(splitColumn2))):
            if (i == len(splitColumn2) -1):
                objJsonEN = {
                    splitColumn2[i]: row['Column4']
                }
            else:
                objJsonEN = {
                    splitColumn2[i]: objJsonEN
                }

        for i in reversed(range(len(splitColumn2))):
            if (i == len(splitColumn2) -1):
                objJsonES = {
                    splitColumn2[i]: row['Column5']
                }
            else:
                objJsonES = {
                    splitColumn2[i]: objJsonES
                }

        resultPT.append(objJsonPT)
        resultEN.append(objJsonEN)
        resultES.append(objJsonES)