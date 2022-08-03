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
        if (kVmax-20) <= sheet.cell_value(each, 0) <= (kVmax-10):
    
            yarray2Area.append(sheet.cell_value(each, 1))
            yarray2.append(sheet.cell_value(each, 1))
        else:
            yarray2.append(sheet.cell_value(each, 1))
    area2 = np.trapz(np.array(yarray2Area), dx = 1)
    yarray2New = []
    xarray2New = []
    yarrayNorm2 = yarray2/(np.linalg.norm(yarray2))
    #for each in xarray2:
     #   xarray2New.append(each*3)
        

    for each in yarray2: 
        yarray2New.append(each/50)
        
    plt.figure(1)
    plt.xlabel("Energy(keV)")
    plt.ylabel("Intensity")
    plt.plot(xarray2,yarray2)


    xarray = []
    yarray = []
    yarrayArea = []
    indexArr = []
    for i in range(1, kVmax):
        xarray.append(i)
    for i in range(1,kVmax):
        if (Ka-1) < i < (Ka+1):
            CR = ((i*10**3) - (Ka*10**3))**1.5
            yarray.append(((((CR+((kVmax - i)*Z)))*((e**((-22*10**2)/(i**3)))))))
        if (Kb-1) < i < (Kb+1):
            CR = ((i*10**3) - (Kb*10**3))**1.5
            yarray.append(((((CR+((kVmax - i)*Z)))*(((e**((-22*10**2)/(i**3))))))))
        else: 
            if (kVmax-20) < i < (kVmax-10):
                yarrayArea.append(((((kVmax - i)*Z))*(((e**((-22*10**2)/(i**3)))))))
                yarray.append(((((kVmax - i)*Z))*(((e**((-22*10**2)/(i**3)))))))
                indexArr.append(xarray.index(i))
            else:
                yarray.append(((((kVmax - i)*Z))*(((e**((-22*10**2)/(i**3)))))))
    for each in yarray: 
        if isinstance(each, complex):
            indexVal = yarray.index(each)
            yarray.remove(each)
    
        
    #xarray.pop()
    #xarray.pop()
    
    
    yarrayNorm = yarray/(np.linalg.norm(yarray))
    yarrayAreaNorm = []
    for each in indexArr:
        yarrayAreaNorm.append(yarrayNorm[each])


    diffArray = np.divide(yarray2Area, yarrayAreaNorm)
    meanVal = statistics.mean(diffArray)
    #for each in indexArr:
     #     yarrayNorm[each] = yarrayNorm[each] * meanVal
    yarrayNorm = yarrayNorm * meanVal
           
    plt.plot(xarray, yarrayNorm)
    plt.show()    
    return xarray, yarray



userkVp = int(input("Enter max kVp: "))
userMaterial = input("Enter which material you would like: ")
for each in range(6):
    if sheet.cell_value(each,0) == userMaterial:
        IntensityCal(sheet.cell_value(each, 0 + 1), userkVp, (1*10**-3), sheet.cell_value(each, 2), sheet.cell_value(each, 3))
    
           
