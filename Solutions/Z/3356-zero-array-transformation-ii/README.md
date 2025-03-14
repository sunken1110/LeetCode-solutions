**Zero Array Transformation II**
=
[Problem Link](https://leetcode.com/problems/zero-array-transformation-ii/description)

## Intuition
This is an application of [Problem Link](https://leetcode.com/problems/zero-array-transformation-i/description). 

We first check that the zero array transformation is possible with exactly same approach of above problem. If possible, 
then do a binary search to find a minumum `k`.

## Approach
**Step-by-Step Process**

1. Define `isPossible` which checks the possibility of zero array transformation with a sequence of length `idx`.

2. If not possible, then return -1.

3. Else, do a binary search until find a minimum length of sequence.
  
## Solutions
```python
# Complexity O(n*log(n))
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)


        def isPossible(idx):
            pref = [0] * (n+1)

            for q in queries[:idx]:
                l, r, val = q
                pref[l] += val
                pref[r+1] -= val

            psum = 0
            for i in range(n):
                psum += pref[i]
                
                if nums[i] > psum:
                    return False

            return True

        if not isPossible(m):
            return -1

        left, right = 0, m
        while left < right:
            mid = (left + right) // 2

            if isPossible(mid):
                right = mid

            else:
                left = mid + 1

        return right
```
