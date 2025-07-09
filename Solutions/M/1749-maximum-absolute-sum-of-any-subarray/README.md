**Maximum Absolute Sum of Any Subarray**
=
[Problem Link](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description)

## Intuition
The key idea is that the maximum subarray sum can be obtained by subtracting minimum prefix sum from the maximum 
prefix sum. Since our goal is to find a maximum absolute value, the order doesn't affect to the answer.

## Approach
**Step-by-Step Process**

1. Compute partial sum `sums` of `nums` with `accumulate`.

2. Return `max(sums)` - `min(sums)`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution1:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sums = list(accumulate(nums, initial=0))

        return max(sums) - min(sums)


# Time Complexity O(n), Space Complexity O(n)
class Solution2:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxSub = -inf
        minSub = inf
        
        sumSub = 0
        for i in range(n):
            sumSub = max(0, sumSub + nums[i])
            maxSub = max(maxSub, sumSub)

        sumSub = 0
        for i in range(n-1, -1, -1):
            sumSub = min(0, sumSub + nums[i])
            minSub = min(minSub, sumSub)

        return max(abs(maxSub), abs(minSub))
```
