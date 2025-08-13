**Soup Servings**
=
[Problem Link](https://leetcode.com/problems/soup-servings/description)

## Intuition
As `n` gets large, the answer converges to 1. We can set this threshold as 5000 (in this solution, 4800). 
Let `a`, `b` be amount of soup A, soup B, respectively. There are totally 4 chances of operation of same 
probabilities; `(a-100, b)`, `(a-75, b-25)`, `(a-50, b-50)`, and `(a-25, b-75)`. We use DFS until at least 
one of `a` and `b` reaches zero.

## Approach
**Step-by-Step Process**

1. Set the threshold of `n`.

2. Define DFS and get the probability of equivalent 4 cases.
    - If at least one of `a` and `b` reaches 0, return the probability.
  
## Solutions
```python
# Time Complexity O(t/25 * t/25), Space Complexity O(t/25 * t/25)
# where t is a threshold
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
        
        @lru_cache(None)
        def f(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (f(a-100, b) + f(a-75,  b-25) + f(a-50,  b-50) + f(a-25,  b-75))

        return f(n, n)
```
