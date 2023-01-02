"""A simple python library consisting of combinatorics functions

These functions are some of the most common functions used in combinatorics.
They are not intended to be extreemly performant but they should be accurate.
"""
def fact(n):
    """fact(n): where n is a positive integer of a number.
    used to calculate a factorial"""
    ans = 1
    for i in range(2,n+1):
        ans *= i
    return ans
def P(n,r):
    """P(n,r): where n and r are both positive
    calculate the number of permutations that can be created of length r
    given n distinct elements"""
    ans = 1
    for i in range(n-r+1, n+1):
        ans*=i
    return ans
def C(n,r):
    """C(n,r): where n may be positive or negative and r is non-negative
    counts the number of combinations that can be created by choosing r 
    from n distinct elements"""

    if n < 0:
        return C(-n+r-1,r) * (-1)**r
    return P(n,r) // fact(r)
def multinomial(n,*args):
    """multinomial(n, *args): where all arguments are non-negative
    and sum(args) <= n
    
    counts unique permutations of n given args[i] identical elements from group i """


    den = 1
    for k in args:
        den *= fact(k)
    return fact(n) // den

def stirling1(n,m):
    """sterling1(n,m): where n and m are non-negative

    counts permutations of n distinct elements arranged in 
    r distinct cycles.
    for example.  If you have 6 people and 3 three tables, 
    there are sterling1(6,3) unique ways for them to be seated assuming 
    that all tables are identical, every table has at least 1 person sitting at it, and that we do not want to count rotations or reflections"""

    ans1 = 0
    ans = 0
    for k in range(n-m+1):
        ans1 += 1/((n+k)*fact(n-m-k)*fact(n-m+k))
        nested_ans = 0
        for j in range(k+1):
            nested_ans += ((-1)**j * j**(n-m+k))/(fact(j)*fact(k-j))
        ans += nested_ans*ans1
    return ans * (fact(2*n-m)/fact(m-1))
def stirling2(n,k):
    """stirling2(n,k): where n and k are both non-negative
    counts how many ways we can partition n distinct elements into k
    non-empty groups"""
    ans = 0
    for i in range(k+1):
        ans += (-1)**i * C(k,i) * (k-i)**n
    return ans // fact(k)
def bell(n):
    """bell(n): where n is a positive integer:
        calculates the number of nonempty subsets a set of size 'n' can
        be partitioned into"""
    ans = 0
    for k in range(1,n+1):
        ans += stirling2(n,k)
    return ans
def stars_bars(n,k):
    """stars_bars(n,k) == C(n+k-1, k-1)
Where n is the number of identical items and k is tne number of buckets to place them in"""
    return C(n + k-1, k-1)
def binomial_theorem(a,b,n):
    """binomial_theorem(a,b,n)"""
    ans = 0
    for i in range(n+1):
        ans += C(n,i) * a**(n-i) * b**(i)
    return ans
def catalan(n):
    """catalin(n): where n is non-negative

    calculates the nth catalan number.
    catalan numbers appear in many counting problems including Dyck words of length 2n and number of structurally unique BSTs of size n"""
    return fact(2*n) // (fact(n+1)*fact(n))
class ptriangle:
    """this class creates pascals triangle"""
    def __init__(self,n=0):
        self.arr = []
        prev = [1]
        self.arr.append(prev)
        row = []
        for _ in range(2,n+1):
            row = [1]
            for i in range(len(self.arr) - 1 ):
                row.append(prev[i] + prev[i+1])
            row.append(1)
            self.arr.append(row)
            prev = row
    def get(self,row,col):
        if col >= row:
            raise IndexError("collumn must be in range [0,row]")
        if row >= len(self.arr): # grow triangle to requested size
            prev = self.arr[-1]
            for _ in range(row-len(self.arr)+1):
                curr = [1]
                for i in range(len(prev)-1):
                    curr.append(prev[i] + prev[i+1])
                curr.append(1)
                self.arr.append(curr)
                prev = curr

        return self.arr[row][col]

    def print(self):
        for row in self.arr:
            print(row)
    def data(self):
        return self.arr

class btriangle:
    """this class creates an instance of bell's triangle"""
    def __init__(self):
        """initialize bells triangle with first two rows"""
        self.arr = [[1]]
        self.arr.append([1,2])
    def get(self, row, col):
        """get value at (row,col) grow triangle if need be"""
        if col >= row:
            raise IndexError("collumn must be less than row")
        if col < 0 or row < 0:
            raise IndexError("row and col must both be positive integers")
        if row >= len(self.arr):
            for _ in range(row - len(self.arr) + 1):
                prev = self.arr[-1]
                curr = [self.arr[-1][-1]] # start each row with last element
                for p in prev:
                    curr.append(curr[-1] + p)
                prev = curr
                self.arr.append(curr)
        return self.arr[row][col]
    def print(self):
        """print bell's triangle"""
        for row in self.arr:
            for each in row:
                print(each)
    def data(self):
        """get raw array"""
        return self.arr
