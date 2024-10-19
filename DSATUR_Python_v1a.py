#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:56:01 2023


@author: The Dude
"""
import numpy as np
import numpy.linalg as alg
import random

SIZE_GRAPH = 5
graph=np.array ([],[])
graph=np.zeros((SIZE_GRAPH,SIZE_GRAPH))
degre_de_tous_sommets=np.zeros(SIZE_GRAPH)
dsat=np.zeros(SIZE_GRAPH)
graph_coloration=np.zeros(SIZE_GRAPH)


#################################################################
## INTENDANCE GENERALE
#################################################################


###### REMPLISSAGE GRAPH MANUEL
def remplissage_du_graph_manuel():
    j=0
    while j<SIZE_GRAPH:
        i=j+1
        while (i<SIZE_GRAPH):
            print ("relation entre j=",j," et i=",i," =")
            a = int(input("= "))
            """
            while True:
                try:
                    a = int(input("= "))
                    if a > 0:
                        break
                except ValueError:
                        continue
            """
            print(a)
            graph[j][i]=a
            graph[i][j]=a
            ##graph.insert(j,i,a)
            i=i+1
        j=j+1


###### REMPLISSAGE GRAPH MANUEL
def remplissage_du_graph_random():
    j=0
    while j<SIZE_GRAPH:
        i=0
        while (i<SIZE_GRAPH-j):
            graph[j][i]= random.randint(0,1)
            graph[i][j]= graph[j][i]
            ##graph.insert(j,i,a)
            i=i+1
        j=j+1
        
### DISPLAY DU GRAPH        
def display_graph_inferieur():
    j=0
    while j<SIZE_GRAPH:
        i=0
        while (i<SIZE_GRAPH-j):
            print("Graph[",j,",",i,"]=",graph[j][i])
            i=i+1
        print("")
        j=j+1
 
def display_graph():
    j=0
    while j<SIZE_GRAPH:
        i=0
        while (i<SIZE_GRAPH):
            print("Graph[",j,",",i,"]=",graph[j][i])
            i=i+1
        print("")
        j=j+1




#################################################################
## tool box graph
#################################################################

def init_vecteur_negatif(vecteur):
    j=0
    while j<SIZE_GRAPH:
        vecteur[j]=-1
        j=j+1
    return vecteur

def comput_degre_sommet ():
    j=0
    while j<SIZE_GRAPH:
        i=0
        degre=0
        while (i<SIZE_GRAPH):
            if (i != j):
                degre += graph[j][i]
            ##graph.insert(j,i,a)
            i=i+1
        degre_de_tous_sommets[j]=degre
        j=j+1
        

def display_vecteur(vecteur,title):
    j=0
    print("Display vecteur:",title)
    while j<SIZE_GRAPH:
        print(" ",title,"[",j,"]=",vecteur[j])
        j=j+1   
      
    
###################################################################################
## DEBUT DSAT 
###################################################################################

def select_node_to_color():
    max_dsat=0
    node=0
    i=0
    while (i<SIZE_GRAPH):
        ## pas encore colorié et dsat max
        if((graph_coloration[i]<0) and (dsat[i]>=max_dsat)):
            node=i
            max_dsat=dsat[i]
        i+=1
    return node


def select_color_to_this_node(node):
    local_coloration=np.zeros(SIZE_GRAPH)
    local_coloration=init_vecteur_negatif (local_coloration)
    i=0
    while (i<SIZE_GRAPH):
        ## si ils sont voisin et déjà colorié
        if((graph_coloration[i]>=0) and (graph[node][i]>0)):
            tt2 = int (graph_coloration[i])
            local_coloration[tt2]=1
        i+=1
    display_vecteur(local_coloration, "local_coloration")    
    
   
    ##on cherche le minimum des couleurs non utilisés
    i=0
    while (i<SIZE_GRAPH):
        if(local_coloration[i]<0):
            return i
        i+=1
    return i



def update_dsat():
    j=0
    vecteur_color_used_by=np.zeros(SIZE_GRAPH)
    
    while j<SIZE_GRAPH:
        i=0
        vecteur_color_used_by = init_vecteur_negatif (vecteur_color_used_by)
        ##display_vecteur(vecteur_color_used_by, "vecteur_color_used_by")
        if (graph_coloration[j]<0): ## non colorier encore, sinon le
            while (i<SIZE_GRAPH):
                ## i voisin de j et colorié
                if (graph[j][i]>0) and ((graph_coloration[i]>=0)  ):
                    tt = int (graph_coloration[i])
                    ##print(" tt =", tt)
                    vecteur_color_used_by[tt]=1
                i+=1
            ## compter les 1 dans le tableau des couleurs
            i=0
            dsat[j]=0
            while (i<SIZE_GRAPH):
                if vecteur_color_used_by[i]>=0:
                    dsat[j]+=1
                i+=1  
            ##print("DSAT Update sommet j=",j)
            ##display_vecteur(vecteur_color_used_by, "vecteur_color_used_by")
            if dsat[j]==0:
                dsat[j]=degre_de_tous_sommets[j]
        j+=1
                          

        
def graph_coloration_by_DSAT():
    i=0
 

    while (i<SIZE_GRAPH):
        node_to_color = select_node_to_color()
        color = select_color_to_this_node (node_to_color)
        print("Etape ",i,": je colorie ",node_to_color, " par la couleur ",color)
        graph_coloration[node_to_color] = color
        update_dsat ()
        display_vecteur(graph_coloration, "graph_coloration")  
        i+=1

        
#################################################################
##  MAIN
#################################################################


init_vecteur_negatif(graph_coloration)
remplissage_du_graph_random()
#remplissage_du_graph_manuel()
display_graph()
comput_degre_sommet()
display_vecteur(degre_de_tous_sommets, "Degre")
dsat=degre_de_tous_sommets
display_vecteur(dsat, "DSAT")
graph_coloration_by_DSAT()
##display_vecteur(dsat, "Coloration")

DSATUR_v1.py
Affichage de DSATUR_v1.py