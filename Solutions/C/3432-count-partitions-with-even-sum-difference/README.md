**Count Partitions with Even Sum Difference**
=
[Problem Link](https://leetcode.com/problems/count-partitions-with-even-sum-difference/description)

## Intuition
To make the difference of two partitions even, two cases are possible; both are even or both are odd. 
Then clearly the total sum of `nums` should be even. Moreover, any two partitions must have same parity, i.e., 
if `sum(nums)` is even then every pairs are valid.

## Approach
**Step-by-Step Process**

1. Check `sum(nums)`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0
