**Ones and Zeroes**
=
[Problem Link](https://leetcode.com/problems/ones-and-zeroes/description)

## Intuition
It's a kanpsack problem. Construct 2D dp array and fill `dp[i][j]` as a maximum number of strings with `i` zeroes 
and `j` zeroes.

## Approach
**Step-by-Step Process**

1. Initialize 2D array `dp`.

2. For each string `s` in `strs`, count zeroes and ones.

3. Fill `dp[i][j]` in reverse order.
    - Each iteration must not exceed `m` zeroes and `n` ones.
  
## Solutions
```python
# Time Complexity O(s*m*n), Space Complexity O(m*n)
class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n+1) for _ in range(m+1)]

        for s in strs:
            zeroes = s.count('0')
            ones = s.count('1')

            for i in range(m, zeroes-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeroes][j-ones] + 1)

        return dp[-1][-1]
```
