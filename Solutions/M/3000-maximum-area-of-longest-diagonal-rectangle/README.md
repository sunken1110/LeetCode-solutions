**Maximum Area of Longest Diagonal Rectangle**
=
[Problem Link](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description)

## Intuition


## Approach
**Step-by-Step Process**

1. 

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
