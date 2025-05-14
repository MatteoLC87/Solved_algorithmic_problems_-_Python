# -*- coding: utf-8 -*-
"""
Created on Fri May  9 18:49:10 2025

@author: matte
"""

import time

start = time.time()

class Helper:
    def __init__(self):  
        r1, r2, r3 = list(range(3)), list(range(3, 6)), list(range(6, 9))
        self.index_map = [[[i,j]for j in range(9)]for i in range(9)]
        for row in self.index_map: 
            for col in row:
                for i in range(2):
                    col[i] = r1 if col[i] in r1 else r2 if col[i] in r2 else r3

    def is_safe(self, n, i, j):       
        for x in self.index_map[i][j][0]:
            for y in self.index_map[i][j][1]:
                if sudoku[x][y] == n:
                    return False               
        for x in range(0, 9):
            if sudoku[x][j] == n:
                return False                             
        for y in range(0, 9):
            if sudoku[i][y] == n:
                return False                 
        return True


class Node:
    def __init__(self, value, _9x9_position):
        self.value = value
        self.next = None
        self.previous = None
        self._9x9_position = _9x9_position


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
    
    def append(self, value, _9x9_position):
        new_node = Node(value, _9x9_position)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self._length += 1
        return self
    
    
class Sudoku:
    def __init__(self, sudoku_matrix):
        self.helper = Helper()
        self.sudoku_matrix = sudoku_matrix
        self.sudoku_DLL = DoublyLinkedList()
        for i in range(0, 9):        
            for j in range(0, 9):            
                if not sudoku_matrix[i][j]:
                    self.sudoku_DLL.append(sudoku_matrix[i][j], [i, j])
        self.iterations = 0
                    
    def solver(self):
        current_node = self.sudoku_DLL.head
        while current_node:
            self.iterations += 1
            i, j = current_node._9x9_position[0], current_node._9x9_position[1]
            if not current_node.value:
                current_node.value += 1
            if current_node.value == 10:
                current_node.value = 0
                self.sudoku_matrix[i][j] = current_node.value
                current_node = current_node.previous
                if not current_node:
                    raise Exception(f'no solution\niterations: {self.iterations}')
            elif self.helper.is_safe(current_node.value,i,j):
                self.sudoku_matrix[i][j] = current_node.value
                current_node = current_node.next
            else:
                current_node.value += 1
        return self
    
    def printer(self):
        print("solution:")
        for i in range(0, 9):        
            for j in range(0, 9):  
                if j != 8:
                    print(self.sudoku_matrix[i][j], end = " ")
                else:
                    print(self.sudoku_matrix[i][j])       
        print(f'iterations: {self.iterations}')  
        return self
    
    
    def get_solution(self):
        self.solver().printer()
        return self
       

sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 6, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 9, 0, 2, 0, 0],
          [0, 5, 0, 0, 0, 7, 0, 0, 0],
          [0, 0, 0, 0, 4, 5, 7, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 3, 0],
          [0, 0, 1, 0, 0, 0, 0, 6, 8],
          [0, 0, 8, 5, 0, 0, 0, 1, 0],
          [0, 9, 0, 0, 0, 0, 4, 0, 0]]

Sudoku(sudoku).get_solution()
           
end = time.time() 

print(f"time: {round(end-start, 2)} s")
