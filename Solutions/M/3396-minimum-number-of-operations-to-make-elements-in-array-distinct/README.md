**Minimum Number of Operations to Make Elements in Array Distinct**
=
[Problem Link](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description)

## Intuition
Since an operation allows to remove **first** 3 elements, if the result array is distinct then these elements are 
located in the end of `nums`. The idea is to visit elements in reverse order and store newly found integer, and if 
we meet already visited integer then remove all of the remained part.

## Approach
**Step-by-Step Process**

1. Initialize the visited integer `check = set()`.
  
2. In reverse order, traverse `nums`.
    - In each step, add newly found integer to `check`.
    - If already exists in `check`, then return the number of operations based on the index.
  
## Solutions
```python
# Time Complexity O(n), Space Complexityt O(n)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        check = set()

        for i in range(n-1, -1, -1):
            if nums[i] in check:
                return i//3 + 1

            check.add(nums[i])

        return 0
```
