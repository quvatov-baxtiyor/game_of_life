#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
#from IPython.display import clear_output
from time import sleep


# In[6]:


class game_of_life:
    def __init__(self, grid_size_x, grid_size_y, starting_grid=0):
        self.grid_size_x, self.grid_size_y = grid_size_x, grid_size_y
        if starting_grid == 0:
            self.cells = np.zeros((grid_size_y,grid_size_x))
        else:
            self.cells = starting_grid
            
        self.next_iter = np.zeros((self.grid_size_y,self.grid_size_x))
        
        self.cells = self.cells.astype(int)
        self.next_iter = self.next_iter.astype(int)
    
    def neighbors(self, cell_x, cell_y):
        
        ### CORNERS ###
        if (cell_x == self.grid_size_x-1) and (cell_y == self.grid_size_y-1): #bottom right - only 3 neighbors
            return [self.cells[cell_y,   cell_x-1],
                    self.cells[cell_y-1, cell_x-1],
                    self.cells[cell_y-1, cell_x]]
        
        elif (cell_x == self.grid_size_x-1) and (cell_y == 0): #top right
            return [self.cells[cell_y+1, cell_x],
                    self.cells[cell_y+1, cell_x-1],
                    self.cells[cell_y,   cell_x-1]]
        
        elif (cell_x == 0) and (cell_y == self.grid_size_y-1): #bottom left
            return [self.cells[cell_y,   cell_x+1],
                    self.cells[cell_y-1, cell_x+1],
                    self.cells[cell_y-1, cell_x]]
                    
        elif (cell_x == 0) and (cell_y == 0): #top left
            return [self.cells[cell_y,   cell_x+1],
                    self.cells[cell_y+1, cell_x+1],
                    self.cells[cell_y+1, cell_x]]
        
        ### EDGES ###
        elif (cell_x == 0): #left
            return [self.cells[cell_y-1, cell_x],
                    self.cells[cell_y-1, cell_x+1],
                    self.cells[cell_y,   cell_x+1],
                    self.cells[cell_y+1, cell_x+1],
                    self.cells[cell_y+1, cell_x]]
        
        elif (cell_x == self.grid_size_x-1): #right
            return [self.cells[cell_y-1, cell_x],
                    self.cells[cell_y-1, cell_x-1],
                    self.cells[cell_y,   cell_x-1],
                    self.cells[cell_y+1, cell_x-1],
                    self.cells[cell_y+1, cell_x]]
        
        elif (cell_y == 0): #top
            return [self.cells[cell_y,   cell_x-1],
                    self.cells[cell_y+1, cell_x-1],
                    self.cells[cell_y+1, cell_x],
                    self.cells[cell_y+1, cell_x+1],
                    self.cells[cell_y,   cell_x+1]]
        
        elif (cell_y == self.grid_size_y-1): #bottom
            return [self.cells[cell_y,   cell_x-1],
                    self.cells[cell_y-1, cell_x-1],
                    self.cells[cell_y-1, cell_x],
                    self.cells[cell_y-1, cell_x+1],
                    self.cells[cell_y,   cell_x+1]]
        
        ### MIDDLE ###
        else:
            return [self.cells[cell_y,   cell_x+1],
                    self.cells[cell_y+1, cell_x+1],
                    self.cells[cell_y+1, cell_x],
                    self.cells[cell_y+1, cell_x-1],
                    self.cells[cell_y,   cell_x-1],
                    self.cells[cell_y-1, cell_x-1],
                    self.cells[cell_y-1, cell_x],
                    self.cells[cell_y-1, cell_x+1]]
    
    def life(self, cell_x, cell_y):
        alive = self.neighbors(cell_x, cell_y).count(1)
        if self.cells[cell_y, cell_x] == 1:
            if alive >= 2 and alive <= 3:
                return 1
            else:
                return 0
        else:
            if alive == 3:
                return 1
            else:
                return 0
    
    def cycle(self):
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                self.next_iter[y,x] = self.life(x,y)
        
        self.cells = self.next_iter
        self.next_iter = np.zeros((self.grid_size_y,self.grid_size_x))
    
    def printCells(self):
        for y in range(self.grid_size_y):
            for x in range(self.grid_size_x):
                if self.cells[y,x] == 1:
                    print("█", end="")
                else:
                    print(" ", end="")
            print("")
    
                


# In[7]:


def print_2D(array):
    for y in array:
        for x in y:
            print(x, end=" ")
        print("")


# In[8]:


test = game_of_life(20,20)
test.cells[1,17] = 1
test.cells[2,16] = 1
test.cells[3,16] = 1
test.cells[3,17] = 1
test.cells[3,18] = 1


# In[9]:


while True:
    test.cycle()
    print("\u001b[999A\u001b[999D")
    test.printCells()
    sleep(0.1)


# In[ ]:




