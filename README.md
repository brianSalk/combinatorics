# combinatorics
A python library of various useful combinatorics functions and classes.
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
