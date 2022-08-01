#Kramer's Law
import matplotlib.pyplot as plt
import numpy as np
from math import e
import pandas as pd 
import xlrd
from sklearn import preprocessing
import statistics


def Filtration(MolAtt, PathLen, Conc):
    absorb = MolAtt * PathLen * Conc
    return absorb



loc = ('X-Ray data.xls')

wb = xlrd.open_workbook(loc)     
sheet = wb.sheet_by_index(0)

df = pd.read_excel(r'X-Ray data.xls')

def IntensityCal(Z, kVmax, I, Ka, Kb):
    loc = ('X-Ray image dataT.xls')
    wb = xlrd.open_workbook(loc)     
    sheet = wb.sheet_by_index(0)
    xarray2 = []
    yarray2 = []
    yarray2Area = []
    for each in range(183):
        xarray2.append(sheet.cell_value(each,0))
    for each in range(183):
        if 80 <= sheet.cell_value(each, 0) <= 90:
    
            yarray2Area.append(sheet.cell_value(each, 1))
            yarray2.append(sheet.cell_value(each, 1))
        else:
            yarray2.append(sheet.cell_value(each, 1))
    area2 = np.trapz(np.array(yarray2Area), dx = 1)

    
    plt.figure(1)
    plt.xlabel("Energy(keV)")
    plt.ylabel("Intensity")
    plt.plot(xarray2,yarray2)


    xarray = []
    yarray = []
    yarrayArea = []
    indexArr = []
    print(Ka)
    print(Kb)
    for i in range(1, kVmax):
        xarray.append(i)
    for i in range(1,kVmax):
        if (Ka-1) < i < (Ka+1):
            CR = ((i*10**3) - (Ka*10**3))**1.5
            yarray.append((CR+((kVmax - i)*Z*(e**((-22*10**2)/(i**3))))))
        elif (Kb-1) < i < (Kb+1):
            CR = ((i*10**3) - (Kb*10**3))**1.5
            yarray.append((CR+((kVmax - i)*Z*(e**((-22*10**2)/(i**3))))))
        else: 
            if 80 < i < 90:
                yarrayArea.append(((kVmax - i)*Z*(e**((-22*10**2)/(i**3)))))
                yarray.append(((kVmax - i)*Z*(e**((-22*10**2)/(i**3)))))
                indexArr.append(xarray.index(i))
            else:
                yarray.append(((kVmax - i)*Z*(e**((-22*10**2)/(i**3)))))
    for each in yarray: 
        if isinstance(each, complex):
            ind = yarray.index(each)
            xarray.pop(ind)
            yarray.remove(each)
    
    
    yarrayNorm = yarray/(np.linalg.norm(yarray))
    yarrayAreaNorm = []
    for each in indexArr:
        
        yarrayAreaNorm.append(yarrayNorm[each])
    area = np.trapz(np.array(yarrayAreaNorm), dx = 1)

    print(yarrayAreaNorm)
    print(yarray2Area)
    
    #yarray2Area = yarray2Area[:-1]
    #yarray2Area = yarray2Area[:-1]
    diffArray = np.subtract(yarray2Area, yarrayAreaNorm)
    #print(diffArray)
    meanVal = statistics.mean(diffArray)
    #print(meanVal)
    yarrayNorm = yarrayNorm + meanVal
    #addArr = np.add(yarrayAreaNorm, diffArray)
    #print(addArr)
    #for each in indexArr:
    #    yarrayNorm[each] = addArr[each - 80]
    
           
    plt.plot(xarray, yarrayNorm)
    plt.show()    
    return xarray, yarray



user = input("Enter which element you like graph: ")
for each in range(6):
    if sheet.cell_value(each,0) == user:
        IntensityCal(sheet.cell_value(each, 0 + 1), 100, (1*10**-3), sheet.cell_value(each, 2), sheet.cell_value(each, 3))
    
           
