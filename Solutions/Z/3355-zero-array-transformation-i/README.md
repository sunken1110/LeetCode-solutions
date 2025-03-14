**Zero Array Transformation I**
=
[Problem Link](https://leetcode.com/problems/zero-array-transformation-i/description)

## Intuition
We decrement every value of selected indices, not just 1. Then it is enough to check that the decrement amount is larger thatn 
`nums[i]` for all i. To efficiently do a task, We use a prefix sum. 

## Approach
**Step-by-Step Process**

1. Define a prefix sum array `pref`.

2. For all queries in `queries`, cummulatively sum up the maximal decrement amount to `psum`.

3. If `nums[i] > psum` for at least one `i`, then the zero array transformation cannot be completed so return `False`.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        pref = [0] * (n+1)
        psum = 0

        for l, r in queries:
            pref[l] += 1
            pref[r+1] -= 1

        for i in range(n):
            psum += pref[i]

            if nums[i] > psum:
                return False

        return True
```
