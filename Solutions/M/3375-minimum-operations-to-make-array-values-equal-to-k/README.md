**Minimum Operations to Make Array Values Equal to K**
=
[Problem Link](https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description)

## Intuition
In short, the operation is to remove the maximum of `nums` and to replace it to the integer equal to or 
larger than the second maximum value of `nums`. To minimize the number of operations, we can consider the operation 
replacing the value to the second maximum value. Now, to make `nums` identical to `k`, there should be no integer 
smaller than `k`. 

## Approach
**Step-by-Step Process**

1. To extract unique values of `nums`, change the type to set.
  
2. According to the relation between `k` and `min(nums)`, return the answer.
    - To accomplish the task, `k` must be larger than the minimum value of `nums`.
    - Elif `k` is in `nums`, then `len(nums) - 1` operations needed.
    - If `k` is strictly smaller than the minimum value of `nums`, additional 1 operation required.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        if k > min(nums):
            return -1

        elif k == min(nums):
            return len(nums) - 1

        else:
            return len(nums)
```
