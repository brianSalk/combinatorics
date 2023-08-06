"""A simple python library consisting of combinatorics functions

These functions are some of the most common functions used in combinatorics.
They are not intended to be extreemly performant but they should be accurate.
"""
import typing
def P(n: int,r: int) -> int:
    """P(n,r): where n and r are both positive
    calculate the number of permutations that can be created of length r
    given n distinct elements"""
    if n < 0 or r < 0:
        raise ValueError(f'n and r must be non-negative')
    ans = 1
    for i in range(n-r+1, n+1):
        ans*=i
    return ans


def C(n: int,r: int) -> int:
    """C(n,r): where n may be positive or negative and r is non-negative
    counts the number of combinations that can be created by choosing r 
    from n distinct elements"""
    if r < 0:
        raise ValueError("r must be non-negative")
    if n < 0:
        return C(-n+r-1,r) * (-1)**r
    return P(n,r) // fact(r)


def fact(n: int) -> int:
    """fact(n): where n is a positive integer of a number.
    used to calculate a factorial"""
    return P(n,n)


def multinomial(n: int,*args: int) -> int:
    """multinomial(n, *args): where all arguments are non-negative
    and sum(args) <= n
    
    counts unique permutations of n given args[i] identical elements from group i """
    if n < 0 or any(each < 0 for each in args):
        raise ValueError('all arguments must be non-negative')
    if sum(args) > n:
        raise ValueError('sum of args must not exceed n')
    den = 1
    for k in args:
        den *= fact(k)
    return fact(n) // den

def stirling1(n: int,k: int) -> int:
    """sterling1(n,m): where n and m are non-negative

    counts permutations of n distinct elements arranged in 
    r distinct cycles.
    for example.  If you have 6 people and 3 three tables, 
    there are sterling1(6,3) unique ways for them to be seated assuming 
    that all tables are identical, every table has at least 1 person sitting at it, and that we do not want to count rotations or reflections"""
    if n < 0:
        raise ValueError('n must be positive')
    if k > n:
        raise ValueError('k must be in the range [0,n]')
    if n == k == 0:
        return 0
    def __S1(n, k):
        if n == k == 0:
            return 1
        elif n == 0 or k == 0:
            return 0
        return -(n-1)*__S1(n-1,k) + __S1(n-1,k-1)
    ans = __S1(n,k)
    return ans if ans >=0 else -ans

def stirling2(n: int,k: int) -> int:
    """stirling2(n,k): where n and k are both non-negative
    counts how many ways we can partition n distinct elements into k
    non-empty groups"""
    ans = 0
    for i in range(k+1):
        ans += (-1)**i * C(k,i) * (k-i)**n
    return ans // fact(k)


def bell(n: int) -> int:
    """bell(n): where n is a non-negative integer:
        calculates the number of nonempty subsets a set of size 'n' can
        be partitioned into"""
    if n < 0:
        raise ValueError('n must be non-negative')
    ans = 0
    for k in range(1,n+1):
        ans += stirling2(n,k)
    return ans if ans != 0 else 1

def ordered_bell(n: int) -> int:
    """ordered_bell(n): where n is a non-negative integer

    counts the number of permutations of non-empty sets that a set of size 'n' can be partitioned into"""
    if n < 0:
        raise ValueError('n must be non-negative')
    ans = 0
    for k in range(1,n+1):
        ans += ( fact(k) * stirling2(n,k) )
    return ans if ans != 0 else 1
# should i just delete this?
def binomial_theorem(a,b,n) -> int:
    """binomial_theorem(a,b,n)
    (a+b)**n"""
    ans = 0
    for i in range(n+1):
        ans += C(n,i) * a**(n-i) * b**(i)
    return ans
    
def stars_bars(n: int,k: int) -> int:
    """stars_bars(n,k) == C(n+k-1, k-1)
Where n is the number of identical items and k is tne number of buckets to place them in"""
    return C(n + k-1, k-1)


def catalan(n:int) -> int:
    """catalin(n): where n is non-negative

    calculates the nth catalan number.
    catalan numbers appear in many counting problems including Dyck words of length 2n and number of structurally unique BSTs of size n"""
    return fact(2*n) // (fact(n+1)*fact(n))


def paths_in_matrix(m:int,n:int) -> int:
    """paths_in_matrix(m,n)

    calculates the number of shortest paths from one corner to
    the other in a mXn matrix"""
    return C(n+m-2, n-1)


def pbinom(n:int,r:int,p: float=.5,type:str='equal') -> float:
    """probability of getting r successes in n attempts with success probability p """
    type = type.lower()
    ans = 0
    if r < 0: 
        if type == 'gt' or type == 'greater_than' or type == 'ge' or type == 'greater_than_or_equal' or type == 'not_equal' or type == 'ne':
            return 1
        return 0
    if r > n:
        if type == 'lt' or type == 'less_than' or type == 'le' or type == 'less_than_or_equal' or type == 'not_equal' or type == 'ne':
            return 1
        return 0
    if p < 0 or p > 1:
        raise ValueError(f'p must be in range [0,1]')
    if type == 'equal' or type == 'eq':
        return C(n,r) * p**r * (1-p)**(n-r)
    elif type == 'less_than' or type == 'lt':
        for i in range(r):
            ans += C(n,i) * p**i * (1-p)**(n-i)
        return ans
    elif type == 'less_than_or_equal' or type == 'le':
        for i in range(r+1):
            ans += C(n,i) * p**i * (1-p)**(n-i)
        return ans
    elif type == 'greater_than' or type == 'gt': 
        for i in range(r+1,n+1):
            ans += C(n,i) * p**i * (1-p)**(n-i)
        return ans
    elif type == 'greater_than_or_equal' or type == 'ge':
        for i in range(r, n+1):
            ans += C(n,i) * p**i * (1-p)**(n-i)
        return ans
    elif type == 'not_equal' or type == 'ne':
        return 1-(C(n,r) * p**r * (1-p)**(n-r))
