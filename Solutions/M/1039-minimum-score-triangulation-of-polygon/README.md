**Minimum Score Triangulation of Polygon**
=
[Problem Link](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description)

## Intuition
Suppose we fixed two vertices `i`, `j`. If we choose the in-between vertex `k` and triangulize, then the original 
polygon divides into several smaller polygons. That is, divide-and-conquer approach is valid. As a bottom-up approach, 
if `dp[i][j]` is a minimum score of triangles `(i, k, j)`, then the score can be formulated as the sum of 
`(i, k1, k)`, `(i, k, j)`, and `(k, k2, j)`. 

## Approach
**Step-by-Step Process**

1. Initialize `dp`, where `dp[i][j]` is the minimum score of triangle `(i, k, j)` with some in-between vertex `k`.

2. Construct a divide-and-conquer structure.
    - To choose two side vertices, 2 loops `i` and `j` are needed.
    - If two vertices are fixed, again make a loop `k` for the in-between vertex.
    - For fixed `k` the original polygon is divided into 3 partitions.
    - Each has score `dp[i][k]`, `dp[k][j]` and `values[i]*values[j]*values[k]`, respectively.
  
## Solutions
```python
# Time Complexity O(n^3), Space Complexity O(n^2)
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j] if dp[i][j] != 0 else inf,
                             dp[i][k] + dp[k][j] + values[i]*values[j]*values[k])

        return dp[0][n-1]
```
