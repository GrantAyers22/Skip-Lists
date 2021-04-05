import sys
import matplotlib.pyplot as plt
import time
import math
import random
sys.path.append("/C:/Users/12816/Documents/School/Junior-Year/Spring-2021/CS-3353/MidTerm/")
from skiplist import SkipList
from standardlist import StandardList
from avltree import AVLTree
from hashtable import HashTable
from doublylinkedlist import DoublyLinkedList

def insertion_plot(DATA_STRUCTURE_TABLE):
    c_index = 0
    for name, Data_Structure in dict(DATA_STRUCTURE_TABLE).items():
        x = list()
        y = list()
        colors = ['b',
                  #'g',
                  #'r',
                  'c',
                  #'m'
                  ]
        for max in range(1000, 10000, 1000):
            x.append(max)
            tick = time.perf_counter()
            for i in range(max):
                Data_Structure.insertElement(random.randrange(0, n))
            tock = time.perf_counter()
            y.append(tock-tick)
        plt.plot(x, y, color=colors[c_index])
        c_index+=1
        
    plt.xlabel("Number of Values")
    plt.ylabel("Time to Insert")
    plt.title("Insertion Times as a function of number of values")
    plt.show()

def search_plot(DATA_STRUCTURE_TABLE, n):
    c_index = 0
    colors = ['b',
              #'g',
              #'r',
              'c',
              #'m'
              ]
    for name, Data_Structure in dict(DATA_STRUCTURE_TABLE).items():
        x = list()
        y = list()
        
        for i in range(n):
            Data_Structure.insertElement(random.randrange(0, n))
        for i in range(100):  
            x.append(i)
            tick = time.perf_counter()
            Data_Structure.searchElement(random.randrange(0, n))
            tock = time.perf_counter()
            y.append(tock-tick)

        plt.plot(x, y, color=colors[c_index])
        c_index+=1
        
    plt.xlabel("Number of Searches")
    plt.ylabel("Time to Search")
    plt.title("Search time as a function of number of searches")
    plt.show()

def delete_plot(DATA_STRUCTURE_TABLE, n):
    c_index = 0
    colors = ['b',
              #'g',
              #'r',
              'c',
              #'m'
              ]
    for name, Data_Structure in dict(DATA_STRUCTURE_TABLE).items():
        x = list()
        y = list()
        
        for i in range(n):
            Data_Structure.insertElement(random.randrange(0, n))
        for i in range(100):  
            x.append(i)
            tick = time.perf_counter()
            Data_Structure.deleteElement(random.randrange(0, n))
            tock = time.perf_counter()
            y.append(tock-tick)

        plt.plot(x, y, color=colors[c_index])
        c_index+=1
        
    plt.xlabel("Number of Deletes")
    plt.ylabel("Time to Delete")
    plt.title("Deletion Times as a function of number of deletions")
    plt.show()        

def runner(DATA_STRUCTURE_TABLE, n):
    insertion_plot(DATA_STRUCTURE_TABLE)
    search_plot(DATA_STRUCTURE_TABLE, n)
    delete_plot(DATA_STRUCTURE_TABLE, n)
    

        
if __name__ == '__main__':
    r = list()
    n = 10000
    DATA_STRUCTURE_TABLE_1 = { #'AVL-Tree': AVLTree(),
                            #'Doubly-Linked List': DoublyLinkedList(),
                            #'Hash Table': HashTable(), 
                            'Skip List': SkipList()
                            #'Standard List': StandardList()
                           }
    r = runner(DATA_STRUCTURE_TABLE_1, n)
