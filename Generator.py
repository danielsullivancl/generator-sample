# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:46:51 2019

@author: daniel sullivan
"""
import random


def generateSample(individuals, percFs, n):
    
    sFemale = []
    sMale = []
    
    
    
    w = getAllWomen(individuals)
    m = getAllMen(individuals)
    
        

    random.shuffle(w)
    random.shuffle(m)
        
    sample = []
    
        
    for i in range(0, n):
        
        if(i/n <= percFs):
            sFemale.append(w[i])
        else:
            sMale.append(m[i])
    
    
    sample = sFemale + sMale
    
    random.shuffle(sample)
    
    return sample        

def getAllWomen(individuals) :
    
    women = []
    
    for i in individuals:
        value = i.split(';')[1]
        
        if value.lower() == 'f':
            women.append(i)
    
    return women
        
def getAllMen(individuals) :
    
    men = []
    
    for i in individuals:
        value = i.split(';')[1]
        
        if value.lower() == 'm':
            men.append(i)
    
    return men
        