import csv
from copy import deepcopy

nombre = raw_input("Ingrese nombre archivo: ")
nombre = nombre + ".csv"

class DataTable():
    """docstring for DataTable"""
    Matriz_data = [ [ 1 for i in range(100) ] for j in range(100) ]
    NumF = 0
    NumC = 0
    def read_file(self, fileName):

        lines = []        
        with open(fileName, 'r') as f:
            for lines in f:
                line = lines.strip().split(",")
                self.NumC = 0
                for row in line:
                    self.Matriz_data[self.NumF][self.NumC] = int(row)
                    self.NumC = self.NumC + 1
                self.NumF = self.NumF + 1
    def getNumF(self):
        return self.NumF - 1

    def getNumC(self):
        return self.NumC - 1

    def getData(self, numF,numC):
        return self.Matriz_data[numF][numC]
    
    def __init__(self, fileName):
        self.read_file(fileName)

class Process():
    """docstring for Process"""
    def Find_Ns(self, Ro, arrayPositions, ObjDataTable, ColumPosition, FindData):
        index = 0
        cont = 0
        while (index < len(arrayPositions)):
            Result = 1
            indexRo = 0
            while (indexRo < len(Ro)):
                Result = Result * ObjDataTable.getData(arrayPositions[index],Ro[indexRo])
                indexRo = indexRo + 1
            Result = Result * ObjDataTable.getData(arrayPositions[index], ColumPosition)
            if (FindData == 'P'):
                if (Result == ObjDataTable.getData(arrayPositions[index], ObjDataTable.getNumC())):
                    cont = cont + 1
            else:
                if (Result != ObjDataTable.getData(arrayPositions[index], ObjDataTable.getNumC())):
                    cont = cont + 1
            index = index + 1
        if (FindData != 'P' and cont == 0):
            return 0.001
        return cont 

    def Result_Explication(self, RoArray, ObjDataTable, arrayData, arrayPosition):
        Result = 1
        indexRo = 0
        while (indexRo < len(RoArray)):
            Result = Result * ObjDataTable.getData(arrayData[arrayPosition], RoArray[indexRo])
            indexRo = indexRo + 1
        return Result               
        
           

objclass = DataTable(nombre)
objProcess = Process()
P = []
H = []
R = []
N = []
nP = []
nN = []
index = 0
while ( index <= objclass.getNumF()):
    if (objclass.getData(index, objclass.getNumC()) == 1):
        P.append(index)
    index = index + 1
while (len(P) != 0):
    if (len(N) == 0):
        index = 0
        while (index <= objclass.getNumF()):
            if (objclass.getData(index,objclass.getNumC()) == 0):
                N.append(index)
            index = index + 1
    index = 0
    position = -1
    divResul = -1
    while (index <= objclass.getNumC() - 1):
        nP.append(objProcess.Find_Ns(R, P, objclass, index, 'P'))
        nN.append(objProcess.Find_Ns(R, N, objclass, index, 'N'))
        if (position == -1):
            position = 0
            divResul = float(nP[index])/ float(nN[index])
        elif (divResul < float(nP[index])/ float(nN[index])):
            divResul = float(nP[index])/ float(nN[index])
            position = index
        index = index + 1
    print('Resultado de P', nP)
    print('Resultado de N', nN)
    print ('Posicion Mayor: ', position)
    R.append(position)
    indexN = 0
    del nP[:]
    del nN[:]
    while (indexN < len(N)):
        if (objProcess.Result_Explication(R, objclass, N, indexN) == objclass.getData(N[indexN], objclass.getNumC())):
            N.pop(indexN)
        else:
            indexN = indexN + 1
    print ('Vector N',N)
    print ('Vector P: ', P)
    print('Ro: ', R)
    if (len(N) == 0):
        H.append(deepcopy(R))
        print (H)
        indexH = 0
        del R[:]
        while (indexH < len(H)):
            indexP = 0
            while (indexP < len(P)):
                if (objProcess.Result_Explication(H[indexH], objclass, P, indexP) == objclass.getData(P[indexP], objclass.getNumC())):
                    print ('Posicion a Eliminar: ', P[indexP])
                    P.remove(P[indexP])
                else:
                    indexP = indexP + 1
            indexH = indexH + 1
        print (P)
print (H)        











