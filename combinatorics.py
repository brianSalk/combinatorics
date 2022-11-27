"""A simple python library for combinatorics

counting functions:
fact(n) - factorial of n
C(n,r)- number of ways one could choose r items from n distinct items
P(n,r)- number of permutations of length r from n distinct items
permutations_with_nondistinct(n,*args) - number of permutation
    that can be created from len(args) groups of identical items each 
    of len(args[i])

"""

def fact(n):
    ans = 1
    for i in range(2,n+1):
        ans *= i
    return ans
def C(n,r):
    if n < 0:
        return C(-n+r-1,r) * (-1)**r
    return P(n,r) // fact(r)
def P(n,r):
    ans = 1
    for i in range(n-r+1, n+1):
        ans*=i
    return ans
def permutations_with_nondistinct(n,*args):
    den = 1
    for k in args:
        den *= fact(k)
    return fact(n) // den
def multinomial_coefficient(*args):
    num = fact(args[0])
    den = 1
    for each in args[1:]:
        den *= fact(each)
    return num//den

def stirling1(n,m):
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
    ans = 0
    for i in range(k+1):
        ans += (-1)**i * C(k,i) * (k-i)**n
    return ans // fact(k)
def stars_bars(n,k):
    """stars_bars(n,k) === C(n+k-1, k-1)
Where n is the number of identical items and k is tne number of buckets to place them in"""
    return C(n + k-1, k-1)
def multinomial_coefficient_with_unlabeled_groups(n,*args):
    return multinomial_coefficient(n,*args) // fact(len(args))
def binomial_theorem(a,b,n):
    ans = 0
    for i in range(n+1):
        ans += C(n,i) * a**(n-i) * b**(i)
    return ans
"""
Catalin number:
"""
def catalin(n):
    return (1/(n+1))*C(2*n,n)
