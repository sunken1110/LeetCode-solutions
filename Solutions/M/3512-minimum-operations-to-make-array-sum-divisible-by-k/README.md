**Minimum Operations to Make Array Sum Divisible by K**
=
[Problem Link](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description)

## Intuition
Index `i` of applying operations doesn't matter here. Simply sum up every `num` in `nums`, and calculate the 
remainder of dividing by `k`. Apply that remainder times operations to any one of `num`.

## Approach
**Step-by-Step Process**

1. Compute `sum(nums) % k`, and then return.
  
## Solutions
```python
# Time Complexity O(n), Space Complexityt O(1)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
```
