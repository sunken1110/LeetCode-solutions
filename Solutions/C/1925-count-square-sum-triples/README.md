**Count Square Sum Triples**
=
[Problem Link](https://leetcode.com/problems/count-square-sum-triples/description)

## Intuition
Since the maximum value of `c` is `n`, we first make a set of squares `squares` to compare if the sum of 
two squares of integer `a`, `b` is also a square. Note that `a` and `b` can be swapped and there is no square 
of form `2*x^2`, we count the pair of `(a, b)` twice.

## Approach
**Step-by-Step Process**

1. Create a set of squares `squares`.

2. For each `(a, b)` pair less than or equal to `n`, check if `a**2` + `b**2` is in `squares.
    - If so, count twice.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def countTriples(self, n: int) -> int:
        squares = set([s*s for s in range(1, n+1)])
        cnt = 0

        for a in range(1, n+1):
            for b in range(a+1, n+1):
                if a**2 + b**2 in squares:
                    cnt += 2

        return cnt
