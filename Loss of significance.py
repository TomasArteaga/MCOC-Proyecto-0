# -*- coding: utf-8 -*-
"""
Created on Sun Aug 04 21:32:22 2019

@author: josetomas
"""

import numpy as np
from decimal import *
import matplotlib.pylab as plt
from numpy import *

datos=[12*(10**-10),25*(10**-10),57*(10**-10)]

datos_tg=[tan(12),tan(25),tan(57)]
print datos_tg ,"datos transformado por la funcion tangente"

s = []
for i in datos:
    k = sp.float32(tan(i))
    s.append(k)
print s 

t = []
for i in datos:
    k = sp.float64(tan(i))
    t.append(k)
print t

error32=[(datos[0]-s[0])/datos[0],(datos[1]-s[1])/datos[1],(datos[2]-s[2])/datos[2]]
error64=[(datos[0]-t[0])/datos[0],(datos[1]-t[1])/datos[1],(datos[2]-t[2])/datos[2]]
print error32
print error64
#plt.figure(1)
plt.plot(datos_tg,error32)
plt.plot(datos_tg,error64)
plt.legend(["error32","error64"])
#plt.tittle("loss-of-significance")
plt.show()
