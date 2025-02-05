**Maximum Ascending Subarray Sum**
=
[Problem Link](https://leetcode.com/problems/maximum-ascending-subarray-sum/description)

## Intuition
During scanning each element of `nums`, we record a sum of each ascending subarray. Then we take the maximum value of them.

## Approach
**Step-by-Step Process**

1. Scan each element of `nums` and initiate `max_sum`.

2. Get a sum of subarray `curr_sum` until ascending condition holds.
    - If `nums[i-1] >= nums[i]`, then get a maximum value between `max_sum` and `curr_sum`.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curr_sum += nums[i]

            elif nums[i-1] >= nums[i]:
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]

        return max(max_sum, curr_sum)
```
