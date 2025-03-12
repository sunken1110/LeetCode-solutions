**Maximum Count of Positive Integer and Negative Integer**
=
[Problem Link](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description)

## Intuition
Since `nums` are already sorted, we use binary search to solve the problem. With `left` and `right`, 
we set `mid = (left + right) // 2` and check the value of `nums[mid]`. Firstly we find the maximal 
index of negative value. Secondly check if there exists any zeroes. Finally find the 
minimal index of positive value.

## Approach
**Step-by-Step Process**

1. Initialize `left = 0` and `right = n-1`.

2. With `mid = (left + right) // 2`, find maximal index `left` of negative values by `nums[mid] < 0`.

3. If there exists any zeros in `nums`, then `nums[left+1] = 0`. Again find the maximal index of zeroes.
    - If not, then the rest of `nums` are eventually positive. Return the answer directly.

4. Conclude the minimal index of positive values.
  
## Solutions
```python
# Complexity O(log(n))
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1

            else:
                right = mid - 1

        if left < n and nums[left] > 0:
            return max(left, n - left)

        neg = left
        right = n-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == 0:
                left = mid + 1

            else:
                right = mid - 1

        return max(neg, n - left)
```
