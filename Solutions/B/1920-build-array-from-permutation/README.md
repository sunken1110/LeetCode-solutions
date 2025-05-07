**Build Array From Permutation**
=
[Problem Link](https://leetcode.com/problems/build-array-from-permutation/description)

## Intuition
Implement as written in the problem.

## Approach
**Step-by-Step Process**

1. Initialize `ans = list()`.

2. In one pass, append `nums[nums[i]]` to `ans`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            ans.append(nums[nums[i]])

        return ans
```
