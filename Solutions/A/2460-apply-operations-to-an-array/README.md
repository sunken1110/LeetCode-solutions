**Apply Operations to an Array**
=
[Problem Link](https://leetcode.com/problems/apply-operations-to-an-array/description)

## Intuition
Naive approach is enough. Scan `nums`, find indices that operation condition holds, then rearrange indices.

## Approach
**Step-by-Step Process**

1. As a first loop, find indicies that `nums[i] == nums[i+1]` and do an operation at `i`.

2. As a second loop, rearrange `nums` with indices that operation processed.
    - In this step, the result only reflects nonzero elements.

3. Fill remained indices of `nums` with zeroes. 
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        if len(nums1) % 2 != 0:
            for num in nums2:
                ans ^= num

        if len(nums2) % 2 != 0:
            for num in nums1:
                ans ^= num

        return ans
```
