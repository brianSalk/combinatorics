"""A simple python library consisting of combinatorics functions

These functions are some of the most common functions used in combinatorics.
They are not intended to be extreemly performant but they should be accurate.
"""
def P(n,r):
    """P(n,r): where n and r are both positive
    calculate the number of permutations that can be created of length r
    given n distinct elements"""
    if n < 0 or r < 0:
        raise ValueError(f'n and r must be non-negative')
    ans = 1
    for i in range(n-r+1, n+1):
        ans*=i
    return ans


def C(n,r):
    """C(n,r): where n may be positive or negative and r is non-negative
    counts the number of combinations that can be created by choosing r 
    from n distinct elements"""
    if r < 0:
        raise ValueError("r must be non-negative")
    if n < 0:
        return C(-n+r-1,r) * (-1)**r
    return P(n,r) // fact(r)


def fact(n):
    """fact(n): where n is a positive integer of a number.
    used to calculate a factorial"""
    return P(n,n)


def multinomial(n,*args):
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

def stirling1(n,k):
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
    if n < 0:
        raise ValueError('n must be non-negative')
    ans = 0
    for k in range(1,n+1):
        ans += stirling2(n,k)
    return ans if ans != 0 else 1

def binomial_theorem(a,b,n):
    """binomial_theorem(a,b,n)"""
    ans = 0
    for i in range(n+1):
        ans += C(n,i) * a**(n-i) * b**(i)
    return ans
    
def stars_bars(n,k):
    """stars_bars(n,k) == C(n+k-1, k-1)
Where n is the number of identical items and k is tne number of buckets to place them in"""
    return C(n + k-1, k-1)


def catalan(n):
    """catalin(n): where n is non-negative

    calculates the nth catalan number.
    catalan numbers appear in many counting problems including Dyck words of length 2n and number of structurally unique BSTs of size n"""
    return fact(2*n) // (fact(n+1)*fact(n))


def paths_in_matrix(m,n):
    """paths_in_matrix(m,n)

    calculates the number of shortest paths from one corner to
    the other in a mXn matrix"""
    return C(n+m-2, n-1)


def pbinom(n,r,p=.5):
    """probability of getting r successes in n attempts with success probability p """
    if p < 0 or p > 1:
        raise ValueError(f'p must be in range [0,1]')
    return C(n,r) * p**r * (1-p)**(n-r)

