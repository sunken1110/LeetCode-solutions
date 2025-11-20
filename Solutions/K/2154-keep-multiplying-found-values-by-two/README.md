**Keep Multiplying Found Values by Two**
=
[Problem Link](https://leetcode.com/problems/keep-multiplying-found-values-by-two/description)

## Intuition
Simply check a double of `original` is already in `nums`. Use `set` for an efficient search.

## Approach
**Step-by-Step Process**

1. Convert `nums` to `set` type.

2. Double `original` until it is in `nums`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)

        while original in nums:
            original *= 2

        return original
```
