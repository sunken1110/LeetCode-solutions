**Number of Subsequences That Satisfy the Given Sum Condition**
=
[Problem Link](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description)

## Intuition
Our goal is to narrow the range until the sum of the minimum and the maximum is bounded by the target value. 
Then we can use two-pointer after sorting, if the sum exceeds the tagret then decrease the right, if not then 
increase the left. If a proper range is fixed, then the number of subsequences can be computed by the power of 2.

## Approach
**Step-by-Step Process**

1. Sort `nums`.

2. Approach by two-pointer `l` and `r`.
    - Until the sum of minimum and maximum is less than or equal to `target`, narrow the range.
  
3. If `r` is fixed, then count the number of subsequences in the range of `[l, r]`.
    - Repeat until `l` meets to `r`.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        l = 0
        r = n-1
        cnt = 0
        nums.sort()

        while l <= r:
            if nums[l] + nums[r] <= target:
                cnt += pow(2, r-l, mod)
                l += 1

            else:
                r -= 1

        return cnt % mod
```
