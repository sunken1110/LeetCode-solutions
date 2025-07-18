**Find the Maximum Length of Valid Subsequence II**
=
[Problem Link](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description)

## Intuition
This problem is a generalization of the following:

[Problem Link](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description)

Similarly, we know that the even-indexed elements have same modulo of `k` and so do odd-indexed elements. 
Then our task is to trace the counter of each modulos, so we use 2-D DP technique. For `num` in `nums`, if a previous 
modulo is `mod` then we need to take the counter of previous `num` ends by `mod`. In other word, DP refers to 
all possible states that could result in this state, that is, 
`dp[num][mod]` = `dp[mod][num] + 1` for every possible `mod`.

## Approach
**Step-by-Step Process**

1. Initialize 2-D DP array `dp`.

2. For each `mod` in modulo `k`, construct `dp`.

3. For each maximum length of valid subsequence ends with `mod`, return the maximum.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(k^2)
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]

        for num in nums:
            num %= k

            for mod in range(k):
                dp[num][mod] = dp[mod][num] + 1

        return max(map(max, dp))
```
