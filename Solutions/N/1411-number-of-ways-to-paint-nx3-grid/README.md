**Number of Ways to Paint N x 3 Grid**
=
[Problem Link](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description)

## Intuition
For each 1 x 3 grid, note that there are exactly 2 types namely `aba` type and `abc` type where `a, b, c` are 3 colors. 
For the case of `aba` type, the available following grids are `bab`, `bac`, `bcb`, `cab`, `cac`. This again generates 
three `aba` types and two `abc` types. For the case of `abc` type, the available following grids are `bab`, `bca`, 
`bcb`, `cab`. This type again generates two `aba` types and two `abc` types. Then, for each next step, we can compute the 
possibilities of `aba` and `abc` types respectively with a linear transformation `T = [[3, 2], [2, 2]]`. Now the task 
became a matrix exponentation by `n`.

## Approach
**Step-by-Step Process**

1. Count the intial cases of `aba` and `abc` types, respectively.

2. Repeat a linear transformation until `n`th operation.

3. Sum up the total cases of `aba` and `abc` types of `n`th step.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numOfWays(self, n: int) -> int:
        aba = 6
        abc = 6
        mod = 10**9 + 7

        for _ in range(n-1):
            aba, abc = (3*aba + 2*abc) % mod, (2*aba + 2*abc) % mod

        return (aba+abc) % mod
```
