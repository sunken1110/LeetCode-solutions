**Largest Divisible Subset**
=
[Problem Link](https://leetcode.com/problems/largest-divisible-subset/description)

## Intuition
We apply dynamic programming with storing divisible integers. For an easy comparison, we first sort `nums` and 
set `dp` as `num` in `nums`. Then add divisible integers to each array and compare the maximum length. Note that 
if `nums[i] % nums[j] == 0`, then the number of integers in `dp[j]` should be large at least more than 2; if not, 
`dp[j] + nums[i]` cannot exceed a dominant `dp[i]`.

## Approach
**Step-by-Step Process**

1. Sort `nums`.

2. Initialize DP as `num` in `nums`.

3. For each index `i`, visit every smaller index `j` and check `nums[j]` is divisible by `nums[i]`.
    - If so, then compare the length of current divisible subset of `nums[i]` and `nums[j]`.
  
4. After finishing adjust `dp`, return the maximum length of `dp`.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]

        return max(dp, key=len)
```
