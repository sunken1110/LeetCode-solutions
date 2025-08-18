**New 21 Game**
=
[Problem Link](https://leetcode.com/problems/new-21-game/description)

## Intuition
Alice can draw a new number until she has less than `k` points. Suppose `dp[i]` be the probability of Alice gets 
exactly `i` point. If `i < k`, then the previous point is one of `i-1`, `i-2`, ..., `i-maxPts` and each provide 
same probabilities, i.e., `dp[i]` = `(dp[i-1] + ... + dp[i-maxPts]) / maxPts`. Since `dp[i]` requires previous 
`maxPts` sum, we use a 1-D DP array with sliding window technique.

## Approach
**Step-by-Step Process**

1. Initialize 1-D DP array `dp` which refers the probability of Alice gets exactly `i` point.

2. Compute `dp[i]` while constructing a sliding window sum `windowSum`.
    - If `i < k`, Alice still can draw a number so `windowSum += dp[i]`.
    - If `i >= maxPts`, remove the probability of leftmost window.

3. Total probability is the sum of `dp[i]` such that `k <= i <= n`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        windowSum = 1.0
        ans = 0.0

        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts

            if i < k:
                windowSum += dp[i]
            else:
                ans += dp[i]

            if i - maxPts >= 0:
                windowSum -= dp[i - maxPts]

        return ans
```
