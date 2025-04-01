**Special Array I**
=
[Problem Link](https://leetcode.com/problems/special-array-i/description)

## Intuition
A very simple parity check problem.

## Approach
**Step-by-Step Process**

1. For each iteration, check if two adjacent numbers have same parity.
    - If same parity found, return `False`
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i+1] % 2:
                return False

        return True
```
