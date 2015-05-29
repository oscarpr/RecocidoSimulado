'''
Created on 26/02/2015

@author: OPulidoRodriguez
'''

import math
import random
import copy

#Funcion para obtener la matriz de costos
def distancesFromCoords():
    f = open('berlin52.tsp')
    data = [line.replace("\n","").split(" ")[1:] for line in f.readlines()[6:58]]
    coords =  list(map(lambda x: [float(x[0]),float(x[1])], data))
    distances = []
    for i in range(len(coords)):
        row = []
        for j in range(len(coords)):
            row.append(math.sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2))
        distances.append(row)
    return distances


matriz = distancesFromCoords()
solucionInicial = []
nuevaSolucion = []
item = 0
costoInicial = 0
temperatura = 10000
alfa = 0.9995

#Funcion para perturbar la solucion
def perturbacion(tour):
    ciud = random.choice(tour)
    pos1 = tour.index(ciud)
    while True:
        pos2 = tour.index(random.choice(tour))
        if (pos1 != pos2):
            tour[pos1],tour[pos2] = tour[pos2], tour[pos1]
            break
    return tour

#Funcion para hallar el costo de una solucion
def costoTour(tour):
    costo = 0
    item = 0
    while item < 51:
        costo += matriz[tour[item]][tour[item+1]]
        item += 1
    return costo

#Se obtiene solucion inicial
while item < 52:
    solucionInicial.append(item)
    item += 1
    
#Se obtiene el costo de la solucion inicial
costoTour(solucionInicial)

while temperatura > 0.000001:    
    #Se obtiene  x'
    nuevaSolucion = copy.deepcopy(solucionInicial)
    nuevaSolucion = perturbacion(nuevaSolucion)
        
    #Costo x'
    xPrima = 0
    xPrima = costoTour(nuevaSolucion)   
    
    #Aceptacion de la nueva solucion
    if xPrima < costoInicial:
        solucionInicial = nuevaSolucion
        costoInicial = xPrima    
    elif xPrima > costoInicial:        
        papelito = random.uniform(0,1)
        x = -(xPrima - costoInicial)/temperatura
        p = math.exp(x)
        if papelito <= p:            
            solucionInicial = nuevaSolucion 
            costoInicial = xPrima
      
    temperatura = temperatura*alfa         
    
print("El recorrido mas corto es: ")
print(solucionInicial)
print("Con un peso de: ")
print(costoInicial)