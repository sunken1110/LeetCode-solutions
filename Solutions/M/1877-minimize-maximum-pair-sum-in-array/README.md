**Minimize Maximum Pair Sum in Array**
=
[Problem Link](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description)

## Intuition
Since we have to use every number in `nums` exactly once, the largest number must be a pair with the smallest 
number. Similarly, we can conlude that the `i`th largest number must be a pair with the `len(nums)-i`th 
smallest number.

## Approach
**Step-by-Step Process**

1. Sort `nums`.

2. Initialize a set `pairsum`.
    - Add `nums[i] + nums[n-i-1]`, which minimizes maximum pair sum in `nums`.
  
3. Return the maximum value of `pairsum`.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        pairsum = set()
        nums.sort()

        for i in range(n // 2):
            pairsum.add(nums[i] + nums[n-i-1])

        return max(pairsum)
```
