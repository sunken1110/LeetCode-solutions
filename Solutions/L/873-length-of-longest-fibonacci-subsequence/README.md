**Length of Longest Fibonacci Subsequence**
=
[Problem Link](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description)

## Intuition
Due to the Fibonacci-like condition, if two elements are chosen then the other element will also be fixed. 
Then we can apply a 2D dynamic programming of larger elements.   

## Approach
**Step-by-Step Process**

1. Set a 2D dynamic programming list `dp`. We want to find a Fibonacci-like series `f0 = f2 - f1`.

2. For `f1`, take any larger `f2`.

3. Check if `arr` contains `f2-f1`.
    - To update `dp`, we need an auxiliary dictionary `val2idx` which returns an index of value in `arr`.
    - If `f2-f1 >= f1`, there is no Fibonacci-like integer.

4. If such `f0 = f2-f1` exists in `arr`, then the length of Fibonacci-like subsequence increases by 1.
    - In the sense of `dp`, `dp[i1][i2]` has 1 more element than `dp[i0][i1]` which is already a Fibonacci-like subsequence.
  
## Solutions
```python
# Complexity O(n^2)
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        val2idx = {}
        ans = 0

        for idx, val in enumerate(arr):
            val2idx[val] = idx

        for i1 in range(1, n-1):
            f1 = arr[i1]

            for i2 in range(i1+1, n):
                f2 = arr[i2]
                f0 = f2 - f1

                if f0 >= f1:
                    break

                if f0 in val2idx:
                    i0 = val2idx[f0]
                    dp[i1][i2] = dp[i0][i1] + 1

                ans = max(ans, dp[i1][i2])

        return ans + 2 if ans > 0 else 0
```
