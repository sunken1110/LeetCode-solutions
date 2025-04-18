**Count Equal and Divisible Pairs in an Array**
=
[Problem Link](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description)

## Intuition
A simple double loops solve the problem.

## Approach
**Step-by-Step Process**

1. Construct 2 loops and check the condition.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0

        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    cnt += 1

        return cnt
