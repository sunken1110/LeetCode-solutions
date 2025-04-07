**Partition Labels**
=
[Problem Link](https://leetcode.com/problems/partition-equal-subset-sum/description)

## Intuition
Backtracking is also possible, but may trigger time limit error if the stack is very deep. Then we can use 
dynamic programming to efficiently track possible subset sum. Since the partition can be divided by 2, first check if 
the total sum is even. Then construct `dp` wih maximum index `sum(nums) // 2` and store every possible subset sum.

## Approach
**Step-by-Step Process**

1. Check the quotient and the remainder of `sum(nums)` divided by 2, namely `q` and `r`, respectively.
    - If `r == 1`, then return `False`.
  
2. Initialize DP array with maximum index `q+1`.

3. Track every possible subset sum if `dp[q]` is `True`, and conclude by `dp[0]`.


## Solutions
```python
# Time Complexity O(n*sum(nums)), Space Complexity O(sum(nums))
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        q, r = sum(nums) // 2, sum(nums) % 2

        if r == 1:
            return False

        dp = [False] * (q+1)
        dp[q] = True

        for num in nums:
            for i in range(q-num+1):
                dp[i] = dp[i] or dp[i+num]

        return dp[0]
