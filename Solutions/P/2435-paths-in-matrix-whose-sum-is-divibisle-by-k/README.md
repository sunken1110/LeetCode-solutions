**Paths in Matrix Whose Sum Is Divisible by K**
=
[Problem Link](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description)

## Intuition
We use dynamic programming technique to store the number of paths that make cumulative modulo sum in the 
range `[0, k-1]`. That is, we need `m`*`n`*`k` size array where `m`*`n` is the size of `grid`. 

## Approach
**Step-by-Step Process**

1. Initialize `dp` as 3D `m`*`n`*`k` array.
    - The initial point `dp[0][0]` has modulo 0.
  
2. For each path, cumulatively add the number of modulo of previous paths `prev`.
    - For DOWN moving, `dp[i][j][curr] += dp[i-1][j][prev]`.
    - For RIGHT moving, `dp[i][j][curr] += dp[i][j-1][prev]`.

3. Return the total number of modulo 0 paths of `dp[m-1][n-1]`.

## Solutions
```python
# Time Complexity O(m*n*k), Space Complexity O(m*n*k)
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0] * k for j in range(n)] for i in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        mod = 10**9 + 7

        for i in range(m):
            for j in range(n):
                for prev in range(k):
                    curr = (prev + grid[i][j]) % k

                    if i > 0:
                        dp[i][j][curr] += dp[i-1][j][prev]

                    if j > 0:
                        dp[i][j][curr] += dp[i][j-1][prev]

                    dp[i][j][curr] %= mod

        return dp[m-1][n-1][0]
