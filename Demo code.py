#Kramer's Law
import matplotlib.pyplot as plt
import numpy
from math import e


def IntensityCal(Z, kVmax, I, Ka, Kb):
    xarray = []
    yarray = []
    for i in range(1, kVmax):
        xarray.append(i)
    for i in range(1,kVmax):
        if (Ka-1) < i < (Ka+1):
            yarray.append(I*((((i*10**3) - (Ka*10**3))**1.5)+(kVmax - i)*Z*(e**((-22*10**3)/(i**3)))))
        elif (Kb-1) < i < (Kb+1):
            yarray.append(I*((((i*10**3) - (Kb*10**3))**1.5)+(kVmax - i)*Z*(e**((-22*10**3)/(i**3)))))
        else:
            yarray.append(I*((kVmax - i)*Z*(e**((-22*10**3)/(i**3)))))
    for each in yarray: 
        if isinstance(each, complex):
            ind = yarray.index(each)
            xarray.pop(ind)
            yarray.remove(each)
        
    return xarray, yarray


Cal1, Cal2 = IntensityCal(74, 160, (1*10**-3), 59.3, 67.6)
Cal3, Cal4 = IntensityCal(29, 160,(1*10**-3), 8.04, 8.19)
#Cal5, Cal6 = IntensityCal(45, 160, (1*10**-3), 20.2, 22.7)
#Cal7, Cal8 = IntensityCal(42, 160, (1*10**-3), 17.9, 19.5)

plt.figure(1)
plt.xlabel("Energy(keV)")
plt.ylabel("Intensity")

plt.plot(Cal1, Cal2)
plt.plot(Cal3, Cal4)
#plt.plot(Cal5, Cal6)
#plt.plot(Cal7, Cal8)
plt.show()
