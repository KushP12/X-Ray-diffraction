#Kramer's Law

#import the necessary libraries required
import matplotlib.pyplot as plt
import numpy as np
from math import e
import pandas as pd 
import xlrd
from sklearn import preprocessing
import statistics

#created a function for the filtration, with variables that you can change
def Filtration(MolAtt, PathLen, Conc):
    absorb = MolAtt * PathLen * Conc
    return absorb



loc = ('X-Ray data.xls')

wb = xlrd.open_workbook(loc) #allows access to the excel file to retrieve data    
sheet = wb.sheet_by_index(0)

df = pd.read_excel(r'X-Ray data.xls')

def IntensityCal(Z, kVmax, I, Ka, Kb): #defined a function to run the comparison    
    loc = ('X-Ray image dataM.xls') #retrieves data for Molybdenum element
    wb = xlrd.open_workbook(loc)     
    sheet = wb.sheet_by_index(0) #retrieves data line by line from excel
    xarray2 = []
    yarray2 = []
    yarray2Area = []
    for each in range(166): #append x-values to an array to be plotted as it can't be straight from the excel file
        xarray2.append(sheet.cell_value(each,0))
    for each in range(166): #append y-values to an array to be plotted as it can't be straight from the excel file
        if (kVmax-10) <= sheet.cell_value(each, 0) <= (kVmax-5): #separates values that are to be normalized and not to be normalized
    
            yarray2Area.append(sheet.cell_value(each, 1))
            yarray2.append(sheet.cell_value(each, 1))
        else:
            yarray2.append(sheet.cell_value(each, 1))
    area2 = np.trapz(np.array(yarray2Area), dx = 1) #Calculates the area under the values to be normalized. The area can be used to normalize the y-values so it easier to do a comparison

    yarray2New = []
    xarray2New = []
    yarrayNorm2 = yarray2/(np.linalg.norm(yarray2)) # Function that normalizes all y-values
    for each in xarray2:
        xarray2New.append(each*4.5)
        

    #for each in yarray2: 
     #   yarray2New.append(each/50)
        
    plt.figure(1)
    plt.xlabel("Energy(keV)")
    plt.ylabel("Intensity")
    plt.plot(xarray2New,yarray2) #Plots out the x-values and y-values


    xarray = []
    yarray = []
    yarrayArea = []
    indexArr = []
    for i in range(1, kVmax):
        xarray.append(i)
    for i in range(1,kVmax):
        if (Ka-1) < i < (Ka+1): #identifies the points where the Ka characteristic ray occurs and appends to the yarray
            CR = ((i*10**3) - (Ka*10**3))**1.5
            yarray.append(((((CR+((kVmax - i)*Z)))*((e**((-22*10**2)/(i**3)))))))
        if (Kb-1) < i < (Kb+1): #identifies the points where the Kb characteristic ray occurs and appends to the yarray
            CR = ((i*10**3) - (Kb*10**3))**1.5
            yarray.append(((((CR+((kVmax - i)*Z)))*(((e**((-22*10**2)/(i**3))))))))
        else: #appends the rest of the Y-values to the yarray to be plotted
            if (kVmax-10) < i < (kVmax-5):
                yarrayArea.append(((((kVmax - i)*Z))*(((e**((-22*10**2)/(i**3)))))))
                yarray.append(((((kVmax - i)*Z))*(((e**((-22*10**2)/(i**3)))))))
                indexArr.append(xarray.index(i))
            else:
                yarray.append(((((kVmax - i)*Z))*(((e**((-22*10**2)/(i**3)))))))
    for each in yarray:  # this for statement removes the complex numbers from the y-array.
        if isinstance(each, complex):
            indexVal = yarray.index(each)
            yarray.remove(each)
    
        
    #xarray.pop()
    #xarray.pop()
    
    #this to help the scaling of the data to make it easier to compare
    yarrayNorm = yarray/(np.linalg.norm(yarray)) #normalizes all the y-array values for the simulated data
    yarrayAreaNorm = []
    for each in indexArr:
        yarrayAreaNorm.append(yarrayNorm[each])
    yarrayNew2 = []
    for each in yarray:
        yarrayNew2.append(each/2)


    #diffArray = np.divide(yarray2Area, yarrayAreaNorm)
    #meanVal = statistics.mean(diffArray)
    #for each in indexArr:
     #     yarrayNorm[each] = yarrayNorm[each] * meanVal
    #yarrayNorm = yarrayNorm * meanVal
           
    plt.plot(xarray, yarray) #plots out the simulated data
    plt.show()    
    return xarray, yarray


#following code makes it more intuitive and user friendly by letting them choose the Max kVp and anode material
userkVp = int(input("Enter max kVp: "))
userMaterial = input("Enter which material you would like: ")
for each in range(6):
    if sheet.cell_value(each,0) == userMaterial:
        IntensityCal(sheet.cell_value(each, 0 + 1), userkVp, (1*10**-3), sheet.cell_value(each, 2), sheet.cell_value(each, 3))
    
