**Maximum Unique Subarray Sum After Deletion**
=
[Problem Link](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description)

## Intuition
Clearly the maximum sum can be obtained if we only add positive integers. What we need is to scan every integer in 
`nums`, check if it is already added integer and if not, add to the sum. The edge case is an array with all negative 
integers; since a subarray cannot bt empty we return the maximum of it.

## Approach
**Step-by-Step Process**

1. Initialize `unique`.

2. Check every `num` in `nums`.
    - If `num` is not seen before, then add to `ans` and `unique`.
  
3. Return `ans`.
    - If `ans` is 0, which means no positive integer appeared, return the maximum negative integer in `nums`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexityt O(n)
class Solution:
    def maxSum(self, nums: List[int]) -> int:        
        unique = set()
        ans = 0

        for num in nums:
            if num > 0 and num not in unique:
                ans += num
                unique.add(num)

        return ans if ans != 0 else max(nums)
```
