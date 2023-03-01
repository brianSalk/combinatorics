# combinatorics
A python library of various useful combinatorics functions and classes.
# FUNCTIONS
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
## fact
### fact(n): calculate factorial of n
```math
n!
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
## paths_in_matrix
### paths_In_matrix(m,n) where m and n are the heighta dn width of a matrix
```math
{n+m-2 \choose n-1} = {n+m-2 \choose m-1}
```
## pnorm
### pnorm(k,n,p) where n is the number of trials, k is the number of successes and p is the probability of success.
# CLASSES
## ptriangle
### \_\_init\_\_(self)
  create new pascals triangle of size 0 (empty triangle)
### get(self,row,col)
  retrieve value at the specified row and col in pascal's triangle.
### print(self) 
  print entire triangle up to the last row specified by use
### data(self)
  get 2D python list that stores triangle data
## btriangle
### \_\_init\_\_(self)
  create a new bells triangle of size 2 (two rows)
### get(self, row, col)
  retrieve value at the specified row and col in bell's triangle.
### print(self):
  print entire tree
### data(self):
  get list contining tree.
