**Domino and Tromino Tiling**
=
[Problem Link](https://leetcode.com/problems/domino-and-tromino-tiling/description)

## Intuition
The key idea is to count the number of sub-tiling which are exact rectangles. In other word, if we are tiling `n` 
tiles and trying to count the `k` sub-tiling, then we need to count `n-k` tiling which can not be divided by any 
vertical cut. Let `dp[n]` be the target, then `dp[n-1]` has 1 case with 1 vertical domino. `dp[n-2]` also has 1 case
with 2 horizontal dominoes. From `dp[n-3]` to `dp[0]`, there are 2 choices; one is upper tromino at left, lower 
tromino at right, and the internal is filled with zigzag vertical dominoes. The other is a reversed one. 
Then we can count the total number by dynamic programming with memoization.

## Approach
**Step-by-Step Process**

1. Construct a memoization `dp`.
    - Initialize `dp[0]`, `dp[1]`, and `dp[2]`.

2. From `n >= 3`, construct a recursive relation.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1

        elif n == 2:
            return 2

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        prev = dp[0]
        mod = 10**9 + 7

        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * prev) % mod
            prev += dp[i-2]

        return dp[n] % mod
```
