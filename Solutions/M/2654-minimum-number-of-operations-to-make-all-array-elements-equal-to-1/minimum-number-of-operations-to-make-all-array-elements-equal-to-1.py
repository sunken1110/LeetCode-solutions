#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description

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
