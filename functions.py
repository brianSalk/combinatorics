"""A simple python library consisting of combinatorics functions

These functions are some of the most common functions used in combinatorics.
They are not intended to be extreemly performant but they should be accurate.
"""
import typing
from typing import Literal


def P(n: int, r: int) -> int:
    """
    n permutation r
    
    counts the number of ways to arrange r elements from a set of n distinct elements

    args:
    n: number of elements in set
    r: number of elements in permutation
    """
    if n < 0 or r < 0:
        raise ValueError(f"n and r must be non-negative")
    ans = 1
    for i in range(n - r + 1, n + 1):
        ans *= i
    return ans


def C(n: int, r: int) -> int:
    """
    n choose r

    counts the number of ways to choose r elements from a set of n distinct elements
    
    args:
    n: number of elements in set (must be non-negative)
    r: number of elements in combination (may be negative)
    """
    if r < 0:
        raise ValueError("r must be non-negative")
    if n < 0:
        return C(-n + r - 1, r) * (-1) ** r
    return P(n, r) // fact(r)


def fact(n: int) -> int:
    """
    calculates the factorial of n, n!

    args:
    n: number to calculate factorial of (must be non-negative)
    """
    return P(n, n)


def multinomial(n: int, *args: int) -> int:
    """
    multinomial coefficient: calculates the number of distinct ways to arange n elements where each value in args is a group of identical elements
   
    args:
    n: number of elements to arrange (must be non-negative)
    args: array storing size of groups of identical elements (must be non-negative)

    """
    if n < 0 or any(each < 0 for each in args):
        raise ValueError("all arguments must be non-negative")
    if sum(args) > n:
        raise ValueError("sum of args must not exceed n")
    den = 1
    for k in args:
        den *= fact(k)
    return fact(n) // den


def stirling1(n: int, k: int) -> int:
    """
    Stirling cycle number or Stirling number of the first kind: counts # of ways to arrange n distinct elements into k distinct cycles

    args:
    n: number of elements to arrange (must be non-negative)
    k: number of cycles (must be non-negative)

    Example: stirling1(3,2) == 3 
    for example.  If you have 6 people and 3 three tables,
    there are sterling1(6,3) unique ways for them to be seated assuming
    that all tables are identical, every table has at least 1 person sitting at it, and that we do not want to count rotations or reflections"""
    if n < 0:
        raise ValueError("n must be positive")
    if k > n:
        raise ValueError("k must be in the range [0,n]")
    if n == k == 0:
        return 0

    def __S1(n, k):
        if n == k == 0:
            return 1
        elif n == 0 or k == 0:
            return 0
        return -(n - 1) * __S1(n - 1, k) + __S1(n - 1, k - 1)

    ans = __S1(n, k)
    return ans if ans >= 0 else -ans


def stirling2(n: int, k: int) -> int:
    """
    Stirling partition number or stirling number of the second kind:
    counts # of ways to partition n distinct elements into k non-empty groups

    args:
    n: number of elements to partition (must be non-negative)
    k: number of groups (must be non-negative)

    Example: stirling2(3,2) == 3
    If we have 3 unique people and 2 teams to put them on, 
    there are stirling2(3,2) unique ways to put them on teams
    """
    ans = 0
    for i in range(k + 1):
        ans += (-1) ** i * C(k, i) * (k - i) ** n
    return ans // fact(k)


def bell(n: int) -> int:
    """
    Bell number: counts the number of ways to partition a set of size n into subsets

    args:
    n: number of elements to partition (must be non-negative)

    calculates the number of nonempty subsets a set of size 'n' can
    be partitioned into"""
    if n < 0:
        raise ValueError("n must be non-negative")
    ans = 0
    for k in range(1, n + 1):
        ans += stirling2(n, k)
    return ans if ans != 0 else 1


def ordered_bell(n: int) -> int:
    """
    Ordered Bell number: counts the number of ways to partition a set of size n into weakly ordered subsets

    args:
    n: number of elements to partition (must be non-negative)

    counts the number of permutations of non-empty sets that a set of size 'n' can be partitioned into"""
    if n < 0:
        raise ValueError("n must be non-negative")
    ans = 0
    for k in range(1, n + 1):
        ans += fact(k) * stirling2(n, k)
    return ans if ans != 0 else 1


# should i just delete this?
def binomial_theorem(a, b, n) -> int:
    """
    binomial_theorem(a,b,n)
    (a+b)**n
    """
    ans = 0
    for i in range(n + 1):
        ans += C(n, i) * a ** (n - i) * b ** (i)
    return ans


def stars_bars(n: int, k: int) -> int:
    """
    stars_bars aka. multi-choose equal to C(n+k-1,k-1)
    
    args:
    n: number of identical items
    k: number of buckets to place them in

    Where n is the number of identical items and k is tne number of buckets to place them in
    """
    return C(n + k - 1, k - 1)


def catalan(n: int) -> int:
    """
    catalan number C(n) = (2n)!/(n+1)!n!

    args:
    n: number of elements to partition (must be non-negative)

    calculates the nth catalan number.
    catalan numbers appear in many counting problems including Dyck words of length 2n and number of structurally unique BSTs of size n"""
    return fact(2 * n) // (fact(n + 1) * fact(n))


def paths_in_matrix(m: int, n: int) -> int:
    """
    number of paths from one corner to the other in a mXn matrix
    
    args:
    m: number of rows in matrix
    n: number of columns number of columns in matrix

    calculates the number of shortest paths from one corner to
    the other in a mXn matrix
    """
    return C(n + m - 2, n - 1)


def pbinom(n: int, r: int, p: float = 0.5, 
           type: Literal["gt", "ge", "eq", "ne", "lt", "le"] = "eq") -> float:
    """probability of getting r successes in n attempts with success probability p

    args:
    n: number of trials
    r: number of successes 
    p: probability of success
    type: type of probability to calculate, must be one of ["gt", "ge", "eq", "ne", "lt", "le"]
    """
    type = type.lower()
    ans = 0
    if r < 0:
        if (
            type == "gt"
            or type == "greater_than"
            or type == "ge"
            or type == "greater_than_or_equal"
            or type == "not_equal"
            or type == "ne"
        ):
            return 1
        return 0
    if r > n:
        if (
            type == "lt"
            or type == "less_than"
            or type == "le"
            or type == "less_than_or_equal"
            or type == "not_equal"
            or type == "ne"
        ):
            return 1
        return 0
    if p < 0 or p > 1:
        raise ValueError(f"p must be in range [0,1]")
    if type == "equal" or type == "eq":
        return C(n, r) * p**r * (1 - p) ** (n - r)
    elif type == "less_than" or type == "lt":
        for i in range(r):
            ans += C(n, i) * p**i * (1 - p) ** (n - i)
        return ans
    elif type == "less_than_or_equal" or type == "le":
        for i in range(r + 1):
            ans += C(n, i) * p**i * (1 - p) ** (n - i)
        return ans
    elif type == "greater_than" or type == "gt":
        for i in range(r + 1, n + 1):
            ans += C(n, i) * p**i * (1 - p) ** (n - i)
        return ans
    elif type == "greater_than_or_equal" or type == "ge":
        for i in range(r, n + 1):
            ans += C(n, i) * p**i * (1 - p) ** (n - i)
        return ans
    elif type == "not_equal" or type == "ne":
        return 1 - (C(n, r) * p**r * (1 - p) ** (n - r))
    else:
        raise ValueError(f"type must be one of ['gt', 'ge', 'eq', 'ne', 'lt', 'le']")


def derangments(n: int) -> int:
    """
    number of derangements of n elements

    args:
    n: number of elements to derange (must be non-negative)

    calculates the number of derangements of n elements
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n - 1) * (derangments(n - 1) + derangments(n - 2))
