from abc import ABC, abstractmethod
class triangle(ABC):
    @abstractmethod
    def get(self,row,col):
        pass
    def print(self):
        for row in self.arr:
            for each in row:
                print(each,end=" ")
            print()
    def check_bounds(self, row,col):
        if col < 0 or row < 0:
            raise IndexError("row and collumn must be positive")
        if col > row:
            raise IndexError("collumn must be in range [0,row]")
    
class ptriangle(triangle):
    """this class creates pascals triangle"""
    def __init__(self,rows=0):
        """initialize pascals triagle of size max(n,1)"""
        if rows < 0:
            raise IndexError("constructor argument must be non-negative")
        self.arr = []
        prev = [1]
        self.arr.append(prev)
        row = []
        self.__grow_to(rows-1)
    def __grow_to(self, row):
        """helper function to grow tringle, DO NOT USE"""
        prev = self.arr[-1]
        for _ in range(row-len(self.arr) + 1):
            curr = [1]
            for i in range(len(prev)-1):
                curr.append(prev[i] + prev[i+1])
            curr.append(1)
            self.arr.append(curr)
            prev = curr

    def get(self,row,col):
        """get the value at the specified row and col"""
        self.check_bounds(row, col)
        if row >= len(self.arr): # grow triangle to requested size
            self.__grow_to(row)

        return self.arr[row][col]

    def data(self):
        """return the underlying python list"""
        return self.arr

class btriangle(triangle):
    """this class creates an instance of bell's triangle"""
    def __init__(self,rows=1):
        if rows < 0:
            raise IndexError("constructor argument must be non-negative")
        """initialize bells triangle with first row"""
        self.arr = [[1]]
        self.__grow_to(rows-1)

    def __grow_to(self, row):
        """helper function to grow tringle, DO NOT USE"""
        for _ in range(row - len(self.arr) + 1):
            prev = self.arr[-1]
            curr = [self.arr[-1][-1]] # start each row with last element
            for p in prev:
                curr.append(curr[-1] + p)
            prev = curr
            self.arr.append(curr)

    def get(self, row, col):
        """get value at (row,col) grow triangle if need be"""
        self.check_bounds(row, col)
        if row >= len(self.arr):
            self.__grow_to(row)
        return self.arr[row][col]
    def data(self):
        """return underlying python list"""
        return self.arr
