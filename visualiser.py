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
        for i in range(100):
            self.data.append(random.randint(0, 1000))

        self.title = ""
        self.Fig = matplotlib.figure.Figure(figsize=(5,4),dpi=100)
        self.FigSubPlot = self.Fig.add_subplot(111)
        self.graph = self.FigSubPlot.bar(np.arange(len(self.data)), self.data, align='center', alpha=0.5)
        self.canvas = FigureCanvasTkAgg(self.Fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
        button = tk.Button(self, text="Start", command=self.start).pack(side=tk.TOP)
    
    def refresh_graph(self, data):
        self.FigSubPlot.clear()
        self.FigSubPlot.set_title(self.title)
        self.graph = self.FigSubPlot.bar(np.arange(len(data)), data, align='center', alpha=0.5)
        self.canvas.draw()
        
    def start(self):
        self.selection_sort(self.data)
        
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

if __name__ == "__main__":
    app = App(None)
    app.mainloop()