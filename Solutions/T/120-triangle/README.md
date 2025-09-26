**Triangle**
=
[Problem Link](https://leetcode.com/problems/triangle/description)

## Intuition
Dynamic programming is an appropriate approach. For each `i`th row, add the minimum value between two adjacent numbers 
of `i+1`th row.

## Approach
**Step-by-Step Process**

1. Initialize `dp`.

2. Start from the bottom row, or each `i`th row, add the minimum value between two adjacent numbers of `i+1`th row.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]

        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

        return dp[0]
```
