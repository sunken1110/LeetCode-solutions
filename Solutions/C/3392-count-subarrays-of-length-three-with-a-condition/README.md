**Count Subarrays of Length Three With a Condition**
=
[Problem Link](https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description)

## Intuition
A naive brute-force approach is enough.

## Approach
**Step-by-Step Process**

1. Check every triplet `nums[i]`, `nums[i+1]` and `nums[i+2]` in one pass.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cnt = 0

        for i in range(len(nums)-2):
            if 2*(nums[i]+nums[i+2]) == nums[i+1]:
                cnt += 1
            
        return cnt
