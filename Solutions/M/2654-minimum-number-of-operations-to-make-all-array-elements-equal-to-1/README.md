**Minimum Number of Operations to Make All Array Elements Equal to 1**
=
[Problem Link](https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description)

## Intuition
The key idea is to make `1` as fast as possible. If a gcd of two adjacent elements is `1`, then we can broad 
additional operations from here since a gcd of any integer and `1` is always `1`. We first check if there 
already exist any `1` or all of the elements are not coprime each other to avoid redundant computation. 
With sliding window technique, find the minimum size of window that generates `1`.

## Approach
**Step-by-Step Process**

1. At the first scan, check if `1` already exists or no coprime relation is found.

2. For each length of window, check if `1` can be generated.
    - If so, then update the minimum length of such window `len_coprime`.
    - The number operations are clearly `len_coprime - 1`.
  
3. Return the number of total computations.
    - A specific element became `1` at step 3. To make remainder as `1`, extra `n-1` operations are needed.

## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        g = 0
        ones = 0
        len_coprime = n

        for num in nums:
            if num == 1:
                ones += 1

            g = gcd(g, num)

        if ones > 0:
            return n - ones

        elif g > 1:
            return -1

        for i in range(n):
            g = 0

            for j in range(i, n):
                g = gcd(g, nums[j])

                if g == 1:
                    len_coprime = min(len_coprime, j-i+1)
                    break

        return len_coprime + n - 2
```
