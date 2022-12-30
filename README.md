# combinatorics
A python library of various useful combinatorics functions and classes.
# FUNCTIONS
## fact
### fact(n): calculate factorial of n
```math
n!
```
## P
### P(n,r): count permutations of size r that can be made from n distinct items.
```math
\frac{n!}{(n-r)!}
```
## C
### C(n,r): count distinct combinations of size r that can be made from n distinct items.
```math
{n \choose r} = \frac{n!}{(n-r)!r!}
```
## multinomial
### multinomial(n,r1,r2,r3...): count number of distinct permutations of size n when each r is a group of 1 or more identical items
```math
{n \choose r_1 r_2 r_3...} = \frac{n!}{r_1! r_2! r_3!...}
```
## sterling1
### sterling1(n,r): count number of unique ways to arrange n distinct items in r non-empty cycles, excluding rotations and reflections.
```math
\left[ n \atop r \right]
```
## sterling2
### sterling2(n,r): count number of unique ways to partition n distinct items into r non-empty groups
```math
\left\{ n \atop r \right\}
```
## bell
### bell(n): count unique partitions of a set
```math
\sum_{k=1}^{n} \left\{ n \atop k \right\}
```
## stars_bars
### stars_bars(n,k): calculate groups of identical objects
```math
{ n + k - 1 \choose k-1 }
```
## binomial_theorem
### binomial_theorem(a,b,n): where a and b are any two terms that are added and n is the power term.
```math
(a+b)^n = \sum_{k=0}^{n} { n \choose k } a^{n-k} b^k
```
## catalan
### catalan(n) where n is any non-negative integer
```math
\dfrac{(2n)!}{(n+1)!n!}
```
# CLASSES
## triangle
### __init__(self): create new pascals triangle of size 0 (empty triangle)
### get(self,row,col): retrieve value at the specified row and col in pascal's triangle.
### print(self): print entire triangle up to the last row specified by use
### data(self): get raw array that stores triangle data
