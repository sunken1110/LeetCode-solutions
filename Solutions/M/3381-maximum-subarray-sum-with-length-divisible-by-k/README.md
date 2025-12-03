**Maximum Subarray Sum With Length Divisible by K**
=
[Problem Link](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description)

## Intuition
Let `pref` be a prefix sum, then `pref_(idx+k)` - `pref_idx` is the sum of one of length `k` subarray. 
To maximize the value, we need to find `i`, `j` which maximize `pref_(idx+i*k)` and minimize `pref_(idx+j*k)`. 
To easily do this job, we store the minimum prefix sum of each modulo `k` in `dp` of size `k`. 
Update `pref` and `dp` simultaneously, and track the maximum subarray sum.

## Approach
**Step-by-Step Process**

1. Initialize `pref` and size-`k` array `dp`.
    - `dp[i]` refers a minimum prefix sum of length `i` modulo `k`.
    - Since the first `k`-divisible length subarray occurs at `dp[k]`, initialize `dp[k]` as 0.

2. For each `num` in `nums`, update each values.
    - Add `num` to `pref`.
    - Compute `pref` - `dp[idx%k]` to update maximum subarray sum.
    - If current `pref` is much smaller than `dp[idx%k]`, update it.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = 0
        dp = [inf] * (k-1) + [0]
        ans = -inf

        for idx, num in enumerate(nums):
            pref += num
            ans = max(ans, pref - dp[idx%k])
            dp[idx%k] = min(pref, dp[idx%k])

        return ans
```
