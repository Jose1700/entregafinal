#Jose Martinez Hernandez 09/06/2021
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from bresenham import bresenham
from DDA import DDA
matriz = []
matrizOperacional = []
limites = [0, 0, 10, 10]
fig = plt.figure()
ax = fig.add_subplot(111)
    
def llenadoMatriz(aristas, centro, punto0):  
    agr=0
    mayor=0
    menor=7
    x1, y1 = centro
    x2, y2 = punto0 
    for i in range(aristas):
        matriz.append([])
        for j in range(2): 
            if j == 0:
                valor = round((x1+math.cos(agr)*(x2 - x1)-math.sin(agr) * (y2 - y1)))
                matriz[i].append(valor)
            else: 
                valor = round((y1 + math.sin(agr) * (x2 - y1) + math.cos(agr)  * (y2 - y1)))
                matriz[i].append(valor)
        agr += math.radians(360/aristas)

def graficacion(m, aristas, met, color):
    resultado=[]
    for f in range(aristas):
        if f == aristas-1:
            if met == 1:
                plt.title ="DDA"
                valores = DDA(m[f][0], m[f][1], m[0][0], m[0][1])
            else: 
                valores = list(bresenham(m[f][0], m[f][1], m[0][0], m[0][1]))
            resultado+=valores

        else:
            if met==1:
                valores = DDA(m[f][0], m[f][1], m[f+1][0], m[f+1][1])
            else: 
                valores = list(bresenham(m[f][0], m[f][1], m[f+1][0], m[f+1][1]))
            resultado+=valores
            
    for i in resultado:
        rect1 = matplotlib.patches.Rectangle((i),1, 1,linewidth=1, edgecolor=color, facecolor='none')
        ax.add_patch(rect1)
    
    for r in m:
        rect1 = matplotlib.patches.Rectangle((r),1, 1,linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect1)
 
def traslacion(aristas, metodo):
    comodin = matriz
    for i in range(0, aristas):
        comodin[i].append(1)
    puntos=int(input("Veces se va a trasladar:"))
    matrizOperacional.append([])   
    matrizOperacional[0].append(1)
    matrizOperacional[0].append(0)
    matrizOperacional.append([]) 
    matrizOperacional[1].append(0)
    matrizOperacional[1].append(1)
    matrizOperacional.append([])  
    matrizOperacional[2].append(1)  
    matrizOperacional[2].append(1)
       
    for i in range (0, puntos):
        matrizOperacional[2][0] = int(input("Trasladar en x: "))
        matrizOperacional[2][1] = int(input("Trasladar en y: "))    
        tras = multiplicar_matrices(comodin,matrizOperacional)
        print("Matriz trasladad: ", tras)
        graficacion(tras, aristas, metodo, "y")
        mayor(tras, aristas)
        
def escalamiento(aristas, metodo):
    comodin = matriz
    for i in range(0, aristas):
        comodin[i].append(1)
    puntos=int(input("Veces se va a escalar:"))
    matrizOperacional.append([])   
    matrizOperacional[0].append(1)
    matrizOperacional[0].append(0)
    matrizOperacional.append([]) 
    matrizOperacional[1].append(0)
    matrizOperacional[1].append(1)
    matrizOperacional.append([])  
    matrizOperacional[2].append(1)  
    matrizOperacional[2].append(1)
    color = "y"    
    for i in range (0, puntos):
        matrizOperacional[0][0] = float(input("Escalar en x: "))
        matrizOperacional[1][1] = float(input("Escalar en y: "))    
        tras = multiplicar_matrices(comodin,matrizOperacional)
        print("Matriz escalada: ", tras)
        graficacion(tras, aristas, metodo, color)
        mayor(tras, aristas)
        
def rotacion(aristas, metodo):
    comodin = matriz
    for i in range(0, aristas):
        comodin[i].append(1)
    puntos=int(input("Veces se va a rotar:"))
    matrizOperacional.append([])   
    matrizOperacional[0].append(1)
    matrizOperacional[0].append(0)
    matrizOperacional.append([]) 
    matrizOperacional[1].append(0)
    matrizOperacional[1].append(1)
    matrizOperacional.append([])  
    matrizOperacional[2].append(0)  
    matrizOperacional[2].append(0)
    color = "g"    
    for i in range (0, puntos):
        grados = int(input("Grados a rotar la figura: "))
        grados = math.radians(grados)
        matrizOperacional[0][0] = math.cos(grados)    
        matrizOperacional[0][1] = math.sin(grados) 
        matrizOperacional[1][0] = -math.sin(grados)
        matrizOperacional[1][1] = math.cos(grados)  
        tras = multiplicar_matrices(comodin,matrizOperacional)
        print("Matriz rotada: ", tras)
        graficacion(tras, aristas, metodo, color)
        mayor(tras, aristas)
    
def multiplicar_matrices(m1, m2):
    if len(m1[0]) == len(m2):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    m3[i][j] += round(m1[i][k] * m2[k][j])
        return m3        
 
def mayor(matriza, aristas):
    for i in range(aristas): 
        if matriza[i][0] < limites[0]:
            limites[0]= matriza[i][0]
        if matriza[i][0] > limites[2]:
            limites[2] = matriza[i][0]
        
        if matriza[i][1] < limites[1]:
            limites[1] = matriza[i][1]
        if matriza[i][1] > limites[3]:
            limites[3] = matriza[i][1]   
  
    plt.xlim([limites[0]-2, limites[2] +2])
    plt.ylim([limites[1]-2, limites[3]+2])   
        
    return menorx, menory, mayorx, mayory

if __name__ == "__main__": 
    mayorx = 10
    menory = 0
    mayory = 10
    menorx = 0
    met = int(input("Ingrese el medoto a utilizar\n1.DDA\n2.Bresenham:\n"))
    aristas = int(input("Ingresa los lados de tu figura: "))
    x1 = int(input("Ingresa x1 del centro de tu figura: "))
    y1 = int(input("Ingresa y1 del centro de tu figura: "))
    l = int(input("Ingresa el tamaño de tus lados: "))
    punto0= (x1+l, y1)
    origen = (x1, y1)
    llenadoMatriz(aristas, origen, punto0)
    
    graficacion(matriz, aristas, met, "b")
    seleccionMetodo = int(input("Ingrese la accion a realizar\n1.Solo mostrar\n2.Traslación\n3.Escalamiento\n4.Rotacion\n"))
    mayor(matriz, aristas)
    print("Matriz original", matriz)
    if seleccionMetodo==1:
        print("Mostrado con exito")
    elif seleccionMetodo==2:
        traslacion(aristas, met)
    elif seleccionMetodo==3:
        escalamiento(aristas, met)
    elif seleccionMetodo==4:       
        rotacion(aristas, met)
    else: 
        print("Selecciona una opciona valida")
    plt.show() 