# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:05:08 2017

@author: canda
"""

import numpy as np
import math
import matplotlib.pyplot as mpl

def getTstar(c,r):
    if not(c == 0) and not(r == 0):
        return (1/c) * math.log(1/r)
    else :
        print("Erreur division par 0 : c ou r vaut 0")
        

def create_simulation(c,n):
    r_points = np.random.random_sample(n)
    tstar_points = []
    for i in range(0,len(r_points)):
        tstar_points.append(getTstar(c,r_points[i]))

    return tstar_points
    

def create_courbe(points):
    n = len(points)
    points.sort()
    x_max = int(points[n-1])
    
    pas = 1 / n
    y = []
    for i in range(0,n):
        y.append(1-(i*pas))
    
    mpl.plot(points,y,label='moyenne des graphes')
    mpl.axis([0,x_max,0,1])
    mpl.xlabel('Time in s')
    mpl.ylabel('Quantite de molecules')
    mpl.title('Quantite de molecules selon le temps')
    mpl.show()
    
    
def simulate(c,n):
    points = create_simulation(c,n)
    create_courbe(points)
    

def courbe_unique():
    point = np.random.random_sample(1)
    tstar_point = getTstar(1,point)
    y = [1.0,1.0,0.0,0.0]
    mpl.plot([0.0,tstar_point,tstar_point,tstar_point+1.0],y,label='Quantité de molécule selon le temps')
    mpl.xlabel('Time in s')
    mpl.ylabel('Quantite de molecules')
    mpl.title('Quantite de molecules selon le temps')
    mpl.axis([0,tstar_point+1.0,0,1.2])
    mpl.show()
    

for i in range(0,3):
    courbe_unique()

for c in [0.1,1,100]:
    for n in [10,100,1000000,25000000]:
        simulate(c,n)

