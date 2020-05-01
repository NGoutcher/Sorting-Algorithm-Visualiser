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
    
    result = bubble_sort(data, plt)
    data = result[0]
    title = result[1]
    
    plt.title(title)
    plt.bar(np.arange(len(data)), data, align='center', alpha=0.5, color='g')
    plt.draw()
    plt.pause(0.001)
    
def plot_graph(data, graph, title):
    graph.title(title)
    graph.bar(np.arange(len(data)), data, align='center', alpha=0.5)
    graph.draw()
    graph.pause(0.001)
    
def bubble_sort(data, graph):
    title = "Bubble Sort"
    n = len(data)
    swap = False
    
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
                
        if swap == False:
            break
        
        plot_graph(data, graph, title)
    return data, title

def selection_sort(data, graph):
    title = "Selection Sort"
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        
        data[i], data[min_index] = data[min_index], data[i]
        
        plot_graph(data, graph, title)
    return data, title

def merge_sort(data, graph):
    title = "Merge Sort"
    if len(data) > 1:
        mid = len(data)//2
        l = data[:mid]
        r = data[mid:]
        
        merge_sort(l, graph)
        merge_sort(r, graph)
        
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                data[k] = l[i]
                i += 1
            else:
                data[k] = r[j]
                j += 1
            k += 1
            
        while i < len(l):
            data[k] = l[i]
            i += 1
            k += 1
            
        while j < len(r):
            data[k] = r[j]
            j += 1
            k += 1
            
        plot_graph(data, graph, title)
    return data, title
    