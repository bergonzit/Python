import time
import math
import numpy as np
import matplotlib.pyplot as plt


N, M = 600, 1000
matriz = np.random.choice([1, 0], size=(N, M),p=[0.35,0.65])

def vecinos(m):
    aux = np.zeros((N,M))
    for i in range(len(m)):
        for j in range(len(m[i])):
            suma = 0
            if (i == 0):
                if (j == 0):
                    suma = m[i+1][j] + m[i+1][j+1] + m[i][j+1]
                elif (j == len(m[i]) - 1):
                    suma = m[i+1][j] + m[i+1][j-1] + m[i][j-1]
                else:
                    suma = m[i+1][j] + m[i+1][j+1] + m[i][j+1] + m[i][j-1] + m[i+1][j-1]
            elif (i == len(m) - 1):
                if (j == 0):
                    suma = m[i-1][j] + m[i-1][j+1] + m[i][j+1]
                elif (j == len(m[i]) - 1):
                    suma = m[i-1][j] + m[i-1][j-1] + m[i][j-1]
                else:
                    suma = m[i-1][j] + m[i-1][j+1] + m[i][j+1] + m[i][j-1] + m[i-1][j-1]
            else:
                if (j == 0):
                    suma = m[i-1][j] + m[i-1][j+1] + m[i][j+1] + m[i+1][j+1] + m[i+1][j]
                elif (j == len(m[i]) - 1):
                    suma = m[i-1][j] + m[i-1][j-1] + m[i][j-1] + m[i+1][j-1] + m[i+1][j]
                else:
                    suma = m[i-1][j-1] + m[i-1][j] + m[i-1][j+1] + m[i][j+1] + m[i+1][j+1] + m[i+1][j] + m[i+1][j-1] + m[i][j-1]
            aux[i][j] = suma
    return aux

#plt.imshow(matriz, cmap='gray')   
#plt.show()
#plt.imshow(vecinos(matriz), cmap='gray')   
#plt.show()


for i in range(15):
    matriz = np.where(vecinos(matriz) >= 4, 1,0)
matriz = np.where(vecinos(matriz) >= 3, 1,0)
plt.imshow(vecinos(matriz), cmap='gray')
#plt.imshow(matriz, cmap='gray')
plt.show()
