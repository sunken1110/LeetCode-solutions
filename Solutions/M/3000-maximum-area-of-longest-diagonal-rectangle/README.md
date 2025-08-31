**Maximum Area of Longest Diagonal Rectangle**
=
[Problem Link](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description)

## Intuition
Simply track the diagonal of each rectangle in `dimensions`. If the current diagonal is equal to the previous 
maximum diagonal, then return the larger area.

## Approach
**Step-by-Step Process**

1. For each `length`, `width` in `dimensions`, compute the current diagonal.
    - For the simplicity, we only compute `curr_diag` = `length**2` + `width**2`.
  
2. Track `curr_diag` and return the area of maximal diagonal.
    - If `curr_diag` is strictly longer, then return the area `length * width`.
    - If `curr_diag` is equal to `max_diag`, then return the larger area.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        ans = 0

        for length, width in dimensions:
            curr_diag = length**2 + width**2

            if max_diag < curr_diag:
                max_diag = curr_diag
                ans = length * width

            elif max_diag == curr_diag:
                ans = max(ans, length*width)

        return ans
```
