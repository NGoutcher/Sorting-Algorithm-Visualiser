# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:23:09 2020

@author: Nathan
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random
import tkinter as tk
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class App(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.title("Sorting Algorithm Visualisation")
        self.data = []
        self.unsorted_data = []
        self.data_length = 51
        for i in range(self.data_length):
            self.data.append(random.randint(0, 1000))
        self.unsorted_data = self.data.copy()
        
        self.title = ""
        self.isSorted = False
        self.Fig = matplotlib.figure.Figure(figsize=(5,4),dpi=100)
        self.FigSubPlot = self.Fig.add_subplot(111)
        self.graph = self.FigSubPlot.bar(np.arange(len(self.data)), self.data, align='center', alpha=0.5)
        self.FigSubPlot.set_xlabel('List Size', fontsize = 10)
        self.FigSubPlot.set_ylabel('Data Values', fontsize = 8)
        self.canvas = FigureCanvasTkAgg(self.Fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
        buttonNewData = tk.Button(self, text="Reset Data", command=self.newData).pack(side=tk.LEFT)
        buttonBubbleSort = tk.Button(self, text="Bubble Sort", command=self.start_bubble).pack(side=tk.LEFT)
        buttonSelectionSort = tk.Button(self, text="Selection Sort", command=self.start_selection).pack(side=tk.LEFT)
        buttonMergeSort = tk.Button(self, text="Merge Sort", command=self.start_merge).pack(side=tk.LEFT)
        buttonInsertionSort = tk.Button(self, text="Insertion Sort", command=self.start_insertion).pack(side=tk.LEFT)
    
    def newData(self):
        self.data = []
        for i in range(self.data_length):
            self.data.append(random.randint(0, 1000))
        self.unsorted_data = self.data.copy()
        self.isSorted = False
        self.refresh_graph(self.data)
        
    def refresh_graph(self, data):
        self.FigSubPlot.clear()
        self.FigSubPlot.set_title(self.title)
        self.FigSubPlot.set_xlabel('List Size', fontsize = 10)
        self.FigSubPlot.set_ylabel('Data Values', fontsize = 8)
        if self.isSorted == False:
            self.graph = self.FigSubPlot.bar(np.arange(len(data)), data, align='center', alpha=0.5)
        else:
            self.graph = self.FigSubPlot.bar(np.arange(len(data)), data, align='center', alpha=0.5, color="g")
        self.canvas.draw()
        
    def start_selection(self):
        if self.isSorted:
            self.data = self.unsorted_data.copy()
            self.isSorted = False
            self.refresh_graph(self.data)
        self.data = self.selection_sort(self.data)
        self.isSorted = True
        self.refresh_graph(self.data)
        
    def start_bubble(self):
        if self.isSorted:
            self.data = self.unsorted_data.copy()
            self.isSorted = False
            self.refresh_graph(self.data)
        self.data = self.bubble_sort(self.data)
        self.isSorted = True
        self.refresh_graph(self.data)
        
    def start_merge(self):
        if self.isSorted:
            self.data = self.unsorted_data.copy()
            self.isSorted = False
            self.refresh_graph(self.data)
        self.data = self.merge_sort(self.data)
        self.isSorted = True
        self.refresh_graph(self.data)
        
    def start_insertion(self):
        if self.isSorted:
            self.data = self.unsorted_data.copy()
            self.isSorted = False
            self.refresh_graph(self.data)
        self.data = self.insertion_sort(self.data)
        self.isSorted = True
        self.refresh_graph(self.data)
        
    def bubble_sort(self, data):
        self.title = "Bubble Sort"
        n = len(data)
        swap = False
    
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    swap = True
                
            if swap == False:
                break
        
            self.refresh_graph(data)
        return data
    
    def selection_sort(self, data):
        self.title = "Selection Sort"
        for i in range(len(data)):
            min_index = i
            for j in range(i+1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j
            
            data[i], data[min_index] = data[min_index], data[i]
            
            self.refresh_graph(data)
        return data
    
    def merge_sort(self, data):
        self.title = "Merge Sort"
        if len(data) > 1:
            mid = len(data)//2
            l = data[:mid]
            r = data[mid:]
            
            self.merge_sort(l)
            self.merge_sort(r)
            
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
                
            self.refresh_graph(data)
        return data
    
    def insertion_sort(self, data):
        self.title = "Insertion Sort"
        for i in range(1, len(data)):
            key = data[i]
            
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key
        
            self.refresh_graph(data)
        return data

if __name__ == "__main__":
    app = App(None)
    app.mainloop()