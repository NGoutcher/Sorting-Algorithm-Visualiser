# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:23:09 2020

@author: Nathan
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def driver():
    data = []
    for i in range(100):
        data.append(random.randint(0, 1000))
    
    plt.ion()
    
    data = selection_sort(data, plt)
    
    
def plot_graph(data, graph, title):
    graph.title(title)
    graph.bar(np.arange(len(data)), data, align='center', alpha=0.5)
    graph.draw()
    graph.pause(0.0005)
    
def bubble_sort(data, graph):
    n = len(data)
    swap = False
    
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
                
        if swap == False:
            break
        
        plot_graph(data, graph, "Bubble Sort")
    return data

def selection_sort(data, graph):
    graph.title('Selection Sort')
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        
        data[i], data[min_index] = data[min_index], data[i]
        
        plot_graph(data, graph, "Selection Sort")
    return data