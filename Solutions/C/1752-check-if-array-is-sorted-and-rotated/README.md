**Check if Array Is Sorted and Rotated**
=
[Problem Link](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description)

## Intuition
First, suppose `nums` is not rotated. Then `nums` is sorted in non-decreasing order if `nums[i] <= nums[i+1]` for all `i`.
In this case, note that `nums[n-1] > nums[0] = nums[((n-1) + 1) % n]` where `n = len(nums)`.
Now, if `nums` is originally sorted and rotated, then `nums` is equal to `nums[i:] + nums[:i]` for exactly one `i` with 
`nums[i-1] > nums[i]`. Therefore, it is enough to check that there is exactly 1 index such that `nums[i] > nums[i+1]`.

## Approach
**Step-by-Step Process**

1. To count the condition, we initialize `cnt`.

2. Iterate in range `len(nums)` to check how many times `nums[i] > nums[i+1]` occured.
    - To check the rotated condition, we use modulo which also can handle index continuity.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                cnt += 1
            if cnt > 1:
                return False

        return True
```
