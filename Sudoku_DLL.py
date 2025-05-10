import time

start = time.time()

r1 = list(range(3))
r2 = list(range(3,6))
r3 = list(range(6,9))

index_map = [[[x,y]for y in range(9)]for x in range(9)]
for lists in index_map: 
    for element in lists:         
        if element[0] in r1:
            element[0] = r1[:]
        elif element[0] in r2:
            element[0] = r2[:]
        else:
            element[0] = r3[:]
        if element[1] in r1:
            element[1] = r1[:]
        elif element[1] in r2:
            element[1] = r2[:]
        else:
            element[1] = r3[:]

def check(n,i,j):       
    for x in index_map[i][j][0]:
        for y in index_map[i][j][1]:
            if sudoku[x][y] == n:
                return False               
    for x in range(0,9):
        if sudoku[x][j] == n:
            return False                             
    for y in range(0,9):
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
    def __init__(self, sudoku):
        self.sudoku_DLL = DoublyLinkedList()
        for i in range(0,9):        
            for j in range(0,9):            
                if not sudoku[i][j]:
                    self.sudoku_DLL.append(sudoku[i][j], [i, j])
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
                sudoku[i][j] = current_node.value
                current_node = current_node.previous
                if not current_node:
                    raise Exception(f'no solution\niterations: {self.iterations}')
            elif check(current_node.value,i,j):
                sudoku[i][j] = current_node.value
                current_node = current_node.next
            else:
                current_node.value += 1
        return self
    
    def printer(self):
        print("solution:")
        printed_cells = 1
        for i in range(0,9):        
            for j in range(0,9):  
                if printed_cells%9:
                    print(sudoku[i][j], end = " ")
                else:
                    print(sudoku[i][j])
                printed_cells += 1
        print(f'iterations: {self.iterations}')  
        return self

def sudoku_solver(sudoku):
    Sudoku(sudoku).solver().printer()


sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 6, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 9, 0, 2, 0, 0],
          [0, 5, 0, 0, 0, 7, 0, 0, 0],
          [0, 0, 0, 0, 4, 5, 7, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 3, 0],
          [0, 0, 1, 0, 0, 0, 0, 6, 8],
          [0, 0, 8, 5, 0, 0, 0, 1, 0],
          [0, 9, 0, 0, 0, 0, 4, 0, 0]]

sudoku_solver(sudoku)                    

end = time.time() 

print(f"time: {round(end-start, 2)} s")
